# Healthcare cost as a proxy: a published case

**Source:** Ziad Obermeyer, Brian Powers, Christine Vogeli, and Sendhil Mullainathan, *Dissecting racial bias in an algorithm used to manage the health of populations*, Science 366(6464), 447–453 (2019), DOI `10.1126/science.aax2342`. [Author-hosted article](https://sendhil.org/wp-content/uploads/2020/01/Publication-67.pdf).

**Status:** AI-assisted retrospective reading, 2026-09-16; author review pending. Not a replication, clinical recommendation, or claim about current products.

## Attributed findings

The study examined a commercial care-management score using a large academic hospital's 2013–2015 primary-care data. At equal scores, Black patients had higher illness burden. Predicting expenditure rather than illness, amid unequal spending relative to need, produced the mismatch. In a simulated reallocation at the 97th-percentile threshold, the Black share of the auto-identified group changed from 17.7% to 46.5% (pp. 1–3, Fig. 1B). That is not the share of all Black patients served or an observed post-deployment improvement. Enrollment also involved clinical and administrative decisions (p. 6).

## Our interpretation, not the study's terminology

For C-001 and C-005, the useful question is whether evidence of success concerns the intended outcome or a different target. Before declaring a system coherent, specify the purpose against which that description is made.

A UCF layer review can organize questions without claiming to discover the mechanism:

| Layer | Question for a future assessment, not an additional finding |
|---|---|
| Internal | What exactly does the target measure, and what would falsify its adequacy for the intended task? |
| Inter-agent | How do users interpret the output, and who may challenge or override it? |
| Systemic | Which relevant conditions sit outside the data boundary, and what evidence would justify including them? |
| Temporal | What follow-up would distinguish a better selection rule from improved outcomes over time? |

These questions do not require UCF terminology. We have not shown that the framework adds information beyond the original explanation or a competent sociotechnical review. A source documenting harm is not an endorsement of our method.

## Limits of this pass

The reading covered the main article's data/strategy, disparity and mechanism passages, and discussion of human judgment; Table 1 and Figure 1 were visually checked. Supplementary methods, raw patient records, code, and the authors' wider data were not independently analyzed. No new medical conclusions or patient-level predictions are made.

Do not generalize a study setting to every institution, racial group, algorithm, or present-day implementation. Do not reinterpret a modeled change in selection as a measured benefit from treatment. A future model must justify its own target, scope, and evaluation rather than borrowing this paper's findings as a universal guarantee.

## What this changes in our paper

Add the case beside the synthetic booking example, keeping source findings, our interpretation, and untested implications visibly distinct. The booking fixture exposes assumptions; this note examines published evidence. Neither validates C-012's added-value hypothesis.

The key author-review task is to explain the difference between **what was predicted**, **what the decision was intended to accomplish**, and **what outcome evidence would be needed next**. Uncertainty belongs in that explanation rather than being filled with a stronger story.

[Manuscript](../paper.md) · [Related work](../notes/related-work.md) · [Source coverage](../notes/source-map.md)
