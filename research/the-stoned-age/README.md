# The Stoned Age

**Altered States, Human Curiosity, and the Long History of Making Meaning**

Companion provocation: **How Drugs Explain the Universe**.

**Status:** v0.1 local review suite · 13 October 2026 · AI-assisted · author, scholarly and cultural review pending. This is substantial first-edition production, not a completed scholarly monograph or reviewed release.

Open [the project](index.html), then choose:

- [Living research paper](paper/index.html), with [Markdown source](paper/manuscript.md).
- [Illustrated booklet](booklet/index.html), [16-page PDF](booklet/the-stoned-age.pdf), [Markdown](booklet/book.md) and [editable content](booklet/book.json).
- [Illustrated web essay](essay/index.html), with [Markdown source](essay/essay.md).
- [Talk](talk/index.html), [12-slide PDF](talk/the-stoned-age-talk.pdf), [25-minute outline](talk/outline.md) and [editable slide content](talk/slides.json).
- [Validation record](VALIDATION.md), [change record](CHANGELOG.md), [source register](research/sources.md), [machine-readable sources](research/sources.json), [claims ledger](research/claims.csv), [method and phased research agenda](research/methods.md).

## Exact proposed home

Repository: **Root-Sequence/root-sequence**. Directory: **research/the-stoned-age/**. The files here are the proposed contents of that directory, including `paper/`, `booklet/`, `essay/`, `talk/`, `research/`, `assets/` and `tools/`. The nested `research/` contains evidence records for this inquiry, not a second organizational research hub.

Rationale: the live root README, PROJECT-CONTEXT, research index, research method, root map and ecosystem map identify this repository as the umbrella inquiry and research coordinator. Existing focused inquiries demonstrate that a bounded research area can live here without claiming a separate institution or novel expertise. No existing Stoned Age/psychedelic/altered-state treatment was found in the inspected main tree or the targeted issue search.

Audit base: main commit `5ba3593f9d1b335e9fbe29ee85eeb77e3a9d1b42`, cloned clean on 2026-10-13. Only a fresh local checkout was edited. Connected repository listing was partial, so it is not treated as an exhaustive organizational census; the canonical live ECOSYSTEM map supplied the broader ownership map. Open PRs #40–44 were inspected at summary level. #42 and #44 also touch research navigation; rebase/reconcile that index before applying this patch remotely.

The proposed nearest-index addition is in the accompanying repository patch. The suite creates no new top-level architecture or cross-project ownership. No changes are needed to the public homepage, private projects or fictional canon. A later Wiki entry should be a pointer, if requested, not a duplicated substantive home.

## Publication boundary

Nothing has been pushed, merged or deployed. The repository's `research/README.md` states: “Website presentation is separate and requires an explicit publication pass.” A public branch or draft PR is itself public. The package is ready for review before approving those external actions. Existing homepage approval does not apply to this essay.

## Provenance and contribution

The user supplied the title, subtitle, companion framing, scope, humor and instruction to make a substantial suite, building on the conversation titled Drug Origins Theory. That conversation was read through the connected tool. Some assistant turns were content-reference placeholders and the original image was not reconstructed or reused.

AI assistance supplied the structure, source discovery, interpretive synthesis, prose drafts, diagrams, formats and checks. These additions are not attributed as the user's approved conclusions. No human domain reviewer, Indigenous consultation, experiment or data reanalysis is claimed. The paper itself discusses the risk that fluent synthesis can exceed evidence.

## Source and media reuse

All illustrations are original editable SVG conceptual diagrams, generated from `tools/build.py`; no third-party photographs, sacred motifs or historical reconstructions are used. The project sources are offered under CC0 1.0 consistently with the target repository. Source publications, linked pages, names and third-party research remain subject to their own rights. Their inclusion in the bibliography does not confer endorsement.

## Build and accessibility

The HTML and SVG outputs work offline without JavaScript, external fonts, accounts or analytics. Open `index.html` locally. Semantic headings, keyboard links, visible focus, a skip link, responsive widths and reduced-motion handling are included. HTML is the accessible reading edition; PDFs are not claimed to be fully tagged or PDF/UA conformant.

Rebuild from this directory with `python3 tools/build.py`. HTML/SVG generation uses the Python standard library. PDF generation additionally needs `reportlab`; without it the script generates HTML/SVG and reports the missing PDF dependency. The small renderer supports the formats used here, not arbitrary Markdown. JSON is the authoritative booklet/slide content; Markdown is the paper/essay source. The booklet Markdown is an editorial companion; keep it aligned when changing JSON content.

## Release phases

1. **Delivered: v0.1 review suite.** Four reader formats, shared citations, claims ledger, original diagrams and additive patch.
2. **Next: evidence depth.** Full study extraction and expert critique before stronger historical, clinical or evolutionary claims; prioritized details in the method record.
3. **Then: cultural chapters and revised editions.** Appropriately situated authorship and review, with clear consent and reuse terms.
4. **Publication pass.** Approve a public draft PR and, separately, a deployment destination. No new repository or hosting account is necessary for this low-maintenance static suite.

A phase is complete when its evidence or review work is complete, not merely when more pages exist.
