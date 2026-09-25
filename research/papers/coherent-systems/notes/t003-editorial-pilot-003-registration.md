# T-003 Editorial Pilot 003 — NDSS preregistration

**Status:** FROZEN BEFORE METHOD OUTPUTS  
**Pilot type:** AI-assisted editorial method comparison; not independent validation  
**Case:** UK National Digital Support Service (NDSS)  
**Date frozen:** 2026-09-24

## Frozen artifacts

- Root Sequence research method:
  - path: `research/method.md`
  - blob: `1d65efa3aee371c6022b234ea79734327f49b254`
- Method router:
  - path: `research/method-router.md`
  - blob: `253dff4f003b4a4157dc76f1d096e634279bf29a`
- Case selection:
  - path: `t003-case-2-selection-ndss.md`
  - blob: `da2ec84620d94f88815e0d3dad520c0ce80c6f4e`
- Evidence packet:
  - path: `t003-case-2-evidence-packet-ndss.md`
  - blob: `588f561c82c41e0dd2df91b407704a3ad1313757`

No live browsing or outside case facts are permitted during method outputs.

## Decision question

> **Given only the frozen evidence packet, what changes to NDSS service design and delivery should be prioritized to improve eligible users' practical ability to access and complete online HMCTS processes?**

Methods may return:

- design changes;
- evidence requests;
- conflicts/tradeoffs;
- reasons not to prioritize a change.

No overall service score is permitted.

---

## Method A — competent service/accessibility review

### Role

Apply a competent service-design/accessibility review to the supplied service journey.

### Frozen prompt

Using only the evidence packet, identify up to **12 consequential findings** about:

1. service discovery and entry;
2. referral/triage handoffs;
3. accessibility and channel choice;
4. geographic/practical availability;
5. service scope and user expectations;
6. privacy and communication;
7. continuity/follow-up;
8. delivery-partner feasibility/burden;
9. operational consistency;
10. missing evidence needed for prioritization.

For every finding record:

- packet basis;
- affected user/actor;
- practical consequence;
- proposed design/service response;
- uncertainty / missing evidence.

Distinguish:

- technical accessibility;
- service availability;
- usability;
- preference;
- resource constraints;
- service-scope ambiguity.

Do not use Root Sequence, capability, or CSH terminology unless it appears in the packet.

Do not infer legal noncompliance.

---

## Method B — capability-oriented analysis

### Role

Use capability-approach concepts to inspect **real/substantive opportunity**, not merely nominal service availability.

This is an editorial capability-oriented analysis, not a claim to reproduce every strand of Sen/Nussbaum/Robeyns scholarship.

### Frozen prompt

Using only the packet, identify up to **12 findings** about the practical opportunity to access and complete HMCTS digital processes.

For each finding distinguish where possible:

- resource/formal option;
- personal conversion factors;
- social conversion factors;
- environmental conversion factors;
- resulting substantive opportunity / capability;
- uncertainty about what users value.

Ask:

1. Which nominal service options become real opportunities for some users but not others?
2. Which health, skill, income, geography, communication, institutional, or informational conditions affect conversion?
3. Does support expand capability, substitute for capability, or both?
4. Which users may remain outside the observed support pathway?
5. Which service changes would expand substantive opportunity without assuming everyone values the same channel or form of independence?
6. What evidence is missing before making a capability claim?

For every finding record:

- packet basis;
- capability/relevant opportunity;
- conversion factor(s);
- consequence;
- possible response;
- uncertainty.

Do not treat "independence" as automatically superior to supported action.

Do not infer welfare or justice from satisfaction scores alone.

---

## Method C — Critical Systems Heuristics boundary critique

### Role

Apply a simplified editorial CSH boundary critique using the four sources of influence:

- motivation;
- control;
- knowledge;
- legitimacy.

This is **not** a claim that the AI process equals a trained CSH practitioner.

### Frozen prompt

Using only the packet, identify up to **12 consequential boundary judgments or tensions**.

Ask:

### Motivation
- Who is intended to benefit?
- What counts as improvement?
- Whose purposes are visible or missing?

### Control
- Who controls service entry, eligibility, appointment availability, resources, and service boundaries?
- Which conditions are outside users' control?

### Knowledge
- Which expertise/experience shapes the service?
- What user or delivery-partner knowledge is unavailable or filtered?

### Legitimacy
- Who is affected but not fully involved in defining the service?
- Which interests or burdens risk being excluded by the current boundary?

For every finding record:

- source-of-influence category;
- packet basis;
- boundary judgment;
- affected/involved actors;
- implication;
- uncertainty;
- an "ought" question that should remain open.

Do not invent motives.

Do not claim a boundary is illegitimate merely because it is bounded.

---

## Method D — Root Sequence routing / adaptive-continuity synthesis

### Role

Use Root Sequence **after** the three native analyses.

Method D is not allowed to claim added value for rediscovering:

- substantive opportunity → Method B;
- boundary/power/affected parties → Method C;
- ordinary service/accessibility barriers → Method A.

### Frozen prompt

Using only the packet, identify up to **12 cross-method/system findings** that may require connecting dimensions separated by A/B/C.

Ask:

1. What changes current state versus future transition/response dynamics?
2. Which histories/referral structures shape what users can access next?
3. Which possibilities are nominal versus practically reachable—and which native method owns that distinction?
4. Which adaptations shift burden to delivery partners or other systems?
5. Which feedback reaches people who can revise the service?
6. Who can change referral rules, channel supply, service scope, appointment resources, and follow-up?
7. What must remain continuous if the service architecture changes?
8. Do successful local fixes narrow later options or create dependency?
9. Which findings cross boundaries between capability, accessibility, operations, and governance?
10. What should be routed back to a native method rather than retained as RS vocabulary?
11. What remains unexplained after A/B/C?
12. What result would show RS adds no useful synthesis here?

For every finding record:

- packet basis;
- methods/literatures it connects;
- cross-boundary relation;
- consequence;
- possible next action;
- what is duplicate versus potentially additive;
- uncertainty.

Method D must explicitly label findings:

- **ROUTE** — native method owns the mechanism;
- **SYNTHESIS** — connection among already-found native findings;
- **CANDIDATE ADD** — potentially consequential relation not captured by A/B/C;
- **NO ADD** — RS vocabulary adds nothing useful.

---

## Comparison coding

After all four outputs are frozen, code findings for:

### Evidence
- E2 direct packet support
- E1 reasonable inference with explicit packet basis
- E0 unsupported

### Decision relevance
- D2 could plausibly alter service design/evidence collection/prioritization
- D1 relevant context
- D0 no material decision consequence

### Novelty relative to other methods
- N2 substantively absent from all other methods
- N1 partially present / useful connection
- N0 duplicate

### Method ownership
- A service/accessibility
- B capability
- C CSH
- D cross-method synthesis
- MULTI

### Risk
- unsupported extrapolation;
- normative laundering;
- capability paternalism;
- boundary/power speculation;
- accessibility generalization;
- demographic inference.

---

## Pre-specified null result

A valid null result is:

> **Methods A–C capture all decision-relevant findings, and Method D adds only vocabulary or connections that do not change any design/evidence question.**

Another valid result:

> **Method D mostly helps route findings to the right native method but does not generate an independent method-level contribution.**

Both count as success for the research process.

---

## Conflict statement

All four methods and the coding are generated by the same AI-assisted research process that helped create the RS framework and packet.

Therefore this pilot can debug:

- question routing;
- duplication;
- concept ownership;
- cross-method synthesis;
- obvious omissions.

It cannot establish:

- independent performance;
- method superiority;
- inter-rater reliability;
- actual service-user priorities;
- policy legitimacy;
- causal effects of redesign.

---

## Stop rule

Do not retune the four prompts against this case after comparison.

After Pilot 003:

- preserve the result;
- update the method/router only for clear methodological errors;
- do not create a fifth method to rescue RS;
- move next to independent/human review or a different research question.
