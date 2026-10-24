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
