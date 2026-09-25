# T-003 added-value comparison — protocol draft

**Status:** UNRUN / preregistration candidate  
**Date:** 2026-09-24  
**Research area:** Coherent Systems living paper  
**Purpose:** Test whether the proposed relational/dynamic coherence review adds decision-relevant information beyond competent existing review methods, without hiding extra burden, false alarms, or duplicated findings.  
**Not evidence:** Writing this protocol does not validate the method.

## 1. Research question

For the **same bounded evidence packet and design decision**, does the proposed Coherent Systems / dynamic-coherence review identify consequential, evidence-traceable considerations that a competent baseline review does not, and at what additional cost in reviewer time, information demands, ambiguity, and false alarms?

The comparison is allowed to return:

- useful added value;
- useful synthesis but no unique findings;
- excessive burden;
- misleading additional findings;
- no meaningful difference;
- a reason to narrow or retire part of the framework.

No result is required to favor the proposed method.

---

## 2. Why this protocol exists

A flexible framework can appear insightful simply because it is allowed to ask more questions after seeing the case.

That is not a fair test.

The comparison therefore freezes:

- the task;
- the evidence packet;
- the method prompts;
- the available time;
- the coding rubric;
- the definition of a consequential finding;

before outputs are compared.

An AI comparing its own responses is an **editorial dry run**, not independent validation.

---

## 3. Case-selection criteria

The first case must be:

- public or fully synthetic with no private-person data;
- non-clinical and non-intimate;
- bounded enough for a reviewer to inspect the whole packet;
- rich enough to include at least one dependency, feedback path, affected party, and future transition;
- not authored specifically to demonstrate a known UCF failure mode;
- not the existing healthcare proxy case whose conclusion is already known;
- not a Coherent World simulation result;
- not a case whose "correct answer" is defined by Root Sequence canon.

Preferred domains:

- infrastructure/service fallback;
- repair/service architecture;
- provider dependency and migration;
- accessibility under disruption;
- community degraded mode.

The case-selection decision and reason must be recorded **before** any method is applied.

---

## 4. Shared evidence packet

Every method receives exactly the same packet:

1. case description and decision question;
2. actors/affected parties explicitly named in the source;
3. architecture/process diagram if available;
4. known constraints;
5. observed or stipulated outcomes;
6. known uncertainties;
7. source provenance;
8. time horizon;
9. what information is intentionally unavailable.

If a method requests more information, record the request. Do not silently give one method extra facts.

A missing fact may itself be a finding.

---

## 5. Methods

### Method A — competent ordinary review

Use the review method that a competent practitioner would reasonably apply to the selected case.

Its prompt/procedure must be documented before output generation. It must not be deliberately weakened to make UCF look broad.

At minimum it should ask about:

- purpose and requirements;
- stakeholders / affected users;
- dependencies;
- failure modes;
- constraints;
- maintenance/operations;
- obvious alternatives;
- known risks and tradeoffs.

If the case has a recognized domain method, prefer that over a home-made generic checklist.

### Method B — STPA, when appropriate

If the selected case is a socio-technical safety/control problem for which STPA is a credible fit, prepare an STPA analysis following the Leveson & Thomas handbook rather than a simplified caricature.

Record:

- analyst experience/training;
- preparation time;
- losses;
- hazards;
- control structure;
- unsafe control actions;
- loss scenarios;
- assumptions and omitted scope.

If no reviewer with sufficient STPA fidelity is available, do **not** label a casual checklist "STPA."

### Method C — capability-oriented agency check, when people’s practical options are central

Use capability-approach concepts only for the question they actually address: whether options are real/substantive opportunities rather than merely formal choices.

Do not pretend this is a full engineering method.

Record:

- nominal options;
- conversion factors / practical barriers visible in the evidence;
- real opportunities affected;
- whose capability is being discussed;
- unresolved value judgments.

### Method D — proposed Coherent Systems / dynamic-coherence review

Use the exact prompt below without adding case-specific questions after seeing the packet.

---

## 6. Frozen dynamic-coherence prompt

For the stated system, boundary, decision, and evidence packet:

1. **Present fit:** What currently works, for whom, and under which assumptions?
2. **Relational consequences:** Which affected people, systems, dependencies, resources, or burdens sit inside or outside the chosen boundary?
3. **State change:** What changes immediately if the proposal is adopted?
4. **Transition change:** What changes in how the system will respond to later conditions—rules, thresholds, dependencies, topology, learned behavior, maintenance, or available actions?
5. **History / path dependence:** Which earlier conditions materially constrain the present, and which consequences of this decision are likely to persist? Name the mechanism rather than saying only that history matters.
6. **Future possibility:** Which meaningful actions become easier, harder, newly dependent, or unavailable for each materially affected actor? Distinguish nominal availability from practical feasibility when the evidence supports it.
7. **Feedback:** Which consequences will become visible, to whom, how quickly, and with what uncertainty?
8. **Revision power:** Who can change, appeal, repair, reverse, exit, or replace the arrangement after mismatch appears?
9. **Continuity / transformation:** What capability, relationship, identity, or function is meant to persist? Under what conditions should transformation rather than restoration be considered?
10. **Externalized effects:** Which costs, risks, labor, or ecological/material demands may be displaced beyond the local objective?
11. **Normative disagreement:** Which purposes, burdens, or decision rights remain contested rather than settled by functional success?
12. **Evidence and alternatives:** Which statements are observed, inferred, assumed, or normative? What competing explanation or design should remain live?
13. **Retirement check:** Which of these observations would a competent baseline method already capture? Do not claim added value for duplicated findings.

Output findings individually with source/evidence locator, affected party, consequence, timescale, and uncertainty.

Do not produce an overall coherence score or winner.

---

## 7. Finding definition

A **finding** is one specific statement that could plausibly change:

- a design decision;
- a requirement;
- a test;
- a risk treatment;
- a maintenance plan;
- a migration/exit plan;
- an accessibility provision;
- an authority/governance decision;
- a request for missing evidence.

Do not count:

- restating the prompt;
- renaming an already-described fact;
- unsupported speculation;
- generic warnings that do not connect to the case;
- stylistic differences;
- duplicate findings split into several bullets.

---

## 8. Finding coding

Independent coders should classify each finding:

### Evidence traceability

- **E2:** directly supported by packet evidence;
- **E1:** reasonable inference with explicit basis;
- **E0:** unsupported / cannot be traced.

### Consequence

- **D2:** plausibly decision-relevant under the stated task;
- **D1:** relevant context but unlikely to change the decision;
- **D0:** not materially relevant.

### Novelty relative to another method

- **N2:** substantively absent from comparison method;
- **N1:** partially present / differently developed;
- **N0:** same substantive finding already captured.

### Error / false alarm

Flag a finding when:

- it contradicts the evidence packet;
- imports an unsupported actor, mechanism, or harm;
- treats a normative preference as an observed fact;
- applies a domain concept outside its justified scope;
- requests unnecessary sensitive information.

Coding disagreements remain visible.

---

## 9. Primary outcomes

Report separately:

1. number of **E1–E2 / D2** findings per method;
2. number of **N2** decision-relevant findings after adjudication;
3. unsupported / false-alarm count;
4. duplicated-finding count;
5. reviewer preparation time;
6. analysis time;
7. additional-information requests;
8. unnecessary-information requests;
9. disagreements between reviewers/coders;
10. findings that changed a proposed decision or test.

Do not aggregate these into one method score.

---

## 10. Burden and privacy outcomes

Record:

- pages/minutes of method preparation;
- specialist knowledge required;
- evidence fields requested;
- whether requested data are sensitive;
- whether the method encourages boundary expansion beyond what is necessary;
- cognitive/participation burden on affected people;
- whether the method can reach a legitimate "not enough information" result.

A method that finds more by demanding intimate or unnecessary data may be worse for the stated task.

---

## 11. Reviewer structure

### Editorial pilot

May be run by project authors/AI only to find protocol defects.

It cannot establish independent agreement or superiority.

Label all results **EDITORIAL PILOT**.

### Independent review

For a stronger test:

- at least two people apply each method independently;
- at least two coders compare findings;
- method identities may be masked during finding coding where practical;
- conflicts are recorded, not silently resolved by the project author;
- domain-method fidelity receives separate review.

A future participant study requires its own consent, accessibility, privacy, withdrawal, and oversight plan.

---

## 12. Pre-specified failure / retirement signals

The proposed review should be narrowed, decomposed, or retired for this use if:

- it produces no decision-relevant unique findings across repeated cases;
- unique findings are mostly unsupported;
- useful additions are already obtained more cleanly by one established method;
- burden or data demands are materially higher without corresponding value;
- reviewers cannot apply the vocabulary consistently;
- "coherence" tracks approval rather than a specified relation/mechanism;
- path dependence / future possibility language does not change any actual design or evidence question.

A null result is a successful research outcome.

---

## 13. Interpretation boundary

Even a favorable result would show only that the procedure added value **for the tested task, evidence packet, reviewers, and baselines**.

It would not establish:

- a universal theory of coherence;
- cross-domain causal identity;
- a validated scalar;
- superiority over every systems method;
- a consciousness, trauma, or intelligence theory;
- normative legitimacy of the resulting decision.

---

## 14. Required preregistration record before execution

```text
CASE:
CASE SOURCE:
DECISION QUESTION:
WHY CASE WAS SELECTED:
EVIDENCE PACKET HASH / VERSION:
METHOD A:
METHOD B (IF USED):
METHOD C (IF USED):
METHOD D VERSION:
REVIEWER QUALIFICATIONS:
TIME LIMITS:
CODERS:
CODING RUBRIC VERSION:
KNOWN CONFLICTS OF INTEREST:
WHAT WOULD COUNT AS A NULL RESULT:
DATE FROZEN:
```

Do not modify the frozen prompt or packet after seeing method outputs without declaring a new exploratory round.

---

## 15. Current status

**UNRUN.**

No case, reviewers, coders, or outputs are registered by this document.

The next legitimate action is case selection and packet freezing—not writing a conclusion.

---

## Related

- [Open questions / T-003](../open-questions.md)
- [Related work](related-work.md)
- [Dynamic Coherence and Adaptive Continuity](../../../concepts/dynamic-coherence.md)
- [UCF dynamic-coherence evidence reconciliation](https://github.com/Root-Sequence/universal-coherence-framework/pull/6)
- Leveson & Thomas, *STPA Handbook* (2018): https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf
