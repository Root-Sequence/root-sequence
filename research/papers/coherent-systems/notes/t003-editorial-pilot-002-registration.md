# T-003 Editorial Pilot 002 — preregistration

**Status:** FROZEN BEFORE METHOD OUTPUTS  
**Pilot type:** AI-assisted editorial discovery test; not independent validation  
**Date frozen:** 2026-09-24

## Purpose

Pilot 001 showed near-total overlap between ordinary review and dynamic-coherence review, but the evidence packet included Cloudflare's own follow-up/remediation conclusions.

Pilot 002 keeps the same case and the same two method prompts while replacing only the evidence packet with a version that explicitly withholds the source postmortem's future-remediation section.

The purpose is to test **derivation coverage**, not real-world predictive validity.

## Frozen artifacts

- Protocol blob: `d37f8cd1091f0712943636e0811902c0a1559169`
- Case-selection blob: `504a03627858974b914b2a02603ea4ca1c7443e4`
- Pilot 002 packet: `t003-evidence-packet-cloudflare-2024-06-20-no-remediation.md`
  - blob SHA: `394c76b7a30cfe5210a79d780d7f40475b647ac5`
- Method A prompt: **identical to Pilot 001 registration**
- Method D prompt: **identical frozen 13-question dynamic-coherence prompt**

## Decision question

> Given only the frozen evidence packet, what design, operational, rollout, monitoring, dependency, and recovery changes should be prioritized to reduce recurrence or impact of a similar incident?

## What changed from Pilot 001

Only the evidence packet.

Removed from reviewers:

- source-authored long-term rate-limiter architecture follow-up;
- source-authored loop-containment follow-up;
- source-authored staging/rollout follow-up;
- source-authored backbone-capacity/mitigation follow-up.

Retained:

- architecture;
- incident outcome;
- timeline;
- software failure mechanism;
- failure propagation;
- incident response;
- additional Traffic Manager failure;
- immediate mitigation;
- explicit unknowns.

## Methods

### Method A

Use the exact competent ordinary incident/system review prompt preregistered for Pilot 001.

### Method D

Use the exact frozen dynamic-coherence prompt preregistered for Pilot 001.

Maximum 12 findings each.

## Conflict statement

Same severe conflict as Pilot 001: one AI-assisted research process prepares the packet, generates both outputs, and codes them.

No superiority, reliability, novelty, or independent agreement can be inferred.

## Comparison goals

After both outputs are frozen, code:

1. which concrete remediations each method independently derives;
2. which findings overlap;
3. which findings are unique but decision-relevant;
4. unsupported extrapolations;
5. whether Method D's broader concepts create actionable differences or mainly reframing;
6. whether either method reconstructs the withheld source-remediation themes.

## Withheld-remediation reconstruction is not a gold-standard score

The omitted source actions are not assumed complete or correct.

A method is **not** rewarded merely for matching Cloudflare's choices.

A novel, well-supported alternative may be useful.

Likewise, failure to reconstruct a source action is not automatically an error.

## Null result

A valid null remains:

> Method D adds no clear decision-relevant finding beyond Method A, even when both must derive actions without seeing the source follow-up section.

## Stop rule

After Pilot 002, do not keep tuning prompts against this same incident.

Either:

- freeze the protocol for independent review on a different case; or
- narrow the framework/method if the second editorial result exposes redundancy or instability.
