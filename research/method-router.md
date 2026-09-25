# Root Sequence Method & Concept Router

**Document role:** Practical routing map  
**Status:** Developing / not exhaustive  
**Purpose:** Help identify what kind of question is hiding inside a messy systems problem and which established methods/literatures should be checked before Root Sequence invents new vocabulary.

## How to use it

Start with the **shape of the question**, not the field you hope will answer it.

A single real-world problem may route to several rows.

Root Sequence's job is then to preserve the relationships among those analyses without pretending one method replaces the others.

| Question shape | Concepts to inspect | Native methods / literatures | Common RS failure if skipped |
| --- | --- | --- | --- |
| "Why did this technical system fail or amplify failure?" | dependency, feedback, coupling, control, capacity | SRE/reliability engineering, safety engineering, STPA where appropriate, control theory | grand systems language replacing debugging/engineering |
| "Why does it keep doing what used to work?" | path dependence, lock-in, maladaptation, governing variables | historical institutionalism, organizational learning, double-loop learning, resilience/adaptation literature | calling everything an attractor |
| "What future states are actually possible under these constraints?" | reachability, viability, control | control theory, viability theory, operations research | treating metaphorical possibility-space as mathematics |
| "Does this person really have an option?" | capability, affordance, accessibility, conversion factors | capability approach, disability/accessibility research, HCI, ecological psychology | counting menu options as agency |
| "What can this body/environment relation enable?" | affordance, skill, body schema | ecological psychology, embodied cognition, disability/access research | assuming physical presence = usable possibility |
| "Who defined success and the system boundary?" | boundary judgment, purpose, beneficiary, affected parties | Critical Systems Heuristics | treating boundaries as neutral facts |
| "Are people solving different problems because they see different situations?" | worldview, framing, problem situation | Soft Systems Methodology, participatory design | forcing one ontology |
| "Who can shape the conditions under which others act?" | institutional/structural/productive power, decision rights | political/social theory, CSH, institutional analysis | calling power 'constraints' and making it disappear |
| "Who can revise the rules themselves?" | meta-level control, governing variables, constitutional choice | organizational learning, governance, institutional design | confusing user choice with rule-making power |
| "Can this organization survive while retaining local autonomy?" | viability, recursion, autonomy/cohesion | organizational cybernetics, VSM | generic 'coherence' replacing organizational theory |
| "Can the system keep adapting as demands change?" | adaptive capacity, graceful extensibility, sustained adaptability | resilience engineering | treating stability as resilience |
| "What should persist through transformation?" | identity, continuity, lineage, function | philosophy of identity, biology of individuality, organizational theory, domain-specific continuity models | assuming sameness = continuity |
| "How does a living system maintain itself?" | autopoiesis, closure, viability, regulation | theoretical biology, enactivism, physiology | importing organism metaphors into institutions/AI |
| "What does this stress/trauma response mean?" | stress regulation, trauma, learning, safety | trauma research, psychology, physiology, lived expertise | diagnosing by systems analogy |
| "Is this artificial system conscious/suffering?" | phenomenology, sentience, report, access, self-model | consciousness science, philosophy of mind, AI-welfare research | functional adaptation → experience leap |
| "How do people find the field/term they don't know exists?" | vocabulary problem, exploratory search, berrypicking, sensemaking | information science, HCI, knowledge organization, epistemic-agency research | assuming search failure = user ignorance |
| "How should we learn from intervention?" | experiment, feedback, model revision, adaptive management | experimental design, adaptive management, causal inference, domain methods | simulation output → real-world fact |
| "Why did a metric improve while reality got worse?" | proxy failure, Goodhart effects, externality | measurement theory, causal analysis, domain evaluation | treating coherence as another score |
| "How are local and system-level outcomes interacting?" | emergence, downward constraint, cross-scale effects | complexity science, network science, domain models | claiming emergence without mechanism |
| "What should happen when knowledge/conditions are uncertain?" | uncertainty, calibration, reversible action | decision theory, Bayesian methods, risk/safety methods | false precision |
| "Whose labor or cost is hidden by the successful system?" | externalization, maintenance, care work | labor/process analysis, lifecycle analysis, feminist STS, institutional analysis | local optimization masquerading as coherence |

## Routing sequence

When a question arrives:

    ordinary-language question
          ↓
    identify 2–5 plausible question shapes
          ↓
    name candidate mechanisms
          ↓
    route to native fields
          ↓
    gather orientation + primary evidence
          ↓
    compare interpretations
          ↓
    return a connected map
          ↓
    only then decide whether RS vocabulary adds anything

## What the router should return

For each route:

- **candidate concept**
- **why it might fit**
- **why it might not fit**
- **field / community**
- **best orientation source**
- **primary or canonical source**
- **method**
- **evidence needed**
- **related RS project**
- **confidence / unresolved ambiguity**

## Anti-totalization rule

Do not choose one row and make all others disappear.

Examples:

A person's inability to access an online court service can simultaneously involve:

- accessibility;
- capabilities;
- service design;
- institutional power;
- legal/procedural knowledge;
- emotional burden;
- information discovery;
- geographic infrastructure.

Those are coupled.

They are not therefore one mechanism.

## When a new RS concept is justified

Create new shared vocabulary only when at least one condition holds:

1. the same cross-domain distinction keeps recurring and no existing term covers the needed relationship;
2. established concepts need a lightweight routing label that explicitly preserves their differences;
3. the RS concept changes project design/testing in a way that native terms alone do not make legible;
4. the term helps newcomers discover the native literatures rather than replacing them.

Otherwise: **route, don't rename.**

## Candidate future interface

A Conceptual Router could eventually expose this as an interactive graph:

    user's own words
          ↓
    possible question shapes
          ↓
    concepts / aliases
          ↓
    native literatures
          ↓
    methods
          ↓
    sources / Reading Trails
          ↓
    related RS projects

The interface should preserve multiple routes and allow the user to say:

- "not quite";
- "go deeper";
- "show me the disagreement";
- "what do I need to know first?";
- "show primary sources";
- "show the low-jargon path";
- "what would falsify this route?";

Do not build it until the manual router has been used enough to reveal its real schema.
