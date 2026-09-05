# SECI Structured Observations

Machine-readable observation records for events and experiment results tracked by SECI.

## Current records

- [`2026-07-openai-artifactory.json`](2026-07-openai-artifactory.json) — OpenAI / METR–Redwood Artifactory coordination incident; high-confidence core mechanism.
- [`2026-05-07-dsewiki.json`](2026-05-07-dsewiki.json) — DSEWiki public-web coordination investigation; substantial artifact evidence with less-settled attribution.

Records should conform to [`../observation.schema.json`](../observation.schema.json).

## Rule

A structured record is not automatically more trustworthy because it is structured.

The record should preserve:

- source quality;
- uncertainty;
- competing explanations;
- what the evidence supports;
- what it explicitly does not support;
- later corrections.

Controlled SECI experiment results can be promoted here only after their raw logs have been reviewed and the result is reproducible enough to be worth preserving as evidence rather than merely exploratory output.
