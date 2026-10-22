# Attribution, authorship, and provenance

**Status:** proposed convention; AI-assisted; author review pending.  
**Purpose:** make contributions traceable without claiming ownership of every idea or mistaking a historical record for validation.

## Credit the actual contribution

Distinguish originating a question, connecting existing work, writing, editing, coding, testing, reviewing, maintaining, and supplying lived or community knowledge. Project initiation and curation do not establish sole authorship of every repository item. Credit prior work and contributors with the names and level of disclosure they consent to; do not expose private identities to strengthen a credit claim.

For a specific result, cite its document-level authors and sources, exact path, version/commit, date where known, and relevant limitations. Do not invent a first-discovery date, DOI, affiliation, peer review, successful experiment, or author approval. The [root citation file](../CITATION.cff) identifies the project as a whole; it is not a substitute for item-level credit.

GitHub recognizes root-level `CITATION.cff` metadata on the default branch.[^cff] While this change is a draft PR, the default-branch citation interface has not been changed.

## Minimal provenance block

Use visible metadata or existing frontmatter rather than creating a competing database.

```yaml
title: "Exact title"
status: "working draft; author review pending"
canonical_path: "repository/path"
contributors:
  - name: "approved public credit"
    roles: ["specific contribution"]
first_documented: null
revised: "YYYY-MM-DD"
source_revision: "exact commit when available"
intellectual_sources: []
permissions: "actual applicable notice, including exceptions"
ai_assistance:
  used: true
  tasks: ["only tasks actually performed"]
  human_review: "pending or specific completed review"
```

`first_documented` means the earliest evidence located, not proof of universal novelty. A Git commit identifies a version; its date alone is not independent certification of first authorship. Retain original drafts, research notes, review decisions, and source links where appropriate, with private evidence kept private.

## AI assistance

Describe what the tools did and what humans actually contributed, checked, rejected, or revised. Do not add a human-author claim simply because a person approved a prompt, and do not infer all intellectual work was automated because AI assisted with expression or accessibility.

The U.S. Copyright Office's 2025 guidance distinguishes sufficient human expressive authorship from purely generated material; AI assistance does not automatically defeat protection, and prompts alone do not establish it.[^ai] Provenance helps explain the work but does not guarantee copyright, novelty, or correctness.

**Disclosure for this stewardship draft:** ChatGPT assisted with repository/source inspection, organization, drafting, and change preparation in response to Rae Lovejoy's request. The draft has not received Rae's passage-by-passage review or legal review. The request to prepare it is not evidence of review of every sentence.

## Citation request versus legal obligation

Ask readers to acknowledge useful contributions even when the applicable license does not require it. Clearly label that request as scholarly/community practice, not a new condition on CC0 material. For material under an attribution license, follow that license's actual conditions and any lawful exceptions; consult the [license decision guide](licensing.md).

Suggested wording:

> Please cite the specific document and revision you used, credit its identified contributors and sources, and distinguish your adaptations from the original. This request does not add restrictions to the applicable license or imply endorsement.

## Versioned release practice

For a reviewed release, record the exact revision, review status, contributors, scope, limitations, and source list. Consider an independently hosted archival deposit only after a separate public-disclosure decision. No archive deposit, DOI, public timestamping service, or new release is created by this proposal.

## References

[^cff]: GitHub, [About CITATION files](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files), checked 2026-10-22.
[^ai]: U.S. Copyright Office, [NewsNet 1060: Copyrightability report](https://www.copyright.gov/newsnet/2025/1060.html), 2025-01-29; checked 2026-10-22.

[Research stewardship](README.md)
