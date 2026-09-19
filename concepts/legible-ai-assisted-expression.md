# Legible AI-Assisted Expression

**Document role:** Cross-project design principle and authoring method<br>
**Status:** Active / developing<br>
**Canonical scope:** Shared Root Sequence treatment of provenance and review in AI-assisted expression; project-specific workflows, interfaces, and tests should transform it rather than duplicate it.<br>
**Evidence boundary:** This page proposes normative and design guidance. No interface can perfectly reconstruct where a thought originated, prove authorship from a generated trace, or make an unchecked claim true.<br>
**First formalized here:** 2026-09-19<br>

**Idea Trails:** [Accessibility, Dependence & Participation](https://github.com/Root-Sequence/root-sequence/blob/main/IDEA_TRAILS.md#trail-5--accessibility-dependence-and-participation) · [Intelligence, Automation & Legitimate Authority](https://github.com/Root-Sequence/root-sequence/blob/main/IDEA_TRAILS.md#trail-9--intelligence-automation-and-legitimate-authority) · [Memory, Provenance & Continuity](https://github.com/Root-Sequence/root-sequence/blob/main/IDEA_TRAILS.md#trail-11--memory-provenance-and-continuity)<br>
**Trail role:** analytical lens

<!-- idea-trails: accessibility-participation, intelligence-authority, memory-provenance -->
<!-- trail-role: analytical-lens -->

## Core principle

> **AI should reduce the cost of expression without reducing the visibility of thought.**

AI can help a person externalize, organize, connect, test, develop, and phrase what they are trying to express. That help becomes harder to trust when the finished artifact conceals which ideas came from the person, which connections the AI inferred, which language it generated, which claims have support, and which choices remain unsettled.

The goal is not to keep AI at the edge of substantive work. The goal is to make substantive assistance **legible enough to inspect, correct, challenge, continue, or refuse**.

## Writing and thinking are not one universal process

For some people, writing is a primary way of discovering what they think. For others, much of the thinking happens through association, images, conversation, experience, or a large network of connected ideas before prose begins. Writing then becomes a difficult serialization task: turning something nonlinear into a sequence of words another person can encounter.

AI can be especially useful in that second situation. It can lower working-memory, language, motor, organizational, or formatting burdens without taking over the underlying conceptual direction. It can also support thinking-through-writing by offering questions, counterexamples, and alternative structures.

Neither pattern should become a universal theory of authorship. Assistance should adapt to the actual relationship between the person, the thought, and the artifact.

The central risk in both cases is **premature coherence**: generated prose can make an idea look settled before its assumptions, contradictions, evidence, or ownership have become visible. Fluency is not a reliable signal that the thinking is complete.

## Visibility does not mean surveillance

The phrase **visibility of thought** refers to the provenance and development of the artifact—not unrestricted access to a person's interior life.

A system should not infer a complete mental model, publish private scratch material, preserve every keystroke, or demand an unaided performance of authorship merely to make a draft traceable. It should show what it actually knows about the contribution and transformation history, preserve uncertainty where the history is mixed, and keep private source material within its authorized boundary.

The relevant asymmetry from [Legible Systems](legible-systems.md) still applies: assistance should become legible to the person using it without requiring that person to become universally legible to the system.

## What the record should preserve

The useful unit is not a binary label such as “human-written” or “AI-written.” A substantially assisted artifact may contain several kinds of contribution at once.

| Question | What should remain visible |
| --- | --- |
| **What came from the person?** | Their questions, claims, metaphors, examples, observations, constraints, objections, selections, corrections, and decisions—quoted or paraphrased honestly where the distinction matters. |
| **What did the AI add?** | New inference, interpretation, synthesis, structure, examples, counterarguments, transitions, or wording. An inference should not be presented as something the person already believed. |
| **How was the material transformed?** | Whether fragments were reordered, merged, compressed, expanded, generalized, translated, connected, or rewritten for a different audience or form. |
| **What supports factual claims?** | Sources, dates, inspected passages, calculations, tests, and the exact scope of their support. Model recall and plausible wording are not verification. |
| **What remains uncertain or contested?** | Missing evidence, conflicting sources, ambiguous intent, alternative interpretations, unresolved tensions, and limits of the available record. |
| **Where were decisions made?** | Options considered, who chose among them, what was rejected or deferred, and whether the current wording is proposed, accepted, verified, or still awaiting review. |
| **What is the artifact's current status?** | Draft, assistant synthesis, author-reviewed passage, source-checked claim, tested implementation, independently reviewed work, or published artifact. These states should not collapse into one “done” label. |

Not every sentence needs a badge. The trace should be available at the level where origin or transformation changes meaning, evidence, authority, or accountability.

## “Show the work” at the artifact boundary

Showing the work does not require publishing a model's hidden internal reasoning or an exhaustive transcript. Such material may be unavailable, unreliable as an explanation, privacy-invasive, or far more burdensome than the artifact it is meant to clarify.

The durable trace should instead expose the work a reviewer can actually inspect:

- the source fragments or an authorized summary of them;
- the requested purpose, audience, and constraints;
- the AI's additions and material interpretations;
- a transformation summary or meaningful diff;
- alternative structures or readings when a consequential choice was open;
- factual sources and verification status;
- unresolved questions and uncertainty;
- human corrections, selections, rejections, and approvals;
- the artifact version to which each decision applies.

Use [technical accessibility](legible-systems.md#technical-accessibility): give an ordinary-language account first, with deeper source, version, prompt, model/tool, diff, or machine-readable detail available when it helps verification. A technical log without a comprehensible account is not sufficient legibility.

The trace should also reduce review cost. Generating ten pages of explanation for one page of prose merely transfers cognitive labor to the reviewer. Prefer a concise contribution and decision summary linked to details that can be opened when needed.

## A practical authoring pattern

This is a working pattern, not a mandatory ritual:

1. **Capture the source material.** Preserve the person's fragments, questions, examples, constraints, or spoken explanation within the appropriate privacy boundary.
2. **Name the requested transformation.** Organize, connect, challenge, summarize, translate, polish, or develop are different operations and should not silently become one another.
3. **Draft with contribution boundaries.** Keep human-originated material distinguishable from AI-added inference, synthesis, and wording wherever the distinction affects meaning or attribution.
4. **Separate claims from support.** Identify which factual statements were checked, what supports them, and which remain unverified or interpretive.
5. **Surface decisions in manageable units.** Present consequential alternatives, assumptions, and conflicts without requiring review of an enormous finished artifact all at once.
6. **Record the person's response.** Accept, revise, reject, qualify, or leave unresolved. Agreement with one passage does not approve the entire artifact.
7. **Preserve a resumable trace.** Keep the current version, decision state, unresolved question, and next useful step together so work can continue without reconstructing the whole conversation.

This process permits genuine co-development. It does not require pretending that every phrase was independently composed by the person, or that accepting an AI proposal transfers its full origin to them.

## Common failure modes

### Premature coherence

Polished structure hides that the underlying idea is partial, contradictory, or not yet reviewed.

### Provenance laundering

AI-added inference or wording is retrospectively described as the person's original thought, or substantive drafting is minimized as “grammar help.”

### Intent capture

The system treats its best guess about what the person means as authoritative, then rewrites later material around that guess.

### Factual inflation

A plausible sentence gains apparent credibility from tone or citations that do not actually support it.

### Review theater

A person is asked to approve a large coherent artifact after the important framing choices have already become difficult to see or undo.

### Voice capture

Repeated assistance narrows expression toward the model's preferred rhythm, register, assumptions, or genre while presenting the result as neutral improvement.

### Trace overload

The provenance record becomes so verbose or technical that meaningful review is less possible, not more.

## Design test

When evaluating an AI-assisted authoring process, ask:

1. Can the person see which important ideas, examples, and constraints came from them?
2. Are AI-added inference, synthesis, structure, and wording distinguishable where the difference matters?
3. Can someone inspect how source material became the current artifact?
4. Are factual support, model recall, interpretation, and speculation kept separate?
5. Do uncertainty, contradiction, and missing context remain visible after polishing?
6. Can the person accept one contribution without endorsing the whole artifact?
7. Are rejected alternatives and consequential decision points recoverable?
8. Can the work continue without the AI, the original session, or unaided recall?
9. Does the trace protect private source material and other contributors' boundaries?
10. Does assistance reduce total expression and review burden rather than merely increasing output volume?

## Relationship to other Root Sequence work

- [Legible Systems](legible-systems.md) supplies progressive explanation, inspectable automation, technical accessibility, and the warning against transferring review burden.
- [Human(e) Design](humane-design.md) asks whether the authoring process preserves agency, accessibility, refusal, reversibility, privacy, plurality, and honest power relationships.
- [User-Configurable Cognitive Interfaces](user-configurable-cognitive-interfaces.md) provides a broader interaction context for tools shaped around how a person thinks and works without making adaptation opaque.
- [AI assistance, verification, and author review](../research/papers/coherent-systems/AI-ASSISTANCE.md) is a public project-specific application: it distinguishes author contributions, substantive AI drafting, source verification, passage-level review, and publication status.
- [**Coherent Computing / Wingbot**](https://github.com/Root-Sequence/coherent-computing/blob/main/docs/wingbot.md) **(private / access restricted):** the project-local design study applies this principle to suggestions beside unfinished writing, including scope, uncertainty, revision binding, authority, retention, and review cases. Its implementation questions and tests remain canonical in that project rather than here.

This principle should travel by transformation, not by copying the same disclosure or workflow into every project.

## Provenance and status

The core sentence—“AI should reduce the cost of expression without reducing the visibility of thought”—was established by Rae in the 2026-09-19 request to canonize this conversation's principle. It develops an earlier discussion of AI “showing its work,” writing as an expression bottleneck for some people, and AI helping externalize and organize thought.

The distinction among human-originated material, AI-added inference, synthesis, wording, transformations, factual support, uncertainty, and decision points was also explicitly requested. The name of this page, its tables, authoring pattern, design test, failure modes, and connections are an AI-assisted synthesis prepared to make that direction inspectable and revisable. The page does not claim that the broader traditions of accessible writing support, provenance, editorial disclosure, or computer-supported authorship originated in Root Sequence.
