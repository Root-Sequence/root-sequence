# T-003 Editorial Pilot 002 — comparison and coding

**Status:** EDITORIAL PILOT RESULT / NOT INDEPENDENT VALIDATION  
**Case:** Cloudflare June 20, 2024 incident  
**Packet:** remediation-withheld v0.2  
**Methods:** ordinary incident/system review (A2) vs frozen dynamic-coherence review (D2)  
**Coders:** same AI-assisted process that generated both methods  
**Conflict level:** severe

## Executive result

Pilot 002 replicates Pilot 001's main result under a harder evidence condition.

Removing the source-authored remediation section did **not** reveal clear unique decision-relevant added value from Method D.

Method D again generated a coherent synthesis around:

- reachable failure trajectories;
- implementation history;
- shrinking recovery options;
- feedback/model revision;
- emergency control points;
- reversibility;
- capability-level continuity.

But the ordinary review independently derived the concrete prevention, containment, detection, recovery, and test actions needed for the case.

### Primary coding result

- Method D findings coded **E1–E2 / D2 / N2:** **0**
- Method A findings coded **E1–E2 / D2 / N2:** **1 clear case: A2-02 execution bounds/watchdog**
- Method D had two substantively unique interpretive contributions that did not meet the D2 decision threshold:
  - D2-10 capability-level continuity;
  - D2-11 explicit boundary restraint against unsupported normative/human-agency claims.

The repeated result strengthens a narrower interpretation:

> **Dynamic coherence currently looks more defensible as a cross-domain synthesis / routing grammar than as a standalone technical incident-review method.**

---

## Output size

| Measure | Method A2 | Method D2 |
| --- | ---: | ---: |
| Findings | 12 | 12 |
| Words | 1,239 | 1,182 |
| Characters | 9,852 | 9,890 |
| Human preparation time | not measured | not measured |
| Human application time | not measured | not measured |

Again, similar output length does not establish similar human burden.

---

## Method D2 coding

| Finding | E | D | N | Closest A2 | Note |
| --- | --- | --- | --- | --- | --- |
| D2-01 composition assumptions | E2 | D2 | N0 | A2-01 | Same composition defect; D adds assumption language. |
| D2-02 new reachable failure trajectories | E1/E2 | D2 | N1 | A2-01, A2-03, A2-10 | Useful change-review abstraction; concrete actions already present. |
| D2-03 reuse/history constraint | E1/E2 | D1 | N1 | A2-01 | Broadens reuse review but no distinct high-priority action. |
| D2-04 shrinking recovery options | E2 | D2 | N0/N1 | A2-04, A2-05, A2-09, A2-11 | Strong synthesis, ordinary method explicitly preserves reserve/independent recovery paths. |
| D2-05 feedback ambiguity | E2 | D2 | N0 | A2-06 | Same diagnostic requirement. |
| D2-06 locally corrective balancing amplified failure | E2 | D2 | N0 | A2-04 | Same propagation-aware containment. |
| D2-07 emergency control/revision map | E1 | D1 | N1 | A2-05, A2-07, A2-12 | Useful information request, no evidence authority ambiguity caused delay. |
| D2-08 rollout as reversibility | E2 | D2 | N0 | A2-03 | Same canary/rollback issue. |
| D2-09 human response capacity | E1/E2 | D2 | N0 | A2-07 | Same concurrent-incident response issue. |
| D2-10 capability-level continuity | E1 | D1 | N2 | none direct | Distinct framing for redesign scope, but packet does not support one specific architecture decision. |
| D2-11 no broad normative inference | E2 | D0 | N2 | none | Valuable restraint; not a case remediation. |
| D2-12 evidence that future changes alter recurrence | E1/E2 | D2 | N1 | A2-09, A2-10, A2-12 | Stronger lifecycle framing, but verification/testing is already present. |

### D2 decision-relevant novelty

**E1–E2 / D2 / N2 = 0**

---

## Method A2 coding

| Finding | E | D | N | Closest D2 | Note |
| --- | --- | --- | --- | --- | --- |
| A2-01 eliminate validation/self-reference defect | E2 | D2 | N0 | D2-01, D2-02 | Same immediate defect. |
| A2-02 runtime execution bounds | E2 | D2 | N2 | none direct | Concrete containment missing from Method D. |
| A2-03 canary promotion/rollback | E2 | D2 | N0 | D2-08 | Same rollout risk. |
| A2-04 stop balancing from propagating trigger | E2 | D2 | N0 | D2-06 | Same propagation failure. |
| A2-05 harden Traffic Manager | E2 | D2 | N0/N1 | D2-04, D2-07 | A is more component-specific. |
| A2-06 overload-vs-poison diagnostics | E2 | D2 | N0 | D2-05 | Same. |
| A2-07 concurrent incident separation | E1/E2 | D2 | N0 | D2-09 | Same. |
| A2-08 selective/evidence-preserving recycling | E1 | D1/D2 | N1 | D2-04 | More operational detail. |
| A2-09 compound failure test | E1/E2 | D2 | N1 | D2-04, D2-06 | D supplies synthesis; A states direct test. |
| A2-10 rare-trigger/adversarial composition test | E1/E2 | D2 | N1 | D2-02, D2-08 | More concrete test design. |
| A2-11 reserve capacity / independent recovery paths | E2 | D2 | N0/N1 | D2-04 | Direct operational form of response-space preservation. |
| A2-12 missing architecture evidence | E2 | D2 | N1 | D2-07, D2-12 | Broader evidence request. |

### A2 decision-relevant novelty

**E1–E2 / D2 / N2 = 1: A2-02**

---

## Withheld-remediation reconstruction

The omitted source remediation section included four broad themes:

1. architecture / affected rate-limiter service replacement;
2. containment of non-terminating execution;
3. staged rollout improvement;
4. network-capacity/mitigation improvement.

This is **not a gold standard**, but it is useful for checking whether methods can derive plausible actions without seeing the source's list.

### Method A2

- **Architecture change:** partial — focuses on composition contracts rather than replacing the service because legacy/replacement facts were withheld.
- **Execution containment:** yes — A2-02.
- **Staged rollout:** yes — A2-03.
- **Network/capacity mitigation:** yes, in mechanism-specific form — A2-04, A2-09, A2-11.

### Method D2

- **Architecture change:** partial — D2-03 and D2-10 suggest reuse review and capability-level redesign, but not a specific replacement.
- **Execution containment:** **not explicit**.
- **Staged rollout:** yes — D2-08.
- **Network/capacity mitigation:** yes — D2-04 and D2-06.

The missing execution-bound recommendation is now replicated across both Pilot 001 and Pilot 002 Method D outputs.

That suggests a real prompt-level weakness:

> **A framework focused on relationships, trajectories, and option structure can underweight simple component-level defensive engineering.**

---

## New protocol lesson: preserve the component level

The dynamic-coherence framework explicitly warns against collapsing scales, but its frozen prompt does not force a direct **component-level defensive control** pass.

That matters.

In this case, "limit how long one request may run" is neither a grand systems insight nor a future-agency finding.

It is a straightforward local containment measure.

And it is valuable.

### Proposed framework correction

Dynamic coherence should **not** add another broad question merely to ensure every engineering detail appears.

Instead, its method role should become clearer:

> **Use competent domain methods first. Use dynamic coherence to connect temporal, cross-boundary, path-dependent, agency, and revision questions that those methods may distribute or omit.**

It should not pretend to replace:

- debugging;
- hazard analysis;
- SRE/incident review;
- reliability engineering;
- control theory;
- accessibility analysis;
- capability analysis;
- clinical science;
- other domain methods.

This is a conceptual narrowing, not a defeat.

---

## False alarms

No clear E0 false alarm was coded.

As in Pilot 001, that result is weak because the same AI process generated and coded the outputs.

Potential overreach points:

- D2-07 could become authority-theater if used without evidence that emergency decision rights are a real problem.
- D2-10 could become vague transformation language if not connected to a concrete service contract.
- A2-08 is precautionary because restart-induced harm was not reported.

All three outputs label their uncertainty.

---

## Two-pilot synthesis

Across two editorial pilots on the same incident:

### Repeated strengths of Method D

- connects local remediation to changing future system trajectories;
- names contraction of recovery possibilities;
- makes path dependence/reuse explicit;
- treats feedback as model revision;
- distinguishes capability continuity from implementation continuity;
- strongly resists unsupported normative transfer.

### Repeated weaknesses

- no clear D2/N2 decision-relevant finding beyond competent ordinary review;
- misses one simple concrete defensive action twice;
- conceptual vocabulary is broader than needed for this technical case;
- requires a domain method anyway.

### Repeated strengths of Method A

- concrete component and operational controls;
- direct testing/remediation proposals;
- good coverage of propagation, dependencies, recovery, rollout, and monitoring.

### Repeated weaknesses

- cross-finding relationships remain more fragmented;
- does not explicitly distinguish current state from future transition dynamics;
- does not explicitly ask how response options contract over time;
- provides less vocabulary for transferring the same question to non-incident domains.

---

## Decision after Pilot 002

The preregistered stop rule applies:

> **Do not tune the prompts further against this incident.**

No Pilot 003 on Cloudflare June 20 should be created to rescue the framework.

### Framework status after two pilots

Keep:

- dynamic coherence as a **conceptual synthesis / routing grammar**;
- state vs transition dynamics;
- path dependence;
- future possibility / response-space questions;
- revision power;
- continuity-through-transformation;
- cross-scale/boundary discipline.

Downgrade:

- any implication that Dynamic Coherence is already a standalone general review method.

Require:

- a competent domain method;
- explicit statement of what Dynamic Coherence adds beyond that method;
- willingness to report "nothing" when it adds nothing.

---

## Next validation gate

Do **not** run another same-model case immediately and call the resulting volume evidence.

The next meaningful gate is one of:

### A. Independent reviewer comparison

Use a different case, frozen packet, and human reviewers/coders.

### B. Method-fidelity comparison

Add a properly prepared established method—e.g. STPA for an appropriate case—with someone able to evaluate fidelity.

### C. A domain where the dynamic concepts should matter more

Select a case involving real path-dependent option structure, such as infrastructure migration or institutional dependency, **but select it before inspecting whether Dynamic Coherence produces a favorable result**.

If none of these is available, stop and preserve the current uncertainty.

---

## Editorial conclusion

Pilot 002 again fails to demonstrate unique decision-relevant added value for Dynamic Coherence as a technical incident-review method.

It does, however, clarify a potentially more durable role:

> **Dynamic Coherence may be the grammar that helps Root Sequence carry questions about history, future possibility, revision, and continuity across domains—while domain methods remain responsible for the actual mechanisms.**

That is narrower than a universal method.

It may also be better.
