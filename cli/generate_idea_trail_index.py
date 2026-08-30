#!/usr/bin/env python3
"""Generate a browsable Markdown index from IDEA_TRAIL_GRAPH.yml.

Usage:
  python cli/generate_idea_trail_index.py
  python cli/generate_idea_trail_index.py --check

Requires PyYAML (`python -m pip install pyyaml`).
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    raise SystemExit("PyYAML is required: python -m pip install pyyaml")

ROOT = Path(__file__).resolve().parents[1]
GRAPH_PATH = ROOT / "IDEA_TRAIL_GRAPH.yml"
OUTPUT_PATH = ROOT / "IDEA_TRAIL_INDEX.md"

ROLE_ORDER = {
    "research": 10,
    "human-practice": 20,
    "embodied-practice": 30,
    "real-system": 40,
    "analytical-lens": 50,
    "speculative-design": 60,
    "narrative": 70,
    "preservation": 80,
    "routing-map": 90,
}

ROLE_LABELS = {
    "research": "Research",
    "human-practice": "Human practice",
    "embodied-practice": "Embodied practice",
    "real-system": "Real-system work",
    "analytical-lens": "Analytical lens",
    "speculative-design": "Speculative design",
    "narrative": "Narrative",
    "preservation": "Preservation",
    "routing-map": "Routing / maps",
}


def load_graph() -> dict:
    with GRAPH_PATH.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError("Graph root must be a mapping")
    return data


def validate_graph(data: dict) -> list[str]:
    errors: list[str] = []
    trails = data.get("trails") or {}
    documents = data.get("documents") or []

    if not isinstance(trails, dict) or not trails:
        errors.append("`trails` must be a non-empty mapping")
        return errors

    if not isinstance(documents, list):
        errors.append("`documents` must be a list")
        return errors

    known = set(trails)
    seen_docs: set[tuple[str, str]] = set()

    for trail_id, trail in trails.items():
        if not isinstance(trail, dict) or not trail.get("title"):
            errors.append(f"trail `{trail_id}` is missing a title")

    for index, doc in enumerate(documents):
        if not isinstance(doc, dict):
            errors.append(f"documents[{index}] must be a mapping")
            continue

        repo = doc.get("repo")
        path = doc.get("path")
        role = doc.get("role")
        doc_trails = doc.get("trails") or []
        canonical_for = doc.get("canonical_for") or []

        if not repo or not path:
            errors.append(f"documents[{index}] must include repo and path")
            continue

        key = (repo, path)
        if key in seen_docs:
            errors.append(f"duplicate document entry: {repo}/{path}")
        seen_docs.add(key)

        if not role:
            errors.append(f"{repo}/{path} is missing role")
        elif role not in ROLE_LABELS:
            errors.append(f"{repo}/{path} has unknown role `{role}`")

        if not isinstance(doc_trails, list) or not doc_trails:
            errors.append(f"{repo}/{path} must list at least one trail")
            doc_trails = []

        for trail_id in [*doc_trails, *canonical_for]:
            if trail_id not in known:
                errors.append(f"{repo}/{path} references unknown trail `{trail_id}`")

        for trail_id in canonical_for:
            if trail_id not in doc_trails:
                errors.append(
                    f"{repo}/{path} is canonical_for `{trail_id}` but does not list it in trails"
                )

    return errors


def github_url(repo: str, path: str) -> str:
    return f"https://github.com/{repo}/blob/main/{path}"


def render(data: dict) -> str:
    trails: dict = data["trails"]
    documents: list[dict] = data.get("documents") or []

    by_trail: dict[str, list[dict]] = defaultdict(list)
    for doc in documents:
        for trail_id in doc.get("trails") or []:
            by_trail[trail_id].append(doc)

    lines = [
        "# Root Sequence — Idea Trail Browser",
        "",
        "<!-- GENERATED FILE: edit IDEA_TRAIL_GRAPH.yml, not this file. -->",
        "",
        "This index is generated from [`IDEA_TRAIL_GRAPH.yml`](IDEA_TRAIL_GRAPH.yml). "
        "It provides a document-level view of the cross-project Idea Trails defined in "
        "[`IDEA_TRAILS.md`](IDEA_TRAILS.md).",
        "",
        "> **Trail membership indicates a meaningful relationship, not canonical authority.** "
        "Each project's own source-of-truth rules still apply.",
        "",
        "## Trails",
        "",
    ]

    for trail_id, trail in trails.items():
        title = trail["title"]
        lines.append(f"- [{title}](#{trail_id}) — `{trail_id}`")

    lines.extend(["", "---", ""])

    for trail_id, trail in trails.items():
        title = trail["title"]
        lines.extend([
            f"<a id=\"{trail_id}\"></a>",
            f"## {title}",
            "",
            f"**Stable ID:** `{trail_id}`",
            "",
        ])

        docs = by_trail.get(trail_id, [])
        if not docs:
            lines.extend(["_No document mappings yet._", "", "---", ""])
            continue

        grouped: dict[str, list[dict]] = defaultdict(list)
        for doc in docs:
            grouped[doc["role"]].append(doc)

        for role in sorted(grouped, key=lambda r: (ROLE_ORDER.get(r, 999), r)):
            lines.append(f"### {ROLE_LABELS.get(role, role)}")
            lines.append("")
            for doc in sorted(grouped[role], key=lambda d: (d["repo"], d["path"])):
                repo = doc["repo"]
                path = doc["path"]
                marker = " **(canonical treatment)**" if trail_id in (doc.get("canonical_for") or []) else ""
                lines.append(
                    f"- [`{repo}/{path}`]({github_url(repo, path)}){marker}"
                )
            lines.append("")

        lines.extend(["---", ""])

    lines.extend([
        "## Maintenance",
        "",
        "- Edit `IDEA_TRAIL_GRAPH.yml` to add/remove document mappings.",
        "- Use stable IDs from `IDEA_TRAIL_METADATA.md`.",
        "- Run `python cli/generate_idea_trail_index.py` to regenerate this file.",
        "- Run `python cli/generate_idea_trail_index.py --check` in CI or before merging graph changes.",
        "- Do not add weak thematic links merely to make the graph dense.",
        "",
    ])

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="validate graph and verify generated index is current")
    args = parser.parse_args()

    try:
        data = load_graph()
    except Exception as exc:
        print(f"ERROR: could not load {GRAPH_PATH.name}: {exc}", file=sys.stderr)
        return 1

    errors = validate_graph(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    rendered = render(data)

    if args.check:
        if not OUTPUT_PATH.exists():
            print(f"ERROR: {OUTPUT_PATH.name} does not exist; run generator", file=sys.stderr)
            return 1
        current = OUTPUT_PATH.read_text(encoding="utf-8")
        if current != rendered:
            print(
                f"ERROR: {OUTPUT_PATH.name} is stale; run python cli/generate_idea_trail_index.py",
                file=sys.stderr,
            )
            return 1
        print("Idea Trail graph is valid and generated index is current.")
        return 0

    OUTPUT_PATH.write_text(rendered, encoding="utf-8")
    print(f"Wrote {OUTPUT_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
