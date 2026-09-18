# Local validation — 2026-09-16

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

Live GitHub Pages delivery, DNS propagation, the GitHub TLS certificate, and
post-cutover browser behavior remain to be verified during deployment.

- 13 automated tests passed for this site: generated structure, local links/fragments, feed/sitemap parsing, archive contents, missing/exact/stale release approval, unsafe/duplicate routes, unsafe external links, missing internal targets, overwrite refusal, HTML escaping/graph consistency, and private-repository address exclusion.
- Eleven pages built successfully in preview mode.
- Twenty-two in-memory Chromium renders (11 pages at 1280px and 390px) had no horizontal document overflow. Homepage screenshots were visually inspected. This used generated HTML plus its stylesheet; it was **not** HTTP navigation or a deployed-site test.
- Companion No One Noticed build: nine pages, 13 tests, and 18 analogous renders. A dark-mode fragment screenshot was also produced.
- Total across the two candidates: 26 passing automated tests and 40 desktop/mobile layout checks.

## Not established

No live domain deployment, HTTPS result, external-link availability, full keyboard/screen-reader audit, independent code review, actual author approval of fragments, or independent preservation copy is established by these checks. Automated address scanning is a limited guard, not a complete content-privacy review.

Remote repository verification should compare the committed blobs with the tested source, not assume that a successful write means byte parity. Keep this receipt paired with the source version being reviewed.
