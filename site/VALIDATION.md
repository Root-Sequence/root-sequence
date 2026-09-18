# Local validation — 2026-09-16

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
