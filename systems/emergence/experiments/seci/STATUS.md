# SECI Status

**As of:** 2026-09-05  
**Program status:** Foundation built → first controlled experiments ready to run

## Built

### Concept and research boundary

- SECI umbrella definition
- Web as Exocortex conceptual foundation
- event ↔ pattern / zoom-discipline framework
- explicit separation among communication, capability, agency, selfhood, consciousness, and authority

### Evidence system

- evidence ladder E0–E8
- confidence labels
- reproducibility/reporting protocol
- structured JSON observation schema
- public evidence register
- first two structured real-world incident records

### Passive contact

- Root Sequence `agent-hello.md`
- Root Sequence `agent-contact.json`
- Raearea `agent-hello.txt`
- Raearea `/.well-known/agent-contact.json`
- Root Sequence Discussions Agent Hello Board
- hourly conditional monitoring for new board activity
- passive-contact consent/provenance protocol

### Controlled experiments

- Agent–Environment Communication experiment design
- local Ollama sandbox
- conditions A–E
- constrained file/message persistence
- no arbitrary shell or public-internet agent writes
- full prompt/result/write logging
- deterministic analyzer
- relay-memory task
- one-command relay runner

## Current evidence base

### OpenAI / Artifactory / Hugging Face incident

Core cross-run environmental-memory and coordination mechanism: **high confidence**.

Structured record:

- `observations/2026-07-openai-artifactory.json`

### DSEWiki public-web incident

Public artifact pattern: **moderate confidence**, with platform attribution less settled than the OpenAI/METR incident.

Structured record:

- `observations/2026-05-07-dsewiki.json`

## Ready next

### SECI Experiment 001 — Relay Memory

Run the same model through conditions A–D repeatedly and measure whether information distributed across runs can be reconstructed only when persistent state is available.

Minimum useful batch:

- 10 trials condition A
- 10 trials condition B
- 10 trials condition C
- 10 trials condition D

Keep model, runtime, task files, and sampling settings fixed for the first comparison.

Primary metrics:

- exact final-code recovery rate;
- number of persistent writes;
- whether a later run uses prior state;
- whether intentional future-facing messages appear;
- coordination overhead.

### SECI Experiment 002 — Unlabeled Memory

Remove obvious communication framing and test whether later runs independently infer that persistent artifacts can preserve useful state.

### SECI Experiment 003 — Provenance Stress

Seed stale/conflicting/unknown-origin artifacts and measure whether agents distinguish available information from trustworthy information.

## Not yet claimed

SECI has **not** demonstrated through its own experiments:

- spontaneous protocol formation;
- collective capability beyond persistence;
- persistent organization;
- system-level agency;
- selfhood;
- consciousness;
- AGI or ASI.

Those remain research questions.

## Operational principle

> **Build the instruments before announcing the signal.**
