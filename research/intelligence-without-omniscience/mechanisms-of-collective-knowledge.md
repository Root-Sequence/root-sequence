# Mechanisms of collective knowledge: from information to effective action
## Source-aware causal questions, competing explanations, and a first bounded probe

**Document role:** Focused mechanism investigation linked to [Intelligence Without Omniscience](README.md).  
**Status:** WORKING / AI-assisted / review pending — 2026-10-07.  
**Epistemic boundary:** Do not confuse original source results, illustrative mathematics, proposed mechanisms, or causal claims about actual groups.  
**Method:** [Root Sequence Research Method](../method.md) — preserve → decompose → route → compare competent baselines → test → revise.  
**Idea Trails:** Intelligence & Authority; Collective Judgment & Dissent; Commons & Shared Capacity; Accessibility & Participation.  
**Trail role:** research  
<!-- idea-trails: intelligence-authority, collective-judgment-dissent, commons-shared-capacity, accessibility-participation -->
<!-- trail-role: research -->

> A group can hold information sufficient for a better judgment yet fail to use it. That sentence names an outcome, not a single mechanism.

## 1. The causal distinction

A *heuristic, non-universal* chain of constraints:

\`\`\`text
world / problem / affected actors
          ↓
observation, information creation, documentation
          ↓
findability and knowledge / expertise routing
          ↓
willingness and permission to disclose
          ↓
communication, translation, representation
          ↓
source/evidence assessment and error checking
          ↓
integration into the working model
          ↓
critical uptake / reconsideration of problem or options
          ↓
legitimate authorization, resources, and implementation
          ↓
consequences, maintenance, feedback, change in future conditions
          ↺
\`\`\`

The real processes are non-linear. Actors can act without all knowledge; a sound objection may be rejected for legitimate reasons; private or community-governed knowledge may never be disclosed. The stages are diagnostic *distinctions* that can be reordered or bypassed, not a compulsory participation pipeline.

This is especially important where the same observed outcome—an institution ignores a useful fact—could arise from incompatible causes:
- no one observed it;
- it was not discoverable;
- the knowledgeable actor did not share it;
- the speaker was prevented from participating;
- translation distorted its meaning;
- prejudice reduced warranted credibility;
- the claim was evaluated and reasonably rejected;
- it was accepted but the institution lacked authority or resources to act;
- interests or incentives favored a different outcome.

The remedy depends on which mechanism is present, who controls it, and whether proposed remediation creates new burdens or coercion.

## 2. Mechanisms worth keeping separate

| ID | Mechanism | Domain baseline | Observable signature | Candidate intervention | Failure case |
| --- | --- | --- | --- | --- | --- |
| M01 | Shared information repeatedly dominates discussion | Hidden-profile literature | High shared-fact talk; low unique-fact **coverage** | Ask separately for potentially unique evidence | Less coverage does not by itself establish harm; the unique evidence may be irrelevant |
| M02 | Unknown or incorrect map of expertise | Transactive memory / organizational knowledge | Questions fail to reach holders, or reach misleading ones | Scoped expertise/source directory; check freshness | Stale directory can be worse than informal routing |
| M03 | Strategic withholding or unsafe disclosure | Social psychology / power and consent | Selective silence under competition, fear, or privacy concerns | Incentive changes, safe alternatives, paid consultation | Forced disclosure and surveillance create harm |
| M04 | Evidence credibility misallocated | Social epistemology, expert-assessment methods | Sound evidence discounted or unreliable claims elevated | Source-context evaluation and independent challenge | Treating testimony equally regardless of relevance is not justice |
| M05 | Message/representation loss | HCI, classification, boundary-object studies | Summary loses conditions, restrictions, dissent | Source-linked, contestable representations | Additional translation work overwhelms participants |
| M06 | Correct knowledge has no *uptake* | Longino, organizational learning | Objection logged but institutional model cannot revise | Review conditions that actually permit revision | Feedback theater or endless procedure |
| M07 | Correct recommendation cannot become legitimate action | Capability approach, governance, material analysis | Correct answer but no resources, access, consent, or authorization | Address specific conversion and decision rights | Accuracy is used to justify unaccountable authority |
| M08 | Outcomes reshape the conditions of future knowledge | Path dependence / institutional and cultural evolution | Access, trust, maintenance, incentives, or capacity change after action | Compare future action space, maintenance, governance | Temporary improvement creates brittle dependency |
| M09 | False independent corroboration | Source criticism, reproducibility | Multiple apparent sources inherit one weak original | Claim-level lineage and truly independent checking | "Many citations" laundering one error |
| M10 | Explanatory fluency mistaken for verified understanding | Illusion of explanatory depth, human-AI reliance | Confidence grows without independent verification ability | Calibrated source-linked explanation or review | Compulsory testing excludes legitimate assisted users |

These IDs are a **local investigation aid**, not new canonical Root Sequence vocabulary or a scientifically validated ontology.

## 3. What external evidence currently warrants

### Shared versus unshared information (M01)

The [Lu, Yuan & McLeod 2012 meta-analysis](https://pubmed.ncbi.nlm.nih.gov/21896790/) covers 65 studies and 3,189 groups. Groups discussed considerably more commonly held than unique information; **unique-information coverage**, rather than merely the proportion of discussion about unique information, was more strongly related to decision quality in those studies. It also found that communication medium did not, by itself, significantly affect unique information pooling or decision quality.

**Interpretation:** facilitating more talking or shifting media is not an adequate mechanism claim. A probe should measure which decisive information became available and whether it actually changed the decision process.

### Incentives and strategic disclosure (M03)

[Toma & Butera 2009](https://pubmed.ncbi.nlm.nih.gov/19332434/) report that competition, compared with cooperation in their hidden-profile experiments, fostered withholding of unshared information and less use of preference-disconfirming evidence. Their analysis identified reluctance to use disconfirming information as part of the difference in decision quality. This supports testing **sharing** and **belief revision** separately, without extrapolating an exact probability to a real setting.

### A counterexample to procedural optimism (M06)

A [hidden-profile experiment with organizational board members, published 2021](https://www.sciencedirect.com/science/article/pii/S0025174721000434) found that the particular structured discussion procedures improved perceived consideration of pros and cons but did not improve objective decision quality. The result is task- and procedure-specific.

**Inference:** apparently thoughtful deliberation is not enough. We must record accuracy, information coverage, source integrity, material consequences, and participant burden—not merely meeting satisfaction or confidence.

### Recent AI agents (M01, M02, M04)

[Li, Naito & Shirado, ICML 2026, *Systematic Failures in Collective Reasoning under Distributed Information in Multi-Agent LLMs*](https://proceedings.mlr.press/v306/li26ej.html) introduces HiddenBench (65 tasks, 15 models). The reported 30.1% multi-agent distributed-information versus 80.7% single-agent full-information scores compare **different access to information**, not inherent group-vs-individual cognition under an equal-information design. The authors find premature convergence around shared evidence and improvements from a lightweight structured communication protocol.

This is an especially relevant empirical benchmark but does not authorize copying its scores into a fictional society model. Its mechanism remains bounded to the evaluated configurations, prompts, tasks, and versions.

### Expertise maps, motives, and what happens *after* information is shared

[Van Ginkel & Van Knippenberg (2009)](https://doi.org/10.1016/j.obhdp.2008.10.003) experimentally examined knowledge of distributed expertise, group task representations, reflection, and information elaboration (reported N=125; the abstract does not clarify the unit of the sample size). Their results distinguish awareness of **who knows what** from how the group frames and uses that knowledge. This constrains a simple "make an expertise directory" proposal: the directory may be useful through changing task interpretation, not just through direct retrieval.

[Toma, Vasiljevic, Oberlé & Butera (2013)](https://pubmed.ncbi.nlm.nih.gov/22577834/) examined expertise assignment combined with cooperative versus competitive goals in hidden-profile groups. Assigning experts supported information pooling with cooperative goals but **reduced it under competitive goals**. A system must examine whether expertise labels change status competition and willingness to contribute.

[Xiao, Zhang & Basadur (2016)](https://doi.org/10.1016/j.jbusres.2015.05.014) investigate the gap between information sharing and its actual use in new product development decisions. Their findings caution against making *fact coverage* stand in for adequate information integration, especially with unequally distributed information.

These empirical studies do not guarantee any intervention will work outside their investigated tasks. They also show why the attractive claim "just ask the right person" is not sufficiently specified.

## 4. First mechanistic probe: hidden information under a fixed message budget

**Location:** the private [Coherent World mechanism probe 001](https://github.com/Root-Sequence/coherent-world/blob/research/intelligence-without-omniscience-2026-10/simulation/scenarios/distributed-intelligence/MECHANISM-PROBE-001.md). This is a *paper calculation*, not a new world simulator, study of real participants, or independent validation.

### Predeclared toy assumptions

- A bounded problem has **two separate critical facts** known to distinct participants. Getting both into the shared record is *necessary* (not sufficient) for a defensible decision.
- **Ordinary discussion:** each of four independent information turns is spent repeating shared facts with probability \`s\`. Otherwise the turn attempts one of the two critical facts with equal chance; it is disclosed with probability \`d\`.
- **Targeted protocol:** within the same overall four-turn allowance, two turns explicitly ask the presumed holders of the critical facts. Each route is correct with probability \`r\`; if routed correctly, the fact is disclosed with probability \`d\`. The other two turns remain for checking or assessment, but their usefulness is **not modeled**.
- These probabilities are **invented sensitivity parameters**, not estimates inferred from the psychological or AI studies. The model ignores message content, source validity, learning, strategic adaptation, unequal costs, and legitimate authorization.
- The outcome is narrowly defined as **both facts surfaced**. It is not group intelligence, correct inference, wellbeing, or legitimate action.

Let \`q = (1-s)d/2\` be the probability that any ordinary turn yields a particular critical fact. Assuming independent turns, inclusion–exclusion gives:

\`\`\`text
P(both critical facts surfaced in n ordinary turns)
  = 1 - 2(1-q)^n + (1-2q)^n

P(both surfaced after two accurately routed, independent requests)
  = (r*d)^2
\`\`\`

For the fixed baseline \`n=4\`, the illustrative sensitivity cases are:

| Condition | Shared-fact repetition \`s\` | Disclosure \`d\` | Routing \`r\` | Ordinary | Targeted |
| --- | ---: | ---: | ---: | ---: | ---: |
| A: high repetition, accurate routing | 0.80 | 0.90 | 1.00 | **8.06%** | **81.00%** |
| B: less repetition, poor routing | 0.50 | 0.90 | 0.60 | **37.00%** | **29.16%** |
| C: no disclosure | 0.80 | 0.00 | 1.00 | **0.00%** | **0.00%** |
| D: extreme repetition | 0.95 | 0.90 | 1.00 | **0.58%** | **81.00%** |

Calculations were checked against exhaustive enumeration of the three multinomial categories (common, fact A, fact B) for four ordinary turns, rather than relying only on sampled Monte Carlo trials. Values are rounded for readability.

### What the probe demonstrates *conditionally*

1. If unique facts are repeatedly overlooked, asking their actual holders can dramatically improve **fact exposure**.
2. If the expertise map is sufficiently unreliable, targeted routing may perform worse than ordinary exploration (case B). Structured processes are not guaranteed improvements.
3. If no disclosure is possible, neither protocol surfaces the facts (case C). Silence might be due to privacy, coercion, lack of safe channels, or simply missing knowledge; the model does **not** diagnose which.
4. Even perfect exposure does not establish reliability, integration into the working model, authorization, or downstream benefit.

### The toy's especially consequential confound

The targeted-query condition already knows, by design, that **two** critical facts exist and which putative knowledge-holders to ask. The ordinary condition is not given an equivalent task-specific missing-fact map. Thus the comparison can isolate neither generic discussion structure nor independent intelligence: it partly reflects **privileged knowledge of what to seek**. A fair next study must give both conditions the same specialist roster and neutral topic list, while varying only whether a structured solicitation step occurs. How accurately participants know the distribution of unique information should be a **separate randomized factor**. Include a case with **no decisive unique fact**, so solicitation may add overhead without benefit.

The model also ignores source validity, use of information after transmission, and incentives. It is an *analytic sensitivity illustration*, not a positive experimental result about groups.

### What it cannot establish

- No study of humans or LLMs was executed.
- It does **not** prove that real groups repeat shared information with \`s=0.8\`, disclose with \`d=0.9\`, or route with \`r=0.6\`.
- A two-fact toy is not general intelligence, political deliberation, or a whole social system.
- The protocols do not have proven equal cognitive/verification costs, even if their *message allowances* match.
- Real sources can be correlated or misleading, and facts can be disputed, private, or irrelevant.
- When task success requires factors beyond both facts, probability of correct action is *at most* the calculated fact-coverage probability; it may be much lower.
- The toy is evidence only of the stated mathematical relationship given its assumptions.

### Immediate falsification / narrowing direction

A next protocol should manipulate **one mechanism at a time**:

- Same actor partitions, task, time, and information → change *only* method of eliciting unique facts.
- Same elicitation method → change expertise map accuracy.
- Same routing and facts → vary privacy, compensation, safety, and willingness to disclose.
- Same acquired evidence → change which conclusions are warranted; include **false, low-quality, or non-independent** evidence.
- Same correct conclusion → vary institution's authority/resources, to separate knowing from acting.
- Introduce a new task family to test transfer, rather than simply redescribing the same facts.

Compare against existing best-practice review; report null/negative effects and all extra work imposed on participants.

## 5. Evidence integrity: what if six citations come from one source?

This is developed as an explicit synthetic trace in the private Coherent World [Mechanism Probe 002](https://github.com/Root-Sequence/coherent-world/blob/research/intelligence-without-omniscience-2026-10/simulation/scenarios/distributed-intelligence/MECHANISM-PROBE-002.md). It is an authored paper exercise, not a set of real documents or an AI test.


An institution sees three apparently independent reports supporting a proposal. All three copied one original inference. A fourth source raises an independent objection.

The count is 3 versus 1, but the number of **independent evidential lineages** could be 1 versus 1. That is not a tie on truth; each original must be assessed on its actual evidence and method.

Possible intervention: attach *claim and evidence lineage* to summaries and recommendations, with careful access restrictions. Counting lineages is neither a substitute for validating source quality nor a reason to reveal sensitive source identity.

This mechanism is distinct from hidden-profile fact elicitation: unique evidence can be surfaced and still misweighted by falsely duplicated citations.

See [Epistemic Trust and Collective Verification](epistemic-trust-and-collective-verification.md).

## 6. Why the Root Sequence synthesis might be redundant

Competent information-sharing protocols, methods for vetting expertise, accessibility audits, source criticism, participatory research, and institutional decision procedures already exist.

The research contribution here is currently **cross-field routing and a clear diagnostic separation**, not a new general intelligence theory. It adds value only if a case analysis discovers a consequential gap that native methods *in combination* did not already reveal, or provides a demonstrably useful route to the correct native method.

Test against:
- ordinary competent source/decision audit;
- the appropriate domain's access and participation audit;
- a baseline hidden-profile protocol;
- an independent expert review with dissent recorded.

A **null** result or an inefficient new protocol would narrow or retire the proposal.

## 7. Relationship to intelligence infrastructure and agency

Better cognitive infrastructure may help a person find knowledge, locate a specialist, critically understand it, or apply it under real constraints. It can also extract consent-sensitive knowledge, hide source manipulation, centralize authority, and impose unpaid explanation burdens.

Relevant conceptual homes are preserved:
- [Epistemic Discoverability](../../concepts/epistemic-discoverability.md) — term and field routing.
- [Intelligence Ecology](../../concepts/intelligence-ecology.md) — what system design and environments reward or select.
- [From Knowledge to Uptake](from-knowledge-to-uptake.md) — critical responsiveness, boundary objects, framing, and epistemic labor.
- [Epistemic Injustice and Knowledge Recognition](epistemic-injustice-and-knowledge-recognition.md) — testimonial/hermeneutical injustice, silencing, and interpretation.
- [Intelligence Commons](intelligence-commons.md) — access, governance, consent, and distribution of useful capabilities.
- [Epistemic Trust and Collective Verification](epistemic-trust-and-collective-verification.md) — evidence independence, warranted reliance, expert assessment.
- [Epistemic Contrast](../methods/epistemic-contrast.md), [Deliberative Inquiry](../methods/deliberative-inquiry.md), and the [Research Method](../method.md) remain the **methods**; do not replace them with a new compulsory checklist.

### A third separation: accurate knowledge that still cannot yield action

The private Coherent World [Mechanism Probe 003](https://github.com/Root-Sequence/coherent-world/blob/research/intelligence-without-omniscience-2026-10/simulation/scenarios/distributed-intelligence/MECHANISM-PROBE-003.md) holds one fictional, correct observation fixed while changing *reception*, *institutional uptake*, *available means*, *authority/consent*, and *whether goals can be challenged*. No empirical simulation was run. It illustrates why better information cannot automatically solve institutional or material constraints.

It is motivated by [Longino's norms of scientific uptake](https://plato.stanford.edu/entries/scientific-knowledge-social/), the [capability approach's resource-to-opportunity conversion factors](https://plato.stanford.edu/archives/fall2025/entries/capability-approach/), and a [2024 critique distinguishing goal-level from within-goal criticism](https://doi.org/10.1016/j.shpsa.2024.02.005). The philosophical analogy does not assign scientific epistemic communities automatic political authority over citizens or communities.

## 8. What to investigate next

**Already examined analytically, not empirically:**

- **Probe 001 (M01/M02/M03):** exact fact-coverage probabilities given *invented* sampling, disclosure and routing assumptions. The targeted protocol has an important missingness-map advantage that must be controlled before claiming causality.
- **Probe 002 (M04/M09):** an invented evidence-lineage trace distinguishes multiple citations from independent support without presuming which source is correct.
- **Probe 003 (M06/M07):** a counterfactual separates reception, uptake, means, authority, consent, and who can change a goal, without claiming empirical validity.

**Next useful work:** a frozen, **fairly controlled** comparison where the experimental and baseline groups have exactly the same task, neutral specialty map, information budget, and materials; the only initial manipulation is whether unshared relevant facts are actively solicited. Include an irrelevant-unique-information negative control and a false but confidently stated unique item. Compare both groups against competent ordinary expert review, record labor and disclosure rights, and accept a null outcome.

**Second priority:** an origin-aware evidence assessment pilot that distinguishes source lineage, independent checking, and perceived repetition without presuming source counts establish credibility.

**Then:** analyze incentives and safe disclosure (M03) and investigate whether learning transfers across an unrelated task family rather than overfitting a single contrived scenario. Real participant studies require independent design, consent, and appropriate ethical review.

Do not operationalize private resident histories or override Coherent World's Neighborhood v0.2 briefing and first human playtest. All new fictional neighborhood values must be separately approved before incorporation into the game.
