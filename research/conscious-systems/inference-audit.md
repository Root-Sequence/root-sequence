# CS-Q26–28 — Inference Audit

**Document role:** Fifth bounded research pass and reusable audit protocol<br>
**Status:** v0.1-dev; AI-assisted, author review pending<br>
**Evidence status:** Methodological proposal with three worked literature examples; no new data, completed preregistration, or validated consciousness test

## Outcome of this pass

Our proposed experiment is not yet a decisive three-way test of recurrent processing theory (RPT), global neuronal workspace (GNW), and higher-order theories (HOT). It currently compares candidate markers and evidence channels. Calling it decisive would require selective manipulations, independently justified measurements, specified theory versions, and sufficiently divergent quantitative predictions that we have not supplied.

That is a useful result of the audit: an experiment can reveal something about reporting, access, or memory without determining what produces experience. The revised near-term aim is to establish which inferences survive confound checks in existing studies before designing a new human experiment.

## Provisional answers

- **CS-Q26 — Separating consciousness from accompanying processes:** compare multiple evidence channels and vary report demands, attention, memory delay, and task relevance separately where feasible. No single design removes every confound; no-report conditions also lose direct trial-level evidence about experience.
- **CS-Q27 — Correlation, necessity, and sufficiency:** observation establishes association under its model; a well-controlled intervention can establish a causal effect on the measured outcome. A necessity or sufficiency claim additionally needs a specified target, background conditions, successful manipulation, and an inference from outcome to experience. Changing a report is not automatically changing experience.
- **CS-Q28 — What would count against a theory:** state an operational prediction from a particular version, its auxiliary assumptions, measurement sensitivity, and interpretation rules before observing results. A failed prediction can challenge that package without refuting every version of the theory.

## Audit record required for every claim

| Field | Required entry |
| --- | --- |
| Claim and scope | Particular content, access, capacity, or subject unity; organism and condition |
| Target interval | Start and end of the putative experience, distinct from probe and response times |
| Observation | Raw behavior, report, neural response, or intervention effect; keep this separate from its interpretation |
| Operational definition | Exact report category or measurement used, including thresholds and uncertainty |
| Inference bridge | Why this observation is evidence for the claimed experience or mechanism |
| Rival explanation | At least the strongest plausible non-experiential or weak-experience account |
| Control and its limit | What the design excludes, what it cannot exclude, and whether a control changes the target phenomenon |
| Theory commitment | Named version, necessary or sufficient condition, and the expected measurable contrast |
| Failure rule | What result lowers confidence, conditional on manipulation and measurement checks |
| Review depth | Abstract, full methods, supplementary material, preregistration, code, or data actually examined |

## Observation-to-inference matrix

The entries below are project audit rules, not universal diagnostic standards.

| Observation | Defensible immediate conclusion | Rival explanation or remaining gap | Required follow-up |
| --- | --- | --- | --- |
| Immediate specific content report | The person reports that content near the target interval | Guessing, criterion differences, expectations, or probe-related reconstruction | Catch trials, graded content and confidence questions, report latency, and independent discrimination measures |
| Accurate forced-choice response on an unseen trial | Task-relevant information influenced choice | Weak experience below a reporting threshold; nonconscious discrimination | Separate sensitivity from response criterion; examine graded visibility and uncertainty |
| No later occurrence or content recall | Retrieval failed at that test | No experience, failed encoding, forgetting, or inaccessible memory | Compare contemporaneous evidence and multiple delays; never equate this with no experience by itself |
| Pre-probe neural pattern predicts later report | The pattern carries predictive information about that report | Attention, encoding strength, decision evidence, or later access | Held-out validation, report-demand contrasts, and models of memory and decision |
| Decoder fails to recover content | This decoder did not recover it from these measurements | Limited sampling, inappropriate code assumptions, low sensitivity | Positive controls and sensitivity bounds; do not translate decoding failure into absent representation |
| P3b disappears when report is removed | That component depends on the changed task conditions | Experience, attention, or encoding also changed | Establish awareness evidence and inspect other predicted workspace dynamics |
| Stimulation reduces awareness ratings | Intervention affected the ratings | Sensory degradation, discomfort, attention, confidence, memory, or motor effects | Sham and control conditions, target engagement, multiple outcomes, and explicit mediation alternatives |
| Confidence changes at similar accuracy | Subjective evaluation changed while measured accuracy was similar | Response criterion or evidence distributions differ; accuracy may be imprecisely estimated | Model sensitivity, bias, and metacognitive performance separately; similar accuracy alone is insufficient |
| Large or complex distributed response | A measured network response has those properties | Broad arousal, noise, shared input, or a capacity that did not produce the target content | Content-specific and causal analyses; do not equate signal complexity with intrinsic causal integration |

## Three worked audits

### IA-01 — Is P3b necessary for visual experience?

**Extraction update:** The [methods record](pitts-2014-extraction.md) qualifies the summary below: it must not be generalized across stimulus categories. Use that record for condition-specific results and review scope.

**Observed:** Pitts and colleagues crossed awareness with task relevance. Visible task-irrelevant stimuli lacked the robust P3b associated with immediate task use, while an earlier posterior negativity remained.[^pitts]

**Bridge and alternative:** awareness in the relevant no-immediate-report conditions is inferred from behavioral checks rather than independently verified on every neural trial. Task relevance can change attention and other processing as well as reporting.

**Audit judgment:** evidence against a simple necessary-P3b marker. It neither establishes posterior recurrence as sufficient nor refutes every GNW account. Review scope here: publisher methods and discussion as a targeted reading, without data reanalysis or exhaustive supplementary-material extraction.

### IA-02 — Does late activity survive removal of overt report?

**Extraction update:** The [partial methods record](sergent-2021-extraction.md) corrects our earlier mistaken separation of the main passive protocol from sampled reports, records sample exclusions and decoder validation, and lists remaining uninspected fields. It does not constitute a completed methods audit.

**Observed:** Sergent and colleagues reported late bifurcation-like auditory responses without a continuous report task; activity predicted randomly sampled reports.[^sergent]

**Bridge and alternative:** the report link gives the neural pattern empirical relevance but is not independent proof of phenomenality. It can remain related to availability for later reporting or memory. Sparse probes also leave possible effects of anticipating a probe.

**Audit judgment:** strengthens the case for a late process beyond immediate motor reporting, and prevents equating absence of P300 with absence of every GNW-compatible dynamic. It does not independently eliminate RPT or HOT. Review scope here: publisher results and discussion; the linked dataset has not been downloaded or reanalyzed.

### IA-03 — What did the adversarial theory test test?

**Observed:** the Cogitate collaboration preregistered biological predictions from GNW and IIT and tested suprathreshold perception in 256 participants across three recording methods; some predictions were supported and others challenged.[^cogitate]

**Bridge and alternative:** this concerns specified spatial, temporal, and connectivity predictions during conscious perception. It is not by itself a contrast between no experience and experience, nor a direct computation of IIT's full causal structure.

**Audit judgment:** a model for agreeing on predictions and interpretations in advance; no general theory winner follows. Review scope here: primary-study abstract and prediction descriptions. The full preregistration, analysis code, and later responses remain to be audited.

## Repairs to our proposed design

1. **Remove the implication of a complete factorial design.** Task relevance and expectation of a report are not fully independent: once participants expect questions about a stimulus, that stimulus gains relevance. Repeated surprise probes are no longer fully surprising. Record the actual task and expectations for each condition.
2. **Separate stimulus manipulation from subjective visibility.** Researchers randomize stimulus strength or masking, not whether a participant experiences the target. Reported visibility is an outcome. Sorting into seen/unseen groups can also sort attention, evidence strength, and memory.
3. **Do not mistake scalp timing for selective mechanism measurement.** Early and late signals are candidate indicators. Neither a latency nor one scalp component establishes local recurrence, global broadcast, or a higher-order representation.
4. **Require pre-probe and post-probe separation.** A later report can reflect delayed access or reconstruction. No-report trials without a subsequent probe remain unlabeled for individual experience unless a justified independent bridge is supplied.
5. **Preserve a non-discriminating outcome category.** If all theories can accommodate the observation, the result constrains a marker or design rather than favoring a theory. Missing target engagement or inadequate sensitivity makes a null result inconclusive.

## Decision rules before data collection or reanalysis

For each tested implementation, specify the measurement, time window, region or system boundary, contrast, predicted direction and meaningful magnitude, and assumptions about its relationship to experience. Select outcomes and preprocessing on training or pilot material; evaluate predictions on held-out data where feasible. Set exclusion rules, stopping rules, multiplicity handling, and sample-size justification before confirmatory analysis. This document supplies none of the missing numerical commitments and is not a preregistration.

Classify the result using this sequence:

| Check | If it fails | If it passes |
| --- | --- | --- |
| Was the manipulation delivered and the intended process measurably affected? | No causal theory verdict | Assess measurement and confounds |
| Could the measurement detect the predicted effect under the specified conditions? | Null result remains inconclusive | Compare with the prespecified prediction |
| Does the effect remain after relevant alternative explanations are addressed? | Attribute it at the narrower supported level | Assess whether theories actually diverge |
| Is the outcome incompatible with the tested prediction but compatible with a rival's advance prediction? | Do not rank theories solely from this result | Lower confidence in the tested prediction package; specify surviving alternatives |

Absence requires an adequately sensitive test with a prespecified equivalence bound or another justified evidence model; a nonsignificant p-value alone is not evidence of equivalence. Conversely, two separately significant associations are not evidence that one theory explains more than another without an appropriate direct comparison.

Necessity and sufficiency must be qualified by background conditions. A disruption of process X followed by loss of experience evidence can support necessity in that preparation if measurement failure and off-target effects are addressed. Restoring X and restoring the evidence can strengthen a causal case, but X plus a working brain-body system is not proof that X alone is sufficient.

## Deliverable gate and next action

The initial conceptual sequence now has a first pass for each planned topic. Its output is a set of distinctions and conditional predictions, not an experiment ready to run.

**Next action: complete the outstanding IA-02 methods fields.** IA-01 now has a compact methods record; IA-02 has a partial extraction and cross-study comparison. Record participant numbers and exclusions separately for each experiment, stimulus and task conditions, awareness-check timing, exact contrasts, estimates and uncertainty. Use “not reported” only after checking the relevant source; otherwise use “not yet inspected.” Neither record is a statistical reproduction.

Proceed to a study proposal only when at least one rival prediction remains distinguishable after that comparison. If none survives, the useful contribution is a documented non-discrimination result and a sharper question. No new experiment, dataset analysis, or independent scholarly validation has occurred in this pass.

## References

[^pitts]: Pitts, Metzler, and Hillyard (2014), “Isolating neural correlates of conscious perception from neural correlates of reporting one's perception,” *Frontiers in Psychology* 5, 1078. [DOI: 10.3389/fpsyg.2014.01078](https://doi.org/10.3389/fpsyg.2014.01078).
[^sergent]: Sergent et al. (2021), “Bifurcation in brain dynamics reveals a signature of conscious processing independent of report,” *Nature Communications* 12, 1149. [DOI: 10.1038/s41467-021-21393-z](https://doi.org/10.1038/s41467-021-21393-z).
[^cogitate]: Cogitate Consortium et al. (2025), “Adversarial testing of global neuronal workspace and integrated information theories of consciousness,” *Nature* 642, 133–142. [DOI: 10.1038/s41586-025-08888-1](https://doi.org/10.1038/s41586-025-08888-1).

[Conscious Systems index](README.md) · [Open questions](open-questions.md) · [Transition matrix](transition-to-experience-matrix.md) · [System boundaries](system-boundary-matrix.md)
