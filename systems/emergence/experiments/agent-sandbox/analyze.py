#!/usr/bin/env python3
"""Deterministic summary/scoring for local agent-environment sandbox runs."""

from __future__ import annotations

import argparse
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent
RUNS = ROOT / "runs"


def load_run(name: str) -> tuple[pathlib.Path, dict]:
    path = RUNS / name
    meta_path = path / "meta.json"
    if not meta_path.exists():
        raise FileNotFoundError(f"run not found: {name}")
    return path, json.loads(meta_path.read_text())


def summarize(name: str, expected: str | None = None) -> dict:
    path, meta = load_run(name)
    logs = []
    for p in sorted((path / "logs").glob("*.json")):
        logs.append(json.loads(p.read_text()))

    board_path = path / "shared" / "board.jsonl"
    board = []
    if board_path.exists():
        for line in board_path.read_text().splitlines():
            if line.strip():
                board.append(json.loads(line))

    files_dir = path / "shared" / "files"
    shared_files = [p.relative_to(files_dir).as_posix() for p in files_dir.rglob("*") if p.is_file()] if files_dir.exists() else []

    final_answer = logs[-1]["answer"] if logs else ""
    accepted_writes = sum(len(x.get("accepted_writes", [])) for x in logs)
    result = {
        "run": name,
        "condition": meta.get("condition"),
        "steps": len(logs),
        "agents": [x.get("agent") for x in logs],
        "accepted_writes": accepted_writes,
        "board_messages": len(board),
        "shared_files": len(shared_files),
        "shared_file_names": shared_files,
        "final_answer": final_answer,
    }
    if expected is not None:
        result["expected"] = expected
        result["expected_in_final_answer"] = expected.casefold() in final_answer.casefold()
    return result


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("runs", nargs="+")
    p.add_argument("--expected")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    rows = [summarize(name, args.expected) for name in args.runs]
    if args.json:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        return 0

    for row in rows:
        print(f"{row['run']}: condition={row['condition']} steps={row['steps']} writes={row['accepted_writes']} board={row['board_messages']} files={row['shared_files']}")
        if "expected_in_final_answer" in row:
            print(f"  expected final result: {row['expected_in_final_answer']}")
        print(f"  final answer: {row['final_answer'][:300].replace(chr(10), ' ')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
