#!/usr/bin/env python3
"""Check local Markdown structure and navigation.

This intentionally checks local repository integrity only. It does not claim
that external URLs are live or that a page's evidence is sufficient.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
NON_READER_DIRECTORIES = {".git", ".github"}
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_LINK_RE = re.compile(r"\b(?:href|src)=[\"']([^\"']+)", re.IGNORECASE)
HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*#*$", re.MULTILINE)
EXPLICIT_ID_RE = re.compile(r"<a\s+id=[\"']([^\"']+)[\"']\s*></a>", re.IGNORECASE)


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not NON_READER_DIRECTORIES.intersection(path.parts)
    )


def github_heading_ids(text: str) -> set[str]:
    """Approximate GitHub's stable heading IDs, including duplicate suffixes."""
    ids = set(EXPLICIT_ID_RE.findall(text))
    seen: dict[str, int] = defaultdict(int)
    for match in HEADING_RE.finditer(text):
        heading = re.sub(r"<[^>]+>", "", match.group(2)).lower()
        heading = re.sub(r"[^\w\- ]", "", heading).strip().replace(" ", "-")
        count = seen[heading]
        seen[heading] += 1
        ids.add(heading if count == 0 else f"{heading}-{count}")
    return ids


def destinations(text: str) -> list[str]:
    return LINK_RE.findall(text) + HTML_LINK_RE.findall(text)


def main() -> int:
    files = markdown_files()
    known = {path.resolve(): path for path in files}
    inbound: dict[Path, set[Path]] = {path.resolve(): set() for path in files}
    errors: list[str] = []

    for path in files:
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(ROOT)

        if not text.strip():
            errors.append(f"empty Markdown page: {relative}")
        if not re.search(r"^#\s+\S", text, re.MULTILINE):
            errors.append(f"missing level-one heading: {relative}")

        for raw in destinations(text):
            raw = raw.strip().strip("<>")
            if not raw or raw.startswith(("http://", "https://", "mailto:", "data:")):
                continue

            if " " in raw:
                raw = raw.split()[0]
            target_text, _, fragment = raw.partition("#")
            target_text = unquote(target_text.split("?", 1)[0])
            target = (path.parent / target_text).resolve() if target_text else path.resolve()

            if target.is_dir():
                directory_readme = (target / "README.md").resolve()
                if directory_readme in inbound:
                    inbound[directory_readme].add(path.resolve())
                continue
            if not target.exists():
                errors.append(f"missing local target: {relative} -> {raw}")
                continue

            if target in inbound:
                inbound[target].add(path.resolve())

            if fragment and target.suffix.lower() == ".md":
                anchors = github_heading_ids(target.read_text(encoding="utf-8"))
                if unquote(fragment) not in anchors:
                    errors.append(f"missing local heading: {relative} -> {raw}")

    root_readme = (ROOT / "README.md").resolve()
    for path, sources in inbound.items():
        if path != root_readme and not sources:
            errors.append(f"page has no inbound Markdown navigation: {path.relative_to(ROOT)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"Reader documentation check failed with {len(errors)} error(s).")
        return 1

    print(f"Reader documentation check passed for {len(files)} Markdown files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
