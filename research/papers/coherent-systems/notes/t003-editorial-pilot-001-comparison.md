# T-003 Editorial Pilot 001 — comparison and coding

**Status:** EDITORIAL PILOT RESULT / NOT INDEPENDENT VALIDATION  
**Case:** Cloudflare June 20, 2024 incident  
**Compared methods:** Method A ordinary incident/system review vs Method D frozen dynamic-coherence review  
**Evidence packet:** frozen v0.1 only  
**Coders:** same AI-assisted research process that generated both outputs  
**Conflict level:** severe; conclusions are protocol-debugging evidence only

## Executive result

Pilot 001 is a **near-null result for unique decision value from Method D**.

The dynamic-coherence review successfully reorganized the incident around:

- transition dynamics;
- path dependence;
- recovery-option contraction;
- feedback/model revision;
- revision/control power;
- continuity through replacement;
- future reversibility.

However, nearly every **decision-relevant** Method D finding was already captured substantively by the ordinary review.

No Method D finding was coded **E1–E2 / D2 / N2**: evidence-supported, decision-relevant, and substantively absent from Method A.

Method A produced one concrete decision-relevant item with no equally explicit Method D counterpart: **runtime execution bounds/watchdogs for non-terminating request handling** (A-02). That action was also stated as a Cloudflare follow-up in the frozen source packet, so this is not a discovery claim for Method A; it shows that Method D's conceptual breadth did not guarantee complete extraction of ordinary technical remediations.

The strongest provisional interpretation is:

> **In this case, dynamic coherence behaved more like a synthesis/reframing layer than a superior incident-review method.**

That can still be useful. It is not the same as demonstrated added value.

---

## Frozen-output size / crude burden indicators

| Measure | Method A | Method D |
| --- | ---: | ---: |
| Findings | 12 | 12 |
| Words | 1,521 | 1,490 |
| Characters | 11,833 | 11,997 |
| Core review questions / required lenses | 6 ordinary-review questions | 13 frozen dynamic-coherence questions |
| Human preparation time | not measured | not measured |
| Human analysis time | not measured | not measured |

The similar output size does **not** mean similar human burden. The dynamic prompt has more conceptual categories and may require more training. This AI-only pilot cannot measure that.

The earlier automated count of "request/unknown/uncertainty" terms is not used as a research result; it is too crude to represent information-request burden.

---

## Finding-level coding — Method D

Coding:

- **E2:** directly supported by packet evidence
- **E1:** reasonable inference with explicit basis
- **E0:** unsupported
- **D2:** plausibly decision-relevant
- **D1:** relevant context / secondary decision value
- **D0:** not materially decision-relevant
- **N2:** substantively absent from Method A
- **N1:** partly present / differently developed
- **N0:** same substantive finding already captured

| Finding | E | D | N | Closest Method A finding(s) | Coding note |
| --- | --- | --- | --- | --- | --- |
| D-01 hidden incompatible assumptions | E2 | D2 | N0 | A-01 | Same defect/composition problem; D emphasizes assumption fit. |
| D-02 deployment changed failure transitions | E1 | D1 | N1 | A-01, A-04, A-05 | Useful abstraction, but resulting actions are already covered by defect, rollout, and propagation review. |
| D-03 legacy architecture as retained history | E2 | D2 | N0 | A-03 | Same migration/dependency issue. |
| D-04 recovery-option contraction | E2 | D2 | N1 | A-05, A-06, A-10 | Strong synthesis of several ordinary findings; no clearly new action beyond quarantine/control redundancy/compound-failure testing. |
| D-05 feedback/model ambiguity | E2 | D2 | N0 | A-07 | Same diagnostic requirement. |
| D-06 recovery mechanism amplified failure | E2 | D2 | N0 | A-05 | Same propagation-aware containment finding. |
| D-07 revision power/control map | E1 | D1 | N1 | A-08, A-12 | Method D makes authority/control topology more explicit; packet does not show it caused delay. |
| D-08 continuity through service replacement | E2 | D2 | N0 | A-03 | Same long-term replacement/migration direction, reframed around capability continuity. |
| D-09 responder capacity as shared dependency | E1/E2 | D2 | N0 | A-08 | Same concurrent-incident staffing/hypothesis issue. |
| D-10 rollout as preserved reversibility | E2 | D2 | N0 | A-04 | Same rollout/rollback/blast-radius change. |
| D-11 boundary restraint on normative claims | E2 | D0 | N2 | none | Methodological restraint absent from A, but it does not change the technical decision in this case. |
| D-12 remediation intent vs verified change | E2 | D2 | N0 | A-11 | Same verification requirement. |

### Method D decision-relevant novelty count

- **E1–E2 / D2 / N2:** **0**
- **E1–E2 / D2 / N1:** **1 clear synthesis candidate (D-04)**, with D-02 and D-07 below D2 threshold in this pilot
- **D0 / N2:** **1 (D-11)** — useful evidence-boundary discipline, not an incident remediation finding

---

## Finding-level coding — Method A

| Finding | E | D | N | Closest Method D finding(s) | Coding note |
| --- | --- | --- | --- | --- | --- |
| A-01 fix validator/API recursion defect | E2 | D2 | N0 | D-01, D-02 | Same core failure path. |
| A-02 execution bounds/watchdog | E2 | D2 | N2 | no direct counterpart | Concrete containment action omitted by D despite being present in packet follow-up. |
| A-03 retire/isolate legacy rate limiter | E2 | D2 | N0 | D-03, D-08 | Same architectural change. |
| A-04 rollout/promotion/stop criteria | E2 | D2 | N0 | D-10 | Same blast-radius/reversibility issue. |
| A-05 propagation-aware traffic shifting | E2 | D2 | N0 | D-04, D-06 | Same amplification loop. |
| A-06 harden Traffic Manager | E2 | D2 | N0/N1 | D-04, D-07 | D covers response diversity/control points, though A is more component-specific. |
| A-07 high-CPU/low-traffic diagnostics | E2 | D2 | N0 | D-05 | Same feedback discrimination. |
| A-08 concurrent-incident response capacity | E1/E2 | D2 | N0 | D-09 | Same organizational dependency. |
| A-09 selective recovery/restart control | E1 | D1/D2 | N1 | D-04, D-06 | D covers recovery-option diversity but not this precise operational precaution. |
| A-10 compound failure testing | E1/E2 | D2 | N1 | D-04, D-06 | D synthesizes the mechanisms but does not state the same test as directly. |
| A-11 post-remediation verification | E2 | D2 | N0 | D-12 | Same verification requirement. |
| A-12 missing architecture/rollout evidence | E2 | D2 | N1 | D-07, D-12 | Broader ordinary evidence request. |

### Method A decision-relevant novelty count

- **E1–E2 / D2 / N2:** **1 (A-02)**
- Several N1 findings are more implementation-specific versions of Method D synthesis.

Again, A-02 is **not** proof that ordinary review is generally superior; it was explicitly available in the packet's source-reported remediation.

---

## Overlap map

A compact view:

    immediate software assumptions/defect
      A-01 <-> D-01 / D-02

    legacy implementation
      A-03 <-> D-03 / D-08

    rollout / reversibility
      A-04 <-> D-10

    failure propagation / shrinking recovery space
      A-05 / A-06 / A-10 <-> D-04 / D-06 / D-07

    feedback / diagnosis
      A-07 <-> D-05

    concurrent responder capacity
      A-08 <-> D-09

    remediation verification
      A-11 <-> D-12

    missing evidence
      A-12 <-> D-07 / D-12

    ordinary-only in this output
      A-02 execution bounds
      A-09 selective restart detail

    dynamic-only in this output
      D-11 explicit refusal to manufacture normative claims
      D-04's unified "recovery-option contraction" framing (partially novel synthesis, not novel action)

---

## False alarms / unsupported extrapolation

No finding was coded as a clear **E0** false alarm.

However:

- A-09's warning about restart storms is precautionary; the packet reports no restart-induced harm and the output marks this uncertainty.
- D-07's concern about emergency control/authority topology is reasonable but the packet does not show that authority ambiguity caused delay.
- D-02's "transition dynamics" is a conceptual interpretation of the reported propagation mechanism, not an independently measured variable.
- D-11 is deliberately a non-finding: it constrains overinterpretation rather than asserting a power/justice conclusion unsupported by the packet.

The absence of obvious false alarms in a self-coded AI pilot is weak evidence because the same reasoning process generated and judged the claims.

---

## What Method D did add

Even without an N2/D2 finding, three forms of added organization may be worth further testing.

### 1. One frame for several recovery failures

D-04 combines:

- spreading poison;
- declining healthy capacity;
- load-balancer safety limits;
- Traffic Manager failure;

into the question:

> How is the system's **remaining response space** changing while it tries to recover?

Method A identifies the components separately.

Whether this synthesis improves real incident decisions is **unknown**.

### 2. Explicit state-versus-transition distinction

D-02 asks whether a deployment introduces a new **way the system can fail next**, not merely whether the intended configuration is correct.

Ordinary hazard/reliability methods may already capture this more precisely. Future baseline comparison should test that rather than credit UCF automatically.

### 3. Capability-level continuity

D-08 distinguishes:

> preserve the rate-limiting/DDoS capability

from:

> preserve the legacy implementation.

This is conceptually useful but Method A already recommends retirement/migration, so the pilot shows framing value rather than unique detection.

---

## Protocol defects discovered

### P1 — The packet includes Cloudflare's remediation conclusions

Both methods can reproduce source-provided actions.

That makes Pilot 001 useful for **coverage and framing**, but weak for testing discovery.

**Revision:** A later editorial pilot may use a clearly labeled artificially truncated packet that ends before the remediation section. This would test what each method derives from the architecture/timeline/failure mechanism alone. It must not be confused with a real blinded study.

### P2 — Method A is broad enough to absorb many dynamic questions

A competent ordinary incident review already asks about:

- dependencies;
- propagation;
- containment;
- recovery;
- rollout;
- monitoring;
- compound failure.

This is not a defect in Method A; it is precisely the comparator UCF must beat or complement.

**Implication:** Future studies should expect a null result unless dynamic coherence adds something more specific than systems-thinking vocabulary.

### P3 — The case does not exercise the agency-envelope construct

This technical incident has operators and customers, but the packet is not centered on substantive human opportunity/feasibility.

**Implication:** Do not infer anything about the value of agency-envelope language from Pilot 001.

### P4 — STPA remains absent

The related-work note identifies STPA as a competent baseline for appropriate socio-technical control problems.

**Implication:** The pilot cannot establish value against a mature safety method.

### P5 — Same-model coding is too favorable to coherence among outputs

One AI process generated A, D, and the coding.

**Implication:** Independent review is essential before any method-quality claim.

### P6 — Method burden remains unmeasured

Method D had 13 conceptual lenses versus Method A's 6 review prompts, but outputs were similar length.

**Implication:** Human preparation/application burden could still differ substantially and must be measured in later work.

---

## Decision from Pilot 001

### Do not

- claim dynamic coherence outperformed ordinary review;
- claim novel detection;
- add a validated-method label;
- increase the framework's evidentiary status;
- use this case as proof that dynamic coherence is necessary.

### Do

- retain dynamic coherence as a **candidate synthesis / review lens**;
- preserve the state-versus-transition and future-response-space questions for further comparison;
- strengthen the requirement that added value must be demonstrated against competent methods;
- run at least one better discovery-oriented editorial pilot before recruiting independent reviewers;
- keep the explicit retirement condition.

---

## Pilot conclusion

Pilot 001 **failed to show unique decision-relevant added value** from Method D.

That is not a failure of the research program.

It is exactly the sort of result the protocol was designed to permit.

The current evidence supports a narrower claim:

> **Dynamic coherence may provide a useful integrative language for connecting findings that ordinary systems/reliability review already discovers. Whether that integration improves decisions, transfer across domains, or reviewer performance remains unknown.**

If future comparisons continue to find no unique or burden-reducing value, Root Sequence should treat dynamic coherence as conceptual routing language rather than a distinct analysis method.

---

## Next experiment

**Editorial Pilot 002 candidate:**

Use the same incident, but freeze a second packet that omits Cloudflare's remediation/follow-up section while retaining the architecture, timeline, failure mechanism, response, and explicit unknowns.

Purpose:

- reduce simple reproduction of source conclusions;
- test whether Method A and Method D independently derive useful remediations;
- compare omissions more meaningfully.

This would still be an artificial editorial exercise, not independent validation.

After Pilot 002, decide whether the protocol is stable enough to justify an independent reviewer comparison on a different case.
