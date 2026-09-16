#!/usr/bin/env python3
"""Small, offline static publisher. Preview by default; exact-source approval for release."""
from __future__ import annotations
import argparse
import hashlib
import html
import json
import re
import sys
import zipfile
from datetime import date
from pathlib import Path
from urllib.parse import urlparse
from xml.etree import ElementTree as ET

HERE = Path(__file__).resolve().parent
SAFE_SLUG = re.compile(r"^(?:[a-z0-9]+(?:-[a-z0-9]+)*(?:/[a-z0-9]+(?:-[a-z0-9]+)*)*/)?$")
STATES = {"Seed", "Growing", "Established"}

def source_digest(root: Path) -> str:
    digest = hashlib.sha256()
    for name in ("build.py", "content.json", "style.css"):
        digest.update(name.encode() + b"\0" + (root / name).read_bytes() + b"\0")
    return digest.hexdigest()

def safe_url(value: str) -> str:
    parsed = urlparse(value)
    if parsed.scheme:
        if parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password:
            raise ValueError(f"Only ordinary HTTPS external links are allowed: {value!r}")
    elif parsed.netloc or not value.startswith("/") or value.startswith("//") or ".." in value.split("/"):
        raise ValueError(f"Invalid internal link: {value!r}")
    return value

def validate(data: dict) -> None:
    base = urlparse(data["base_url"])
    if base.scheme != "https" or not base.netloc or base.path not in ("", "/") or base.query or base.fragment:
        raise ValueError("base_url must be an HTTPS origin, without a path or query")
    if data["theme"] not in ("research", "story"):
        raise ValueError("Unknown theme")
    pages = data["pages"]
    slugs = [p["slug"] for p in pages]
    if len(set(slugs)) != len(slugs) or "" not in slugs:
        raise ValueError("Page slugs must be unique and include the homepage")
    targets = {"/" + s for s in slugs}
    targets |= {"/feed.xml", "/seed-archive.zip", "/project-map.json"}
    for p in pages:
        if not SAFE_SLUG.fullmatch(p["slug"]):
            raise ValueError(f"Unsafe slug: {p['slug']!r}")
        if p["maturity"] not in STATES or not p.get("kind") or not p.get("epistemic_status"):
            raise ValueError("Each page needs separate maturity, kind and epistemic status")
        created, updated = date.fromisoformat(p["created"]), date.fromisoformat(p["updated"])
        if updated < created:
            raise ValueError("Updated date precedes created date")
        for section in p.get("sections", []):
            for link in section.get("links", []):
                check_link(link, targets)
        for link in p.get("sources", []) + p.get("related", []):
            check_link(link, targets)
    for link in data["nav"]:
        check_link(link, targets)
    ids = {n["id"] for n in data.get("projects", [])}
    if len(ids) != len(data.get("projects", [])):
        raise ValueError("Duplicate project identity")
    for node in data.get("projects", []):
        safe_url(node["url"])
    for edge in data.get("relationships", []):
        if edge["from"] not in ids or edge["to"] not in ids or not edge.get("relation"):
            raise ValueError("Graph edge references an unknown project or lacks a relation")

def check_link(link: dict, targets: set[str]) -> None:
    value = safe_url(link["url"])
    if value.startswith("/") and urlparse(value).path not in targets:
        raise ValueError(f"Internal link has no generated target: {value}")

def render(data: dict, page: dict, preview: bool) -> str:
    esc = html.escape
    prefix = "../" * page["slug"].count("/")
    def href(value: str) -> str:
        safe_url(value)
        if value.startswith("/"):
            parsed = urlparse(value)
            path = parsed.path[1:]
            if not path or path.endswith("/"):
                path += "index.html"
            suffix = ("?" + parsed.query if parsed.query else "") + ("#" + parsed.fragment if parsed.fragment else "")
            return esc(prefix + path + suffix, quote=True)
        return esc(value, quote=True)
    def link(item: dict) -> str:
        return f'<a href="{href(item["url"])}">{esc(item["label"])}</a>'
    nav = "".join(link(n) for n in data["nav"])
    body = []
    for i, section in enumerate(page.get("sections", []), 1):
        heading = f'<h2 id="section-{i}">{esc(section["heading"])}</h2>' if section.get("heading") else ""
        paragraphs = "".join(f'<p>{esc(p)}</p>' for p in section.get("paragraphs", []))
        quotation = f'<blockquote><p>{esc(section["quote"])}</p></blockquote>' if section.get("quote") else ""
        items = "".join(f'<li>{link(item)}<span>{esc(item.get("description", ""))}</span></li>' for item in section.get("links", []))
        listing = f'<ul class="directory">{items}</ul>' if items else ""
        body.append(f'<section>{heading}{quotation}{paragraphs}{listing}</section>')
    if page.get("show_project_map"):
        nodes = {n["id"]: n for n in data["projects"]}
        rows = "".join(f'<tr><th scope="row">{esc(nodes[e["from"]]["title"])}</th><td>{esc(e["relation"])}</td><td>{esc(nodes[e["to"]]["title"])}</td></tr>' for e in data["relationships"])
        body.append('<div class="table-scroll"><table><caption>Selected relationships, not a hierarchy of ownership</caption><thead><tr><th scope="col">Project</th><th scope="col">Relationship</th><th scope="col">Project</th></tr></thead><tbody>' + rows + '</tbody></table></div>')
    def reference_section(title: str, key: str) -> str:
        items = "".join(f'<li>{link(n)}</li>' for n in page.get(key, []))
        return f'<section class="references"><h2>{title}</h2><ul>{items}</ul></section>' if items else ""
    canonical = esc(data["base_url"].rstrip("/") + "/" + page["slug"], quote=True)
    state = "PREVIEW — not a live release" if preview else "Public Seed v0.1"
    robots = '<meta name="robots" content="noindex,nofollow">' if preview else '<meta name="robots" content="index,follow">'
    canon = f'<span>Canon: {esc(page["canon_status"])}</span>' if page.get("canon_status") else ""
    source_note = f'<p class="source-note">{esc(page["provenance"])}</p>' if page.get("provenance") else ""
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(page['title'])} · {esc(data['title'])}</title><meta name="description" content="{esc(page['description'], quote=True)}">
{robots}<link rel="canonical" href="{canonical}"><link rel="alternate" type="application/atom+xml" title="{esc(data['title'], quote=True)} updates" href="{prefix}feed.xml"><link rel="stylesheet" href="{prefix}style.css"></head>
<body class="{data['theme']}"><a class="skip" href="#main">Skip to content</a>
<header class="site-header"><a class="wordmark" href="{prefix}index.html">{esc(data['title'])}<span>{esc(data['tagline'])}</span></a><nav aria-label="Main navigation">{nav}</nav></header>
<main id="main" tabindex="-1"><p class="eyebrow">{esc(data['edition'])} / {esc(page['kind'])}</p><h1>{esc(page['title'])}</h1><p class="lede">{esc(page['description'])}</p>
<div class="metadata"><span>{esc(page['maturity'])}</span><span>{esc(page['epistemic_status'])}</span>{canon}<span>Created <time datetime="{page['created']}">{page['created']}</time></span><span>Updated <time datetime="{page['updated']}">{page['updated']}</time></span></div>
<p class="build-status">{state}</p>{''.join(body)}{reference_section('Sources and canonical homes', 'sources')}{reference_section('Continue exploring', 'related')}{source_note}</main>
<footer><p>{esc(data['footer'])}</p><p><a href="{prefix}feed.xml">Atom feed</a> · <a href="{prefix}seed-archive.zip">Download this edition</a> · <a href="{prefix}project-map.json">Project relationships (JSON)</a></p><p class="fine">{state}. No accounts, analytics, external fonts, or client-side JavaScript.</p></footer></body></html>'''

def build(root: Path, output: Path, release: bool = False) -> dict:
    data = json.loads((root / "content.json").read_text(encoding="utf-8"))
    validate(data)
    digest = source_digest(root)
    if release:
        approval_path = root / "approval.json"
        approval = json.loads(approval_path.read_text(encoding="utf-8")) if approval_path.exists() else {}
        if approval.get("source_sha256") != digest or not approval.get("approved_by") or not approval.get("approved_at"):
            raise ValueError("Release blocked: review these exact source files and record their digest, approved_by and approved_at in approval.json. Preview needs no approval.")
        date.fromisoformat(approval["approved_at"])
    if output.exists() and (output.is_symlink() or any(output.iterdir())):
        raise ValueError("Choose a new empty output directory; the builder will not delete or overwrite an existing build.")
    output.mkdir(parents=True, exist_ok=True)
    contents: dict[str, bytes] = {}
    for page in data["pages"]:
        contents[page["slug"] + "index.html"] = render(data, page, not release).encode("utf-8")
    contents["style.css"] = (root / "style.css").read_bytes()
    graph = {"scope": "Selected public-facing project relationships; existing Wiki remains canonical for ecosystem identity.", "projects": data.get("projects", []), "relationships": data.get("relationships", [])}
    contents["project-map.json"] = (json.dumps(graph, indent=2, ensure_ascii=False) + "\n").encode()
    ET.register_namespace("", "http://www.w3.org/2005/Atom")
    ns = "{http://www.w3.org/2005/Atom}"
    feed = ET.Element(ns + "feed")
    for tag, value in (("title", data["title"]), ("id", data["base_url"]), ("updated", max(p["updated"] for p in data["pages"]) + "T00:00:00Z")):
        ET.SubElement(feed, ns + tag).text = value
    ET.SubElement(feed, ns + "link", {"href": data["base_url"].rstrip("/") + "/feed.xml", "rel": "self"})
    author = ET.SubElement(feed, ns + "author")
    ET.SubElement(author, ns + "name").text = data["author"]
    for page in sorted(data["pages"], key=lambda p: (p["updated"], p["slug"]), reverse=True):
        entry = ET.SubElement(feed, ns + "entry")
        url = data["base_url"].rstrip("/") + "/" + page["slug"]
        for tag, value in (("title", page["title"]), ("id", url), ("updated", page["updated"] + "T00:00:00Z"), ("summary", page["description"])):
            ET.SubElement(entry, ns + tag).text = value
        ET.SubElement(entry, ns + "link", {"href": url})
    contents["feed.xml"] = ET.tostring(feed, encoding="utf-8", xml_declaration=True)
    sitemap = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for page in data["pages"]:
        url = ET.SubElement(sitemap, "url")
        ET.SubElement(url, "loc").text = data["base_url"].rstrip("/") + "/" + page["slug"]
        ET.SubElement(url, "lastmod").text = page["updated"]
    contents["sitemap.xml"] = ET.tostring(sitemap, encoding="utf-8", xml_declaration=True)
    contents["robots.txt"] = ("User-agent: *\nDisallow: /\n" if not release else "User-agent: *\nAllow: /\nSitemap: " + data["base_url"].rstrip("/") + "/sitemap.xml\n").encode()
    contents[".nojekyll"] = b""
    manifest = {"site": data["title"], "build_mode": "release" if release else "preview", "source_sha256": digest, "html_pages": len(data["pages"]), "files": {name: hashlib.sha256(value).hexdigest() for name, value in contents.items()}, "note": "Hashes cover generated files before this manifest and its preservation ZIP. Build success is not deployment verification."}
    contents["build-manifest.json"] = (json.dumps(manifest, indent=2) + "\n").encode()
    for name, value in contents.items():
        target = output / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(value)
    with zipfile.ZipFile(output / "seed-archive.zip", "w", zipfile.ZIP_DEFLATED) as archive:
        for name, value in contents.items():
            info = zipfile.ZipInfo(name, (2026, 9, 16, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, value)
    return manifest

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=HERE / "preview")
    parser.add_argument("--release", action="store_true", help="Requires approval of the exact current source digest")
    parser.add_argument("--digest", action="store_true", help="Print the exact-source digest without approving or publishing anything")
    args = parser.parse_args()
    try:
        if args.digest:
            print(source_digest(HERE))
        else:
            manifest = build(HERE, args.output, args.release)
            print(json.dumps({"output": str(args.output.resolve()), "mode": manifest["build_mode"], "pages": manifest["html_pages"], "source_sha256": manifest["source_sha256"]}, indent=2))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"Build failed: {exc}", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
