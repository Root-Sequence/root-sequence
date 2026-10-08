# Epistemic injustice and knowledge recognition
## When relevant knowledge is present but fails to change the system

**Role:** Focused research extension of [Intelligence Without Omniscience](README.md).  
**Status:** PROVISIONAL / source-aware, AI-assisted / author review pending, 2026-10-07.  
**Boundary:** A case-specific injustice claim needs evidence about prejudice, social power, interpretive resources, or silencing—not merely an unsuccessful conversation.

## The first distinction: information deficit or recognition failure?

These are different diagnostic possibilities:

| Mechanism | Example of failure | What to investigate |
| --- | --- | --- |
| Absent information | Nobody has measured whether the route is accessible | How should evidence be gathered, with whose consent and at whose expense? |
| Hidden information | One participant has relevant information, but the meeting repeats what is already shared | Which deliberative protocol exposes unique information? |
| Failed discoverability | The answer is documented, but nobody knows the search term | Can questions route to the relevant field or source? |
| Failed comprehension | A finding is presented in inaccessible language or format | Can the representation change without altering the claim? |
| Unjust credibility deficit | A credible witness is discounted due to prejudice | What evidence of biased credibility allocation exists? |
| Interpretive exclusion | A system's available categories obscure an important experience | Who shaped the categories and who is disadvantaged by them? |
| Refusal to recognize others' interpretive resources | Marginalized communities have developed useful concepts that dominant institutions refuse to acknowledge | Is ignorance maintained despite available interpretive resources? |
| Fear-driven withholding | Someone restricts what they say because the audience is unsafe or incompetent to receive it | What structural consequences make truthful testimony risky? |
| Normative conflict | Everyone understands the facts but disagrees about acceptable tradeoffs | What values and legitimate authority must be adjudicated? |

These failure modes can coexist; their remedies differ.

## Fricker's distinction

In *Epistemic Injustice* (2007), Miranda Fricker identifies **testimonial injustice** (a prejudice-caused credibility deficit) and **hermeneutical injustice** (unfair impediments to understanding or communicating significant social experience caused by structural gaps in shared interpretive resources). [Oxford University Press](https://doi.org/10.1093/acprof:oso/9780198237907.001.0001).

**Testimonial example (hypothetical):** A maintenance worker reports recurrent equipment faults. Investigators disregard the report because of prejudice against the worker's background, even though the worker has direct evidence and an appropriate track record. The wrong is to the worker as a knower; it can also lower investigative quality. If investigators independently verify the observation and find it false, that is not by itself epistemic injustice.

**Hermeneutical example (hypothetical):** An institution offers categories that cannot capture a pattern of exclusion experienced by affected participants. The absence of adequate shared interpretive tools prevents a fair hearing. This is more than confusion; the structural distribution of interpretive power matters.

## Beyond Fricker

**Kristie Dotson:** Silencing can arise not only when testimony is rejected but when audiences repeatedly fail to meet speakers' vulnerability to misunderstanding. Dotson describes *testimonial smothering*: people constrain what they tell audiences they reasonably expect to be unable or unwilling to hear safely. [Dotson 2011, Hypatia](https://doi.org/10.1111/j.1527-2001.2011.01177.x). Do not infer a specific person's internal decision without their account or evidence.

**Gaile Pohlhaus Jr.:** *Willful hermeneutical ignorance* concerns dominant knowers' refusal to recognize interpretive tools developed by marginalized knowers. This challenges any suggestion that marginalized people necessarily lack the words or concepts—they may have them, while institutions refuse to engage. [Pohlhaus 2012, Hypatia](https://doi.org/10.1111/j.1527-2001.2011.01222.x).

**José Medina:** Active ignorance and epistemic friction: different social positions can reveal blind spots, but dialogue requires humility and openness, and power relations must be taken seriously. [Medina 2013](https://doi.org/10.1093/acprof:oso/9780199929023.001.0001).

**Hidden-profile experimental research:** Group participants may each possess part of a solution and still fail to combine their information. A meta-analysis of 65 studies (3,189 groups) reported large deficits in unshared-information coverage and decision success in the studied hidden-profile paradigm. These experiments concern defined group tasks, not a universal measure of all human discussion. [Lu, Yuan & McLeod 2012](https://pubmed.ncbi.nlm.nih.gov/21896790/).

**Important difference:** hidden profiles are primarily a failure of information integration; epistemic injustice is a wrong involving credibility or interpretive power. Their consequences can intersect without becoming the same mechanism.

## How AI can compound or interrupt these mechanisms

Potential failure modes to test, not assume:
- An AI retrieval system privileges well-indexed institutional documents and omits local testimony.
- A summarizer produces a consensus narrative by omitting a minority's evidence or unresolved objection.
- A model translates testimony into official categories that lose the concern's original meaning.
- Source rankings reward perceived authority over direct evidence.
- A recommendation interface makes it unclear who authorized the resulting decision.
- Users selectively disclose less because the model or its operator is not trusted with sensitive context.
- A model confidently invents an explanation of a person's testimony and substitutes that for the account.

Possible interventions:
- Record what was actually said, what the assistant inferred, and what it remains unable to determine.
- Attach claim-level provenance and uncertainty.
- Expose alternative categorizations and allow people to reject a proposed paraphrase.
- Invite independent initial assessments before displaying model conclusions.
- Provide a way to dispute the framing, not merely choose among offered options.
- Prevent one assistant from being the only path to evidence or appeal.
- Preserve refusal, selective disclosure, and deletion where legitimately available.

None of these guarantees justice or scientific accuracy. Privacy can conflict with preserving a complete record; giving everyone unlimited review work can make participation impossible. Evaluate burdens and tradeoffs.

## A concrete Coherent World case

A fictional neighborhood seeks to improve early morning transit.

- The transit office possesses a schedule that seems to satisfy service targets.
- A rider knows the destination requires *arrival* by 07:00, not *departure* at 07:00.
- A disabled resident knows an apparently compliant curb approach is not continuously passable.
- A small business knows an alternative loading window is infeasible for perishable deliveries.
- A maintainer knows an upgrade depends on vehicles and spare parts that are not funded.
- The official planning interface recognizes average throughput but not all these situated constraints.

**Question A — hidden profile:** does any group with all these individuals available still overlook unique facts in discussion?

**Question B — epistemic injustice:** are some accounts unfairly discounted due to prejudicial assumptions, or are crucial experiences systematically absent from official categories? This requires separate evidence; mere omission is not enough.

**Question C — material conditions:** can the group act on corrected information? Who has budget and authorization?

**Question D — authority:** does accurate AI synthesis become a de facto veto over affected participants?

**Question E — temporal effects:** does today's solution make future independent action easier or more constrained?

Compare at least four protocols: unstructured discussion; explicit unique-information solicitation; evidence/provenance mapping; and AI-supported mapping with protected independent judgment. Hold participant information and resource budgets stable where plausible, add a misleading but plausible source, and record failures as well as improvements.

## Qualitative evaluation prompts

- What relevant evidence was available but never mentioned?
- What was mentioned but judged irrelevant—and on what grounds?
- Who decided what question the group was permitted to answer?
- How did the interface choose, translate, or erase categories?
- Which participant or source was treated as an expert, and for which claim?
- Was a disputed assertion empirically testable, value-dependent, or an authority question?
- What could a participant safely decline to disclose?
- Which group members could revisit a decision after observing harm?
- Who could request an alternate explanation or challenge the AI's proposed synthesis?
- If more information had been recognized, would the decision have changed, and why?
- Did the new process consume unreasonable amounts of time, care, or unpaid labor?

## Missing knowledge isn't automatically nonexistent knowledge

A connected but **distinct** investigation concerns the meaning of a missing record, a non-response, or the absence of a formal complaint.

### Formal information systems: open versus closed world

[Raymond Reiter's 1977/1978 closed-world database work](https://www.cs.ubc.ca/tr/1977/tr-77-16) establishes an important logical distinction: under declared closed-world assumptions, absence of a provable fact can support a negative conclusion within the specified database domain; under open-world assumptions it need not. The [W3C's OWL 2 Primer](https://www.w3.org/TR/owl-primer/) gives an accessible example: an assertion not present in an ontology may be unknown rather than false.

**Boundary:** this is a formal knowledge-representation distinction. It is not a social-science causal theory, a blanket rule that every missing record hides a harm, or a justification for universal collection. A closed world can be appropriate for a genuinely complete, defined operational register.

### Statistical nonresponse: how did observations become missing?

[Donald Rubin (1976), *Inference and Missing Data*](https://doi.org/10.1093/biomet/63.3.581), and [Roderick Little's 2021 review](https://doi.org/10.1146/annurev-statistics-040720-031104) examine missing-data mechanisms and when a statistical analysis may safely ignore the process causing non-observation. This is different from open-world **logical semantics**. Missingness related to observed and unobserved conditions can distort prevalence estimates; formal MCAR/MAR/MNAR assumptions require an explicit statistical setup and cannot be casually diagnosed from one anecdote.

**Sensible design question:** Is the dataset actually complete for the precise predicate, population and period being queried? If not, what could make its omissions systematically unequal?

### Real-world example: worker violations and complaints

A [March 2026 *ILR Review* study by David Weil, Gonçalo Costa and Daniel Schneider](https://www.hks.harvard.edu/publications/labor-standards-compliance-and-worker-complaints-new-data-and-insights) examined sampled retail/food service workers. The authors reported that 38% experienced labor-standards violations, yet only **26.5% of affected workers complained at all**, predominantly to management, while **1.4% reported to state or federal agencies**. They linked the complaint gap to fears of retaliation and reported an **association**, not a randomized causal estimate, between unionization and much more frequent government reporting.

The result applies to the researchers' surveyed population, not to every industry or period. It is evidence that **official complaint incidence need not approximate underlying violation prevalence**. An institution might see relatively few complaints because the reporting conditions themselves discourage reporting—not because the underlying violations are absent.

Counterintuitively, a rise in complaints after a change in reporting protection *could* indicate improved safety to report rather than more underlying wrongdoing. That is a **hypothesis requiring before/after evidence**, not a conclusion from this cross-sectional study.

### Epistemic justice, but preserve the difference

Different phenomena can produce no record:
- The problem or event did not occur, and the register is complete for that scope.
- The event occurred but the observer lacked knowledge or vocabulary to describe it.
- A person knew something but declined to disclose, for entirely legitimate privacy reasons.
- A person withheld testimony due to fear, exclusion, coercion, or an unsafe audience.
- A person reported, but the complaint was lost, recategorized or excluded by the institution.
- A person reported a mistaken belief that was properly investigated and rejected.

Not every missing complaint constitutes **testimonial injustice** (which involves prejudicial credibility deficits) or **hermeneutical injustice** (which involves unfair structural constraints in interpretive resources). Investigate the relevant mechanisms rather than making the label a catch-all.

Potential ethical interventions include optional private reporting channels, meaningful protection from retaliation, participant-chosen representation, independent evidence gathering, accessible forms, and independent appeals. Each intervention needs an actual governance/consent basis and real maintenance support; "more reporting" is not automatically an end in itself.

### Coherent World translation, not a new population claim

A [five-world identical-dashboard probe](https://github.com/Root-Sequence/coherent-world/blob/research/intelligence-without-omniscience-2026-10/simulation/scenarios/distributed-intelligence/MECHANISM-PROBE-006.md) already demonstrates the *logical* inability to distinguish hidden situations from an identical aggregate. A **future unexecuted extension** could hold the recorded complaint count fixed while varying actual harms, availability of safe channels, and reasons for silence. The lesson would be a sensitivity test of **information generation and missingness**, not a license to simulate marginalized people's private testimony, or proof about any real institution.

Working question:

> **What must be true about who can observe, record, and safely disclose a problem before an intelligent system can treat silence as evidence that the problem is absent?**

## Synthesis boundary

**A useful group must be able to recognize and evaluate relevant knowledge, not merely collect more of it.**

But this must not become a demand for universal transparency or a license to extract knowledge from everyone. Protection against epistemic injustice also means respecting privacy, culturally governed knowledge, safety, disability access, dissent, and the right not to participate.

The companion [From knowledge to uptake](from-knowledge-to-uptake.md) distinguishes recognition from *uptake*, connects Longino's critical community norms, and examines boundary objects, exploitation of epistemic labor, and the right to contest the framing of a problem. These are related but not interchangeable forms of institutional failure.

## Next sources and related homes

- [Epistemic Contrast](../methods/epistemic-contrast.md): differently situated accounts and evidence roles.
- [Deliberative Inquiry](../methods/deliberative-inquiry.md): fair process without forced consensus.
- [Epistemic Discoverability](../../concepts/epistemic-discoverability.md): vocabulary and routing.
- [Collective Judgment and Manufactured Consensus](../../analysis/collective-judgment-and-manufactured-consensus.md): process integrity and dissent.
- [Intelligence Ecology](../../concepts/intelligence-ecology.md): incentives selecting against or in favor of truth-telling.
- [Root Sequence Research Method](../method.md): competent baselines, alternative explanations, and adversarial testing.
