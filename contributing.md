# Contributing to Root Sequence

Root Sequence welcomes writing, research, critique, art, design, code, translation, and careful connective work.

This repository is the **public conceptual commons**, not the whole Root Sequence organization. Contributions should strengthen this repository's broad systems inquiry or help readers navigate it. Project-specific work belongs with the project that can maintain it.

Contribute in a spirit of curiosity rather than doctrine: make the scope of a claim visible, preserve meaningful disagreement, and leave room for revision.

## Start here

Before proposing a substantial change, read the smallest set of maps that answers your question:

- [`README.md`](README.md) — the public front door;
- [`root_map.md`](root_map.md) — repository structure, canonical-page rules, and status language;
- [`ECOSYSTEM.md`](ECOSYSTEM.md) — project boundaries and canonical homes across the organization;
- [`THOUGHT_ROUTING.md`](THOUGHT_ROUTING.md) — how to capture an idea once and route it without duplicating the substance;
- [`IDEA_TRAILS.md`](IDEA_TRAILS.md) — recurring questions that connect work across projects.

Search the repository's existing files, [issues](https://github.com/Root-Sequence/root-sequence/issues), and [pull requests](https://github.com/Root-Sequence/root-sequence/pulls) before creating a parallel treatment.

## Choose the right contribution path

| If you want to… | Use… |
|---|---|
| fix or extend material in this repository | an issue or pull request in `Root-Sequence/root-sequence` |
| ask where an idea belongs, or discuss something spanning projects | [Root Sequence Discussions](https://github.com/orgs/Root-Sequence/discussions), usually **Orientation & Q&A** or **Ideas & Open Questions** |
| add a short definition, alias, provenance note, or project relationship | the [Root Sequence Wiki](https://github.com/Root-Sequence/wiki) |
| change a specific project, implementation, gathering practice, archive, or work of fiction | the canonical project named in [`ECOSYSTEM.md`](ECOSYSTEM.md) |
| report a privacy or safety concern that should not be public | the [maintainer contact page](https://raearea.net/contact) |

When the destination is unclear, begin with a discussion rather than creating a new top-level file or folder.

## What belongs in this repository

Use the narrowest appropriate maintained home:

- [`concepts/`](concepts/README.md) — shared definitions, cross-project frameworks, design principles, and methods;
- [`systems/`](systems/README.md) — analytical principles, models, and methods for system behavior;
- [`analysis/`](analysis/README.md) — diagnosis of power, infrastructure, political economy, surveillance, and related conditions;
- [`ideology/`](ideology/README.md) — myths, philosophies, and narratives that justify or contest power;
- [`futures/`](futures/README.md) — trajectories, alternatives, collapse, resilience, and possible liberations;
- [`founding-texts/`](founding-texts/README.md) — founding manifestos, early models, normative essays, and historical orientations;
- [`commons/`](commons/README.md) — public and reusable artifacts such as zines, maps, practices, and deliberate fragments;
- [`site/`](site/README.md) — the approved introductory website projection, not a second research canon.

Raw notes that are not ready for public reading should remain in a temporary capture system. Deliberately unfinished, poetic, or compostable public material belongs in [`commons/fragments/`](commons/fragments/), with its role made clear.

## Ways to contribute

- **Research and sources** — strengthen factual grounding, identify evidence gaps, or challenge unsupported claims.
- **Writing and editing** — clarify arguments, add context, improve structure, or make language more accessible.
- **Connections and routing** — repair navigation, identify duplication, or connect related work without copying it.
- **Visual and sonic work** — contribute diagrams, illustrations, layouts, readings, sound, or other public artifacts with appropriate attribution and licensing information.
- **Code and interfaces** — improve the website, validation tools, indexes, accessibility, or small experimental interfaces.
- **Translation** — adapt material across languages, cultures, or modalities while recording the source and meaningful interpretive choices.
- **Critique and alternatives** — document limitations, counterexamples, contested interpretations, or models that do not fit.

## Canonical homes and boundaries

- Give substantive material one maintained canonical home. Other pages should summarize briefly and link to it.
- Do not copy private repository material, unpublished fiction canon, participant or contributor data, credentials, security details, or sensitive archival material into this public repository.
- Do not treat a cross-project resemblance as proof that every project shares one model or conclusion.
- Do not let fiction override the consent, identity, governance, or provenance of a real person, community, institution, or archive.
- Respect the license and attribution requirements of external sources. This repository's CC0 license does not erase someone else's rights.
- Preserve superseded or contested work through history, status notes, or deliberate archival treatment rather than silently erasing it.

## Make status and evidence legible

Use the distinctions in [`root_map.md`](root_map.md) when readers could otherwise misread a page:

- **document role** — what job the page performs;
- **status or maturity** — how current or developed it is;
- **canonical scope** — what material it primarily maintains;
- **evidence status** — whether a claim is observed, supported, hypothetical, interpretive, normative, metaphorical, or open;
- **access** — whether a referenced destination is public, private, or unpublished.

Not every page needs every label. Add the context required to prevent a draft from looking settled, a metaphor from looking empirical, or a project-specific claim from looking universal.

## GitHub workflow

1. Fork the repository or clone it locally.
2. Create a focused branch, such as `docs/clarify-feedback-loops` or `commons/new-zine`.
3. Make the smallest coherent change that preserves existing substantive ideas.
4. Update the nearest relevant README or index when readers could otherwise miss or misunderstand the change.
5. Run the relevant validation checks.
6. Open a pull request explaining what changed, why it belongs here, what you verified, and what remains uncertain.

Draft pull requests are welcome when the direction is useful but wording, evidence, placement, or scope still needs discussion.

If GitHub is unfamiliar, ask for orientation in [Root Sequence Discussions](https://github.com/orgs/Root-Sequence/discussions). You do not need to understand the whole ecosystem before asking a question.

## Citations and attribution

This repository generally uses Markdown footnotes for references.

```markdown
Liberation is always recursive.[^1]

[^1]: Murray Bookchin, *The Ecology of Freedom* (1982).
```

- Cite factual or research-dependent claims with sources appropriate to the claim.
- Keep quotations accurate and short enough to respect the source's rights.
- Put references at the bottom of the file under `## References` when the page uses them.
- Distinguish what a source establishes from your interpretation or extension of it.
- Record attribution, license, and source information for media and remixed work.
- If research is still needed, name the evidence gap instead of adding a decorative placeholder citation.

Citations are invitations into the roots of an idea, not a substitute for explaining it clearly.

## Documentation coherence

When a canonical idea, project relationship, architecture, path, or current priority changes, check the documents that help readers discover and correctly understand it.

As applicable, update:

- the nearest README or local index;
- affected links and migration pointers;
- [`root_map.md`](root_map.md) when repository architecture changes;
- [`ECOSYSTEM.md`](ECOSYSTEM.md) when project boundaries or canonical homes change;
- Idea Trail sources when a recurring cross-project relationship changes;
- status, roadmap, or decision records that would otherwise become misleading.

Do not repeat the same explanation everywhere. The goal is **coherence without duplication**.

Before submitting reader-facing changes, run:

```sh
python3 cli/check_reader_docs.py
python3 cli/generate_idea_trail_index.py --check
python3 site/test_site.py
```

The documentation check validates local files, headings, links, and discoverability. It does not verify external URLs or the evidence behind a claim; record those checks separately when they matter.

## Licensing

Root Sequence is released under [CC0 1.0](license). By submitting material, you confirm that you have the right to contribute it under that license. Do not submit work copied from a source whose terms are incompatible with CC0.

Thank you for helping the work become clearer, more grounded, more connected, and easier to navigate.
