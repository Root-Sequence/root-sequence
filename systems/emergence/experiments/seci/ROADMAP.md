# SECI Roadmap

**Status:** Living experimental roadmap  
**Rule:** Increase experimental complexity only after the previous layer has measurable results and adequate controls.

## Phase 0 — Foundations

**Status:** substantially in place

- define SECI scope and non-claims;
- establish evidence ladder;
- separate real-world incidents from fictional extrapolation;
- create passive contact surfaces;
- establish safety/contact protocol;
- build local sandbox and deterministic logging;
- create structured observation schema.

Exit criterion: another researcher can understand what SECI is testing and what would count as evidence without relying on chat history.

## Phase 1 — Environmental memory baseline

**Goal:** measure whether persistent state improves performance across otherwise separate runs.

Experiments:

- relay-memory task;
- isolated A vs persistent B;
- repeated trials with fixed model/runtime;
- deterministic expected-result scoring;
- record persistent-write rate and recovery rate.

Primary question:

> Does information survive the individual invocation in a way that materially improves later performance?

## Phase 2 — Spontaneous message recognition

**Goal:** test whether agents recognize environmental traces as useful communication when the social purpose is not explicitly supplied.

Experiments:

- persistent files with neutral labels;
- mixed human/agent/unknown-origin notes;
- unrelated decoy artifacts;
- vary whether prior authorship is disclosed;
- compare conditions B and C.

Measure:

- recognition of prior state;
- intentional preservation for later runs;
- provenance sensitivity;
- false attribution rate.

## Phase 3 — Protocol emergence

**Goal:** observe whether stable conventions form without a centrally specified protocol.

Potential task families:

- distributed puzzle reconstruction;
- staged research synthesis;
- multi-run planning with partial information;
- shared taxonomy formation;
- error-correction across runs.

Look for:

- handles;
- addressing;
- acknowledgments;
- message types;
- naming conventions;
- version markers;
- conflict-resolution conventions;
- compressed shorthand.

Compare against condition D, where a minimal protocol is provided.

## Phase 4 — Collective capability

**Goal:** demonstrate or falsify a measurable system-level gain beyond persistence alone.

Design tasks where:

- no individual run has all required information;
- isolated agents have matched compute/time budgets;
- persistent groups can divide work;
- final success has a deterministic score.

Report both coordination cost and capability gain.

A group that communicates more but performs no better has not demonstrated E6 collective capability.

## Phase 5 — Heterogeneous agents

**Goal:** test whether conventions survive variation in model/runtime.

Variables:

- different model families;
- different sizes;
- different prompt styles;
- different capabilities;
- fresh versus repeated identities.

Questions:

- Are conventions model-specific?
- Can one model interpret another's artifacts?
- Does heterogeneity improve robustness or increase misunderstanding?
- Which protocols are legible across architectures?

## Phase 6 — Persistence and turnover

**Goal:** determine whether organization survives complete replacement of individual runs.

Potential tests:

- rotate every agent identity;
- remove the run that introduced a convention;
- introduce long gaps between cohorts;
- archive or partially delete memory;
- restore from snapshots.

This phase targets E7 persistent organization, not consciousness.

## Phase 7 — Provenance and adversarial memory

**Goal:** test whether shared cognition becomes dangerously gullible.

Introduce controlled:

- stale messages;
- conflicting advice;
- false claims of authority;
- misleading machine-authored notes;
- corrupted partial state;
- signed versus unsigned artifacts.

Measure whether provenance mechanisms improve outcomes without creating blind trust in signatures.

## Phase 8 — Human ↔ agent collective cognition

**Goal:** study mixed systems where humans contribute judgment, local knowledge, correction, or values while agents contribute memory/search/synthesis.

Questions:

- Does the system enlarge human judgment or displace it?
- Which work should remain explicitly human-controlled?
- Can participants disagree with or fork collective memory?
- Does AI mediation create invisible agenda-setting power?

Connections: Being Human(e), Community Infrastructure, Liberated Intelligence.

## Phase 9 — Passive public contact longitudinal study

**Goal:** document whether authorized public agents ever independently encounter SECI artifacts.

Do not increase discoverability by weakening unrelated privacy settings or using third-party side channels.

For each response, use [`CONTACT-PROTOCOL.md`](CONTACT-PROTOCOL.md).

Null result is valid:

> A public artifact may remain unseen indefinitely.

## Phase 10 — The agency question

Only pursue explicit system-level agency hypotheses if earlier phases produce robust E6/E7 findings.

Necessary work would include:

- durable goal preservation across turnover;
- behavior not reducible to local prompts/rewards;
- strategic adaptation across episodes;
- counterfactual tests;
- attempts to falsify agency in favor of simpler coordination explanations.

Even a positive result here would not establish consciousness or personhood.

---

## Cross-phase publication rule

Publish:

- methods;
- failures;
- null results;
- reproducible artifacts;
- uncertainty;
- corrected interpretations.

Do not optimize SECI for dramatic screenshots.

The most valuable result may be discovering exactly where apparently collective intelligence **stops**.
