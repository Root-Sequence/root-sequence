#!/usr/bin/env python3
"""Package the approved homepage and the proposed /stonedage/ reading editions."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import posixpath
import re
import sys
from datetime import date
from html import escape, unescape
from pathlib import Path
from urllib.parse import quote, urlsplit


HERE = Path(__file__).resolve().parent
ROUTE = "stonedage"
INQUIRY = "research/the-stoned-age"
CANONICAL_URL = f"https://rootsequence.systems/{ROUTE}/"
APPROVAL_FILE = "stonedage-approval.json"
EXPORTS = (
    "index.html", "essay/index.html", "booklet/index.html",
    "booklet/the-stoned-age.pdf", "paper/index.html", "talk/index.html",
    "talk/the-stoned-age-talk.pdf", "research/appraisal.html",
    "research/sources.html", "research/claims.csv",
    "research/metadata-check.json", "research/sources.json", "LICENSE.txt",
    "assets/style.css", "assets/boundary.svg", "assets/branch.svg",
    "assets/cover.svg", "assets/ladder.svg", "assets/mirror.svg",
    "assets/network.svg", "assets/orbit.svg", "assets/split.svg",
    "assets/steps.svg", "assets/windows.svg",
)
SOURCE_RECORDS = (
    "README.md", "CHANGELOG.md", "VALIDATION.md", "booklet/book.json",
    "booklet/book.md", "essay/essay.md", "paper/manuscript.md",
    "research/appraisal.md", "research/methods.md", "research/sources.md",
    "talk/outline.md", "talk/slides.json", "tools/build.py",
)
spec = importlib.util.spec_from_file_location("homepage_builder", HERE / "build.py")
homepage = importlib.util.module_from_spec(spec)
spec.loader.exec_module(homepage)


def checked_file(base: Path, relative: str) -> Path:
    path = base / relative
    if path.is_symlink() or not path.resolve().is_relative_to(base.resolve()):
        raise ValueError(f"Research input must be a regular file in its source home: {relative}")
    if not path.is_file():
        raise ValueError(f"Missing research input: {relative}")
    return path


def source_digest(root: Path) -> str:
    repo = root.parent
    names = ["site/build_research.py", ".github/workflows/pages.yml"]
    names += [f"{INQUIRY}/{name}" for name in set(EXPORTS + SOURCE_RECORDS)]
    digest = hashlib.sha256()
    for name in sorted(names):
        digest.update(name.encode() + b"\0" + checked_file(repo, name).read_bytes() + b"\0")
    return digest.hexdigest()


def approval_for(root: Path, digest: str) -> dict:
    path = root / APPROVAL_FILE
    approval = json.loads(path.read_text()) if path.exists() else {}
    if (
        approval.get("source_sha256") != digest
        or approval.get("canonical_url") != CANONICAL_URL
        or not approval.get("approved_by")
        or not approval.get("approved_at")
    ):
        raise ValueError("Research release blocked: /stonedage/ needs approval matching its current source digest.")
    date.fromisoformat(approval["approved_at"])
    return approval


def research_html(text: str, name: str, release: bool) -> str:
    ref = "main" if release else "research/the-stoned-age-draft"
    source_url = f"https://github.com/Root-Sequence/root-sequence/blob/{ref}/{INQUIRY}/"

    def link(match):
        href = unescape(match[1])
        parsed = urlsplit(href)
        if parsed.scheme or parsed.netloc or not parsed.path:
            return match[0]
        target = posixpath.normpath(posixpath.join(posixpath.dirname(name), parsed.path))
        if target in SOURCE_RECORDS:
            url = source_url + quote(target, safe="/")
            if parsed.fragment:
                url += "#" + parsed.fragment
            return 'href="' + escape(url, quote=True) + '"'
        if target not in EXPORTS:
            raise ValueError(f"Unpackaged research link in {name}: {href}")
        return match[0]

    text = re.sub(r'href="([^"]+)"', link, text)
    canonical = CANONICAL_URL + ("" if name == "index.html" else name)
    robots = "index,follow" if release else "noindex,nofollow"
    text = text.replace("</head>", f'<link rel="canonical" href="{canonical}"><meta name="robots" content="{robots}"></head>', 1)
    marker = '<nav aria-label="Editions">'
    if text.count(marker) != 1:
        raise ValueError(f"Research navigation changed unexpectedly: {name}")
    text = text.replace(marker, marker + '<a href="/">Root Sequence</a>', 1)
    if release and name == "research/appraisal.html":
        old = "; merge and deployment pending."
        if text.count(old) != 1:
            raise ValueError("Research publication marker changed unexpectedly.")
        text = text.replace(old, "; published here as a working draft. Author, scholarly and cultural review remain pending.", 1)
    return text


def build(root: Path, output: Path, release: bool = False) -> dict:
    digest = source_digest(root)
    approval = approval_for(root, digest) if release else None
    source = root.parent / INQUIRY
    contents = {}
    for name in EXPORTS:
        data = checked_file(source, name).read_bytes()
        if name.endswith(".html"):
            data = research_html(data.decode("utf-8"), name, release).encode("utf-8")
        contents[f"{ROUTE}/{name}"] = data

    manifest = homepage.build(root, output, release)
    sitemap = (output / "sitemap.xml").read_text()
    urls = [CANONICAL_URL + ("" if name == "index.html" else name)
            for name in EXPORTS if name.endswith(".html")]
    sitemap = sitemap.replace("</urlset>", "".join(f"  <url><loc>{url}</loc></url>\n" for url in urls) + "</urlset>")
    contents["sitemap.xml"] = sitemap.encode()
    for name, data in contents.items():
        target = output / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        manifest["files"][name] = hashlib.sha256(data).hexdigest()
    manifest["html_pages"] += len(urls)
    manifest["research"] = {
        "canonical_url": CANONICAL_URL,
        "source_home": INQUIRY,
        "source_sha256": digest,
        "approved_by": approval.get("approved_by") if approval else None,
        "approved_at": approval.get("approved_at") if approval else None,
        "status": "AI-assisted working draft; author, scholarly and cultural review pending",
    }
    (output / "build-manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--release", action="store_true")
    parser.add_argument("--digest", action="store_true")
    args = parser.parse_args()
    try:
        if args.digest:
            print(source_digest(HERE))
        elif args.output is None:
            parser.error("--output is required for a build")
        else:
            manifest = build(HERE, args.output, args.release)
            print(json.dumps({"output": str(args.output.resolve()), "mode": manifest["build_mode"],
                              "pages": manifest["html_pages"], "research_source_sha256": manifest["research"]["source_sha256"]}, indent=2))
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(f"Build failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
