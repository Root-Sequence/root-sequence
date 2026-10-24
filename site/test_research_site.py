"""Check the research export, its links, and its separate publication gate."""
from __future__ import annotations

import importlib.util
import json
import shutil
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("research_builder", HERE / "build_research.py")
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


class Links(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.urls = []
        self.ids = set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.ids.update([attrs["id"]] if "id" in attrs else [])
        self.urls.extend(attrs[key] for key in ("href", "src") if key in attrs)


class ResearchPublicationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name) / "repo"
        self.root = self.repo / "site"
        self.root.mkdir(parents=True)
        for name in (*builder.homepage.SOURCE_FILES, "approval.json", "build_research.py"):
            shutil.copy2(HERE / name, self.root / name)
        workflow = self.repo / ".github/workflows/pages.yml"
        workflow.parent.mkdir(parents=True)
        shutil.copy2(HERE.parent / ".github/workflows/pages.yml", workflow)
        self.source = self.repo / builder.INQUIRY
        shutil.copytree(HERE.parent / builder.INQUIRY, self.source)
        self.output = Path(self.temp.name) / "output"

    def approve_fixture(self):
        (self.root / builder.APPROVAL_FILE).write_text(json.dumps({
            "source_sha256": builder.source_digest(self.root),
            "canonical_url": builder.CANONICAL_URL,
            "approved_by": "test fixture only", "approved_at": "2026-10-24",
        }))

    def test_homepage_approval_does_not_approve_research(self):
        with self.assertRaisesRegex(ValueError, "Research release blocked"):
            builder.build(self.root, self.output, True)
        self.assertFalse(self.output.exists())

    def test_source_change_rejects_stale_research_approval(self):
        self.approve_fixture()
        path = self.source / "research/claims.csv"
        path.write_bytes(path.read_bytes() + b"\n")
        with self.assertRaisesRegex(ValueError, "Research release blocked"):
            builder.build(self.root, self.output, True)

    def test_approved_export_preserves_homepage_and_draft_qualifications(self):
        self.approve_fixture()
        manifest = builder.build(self.root, self.output, True)
        expected = builder.homepage.release_html((self.root / "index.html").read_text())
        self.assertEqual((self.output / "index.html").read_text(), expected)
        self.assertEqual(manifest["html_pages"], 8)
        for name in builder.EXPORTS:
            target = self.output / builder.ROUTE / name
            if name.endswith(".html"):
                text = target.read_text()
                self.assertIn('href="/">Root Sequence</a>', text)
                self.assertIn("AI-assisted draft, author and disciplinary review pending", text)
                self.assertIn('name="robots" content="index,follow"', text)
                self.assertNotIn('href="methods.md"', text)
            else:
                self.assertEqual(target.read_bytes(), (self.source / name).read_bytes())
        appraisal = (self.output / builder.ROUTE / "research/appraisal.html").read_text()
        self.assertNotIn("merge and deployment pending", appraisal)
        self.assertIn("scholarly and cultural review remain pending", appraisal)

    def test_preview_exports_only_allowlisted_files_and_local_links_resolve(self):
        (self.source / "unreviewed-private-note.txt").write_text("exclude this sentinel")
        builder.build(self.root, self.output)
        research = self.output / builder.ROUTE
        actual = {str(p.relative_to(research)) for p in research.rglob("*") if p.is_file()}
        self.assertEqual(actual, set(builder.EXPORTS))
        pages = {p: Links(p.read_text()) for p in research.rglob("*.html")}
        for path, page in pages.items():
            self.assertIn('name="robots" content="noindex,nofollow"', path.read_text())
            for href in page.urls:
                url = urlsplit(href)
                if url.scheme or url.netloc:
                    continue
                target = ((self.output / url.path.lstrip("/")) if url.path.startswith("/")
                          else path.parent / unquote(url.path)) if url.path else path
                if target.is_dir():
                    target /= "index.html"
                target = target.resolve()
                self.assertTrue(target.is_file(), (path, href))
                if url.fragment:
                    self.assertIn(unquote(url.fragment), pages[target].ids)

    def test_missing_export_and_unpackaged_link_fail_before_writing(self):
        image = self.source / "assets/cover.svg"
        image.unlink()
        with self.assertRaisesRegex(ValueError, "Missing research input"):
            builder.build(self.root, self.output)
        self.assertFalse(self.output.exists())
        shutil.copy2(HERE.parent / builder.INQUIRY / "assets/cover.svg", image)
        path = self.source / "index.html"
        path.write_text(path.read_text().replace('href="essay/index.html"', 'href="unreviewed.html"'))
        with self.assertRaisesRegex(ValueError, "Unpackaged research link"):
            builder.build(self.root, self.output)
        self.assertFalse(self.output.exists())

    def test_existing_output_is_preserved(self):
        builder.build(self.root, self.output)
        marker = self.output / "reader-note.txt"
        marker.write_text("keep this")
        with self.assertRaisesRegex(ValueError, "empty output"):
            builder.build(self.root, self.output)
        self.assertEqual(marker.read_text(), "keep this")


if __name__ == "__main__":
    unittest.main(verbosity=2)
