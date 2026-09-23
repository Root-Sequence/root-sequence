# IA-02 — Sergent 2021: Partial Methods Extraction

**Status:** AI-assisted; author review pending<br>
**Scope:** Abstract, introduction, and opening results inspected. Full methods, supplements, source data, and code not inspected; no reanalysis. Retrieval failures prevented completing the methods record in this pass.

## Compact evidence record

Source: [Sergent et al. (2021), DOI 10.1038/s41467-021-21393-z](https://doi.org/10.1038/s41467-021-21393-z). Locators refer to article sections.

| Field | Extracted information | Section |
| --- | --- | --- |
| Sample | Twenty participants in the main active/passive comparison; recruitment and exclusions not yet inspected | Results, opening experiment |
| Manipulation | Vowels in continuous noise at varying signal-to-noise ratios; active/passive session order counterbalanced | Results, opening experiment |
| Awareness check | Active identity/audibility reports; randomly sampled reports in a task-free listening experiment. Exact probe schedule and that experiment's sample not yet inspected | Results; abstract |
| Controls | Main passive sessions used unrelated visual or amodal tasks: passive did not mean absence of all tasks | Results, opening experiment |
| Candidate marker | Single-trial activity bifurcation around 250–300 ms; compared with linear and nonlinear unimodal models | Abstract; Results, model comparison |
| Estimates and uncertainty | Full contrasts, intervals, validation procedure, and control-experiment details not yet inspected | Outstanding |

## Comparison with IA-01

Use the [Pitts extraction](pitts-2014-extraction.md) for its verified sample and condition estimates. These are not matched experiments or directly poolable effect sizes.

| Audit dimension | Pitts | Sergent |
| --- | --- | --- |
| Stimulus | Visual masking | Auditory noise |
| Main measurement | Scalp ERP component | Single-trial model of neural dynamics |
| Report reduction | Task-irrelevant stimulus conditions | Passive listening and separate sampled-report validation |
| Remaining bridge | Behavioral checks to inferred awareness | Neural model to reported awareness |

**Project inference:** loss or attenuation of one ERP component and persistence of another neural dynamic are not logically contradictory. A component, a computational model, and a consciousness theory are different objects. Neither study alone establishes a sufficient mechanism for experience or settles which theory is correct.

Do not collapse the main active/passive comparison and the sampled-report experiment into one protocol. Until the full methods are extracted, the equivalence of their tasks, samples, and awareness checks remains an open audit item.

## Next bounded action

Complete the missing fields before proposing new experiments or reproducing numerical claims:

1. Obtain accessible full methods and supplements through an ordinary publisher or author-provided source; do not treat access failures as missing reporting by the authors.
2. Separate every experiment's recruited/analyzed sample, exclusions, task instructions, session order, and probe timing.
3. Establish how models were fitted and evaluated, including whether feature selection or fitting reused evaluation trials. This is a verification question, not an allegation of leakage.
4. Extract direct model comparisons and report-prediction estimates with uncertainty; distinguish active-session validation from passive sampled-report validation.
5. Check data/code provenance and licenses before any reanalysis. Record what is available versus what has actually been reproduced.

**Current gate:** incomplete methods extraction. The conceptual comparison is useful, but it is not a completed statistical audit, a preregistration, or evidence that all confounds have been removed.

[Inference audit](inference-audit.md) · [Conscious Systems index](README.md)
