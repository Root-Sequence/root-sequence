# Repository coherence audit

**Document role:** Audit record and cleanup change log<br>
**Status:** Active record<br>
**Audit date:** 2026-09-17<br>
**Reconciled with `main`:** 2026-09-18<br>
**Baseline:** `main` at `8b551209ea04d4ce5425d569565a2a9784fd463c`<br>

This audit covers the reader-facing Markdown, generated-site pages, directory indexes, navigation sources, and related publishing records in `Root-Sequence/root-sequence`.

It does not revise other repositories. Private or project-specific pages are named only when this repository needs to explain a boundary or route a reader to the canonical home.

## Architecture adopted

- [`README.md`](README.md) is the concise public front door.
- [`root_map.md`](root_map.md) is the canonical repository architecture and linking guide.
- [`ECOSYSTEM.md`](ECOSYSTEM.md) is the canonical organization-level project map.
- [`IDEA_TRAILS.md`](IDEA_TRAILS.md) explains recurring cross-project questions; [`IDEA_TRAIL_INDEX.md`](IDEA_TRAIL_INDEX.md) is generated from [`IDEA_TRAIL_GRAPH.yml`](IDEA_TRAIL_GRAPH.yml).
- Every content directory owns its local navigation through its `README.md`.
- Substantive pages keep one primary home. Historical summaries, project-specific transformations, migration pointers, generated pages, and validation records identify themselves instead of competing with that home.

The detailed canonical-page, linking, and status-label rules live in [`root_map.md`](root_map.md) so this audit does not become a second architecture specification.

## Coverage

The pass inspected:

- 156 Markdown files present at the baseline;
- the 11-page website candidate present at the audit baseline, followed by the approved single-page site merged to `main` on 2026-09-18;
- repository, directory, Idea Trail, and website navigation;
- the machine-readable Idea Trail graph and generated browser;
- the public agent-contact files and SECI research indexes;
- local and cross-repository links;
- the two open draft pull requests that overlap adjacent website and research work.

The repository was reviewed by role and directory, not only by searching for broken URLs. Long research pages were checked for scope, status, placement, and discoverability; short and legacy pages were checked for missing context, duplication, source debt, and malformed navigation.

## Findings and resolutions

### Empty and misleading pages

Fifteen tracked Markdown files were empty at the baseline. One, `systems/adaptation/README.md`, now provides a real local index. The remaining empty files were retired; their intended topics remain recorded as planned directions in the appropriate directory README instead of appearing as finished pages.

### Broken and ambiguous links

Relative links were repaired in the root README, concepts, core, commons, zines, Collapse Memory, and futures material. Old personal-account repository URLs were replaced with current Root Sequence homes. Directory indexes now use actual links instead of filenames formatted as code.

The previously linked `noonenoticed.world` domain could not be verified through either a direct request or a browser request during the audit. Public pages now route to the maintained Ecosystem description and identify the canonical workspace as private instead of presenting an unavailable public site as current.

### Duplicated or unclear canonical homes

- `core/` is no longer presented as one uniformly authoritative framework. Its index separates exploratory cycles and metaphors, manifestos and normative essays, and historical project orientations. The Liberation Cycle, Visibility Loop, and ecological project-cycle metaphor remain available without serving as repository architecture or universal causal claims.
- A follow-up architecture pass confirmed that the top-level `core/` name had become historical rather than descriptive. Its reader-facing role is now **Founding texts and early orientations**; current shared definitions, frameworks, design principles, and methods route to `concepts/`, while analytical principles and models route to `systems/`. Legible Systems moved canonically to `concepts/`, with its old path retained as a migration pointer.
- The nine-page `what-is-*` series mixed vocabulary, poetic fragments, political interpretation, personal reflection, and fictional mythology. Six recurring terms now share one scoped [`concepts/working-vocabulary.md`](concepts/working-vocabulary.md); the capitalism fragment was merged into its interpretive essay, Personal Anarchism moved to the founding/normative shelf, and the Auryn sketch was merged into the historical Liberated Intelligence overview. Duplicate Curiosity and Empathy cycle notes were retired after their distinct cautions were preserved in the vocabulary.
- Root-level Liberated Intelligence and UCF pages are retained as historical Root Sequence overviews and point to their dedicated canonical repositories.
- The two SECI entry layers are explicitly separated: the parent page defines the research umbrella; the nested README operates the active program.
- Collapse Memory and Auryn material now identifies its speculative or fictional status and does not present itself as practical emergency guidance or current fiction canon.

### Missing local navigation

Concepts, founding texts, commons fragments and zines, and systems subareas now link their developed pages. Empty application directories no longer masquerade as populated sections. Planned work is named without creating placeholder links.

### Status and evidence language

[`root_map.md`](root_map.md) separates document role, maturity, canonical scope, evidence status, and access. Pages touched in this cleanup use those meanings. Unsupported citation placeholders were converted into explicit evidence-work notes or removed from non-evidentiary manifestos rather than remaining as decorative footnotes.

The consolidated [Working Vocabulary](concepts/working-vocabulary.md) also labels each related destination by role and maturity, so readers can distinguish poetic fragments, developing systems work, historical manifestos, active indexes, and dedicated project repositories before following a link.

### Generated website

While this cleanup remained in draft, the separately reviewed single-page website was approved and merged to `main`. This branch incorporates that completed work without changing the approved [`site/index.html`](site/index.html), its approval digest, or its publication controls. The former 11-page candidate now lives under [`site/legacy-public-seed-v0.1/`](site/legacy-public-seed-v0.1/README.md) as historical source rather than deployment input.

The website remains an introductory projection, not a replacement for repository research or the Wiki. Obsolete cleanup edits to the former `site/content.json` were not carried into the historical archive. Only repository navigation and this audit record were reconciled with the new canonical site structure.

## Remaining work

This cleanup makes evidence debt visible; it does not invent sources or claim that every exploratory argument is established. Several older analysis, ideology, and futures pages still need source-by-source research review. That work should happen in bounded evidence passes and should preserve the distinction between observation, interpretation, metaphor, and normative claim.

Two draft pull requests remain separate by design:

- PR #6 develops the coherent-systems paper and should rebase or reconcile any shared navigation files before merge.
- PR #7 is the older isolated website editorial/accessibility prototype. The approved site now carries its central project-first and accessible-theme direction; do not merge the alternate review builder as a second website system. Preserve any still-useful review notes before closing it as superseded.

Neither draft was merged into this audit branch, and neither was treated as current published state.

## Verification record

The final branch was checked for:

- zero empty Markdown files across the final 140-file set;
- local Markdown links, local heading fragments, inbound Markdown navigation, and at least one readable top-level heading per reader-facing Markdown page;
- all 99 distinct GitHub repository or file destinations referenced by Markdown, JSON, or HTML through the GitHub API;
- current generated Idea Trail output;
- all 11 current website publication tests and a fresh preview build of the approved single-page source;
- the approved single-page site at narrow and wide viewport sizes, including navigation, controls, heading presence, and horizontal-overflow checks;
- representative external destinations, with access-denied responses recorded as inconclusive rather than silently treated as success;
- changed-file scope, whitespace integrity, valid JSON, and a full diff review.

See the draft pull request for the exact command results, limitations, and any unresolved external-link behavior.
