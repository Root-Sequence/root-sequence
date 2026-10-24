# Root Sequence website

This directory is the canonical source for `rootsequence.systems`.

The current [`index.html`](index.html) is the **approved October 19, 2026 professional refresh** of the existing single-page public seed. Rae explicitly approved website publication after the supported page pass. The page introduces the independent interdisciplinary initiative, explains research/evidence and AI assistance, and retains its exploratory character and the linked work’s review limits.

The opening separates the mission from reading routes. About explains the initiative’s focus and connects research with projects, followed by the accepted invitation to take part. The founder credit stays in Credits and reuse; the AI disclosure introduces Rae’s role where the name first appears. About, research, and footer notes share one native expandable-section style.

All six research descriptions, seven related-project descriptions, Take part, four footer passages, and seven project-panel refinements are applied. The Wiki panel keeps its approved description and website action without the repeated extra paragraph. The [latest copy record](COPY-REVIEW.md#wiki-panel-and-full-page-review-october-18-2026-pacific) and [validation](VALIDATION.md#wiki-panel-and-full-page-review-2026-10-18-pacific) describe the supported full-page pass and its limits. Earlier passage approvals remain in COPY-REVIEW.md. The companion organization profile was published on October 23. Public/private Wiki reconciliation remains queued separately.

The candidate uses one dark palette, including without JavaScript. The theme selector and its startup script are removed. Larger text, one background color, reduced motion, and in-page navigation settings remain available. System high-contrast styles and black-on-white print output are retained. Saved theme choices from an earlier candidate are ignored; other reading choices keep their existing storage key.

[`approval.json`](approval.json) identifies the exact homepage/publisher digest and Rae’s publication approval. Any later change to those sources requires a matching approval record. The [canonical refresh checklist](../ROADMAP.md) records the separate documentation, research and portfolio work.

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

## Proposed research route: 24 October 2026

The proposed address is **`https://rootsequence.systems/stonedage/`**. It serves the existing [Stoned Age inquiry](../research/the-stoned-age/README.md), keeping its paper, illustrated essay, booklet, talk and evidence notes together. The research directory remains the substantive source. The homepage copy and its original approval are unchanged.

[`build_research.py`](build_research.py) packages the approved homepage with an explicit list of research reading files. It adds a return link to Root Sequence, canonical addresses and publication-state metadata to the generated research pages. Markdown source links point to GitHub; the PDFs and downloadable evidence records remain local to the research route. Source tools, editable content files, unrelated research and private material are not copied into the hosting artifact. The reading editions retain their AI-assisted draft and unfinished-review wording.

Preview the combined artifact in a fresh directory:

```sh
python3 site/test_site.py
python3 site/test_research_site.py
python3 site/build_research.py --output /tmp/root-sequence-with-stonedage
python3 -m http.server 8000 --directory /tmp/root-sequence-with-stonedage
```

Open `/stonedage/` on that local server. This does not publish it. The proposed Pages workflow uses the combined builder and also watches this inquiry for changes.

`stonedage-approval.json` is a **pending** record for the separate hosting decision. Release builds require both the existing homepage approval and an exact research-source approval. The research digest includes the route publisher, workflow, exported files and named source records. No approval has been recorded for this route. Once approved, `python3 site/build_research.py --release --output <fresh-directory>` builds the combined publication artifact. Existing deployed content is unaffected by preparing this draft.
