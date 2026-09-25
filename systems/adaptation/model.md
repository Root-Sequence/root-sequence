# Adaptation — Working Analysis Model

**Document role:** Reusable systems model for describing how a system changes its responses, structure, or environment over time  
**Status:** AI-assisted draft for author review, 2026-09-24  
**Scope:** Cross-domain systems analysis; not a validated universal scientific model and not a clinical model of human behavior  
**Conceptual parent:** [Dynamic Coherence and Adaptive Continuity](../../concepts/dynamic-coherence.md)

**Idea Trails:** [Adaptive Continuity, Agency, and Becoming](../../IDEA_TRAILS.md#trail-17--adaptive-continuity-agency-and-becoming) · [Resilience, Failure & Graceful Degradation](../../IDEA_TRAILS.md#trail-10--resilience-failure-and-graceful-degradation)  
**Trail role:** research

<!-- idea-trails: adaptive-continuity-agency, resilience-failure -->
<!-- trail-role: research -->

## 1. Claim

Adaptation is not merely movement from one state to another.

A system adapts when feedback, pressure, experience, or changed conditions alter how it responds, organizes, allocates capacity, modifies its environment, or transitions among future states.

A minimal conceptual sketch is:

\[
S_{t+1} = F_t(S_t, E_t)
\]

with adaptation represented as change in the transition dynamics:

\[
F_{t+1} = G(F_t, S_t, E_t, H_t, B_t)
\]

where:

- \(S_t\) — current system state;
- \(E_t\) — relevant environment;
- \(F_t\) — current transition dynamics;
- \(H_t\) — relevant accumulated history;
- \(B_t\) — feedback, consequences, or signals available to the system.

This is a bookkeeping device for reasoning, not an empirical law.

The practical question is:

> **What changed about the system's future responses, and through what mechanism?**

---

## 2. Distinguish state change from adaptive change

Not every change is adaptation.

### State change

The system is different now, but its response rules may be unchanged.

Examples:

- a battery charge falls;
- a bank balance changes;
- a room gets warmer;
- a person moves to another location;
- an inventory count decreases.

### Adaptive change

The system's future response pattern, structure, or action space changes.

Examples:

- a control system updates parameters from error;
- an organization changes procedure after a failure;
- an organism learns a cue;
- a community creates a new mutual-aid practice after a crisis;
- a software agent updates a persistent policy;
- infrastructure is redesigned after repeated overload.

### Environmental modification

The system changes the conditions it will later encounter.

Examples:

- building a shelter;
- adding a road;
- creating documentation;
- changing a law;
- modifying a user interface;
- constructing a social norm;
- storing external memory.

Environmental modification can itself be adaptive and can later become path-dependent structure.

---

## 3. What kind of adaptation occurred?

Use the narrowest description that fits.

| Type | Working description | Example form |
| --- | --- | --- |
| **Compensation** | Temporary adjustment that offsets a disturbance without changing the underlying structure much | reroute load around a failed node |
| **Learning** | Feedback changes future responses or expectations | update a policy after outcomes |
| **Accommodation** | Existing structure changes enough to handle conditions it previously could not | modify workflow around a recurring access need |
| **Reallocation** | Resources or attention shift among existing functions | increase maintenance capacity after repeated failures |
| **Structural adaptation** | Relationships, topology, or roles change | decentralize a bottleneck |
| **Environmental modification** | The system changes its future operating conditions | build infrastructure or alter defaults |
| **Transformation** | The system reorganizes into a materially different configuration | replace an institutional arrangement rather than repair it |
| **Defensive adaptation** | The system reduces exposure to a perceived threat or uncertainty | isolate, harden, restrict, or withdraw |
| **Harmful optimization** | The system becomes better at preserving a target while worsening unmodeled consequences | increase throughput by shifting burden elsewhere |
| **Capture / entrenchment** | Adaptation primarily increases the system's ability to preserve its own power or persistence | change rules to block challenge |

These categories can overlap. They do not imply approval.

---

## 4. Trigger, signal, and interpretation

Record separately:

**Trigger:** What changed or happened?

**Signal:** What information about that change reached the system?

**Interpretation:** What did the system treat the signal as meaning?

**Response:** What changed in behavior or structure?

**Consequence:** What followed?

**Learning:** Which later responses changed because of that consequence?

This separation matters because an adaptive failure may occur at different points:

    world changed
        ↓
    signal missing
        ↓
    no adaptation

or:

    signal received
        ↓
    interpretation wrong
        ↓
    maladaptive response

or:

    correct interpretation
        ↓
    no authority/resources to change
        ↓
    adaptation blocked

or:

    effective local response
        ↓
    wider costs hidden
        ↓
    harmful adaptation reinforced

---

## 5. Scale and boundary

An adaptation claim is incomplete without a boundary.

Ask:

- What is adapting: component, person, organization, network, ecosystem, institution, technical system?
- Which environment is being treated as external?
- Who or what supplies labor, information, energy, money, enforcement, or care?
- Which actors can change the rules?
- Who experiences the consequences without participating in the adaptation?
- Does the adaptation preserve the system by transferring cost beyond the chosen boundary?

A system can appear adaptive because another system absorbs its damage.

---

## 6. Timescale

Record at least:

- response timescale;
- learning or restructuring timescale;
- persistence timescale;
- delayed consequences;
- reversal timescale.

The same adaptation may look different at different horizons.

| Horizon | Possible reading |
| --- | --- |
| Immediate | prevented acute failure |
| Short term | restored function |
| Medium term | created dependency or burden |
| Long term | produced lock-in, resilience, degradation, or transformation |

Do not infer long-term coherence from short-term success.

---

## 7. Path dependence

Ask what prior states make the present response more likely.

Relevant history may include:

- training;
- accumulated infrastructure;
- habits;
- institutional precedent;
- previous shocks;
- trust or distrust;
- legal constraints;
- technical compatibility;
- social norms;
- resource depletion;
- developmental history;
- learned threat or reward associations.

A useful record is:

| Historical condition | Present effect | Mechanism | Reversible? |
| --- | --- | --- | --- |
|  |  |  |  |

The goal is to identify an actual channel, not merely say “history matters.”

---

## 8. Adaptation changes the future possibility structure

For a bounded system, distinguish:

- **currently reachable states;**
- **states that become easier after adaptation;**
- **states that become harder or impossible;**
- **new dependencies created;**
- **new capabilities created;**
- **new actors with veto or control;**
- **exit and reversal paths that remain.**

This is the systems-level counterpart of the [agency envelope](../../concepts/dynamic-coherence.md#3-possibility-space-affordance-space-and-the-agency-envelope).

A locally successful adaptation may narrow future possibilities.

Example form:

    immediate problem solved
            ↓
    one provider becomes indispensable
            ↓
    alternatives atrophy
            ↓
    later exit becomes expensive
            ↓
    future agency narrows

Or it may widen them:

    accessible documentation
            ↓
    more people can diagnose
            ↓
    more maintainers can participate
            ↓
    dependency falls
            ↓
    future repair options widen

---

## 9. Persistent regimes and attractor-like behavior

If a system repeatedly returns to a pattern, ask why.

Possible mechanisms:

- reinforcing feedback;
- sunk cost;
- infrastructure lock-in;
- habit;
- learned expectation;
- network effects;
- institutional incentives;
- resource concentration;
- topology;
- punishment of deviation;
- coordination benefits;
- ecological constraints.

Use **attractor-like** only as an analogy unless a formal dynamical model exists.

A useful test is counterfactual:

> What perturbation should move the system into a different regime if this explanation is correct?

If no possible observation would distinguish the claim from “the system tends to do this,” the attractor language is not adding much.

---

## 10. Maladaptation and mismatch

An adaptation may become costly when:

- the environment changes;
- the original signal was misleading;
- the response persists too long;
- the response is overgeneralized;
- the adaptation improves one metric while damaging another;
- feedback about harm is missing or suppressed;
- a local optimum prevents better global reorganization;
- the system's power allows it to externalize costs.

Describe the mismatch explicitly:

    adaptation was selected under:
    [conditions A]

    current conditions:
    [conditions B]

    persistent response:
    [response R]

    present cost:
    [cost C]

    mechanism preventing revision:
    [feedback / lock-in / power / resource / information problem]

For human trauma, stress, or clinical claims, this framework is only a conceptual scaffold. Use domain evidence and qualified sources rather than diagnosing a person from this template.

---

## 11. Feedback quality

Adaptation depends on feedback, but feedback can be:

- delayed;
- noisy;
- incomplete;
- biased;
- strategically manipulated;
- visible only to some actors;
- costly to provide;
- ignored by decision-makers;
- measured through a poor proxy.

Ask:

1. What consequence is measured?
2. Which consequence is invisible?
3. Who receives the signal?
4. Who can act on it?
5. Who benefits if the signal is ignored?
6. Does adaptation improve the measured proxy while degrading the underlying need?
7. Can affected people challenge the interpretation?

A system that “learns” from distorted feedback can become increasingly effective at the wrong thing.

---

## 12. Power and adaptive capacity

Adaptive capacity is unevenly distributed.

Record:

- who can alter rules;
- who can modify infrastructure;
- who controls resources;
- who can experiment safely;
- who bears failed experiments;
- who can leave;
- who is required to adapt instead of the environment;
- who can force others to absorb change.

A recurring anti-pattern is:

> **the least powerful component is required to become more resilient so the higher-level system can avoid changing.**

Examples might include workers absorbing scheduling volatility, disabled users working around inaccessible design, communities compensating for failing infrastructure, or downstream systems absorbing technical debt.

Do not praise adaptation when it merely transfers responsibility downward.

---

## 13. Adaptation, recovery, resilience, and transformation

Use these as related but distinct questions.

### Recovery

What capability or state returns after disruption?

### Adaptation

What changes in response to conditions or feedback?

### Resilience

What important relationships or capacities persist through disturbance, and under which definition of resilience?

### Transformation

When is maintaining the earlier configuration no longer the relevant goal?

One sequence might be:

    disruption
        ↓
    degraded operation
        ↓
    recovery attempt
        ↓
    feedback shows old state is no longer viable
        ↓
    adaptation / transformation
        ↓
    new persistent regime

Another system might recover fully without meaningful adaptation.

---

## 14. Identity and continuity

If a system changes substantially, specify what continuity claim is being made.

Possible continuity criteria include:

- same physical components;
- same organizational lineage;
- same governing purpose;
- same people or membership;
- same causal trajectory;
- same critical capabilities;
- same relationships;
- same legal identity;
- same memory;
- same interface or protocol;
- same ecological function.

Different criteria can diverge.

A rebuilt organization can preserve legal identity while replacing its people and practices. A biological organism can preserve organismic continuity while personality or capacity changes. A software service can preserve a name while its architecture and ownership change completely.

Do not treat “same system” as self-evident.

---

## 15. Reflexive adaptation

Some systems adapt in response to models, predictions, or classifications about themselves.

Record whether:

- a metric changes the behavior being measured;
- a forecast changes the event being forecast;
- a category changes how participants identify or act;
- a policy changes incentives and therefore the data used to evaluate the policy;
- an AI output changes later training or decision environments.

A reflexive loop can amplify model error:

    model
      ↓
    intervention
      ↓
    changed behavior
      ↓
    data produced by intervention
      ↓
    apparent confirmation of model

The evaluation should ask whether the system would have produced the same evidence without the intervention.

---

## 16. Intervention levels

| Level | Possible intervention |
| --- | --- |
| Signal | improve sensing, reporting, provenance |
| Interpretation | compare models, expose uncertainty |
| Response repertoire | add skills, protocols, fallback modes |
| Resources | redistribute time, money, energy, labor |
| Relationships | change coordination, reciprocity, dependency |
| Topology | decentralize, bridge, isolate, modularize |
| Rules | alter incentives, permissions, constraints |
| Environment | redesign infrastructure or defaults |
| Feedback | make consequences visible and actionable |
| Power | change ownership, vetoes, review, appeal |
| Memory | preserve lessons without over-retention |
| Time | slow, stage, pilot, sunset, revisit |
| Exit | preserve migration, refusal, rollback |

Interventions can themselves become new path dependencies.

---

## 17. Evidence and claim status

Label claims explicitly:

- **OBSERVED** — directly documented state, change, or behavior;
- **SUPPORTED** — mechanism has substantial evidence;
- **HYPOTHESIS** — plausible mechanism to test;
- **ANALOGY** — cross-domain structural comparison;
- **INTERPRETATION** — proposed meaning of the pattern;
- **NORMATIVE** — judgment about what should be preserved or changed;
- **SPECULATIVE** — untested possibility;
- **UNKNOWN** — unresolved.

For each adaptive claim, record:

    Claim:
    System boundary:
    Trigger:
    Response:
    What changed in future behavior:
    Proposed mechanism:
    Evidence:
    Competing explanation:
    Who benefited:
    Who bore costs:
    Timescale:
    Reversibility:
    What would disconfirm this:

---

## 18. Cross-domain transfer test

Before applying an adaptation concept from one domain to another, compare:

| Dimension | Source domain | Target domain |
| --- | --- | --- |
| What persists? |  |  |
| What varies? |  |  |
| What receives feedback? |  |  |
| How is memory implemented? |  |  |
| What selects among responses? |  |  |
| What counts as viability? |  |  |
| Is there subjective experience? |  |  |
| Is there an agent? |  |  |
| What power structure exists? |  |  |
| What evidence supports the mapping? |  |  |

Possible result:

- mechanism plausibly shared;
- partial structural analogy;
- metaphor only;
- comparison misleading;
- unresolved.

---

## 19. Compact adaptation canvas

    SYSTEM / BOUNDARY:

    CURRENT STATE:

    RELEVANT ENVIRONMENT:

    TRIGGER / PRESSURE:

    SIGNAL RECEIVED:

    INTERPRETATION:

    RESPONSE:

    WHAT CHANGED IN THE TRANSITION DYNAMICS:

    HISTORY / PATH DEPENDENCE:

    FEEDBACK LOOP:

    CAPABILITIES GAINED:

    POSSIBILITIES LOST:

    NEW DEPENDENCIES:

    WHO CAN ALTER THE RESPONSE:

    WHO BENEFITS / WHO BEARS COSTS:

    SHORT-TERM EFFECT:

    LONG-TERM EFFECT:

    RECOVERY / TRANSFORMATION RELATION:

    REVERSIBILITY / EXIT:

    EVIDENCE STATUS:

    COMPETING EXPLANATIONS:

    WHAT WOULD DISCONFIRM THIS:

---

## 20. Root Sequence principle

> **Adaptation is not evidence of improvement. Ask what changed, what future responses became more likely, which possibilities opened or closed, who shaped the change, and whether the system can still revise itself when conditions change again.**

This model should make adaptation more specific, not turn every historical effect into one grand theory.
