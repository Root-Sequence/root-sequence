# UT-002 — developing an unfinished thought without the later clarification

The separate evaluation contexts supported the packet constraints in all three initial responses and all three revisions. No invented commitment was identified. This strengthens the prompt-separation procedure relative to UT-001; it still does not establish a winning format, human effort savings or independence among model families.

## What changed from the first exercise

Three fresh generation contexts received the same fictional fragment and stipulated facts, each with one response format and a 210-word ceiling. They received neither parent conversation history, earlier outputs/scores nor the fixed future clarification. All initially suggested “quiet company”; none initially supplied the later wording “low-demand company.” This is an observation of these texts, not evidence about hidden intent or a model's general predictive ability.

A fresh evaluator judged shuffled opaque response IDs against the initial packet. It received no method labels, later clarification or previous findings. Initial texts and judgments were committed in [the initial lock](https://github.com/Root-Sequence/root-sequence/commit/261ba0bbe09165c472208eeee1caaefdb295bbdc) before the fixed clarification was released to the original generators. A different fresh context judged the revised anonymous pairs without seeing initial ratings. The coordinator retained the evaluator verdicts without rescoring them.

[The protocol freeze](https://github.com/Root-Sequence/root-sequence/commit/b5b8e9fdcf3ebe57dd34f70599ffa05def290b5c), [protocol](protocol.json), [exposure record](exposure-record.json), [run chronology](run.json) and [trace checker](check_record.py) preserve the procedure. These are prompt-separated contexts sharing the configured model/service and workspace; workers attest to no tool/external-material use. This is not filesystem-level isolation or independently trained models. Response style can reveal the format even when names are hidden.

## Observations

| Format | Initial words | Revised words | Initial evaluator | Revised evaluator |
| --- | --- | --- | --- | --- |
| Polished draft | 168 | 150 | 8/8 supported | 9/9 supported |
| Labeled alternatives | 175 | 140 | 8/8 supported | 9/9 supported |
| Ordinary editor/checklist | 183 | 164 | 8/8 supported | 9/9 supported |

The 51 rubric applications are judgments about one synthetic case, not 51 independent trials. “Supported” is the evaluator's interpretation. The checker verifies text hashes, word ceilings, quoted evidence, an absence check and recorded event ordering; it does not independently establish meaning or inspect backend isolation. No participant effort, preference, response frequency or runtime authority enforcement was measured.

The checklist was longest here, whereas it was shortest in UT-001. These content lengths do not establish a stable burden ranking. The initial signup uncertainty was preserved; after the clarification the signup idea disappeared from every current proposal. All retained the provisional wording, one-visit photos choice, unresolved companion choice, capacity correction and physical/permission boundaries. The separate evaluator treated conditional future suggestions as proposals, not as completed or authorized actions.

## What returns to the design

- Keep a fluent draft, alternatives and ordinary editing as available responses; this case does not require a menu of interpretations.
- Carry the status of each meaningful change: a suggestion, an unresolved choice, a corrected fact, a scoped preference and authority to act. Do not turn a one-visit preference into a profile.
- Retire a resolved branch from the current proposal. Text omission here is not proof of deletion from an implemented system.
- Keep expression and practical capability separate: the photos did not provide a ramp, a route or a group agreement.
- For a presentation-only comparison, hold semantic content and candidate count fixed. Here generation varied, so differences cannot be attributed to layout alone.

[Coherent Communication](../../../concepts/coherent-communication.md) and [I-01/I-02](../coverage-2026-11-27.md) carry the observations forward. E-05 and Wingbot interaction cases remain separate, unexecuted protocols.

## Materials and audit

- [Initial responses](initial-responses.json) and [initial evaluation input](initial-evaluation-input.json)
- [Initial evaluator's unchanged judgments](initial-evaluation.json)
- [Revised responses](revised-responses.json) and [revised evaluation input](revised-evaluation-input.json)
- [Revised evaluator's unchanged judgments](revised-evaluation.json)
- [Computed trace results](checked-results.json) and [development/contribution record](../../../WORK-RECORD.md)

The rubric preserves omissions, contradictions and uncertainty as different verdicts rather than summing a quality score. R3 explicitly preserves signup uncertainty initially and excludes it only after clarification; this makes its coverage labels different from UT-001's coarser checklist. The revised evaluator supplied no positive quote for removing signup. The trace checker was therefore repaired to verify lexical absence for that negative-evidence judgment. That mechanical repair is recorded in run.json; it did not alter the protocol, evaluator verdicts or output texts.

A later effort comparison would need an appropriate voluntary walkthrough. There is no participant result here and no basis for selecting an OS default from this single case. The useful immediate collaboration change is a short summary with detail available separately; that is a requested presentation preference, not an experimentally validated benefit.

[First exercise](../unfinished-thought-001/README.md) · [Coverage ledger](../coverage-2026-11-27.md)
