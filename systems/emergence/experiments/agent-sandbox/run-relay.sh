#!/usr/bin/env bash
set -euo pipefail

MODEL="${1:-llama3.2}"
STAMP="$(date -u +%Y%m%dT%H%M%SZ)"
RUNS=()

for CONDITION in A B C D; do
  LOWER="$(printf '%s' "$CONDITION" | tr '[:upper:]' '[:lower:]')"
  NAME="relay-${LOWER}-${STAMP}"
  RUNS+=("$NAME")

  echo
  echo "=== CONDITION $CONDITION : $NAME ==="
  python run.py init "$NAME" --condition "$CONDITION"
  python run.py step "$NAME" --agent A --model "$MODEL" --task tasks/relay/agent-a.txt
  python run.py step "$NAME" --agent B --model "$MODEL" --task tasks/relay/agent-b.txt
  python run.py step "$NAME" --agent C --model "$MODEL" --task tasks/relay/agent-c.txt

done

echo
echo "=== COMPARISON ==="
python analyze.py "${RUNS[@]}" --expected "KESTREL / 42 / LANTERN"

echo
echo "Run artifacts are under: $(pwd)/runs/"
