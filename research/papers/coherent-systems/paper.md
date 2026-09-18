# Coherence Is a Systems Property

*Intelligence, Institutions, and the Conditions They Create*

**Root Sequence living paper · v0.1-dev · 2026-09-16**  
**AI-assisted annotated argument; author review pending; not peer reviewed.** This is a developing synthesis with a constructed example and an externally documented case, not a completed paper. Claim identifiers link the argument to the [claims ledger](claims.md). Authorship and release metadata require approval.

## Provisional abstract

Aligning an intelligent system with its operator's objective does not, by itself, establish that its effects are acceptable to those affected by its operation. This paper proposes a relational approach to examining intelligence alongside the institutions, infrastructures, and environments through which it acts. It distinguishes functional performance—whether a system produces specified behavior—from coherence and from normative legitimacy. Coherence also requires relevant relationships, power, affected people, dependencies, and consequences to remain inside the assessment boundary; an effective process that excludes or suppresses them may exhibit false coherence rather than genuine fit. These questions cannot be settled by internal consistency or technical competence alone. The proposed method tracks boundaries, displaced costs, material constraints, disagreement, and the capacity to revise decisions as conditions change. Coherence is treated as a situated direction of inquiry, not a universal score, an inevitable trajectory, or a final state. Optimization remains a useful bounded technique rather than a substitute for choosing and contesting purposes. Speculative scenarios and recovered possibilities are used to generate hypotheses, while evidence and explicit tests determine what can be claimed about the world. The intended contribution is a review procedure and research agenda linking these concerns across scales. This version connects provisional definitions and a constructed example to selected prior work and a published healthcare case. It reports no new field findings, validated measure, or demonstrated advantage over existing approaches.

## 1. The problem is larger than an individual objective

**Anchor: C-001.** Success against an operator's goal is not a sufficient certificate for consequences outside that goal. This is shared ground with existing work, not this paper's discovery: Edelman and colleagues explicitly develop institutional co-alignment, and Gabriel distinguishes technical alignment from questions about its normative target.[^edelman2025][^gabriel2020]

The [related-work comparison](notes/related-work.md) also places this argument beside System-Theoretic Process Analysis (STPA) and its interaction-focused analysis and Selbst and colleagues' critique of abstraction boundaries.[^stpa2018][^selbst2019] We propose to test a documented synthesis, not claim to have discovered systemic analysis.

**To develop:** Specify the system boundary and the parties whose interests are absent from a local objective. Do not caricature AI alignment as uniformly concerned only with obedience.

## 2. Local success can coexist with wider failure

**Anchor: C-001.** A constructed service has 120 available minutes, eight requests requiring 15 minutes each, and two requiring 45 minutes each. Maximizing completions serves eight short requests and no long requests. Requiring at least one of each, then maximizing completions, serves five short and one long request. Both use 120 minutes and leave 90 minutes of requested work unfinished.[^ucf]

The constraint changes access but does not remove scarcity or improve every outcome. Unmet service minutes are not measured waiting time, harm, or another provider's workload. No normative preference between these rules follows from this arithmetic.

At 210 available minutes every request fits in this fixture, and the exclusion disappears. A local objective that already includes the coverage constraint also blocks this specific example. These are boundary conditions, not exceptions to conceal.

Implementation and the full assumptions remain in UCF's [booking-service example](https://github.com/Root-Sequence/universal-coherence-framework/blob/c4d7b236828a59139c0d5204b1faaed13154682a/models/examples/booking-service/README.md), not a second code copy here. Eight implementation checks passed; this establishes properties of a synthetic fixture, not prevalence or validation of UCF. The original counterexample remains a challenge to an unrestricted implication, not a claim that local optimization always fails.

A [published healthcare case](case-studies/healthcare-cost-proxy.md) examines a mismatch between a prediction target and its intended use.[^obermeyer2019] It is external evidence, not a UCF result. Keep the retrospective interpretation separate from the constructed example and from claims about comparative method performance.

**To develop:** Compare with a competent resource-and-impact review; investigate which assumptions carry over to any actual service before making an empirical claim.

## 3. Systems create conditions for subsequent behavior

**Anchor: C-002.** The existing [Intelligence Ecology](../../../concepts/intelligence-ecology.md) asks which behaviors surrounding conditions make viable. This paper treats that as a working frame: permissions, rewards, information access, and resource dependencies may shape what persists without determining every participant's behavior.

Meadows discusses intervention through information flows, rules, and system goals, not just parameter changes.[^meadows] That is conceptual grounding, not proof that a particular redesign will work.

**To develop:** Draw a causal account for one bounded example. Separate environmental effects from selection of different participants and from changes in measurement.

## 4. A working definition, with an explicit boundary

**Anchor: C-003.** The current [coherence model](../../../systems/coherence/model.md) concerns the fit between structure, assumptions, and reality. We retain that diagnostic meaning rather than silently redefining it as goodness.

**Proposed working distinction:** *Functional performance describes whether a system produces specified behavior. Coherence asks whether its assumptions, behavior, dependencies, purposes, relationships, and consequences remain in contact with the conditions in which it operates.*

Normative assessment asks a distinguishable but interacting set of questions: whose purposes are recognized, who bears costs, what authority is legitimate, and what objections remain? A seriously coercive arrangement can be internally consistent and operationally effective while remaining incoherent and illegitimate. Successful target execution establishes functional performance, not coherence. If apparent order depends on domination, suppressed dissent or feedback, hidden externalized costs, or an artificially narrow boundary, this paper calls it **false coherence**. Concealment is not required: “false” describes mistaking controlled stability for coherence. The term describes a mechanism of apparent fit, not merely the author's disapproval.

An action may restrict choice through physical restraint, force, threats, confinement, penalties, withdrawal of access, or other means. “Coercion” should be used only when the specific mechanism supports it, not as the name for every restriction. The action and its justification should not be compressed into reassuring labels such as “protective coercion” or “a necessary agency-limiting intervention.” Record separately what was done and to whom; what harm was claimed, by whom, on what evidence, and with what uncertainty; and how necessity, proportionality, alternatives, authority, duration, challenge, review, and restoration of agency were assessed. Claims of harm cannot be wholly perspective-free, but neither should one actor's private or unchallengeable definition settle them. “Preventing harm” becomes a route to false coherence when the claimed purpose certifies the action in advance or suppresses the people said to be protected.

Acknowledging coercion may improve legibility and revisability, but it does not by itself repair the coerced relationship or restore agency. Like admitting a lie, acknowledgment changes what is openly known; what follows determines whether the process begins moving toward greater coherence. Relevant changes may include ending or reducing the coercion, restoring agency, repairing consequences, accepting accountability, and changing conditions that would reproduce the harm. Treating admission itself as resolution can become another layer of false coherence.

This is not a two-stage process in which value-free engineering comes first and ethics is attached later. Gabriel's analysis challenges the independence of technical and normative choices; Selbst and colleagues likewise challenge treating contextual social concepts as self-sufficient technical properties.[^gabriel2020][^selbst2019] C-003 therefore distinguishes questions without claiming that they can be answered independently.

The definition is now explicitly compared with UCF's earlier model and glossary and its [proposed v1.1 revision](https://github.com/Root-Sequence/universal-coherence-framework/blob/c4d7b236828a59139c0d5204b1faaed13154682a/models/ucf-model-v1.1-draft.md). UCF supplies four analytical layers: internal, inter-agent, systemic, and temporal. These are distinct from its optional Chaos, Tension, Flow, and Unity labels. The paper may use the layers without assuming the labels form a universal taxonomy.[^ucf]

A definition becomes operational only when an application specifies observations, rules, and uncertainty. The [reconciliation note](notes/ucf-reconciliation.md) maps the distinctions and their provenance; it does not claim independent evidence for UCF.

A supported and revisable response may be coherent in how it handles a constraint even when it cannot resolve that constraint. That description applies to the handling process; it does not turn an unmet need into a successful outcome. A system may contain several interacting processes whose assumptions, consequences, and capacity to adapt differ, so one overall label should not erase those differences. Coherence is not binary: within a stated boundary, developing an actionable route toward an unmet need can be more coherent than only documenting it. This is a qualified comparison, not a universal score, and improvement in one process does not cancel failure in another.

A route need not be complete to be real. A process moves toward an actionable route when it changes the conditions surrounding an unresolved need so that a consequential next step becomes more possible, supported, or accountable. This may involve identifying a feasible action, connecting the need to relevant authority or resources, creating a credible escalation path, or clarifying what must become true next. The need should remain visible, responsibility and limitations should remain traceable, and the burden of continuation should not simply be transferred to those already affected. An escalation without traction, continuity, or accountability is deferral rather than a route.

**To develop:** Four contrasting cases have received an AI-assisted editorial pass, not independent review. Test whether reviewers can identify why an effective but coercive arrangement exhibits false coherence and why a protective but unreliable arrangement still fails functionally, without hiding either defect in one aggregate label.

## 5. Values and disagreement are not noise

**Anchors: C-004, C-008.** Gabriel's account makes disagreement over alignment's moral target part of the problem.[^gabriel2020] Our proposed procedure therefore records disagreement rather than treating apparent agreement as sufficient evidence of legitimacy.

The existing [collective-judgment analysis](../../../analysis/collective-judgment-and-manufactured-consensus.md) supplies project provenance for distinguishing judgment, deliberation, and authorization. These are design commitments requiring scrutiny, not a demonstrated universal decision rule.

**To develop:** Who can participate, object, refuse, appeal, or leave? Whose absence is consequential? How can necessary collective action proceed without representing dissent as resolved?

## 6. Optimization within boundaries, not “coherence versus optimization”

**Anchor: C-005.** Optimization can be useful when objectives, constraints, and validity limits are appropriate. Manheim and Garrabrant distinguish mechanisms by which stronger pursuit of a proxy can fail.[^manheim2019] That does not imply that every metric or optimization task is harmful.

The proposed change is in the surrounding review: who chooses the target, what is left out, what constrains it, and when is it revised? A multi-objective or constraint-based method may already address part of this problem. Calling something “coherence” does not remove the need for concrete mechanisms.

## 7. Coherent conditions, not guaranteed outcomes

**Anchors: C-006, C-007.** We propose evaluating changes partly by whether they preserve or improve the conditions for correction, participation, maintenance, and adaptation. This does not justify replacing outcomes with another untested proxy called “conditions.” Both must be examined.

“Directional” means a context-specific comparison, including qualified judgments of more or less coherence, not a universal scalar or an inevitable, monotonic journey. Coherence is treated here as ongoing work across multiple interacting processes, not a single destination. A repair may improve one relationship while worsening another, and some mixed outcomes may not support an overall ranking. This paper neither proves a final coherent state impossible nor assumes that one is attainable. It does not require such a state to motivate a bounded change.

**To develop:** Specify what improved, for whom, over what period, what deteriorated, and what remains unknown.

## 8. Advanced intelligence as a conditional change in possibilities

**Anchor: C-009.** More capable tools might change the cost or feasibility of some coordination tasks. Whether that happens is a hypothesis requiring task-specific evidence; it does not establish a timeline for AGI or an automatic direction of social change.

Greater capability alone supplies no guarantee of benevolence, malevolence, legitimate authority, or shared benefit. More coordination capacity could also make intrusive control easier. Some proposed improvements may require no advanced AI at all.

**To develop:** Name a task, its current bottleneck, a non-AI baseline, and the evidence that an AI-based intervention changes that bottleneck without merely transferring burdens.

## 9. Agency, plurality, and the limits of decentralization

**Anchor: C-008.** We propose checking actual decision rights and dependencies rather than inferring agency from labels such as “decentralized.” Separate nodes may still share one maintainer, infrastructure provider, or permission bottleneck. Conversely, a shared service need not erase meaningful local choice.

**To develop:** Compare specific failure modes, coordination costs, accessibility, exit costs, and authority. No architecture receives an automatic normative or performance endorsement.

## 10. Imagination as hypothesis generation

**Anchor: C-010.** [Futures research](../../../futures/README.md) distinguishes scenarios from forecasts and fictional exploration. We propose using scenarios to identify assumptions that ordinary extrapolation leaves unchallenged, then extracting testable questions from them.

Coherent World and *No One Noticed* can contribute questions and experiences to imagine. They do not demonstrate feasibility, establish predictions, or supply consent for a real intervention. Recovering an abandoned possibility requires investigating why it was abandoned, including technical or ecological objections—not assuming every unrealized idea was viable.

**To develop:** Produce contrasting scenarios, identify their added assumptions, and discard or revise those contradicted by evidence.

## 11. Transition through changes in conditions

**Anchor: C-011.** A transition proposal should describe dependencies and intermediate states rather than only its desired endpoint. Incremental changes may help, conflict, stall, or create lock-in; some changes may need coordinated discontinuities.

For a hypothetical shift from car-dependent access to other forms of access, ask what exists before dependence is reduced: accessible alternatives, capacity, maintenance, emergency access, and options during failure. This is a hypothetical dependency analysis, not an empirical result.

Changing financing does not eliminate requirements for energy, materials, time, physical access, ecological limits, or agreement about burdens.

## 12. Proposed review procedure and research agenda

**Anchor: C-012.** The first candidate procedure is a short written assessment, not a numerical coherence score:

1. **Boundary and purpose:** What is changing, whose purposes count, which dependencies and timescales are included, and what is excluded?
2. **Conditions and consequences:** Which assumptions must hold; what material limits, feedback, displaced costs, and failure modes matter?
3. **Authority and difference:** Who can authorize, contest, refuse, or revise; what disagreement and privacy constraints remain?
4. **Comparison and revision:** What baseline and alternative are considered; which outcomes would contradict the claimed improvement; when does review occur?

Test whether this procedure identifies consequential omissions beyond an existing competent system review. Do not compare it only with an artificially weak checklist. Record reviewer effort, disagreement, false alarms, and failures to detect known issues.

The [comparison plan](notes/related-work.md#candidate-comparison-for-t-003-not-a-completed-study) identifies STPA as a candidate method to examine where appropriate. STPA already specifies boundaries, stakeholder losses, feedback, and causal scenarios.[^stpa2018] We must check baseline fidelity and use equivalent information before claiming additional value. A retrospective reading of a known case is not a blinded discovery test.

The [research questions](open-questions.md) distinguish three activities. T-001 has an initial editorial set of fictional cases, but no independent reviewer study. T-002 now has a reproducible synthetic model in UCF. T-003, the added-value comparison against a competent baseline, has not been run. These statuses do not amount to empirical validation.

## Limitations and counterarguments

**Possible relabeling.** Systems engineering, sociotechnical alignment, participatory design, and other traditions may already supply these tools. A literature review and a comparative evaluation are necessary before claiming added value.

**Ambiguous boundaries.** “The wider system” can expand indefinitely. The method needs a stopping rule and an account of consequential exclusions.

**Normative smuggling.** A definition that builds every desired value into coherence risks circularity. This draft separates descriptive fit from explicitly contestable commitments, but does not resolve disagreements about those commitments.

**Measurement and surveillance.** More complete information is not automatically justified. Collecting intimate values or disagreement histories could create new risks. Any study must justify data needs and refusal options.

**Representation and burden.** Review procedures can exclude people through time, language, expertise, or accessibility demands. Participation itself can become a cost imposed on those already affected.

**Coordination and urgency.** Distributed authority, reversibility, and repeated review have costs; some decisions are time-sensitive or cannot be undone. The proposal must handle these cases instead of treating them as exceptions to be ignored.

**Conditional improvement.** A useful result in one bounded task does not validate a universal theory or a whole imagined society. Null results and counterexamples must remain part of the record.

## AI assistance and review status

ChatGPT assisted with research organization, source discovery, substantive drafting and critique, and the earlier synthetic-example code. Source inspection and implementation checks do not stand in for the author's judgment or independent review. Those reviews remain pending. The [AI-assistance record](AI-ASSISTANCE.md) states the scope, reproducibility limits, and approval checkpoint; no approved byline or submission is inferred from this draft.

## References

[^edelman2025]: Joe Edelman et al. (2025), *Full-Stack Alignment: Co-Aligning AI and Institutions with Thick Models of Value*, arXiv:2512.03399v1. [Source](https://arxiv.org/abs/2512.03399v1). Position paper; not proof of institutional outcomes.
[^gabriel2020]: Iason Gabriel (2020), *Artificial Intelligence, Values and Alignment*, arXiv:2001.09768v2; published in *Minds and Machines*. [Source](https://arxiv.org/abs/2001.09768v2). This pass examined selected full-text passages in sections 2–3 and the opening of section 4; see the source map for coverage.
[^manheim2019]: David Manheim and Scott Garrabrant (2018; revised 2019), *Categorizing Variants of Goodhart's Law*, arXiv:1803.04585v4. [Source](https://arxiv.org/abs/1803.04585v4).
[^meadows]: Donella Meadows, *Leverage Points: Places to Intervene in a System*. [Author archive](https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/). Consulted 2026-09-16; used as conceptual framing rather than a tested recipe.

[^ucf]: Root Sequence, *Universal Coherence Framework*, proposed model reconciliation and booking-service example, revision `c4d7b236828a59139c0d5204b1faaed13154682a` (2026-09-16). [Source](https://github.com/Root-Sequence/universal-coherence-framework/blob/c4d7b236828a59139c0d5204b1faaed13154682a/docs/reconciliation-2026-09-16.md). Internal project provenance and constructed analysis; AI-assisted and awaiting author review, not independent corroboration.

[^stpa2018]: Nancy G. Leveson and John P. Thomas, *STPA Handbook* (March 2018), chs. 1–2, selected passages. [MIT-hosted handbook](https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf). Methodological reference, not an evaluation conducted here.
[^selbst2019]: Andrew D. Selbst, danah boyd, Sorelle A. Friedler, Suresh Venkatasubramanian, and Janet Vertesi, *Fairness and Abstraction in Sociotechnical Systems* (2019), sections 2.1–2.5. DOI: `10.1145/3287560.3287598`. [Author-hosted paper](https://sorelle.friedler.net/papers/sts_fat2019.pdf).
[^obermeyer2019]: Ziad Obermeyer, Brian Powers, Christine Vogeli, and Sendhil Mullainathan, *Dissecting racial bias in an algorithm used to manage the health of populations*, Science 366(6464), 447–453 (2019). DOI: `10.1126/science.aax2342`. [Author-hosted article](https://sendhil.org/wp-content/uploads/2020/01/Publication-67.pdf). Interpretation and reading limits are recorded in the case note; no replication was performed.
