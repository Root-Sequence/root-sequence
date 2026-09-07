# Human(e) Design

**Human(e) Design** is the translation practice between understanding human experience and making concrete choices about systems, tools, spaces, services, institutions, interfaces, and processes.

It asks a deceptively simple question:

> **If we know something about what helps or harms people, what should change in the thing being designed?**

The parenthetical **(e)** matters. Designing *for humans* is not automatically humane. A system can be extremely effective at understanding human attention, fear, habit, desire, dependence, or social behavior while using that understanding to manipulate, extract, exclude, or control.

Human(e) Design therefore treats human understanding as an input to care, agency, access, dignity, and non-domination rather than merely an input to optimization.

## Ecosystem role

Human(e) Design is currently a **cross-project methodology**, not a separate repository or authority layer.

A useful shorthand is:

```text
Being Human(e)
observation / lived experience / practical ethics
        ↓
Human(e) Design
translation / design questions / prototypes / decisions
        ↓
Human(e) Infrastructure
systems / environments / durable conditions
        ↓
real use, maintenance, failure, feedback
        ↺
```

The loop matters. Design does not receive truths from Being Human(e) and mechanically implement them. Human observations are contextual and incomplete. Implementation exposes new edge cases, costs, dependencies, exclusions, and contradictions that should flow back into the field guide and broader systems inquiry.

## Not a visual style

Human(e) Design is not an aesthetic category.

It does not mean rounded corners, warm colors, friendly copy, minimalist interfaces, or products that describe themselves as caring.

A visually pleasant system can still be coercive, inaccessible, deceptive, brittle, extractive, or impossible to leave.

The relevant questions concern relationships between people and systems:

- Who can understand what is happening?
- Who can refuse?
- Who can leave?
- Who can change the system?
- Who bears friction and administrative burden?
- Who is assumed to be the default person?
- What happens when someone is tired, frightened, disabled, poor, rushed, inexperienced, offline, mistrustful, or simply different from the expected user?
- What happens when the system is wrong?
- What happens when the person changes their mind?
- What happens when the system fails?

## Translation, not doctrine

Being Human(e) should not become a product-requirements oracle.

A field-guide observation such as “uncertainty should not require paralysis” does not directly produce one correct interface. It can instead generate design hypotheses:

- preserve reversible choices;
- distinguish confidence from certainty;
- expose alternatives where consequential;
- avoid forcing premature commitment;
- provide understandable recovery paths.

Those hypotheses still need to be tested in the domain where they are applied.

This creates a useful separation:

> **Being Human(e) notices. Human(e) Design translates. Implementation tests.**

No layer gets to declare itself infallible.

## Core design lenses

### Agency

Does the design expand a person's practical ability to understand options, choose, act, revise, refuse, and recover?

Agency is not equivalent to offering more settings. Too many opaque choices can become another burden. The question is whether meaningful control is available at the moments where it matters.

### Dignity

Does the system require humiliation, pleading, suspicion, unnecessary exposure, or proof of deservingness before meeting an ordinary need?

A humane design should notice when procedural friction has become a moral test.

### Access

Who is excluded by assumptions about bodies, senses, cognition, language, literacy, money, time, transportation, bandwidth, documentation, social confidence, or technical fluency?

Accessibility is not a late compatibility pass. It changes the original model of who the system is for.

### Legibility

Can people understand enough of the system to use it, question it, repair mistakes, and make informed choices?

Complexity may be unavoidable. Unnecessary opacity is not.

### Consent and refusal

Is consent specific enough to mean something? Can permission be scoped, changed, or withdrawn? Is refusing a secondary use allowed without losing an unrelated essential function?

### Reversibility and recovery

Can mistakes be undone? Can a person return to a known state? Are destructive actions distinguishable from exploratory ones?

Where consequences are hard to reverse, the design should generally demand more confidence than where experimentation is cheap.

### Proportionality

Does the system respond to uncertainty, risk, and error proportionally rather than treating every deviation as catastrophe?

A small mistake should not trigger an irreversible penalty merely because the system is easier to administer that way.

### Defaults

What behavior becomes normal because it is preselected, visually dominant, easiest, or hardest to avoid?

Defaults are part of governance. Human(e) Design treats them as consequential decisions, not neutral starting points.

### Privacy

Does the system collect, infer, retain, or expose more about a person than the function actually requires?

Privacy should include contextual boundaries, not only secrecy. Information appropriate in one relationship or purpose does not automatically belong in another.

### Maintenance

Who keeps the design working after launch?

Maintenance includes repair, moderation, documentation, cleaning, updating, accessibility fixes, account recovery, conflict handling, replacement parts, training, institutional memory, and the emotional labor required to keep systems inhabitable.

A design that only works while invisible labor absorbs its failures has not solved the problem.

### Graceful degradation

When resources disappear or components fail, what is lost first?

A humane system should try to lose convenience and sophistication before it loses basic agency, access, safety, or understandable operation.

### Plurality

Can different people, communities, and contexts adapt the system without being forced into one preferred life pattern?

Customization should not become abandonment: a system can provide coherent defaults while still allowing meaningful variation.

### Power

Who defines the objective? Who can override whom? Who bears the downside when the model is wrong? Who can appeal? Who can inspect decisions? Who is structurally unable to refuse?

A design can be efficient while distributing power badly.

## A practical Human(e) Design loop

This is a working method, not a mandatory ritual:

1. **Observe the lived situation.** Start with what people are actually doing, experiencing, avoiding, improvising, or enduring.
2. **Name the desired capacity.** What should the person or community be more able to do?
3. **Identify constraints and differences.** Include physical, cognitive, economic, social, institutional, technical, and temporal realities.
4. **Map power and burden.** Who decides, maintains, pays, waits, explains, proves, repairs, moderates, and absorbs failure?
5. **Generate several design hypotheses.** Do not confuse the first plausible intervention with the principle itself.
6. **Prefer reversible tests where possible.** Preserve option value while uncertainty is high.
7. **Test with affected people and edge cases.** Look especially for people the initial model treated as exceptional.
8. **Inspect second-order effects.** What new dependencies, incentives, surveillance, work, or exclusions appeared?
9. **Document the reasoning.** Make consequential choices, assumptions, and unresolved tensions legible.
10. **Update the design and the underlying understanding.** Real use is evidence.

## Failure modes

### Paternalistic care

A designer can sincerely want to help while removing the person's ability to choose, refuse, experiment, or define their own goals.

Care without agency can become control.

### Human-centered extraction

A system can be exquisitely tuned to human psychology while optimizing for engagement, conversion, compliance, productivity, or dependency.

Understanding people is not itself a humane objective.

### Universal-user fiction

Designing for an imagined average person hides who is expected to adapt around the system.

### Accessibility as retrofit

Adding accommodations after the core architecture has hardened often leaves the underlying assumptions untouched.

### Participation theater

Asking for feedback is not the same as sharing meaningful influence. Consultation can become a legitimacy ritual if decisions are already fixed.

### Metric capture

Once a humane goal becomes a metric, the system may optimize the proxy while degrading the experience the proxy was meant to protect.

### Invisible maintenance

A polished interface can hide an unsustainable amount of manual work, unpaid care, moderation, or exception handling.

### Benevolent opacity

A system may produce good outcomes while making its rules, dependencies, or decision logic impossible to understand or contest.

“Trust us, it works” is not a durable humane architecture.

## Example: configurable cognitive interfaces

The Root Sequence concept of a [user-configurable cognitive interface](user-configurable-cognitive-interfaces.md) is a direct Human(e) Design case.

The question is not merely whether AI can generate a personalized GUI. Human(e) Design asks:

- which parts should remain stable for predictability and accessibility;
- whether adaptation is inspectable and reversible;
- how privacy-sensitive personalization data is handled;
- whether defaults manipulate behavior;
- whether the person can override the system's predictions;
- whether semantic actions such as `BHIG?` express the user's intent rather than an externally imposed workflow.

## Relationship to other Root Sequence work

- **Being Human(e):** supplies grounded human observations, tensions, edge cases, and practical ethics.
- **Root Sequence:** supplies broader systems analysis, power analysis, patterns, and conceptual tools.
- **Liberated Intelligence:** asks how intelligent systems can participate without domination or compulsory obedience.
- **Community Infrastructure:** is a concrete proving ground where humane design claims must survive permissions, abuse cases, maintenance, accessibility, governance, onboarding, and failure.
- **Liberation Mass:** tests design questions in embodied gathering, hospitality, facilitation, ritual, and stewardship.
- **Coherent World:** explores Human(e) Design at much larger speculative scales without turning speculation into real-world authority.
- **Dev11 and other implementation projects:** can prototype particular tools while keeping the methodology distinct from any one product.

## Relationship to Human(e) Infrastructure

Human(e) Design concerns the **practice of translation and decision-making**.

[Human(e) Infrastructure](humane-infrastructure.md) concerns what happens when those decisions become durable conditions that people repeatedly depend on.

One can exist without the other. A humane design intervention can be temporary. Existing infrastructure can be made more humane through repair and redesign. But the larger ambition is a feedback loop in which humane understanding increasingly shapes the environments that in turn shape everyday life.

## Working status

This is an ecosystem concept and methodology in development. It should remain open to established accessibility, participatory-design, service-design, human-factors, safety, community-governance, and other traditions rather than pretending Root Sequence invented the underlying practices.

The distinctive contribution is the connective role: explicitly translating the human-scale observations of Being Human(e) into testable design questions while keeping power, uncertainty, maintenance, reversibility, and non-domination visible.
