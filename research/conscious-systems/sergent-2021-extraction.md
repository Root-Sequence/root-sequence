# IA-02 — Sergent 2021: Partial Methods Extraction

**Status:** AI-assisted; author review pending<br>
**Scope:** Abstract, introduction, selected results, and indexed primary-text methods excerpts inspected (participants, tasks, controls, MVPA, and report prediction). Complete methods, supplements, source data, and code have not been audited; no reanalysis. Direct full-text retrieval remains unreliable; indexed excerpts supplied the updates below.

## Compact evidence record

Source: [Sergent et al. (2021), DOI 10.1038/s41467-021-21393-z](https://doi.org/10.1038/s41467-021-21393-z). Locators refer to article sections.

| Field | Extracted information | Section |
| --- | --- | --- |
| Sample | Main: 25 enrolled; two discontinued, three excluded for artifacts in over 25% of trials; 20 analyzed | Methods, Participants |
| Manipulation | Vowels in continuous noise at varying signal-to-noise ratios; active/passive session order counterbalanced | Results, opening experiment |
| Awareness check | Active identity/audibility reports; passive sessions randomly intermixed mind-wandering probes with other tasks. Response screen followed the vowel by 2–3 seconds | Methods, Stimulus presentation and task |
| Controls | Main passive sessions used unrelated visual or amodal tasks: passive did not mean absence of all tasks | Results, opening experiment |
| Candidate marker | Single-trial activity bifurcation around 250–300 ms; compared with linear and nonlinear unimodal models | Abstract; Results, model comparison |
| Estimates and uncertainty | Report-prediction procedure inspected below; full numerical contrasts, intervals, and control analyses remain unaudited | Outstanding |
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

## Report-prediction audit — 2026-09-23

**Source locators:** Results, “Predicting mind-wandering content from neural activity in the passive sessions”; Methods, “Predicting conscious report…” and “Predicting mind-wandering content…”; Figure 5C caption. Same primary source linked above; inspected through indexed text.

**Verified procedure:** model-derived high/low-state likelihood ratios were evaluated against reports using AUC. Report labels were not supplied to model fitting. Active labels used a 30% audibility criterion. Passive labels contrasted sound-on-mind with other responses, on probe trials. Figure 5C includes all stimulus intensities; shading denotes SEM, with FDR-corrected tests. Exact passive AUC estimates and intervals have not been extracted.

**Our inference:** predicting reported sound-related content is narrower than detecting every occurrence of auditory experience. A participant could hear the sound and have moved on to another thought by the probe. Conversely, a sound-related response need not establish that the preceding target vowel was consciously identified. These are possibilities the operational measure does not by itself rule out, not demonstrated explanations of the data.

Two separate questions therefore remain:

- **Outcome validity:** how reliably does this report category track the target experience during the earlier interval? Do not relabel “other response” as “unconscious trial.”
- **Incremental prediction:** does neural activity predict reports beyond stimulus intensity? Including all intensities is not proof of confounding, but an aggregate association alone cannot answer that question. Inspect existing intensity-conditioned analyses first; if absent, propose a within-intensity comparison or a held-out model comparison against an intensity-only baseline. Sufficient trials in both report categories are needed; do not invent that adequacy.

Not using report labels during fitting avoids one route to circularity. It does not, by itself, establish out-of-sample performance for every pipeline stage or prove that the recovered states are conscious versus nonconscious. Decoder validation, model comparison, report prediction, and interpretation must remain separate checks.

**Decision:** retain evidence for a relationship between neural dynamics and later reported content under reduced auditory-task demands. Do not promote it to an independently validated binary detector of experience. This is an audit of our inference, not a finding that the published study is invalid.

## Remaining bounded work

Complete the missing fields before proposing new experiments or reproducing numerical claims:

1. Complete the methods and supplement audit; do not treat access failures as missing reporting by the authors. The participant/task gaps above are now partly resolved through indexed primary text.
2. Verify probe frequencies and per-category trial counts; report coding is now checked above. Participant counts alone do not establish effective sample size for every analysis.
3. Establish how the bifurcation models were fitted and evaluated, separately from the verified decoder cross-validation. Check whether feature selection or fitting reused evaluation trials. This is a verification question, not an allegation of leakage.
4. Extract direct model comparisons and report-prediction estimates with uncertainty; check intensity-conditioned prediction before claiming performance beyond stimulus strength. Distinguish active-session validation from passive sampled-report validation.
5. Check data/code provenance and licenses before any reanalysis. Record what is available versus what has actually been reproduced.

**Current gate:** incomplete methods extraction. The conceptual comparison is useful, but it is not a completed statistical audit, a preregistration, or evidence that all confounds have been removed.

[Inference audit](inference-audit.md) · [Conscious Systems index](README.md)
