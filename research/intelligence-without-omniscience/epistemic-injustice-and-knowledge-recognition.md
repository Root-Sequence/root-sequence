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

## Synthesis boundary

**A useful group must be able to recognize and evaluate relevant knowledge, not merely collect more of it.**

But this must not become a demand for universal transparency or a license to extract knowledge from everyone. Protection against epistemic injustice also means respecting privacy, culturally governed knowledge, safety, disability access, dissent, and the right not to participate.

## Next sources and related homes

- [Epistemic Contrast](../methods/epistemic-contrast.md): differently situated accounts and evidence roles.
- [Deliberative Inquiry](../methods/deliberative-inquiry.md): fair process without forced consensus.
- [Epistemic Discoverability](../../concepts/epistemic-discoverability.md): vocabulary and routing.
- [Collective Judgment and Manufactured Consensus](../../analysis/collective-judgment-and-manufactured-consensus.md): process integrity and dissent.
- [Intelligence Ecology](../../concepts/intelligence-ecology.md): incentives selecting against or in favor of truth-telling.
- [Root Sequence Research Method](../method.md): competent baselines, alternative explanations, and adversarial testing.
