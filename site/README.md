# Root Sequence website

This directory is the canonical source for `rootsequence.systems`.

The current [`index.html`](index.html) is the **unapproved October 17, 2026 professional-refresh candidate**, extending the existing single-page public seed. It adds an independent interdisciplinary mission, a visible methods/evidence/AI-use disclosure, and clearer research status labels. The headline, green palette, wordmark, reading controls, section order, and existing URLs remain in place.

The opening separates the mission from reading routes. Rae accepted the About explanation of the initiative’s focus and requested the invitation that follows it. The founder credit is in Credits and reuse. The research header groups its introduction with one methods disclosure, and the wider repository link follows the selected entries. Broader presentation review remains open; see the [copy record](COPY-REVIEW.md#accepted-about-explanation-and-invitation-october-17-2026).

The latest [About layout proposal](COPY-REVIEW.md#shorter-about-layout-proposal-october-17-2026) keeps the accepted introduction visible and puts background in two native expandable sections. The following repair example and the research section’s methods disclosure supply the detail previously repeated in About.

The candidate uses one dark palette, including without JavaScript. The theme selector and its startup script are removed. Larger text, one background color, reduced motion, and in-page navigation settings remain available. System high-contrast styles and black-on-white print output are retained. Saved theme choices from an earlier candidate are ignored; other reading choices keep their existing storage key.

[`approval.json`](approval.json) records the earlier September 25 edition. It is unchanged and does not approve this candidate. `build.py --release` must reject the current digest until Rae separately approves the final source. See [`COPY-REVIEW.md`](COPY-REVIEW.md) and the canonical [refresh checklist](../ROADMAP.md).

The page is one self-contained file with its styles, scripts, favicon, and
Cascadia Mono wordmark font embedded. It makes no runtime requests for fonts,
images, analytics, translation, or previews.

## Files

- `index.html`: current unapproved review candidate and canonical editorial source.
- `approval.json`: approval record for the last approved edition; it intentionally does not match the current candidate.
- `build.py`: offline publisher. Preview output preserves `index.html` exactly;
  release output changes only preview/publication-state labels.
- `test_site.py`: checks that the candidate differs from the last approved preview, preserves the release gate, and validates links, fragments, embedded assets, Content Security Policy hashes, English-only setup, and required controls and copy.
- `DEPLOYMENT.md`: GitHub Pages and Fastmail DNS migration runbook.
- `legacy-public-seed-v0.1/`: clearly labelled source from the superseded
  11-page candidate.

Supporting records and instructions:

- [`AGENTS.md`](AGENTS.md): writing, page-structure, and review instructions.
- [`COPY-REVIEW.md`](COPY-REVIEW.md): approval and editorial review record.
- [`VALIDATION.md`](VALIDATION.md): validation history and limits.
- [`PLACEMENT.md`](PLACEMENT.md): repository placement and publication boundary.

The research repository remains the canonical home of the full arguments. The
Root Sequence Wiki remains the shared project reference. This site introduces
and routes into that work rather than copying it.

## Build and inspect

From the repository root, with Python 3.10 or later:

```sh
python site/test_site.py
python site/build.py --output /tmp/root-sequence-preview
python -m http.server 8000 --directory /tmp/root-sequence-preview
```

The preview page is byte-for-byte identical to `site/index.html` and remains
`noindex`. Choose a fresh empty output directory; the builder will not delete or
replace an earlier build.

After separate exact-source approval, build the publication artifact with:

```sh
python site/build.py --release --output /tmp/root-sequence-release
```

The release changes `noindex` to `index,follow` and replaces only statements
that describe a local, unpublished preview. It also creates `robots.txt`,
`sitemap.xml`, `.nojekyll`, `CNAME`, and a build manifest. Any change to
`build.py` or `index.html` invalidates the approval until the new digest is
reviewed and recorded.

## Hosting

`.github/workflows/pages.yml` tests and builds the approved release before it
can deploy to GitHub Pages. Deploy only that generated directory, never the
repository or the historical source directory.

This review does not change hosting, DNS, or mail. Historical migration steps are recorded in [DEPLOYMENT.md](DEPLOYMENT.md); current DNS and provider behavior must be checked before a future publication change.
