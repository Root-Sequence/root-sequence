# T-003 case selection — 2026-09-24

**Status:** FROZEN FOR EDITORIAL PILOT  
**Protocol:** [T-003 added-value comparison](t003-added-value-protocol.md)  
**Selection date:** 2026-09-24  
**Method outputs generated before this record:** none

## Selected case

**Cloudflare incident on June 20, 2024**

Primary source:

- Cloudflare, "Cloudflare incident on June 20, 2024," published June 26, 2024: https://blog.cloudflare.com/cloudflare-incident-on-june-20-2024/

## Why this case

It satisfies the protocol's first-case criteria:

- public;
- non-clinical and non-intimate;
- bounded incident;
- one detailed primary-source postmortem;
- explicit architecture, timeline, failure propagation, incident response, and remediation;
- real feedback, dependencies, automation, legacy components, rollout process, and future design changes;
- no need to infer private human experience.

It is **not** selected because its conclusion already matches Root Sequence.

## Anti-cherry-pick rule

Before any method output, candidate incident reports were gathered from official engineering/postmortem sources.

We deliberately excluded Cloudflare's November 2023 / March 2024 repeat data-center-power pair from the first pilot because the second event explicitly tests how prior history changed later response. That makes it unusually favorable to the new framework's central intuition and therefore a poor first falsification-risk case.

The June 20 incident was chosen instead because:

1. its primary postmortem is detailed enough to freeze a self-contained evidence packet;
2. it contains ordinary engineering failure modes a competent incident review should already detect;
3. its central story is not "we learned from a prior identical event";
4. it therefore creates a credible possibility that the dynamic-coherence method will add **nothing unique**.

## Decision question

> Given only the frozen evidence packet, what design, operational, rollout, monitoring, dependency, and recovery changes should be prioritized to reduce recurrence or impact of a similar incident?

This asks for actionable review findings rather than a retrospective label.

## Methods in the first editorial pilot

### Included

- **Method A:** competent ordinary incident/system review.
- **Method D:** frozen dynamic-coherence review from the T-003 protocol.

### Not included

- **STPA:** not labeled or simulated in the first pilot because this pass has not established sufficient analyst fidelity to STPA. A future comparison can add STPA after method-fidelity review.
- **Capability-oriented check:** omitted because human substantive opportunity is not central to this technical incident.

## Interpretation boundary

The first comparison is an **EDITORIAL PILOT** run by the same AI-assisted research process that helped draft the framework.

It can reveal:

- protocol defects;
- duplicate questions;
- obvious false alarms;
- coding ambiguity;
- whether the dynamic prompt produces usable findings at all.

It cannot establish:

- independent reviewer agreement;
- method superiority;
- empirical validity;
- novelty;
- generalizability.

## Freeze rule

The evidence packet at [t003-evidence-packet-cloudflare-2024-06-20.md](t003-evidence-packet-cloudflare-2024-06-20.md) is the only factual case material available to Method A and Method D in the editorial pilot.

No live browsing, hidden source expansion, or later incident knowledge may be used during the method outputs.

If the packet proves materially incomplete, stop the run and create a new packet version rather than silently adding evidence.
