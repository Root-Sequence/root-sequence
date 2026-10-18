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

- The former `core/` area mixed exploratory cycles and metaphors, manifestos and normative essays, historical project orientations, and one current design principle. The Liberation Cycle, Visibility Loop, and ecological project-cycle metaphor remain available without serving as repository architecture or universal causal claims.
- A follow-up architecture pass confirmed that the top-level `core/` name had become historical rather than descriptive. Founding and historical material now lives under [`founding-texts/`](founding-texts/README.md); current shared definitions, frameworks, design principles, and methods route to [`concepts/`](concepts/README.md); and analytical principles and models route to [`systems/`](systems/README.md).
- A directory-naming pass moved the founding material physically to `founding-texts/`, renamed `systems/core/` to `systems/principles/`, and moved Legible Systems canonically to [`concepts/legible-systems.md`](concepts/legible-systems.md). After the current website link was updated, the obsolete top-level `core/` compatibility directory was removed. Path naming rules in [`root_map.md`](root_map.md) now favor descriptive current roles and lowercase kebab-case over inherited labels such as `core` or `framework`.
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

While this cleanup remained in draft, the separately reviewed single-page website was approved and merged to `main`. This branch incorporates that completed work, then updates its Legible Systems source link and source-overlay recognition to use the canonical [`concepts/legible-systems.md`](concepts/legible-systems.md) path. The corresponding approval digest and inline-script security hash were updated; site copy and layout were not changed. The former 11-page candidate remains under [`site/legacy-public-seed-v0.1/`](site/legacy-public-seed-v0.1/README.md) as historical source rather than deployment input. Its two source links to retired `core/` paths are pinned to the last published commit that contained those files.

The approved site now expands its Selected Research section with [Intelligence Ecology](concepts/intelligence-ecology.md), [Events, Patterns, and Scale](systems/events-patterns-and-scale.md), and [Resilience and Graceful Degradation](systems/resilience-and-graceful-degradation.md). The exact-source approval and publication checks were updated after Rae reviewed the six-item selection.

The website remains an introductory projection, not a replacement for repository research or the Wiki. Obsolete cleanup edits to the former `site/content.json` were not carried into the historical archive. Only repository navigation and this audit record were reconciled with the new canonical site structure.

## Remaining work

This cleanup makes evidence debt visible; it does not invent sources or claim that every exploratory argument is established. Several older analysis, ideology, and futures pages still need source-by-source research review. That work should happen in bounded evidence passes and should preserve the distinction between observation, interpretation, metaphor, and normative claim.

Post-audit follow-up on 2026-09-18 retired both pre-cleanup pull requests
without merging their outdated structures:

- PR #7 was closed after its useful project-first and accessibility direction
  had been incorporated into the approved single-page website.
- PR #6 was closed after [PR #13](https://github.com/Root-Sequence/root-sequence/pull/13)
  preserved its twelve-file coherent-systems paper package on a fresh branch
  from current `main`, repaired retired paths, and reconciled its useful
  cross-domain additions with their canonical pages. The paper remains
  `v0.1-dev`, AI-assisted, author review pending, and not approved for release.
  Rae approved the technical preservation and routing work on 2026-09-18; that
  approval does not extend to the manuscript's claims or publication.

The separate Wiki's former Legible Systems routes were corrected by merged
[Wiki PR #1](https://github.com/Root-Sequence/wiki/pull/1). Merged
[Wiki PR #2](https://github.com/Root-Sequence/wiki/pull/2) later added the
Root Sequence name and provenance entry.

## Verification record

The final branch was checked for:

- zero empty Markdown files across the final 139-file set;
- local Markdown links, local heading fragments, inbound Markdown navigation, and at least one readable top-level heading per reader-facing Markdown page;
- all 99 distinct GitHub repository or file destinations referenced by Markdown, JSON, or HTML through the GitHub API;
- current generated Idea Trail output;
- all 11 website publication checks and fresh preview and approved release builds of the expanded Selected Research source;
- the approved Selected Research section at narrow and wide viewport sizes, including all six entries, contextual link details, controls, heading presence, and horizontal-overflow checks;
- representative external destinations, with access-denied responses recorded as inconclusive rather than silently treated as success;
- changed-file scope, whitespace integrity, valid JSON, and a full diff review.

See the draft pull request for the exact command results, limitations, and any unresolved external-link behavior.


## Professional refresh audit: 2026-10-17

**Scope:** current GitHub organization, public registry, canonical site source, target repository structures/context, outstanding work, and publication boundaries. This is a documentation and positioning audit, not scientific validation or a security review. Progress lives only in [ROADMAP.md](ROADMAP.md).

### Inventory and source authority

The live organization listing returned 15 repositories, all with `main` as default. Visibility was checked live. Public-safe role descriptions below come from the existing [organization registry](https://github.com/Root-Sequence/.github/blob/main/PROJECT_REGISTRY.yml) and public source. Private contents were inspected for boundaries but are not reproduced here.

| Repository | Visibility | Existing role / treatment in this refresh |
| --- | --- | --- |
| `root-sequence` | public | Conceptual commons and research coordination; owns this checklist and the canonical `site/` source. |
| `.github` | public | Organization profile, registry, contribution and stewardship defaults. |
| `liberated-intelligence` | public | Focused intelligence, agency, ownership, and non-domination inquiry. |
| `universal-coherence-framework` | public | Optional analytical framework; no universal validation claim. |
| `beinghumane-guide` | public | Public field-guide writing; separate from its private workbench. |
| `liberation-mass` | public | Embodied gathering and shared practice. |
| `existential-euphoria` | public | In-formation experiential/aesthetic work; no scope change or hold release. |
| `root-sequence-discussions` | public | Cross-project conversation and routing. |
| `wiki` | public | Names, provenance, relationships, and routes; not a duplicate research home. |
| `coherent-world` | private | Speculative systems, simulation, and narrative; retain project-local authority. |
| `coherent-computing` | private | Concept-first operating-system inquiry; retain project-local plan and gates. |
| `community-infrastructure` | private | Community-controlled systems research/design. |
| `beinghumane-atlas` | private | Editorial/research workbench; no automatic public export. |
| `wiki-private` | private | Private routing overlay. |
| `good-chaos-music` | private | Fictional music work; separate release decisions. |

Verified public base commits: `root-sequence` **5ba3593f9d1b335e9fbe29ee85eeb77e3a9d1b42**; `.github` **1f53db3ce3da497c402e5b076502ccffb089d71c**. The private target trees, READMEs, short introductions, and project context were checked through the connected GitHub service. Public projections use already-public descriptions, not private research details or evidence records.

`site/index.html` is the authoritative one-file page, with an exact-source publication gate in `site/build.py` and `site/approval.json`. Its approved September 25 edition supplies the structure, green palette, headline, wordmark, controls, selected research, and project panels for this refresh. A README contained contradictory approval/candidate statements; this refresh reconciles them around the unapproved new candidate.

### Outstanding work and reuse

There were **28 open PRs** organization-wide at audit time. All titles and descriptions were inspected for relevance. Changed-file lists were inspected for all **14 open PRs across the four target repositories**; deeper research review is not claimed. Branch listings were checked for those same four repositories. Closed historical branches were not treated as new work.

| Existing public work | Treatment / overlap |
| --- | --- |
| [root-sequence #40](https://github.com/Root-Sequence/root-sequence/pull/40), anticipation/surprise | Preserve current draft; no changes to its systems/concept files. |
| [#41](https://github.com/Root-Sequence/root-sequence/pull/41), representational legibility | Preserve canonical Legible Systems work; link current `main`, do not copy pending arguments. |
| [#42](https://github.com/Root-Sequence/root-sequence/pull/42), agency under stress | Reuse through a labelled draft route. Shares `research/README.md`; reconcile index additions before merge. |
| [#43](https://github.com/Root-Sequence/root-sequence/pull/43), commons collaboration | Preserve substantive `commons/README.md`. Shares root README; reconcile its commons navigation with the mission edit. |
| [#44](https://github.com/Root-Sequence/root-sequence/pull/44), intelligence without omniscience | Reuse through its existing draft PR; preserve notes, claims, graph, and lineage work. Shares research index. |
| [#45](https://github.com/Root-Sequence/root-sequence/pull/45), The Stoned Age | Reuse source/appraisal/claims package through its draft PR. Do not duplicate its paper, booklet, essay, or talk. Shares research index. |
| [.github #9](https://github.com/Root-Sequence/.github/pull/9), commons contribution/stewardship | Shares `profile/README.md`; preserve its canonical commons routing and reconcile profile text during review. It has a different substantive scope and is not silently replaced. |
| [.github #5](https://github.com/Root-Sequence/.github/pull/5), Commons of Inquiry registry seed | Registry-only; no registry or institutional-status change in Phase 1. |

The named `site-accessibility-editorial-review` branch adds a separate five-file review generator tied to an older multi-page candidate. It is not the current authoritative site and is not adopted as a second publishing system. The earlier `docs/clarify-org-profile-2026-09-18` and site README context-fix branches add no outstanding diff against current `main`. The earlier repository-coherence audit branch also adds no outstanding diff against current `main`.

Research drafts keep one substantive home. New material in `research/work-samples/` is explicitly a transformed proposal-development exercise, with links to existing sources and actual assistance/review limits.

### Baseline checks and practical findings

- Untouched base: **11/11 site checks passed**.
- Untouched base: reader-document checker reports **15 errors**, comprising one broken relative link and fourteen missing inbound links in living-paper notes. These are pre-existing, not introduced by this refresh. Fixing that paper requires its scoped instructions and a separate pass.
- Default and bundled Python lack PyYAML; the existing isolated validation environment supplies it for the generated Idea Trail index check. No project dependency change is needed.
- The organization bio read “A systems-oriented lab exploring root structures and unfolding sequences shaping systems, intelligence, technology, and reality.” at the initial audit. Rae has since approved the replacement wording below; live settings have not been changed.
- Current site links and research entry points already provide a useful baseline. Improve identity, claim-status visibility, and disclosure within that structure.

### Refresh compatibility review: 2026-10-17

After the six homepage descriptions completed passage review, the live heads and shared-file patches were checked again. All named PRs remain open, draft, and unmerged. `main` still points to the public base commits recorded above.

Local compatibility checks used Git's tree-only merge calculation. They created temporary Git objects and local review refs; they did not merge a branch, change either working tree, or update any existing research/commons PR. Each calculation compared the refresh with one older draft independently; this does not establish compatibility among all older drafts combined or approve their substance.

| Draft compared with refresh | Inspected head | Shared work | Result / retained intent |
| --- | --- | --- | --- |
| root #42 | `6329bfea8b9d25a3bf5845046f3313f17d063b57` | Research index | No textual conflict. Preserve its bounded agency-under-stress entry when that research is reviewed; keep the current labelled PR route while it remains unmerged. |
| root #43 | `6097553039e985d94a6460ea57fe105d38045f94` | Root README | No textual conflict. Its commons-proposal paragraph is an addition, not a replacement for the independent-research mission. |
| root #44 | `00f14ffd8fb8bffc0c551e1bab88b64c1f5c58b2` | Research index | No textual conflict. Preserve the research-area route and companion inquiries if that draft is later approved. |
| root #45 | `30748ee8db9bfde29fc0312a41b8f04edd98340d` | Research index | No textual conflict. Preserve its source/claim package in its existing home; a merged index route would replace its entry in the draft-only queue. |
| organization #9 versus #10 | #9 `e95fda37278b0b1f4d5a03be219f0bcf078d556c`; #10 `8989e7f156f6b2e9e9923eafe3c3d67d9c30abe9` | Organization README and profile | The README additions coexist. `profile/README.md` has a textual conflict between the rewritten introduction and the older commons paragraph. |

The root calculations used refresh head `d735d657fb3bd917c84e70ddea36e09414fc0782`, immediately before the Reading Trails wording update. That update changes only the last site's research description and its records, outside the older drafts' files.

**Profile resolution proposed for the next review:** retain #10's independent-research introduction and current project boundaries. Keep the commons proposal clearly labelled and linked to root #43 while it remains a draft, and fold #9's short profile-level invitation into that existing paragraph rather than appending a second overview. Preserve #9's substantive contribution/stewardship documents in their own review. Its links to the future `main` commons anchor require root #43 to land first, or a temporary route to that PR; neither dependency is resolved by this refresh.

The check itself did not close, rebase, or overwrite an older PR. The remaining profile conflict was resolved in the subsequent draft update below. Before any eventual merge, rerun compatibility checks on the then-current heads and check the research queue for duplicate or newly merged routes. Compatibility does not approve publication.

### Organization profile overlap resolved: 2026-10-17

The professional-refresh profile in organization #10 now contains one concise collaboration summary. It retains the independent-research mission and existing project boundaries, routes to the review-pending commons proposal, and keeps maintenance responsibility and decision powers provisional. Previously approved mission, research-method, evidence, and AI/accessibility passages are preserved verbatim. The new collaboration summary is prepared for PR review; it is not recorded as a separately approved passage.

The redundant profile-only paragraph has been removed from organization #9’s diff by restoring that file to its existing base version. Its four substantive guidance files (`README.md`, `CONTRIBUTING.md`, `PROJECT_STEWARDSHIP.md`, and `PULL_REQUEST_TEMPLATE.md`) remain byte-for-byte identical to #9’s original head. This preserves their separate review instead of including governance proposals in the professional refresh. The earlier profile wording remains recoverable in Git history.

Updated draft heads: #9 `36527befd9f1f5576966940e9b57ef7aa194167f`; #10 `71753723acc549d6014bd6170ed9d6ffe514cf43`. A fresh tree-only merge of those heads completes without a conflict. It preserves #10’s profile, both README additions, and all three other contribution/stewardship files. Neither branch is merged to `main`, force-updated, or closed. This does not adopt either proposal as operating governance.

The original #9 guidance still links to a proposed canonical commons anchor. Root #43 must be reviewed and accepted before those `main`-anchor links can resolve. That dependency remains explicit in #9’s description; resolving the profile conflict does not bypass it. Root research drafts #42, #44, and #45 also remain separately reviewable. Their substantive material has not been copied into the refresh.

### Proposed short organization bio

> Independent interdisciplinary research exploring how intelligence, technology, and social systems shape one another.

Rae approved this exact sentence from writing block `61582` on **2026-10-17 (Pacific)** by responding “indeed.” It reuses the agreed mission. The heading remains stable for existing links. Wording approval and a later live-settings change remain separate; no live bio change has been made. It does not assert an incorporated institute, funded team, academic affiliation, AIAF connection, completed study, or deployed product.

### Review boundary

Prepare two linked draft source PRs: the canonical repository/site/plan and the organization profile. Private projects remain in their own repositories. Do not merge, deploy, update live settings, release a held project, or overwrite `site/approval.json`. The existing Pages workflow runs on a merge to `main`; the candidate's release digest remains deliberately unapproved. Check [ROADMAP.md](ROADMAP.md) for final validation and review links.
