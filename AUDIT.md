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

## Website publication and organization README consistency: 2026-10-19

Rae explicitly approved website publication after reviewed source commit `0780c6d3ce846680b4485330df3e1dc0af1084bf`: “Website changes approved. Publish and continue with org readme consistency etc.” The approved page/publisher source was isolated in [website-only PR #47](https://github.com/Root-Sequence/root-sequence/pull/47), based on main `5ba3593f9d1b335e9fbe29ee85eeb77e3a9d1b42`, and merged as `b179a7fa56252dfd9fefbb3f93dcf1a9e1dd3ec6`. Only eight `site/` files changed. No research, portfolio, organization profile, workflow, DNS, mail, private source, or fictional canon was merged.

The page and publisher match the reviewed source digest `8dcd150886446fe180c985b87cc8f913b5d920ad81d8d422de208e46d634847e`; preview HTML is `b532f50c0b875f762d695a6d872553983d733d6209e360383ab64776be08eb36`. The explicit approval is recorded in `site/approval.json`. All 11 local publication checks pass, including rejection of missing, historical, and changed-source approval. The only approval-specific test update replaces the candidate-only rejection assertion with a current-record match and explicit historical rejection fixture. Other tests retain their previous checks. The approved release uses only the existing publication-state substitutions.

[Pages run 39211072192](https://github.com/Root-Sequence/root-sequence/actions/runs/39211072192) completed successfully. HTTPS `https://rootsequence.systems/` returns HTTP 200; `https://www.rootsequence.systems/` resolves to that same canonical URL. Both HTML responses match the local generated release SHA-256 `11688c47ffdde09879de721d6fe0982d2bc596ffaa5f0680334d05cd354cce8f`. The public manifest matches the approved source/release hashes and reviewer/date. Live robots.txt matches the generated indexable version. A browser load at 1575 × 897 shows the current mission and dark layout, `index,follow`, published footer, and no horizontal overflow. These checks verify this release, not all external project destinations or full accessibility conformance.

The remaining professional-refresh branch incorporates published main with all `site/` files retained exactly from main. This prevents a later documentation merge from restoring the obsolete approval gate or preview state. The canonical checklist remains `ROADMAP.md`; it is not duplicated into another planning location.

[Organization draft #10](https://github.com/Root-Sequence/.github/pull/10), head `7d772afaef9e99c089e1189f2148b1d6f9ff790e`, aligns the mission/About invitation with the approved site, retains the contextual founder and credit, expands its curated table to the same six research routes with the approved limits, and reuses all seven project descriptions with useful development/consent notes. Computing now covers computing systems and device lifecycle beyond operating-system design. The Museum’s independent status and real/archive-fiction permission boundary remain. Methods, evidence, and substantive AI/accessibility contributions are retained in one native disclosure. Existing wider-project routes and the pending commons proposal remain. The fuller accessibility link now targets the existing public assistance-record heading, avoiding a draft-only research-README fragment; Discussions uses the same public route as the site.

Checked all eleven unique linked root-sequence main file/fragment destinations against the public tree. The rendered GitHub draft shows six research entries and the approved project descriptions; keyboard opening of the methods disclosure reveals the retained contribution/evidence text. No private-project addresses or diagnosis disclosure were added. The org PR still changes only `README.md` and `profile/README.md`. Organization #9 head `36527befd9f1f5576966940e9b57ef7aa194167f` is unchanged, preserving the earlier ownership split; no substantive policy file was changed here. The README is saved for user review, not merged or applied to the live profile/bio. Writing follows the approved passages and explicit style preferences; a writing-reference retrieval tool was unavailable, so no retrieved personal-style match is claimed.

Publication completes P1-05; the prepared README consistency draft completes P1-10. P1-11 records review/publication of remaining documentation separately from applicant samples, which still await P2-04. Broader reader-document failures retain the earlier 15-error baseline; no new full-documentation audit or Wiki freshness/transfer work is claimed.

## Public repository cleanup: 2026-10-23

**Scope:** current public introductions, navigation, source-status wording, registry visibility, existing PR overlap, and publication candidates. This is an editorial/structural cleanup, not research validation, policy adoption, or legal review. [ROADMAP.md](ROADMAP.md) remains the only progress checklist.

The live accessible inventory contains 15 repositories: eight public and seven private. All 34 open-PR summaries were listed for scope; substantive research and governance drafts remain separate. The eight public repositories' README/on-ramp/context files were inspected, comprising 22 introductory documents. Their relative file targets resolve. This targeted check is not a claim that every historical page or external source across all repositories has been appraised.

| Public repository | Inspected main revision | Treatment |
| --- | --- | --- |
| `root-sequence` | `fa9abcabd36073b9706eca7056f68a9453e859c3` | README/research routes, Intelligence Ecology access notes, source-status clarity, and supporting-record navigation prepared in #46. |
| `.github` | `e244dd16002994fbb1abe0bf0c80933998846a92` | Reviewed organization introduction and current private/public registry prepared in #10. |
| `existential-euphoria` | `eb306d4e83d06790c53b3b6f0a90db227b193fcd` | In-formation status is explicit; introductory local targets resolve. |
| `universal-coherence-framework` | `e1c7b28803f58bea4a5b3a200063d5f579260b50` | Exploratory/author-review limits are explicit; homepage metadata needs repair. |
| `root-sequence-discussions` | `e93ec409bf3f490dbce47ae242921a5ccb276b1e` | Discussion routing and public/private boundaries are explicit; introductory local targets resolve. |
| `wiki` | `f15a718d932c1571d85396b85250b93d8953c6a4` | Existing strict-build repair extended with current public visibility in #15. |
| `beinghumane-guide` | `e7e8b35a7f13e15c041b53475a80aefbdb499437` | Developing field-guide status is explicit; homepage could not be verified. |
| `liberation-mass` | `4c791af6014a6ceedcb2e92cc4622f7a5076d485` | Experimental format and licensing inconsistency are disclosed in the orientation; homepage certificate and metadata need attention. |

### Prioritized public reading path

`concepts/intelligence-ecology.md` already identifies the selection-environment framing as a working hypothesis. The cleanup preserves the argument and section headings, makes clear that this page is not a report of empirical tests or a completed literature review, replaces four private-document links with explicit private-access notes, and links to the public research index and related working paper. No private document was copied and no unread external citation was added.

The main README uses the existing proposed navigation and approved positioning. The research index includes Intelligence Ecology and the already-public epistemic-discoverability concept with their limits. Existing AI/accessibility disclosure, incomplete author-review status, and the distinction between fiction and evidence remain. Current main's newer research and system-relative-limits work is incorporated through a two-parent review-branch update.

### Structural verification

The reader checker now passes 238 Markdown files, replacing its 15 recorded failures with zero errors. The fix is one corrected relative link plus links to fourteen existing T-003 supporting records from their current open-questions section. The existing manuscript argument, pilot results, and independent-review status are unchanged. All 11 site checks pass, and the Idea Trail graph/index is valid and current. The website source and publication gate are unchanged.

Wiki #15 retains its existing six-line orientation/build repair and adds current public routing: its generated public repository registry now contains eight repositories, and Liberated Intelligence is no longer advertised as a publicly accessible context. MkDocs 1.6.1 strict build and the existing public/private build-boundary check pass. Generated output contains 35 canonical entities and 14 project lenses. No private overlay is imported.

### Current access and unresolved decisions

Liberated Intelligence is now private. Rae clarified that it needs substantial revision and updates and is not ready for public inspection. The organization profile, ecosystem map, Wiki project index, and historical Root Sequence overview reflect that status. The historical overview is not presented as an account of the current drafts. No repository visibility was changed and no private contents were exported. Other known private projects retain their boundaries.

Live repository homepage checks found an HTTP 404 for UCF's `/ucf` page, a hostname certificate mismatch for `liberationmass.org`, and a timeout while verifying `beinghumane.guide`. A timeout does not establish permanent absence. The Wiki homepage returns HTTP 200. Corrected homepage/description values are prepared in the local review handoff; live settings are not changed by these source drafts.

Liberation Mass still has inconsistent source licensing labels (CC0 versus CC BY-SA for contributions); Existential Euphoria has no declared license in the inspected root. This pass does not choose licenses, alter existing grants, or adopt the separate research-stewardship proposals in root #50 / organization #12. Private/public Wiki completeness and freshness remain a later deliberate comparison.

### Release scope and preserved drafts

The two unreviewed applicant exercise files are preserved unchanged at `58002e0b547bac6e49b3b38b4c9a0171fe0e7d5a` on `review/work-samples-2026-10-23`. They are excluded from the documentation publication candidate, with their review route retained in the canonical plan. Existing root #46, organization #10, and Wiki #15 are reused; no additional cleanup PR is required. All three still need the user's explicit publication decision. No merge, deployment, policy adoption, private-source release, license change, or source-research endorsement is included.

## Publication and private-project status: 2026-10-23

This later checkpoint supersedes the pending-publication and live-metadata statements above. Dates in this checkpoint use Pacific time.

Root #46 is merged as `ec9ba2f693d482450e2361cde01a9b010089a91e`. Organization profile #10 is open for code review and is no longer a draft; Wiki #15 remains an open draft. Existing root status-update draft #51 is reused for the canonical plan, context, and ecosystem-map follow-up. No new PR is created and none of these remaining PRs is merged here.

### Current public/private boundary

The verified inventory still contains 15 repositories, now seven public and eight private. Rae made Liberation Mass private because it needs substantial revision and updates and is not ready for public inspection, the same reason given for Liberated Intelligence. Their broad roles remain in the public map, with explicit private/revision labels and no direct private-repository reading links in the affected summaries. The machine-readable organization registry records both as private. The Wiki automatic registry excludes them, and its public context index no longer offers Liberation Mass's private files. No private source is copied and no repository visibility is changed.

### Approved and applied live metadata

Rae explicitly approved the proposed bio, descriptions, and link repairs in chat. These values are saved and read back from GitHub:

| Field | Applied value |
| --- | --- |
| Organization bio | Independent interdisciplinary research exploring how intelligence, technology, and social systems shape one another. |
| `root-sequence` description | Independent interdisciplinary research exploring how intelligence, technology, and social systems shape one another. |
| `universal-coherence-framework` description | Exploratory framework for comparing how systems hold together or change; AI-assisted model under author review. |
| `universal-coherence-framework` homepage | `https://github.com/Root-Sequence/universal-coherence-framework#readme` |
| `beinghumane-guide` homepage | `https://github.com/Root-Sequence/beinghumane-guide#readme` |
| `liberation-mass` description | Experimental gathering format connecting collective action with shared ritual and celebration; rotating responsibilities and voluntary participation. |
| `liberation-mass` homepage | Cleared while the project is private pending revision. |

Liberation Mass's new private status makes the earlier proposed private-README homepage unsuitable for public navigation. Clearing the field removes the previously failing website route without suggesting that private drafts are ready for inspection. The historical timeout for Being Human(e) does not establish permanent domain failure. The site's source, publication gate, deployment, DNS, permissions, and existing license grants are unchanged.

### Checks and remaining decisions

Reader-document validation passes all 238 Markdown files. The Wiki public/private boundary check and MkDocs 1.6.1 strict build pass after the registry refresh, with 35 canonical entities and 14 project lenses. The organization registry's visibility values match the live 15-repository snapshot. These are structural and routing checks, not research validation.

Profile #10 still awaits code review, and #10, Wiki #15, and status follow-up #51 still need their publication decisions. P1-11 remains in progress. The preserved work samples, unresolved licensing questions, substantive research review, and private/public Wiki freshness comparison retain their separate scopes.

## Public-documentation batch completed: 2026-10-23

This checkpoint supersedes the remaining-publication statements in the preceding section. Dates use Pacific time.

[Root #46](https://github.com/Root-Sequence/root-sequence/pull/46), [organization profile/registry #10](https://github.com/Root-Sequence/.github/pull/10), [Wiki build/visibility #15](https://github.com/Root-Sequence/wiki/pull/15), and [root status follow-up #51](https://github.com/Root-Sequence/root-sequence/pull/51) are merged. The public website, repository introductions, organization profile and registry, seven-public-repository Wiki projection, and corrected private/revision status for Liberated Intelligence and Liberation Mass are now on their default branches.

The released documentation preserves project-local authority, research/evidence limits, private-source boundaries, and the separation of work-sample review. It does not adopt research claims, governance proposals, licensing changes, or private-Wiki material. The next planned professional-refresh action is the evidence-based open-PR triage in ROADMAP P1-12.

## Open-PR triage: 2026-10-23

Dates in this section use Pacific time. Root #52 is merged as `f42d934a05d1783ee003d3fd9b8f23545a39a30a`, completing the publication-status follow-up. The next work is the existing PR backlog, not another publication receipt.

The inventory taken before opening this audit PR contains **32 open PRs across 15 repositories: 16 public and 16 private**. Every PR has an initial recommendation. This public record covers the public proposals; private titles, branch contents, and findings remain in a private local handoff. No PR was merged or closed during the audit. No open proposal was found to be wholly superseded and ready for closure on that basis alone.

### Progress and review depth

| Check | Status | Evidence / remaining work |
| --- | --- | --- |
| [x] | done | Read current PR metadata, bodies, and changed-file inventories for all 32; read the small documentation diffs and selected scope, method, and boundary sections of the larger drafts. |
| [x] | done | Compare all 16 public PRs with current main using local Git tree merges; repair the sole current-main conflict in existing root #43. |
| [x] | done | Check all 21 pairs of the seven root research/proposal PRs after projecting each onto current main. Two pairs conflict, recorded below. |
| [x] | done | Prepare three existing maintenance PRs for individual review, preserve current privacy labels, and verify their exact remote commit trees. |
| [ ] | to do | Complete deeper source/claim review of root #44/#45, publication-policy review of #50, and separate technical review of the larger private drafts. This triage is not those reviews. |
| [ ] | to do | Decide each merge or closure individually, then reconcile accepted source proposals and their companions. No bulk merge is proposed. |

Full papers, generated PDFs, every external source, and private runtime behavior were not independently validated here. Checks reported in older PR descriptions remain their authors' records unless explicitly rerun below. A clean Git merge establishes textual compatibility, not evidence quality or approval. P1-12 therefore remains **in progress** in the canonical checklist.

### First maintenance candidates

1. **[Organization #13](https://github.com/Root-Sequence/.github/pull/13)** corrects the published profile/Wiki status in two context files and removes the stale pending-publication sentence from the infrastructure README. The branch now changes three documentation files. Profile copy, project registry, and policies are unchanged.
2. **[Organization #5](https://github.com/Root-Sequence/.github/pull/5)** adds the already-public Commons of Inquiry bootstrap under `external_or_nested_projects`. Its actual source is [`incubator/commons-of-inquiry/README.md`](incubator/commons-of-inquiry/README.md). The record retains `canonical_home: pending`, distinguishes the current nested seed from an intended standalone repository, and does not claim an operating institution. Current main is incorporated; all existing project records remain identical to main, including private/revision labels.
3. **[Wiki #12](https://github.com/Root-Sequence/wiki/pull/12)** adds one working Existential Euphoria identity and two index routes, grounded in its public repository and the organization registry. Original reflection and AI-assisted interpretation remain distinct; historical phrase provenance is unverified. The project creation timestamp is September 28 in Pacific time, not a first-use claim. Current Wiki main is incorporated and a generated-site project-index link is repaired. This supersedes the already closed Wiki #11, not another open PR.

Validation: organization registry YAML parses and its only proposed addition is the public seed. Wiki #12 passes the public/private boundary checker and MkDocs 1.6.1 strict build after source generation, with **36 canonical entities and 15 project lenses**. Its seven-public-repository automatic registry and private-project context labels are unchanged from current main. GitHub reports each candidate mergeable; their new heads have no posted reviews or check runs in this snapshot. GitHub's empty commit-status collection is not evidence of a queued or passing review. The local checks above are the evidence available for these small changes.

### Public PR recommendations

These are recommendations for review, not publication authorizations. Heads are the exact versions checked after the repairs in this pass.

| PR | Checked head | Recommendation and reason |
| --- | --- | --- |
| [Organization #13](https://github.com/Root-Sequence/.github/pull/13) | `e7d6c6f6c30b2d4f47e9de3cf76fab373250c3e8` | First maintenance batch. Three context/introduction corrections now agree with published main. Remains draft for review. |
| [Organization #5](https://github.com/Root-Sequence/.github/pull/5) | `7cd6cae1b6b4e43850e73b912c4a8e66c8437afb` | First maintenance batch. Indexes an existing public seed without promoting it to an established institution. |
| [Wiki #12](https://github.com/Root-Sequence/wiki/pull/12) | `4d76d8e03bc1b32139f6e6b6b152427b29ca8ad2` | First maintenance batch. Source comparison and strict build pass; unfinished provenance remains explicit. Remains draft. |
| [Root #43](https://github.com/Root-Sequence/root-sequence/pull/43) | `facfd8da4b3914af1304ba933c7c34ca3bfab4a1` | Merged by Rae as `95f6b73af47a4eb3e75ba3f0829e692af526bb11`; exact published tree verified. Its labelled proposal and main anchor are available; local rule adoption remains separate. |
| [Organization #9](https://github.com/Root-Sequence/.github/pull/9) | `bd4ef2771eff20629f8b081d01b6ff7bdf00f6c3` | Scoped review complete; next public companion batch. Current published profile, registry, and context corrections retained. New contribution guidance explicitly remains proposed; local adoption is separate. |
| [UCF #9](https://github.com/Root-Sequence/universal-coherence-framework/pull/9) | `64c2ddaa5acea2eaa3a3f97256264e083c76a7bc` | Scoped review complete; next public companion batch. Local application remains proposed; models, evidence status, claims register, and runnable examples unchanged. |
| [Discussions #8](https://github.com/Root-Sequence/root-sequence-discussions/pull/8) | `a8dd3ca4ae41dfd14434ec4552a8457146501606` | Scoped review complete; next public companion batch. Moderation extension stays proposed, with honest limits on review routes; no new appeals body or roles. |
| [Being Human(e) #6](https://github.com/Root-Sequence/beinghumane-guide/pull/6) | `0dbb4620a9b8a4a19d0be1e60ae7297b0ccd6f2a` | Scoped review complete; next public companion batch. README proposal preserves editorial scope and unresolved personal-story permissions; site and guide entries unchanged. |
| [Wiki #13](https://github.com/Root-Sequence/wiki/pull/13) | `63b5348822f9abc4a4ca022b659a209afc7716ff` | Scoped review complete; next public companion batch. README route to published source; strict build and public/private boundary pass, preserving #12's identity and current registry. |
| [Root #50](https://github.com/Root-Sequence/root-sequence/pull/50) | `8590f16c6bf8ea2fd010f9fe27be9b53006823a9` | Keep draft for publication-policy, attribution, and licensing decisions. Guidance explicitly remains proposed. Preserve existing grants; the October 22 license audit is dated history, not a current public-access census. Review its complete decision checklist before adoption. |
| [Organization #12](https://github.com/Root-Sequence/.github/pull/12) | `20fe610c6bb7306c49fdef107443a800f3afd303` | Keep paired with #50. Links deliberately pin the proposal's exact revision and describe it as unadopted; review those targets again if #50 changes. |
| [Root #41](https://github.com/Root-Sequence/root-sequence/pull/41) | `8a6c7b0e9bcbcb24ba725500ffd6e132338dc530` | Merged by Rae as `7c7231b9edc9b1d922fbbfd4a050f924b3823a1c`; exact published source verified. Working design distinctions, not formal metrics or empirical validation. See the later checkpoint below. |
| [Root #40](https://github.com/Root-Sequence/root-sequence/pull/40) | `b14ee22016bf9890715ba78e48b819759830f054` | Scoped review complete; author's content decision next. Anticipation remains proposed design guidance. Current main, source-route repair, and explicit inspection limits are included; shared metadata conflict with #42 is resolved. |
| [Root #42](https://github.com/Root-Sequence/root-sequence/pull/42) | `63d0d615000233dd1997869986195656ef1cc649` | Keep draft for source/domain and translation review of agency under stress. Current main and shared metadata are reconciled; original research/resilience wording unchanged. Source page is still absent from main. |
| [Root #44](https://github.com/Root-Sequence/root-sequence/pull/44) | `00f14ffd8fb8bffc0c551e1bab88b64c1f5c58b2` | Keep draft. Large research map and analytical probes require claim-level reading and source checks. Stipulated probabilities and mathematical toys are not human/organizational experiments or proof of an RS diagnostic advantage. Reconcile its index with #45. |
| [Root #45](https://github.com/Root-Sequence/root-sequence/pull/45) | `30748ee8db9bfde29fc0312a41b8f04edd98340d` | Keep draft. The Stoned Age has substantial reader editions and a source/claims ledger, but author, scholarly, cultural, and accessibility review remain incomplete. Existing validation records are not rerun scientific appraisal. Reconcile its research index with #44; website publication remains separate. |

### Dependencies and overlap

The five public companions to #43 are organization #9, UCF #9, Discussions #8, Being Human(e) #6, and Wiki #13. Their links to `commons/README.md#collaboration-as-a-living-experiment` will resolve on main only after a source decision. Accepting a shared proposal would still not approve every project's adaptation. Private companions retain their own review boundaries.

All 16 public proposals now merge individually into the checked current main trees. The root #43 repair passes the reader-document checker for all **238 Markdown files**. Pairwise checks of the seven root proposals found two conflicts:

- **#40 and #42:** `concepts/design-grammar.md`. Their prospective-guidance/agency wording needs a deliberate combined edit after deciding which content to accept.
- **#44 and #45:** `research/README.md`. Both insert research entries at the same place. Retain both only if each research proposal is accepted; no reason to copy one draft's substance into the other now.

The other 19 root pairs merge textually without conflict. This is not a test of every multi-PR order or semantic consistency. In particular, #50's proposed stewardship guidance and #43's collaboration practices need substantive review even though their repaired trees combine cleanly.

Checked public main revisions: root `f42d934a05d1783ee003d3fd9b8f23545a39a30a`; organization `7ea6c4b7cd191775a17d951935c7f9927f691f70`; Wiki `7b7d15120e289ab2798476afaf928f6a567c6172`; UCF `e1c7b28803f58bea4a5b3a200063d5f579260b50`; Discussions `e93ec409bf3f490dbce47ae242921a5ccb276b1e`; Being Human(e) `e7e8b35a7f13e15c041b53475a80aefbdb499437`; Existential Euphoria public source `eb306d4e83d06790c53b3b6f0a90db227b193fcd`. Refresh affected heads and main before an actual merge decision if they change.

Recommended order: review the three maintenance candidates first, then the small #41 conceptual addition. Review #43 as a shared proposal before its companions. Keep the larger research and stewardship families separate so a documentation cleanup cannot silently adopt research conclusions, licensing choices, or new governance.

## Maintenance merges and legibility review: 2026-10-23

This checkpoint supersedes the pending status of the three maintenance candidates above. Dates use Pacific time. Rae merged organization #13 and #5, followed by Wiki #12. All seven affected published files match the reviewed candidate blobs exactly.

| Completed PR | Merge commit | Verified result |
| --- | --- | --- |
| [Organization #13](https://github.com/Root-Sequence/.github/pull/13) | `9880ad1186fa436f70cc152ece60ee064bc37442` | Infrastructure README and both context files describe the completed profile/Wiki publication consistently. |
| [Organization #5](https://github.com/Root-Sequence/.github/pull/5) | `2ac252195775efcef42506027e033c5e84e99fab` | Registry routes to the actual public commons bootstrap, with canonical home pending and no operating institution claimed. |
| [Wiki #12](https://github.com/Root-Sequence/wiki/pull/12) | `446a1294a309051b9bb1590ea459e8d8a343cd0c` | Existential Euphoria identity and index routes are published; provenance and AI-interpretation limits remain. |

Wiki [deployment run 40069319901](https://github.com/Root-Sequence/wiki/actions/runs/40069319901) succeeded for the exact merge commit. The live [entity](https://wiki.rootsequence.systems/entities/existential-euphoria/), [project index](https://wiki.rootsequence.systems/projects/), [lexicon](https://wiki.rootsequence.systems/lexicon/), and [automatic registry](https://wiki.rootsequence.systems/auto-projects/) all return HTTP 200. The new identity and both index routes render; the entity keeps historical provenance unresolved and distinguishes AI interpretation from the original reflection. The automatic registry still contains no reading links to Liberated Intelligence or Liberation Mass. No private source was imported.

### Next content decision: root #41

The complete two-file context and proposed additions in [#41](https://github.com/Root-Sequence/root-sequence/pull/41) were read. The proposal distinguishes whether a structure holds together from whether another person can reconstruct it, then asks what a shorter representation preserves or loses. It explicitly avoids treating internal coherence as correctness or legitimacy. The distinctions remain working design guidance, not measured constructs. The AI-assisted-expression application retains its existing authorship, review, and privacy limits.

The existing branch now incorporates current main `f42d934a05d1783ee003d3fd9b8f23545a39a30a`, at head `8a6c7b0e9bcbcb24ba725500ffd6e132338dc530`. Both proposed source files remain byte-for-byte identical to the original #41 head: exactly **36 added lines in two existing concept pages** relative to current main. No site copy, source claims, external citations, project adaptations, or other draft research is added.

Validation: all 238 reader-document files pass; the whitespace check against current main passes; the new relative link and `representational-legibility` fragment resolve; both current evidence/status introductions are retained. No blocking issue was identified within this scope. This is not scientific or usability validation, an independent review, or the author's approval. #41 remains draft for a content decision. The agent did not merge or close any PR.

The canonical P1-12 remains in progress. This completed maintenance batch and small content review do not finish deeper research, stewardship, private implementation, or Wiki-freshness review. Existing audit draft #53 is reused for this record; no additional tracking PR is created.

## Legibility merged and collaboration proposal reviewed: 2026-10-23

Dates use Pacific time. Rae merged [root #41](https://github.com/Root-Sequence/root-sequence/pull/41) as `7c7231b9edc9b1d922fbbfd4a050f924b3823a1c`. The merged tree matches the checked candidate exactly, including both concept pages. Its representational-legibility distinctions are now public main content; publication does not turn working design guidance into empirical findings.

### Root #43: proposed collaboration practices

The complete four-file change and surrounding source were reviewed against the existing root contribution guide, organization contribution/stewardship documents, and the shared methods it references. The proposal gives one shared home to questions about participation and responsibility while leaving substantive project designs local. It protects criticism and voluntary departure, distinguishes contribution from access or decision authority, and keeps repair voluntary. Its feedback loop is explicitly an analogy, with no claim to have evaluated an operating community or discovered a shared causal law.

The existing draft now incorporates #41's merged main and has head `facfd8da4b3914af1304ba933c7c34ca3bfab4a1`. Three small clarifications were made during review:

- The new section identifies itself as AI-assisted and awaiting author review, and explicitly separates publication of the proposal from adopting project rules.
- Its pointer to organization guidance no longer implies that the unmerged companion update is already established.
- The root README pointer uses two short sentences instead of a dense list of proposed practices.

The proposed principles otherwise remain unchanged. The reviewed root introduction/reuse wording, #41 additions, and current private/revision labels are retained. The delta remains four files: `commons/README.md`, its root README route, and the existing role-power wording in `ECOSYSTEM.md` / `IDEA_TRAILS.md`.

Validation: all 238 reader-document files pass; scoped whitespace passes; the Idea Trail graph/index check and all 11 site checks pass on the exact #43 commit. The README fragment and four canonical local method/seed destinations exist. The existing public organization targets resolve in the inspected main source. No blocking issue was found within this scope. This does not complete the author's review, validate governance outcomes, appoint stewards, create an institution, or adopt rules. Publishing the text would publish a labelled proposal for discussion. Any project-local adoption remains a separate decision.

The five public companions remain open drafts: organization #9, Being Human(e) #6, UCF #9, Discussions #8, and Wiki #13. Their new source anchor is absent from main until #43 is published; local review is still required afterward. Private companions retain their own access and review boundaries. No companion is merged or automatically approved by this source review.

Existing audit draft #53 is reused and incorporates the #41 main merge. P1-12 remains in progress; no new PR, agent-performed merge or closure, deployment, license change, role assignment, or private-source export is included.

## Commons source published and public companions prepared: 2026-10-23

Dates use Pacific time. Rae merged [root #43](https://github.com/Root-Sequence/root-sequence/pull/43) as `95f6b73af47a4eb3e75ba3f0829e692af526bb11`. Its complete published tree matches the checked candidate. The shared source anchor now exists on main, with AI-assisted/pending-author-review status and the distinction between publishing a proposal and adopting local rules intact.

The five public companion PRs listed above were refreshed in their existing branches and reviewed against their current project guidance. Their main revisions were organization `2ac252195775efcef42506027e033c5e84e99fab`, UCF `e1c7b28803f58bea4a5b3a200063d5f579260b50`, Discussions `e93ec409bf3f490dbce47ae242921a5ccb276b1e`, Being Human(e) `e7e8b35a7f13e15c041b53475a80aefbdb499437`, and Wiki `446a1294a309051b9bb1590ea459e8d8a343cd0c`.

Organization #9 adds proposed contribution/stewardship guidance and an optional PR-template prompt. It retains the published profile, seed registry, and corrected publication context. UCF #9 makes the local application explicitly proposed while leaving models and evidence unchanged. Discussions #8 retains its proposed moderation extension and avoids promising unavailable independent review. Being Human(e) #6 states that contribution practices are proposed and personal-story permissions still need separate agreement. Wiki #13 supplies a short source route and preserves the distinction between navigation and project decisions. Crowded README summaries were shortened without copying the substantive commons text.

Together, these are **11 documentation files across five existing PRs**. Scoped whitespace and added local links/fragments pass; the published source anchor is verified. Exact file-scope comparisons preserve unrelated content, including the organization's merged profile/registry/context corrections and the Wiki's merged identity and privacy fixes. Wiki #13 passes its public/private boundary check and MkDocs 1.6.1 strict build with 36 canonical entities and 15 project lenses. No blocking issue was found in this scoped review. Runnable examples and the Being Human(e) site were not rebuilt because their source is unchanged.

The next decision is publication of these proposed local applications and the Wiki pointer. Their draft status and project-local adoption boundaries remain. Publishing #43 does not approve the companions automatically. Private companions have not been refreshed or approved by this public pass, and existing revision holds remain.

### Queued personal-page follow-up

Rae requested adding a small [whoami](https://raearea.net/whoami/) project-ecology/link update to the work list. The canonical checklist records this as P4-01, to do, after the current public PR batch. A preliminary live read returned HTTP 200 and found a direct Liberation Mass repository link that now leads to a private project. Other destinations and the site's actual source/open drafts still need inspection before preparing an edit. No personal-site source, copy, deployment, or settings changed here.

Existing audit #53 incorporates the #43 main merge and records this checkpoint. P1-12 remains in progress; P4-01 adds one queued task. No new PR, agent-performed merge or closure, role assignment, policy adoption, license change, or private-source export is included.

Rae subsequently expanded P4-01 to include homepage links and explicitly requested the proposed changes before either personal page is edited. A read-only inventory of both pages, destination checks, and inspection of the actual public `raelovejoy/raearea` source produced a local keep/change/add/pending proposal. P4-01 remains to do pending that review; neither personal page nor its source has been edited. The detailed link decisions remain in the local proposal rather than becoming unapproved website changes.

## Anticipation review and draft overlap resolved: 2026-10-23

This checkpoint supersedes the unresolved #40/#42 conflict recorded in the initial pairwise audit. The five public commons companions and audit #53 remain open at the checked snapshot; no further merge is inferred from a request to continue.

### Root #40: anticipation and surprise

The full proposed diff and relevant design-grammar, dynamic-coherence, adaptation, resilience, and source-lineage context were reviewed. Its prompt, “Anticipate what you can. Design for what you can't,” asks designers to consider foreseeable effects while retaining ways to notice a mistaken model and recover. It preserves the distinction between preparation and authority, names brittle over-anticipation as a failure mode, and leaves project-specific implementation/canon decisions local. It remains an AI-assisted proposal awaiting author review, with no new empirical result or universal mechanism established.

The existing branch now incorporates current main `95f6b73af47a4eb3e75ba3f0829e692af526bb11`, at head `b14ee22016bf9890715ba78e48b819759830f054`. Four original proposal files remain, plus a focused source repair in the existing `research/dynamic-coherence-lineage.md`. Reviewed main introduction, reuse, #41, #43, and private-project status are retained.

The old Hollnagel author-site route no longer supplied the cited material. The [Resilience Engineering Institute overview](https://resilienceengineeringinstitute.org/resilience-analysis-grid/) was inspected for its account of the four potentials and method orientation. The [Woods publisher abstract and bibliographic record](https://link.springer.com/article/10.1007/s10669-018-9708-3) were inspected for graceful extensibility and sustained adaptability. Neither the full technical note nor the full article was read in this pass. The lineage note now states that scope and labels the stronger claim about an intervention changing later conditions as a Root Sequence interpretation. The two anticipation sections link to that existing lineage treatment instead of leaving the comparison untraceable. No claim of full literature appraisal is added.

Validation on #40: all 238 reader-document files pass; Idea Trail graph/index is valid and current; scoped whitespace and all 11 site checks pass. No blocking issue was identified within this scope. These checks do not complete author review, validate the design prompt, or approve its project-local applications.

### Reconciliation with #42

The conflicting portions were the shared revision-date header and one long source-note paragraph. Both branches now separate pending-review status from dated source additions. #40's existing October 1 addition is recorded under change history; #42 retains its October 5 source addition. The refreshed #42 head is `63d0d615000233dd1997869986195656ef1cc649`, incorporating the same current main. Its agency-under-stress research and resilience source are byte-for-byte unchanged from the original proposal. No anticipation content is imported into #42, and no agency-under-stress content is imported into #40.

A targeted tree check now combines #40/#42 cleanly and retains both separate table additions in the combined fixture. #40/#44 also combines cleanly despite the scoped lineage-reference repair. These are local compatibility checks, not merges or acceptance. #42 passes all 239 reader-document files, the graph/index check, and all 11 site checks; it remains draft pending deeper source/domain review and the author's decision. #44/#45's separate research-index conflict remains unresolved.

Existing audit #53 records this work; P1-12 stays in progress. The personal-site link proposal remains pending review, including the supplied corrected Mastodon URL. Neither personal page was edited. No new PR, agent-performed merge/closure, deployment, clinical guidance approval, policy adoption, or private-source export is included.

## Agency under stress source review: 2026-10-24

This checkpoint uses UTC dates. Rae merged [root #40](https://github.com/Root-Sequence/root-sequence/pull/40) as `4fa71e26bcebd74fd6e1bf3d57c3475a8235d50c`. The published tree is `c1091a8ca9f32820f44c4b04bdd32f2b27d3a18b`, exactly matching the reviewed candidate. The anticipation prompt and its source limits are retained. Existing audit #53 incorporates this main revision without importing #42's unmerged research.

### Root #42: agency under stress

The complete four-file proposal and relevant surrounding source were reviewed. Its design question is how a system can reduce demands while preserving someone's usable agency when capacity is reduced. The current draft is `05abe41053ceb2c0b030aa6703c0d8afb7f407a8`, incorporating #40's published main and preserving both Design Grammar additions.

The source pass inspected selected passages for nine references, with the scope recorded in the [research note's source-check checkpoint](https://github.com/Root-Sequence/root-sequence/blob/05abe41053ceb2c0b030aa6703c0d8afb7f407a8/research/agency-under-stress.md#source-check-checkpoint-2026-10-24). The official GPO Senate PDF was checked at Finding 1. The UNHCR-hosted Istanbul Protocol supplied the relevant chapter passages after the OHCHR route returned an access error. Publisher/author texts supplied the other selected passages, except the 2019 decentering follow-up, checked only through its PubMed abstract and bibliographic record. Access to a document is not recorded as full-document reading. This is an AI-assisted claim/source check, not a systematic search, reanalysis, or independent clinical appraisal.

The revised note replaces the broad negative claim about a universal breaking point with a narrower account of varying stress responses. It supplies a direct acute-stress/executive-function source instead of an unsupported list of cognitive effects. Interrogation findings retain their experimental setting and differences between outcomes. Decentering is described as a proposed model with measurement limits, and its example illustrates perspective rather than giving instructions about danger. The WHO-inspired diagram, recovery framing, and system-design prompts are explicitly Root Sequence interpretations or proposals. None is presented as a clinically evaluated framework.

The research index now offers one route to the canonical note with AI-assisted/author-review-pending status, removing its duplicate unmerged-queue entry from this candidate. The resilience addition calls the design translation untested. The proposal remains four files; it changes no website source, private project, fictional canon, credentials, or participant protocol.

Validation on the revised #42: all 239 reader-document files pass, the Idea Trail graph/index is valid and current, scoped whitespace passes, and all 11 site checks pass. The remote commit tree matches the staged source. No blocking issue was found in this bounded documentation/source check. Author review remains pending; independent domain appraisal and project-local implementation decisions are not completed by this pass. The next decision is whether to publish this labelled working synthesis for discussion.

P1-12 remains in progress, with 31 canonical tasks: 24 done, six to do, one in progress, none blocked. The five public commons companions remain the previously checked review candidates; their status was not re-audited at this checkpoint. #44/#45's research-index conflict and the larger research/stewardship reviews remain. Personal-page edits still await review of the existing link proposal. Existing #53 is reused; no new PR, agent-performed merge or closure, deployment, policy adoption, or private-source export is included.

## Intelligence research review and index overlap resolved: 2026-10-24

Dates in this checkpoint use Pacific time. Rae merged [root #42](https://github.com/Root-Sequence/root-sequence/pull/42) as `bef05bc92b5cc3b7fc90e84aa94dcc9f414965e4`. Its complete published tree `9c0e0b3cbd25bfb19fff35093285b39afc67b85c` matches the reviewed candidate. The bounded source-check record, author-review-pending status, and untested design-translation wording are retained. Publishing the note does not establish clinical validity or adopt project-local applications.

### Root #44: Intelligence Without Omniscience

The seven research pages, changed concept/source pointers, graph/index updates, and relevant main-branch context were reviewed. The existing draft now incorporates #42's published main at head `59923f94ec5ed93576e86259e9cd2a3128b59395`, tree `6673fc42e15bcfbd46793941e8e47b9ce0da8972`. The proposal remains 15 files. It retains the independent-research introduction, approved AI/accessibility wording, private-project notices, the recent anticipation lineage repair, and #42's source. It changes no website source or publication approval.

The inquiry separates generality from knowing everything and distinguishes information discovery, evidence recognition, uptake, material capability, and authority. Its companion pages retain competing explanations and the possibility that established methods already do the useful work. The normative commons proposals do not establish an institution, licensing regime, governance authority, or requirement for disclosure. Fictional probes do not become human/AI-agent experiments or world canon.

A [source-check checkpoint](https://github.com/Root-Sequence/root-sequence/blob/59923f94ec5ed93576e86259e9cd2a3128b59395/research/intelligence-without-omniscience/README.md#source-check-checkpoint-2026-10-24) records the selected abstracts and passages actually inspected. It distinguishes author abstracts and institutional records from selected full-text passages. The remaining bibliography still needs deeper appraisal, especially the broader philosophy, capability, information-science, and governance interpretations. This is an AI-assisted bounded source check, not an independent domain review or systematic literature search.

The review makes four concrete corrections to how the work is presented:

- Fifteen links to private Coherent World supporting drafts became explicit access notes, preserving their names and the public conceptual summaries. The broader simulation route now points to the existing public ecosystem-map entry. Private content was not imported or released.
- The human–AI meta-analysis description now distinguishes 106 experiments from the 74 papers reporting them. The dated METR example retains its uncertainty intervals and explains what the time unit measures.
- The two-fact toy's targeted-request label no longer incorrectly conditions on successful routing while including routing uncertainty. Independent fraction arithmetic and exact enumeration of all 81 four-turn sequences per row reproduce the four rounded table rows. Parameters remain invented and the missing-fact-map confound remains explicit.
- Private follow-up execution counts are identified as reports from the original draft, not independently rerun suites. The research index uses one route to this source rather than retaining a duplicate draft-queue entry.

The #44 research-index addition now sits apart from #45's insertion. A targeted combined-tree calculation with #45 at `30748ee8db9bfde29fc0312a41b8f04edd98340d` is clean, resolving the earlier textual conflict. No #45 paper content is imported into #44, and #45 is not approved by this calculation.

Validation on #44: all 246 reader-document files pass, the Idea Trail graph/index is valid and current, and all 11 site checks pass. Whitespace checks allow the 52 intentional Markdown hard breaks in the added material. All 15 exact remote files match the staged source. No blocking issue was found within this scoped reading, source, arithmetic, and navigation check. Author review and a publication decision remain; deeper bibliography/domain appraisal is incomplete. Publishing would publish a labelled working research map, not validate its combined framework.

Existing audit #53 incorporates #42 main and records this checkpoint without importing #44 research. P1-12 remains in progress: 31 tasks, 24 done, six to do, one in progress, none blocked. The next large public research review is #45; stewardship/licensing and private implementation work remain separate. Personal-site source changes still await Rae's review of the link proposal. No new PR, agent-performed merge/closure, deployment, policy adoption, credential access, or private-source export is included.


## Intelligence research published and Stoned Age reviewed: 2026-10-24

Dates in this checkpoint use Pacific time. Rae merged [root #44](https://github.com/Root-Sequence/root-sequence/pull/44) as `9321c0f020c49068959f493c1ac854ad1bcbf7eb`. Its complete tree `6673fc42e15bcfbd46793941e8e47b9ce0da8972` matches the reviewed candidate. The public introduction, private-source access notes, bounded source-check record and invented-parameter qualifications remain. Publication does not establish the combined framework's validity or complete broader bibliography/domain appraisal.

### Root #45: The Stoned Age

The paper, essay, booklet source and talk source were read alongside the shared 16-source register, 19-claim ledger, existing appraisal/method records and edition builder. The existing draft now incorporates #44 main at head `12efef65ede19744ed1f43df01cb5ebbc1165e22`, tree `cddeab2de6108393af274205362195d946c69df5`. The 40-file delta remains confined to `research/the-stoned-age/` and its nearest research-index entry. It retains playful framing while distinguishing findings, models, hypotheses and editorial proposals. The completed research-index reconciliation preserves the published #44 route and removes the duplicate #45 draft-queue pointer.

This maintenance pass rechecked selected primary-source passages for S01, S03, S04, S06, S07, S14 and S15. The [dated appraisal follow-up](https://github.com/Root-Sequence/root-sequence/blob/12efef65ede19744ed1f43df01cb5ebbc1165e22/research/the-stoned-age/research/appraisal.md#review-follow-up-24-october-2026) distinguishes institutional abstracts, indexed primary text and selected main-text passages. Direct S03 PMC/XML retrieval failed; its indexed Results/Fig. 3 text was inspected without claiming a full analytical reappraisal. This is an AI-assisted targeted maintenance pass, not a new systematic search or independent scientific review. The other source appraisals remain the earlier record.

The creativity account now specifies that follow-up convergent-thinking scores were lower **than placebo**; the paper and appraisal distinguish this from both groups improving relative to their own baselines. Self-rated novelty remains separate from independently verified originality. The comparison is explicit in all four maintained editions and the claims ledger. S15 now pins the reviewed 2023 preprint version, with no inference to every current model or clinical outcome. Archaeological uncertainty, selected-sample/adverse-experience context, cultural authority and the difference between association and causation are retained.

Every HTML edition now links to Evidence notes. PDF generation uses stable metadata, and the editions and cover preview were rebuilt from the existing sources. The shared research index labels the suite as a review draft. No homepage, hosting configuration, private project, fictional canon or source license changes are included.

Validation on #45: all 256 reader-document files pass, the Idea Trail graph/index is valid and current, scoped whitespace passes, and all 11 website tests pass. All 165 local HTML links/assets/fragments resolve across seven pages. Source and claim IDs are unique and resolve. Two consecutive builds produce identical bytes for 20 generated files. All 16 booklet and 12 talk pages have extractable text and were rendered and visually inspected without visible clipping or overlap. Local browser checks cover the skip fragment, evidence navigation, a keyboard-operated speaker-note disclosure and appraisal/talk layout at 390 pixels without horizontal scrolling. Full keyboard, screen-reader and physical-device accessibility checks remain open. The exact remote tree, binary blobs and local staged tree agree.

No blocking issue was found within this bounded source/edition/navigation check. Author review remains pending. Arad full text, relevant supplements and registration comparisons, deeper source appraisal, situated cultural scholarship and independent disciplinary review remain open. Publishing the repository draft would not make it a reviewed scholarly release. Website publication requires a separate destination and deployment decision. No dosing guidance, clinical intervention or human-participant work is authorized.

Existing audit #53 incorporates #44 main and changes only this audit and the canonical checklist relative to main; it imports no unmerged #45 suite. Its reader check passes 246 Markdown files, with graph/index and all 11 site checks passing. The checklist now has one consistent current summary: 31 tasks, 24 done, six to do, one in progress, none blocked. P1-12 remains in progress. Five public commons companions retain their previously checked candidate status, not a fresh audit. Stewardship/licensing and private implementation work remain separate; personal-site changes still await Rae's review of the link proposal. No new PR, agent-performed merge or closure, deployment, policy adoption, credential access or private-source export is included.


## Proposed Stoned Age website route: 2026-10-24

Rae suggested adding the existing suite at `rootsequence.systems/stonedage/`. The actual Pages workflow and publisher were inspected first. They currently export only the homepage, so merging the earlier research suite alone would not create that route. A live check found the proposed route returns HTTP 404; the public build manifest still describes the approved single-page edition.

Existing draft #45 now prepares the route at `08286d1eff9592ed7e5eb01e05d1510972effe86`, tree `30c26ad548640f6ede05b9b2ffb7db640f659ef4`. Its full delta from main is 47 files: the existing 40-file research package/index plus seven site/workflow files. The route is prepared for review, not published. The research source, AI provenance, evidence limits and unfinished author/scholarly/cultural review remain as described in the earlier checkpoint.

The new combined publisher reads `research/the-stoned-age/` and exports 24 explicitly named reading files alongside the existing homepage. It adds the `/stonedage/` path, a return link, canonical addresses and robots metadata to generated research pages. PDFs and data downloads retain their source bytes. Other source links point to the existing GitHub branch in preview and main in release. No second maintained research copy, editable JSON source, build tools, unrelated research, private material or historical site is included in the hosting artifact. The original homepage source, original publisher and original approval are unchanged.

The proposed Pages workflow runs both publisher test suites, builds the combined artifact and watches the inquiry for updates. A separate pending `site/stonedage-approval.json` binds the exact route publisher, workflow, reading files and named source records. Its reviewer and approval date remain unset. The release command rejects that record before producing output. Merging the proposed workflow without the matching hosting approval would leave deployment blocked. No publication approval is inferred from the suggestion to prepare this route.

All 11 homepage tests and six added research-publication tests pass. The combined preview has eight HTML pages; all 192 local links/assets/fragments resolve. It preserves homepage bytes and both PDF files. The new return link reaches the unchanged homepage. The research landing page was inspected at desktop and 390 pixels without horizontal overflow or missing images; screenshots are in the local handoff and the viewport was restored. Reader documentation passes 256 Markdown files on #45, and the graph/index remains current. Scoped whitespace passes. The remote tree and exact publisher/workflow/approval readbacks match the staged candidate. No new scientific appraisal or full accessibility review is claimed by this hosting pass.

P1-13 records this bounded follow-up as in progress until review and publication are resolved. The canonical checklist now has 32 tasks: 24 done, six to do, two in progress, none blocked. Existing audit #53 is reused and changes only AUDIT.md/ROADMAP.md against current main; it imports no unmerged research or publisher code. P1-12, the remaining stewardship/licensing reviews and the personal-page pre-edit approval boundary remain. No new PR, agent-performed merge or public deployment occurred.


## Stoned Age repository references and companion clarification: 2026-10-24

Rae clarified that the Root Sequence homepage does not need a Stoned Age link; the proposed website should be referenced where the research lives. Existing draft #45 now records the planned, unpublished `/stonedage/` address in its research README and parent research index. The homepage is byte-for-byte identical to current main and contains no Stoned Age link.

The current suite contains no separate “How Drugs Explain the Universe” companion text. Its prior “companion provocation” label implied an artifact that was not supplied. The maintained README, paper, booklet JSON and landing-page generator now use “working provocation,” preserving the phrase as framing for the inquiry. The generated editions and booklet cover preview were rebuilt. No separate companion was invented or added, and the evidence and review status remain.

The existing #45 head is `2f382c71c1434f1c2ee447656aa5a1dffe2c57ef`, tree `e58ad9f63cc7c4c59552b0f2b68b036c316d1892`. The full delta remains 47 files against main. All 17 site/publisher tests, the 256-file reader check, graph/index and scoped whitespace pass. The changed cover was rendered and visually checked; text on the other 15 booklet pages is unchanged, and the talk PDF is byte-identical. The pending hosting fingerprint was refreshed without adding a reviewer or approval date. Exact remote research references and the pending record match the staged candidate. No publication is claimed.

Existing audit #53 records the clarification and current P1-13 head without importing the suite. Its reader check passes 246 Markdown files. The checklist retains 32 tasks: 24 done, six to do, two in progress, none blocked. No new PR, agent-performed merge, public deployment, research conclusion or personal-page change is included.
