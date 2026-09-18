# Root Sequence website

This directory is the canonical source for `rootsequence.systems`.

The current site is the single-page public seed approved by Rae Lovejoy on
2026-09-18. [`index.html`](index.html) is the exact approved preview: one
self-contained file with its styles, scripts, favicon, and Cascadia Mono
wordmark font embedded. It makes no runtime requests for fonts, images,
analytics, translation, or previews.

## Files

- `index.html`: exact approved preview and canonical editorial source.
- `approval.json`: approval tied to the exact current source digest.
- `build.py`: offline publisher. Preview output preserves `index.html` exactly;
  release output changes only preview/publication-state labels.
- `test_site.py`: checks the approved-file hash, release gate, links, fragments,
  embedded assets, Content Security Policy hashes, English-only setup, and
  required controls and copy.
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

Build the approved publication artifact with:

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

Fastmail still serves the live website until the DNS cutover is deliberately
completed. Its mail records must remain unchanged. See [DEPLOYMENT.md](DEPLOYMENT.md).
