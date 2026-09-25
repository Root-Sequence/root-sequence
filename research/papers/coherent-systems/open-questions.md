# Open questions and first research tests

**Version:** v0.1-dev · **Updated:** 2026-09-16  
**Status:** T-001 has an AI-assisted editorial case set but no independent reviewer study. T-002 has a synthetic implementation and eight passing implementation tests, rerun after the interruption. T-003 remains unrun. No empirical validation is claimed.

## Questions

| ID | Question | Claim links | What would advance it? |
|---|---|---|---|
| Q-001 | What does the framework add beyond existing systems and sociotechnical methods? | C-001, C-003, C-012 | A prior-work matrix and a fair comparative assessment, including null results. |
| Q-002 | Can functional performance, coherence, and normative legitimacy be distinguished without making any of them arbitrary? | C-003, C-007 | Examples of effective coercion, unreliable protection, and genuinely mixed outcomes, with the mechanism of any false coherence stated explicitly. |
| Q-003 | Who defines boundaries, purposes, harm, and legitimate decision rights when affected parties disagree? | C-003, C-004, C-008 | A bounded account of evidence, representation, exclusions, appeal, urgency, and non-participation. |
| Q-004 | How can assessment avoid a new proxy called “coherence”? | C-005, C-006 | Separate indicators, causal explanations, and cases in which no overall conclusion is warranted. |
| Q-005 | How much information is needed without making participation into surveillance or unpaid work? | C-004, C-008 | Data minimization, accessibility, refusal, and burden assessment. |
| Q-006 | When are changes reversible, and when do dependencies demand coordinated transitions? | C-007, C-011 | Intermediate-state and failure maps, including lock-in and discontinuity. |
| Q-007 | Which bottlenecks are informational, institutional, material, or genuinely mixed? | C-002, C-006, C-009, C-011 | A concrete causal model with competing explanations and non-AI alternatives. |
| Q-008 | What remains constrained when monetary or computational bottlenecks change? | C-009, C-011 | Explicit energy, material, ecology, maintenance, access, decision-rights, and practical-power accounting. |
| Q-009 | When do scenarios broaden inquiry, and when do they reproduce the author's preferred future? | C-010 | Contrasting scenarios and independent evidence checks on extracted hypotheses. |
| Q-010 | Who can revise this framework, and what results would justify retiring it? | C-012 | Publicly visible objections, changelog, review criteria, and recorded failures. |

## T-001 — Definition stress test

**Initial editorial cases are recorded in the [UCF example](https://github.com/Root-Sequence/universal-coherence-framework/blob/c4d7b236828a59139c0d5204b1faaed13154682a/models/examples/booking-service/README.md). Independent review remains to be done.** The case set covers: an effective but coercive system; a protective but unreliable system; a mixed improvement with displaced burdens; and a bounded repair with clearly specified beneficiaries and costs.

Have reviewers first record who acted; what they did and to whom; where and when; how; why they said they acted; the claimed harm, claimant, evidence, and uncertainty; and what effects followed. Separately describe target performance, boundary omissions, affected relationships and power, and the later normative or procedural assessment, including the source, scope, limits, and accountability of decision-making power. Then apply C-003. Record ambiguity, excluded parties, disagreements, the mechanism of any proposed false coherence, and whether the vocabulary adds clarity. Do not treat target execution as coherence, assume that “protection” settles what counts as harm, let a compound label decide the justification in advance, or use “authority” without specifying what kind.

**Failure signal:** The word “coherence” simply tracks approval, “false coherence” merely tracks disapproval without identifying a mechanism, objections become obscured, or the vocabulary produces no distinction beyond ordinary description.

**Boundary:** Editorial review of fictional material, not evidence of real-world intervention success. Any later human-participant study requires a separate protocol, consent, and data handling plan.

## T-002 — Local objective and displaced burden

The hypothetical booking example now has a [synthetic implementation](https://github.com/Root-Sequence/universal-coherence-framework/blob/c4d7b236828a59139c0d5204b1faaed13154682a/models/examples/booking-service/booking_model.py) in UCF. It compares completion maximization, a minimum-coverage constraint, and a fixed arrival-order rule. Eight implementation checks passed; 24 capacity/duration fixtures are generated. The arrival order is arbitrary and is not a fairness or competent-review baseline.

The base fixture leaves 90 minutes of unmet service work under all three rules; distribution changes. This is not measured waiting time or actual downstream burden. All demand is served when base-case capacity reaches 210 minutes. The minimum-coverage rule is reported infeasible when capacity cannot support it.

A later extension should test recurring demand, referrals, service outcomes, uncertain durations, and maintenance rather than assuming they were modeled here.

**Computed quantities:** Completions, unmet requests, used/idle minutes, unmet service minutes, and sensitivity to capacity and duration. Waiting burden and service outcomes remain future measurement needs. Publish every assumption and the conditions under which the hypothesized failure disappears.

**Failure signal:** The claimed spillover depends entirely on an arbitrary setup, vanishes under reasonable constraints, or is already captured by the supposedly local objective.

**Boundary:** A toy result can illustrate a mechanism; it cannot estimate prevalence or validate a social program. The canonical code lives in UCF; no duplicate implementation is maintained here.

## T-003 — Added-value comparison

**Editorial pilots completed; independent comparison still unrun.** The [related-work note](notes/related-work.md#candidate-comparison-for-t-003-not-a-completed-study) identifies candidate baselines and fidelity checks. The [T-003 protocol](notes/t003-added-value-protocol.md) freezes the proposed prompt, finding definitions, coding dimensions, burden/privacy measures, null-result criteria, and the distinction between an editorial pilot and independent review. [Pilot 001](notes/t003-editorial-pilot-001-comparison.md) and [Pilot 002](notes/t003-editorial-pilot-002-comparison.md) both produced a near-null result for unique decision-relevant added value from Dynamic Coherence over a competent ordinary incident/system review. These same-model pilots are method-debugging evidence only; no independent reviewer or method-superiority result exists.

The same-case editorial stop rule now applies. The next legitimate step is **an independent reviewer comparison on a different case or a method-fidelity comparison with a properly prepared established method**, not another prompt-tuning pass on the Cloudflare incident. Choose a small, public, non-sensitive design case and a competent existing review method. Compare it with the section 12 procedure using the same information and a comparable review effort. Avoid choosing a case merely because its known conclusion already matches the framework, and avoid giving the new method more evidence while calling its findings an improvement.

**Measure:** Consequential omissions identified, false alarms, traceability, disagreement, reviewer time, and unnecessary information requests. Define “consequential” before evaluating outputs.

**Failure signal:** No useful additional findings, unacceptable burden, unresolvable reviewer disagreement, or more privacy exposure without corresponding benefit.

**Boundary:** Select the baseline and protocol before execution. No experiment, deployment, or participant recruitment is authorized by this plan.

## Next writing pass

C-003 now records the author's provisional direction that coherence can describe a process, or several processes, rather than a destination; it can also admit qualified levels rather than a binary label. The author accepted the actionable-route passage for the current draft: a route need not be complete, but it must create traction, continuity, and accountability rather than merely document or defer the need. The author also rejected calling a seriously coercive arrangement functionally coherent and identified **false coherence** as the existing project term for apparent effectiveness that excludes people, power, or lived consequences from the boundary. Open acknowledgment can improve legibility without making the coercive arrangement coherent; what follows determines whether the process begins moving toward greater coherence. Because “stopping harm” depends on how harm is defined, the draft no longer treats protective action and coercion as opposites or lets one actor's unchallengeable harm claim settle the issue. It also avoids replacing “protective coercion” with another compound label that embeds its own justification. The factual record now uses who, what, to whom, where, when, how, stated why, claimed harm and evidence, and effects before a separate assessment. Uses of authority are decomposed into the particular kind, source, scope, limits, duration, accountability, and review path. The next passage-level question asks whether this expanded record captures the distinction. After that review, ask who can define, challenge, and review harm when urgent action prevents prior agreement. Then compare C-003 with the related-work passages and healthcare case before selecting the bounded task, baseline, and evidence packet for T-003. The targeted comparison is drafted; a full literature review and independent evaluation remain open.

[Charter](README.md) · [Paper](paper.md) · [Claims](claims.md)
