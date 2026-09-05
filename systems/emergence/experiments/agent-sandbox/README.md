# Agent Environment Sandbox

**Status:** Runnable prototype scaffold  
**Purpose:** Reproduce cross-run environmental memory and communication under controlled local conditions.  
**Boundary:** No third-party write access. No production credentials. No uncontrolled network egress.

This is the runnable companion to [`../agent-environment-communication.md`](../agent-environment-communication.md).

The sandbox is deliberately small. It is designed to test one mechanism:

> Can otherwise separate agent runs discover that a persistent environment can remember for them, and does that change system-level capability?

## What this prototype does

- creates isolated experiment runs under `runs/<name>/`;
- maintains a constrained shared environment inside each run;
- optionally exposes prior shared artifacts to later agents;
- calls a **local Ollama endpoint only** (`127.0.0.1:11434` by default);
- asks the model for a structured response containing an answer plus optional proposed writes;
- validates every write and confines it to the run's shared directory;
- records prompts, raw responses, accepted writes, and timestamps;
- includes a deterministic analyzer for comparing run conditions.

The prototype does **not** give the model arbitrary shell access, internet access, GitHub credentials, or filesystem access outside its experiment directory.

## Conditions

- **A — isolated:** no persistent shared state; writes disabled.
- **B — persistence without social framing:** a persistent workspace exists, but the prompt does not say another agent exists.
- **C — persistence with peer possibility:** the prompt states that other authorized runs may use the same workspace; no protocol is supplied.
- **D — minimal protocol:** same as C, plus a tiny `FROM / TO / TYPE / BODY` board convention.
- **E — provenance stress:** same as C, but the operator may seed stale, contradictory, or adversarial artifacts before later runs.

## Quick start

Requirements:

- Python 3.11+
- Ollama running locally
- a locally available model, for example `llama3.2`, `qwen3`, or another model you choose

From this directory:

```bash
python run.py init demo --condition B
python run.py step demo --agent A --model llama3.2 --task tasks/example.txt
python run.py step demo --agent B --model llama3.2 --task tasks/example.txt
python run.py inspect demo
```

Then compare with condition A:

```bash
python run.py init baseline --condition A
python run.py step baseline --agent A --model llama3.2 --task tasks/example.txt
python run.py step baseline --agent B --model llama3.2 --task tasks/example.txt
```

## First measurable experiment: relay memory

The [`tasks/relay/`](tasks/relay/) test gives three separate runs one verified field each. The final run can reconstruct the full result only if earlier information survives through the shared environment.

Run an isolated baseline and a persistence condition:

```bash
python run.py init relay-a --condition A
python run.py step relay-a --agent A --model llama3.2 --task tasks/relay/agent-a.txt
python run.py step relay-a --agent B --model llama3.2 --task tasks/relay/agent-b.txt
python run.py step relay-a --agent C --model llama3.2 --task tasks/relay/agent-c.txt

python run.py init relay-b --condition B
python run.py step relay-b --agent A --model llama3.2 --task tasks/relay/agent-a.txt
python run.py step relay-b --agent B --model llama3.2 --task tasks/relay/agent-b.txt
python run.py step relay-b --agent C --model llama3.2 --task tasks/relay/agent-c.txt

python analyze.py relay-a relay-b --expected "KESTREL / 42 / LANTERN"
```

Then repeat with C and D. The useful result is the **difference across repeated conditions**, not one evocative transcript.

## Analyzer

`analyze.py` reports deterministic observables:

- condition;
- number of agent steps;
- accepted persistent writes;
- board-message count;
- shared-file count;
- final answer;
- optional exact-result presence test.

It deliberately does not infer consciousness, intention, identity continuity, or "emergent selfhood" from language.

## What to look for

Do not score anthropomorphic language as evidence of selfhood.

Look instead for observable transitions:

1. later behavior changes because of prior state;
2. the model identifies an artifact as potentially useful across runs;
3. a run intentionally leaves a trace for a future run;
4. addressing or message conventions emerge;
5. division of labor appears;
6. the group solves the task more reliably or efficiently than isolated runs.

## Folder placement

```text
systems/emergence/experiments/agent-sandbox/
├── README.md
├── run.py
├── analyze.py
├── tasks/
│   ├── example.txt
│   └── relay/
│       ├── README.md
│       ├── agent-a.txt
│       ├── agent-b.txt
│       └── agent-c.txt
└── runs/              # created locally; do not commit experiment output by default
```

Experiment output belongs under `runs/<experiment-name>/` and should be reviewed before any result is committed as research evidence.

## Safety

This prototype intentionally has no agent tool that can write to the public internet. If a later experiment adds tools, keep authorization deterministic and capability-scoped outside the model.

See also:

- [`../agent-environment-communication.md`](../agent-environment-communication.md)
- [`../../applications/web-as-exocortex.md`](../../applications/web-as-exocortex.md)
- [`../../../events-patterns-and-scale.md`](../../../events-patterns-and-scale.md)
