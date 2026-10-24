# Public Seed placement

**Current source status — 2026-10-19 (UTC)**

`site/index.html` is the canonical reader-facing Root Sequence website source.
Rae approved the professional-refresh source for publication on 2026-10-19 (UTC).
`approval.json` identifies its exact page/publisher digest. The generated release
contains only the single page and generated hosting support files. See the
[site guide](README.md) and [copy review](COPY-REVIEW.md).

The earlier 11-page candidate is retained under
`site/legacy-public-seed-v0.1/` for history only. Existing research files remain
the substantive home of the arguments, and the standalone Wiki remains the
shared project reference. Do not create duplicate canonical copies here.

## Historical hosting note — 2026-09-18

The September 18 placement record reported staged-origin verification and a
web-only DNS cutover, with certificate issuance and the final public-domain
browser check still pending at that time. Fastmail DNS and mail were retained.
Current hosting, DNS, and certificate state must be checked before a later
release; this historical note does not establish their present state.

Deploy only the approved generated output. Never publish the repository root,
the legacy source directory, private Wiki material, or unpublished fiction.

## Proposed Stoned Age route: 2026-10-24

Rae suggested adding the existing research suite at `/stonedage/`. The proposed combined publisher reads `research/the-stoned-age/` and exports only its named reading files under that route. It does not create a second maintained copy in `site/`. Source records remain in the research directory and are linked on GitHub where they are not exported.

The original homepage source, publisher and approval remain intact. The proposed workflow uses `build_research.py` for the combined artifact and requires a separate matching `stonedage-approval.json` before release. That record is pending. This proposal does not publish the route, approve research findings or finish author, scholarly or cultural review. See the [site guide](README.md#proposed-research-route-24-october-2026).
