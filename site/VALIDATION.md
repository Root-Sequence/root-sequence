# Local validation — 2026-09-16

## Approved router-role edition — September 25, 2026

- GitHub Actions run `36181297846` executed all 11 publication tests against
  the September 25 source; all 11 passed.
- The workflow reported exact source digest
  `45288440e4e5f04a6ded6660659bf6f01ade1faf856f59f859b959ee14ea0669`.
- The exact preview HTML SHA-256 is
  `723b6f5025328778fe205de1a36f62d6fa5fcbd0697aa388309bbf702cb95f31`.
- The run then stopped at the approval gate, as expected, because the prior
  September 18 approval still applied at that moment.
- Rae Lovejoy subsequently approved this exact September 25 source and preview;
  `approval.json` now records those hashes.
- The site footer/publication state and sitemap date are updated to
  September 25, 2026.
- The workflow permanently prints future publication digests before attempting
  release, making exact-source approval auditable from Actions logs.
- The router-role edition preserves the existing one-page visual structure and
  interaction architecture while updating the introduction, About explanation,
  repair example, metadata, and six selected research entry points.

The approval establishes permission to publish this exact source. The final
post-approval GitHub Pages run remains the deployment evidence and should be
recorded separately once complete.


## Router-role copy candidate — September 25, 2026

**Status: review candidate only; not approved or released.**

Connector-level structural checks on the branch found:

- one `h1`;
- 60 unique HTML IDs with no duplicates;
- 27 internal fragment links with no missing targets;
- English translation JSON parses and covers all 171 referenced i18n/aria keys;
- two executable inline scripts remain present and the CSP still declares two
  SHA-256 script hashes; the copy edit changed only HTML text, links, and the
  non-executable translation JSON;
- all new canonical GitHub destinations exist on current `main`:
  - `research/method.md`;
  - `research/method-router.md`;
  - `research/papers/coherent-systems/paper.md`;
  - `concepts/dynamic-coherence.md`;
  - `concepts/epistemic-discoverability.md`;
  - `concepts/legible-systems.md`;
  - `research/reading-trails/README.md`;
- the old selected-research labels (Intelligence Ecology, Events/patterns/scale,
  Resilience/graceful-degradation, historical-contingency entry) are no longer
  present in the selected-reading copy;
- required router-role copy is present in both visible HTML and the English
  translation table.

`test_site.py` was updated so this branch is treated as an **unapproved review
candidate** rather than falsely expected to match the September 18 approved
preview. The release approval record remains unchanged, so the actual
`build.py --release` gate is intentionally expected to reject this candidate
until Rae Lovejoy approves the exact current source.

The complete Python site test suite and browser-layout/render checks were **not
executed in this connector-only pass**. They remain required before publication.
No live-domain or deployment check is claimed.


## Approved Root Sequence name explanation — 2026-09-18

- The About section includes a compact explanation of “root,” “sequence,” and
  the question formed by the name, followed by a direct link to the canonical
  `concepts/root-sequence.md` page.
- The canonical destination exists on the research repository's `main` branch.
- A fresh preview build completed with source digest
  `cdf268f194aea69f1bee65dfdb6f3b1afd8e52a0dcff4a1069cfb1cbc419997d`.
- Rae Lovejoy approved the exact candidate with HTML SHA-256
  `08a1ce67f37f3db55e235cb3703bcdb552deead2ffd4aafd6cd732f69b384356`.
- All eleven publication tests pass, including the exact approval gate.
- Fresh preview and approved release builds complete successfully.
- Browser checks at 1280 × 720 and 390 × 844 found the new heading, copy, and
  canonical link. Both layouts were visually inspected, and the narrow layout
  had no horizontal document overflow.

## Approved Selected Research expansion — 2026-09-18

- The approved source contains six selected entries with distinct reader-facing
  roles: working paper, conceptual framework, design principle, systems method,
  systems note, and historical analysis.
- Reader-documentation and Idea Trail checks pass.
- A fresh preview build completed with source digest
  `7d009d9ea493e09db848823a399c9df8d7eebb4334b86aabc7c5343b89afebc3`.
- All eleven publication tests pass, including the exact approval gate.
- Fresh preview and approved release builds complete successfully.
- Browser checks at 1440 × 1000 and 390 × 844 found all six entries, the
  expected destinations, working contextual link details, and no horizontal
  document overflow. Desktop and mobile views were visually inspected.
- This validation records the approved local source and build. It is not a
  deployment or a live-domain check.

## Legible Systems source-route update — 2026-09-18

- The current single-page source now routes its Legible Systems link and
  contextual overlay directly to `concepts/legible-systems.md`.
- The change does not alter visible copy or layout.
- The updated inline-script Content Security Policy hash matches the script.
- All eleven offline publication tests pass, including the exact approval gate.
- Fresh preview and release builds completed with source digest
  `29333bdb919498771bcf514dd7becca13d89efd5cfa1845497c18eef1cadcd88`.
- Browser checks at 1440 × 1000 and 390 × 844 showed the expected headline,
  visible section, reading, and language controls, the new source destination,
  and no horizontal document overflow.
- This branch validation is not a deployment or a check of the live domain.

## Approved single-page edition — 2026-09-18

- The repository copy matches the approved preview byte-for-byte.
- Eleven offline publication checks pass.
- Checks cover the approval gate, page structure, links and fragments,
  self-contained assets, embedded font, Content Security Policy hashes,
  English-only source edition, required reading controls, and generated Pages
  support files.
- Release generation changes only the declared publication-state strings.
- The live Fastmail page and response headers were preserved outside the
  repository before migration work began.
- GitHub Actions workflow run `35322447860` completed successfully.
- The staged GitHub Pages origin returned HTTP 200 with GitHub's HTTPS and HSTS
  headers. Its HTML matched the local release SHA-256
  `232b741bbfecf2622c13ee644f1e303df741fff7a70c5a60122b74a26bf770fd`.
- A browser load at 1440 × 1000 showed the approved headline, all three header
  controls, the embedded Cascadia Mono wordmark, the publication footer,
  `index,follow`, and no horizontal document overflow.

The web-only Fastmail DNS change was saved on 2026-09-18. Google Public DNS and
Cloudflare DNS both returned GitHub's four apex addresses and the explicit
`www` CNAME. The apex MX records still returned Fastmail's two mail servers,
and Fastmail reported that the domain remained correctly configured to send
and receive mail. Public DNS also continued to return Fastmail's nameservers,
SPF, DMARC, and four DKIM records. GitHub's domain health check recognized both
names as valid and served by Pages. A direct request to GitHub's edge returned
the approved release with the expected SHA-256 value. GitHub's custom-domain
TLS certificate and post-cutover browser behavior remain to be verified after
certificate issuance.

- 13 automated tests passed for this site: generated structure, local links/fragments, feed/sitemap parsing, archive contents, missing/exact/stale release approval, unsafe/duplicate routes, unsafe external links, missing internal targets, overwrite refusal, HTML escaping/graph consistency, and private-repository address exclusion.
- Eleven pages built successfully in preview mode.
- Twenty-two in-memory Chromium renders (11 pages at 1280px and 390px) had no horizontal document overflow. Homepage screenshots were visually inspected. This used generated HTML plus its stylesheet; it was **not** HTTP navigation or a deployed-site test.
- Companion No One Noticed build: nine pages, 13 tests, and 18 analogous renders. A dark-mode fragment screenshot was also produced.
- Total across the two candidates: 26 passing automated tests and 40 desktop/mobile layout checks.

## Not established

No completed public-domain HTTPS result, external-link availability, full
keyboard/screen-reader audit, independent code review, actual author approval
of fragments, or independent preservation copy is established by these
checks. Automated address scanning is a limited guard, not a complete
content-privacy review.

Remote repository verification should compare the committed blobs with the tested source, not assume that a successful write means byte parity. Keep this receipt paired with the source version being reviewed.
