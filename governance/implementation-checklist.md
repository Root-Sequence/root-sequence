# Research stewardship — implementation checklist

**Prepared:** 2026-10-22.  
**Status convention:** checked means the draft artifact or inspection exists, not that a policy has been adopted or protection guaranteed.

## Prepared in this proposal

- [x] Record a preliminary public licensing baseline, including scope limits and the Liberation Mass conflict.
- [x] Draft public/limited-review/restricted publication handling and a pre-disclosure checklist.
- [x] Draft attribution, contribution-role, AI-assistance, and exact-version provenance guidance.
- [x] Add project citation metadata without inventing a release, DOI, or validation claim.
- [x] Distinguish responsible-use expectations, actual license obligations, and negotiated agreements.
- [x] Draft non-endorsement, reciprocal collaboration, and proportionate concern-handling guidance.
- [x] Add the bounded knowledge/power research question and navigation to the new material.

## Decisions before adoption or a legal change

- [ ] Review the wording and identify who may authorize each project's publication boundary.
- [ ] Resolve the Liberation Mass licensing conflict with affected contribution history and rights holders.
- [ ] Decide licensing for future separable writing, separately from code, data, and media.
- [ ] Clarify permissions in projects without a top-level license file; preserve existing grants.
- [ ] Complete a rights-and-consent review of third-party contributions and assets where relevant.
- [ ] Adopt any project-specific procedure through that project's normal review; do not treat this draft as organizational consent.
- [ ] Review and merge this documentation only after an explicit decision; no auto-merge.

## Private professional preparation — keep outside public repositories

- [ ] Verify a dated preexisting-work inventory, versions, rights, collaborators, and any earlier obligations.
- [ ] Curate the minimum sufficient application samples; record what is actually sent and under which terms.
- [ ] Review hiring exercise, portal, confidentiality, and IP-assignment language before accepting it.
- [ ] Obtain a written, agreed background-work exclusion and review treatment of future independent work where appropriate.
- [ ] Keep professional legal advice and agreements in personally controlled private storage.

These private tasks have no public evidence attachments. Their checklist entries are not an invitation to upload the underlying records here.

## Validation and rollout

Validate changed links, metadata, preservation of existing license files, and absence of newly introduced private information. Repository-wide checks must be reported as run, failed, or not run; a documentation-only change is not an excuse to invent test results. Keep related unmerged proposals separate, refresh overlapping branches before merge, and record decisions rather than silently resolving them.

### Validation record — 2026-10-22

Scope: PR #50 at `7ebd265dd8b3aebc5039ad7f234668560d49da11`, plus the documentation corrections committed with this record. Original base: `a8b0f805d1c4bbd14c52845b4861854b9ebc6e8f`. Current `main` inspected separately: `fa9abcabd36073b9706eca7056f68a9453e859c3`. This is technical review, not Rae's author review or legal clearance.

- [x] Return PR #50 to draft, as requested; it was marked ready when this pass began.
- [x] Replace the temporary citation-interface claim with wording that remains accurate before and after any future merge.
- [x] Pin the Root Sequence and Being Human(e) license-audit links to inspected commits. The latter still identifies blob `463788c7f9f946e196e14630aa39d781e2cbae1f`; neither license text nor its interpretation changed.
- [x] Validate `CITATION.cff` against the upstream [CFF 1.2.0 JSON schema](https://github.com/citation-file-format/citation-file-format/blob/1.2.0/schema.json), including format checks; parse all three public governance YAML examples.
- [x] Check local links and Markdown fragments in all 13 changed Markdown files; no missing targets or headings.
- [x] Run `python3 cli/generate_idea_trail_index.py --check`: passed.
- [x] Run `python3 site/test_site.py`: all 11 tests passed.
- [x] Run `python3 cli/check_reader_docs.py` on the proposal and unchanged original base: both fail with the same 15 messages. No new reader-documentation error was introduced.
- [x] Recheck the official sources listed in `governance/references.md` for the cited distinctions. This does not establish rights ownership or resolve the recorded license conflict.
- [x] Inspect the diff: documentation/citation paths only; existing license, site, executable, workflow, and contribution terms remain unchanged. No private packet or employment records were added. This scoped inspection is not a complete secrets or rights audit.

The 15 existing reader-check failures are one incorrect relative link in `research/papers/coherent-systems/notes/t003-added-value-protocol.md` and 14 notes without inbound Markdown navigation in that same directory. They remain a separate paper-documentation cleanup; a passing subset of checks must not be reported as an entirely green repository.

### Compatibility record — 2026-10-22

Local `git merge-tree --write-tree` checks found no textual conflicts with the inspected `main` or any other open PR in this repository. They create local test trees only; no PR, branch, or policy was merged. The table lists paths changed by both proposals, excluding changes merely inherited from their different bases.

| Other PR | Inspected head | Shared proposal paths |
| --- | --- | --- |
| [#40](https://github.com/Root-Sequence/root-sequence/pull/40) | `0cf7ed00cd24` | None |
| [#41](https://github.com/Root-Sequence/root-sequence/pull/41) | `c731d2f481c8` | None |
| [#42](https://github.com/Root-Sequence/root-sequence/pull/42) | `6329bfea8b9d` | `research/README.md` |
| [#43](https://github.com/Root-Sequence/root-sequence/pull/43) | `6097553039e9` | `README.md` |
| [#44](https://github.com/Root-Sequence/root-sequence/pull/44) | `00f14ffd8fb8` | `research/README.md` |
| [#45](https://github.com/Root-Sequence/root-sequence/pull/45) | `30748ee8db9b` | `research/README.md` |
| [#46](https://github.com/Root-Sequence/root-sequence/pull/46) | `58002e0b547b` | `README.md`, `PROJECT-CONTEXT.md`, `research/README.md`, `root_map.md` |

The shared navigation retains the stewardship proposal's pending-review status and the other proposals' separate scope. Commons collaboration (#43) and professional presentation (#46) are complementary to the narrower publication/reuse guidance; neither is adopted here. The newer `main` research additions also combine without conflict. In an isolated copy of that combined tree, the Idea Trail check and all 11 site tests pass, and the reader check reports the same 15 baseline errors. Pairwise checks do not prove that every future merge order or combination will be conflict-free.

The companion [organization PR #12](https://github.com/Root-Sequence/.github/pull/12) at `8571eb3de505c6ed8cf7c514d576905b8b70d5be` also combined without textual conflicts with organization #5 (`518f58a876f8`), #9 (`36527befd9f1`), and #10 (`aaaf425d6669`). Its pinned links are snapshots; refresh them when the source proposal changes, and switch to the maintained home only after adoption is approved.

- [ ] Repair the 15 pre-existing reader-documentation failures in their own scoped change.
- [ ] Repeat compatibility and navigation checks if `main` or another relevant proposal changes before a merge decision.
- [ ] Obtain the adoption and licensing decisions above; technical validation supplies no approval by itself.

No monitoring automation, archival deposit, trademark registration, patent action, signature, agreement, or legal representation is created by this proposal.

[Research stewardship](README.md)
