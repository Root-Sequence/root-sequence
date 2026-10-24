# The Stoned Age

**Altered States, Human Curiosity, and the Long History of Making Meaning**

Companion provocation: **How Drugs Explain the Universe**.

**Status:** v0.1.2 public draft suite · 24 October 2026 · AI-assisted · author, scholarly and cultural review pending. It remains a working inquiry, with the evidence and review limits recorded below.

Open [the project](index.html), then choose:

- [Living research paper](paper/index.html), with [Markdown source](paper/manuscript.md).
- [Illustrated booklet](booklet/index.html), [16-page PDF](booklet/the-stoned-age.pdf), [Markdown](booklet/book.md) and [editable content](booklet/book.json).
- [Illustrated web essay](essay/index.html), with [Markdown source](essay/essay.md).
- [Talk](talk/index.html), [12-slide PDF](talk/the-stoned-age-talk.pdf), [25-minute outline](talk/outline.md) and [editable slide content](talk/slides.json).
- [Validation record](VALIDATION.md), [change record](CHANGELOG.md), [source register](research/sources.md), [machine-readable sources](research/sources.json), [claims ledger](research/claims.csv), [method and phased research agenda](research/methods.md).

## Exact proposed home

Repository: **Root-Sequence/root-sequence**. Directory: **research/the-stoned-age/**. The files here are the proposed contents of that directory, including `paper/`, `booklet/`, `essay/`, `talk/`, `research/`, `assets/` and `tools/`. The nested `research/` contains evidence records for this inquiry, not a second organizational research hub.

Rationale: the live root README, PROJECT-CONTEXT, research index, research method, root map and ecosystem map identify this repository as the umbrella inquiry and research coordinator. Existing focused inquiries demonstrate that a bounded research area can live here without claiming a separate institution or novel expertise. No existing Stoned Age/psychedelic/altered-state treatment was found in the inspected main tree or the targeted issue search.

Audit base: main commit `5ba3593f9d1b335e9fbe29ee85eeb77e3a9d1b42`, cloned clean on 2026-10-13. The draft was prepared in a fresh local checkout. Connected repository listing was partial, so it is not treated as an exhaustive organizational census; the canonical live ECOSYSTEM map supplied the broader ownership map. Open PRs #40–44 were inspected at summary level. #42 and #44 also touch research navigation; reconcile that index before merging.

The proposed nearest-index addition is in the accompanying repository patch. The suite creates no new top-level architecture or cross-project ownership. No changes are needed to the public homepage, private projects or fictional canon. A later Wiki entry should be a pointer, if requested, not a duplicated substantive home.

## Publication boundary

Public draft [PR #45](https://github.com/Root-Sequence/root-sequence/pull/45) is open. Merge and deployment remain pending. The draft now proposes publishing the reading editions at `https://rootsequence.systems/stonedage/`, following Rae's suggestion. The combined site publisher requires a separate exact-source hosting approval; its approval record is pending. Merging this branch alone does not satisfy that gate or approve research findings.

## Provenance and contribution

The user supplied the title, subtitle, companion framing, scope, humor and instruction to make a substantial suite, building on the conversation titled Drug Origins Theory. That conversation was read through the connected tool. Some assistant turns were content-reference placeholders and the original image was not reconstructed or reused.

AI assistance supplied the structure, source discovery, interpretive synthesis, prose drafts, diagrams, formats and checks. These additions are not attributed as the user's approved conclusions. No human domain reviewer, Indigenous consultation, experiment or data reanalysis is claimed. The paper itself discusses the risk that fluent synthesis can exceed evidence.

## Source and media reuse

All illustrations are original editable SVG conceptual diagrams, generated from `tools/build.py`; no third-party photographs, sacred motifs or historical reconstructions are used. The project sources are offered under CC0 1.0 consistently with the target repository. Source publications, linked pages, names and third-party research remain subject to their own rights. Their inclusion in the bibliography does not confer endorsement.

## Build and accessibility

The HTML and SVG outputs work offline without JavaScript, external fonts, accounts or analytics. Open `index.html` locally. Semantic headings, keyboard links, visible focus, a skip link, responsive widths and reduced-motion handling are included. HTML is the accessible reading edition; PDFs are not claimed to be fully tagged or PDF/UA conformant.

Rebuild from this directory with `python3 tools/build.py`. HTML/SVG generation uses the Python standard library. PDF generation additionally needs `reportlab`; without it the script generates HTML/SVG and reports the missing PDF dependency. The small renderer supports the formats used here, not arbitrary Markdown. JSON is the authoritative booklet/slide content; Markdown is the paper/essay source. The build regenerates the booklet Markdown and talk outline from JSON.

## Release phases

1. **Delivered: v0.1 review suite.** Four reader formats, shared citations, claims ledger, original diagrams and additive patch.
2. **In progress: evidence depth.** Full study extraction and expert critique before stronger historical, clinical or evolutionary claims; prioritized details in the method record.
3. **Then: cultural chapters and revised editions.** Appropriately situated authorship and review, with clear consent and reuse terms.
4. **Publication pass.** Review the open public draft PR and approve a deployment destination separately. No new repository or hosting account is necessary for this low-maintenance static suite.

A phase is complete when its evidence or review work is complete, not merely when more pages exist.

## Evidence revision

The [source-by-source appraisal](research/appraisal.md) covers all 16 records, distinguishes inspected material from remaining gaps, and records the creativity correction carried through all four editions. Crossref returned 13 of 14 DOI records in this pass; one was rate-limited. Full scholarly appraisal remains incomplete, particularly S01 access and supplements/registrations.

## Review checkpoint: 24 October 2026

This draft incorporates main through #44 and preserves the existing public introduction and privacy fixes. Its research-index entry replaces the old draft-queue pointer. The playful framing and the distinction between findings, hypotheses and editorial proposals remain.

The creativity wording now names placebo as the follow-up comparator across the paper, booklet, essay, talk and claims ledger. The paper and appraisal also distinguish that comparison from within-group improvement. S15 links to the specific 2023 preprint version inspected. The [appraisal follow-up](research/appraisal.md#review-follow-up-24-october-2026) records this pass's selected source checks; it does not replace the earlier appraisal or complete scholarly/cultural review.

All reader editions expose an Evidence notes route. PDF builds now use stable generation metadata so unchanged inputs can reproduce the same files. The [validation record](VALIDATION.md) distinguishes technical checks from remaining research and accessibility work. No homepage, hosting configuration, private project or fictional canon is changed.

## Proposed website route: 24 October 2026

The subsequent route proposal reuses these editions under `/stonedage/`, with a link back to Root Sequence. The [site publisher](../../site/build_research.py) copies an explicit set of reading files and sends other source links to GitHub. This adds no second research home. Its preview remains local; its proposed Pages workflow and publication gate are documented in the [site guide](../../site/README.md#proposed-research-route-24-october-2026). The existing paper, source appraisal and evidence limits remain unchanged.
