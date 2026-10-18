# Root Sequence website

This directory is the canonical source for `rootsequence.systems`.

The current [`index.html`](index.html) is the **unapproved October 18, 2026 professional-refresh candidate**, extending the existing single-page public seed. It adds an independent interdisciplinary mission, a visible methods/evidence/AI-use disclosure, and clearer research status labels. The headline, green palette, wordmark, reading controls, section order, and existing URLs remain in place.

The opening separates the mission from reading routes. Rae accepted the About explanation of the initiative’s focus and requested the invitation that follows it. The founder credit is in Credits and reuse. The research header groups its introduction with one methods disclosure, and the wider repository link follows the selected entries. Broader presentation review remains open; see the [copy record](COPY-REVIEW.md#accepted-about-explanation-and-invitation-october-17-2026).

The current [About layout](COPY-REVIEW.md#about-context-and-consistent-disclosures-october-17-2026) keeps the research-to-projects connection visible alongside the accepted introduction and invitation. The name and contribution background are optional. About, research, and page notes share one native expandable-section style; navigation menus keep their separate controls. The full repair example and detailed methods disclosure retain their existing sections.

Rae has accepted the [contextual name introduction and Coherent World description](COPY-REVIEW.md#accepted-name-context-and-coherent-world-description-october-17-2026-pacific). The AI disclosure explains Rae’s role at the first name reference; the founder credit and profile link stay in Credits and reuse. Related-project descriptions are being reviewed individually: [No One Noticed is now also accepted and applied](COPY-REVIEW.md#accepted-no-one-noticed-description-october-17-2026-pacific), and the [revised Coherent Computing description is applied](COPY-REVIEW.md#accepted-revised-coherent-computing-description-october-17-2026-pacific). [Community Infrastructure is also applied, with the requested concise openings for World and Computing](COPY-REVIEW.md#accepted-community-infrastructure-and-concise-openings-october-17-2026-pacific). [Being Human(e) is applied with “In development” status and an explicitly provisional panel note](COPY-REVIEW.md#being-humane-passage-and-provisional-status-october-17-2026-pacific). [Museum of Ordinary Life is applied, retaining its independent status and fiction/reuse permission explanation](COPY-REVIEW.md#accepted-museum-of-ordinary-life-description-october-17-2026-pacific). [Root Sequence Wiki is applied, completing all 7/7 related-project descriptions](COPY-REVIEW.md#accepted-wiki-description-and-next-review-october-17-2026-pacific). [Take part is approved and applied](COPY-REVIEW.md#accepted-take-part-wording-october-17-2026-pacific), retaining the existing public GitHub routes and explanatory panels. [Sources and page history is approved and applied](COPY-REVIEW.md#accepted-sources-and-page-history-october-18-2026-pacific), with inline source links and corrected draft-history wording. [Accessibility and reading choices is approved and applied](COPY-REVIEW.md#accepted-accessibility-and-reading-choices-october-18-2026-pacific), retaining the explicit need for full accessibility review. [Privacy and this preview is accepted and applied](COPY-REVIEW.md#accepted-privacy-and-this-preview-october-18-2026-pacific), distinguishing page behavior from unverified hosting policies. [Credits and reuse is accepted and applied](COPY-REVIEW.md#accepted-credits-and-reuse-october-18-2026-pacific), completing all four footer passages. [The Coherent World panel is refined](COPY-REVIEW.md#accepted-coherent-world-panel-october-18-2026-pacific), retaining its approved description and a shorter access note without the repeated extra paragraph. [The No One Noticed panel is also refined](COPY-REVIEW.md#accepted-no-one-noticed-panel-october-18-2026-pacific), retaining its science-fiction description and a shorter manuscript-status note. Coherent Computing panel context is next, followed by remaining panels and a full-page pass. The canonical roadmap separately queues later Wiki reconciliation; it has not been audited or transferred as part of this site edit.

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
