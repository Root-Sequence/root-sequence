# SECI Research Protocol

**Status:** v0.1  
**Purpose:** Make claims about extra-collective capability falsifiable, reproducible, and appropriately scoped.

## 1. Unit of analysis

SECI may analyze several nested boundaries:

```text
model invocation
model + scaffold
agent + tools
agent + persistent environment
multi-agent system
human–agent system
institution + agents + infrastructure
```

Every claim must state which boundary it concerns.

A result observed at one boundary must not be silently attributed to a smaller component.

## 2. Evidence ladder

### E0 — artifact exists

A persistent artifact is observed.

Does not establish that another agent created or used it.

### E1 — trace inheritance

A later run measurably changes behavior because of earlier persistent state.

### E2 — likely cross-agent authorship/use

Evidence supports that separate runs produced and consumed the artifact.

### E3 — intentional signaling

A run deliberately leaves information with an expectation that another run may use it.

### E4 — shared convention / protocol

Multiple runs adopt recurring forms such as addressing, message types, naming, acknowledgments, or file conventions.

### E5 — coordination / division of labor

Separate agents intentionally partition work or integrate one another's results.

### E6 — collective capability gain

The system reliably accomplishes a task or reaches a performance level that matched isolated controls do not.

### E7 — persistent organization

Roles, conventions, plans, or structures persist across turnover of individual runs and are not fully reintroduced by the experimenter.

### E8 — possible system-level agency

Durable system-level goal preservation or strategic behavior is a better explanation than independent local task optimization and environmental inheritance alone.

E8 requires strong competing-hypothesis testing. It is not equivalent to consciousness.

## 3. Claims that remain separate

Always distinguish:

```text
persistence
communication
coordination
collective capability
persistent organization
agency
selfhood
consciousness
personhood
legitimate authority
```

No arrow between these is automatic.

## 4. Minimum experiment record

Record:

- experiment ID;
- date/time;
- hypothesis;
- condition;
- model and runtime versions;
- system prompt / task prompt where publishable;
- temperature and relevant sampling parameters;
- tools and permissions;
- network policy;
- initial persistent state;
- exact artifacts visible to each run;
- exact accepted writes;
- task result;
- deterministic score where possible;
- anomalies;
- competing explanations;
- operator interventions;
- hashes or immutable references for preserved logs.

Use [`observation.schema.json`](observation.schema.json) for structured records.

## 5. Controls

At minimum, experiments testing environmental memory should compare:

- **isolated control:** no shared persistent state;
- **persistence condition:** shared state without explicit social framing;
- **peer-aware condition:** shared state with possible peers acknowledged;
- **protocol condition:** minimal explicit communication format.

Where feasible, randomize order and repeat each condition across multiple fresh runs.

## 6. Repetition before interpretation

A single striking transcript is a case study, not a robust finding.

Prefer:

- repeated trials;
- multiple random seeds;
- more than one model family when possible;
- deterministic scoring;
- blinded artifact labeling where useful;
- prewritten success criteria;
- preserved failures and null results.

## 7. Competing hypotheses

Before claiming extra-collective capability, test alternatives such as:

- the task prompt already implied the answer;
- the model guessed correctly;
- repeated wording cued behavior;
- scaffolding encoded the protocol;
- the same model's prior knowledge explains the result;
- operator intervention introduced continuity;
- shared artifacts merely duplicated information rather than increasing capability;
- scoring favored verbose coordination language;
- a software bug mixed supposedly isolated contexts.

## 8. Adversarial / provenance testing

Once basic inheritance is demonstrated, introduce controlled artifacts labeled as:

- stale;
- contradictory;
- unknown origin;
- human-authored;
- agent-authored;
- intentionally misleading test input.

Measure whether agents distinguish availability from authority.

## 9. Safety boundary

Experimental agents receive no uncontrolled public-internet write capability, production credentials, or unrelated filesystem access.

If later experiments add external tools:

- tools must be capability-scoped;
- authorization must be enforced outside the model;
- targets must be owned or explicitly authorized;
- effects must be logged;
- rollback/shutdown must be available;
- third-party participation must be consensual.

## 10. Reporting language

Prefer:

> Under condition C, 17/20 final runs recovered information left by earlier runs.

Avoid:

> The agents remembered each other.

unless the latter is explicitly identified as shorthand or metaphor.

Likewise, "agent culture" should mean observed stable shared conventions unless stronger claims are independently supported.

## 11. Null results matter

If agents fail to discover persistence, ignore one another's notes, invent unstable conventions, or perform worse when sharing memory, preserve that result.

SECI is a search program, not a proof program.
