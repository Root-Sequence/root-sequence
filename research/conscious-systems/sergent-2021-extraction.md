# IA-02 — Sergent 2021: Partial Methods Extraction

**Status:** AI-assisted; author review pending<br>
**Scope:** Abstract, introduction, opening results, and indexed primary-text methods excerpts inspected (participants, tasks, controls, and MVPA). Complete methods, supplements, source data, and code have not been audited; no reanalysis. Direct full-text retrieval remains unreliable; indexed excerpts supplied the updates below.

## Compact evidence record

Source: [Sergent et al. (2021), DOI 10.1038/s41467-021-21393-z](https://doi.org/10.1038/s41467-021-21393-z). Locators refer to article sections.

| Field | Extracted information | Section |
| --- | --- | --- |
| Sample | Main: 25 enrolled; two discontinued, three excluded for artifacts in over 25% of trials; 20 analyzed | Methods, Participants |
| Manipulation | Vowels in continuous noise at varying signal-to-noise ratios; active/passive session order counterbalanced | Results, opening experiment |
| Awareness check | Active identity/audibility reports; passive sessions randomly intermixed mind-wandering probes with other tasks. Response screen followed the vowel by 2–3 seconds | Methods, Stimulus presentation and task |
| Controls | Main passive sessions used unrelated visual or amodal tasks: passive did not mean absence of all tasks | Results, opening experiment |
| Candidate marker | Single-trial activity bifurcation around 250–300 ms; compared with linear and nonlinear unimodal models | Abstract; Results, model comparison |
| Estimates and uncertainty | Full contrasts, intervals, validation procedure, and control-experiment details not yet inspected | Outstanding |
| Additional samples | Passive-only control: 10 enrolled, three EEG-quality exclusions, seven analyzed. Tone control: five, all analyzed | Methods, Control experiments 1–2 |
| Decoder validation | Ten-fold cross-validation; training/testing trials from distinct blocks. Stimulus decoding is not itself validation of the entire consciousness inference | Methods, Multivariate pattern analysis |

## Comparison with IA-01

Use the [Pitts extraction](pitts-2014-extraction.md) for its verified sample and condition estimates. These are not matched experiments or directly poolable effect sizes.

| Audit dimension | Pitts | Sergent |
| --- | --- | --- |
| Stimulus | Visual masking | Auditory noise |
| Main measurement | Scalp ERP component | Single-trial model of neural dynamics |
| Report reduction | Task-irrelevant stimulus conditions | Passive listening with intermittent probes |
| Remaining bridge | Behavioral checks to inferred awareness | Neural model to reported awareness |

**Project inference:** loss or attenuation of one ERP component and persistence of another neural dynamic are not logically contradictory. A component, a computational model, and a consciousness theory are different objects. Neither study alone establishes a sufficient mechanism for experience or settles which theory is correct.

**Correction, 2026-09-23:** The previous version wrongly presented sampled-report validation as necessarily a separate experiment. The main passive protocol itself included mind-wandering probes; the additional passive-only control is a different distinction. This was our extraction error, not an inconsistency in the paper.

**Inference limit:** intermittent reports reduce some reporting demands but do not eliminate expectations, attention, memory, or retrospective interpretation. This is a reason to narrow our conclusion, not a demonstration that those alternatives explain the result.

## Next bounded action

Complete the missing fields before proposing new experiments or reproducing numerical claims:

1. Complete the methods and supplement audit; do not treat access failures as missing reporting by the authors. The participant/task gaps above are now partly resolved through indexed primary text.
2. Verify probe frequencies, report coding, and which trials enter each statistical comparison; participant counts alone do not establish effective sample size for every analysis.
3. Establish how the bifurcation models were fitted and evaluated, separately from the verified decoder cross-validation. Check whether feature selection or fitting reused evaluation trials. This is a verification question, not an allegation of leakage.
4. Extract direct model comparisons and report-prediction estimates with uncertainty; distinguish active-session validation from passive sampled-report validation.
5. Check data/code provenance and licenses before any reanalysis. Record what is available versus what has actually been reproduced.

**Current gate:** incomplete methods extraction. The conceptual comparison is useful, but it is not a completed statistical audit, a preregistration, or evidence that all confounds have been removed.

[Inference audit](inference-audit.md) · [Conscious Systems index](README.md)
