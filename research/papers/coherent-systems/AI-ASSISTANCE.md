# AI assistance, verification, and author review

**Record started:** 2026-09-16. **Applies to:** the v0.1-dev living paper and its documented UCF connection. **Status:** working disclosure, not an author-approved submission statement.

## Disclosure suitable for the current draft

This draft was developed with ChatGPT assistance for organizing project material, locating literature, drafting and critiquing arguments, and developing the synthetic example with associated Python code and tests. AI output is not treated as evidence. Source inspection, software checks, author review, and independent evaluation are separate activities. Source-by-source author review, approval of the current manuscript, and independent evaluation remain incomplete.

The author has contributed motivating questions, project direction, connections among projects, constraints, objections, and revision decisions through conversation. These contributions are already part of developing the work; final manuscript approval is a different activity. Exact quotations or attribution to earlier conversations require traceable sources and appropriate permission. Neither this description nor a request to continue implies approval of every synthesized claim or verification of all references.

This assistance was more extensive than grammar correction. The record should not be narrowed to “language editing” to make it appear more acceptable. It also should not claim that the author has personally verified every reference or approved every argument when that review has not occurred.

## What assistance has covered

| Activity | Actual role | Limit and required review |
|---|---|---|
| Project synthesis | Organizing public project concepts, comparing definitions, proposing structure and claims | User authorization to develop a draft is not endorsement of every resulting proposition. |
| Literature work | Searching, opening primary sources, inspecting selected text and PDF figures, drafting comparisons | Retrieval and AI-assisted inspection are not independent human reading, exhaustive search, or validation of the cited studies. |
| Writing and critique | Drafting substantial prose, proposing examples, objections, and evidence classifications | Agreement between AI outputs is not independent peer review. The author must decide what to retain. |
| Computational work | Earlier assistance produced the UCF booking model and its implementation checks | A code test checks specified behavior. It does not validate a scientific framework, study finding, or allocation rule. |
| Repository work | Preparing files, references, cross-links, change records, and draft-branch updates | A saved commit is not approval, deployment, or a reviewed publication. |

The external-evidence pass added no patient data and ran no empirical or participant study. It did not rerun or replicate the Obermeyer analysis. The earlier booking checks remain documented in their own revision and recovery records rather than being relabeled as tests performed in that pass.

## Tool record and reproducibility limits

The platform used is ChatGPT, with web retrieval, GitHub actions, and local Python where needed. Exact model identifiers and settings for every earlier drafting session are not preserved in the repository; they must not be reconstructed from assumptions about a product name. No claim of full conversational reproducibility is made.

For future sessions, record the tool and visible model/version when available, date, task, affected paths, code inputs and outputs, source locators, and human corrections. If a field is unavailable, say so. Preserve relevant public-safe task instructions, not hidden reasoning or unrelated private conversations. The versioned text and runnable code are the durable artifacts.

The source map records what was actually inspected. Validation records must distinguish a retrieved document, verified bibliographic metadata, checked passages, reproduced arithmetic, and independent replication. None should stand in for another.

## Question-led author review

The author requested clarification questions throughout drafting rather than a large document followed by an all-at-once defense. [AGENTS.md](AGENTS.md) records that working method. Present one small passage or example, provide the relevant context, and ask one meaningful question. Responses may be fragments, examples, corrections, or uncertainty. The assistant proposes a synthesis and shows the resulting change; it must not silently decide unresolved meaning.

Review may use written notes, source passages, repeated explanations, and pauses. It does not require unaided recall or fluent speech on demand. The standard is an inspectable account of the claim, its support, and the author's decisions, not a performance test. This support does not turn unchecked evidence into checked evidence.

The checkpoints below are a sequence to work through with support, not a batch of homework. None is pre-approved:

- [ ] Present a short part of section 4, an example, and the relevant source passage. Ask what is accurate, too strong, unclear, or missing; revise C-003 with the author's response.
- [ ] Present the healthcare case one finding at a time with its source locator. Work through what a reported quantity measures, recording any uncertainty and which source material the author has reviewed.
- [ ] Review C-001, C-003, and C-012 individually. Record accept, qualify, reject, or not yet decided for the exact passage and revision; do not infer reasons the author did not give.
- [ ] Review the abstract and disclosure in small units. Confirm scope, assistance, and remaining uncertainty separately from any eventual release or byline decision.

Do not add an approved personal byline, institutional affiliation, peer-review claim, or release identifier before the appropriate decision is made. Project provenance is not a substitute for an eventual accountable author record.

## Publication and privacy boundary

Elsevier's author guidance, checked in the external-evidence pass on 2026-09-16, permits specified AI support but requires human oversight, verification, and disclosure; research-method uses require methodological documentation. It does not guarantee acceptance elsewhere or certify this draft's compliance.[^elsevier]

Before submission, check the chosen venue's current requirements, actual tool terms, permissions, and data handling. Those terms and account settings have not been audited here. Neither a paid account nor a public repository proves that all confidentiality obligations are satisfied.

This GitHub branch is public. This record describes the collaboration process without publishing personal health information, private conversation excerpts, patient records, or confidential manuscripts. A personal first-person explanation of why the author uses AI requires separate approval of its wording and destination. The package contains original notes and links, not copies of the cited papers or their figures.

## Change recorded 2026-09-16

Added the requested question-led workflow and clarified that conceptual contributions already made are distinct from incomplete review of the current manuscript. Replaced the checkpoint requiring an unaided explanation with supported, passage-level review. Kept all source-verification and independent-evaluation requirements, unmarked review decisions, and substantive AI-assistance disclosure. No research claim, source-check status, authorship approval, or release status was changed by this process edit.

## References

[^elsevier]: Elsevier, *Generative AI policies for journals*, “For authors,” disclosure, research-process/code-development FAQs, and documentation guidance. [Policy](https://www.elsevier.com/about/policies-and-standards/generative-ai-policies-for-journals), accessed in the earlier external-evidence pass on 2026-09-16; not rechecked for this process edit. A publisher's policy, not empirical support for the paper's claims.

[Source map](notes/source-map.md) · [Claims](claims.md) · [Changelog](CHANGELOG.md)
