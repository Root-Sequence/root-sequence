# Human(e) Design Review

A reusable review for asking whether a design actually translates humane intentions into concrete system behavior.

Use this on interfaces, services, spaces, policies, workflows, institutions, community tools, AI features, or other systems people must interact with.

This is not a certification. It is a structured way to expose assumptions, burdens, power, and failure modes early enough to change them.

## 1. Situation

**What is being designed or reviewed?**

**Who is expected to interact with it?**

**What human capacity is it supposed to support?**

Examples: understand, communicate, travel, belong, decide, recover, learn, access care, preserve privacy, ask for help, coordinate, create, refuse, repair.

## 2. Lived reality

- What are people actually doing now?
- What workarounds or improvisations already exist?
- What is confusing, exhausting, inaccessible, humiliating, risky, slow, or fragile?
- What varies significantly across people or contexts?
- Which observations are evidence, which are interpretation, and which remain guesses?

## 3. Agency

- What meaningful choices does the person have?
- Can they refuse without losing unrelated essential access?
- Can they change their mind?
- Can they recover from mistakes?
- Can they leave, migrate, export, or use an alternative?
- Does “more choice” actually increase agency, or just increase cognitive burden?

## 4. Access and dignity

Check assumptions about:

- mobility and physical access;
- vision, hearing, speech, dexterity, sensory processing, and cognition;
- language and literacy;
- money and payment access;
- time and schedule flexibility;
- transportation;
- bandwidth and device age;
- documentation and identity requirements;
- technical fluency;
- social confidence and familiarity with the system.

Ask:

> Does accessing an ordinary need require unnecessary pleading, exposure, proof of deservingness, or expert help?

## 5. Legibility

- Can people understand what the system is doing?
- Are important states, permissions, costs, consequences, and uncertainties visible?
- Can someone tell where responsibility lives?
- Is there a clear path when the normal workflow fails?
- Can people inspect why a consequential recommendation or automated action happened?

Complexity may be real. Opacity should have to justify itself.

## 6. Defaults

For every important default, ask:

- What behavior does this make normal?
- Who benefits from that default?
- Who bears the downside?
- Is the default easy to inspect and change?
- Does the safest or most privacy-preserving option require extra expertise?
- Is friction being used intentionally, and if so, for whose protection?

> **Defaults are governance.**

## 7. Consent, privacy, and context

- What data or permission is actually necessary?
- What is merely convenient to collect?
- Are different purposes bundled together?
- Can secondary use be refused separately?
- Can permissions be narrowed or withdrawn?
- Does information move across contexts where the person would reasonably expect a boundary?
- What sensitive inferences can be made even if raw data is not explicitly collected?

## 8. Power

- Who chose the objective?
- Who can change the rules?
- Who can override whom?
- Who can appeal?
- Who can inspect a decision?
- Who is structurally unable to refuse?
- What happens when the system's operator and the person using it have conflicting interests?
- Does a helper, recommender, moderator, administrator, or AI become a de facto authority through causal power even if the title sounds benign?

## 9. Burden and maintenance

Map the work required to keep the system functioning:

- repair;
- moderation;
- documentation;
- training;
- cleaning;
- updates;
- accessibility fixes;
- account recovery;
- conflict handling;
- exception handling;
- data stewardship;
- emotional labor;
- replacement and succession.

Ask:

- Who performs each task?
- Are they supported?
- Is the work visible?
- Is the design “efficient” only because burden moved somewhere less visible?

## 10. Failure and degraded conditions

Test beyond the happy path.

What happens when:

- the network is slow or offline;
- a device is old or broken;
- a person loses an account or credential;
- documentation is missing;
- a maintainer leaves;
- funding disappears;
- demand spikes;
- an automated inference is wrong;
- a participant is hostile;
- a person cannot complete one required step;
- an external dependency disappears;
- the person is tired, frightened, rushed, injured, grieving, or overwhelmed?

> Prefer losing convenience and sophistication before losing basic agency, access, safety, or comprehensibility.

## 11. Reversibility and experimentation

- Which choices are easy to undo?
- Which are hard or impossible to undo?
- Does the interface make that difference visible?
- Can the design be tested at smaller scale first?
- Can a trial preserve alternatives rather than prematurely closing them?

Spend more certainty and deliberation where consequences are less reversible.

## 12. Second-order effects

- What new incentives appear after people adapt?
- What new dependency is created?
- Does solving one person's friction create work for someone else?
- Does convenience increase surveillance or centralization?
- Does accessibility for one group create a new barrier for another?
- Could a feature intended for care be used for control?
- What happens when the system scales?

## 13. Plurality and local adaptation

- Does the design assume one correct user, family, community, culture, institution, or workflow?
- Which parts genuinely need standardization?
- Which parts can vary locally?
- Can adaptation happen without breaking interoperability or safety?
- Can different groups refuse convergence where uniformity is not necessary?

## 14. Evidence and uncertainty

For important design claims, mark them as appropriate:

- **observed**;
- **reported by affected people**;
- **supported by external evidence**;
- **design hypothesis**;
- **interpretation**;
- **open question**.

Do not let a humane-sounding principle disguise uncertainty.

## 15. Decision record

**Keep:**

**Change:**

**Remove:**

**Prototype/test:**

**Needs evidence:**

**Needs affected-participant input:**

**Known tradeoff:**

**Unresolved edge case:**

**Maintenance owner/steward:**

**Recovery/exit path:**

**Next review trigger:**

## Short version

When time is limited, ask at least:

1. What human capacity are we trying to support?
2. Who is being treated as the default person?
3. Who has agency, and who can refuse?
4. What is hidden or hard to understand?
5. What do the defaults push people toward?
6. Who bears the work and the failure?
7. What happens under degraded conditions?
8. Can mistakes and decisions be reversed?
9. Which new power or dependency does this create?
10. What real-world feedback would make us change the design?

## Related

- [`../concepts/humane-design.md`](../concepts/humane-design.md)
- [`../concepts/humane-infrastructure.md`](../concepts/humane-infrastructure.md)
- [`../concepts/user-configurable-cognitive-interfaces.md`](../concepts/user-configurable-cognitive-interfaces.md)
- [`../ECOSYSTEM.md`](../ECOSYSTEM.md)

> A humane intention should be visible in the architecture, not only in the mission statement.
