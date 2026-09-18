#!/usr/bin/env python3
"""Build the approved single-file Root Sequence site for review or publication."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import date
from pathlib import Path


HERE = Path(__file__).resolve().parent
DOMAIN = "rootsequence.systems"
BASE_URL = f"https://{DOMAIN}/"
SOURCE_FILES = ("build.py", "index.html")

# These are publication-state changes, not an editorial rewrite. Preview output is
# byte-for-byte identical to index.html; release output makes the same approved
# page truthful once it is hosted publicly.
RELEASE_REPLACEMENTS = (
    ('<meta content="noindex,nofollow" name="robots"/>',
     '<meta content="index,follow" name="robots"/>', 1),
    ('This preview rearranges existing project text and adds proposed About and participation copy.',
     'This public seed rearranges existing project text and adds About and participation copy.', 2),
    ('Privacy and this preview', 'Privacy and this site', 2),
    ('This is a local review copy, not a deployment or a publication approval. There are no manuscript scenes in this edition.',
     'This is the public seed edition of the Root Sequence site. There are no manuscript scenes in this edition.', 2),
    ('A future hosted version may produce ordinary request logs at its hosting provider. This local preview makes no claim about the provider’s retention or access policies.',
     'This hosted version may produce ordinary request logs at its hosting provider. This site makes no claim about the provider’s retention or access policies.', 2),
    ('Design study · Updated 17 September 2026 · Not a published site',
     'Public seed · Published 18 September 2026', 2),
    ('This preview has no separate public website to link to for Coherent World.',
     'This site has no separate public website to link to for Coherent World.', 1),
    ('so this preview does not link to it.', 'so this site does not link to it.', 1),
)


def source_digest(root: Path) -> str:
    digest = hashlib.sha256()
    for name in SOURCE_FILES:
        digest.update(name.encode() + b"\0" + (root / name).read_bytes() + b"\0")
    return digest.hexdigest()


def release_html(source: str) -> str:
    result = source
    for old, new, expected_count in RELEASE_REPLACEMENTS:
        actual_count = result.count(old)
        if actual_count != expected_count:
            raise ValueError(
                f"Release marker changed unexpectedly: expected {expected_count} occurrence(s), "
                f"found {actual_count}: {old[:72]!r}"
            )
        result = result.replace(old, new)
    return result


def approval_for(root: Path, digest: str) -> dict:
    path = root / "approval.json"
    approval = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
    if (
        approval.get("source_sha256") != digest
        or not approval.get("approved_by")
        or not approval.get("approved_at")
    ):
        raise ValueError(
            "Release blocked: approval.json must identify the reviewer and match "
            "the exact current source digest."
        )
    date.fromisoformat(approval["approved_at"])
    return approval


def build(root: Path, output: Path, release: bool = False) -> dict:
    digest = source_digest(root)
    approval = approval_for(root, digest) if release else None
    if output.exists() and (output.is_symlink() or any(output.iterdir())):
        raise ValueError("Choose a new empty output directory; the builder will not overwrite it.")
    output.mkdir(parents=True, exist_ok=True)

    source = (root / "index.html").read_text(encoding="utf-8")
    html = release_html(source) if release else source
    contents: dict[str, bytes] = {
        "index.html": html.encode("utf-8"),
        "robots.txt": (
            f"User-agent: *\nAllow: /\nSitemap: {BASE_URL}sitemap.xml\n"
            if release
            else "User-agent: *\nDisallow: /\n"
        ).encode(),
        "sitemap.xml": (
            '<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"  <url><loc>{BASE_URL}</loc><lastmod>2026-09-18</lastmod></url>\n"
            "</urlset>\n"
        ).encode(),
        ".nojekyll": b"",
        "CNAME": f"{DOMAIN}\n".encode(),
    }
    manifest = {
        "site": "Root Sequence",
        "canonical_url": BASE_URL,
        "build_mode": "release" if release else "preview",
        "source_sha256": digest,
        "approved_by": approval.get("approved_by") if approval else None,
        "approved_at": approval.get("approved_at") if approval else None,
        "html_pages": 1,
        "files": {name: hashlib.sha256(value).hexdigest() for name, value in contents.items()},
        "note": "Hashes cover generated files before this manifest. Build success is not live-host verification.",
    }
    contents["build-manifest.json"] = (json.dumps(manifest, indent=2) + "\n").encode()
    for name, value in contents.items():
        (output / name).write_bytes(value)
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / "preview")
    parser.add_argument("--release", action="store_true")
    parser.add_argument("--digest", action="store_true")
    args = parser.parse_args()
    try:
        if args.digest:
            print(source_digest(HERE))
        else:
            manifest = build(HERE, args.output, args.release)
            print(json.dumps({
                "output": str(args.output.resolve()),
                "mode": manifest["build_mode"],
                "pages": manifest["html_pages"],
                "source_sha256": manifest["source_sha256"],
            }, indent=2))
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print(f"Build failed: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
