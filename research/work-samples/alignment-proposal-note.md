# Separating task success, authorization, and alignment

**Role:** proposal-development exercise, not a funding request.
**Revision:** 0.1, 2026-10-17.
**Status:** AI-assisted draft; Rae's source and passage review pending. No study, recruitment, model evaluation, or deployment has been performed.
**Question:** Can a short review aid help readers distinguish successful task completion from authorized action and agreement about the goal?

## Rationale and source boundary

An assistant can complete a requested task while leaving unresolved who had permission to request it or whose interests the goal serves. Treating these questions separately can make a proposal more precise. That is the motivating interpretation here, not an experimental result.

Iason Gabriel distinguishes several possible alignment targets and argues that technical and normative questions interact. His paper supplies a conceptual distinction, not evidence that this proposed aid improves judgment. The [arXiv v2 abstract](https://arxiv.org/abs/2001.09768v2), dated 5 October 2020, was checked for this note on 2026-10-17. This pass did not appraise the whole paper or verify all its citations. The [existing project source map](../papers/coherent-systems/notes/source-map.md) separately records a broader, earlier AI-assisted inspection; that history is not relabelled as a new full reading.

Root Sequence's [Agency and Automation](../../concepts/agency-and-automation.md) and [Legible Systems](../../concepts/legible-systems.md) supply the local design questions about delegated authority and understandable systems. They are developing project arguments, not independent support for effectiveness. The [research method](../method.md) supplies the comparison and revision workflow.

## Proposed investigation

The first deliverable would be a small, public set of synthetic assistant-action cases and a coding guide. Every case would separate three questions: was the stated task completed; was the action within an explicitly stated permission; and which alignment target or unresolved value judgment was at issue? Task success and permission can be stipulated in a fictional case. Moral disagreement should remain visible instead of being scored as an objectively wrong answer.

A domain reviewer would examine the distinctions before comparison begins. The review aid would ask readers to identify the goal, relevant permission, affected parties, uncertain facts, and the claim they can support. The competent baseline would contain the same facts, similar reading length, and ordinary review prompts. An intentionally poor summary would not be a useful baseline.

Only after that design review would a preregistered pilot compare the two formats. A proposed assignment would give each reader both formats on different, counterbalanced cases, with no repeated case for the same reader. An analysis plan would account for reader and case differences. It would define in advance what counts as confusing stipulated task success with permission, how ambiguous responses are handled, and when a case must be excluded. Blinded coding of responses and reporting disagreements would help expose scoring choices. Neither exact sample size nor a powered effect estimate is justified yet.

## Deliverables, gates, and interpretation

| Stage | Deliverable | Gate / failure condition |
| --- | --- | --- |
| Clarify | Annotated case set, coding guide, disagreement log | Revise or abandon if reviewers cannot separate factual stipulations from normative judgments. |
| Compare | Matched baseline and review aid; registered protocol and analysis plan | Specify outcome definitions, counterbalancing, recruitment, consent, and sample-size rationale before collecting responses. |
| Evaluate | De-identified responses and analysis, subject to consent and data-management review | Report errors, uncertainty, missing data, reader/case effects, and coder disagreement; null or adverse results remain reportable. |
| Revise | Short report and a retain/revise/retire decision | Retire the aid if it adds burden without useful error reduction. |

A positive result would concern interpretation of these cases under this protocol. It would not establish that an AI system is aligned, that permission language enforces a security boundary, or that the aid improves real deployments. Better scores might reflect formatting, prior familiarity, or the ease of the cases. Matched content, counterbalancing, and a reading-burden measure would address some of those alternatives; a pilot would still have limited generalizability.

## What a funder would still need

This is a seed for discussion. A submission would need a suitable funding call, a technical/domain lead, related-work appraisal beyond the abstract, an appropriate study-review process, recruitment and data-management plans, a justified analysis and sample size, and costed staff time. Those commitments have not been secured. No budget, partnership, scientific novelty, or match to a current AIAF funding priority is claimed.

## Contribution and evidence record

This note transforms existing public project questions into a proposed comparison. Codex provided substantive synthesis, drafting, and source retrieval. Rae requested the work-samples track and has not yet approved this note's framing or claims. The durable outputs in this revision are the note, its linked sources, and its Git history. There are no participant data or measured findings.

[Work-samples route](README.md) · [Research evidence and AI-use guide](../README.md) · [Canonical checklist](../../ROADMAP.md)
