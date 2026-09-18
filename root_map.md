# 🗺 Root Sequence Repository Map

**Document role:** Canonical repository architecture and content-routing guide<br>
**Status:** Active / living<br>
**Last reviewed:** 2026-09-17<br>

This file is a compass for the **`root-sequence` repository**: how its folders and conceptual flows connect.

It is not the map of the entire GitHub organization. For that, use the [Root Sequence Ecosystem Map](ECOSYSTEM.md).

## Information architecture

Reader-facing material has five layers. Each layer has a different job:

1. [`README.md`](README.md) is the front door. It explains the project and offers a small number of useful entry paths.
2. This map explains the repository's structure, routing rules, and canonical-page conventions.
3. [`ECOSYSTEM.md`](ECOSYSTEM.md) maps projects across the Root Sequence organization; [`IDEA_TRAILS.md`](IDEA_TRAILS.md) maps recurring questions across those projects.
4. A directory `README.md` is the local index for that area. It should name every developed page, distinguish current work from planned work, and link back to the relevant parent.
5. Substantive pages own definitions, arguments, methods, applications, artifacts, or records. Other pages should summarize briefly and link to that home rather than copying the treatment.

Generated indexes, migration pointers, validation receipts, and historical overviews are supporting records. They must identify their role so readers do not mistake them for a second source of truth.

## Canonical-page rules

- Give each substantive idea one primary home at its current level of scope.
- Keep broad, cross-domain work here. Route project-specific software, practice, research conclusions, and fiction canon to their own repositories.
- Preserve stable paths when they have readers, or update known dependents before removing them. If a migration pointer is needed, keep it concise and do not leave a second substantive treatment behind.
- Link to the nearest useful destination, not merely the repository root.
- Use relative links for files in this repository. Use full URLs only across repositories or for external sources.
- When a page changes role, update its nearest directory index in the same change. Update this map or the root README only when the change matters at that level.
- Never use a generated index as the place to make a substantive edit. Change its source and regenerate it.
- Do not publish a private project's content here to repair a public navigation gap. Name the access boundary and provide a public summary only when one already exists.

## Labels describe different things

Do not compress every kind of status into one word.

| Label | Question it answers | Examples |
|---|---|---|
| **Document role** | What job does this page do? | orientation, definition, framework, analysis, method, application, artifact, experiment, routing map, record |
| **Status** | How mature or current is it? | active, developing, exploratory, proposed, historical, generated |
| **Maturity** | How far has this version been developed or reviewed? | seed, growing, established (used by the website) |
| **Canonical scope** | What is this page the primary home for? | repository architecture, shared concept definition, project-specific method |
| **Evidence status** | How strongly are its claims supported? | observed, supported, hypothesis, interpretation, normative, metaphor, open |
| **Access** | Who can follow the destination? | public, private, unpublished |

`Canonical` means “the maintained primary home for this material.” It does not mean final, unquestionably true, or applicable outside the stated scope.

---

## Path naming rules

- Directory names should describe their current function, not historical importance or presumed authority.
- Reader-facing paths use lowercase kebab-case when practical.
- Avoid generic names such as `core`, `framework`, `final`, or `misc` unless the page explicitly explains a compatibility or historical role.
- When a path must remain because an approved artifact or external repository still depends on it, reduce it to a labeled pointer and keep substantive material at the descriptive canonical path.
- A renamed directory requires the same change to local indexes, repository maps, contributor guidance, and every affected internal link.

---

## 🌱 Current structure

- [`founding-texts/`](founding-texts/) — founding texts, early models, manifestos, normative essays, and historical orientations.
- [`concepts/`](concepts/) — shared vocabulary, cross-project frameworks, design principles, and methods.
- [`analysis/`](analysis/) — diagnosis of systems, power, capitalism, infrastructure, surveillance, and related conditions.
- [`ideology/`](ideology/) — myths, philosophies, and narratives that justify or contest power.
- [`systems/`](systems/) — analytical principles, structure, dependency, stress, failure, feedback, recovery, coherence, and adaptation.
- [`futures/`](futures/) — trajectories, alternatives, collapse, resilience, and possible liberations.
- [`commons/`](commons/) — zines, fragments, maps, and practices intended for practical or public reuse.
  - [`commons/fragments/`](commons/fragments/) — short, unfinished, poetic, or compostable material.
  - [`commons/zines/`](commons/zines/) — longer public and printable artifacts.
- [`wiki/`](wiki/) — migration pointer to the standalone [`Root-Sequence/wiki`](https://github.com/Root-Sequence/wiki) repository.
- [`site/`](site/README.md) — source for the introductory Public Seed website; it projects selected material without replacing research or the Wiki.
- [`cli/`](cli/) — experimental scripts and tools.
- [`assets/`](assets/) — visual material and diagrams.

Root-level orientation files:

- [`README.md`](README.md) — repository introduction and entry points.
- [`ECOSYSTEM.md`](ECOSYSTEM.md) — organization-wide project relationships and routing rules.
- [`root_map.md`](root_map.md) — this internal repository map.
- [`AUDIT.md`](AUDIT.md) — latest comprehensive reader-facing audit, decisions, changes, and remaining evidence work.
- [`IDEA_TRAILS.md`](IDEA_TRAILS.md) — recurring questions across the wider ecosystem.
- [`IDEA_TRAIL_INDEX.md`](IDEA_TRAIL_INDEX.md) — generated document browser; edit its graph source rather than the generated file.
- [`THOUGHT_ROUTING.md`](THOUGHT_ROUTING.md) — capture and placement convention for new material.
- [`hello-world.md`](hello-world.md) — early public orientation text.
- [`contributing.md`](contributing.md) — contribution guidance.
- [`license`](license) — repository license text.

Fragments already have a canonical home under [`commons/fragments/`](commons/fragments/). A raw note that is not yet public-facing or deliberately fragmentary should remain in a temporary capture system until it is ready to enter the repository.

The standalone wiki is different from `concepts/`: `concepts/` owns substantive Root Sequence concept treatments, while [`Root-Sequence/wiki`](https://github.com/Root-Sequence/wiki) helps readers recover names, project relationships, provenance, aliases, first-known appearances, and links to canonical homes across the wider ecosystem.

---

## 🔁 Flows

- **Concepts → Analysis** — definitions make diagnosis more precise.
- **Analysis ↔ Ideology** — material systems shape cultural stories; cultural stories reproduce or challenge systems.
- **Analysis → Systems** — diagnosis identifies what is happening; systems work asks how it behaves and propagates.
- **Founding texts ↔ Futures** — early values shape possible paths; imagined futures reveal tensions and limits in those orientations.
- **Systems ↔ Futures** — constraints, feedback, failure, and adaptation determine which futures are plausible.
- **Commons ↔ every layer** — public artifacts translate inquiry into usable forms and return feedback to the research.
- **Wiki ↔ every layer** — the standalone wiki tracks names, provenance, aliases, and project relationships so the rest of the ecosystem is easier to find without becoming a second canonical home.
- **Compost → Curiosity** — failed, superseded, partial, or contradictory work can become material for another sequence.

A useful routing sequence is:

```text
What is it?          → concepts
What is happening?   → analysis
Why is it justified? → ideology
How does it behave?  → systems
What could emerge?   → futures
What can be shared?  → commons
What shaped its values? → founding-texts
What is it called,
where is it, or how
did it evolve?       → Root-Sequence/wiki
```

When more than one answer seems plausible, place the full treatment at the narrowest scope that can maintain it and add short, deliberate routes from the other relevant areas.

---

## Systems layer

The systems layer focuses on what actually happens when structures meet real conditions rather than ideal assumptions.

Current recurring dynamics include:

- **fragility** — small failure, large consequence;
- **cascades** — failure propagating through connections;
- **recovery** — systems restoring or transforming function;
- **coherence** — alignment or misalignment among assumptions, signals, structure, and reality;
- **adaptation** — systems changing under stress;
- **emergence** — collective behavior or capacity arising from interactions among parts;
- **maintenance** — the often-invisible work that allows continuity;
- **power** — who can define goals, impose costs, block alternatives, or escape consequences.

The current [Systems Principles](systems/principles/README.md) are asymmetry, misclassification, feedback loops, reinforcement, and non-reversal.

“Emergence” should not function as a mystical explanation. Emergent outcomes still have mechanisms, participants, histories, power relations, and accountable consequences.

---

## Relationship to the wider ecosystem

Material should remain here when it is broad, cross-domain, or still searching for a narrower home.

It may later be transformed by:

- **Liberated Intelligence**, for intelligence, agency, ownership, and liberation;
- **UCF**, when explicitly developing or testing that framework;
- **Being Human(e)**, when translated into grounded, ordinary-life guidance;
- **Liberation Mass**, when expressed through shared gathering or practice;
- **Coherent World**, when applied to systemic speculative design;
- ***No One Noticed***, when made into plot, character, scene, or fiction canon;
- **the Museum of Ordinary Life**, when preserved as evidence of lived ordinary experience under its own consent and stewardship rules.

Prefer one canonical home plus links over copied documents that silently diverge.

> This map is compost too. Update it when the repository's actual structure or conceptual relationships change—not merely because one new note appears.
