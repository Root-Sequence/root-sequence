# Root Sequence website

This directory is the canonical source for `rootsequence.systems`.

The current [`index.html`](index.html) is the **approved October 19, 2026 professional refresh** of the existing single-page public seed. Rae explicitly approved website publication after the supported page pass. The page introduces the independent interdisciplinary initiative, explains research/evidence and AI assistance, and retains its exploratory character and the linked work’s review limits.

The opening separates the mission from reading routes. About explains the initiative’s focus and connects research with projects, followed by the accepted invitation to take part. The founder credit stays in Credits and reuse; the AI disclosure introduces Rae’s role where the name first appears. About, research, and footer notes share one native expandable-section style.

All six research descriptions, seven related-project descriptions, Take part, four footer passages, and seven project-panel refinements are applied. The Wiki panel keeps its approved description and website action without the repeated extra paragraph. The [latest copy record](COPY-REVIEW.md#wiki-panel-and-full-page-review-october-18-2026-pacific) and [validation](VALIDATION.md#wiki-panel-and-full-page-review-2026-10-18-pacific) describe the supported full-page pass and its limits. Earlier passage approvals remain in COPY-REVIEW.md. The companion organization profile remains under draft review for consistency, particularly its OS-only Computing summary. Later public/private Wiki reconciliation remains queued; no Wiki content has been audited or transferred here.

The candidate uses one dark palette, including without JavaScript. The theme selector and its startup script are removed. Larger text, one background color, reduced motion, and in-page navigation settings remain available. System high-contrast styles and black-on-white print output are retained. Saved theme choices from an earlier candidate are ignored; other reading choices keep their existing storage key.

[`approval.json`](approval.json) identifies this exact page/publisher digest and Rae’s publication approval. Any later source change requires a matching approval record. The [canonical refresh checklist](https://github.com/Root-Sequence/root-sequence/blob/docs/professional-refresh-phase-1-2026-10-17/ROADMAP.md) remains on the review branch with the separate documentation and portfolio work.

The page is one self-contained file with its styles, scripts, favicon, and
Cascadia Mono wordmark font embedded. It makes no runtime requests for fonts,
images, analytics, translation, or previews.

## Files

- `index.html`: approved canonical editorial source; preview labels are converted by the release builder.
- `approval.json`: exact source/preview hashes and Rae’s approval for this edition.
- `build.py`: offline publisher. Preview output preserves `index.html` exactly;
  release output changes only preview/publication-state labels.
- `test_site.py`: checks exact approval and rejection of historical/stale approval, and validates links, fragments, embedded assets, Content Security Policy hashes, English-only setup, and required controls and copy.
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

This review does not change hosting, DNS, or mail. Historical migration steps are recorded in [DEPLOYMENT.md](DEPLOYMENT.md); current DNS and provider behavior must be checked before a future publication change.
