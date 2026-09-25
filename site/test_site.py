"""Offline checks for the approved Root Sequence public seed."""
from __future__ import annotations

import base64
import hashlib
import importlib.util
import json
import re
import shutil
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse
from xml.etree import ElementTree as ET


HERE = Path(__file__).resolve().parent
LAST_APPROVED_PREVIEW_SHA256 = "08a1ce67f37f3db55e235cb3703bcdb552deead2ffd4aafd6cd732f69b384356"
spec = importlib.util.spec_from_file_location("site_builder", HERE / "build.py")
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.links: list[str] = []
        self.resources: list[str] = []
        self.scripts: list[dict] = []
        self._script: dict | None = None
        self.meta: dict[str, str | None] = {}
        self.h1 = 0

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        if tag == "h1":
            self.h1 += 1
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if tag in ("img", "script") and "src" in attrs:
            self.resources.append(attrs["src"])
        if tag == "link" and attrs.get("rel") not in ("canonical",):
            if "href" in attrs:
                self.resources.append(attrs["href"])
        if tag == "meta" and attrs.get("name"):
            self.meta[attrs["name"]] = attrs.get("content")
        if tag == "script":
            self._script = {"attrs": attrs, "text": ""}

    def handle_data(self, data):
        if self._script is not None:
            self._script["text"] += data

    def handle_endtag(self, tag):
        if tag == "script" and self._script is not None:
            self.scripts.append(self._script)
            self._script = None


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "source"
        self.root.mkdir()
        for name in builder.SOURCE_FILES:
            shutil.copy2(HERE / name, self.root / name)

    def build(self, release=False):
        output = Path(self.temp.name) / "output"
        return output, builder.build(self.root, output, release)

    def approve(self):
        approval = {
            "source_sha256": builder.source_digest(self.root),
            "approved_by": "test fixture only",
            "approved_at": "2026-09-18",
        }
        (self.root / "approval.json").write_text(json.dumps(approval), encoding="utf-8")

    def parse(self, path):
        parser = PageParser()
        parser.feed(path.read_text(encoding="utf-8"))
        return parser

    def test_review_candidate_differs_from_last_approved_preview(self):
        actual = hashlib.sha256((HERE / "index.html").read_bytes()).hexdigest()
        self.assertNotEqual(actual, LAST_APPROVED_PREVIEW_SHA256)

    def test_preview_build_preserves_the_review_html_exactly(self):
        output, manifest = self.build()
        self.assertEqual((output / "index.html").read_bytes(), (self.root / "index.html").read_bytes())
        self.assertEqual(manifest["build_mode"], "preview")
        self.assertEqual(self.parse(output / "index.html").meta["robots"], "noindex,nofollow")

    def test_release_needs_exact_approval(self):
        with self.assertRaisesRegex(ValueError, "Release blocked"):
            self.build(True)
        self.approve()
        (self.root / "index.html").write_text(
            (self.root / "index.html").read_text(encoding="utf-8") + "\n",
            encoding="utf-8",
        )
        with self.assertRaisesRegex(ValueError, "Release blocked"):
            self.build(True)

    def test_release_changes_only_publication_state(self):
        self.approve()
        output, manifest = self.build(True)
        text = (output / "index.html").read_text(encoding="utf-8")
        self.assertEqual(manifest["build_mode"], "release")
        self.assertEqual(self.parse(output / "index.html").meta["robots"], "index,follow")
        for phrase in ("local review copy", "Not a published site", "Privacy and this preview"):
            self.assertNotIn(phrase, text)
        self.assertIn("Public seed · Published 18 September 2026", text)
        self.assertIn("This is the public seed edition", text)

    def test_page_structure_and_fragments(self):
        output, _ = self.build()
        page = self.parse(output / "index.html")
        self.assertEqual(page.h1, 1)
        self.assertEqual(len(page.ids), len(set(page.ids)))
        self.assertIn("main", page.ids)
        for href in page.links:
            parsed = urlparse(href)
            if parsed.scheme:
                self.assertEqual(parsed.scheme, "https", href)
                continue
            self.assertFalse(parsed.netloc, href)
            self.assertFalse(parsed.path, href)
            if parsed.fragment:
                self.assertIn(unquote(parsed.fragment), page.ids, href)

    def test_page_is_self_contained_and_font_is_embedded(self):
        output, _ = self.build()
        text = (output / "index.html").read_text(encoding="utf-8")
        page = self.parse(output / "index.html")
        self.assertIn('@font-face{font-family:"Cascadia Mono RS";src:url(data:font/woff2;base64,', text)
        self.assertIn("connect-src 'none'", text)
        for resource in page.resources:
            self.assertTrue(resource.startswith("data:"), resource)

    def test_inline_script_hashes_match_the_csp(self):
        output, _ = self.build()
        text = (output / "index.html").read_text(encoding="utf-8")
        csp = re.search(r'<meta content="([^"]+)" http-equiv="Content-Security-Policy"/>', text).group(1)
        page = self.parse(output / "index.html")
        executable = [s for s in page.scripts if s["attrs"].get("type") != "application/json"]
        self.assertEqual(len(executable), 2)
        for script in executable:
            digest = base64.b64encode(hashlib.sha256(script["text"].encode()).digest()).decode()
            self.assertIn(f"'sha256-{digest}'", csp)

    def test_only_english_source_edition_is_offered(self):
        output, _ = self.build()
        page = self.parse(output / "index.html")
        translations = next(s for s in page.scripts if s["attrs"].get("id") == "translations")
        self.assertEqual(list(json.loads(translations["text"])), ["en"])
        text = (output / "index.html").read_text(encoding="utf-8")
        self.assertIn("English / source edition", text)
        self.assertNotIn("noonenoticed.world", text)

    def test_required_approved_copy_and_controls_are_present(self):
        text = (HERE / "index.html").read_text(encoding="utf-8")
        for phrase in (
            "Research for a",
            "more coherent world",
            "Root Sequence is an open transdisciplinary research and design project",
            "Root Sequence is a place for questions that cross fields",
            "Root Sequence is an independent project started by",
            "https://github.com/raelovejoy",
            "Why “Root Sequence”?",
            "What conditions made this possible, and what does it make possible next?",
            "https://github.com/Root-Sequence/root-sequence/blob/main/concepts/root-sequence.md",
            "Selected research and writing",
            "How Root Sequence researches",
            "Adaptive continuity and dynamic coherence",
            "Epistemic discoverability and knowledge routing",
            "Legible Systems",
            "Reading Trails",
            "https://github.com/Root-Sequence/root-sequence/blob/main/research/method-router.md",
            "Being Human(e): An Incomplete Guide",
            'id="project-humane"',
            "Its public website has not been built yet",
            "Take part in",
            "Cascadia Mono license",
        ):
            self.assertIn(phrase, text)
        for control in ("menu-sections", "menu-display", "menu-language", "context-dialog"):
            self.assertIn(f'id="{control}"', text)

    def test_generated_support_files_are_complete(self):
        output, manifest = self.build()
        self.assertEqual(ET.parse(output / "sitemap.xml").getroot()[0][0].text, builder.BASE_URL)
        self.assertEqual((output / "CNAME").read_text(), builder.DOMAIN + "\n")
        self.assertEqual((output / ".nojekyll").read_bytes(), b"")
        self.assertEqual(set(manifest["files"]), {"index.html", "robots.txt", "sitemap.xml", ".nojekyll", "CNAME"})

    def test_existing_output_is_not_overwritten(self):
        output, _ = self.build()
        marker = output / "reader-note.txt"
        marker.write_text("keep me")
        with self.assertRaisesRegex(ValueError, "empty output"):
            builder.build(self.root, output)
        self.assertEqual(marker.read_text(), "keep me")


if __name__ == "__main__":
    unittest.main(verbosity=2)
