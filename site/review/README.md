# Website review: introduction, credit, and accessibility

This is a review proposal, not a deployment or a new publishing system. It keeps the established website source and manuscript unchanged while Rae considers the direction. After review, integrate accepted changes into the existing builder rather than maintaining two websites.

## Read the proposal

`edition.json` contains the selected routes and proposed page text. `theme.css` and `theme.js` provide the reading styles and System / Light / Dark controls. `build_review.py` builds the existing website in a temporary directory, then applies only the listed review changes. It exports only selected routes and rejects links to excluded pages. It never approves publication or changes story canon.

From this repository's root, run the review builder with `--output` set to a new directory outside the source tree. The result includes regular HTML pages and a self-contained review HTML file in the output's parent directory. No dependency installation is required for the builder. Without JavaScript, the single-file version shows all its pages in reading order; the ordinary pages and links remain usable.

The local review was generated from the last saved browser-review page map, associated with the base commit in `edition.json`. The earlier failed accessibility implementation was not retained in the active workspace. The new controls and styles were rebuilt here. Local rendering did not execute the canonical source builder because direct file transfer was unavailable; the default builder integration needs a repository checkout test before merging.

## Editorial direction

Introduce Root Sequence as a research project, with a short Started by Rae Lovejoy section on About. Describe collaboration as an intention and process, not evidence that shared governance is already operating. Do not change accounts, permissions, licensing, or decision authority by rewriting a biography.

Keep Rae Lovejoy's author credit on No One Noticed. Its review edition contains the premise, a fuller About page, setting notes, occasional project notes, site updates, and accessibility information. Unreviewed sample scenes stay in the private manuscript workspace, outside the selected routes, feeds, sitemap, and edition archive. No source scene is deleted.

The short biography uses project-relevant background only. It is proposed copy for Rae's review. No legal name, medical information, address, or personal history unrelated to the projects is included. Follow the parent AGENTS.md and its Rossmann editing reference. Do not invent a team, testimonials, a publication date, or manuscript readiness.

## Accessibility target and observed checks

Target: WCAG 2.2 Level AA. This is not a conformance claim or certification.

Local checks passed for 18 page routes at 320 and 1280 CSS pixels in both light and dark device modes. Static checks covered links, IDs, main headings, selected exports, archive contents, and file hashes. Theme controls have native radio semantics and labels, keyboard support, and 44-pixel label targets. Checked theme switching, device-scheme following, skip-link focus, single-file page-change focus, print styling, forced-colors emulation, reduced-motion emulation, and text-size/spacing changes. Colors were checked against 32 predefined pairs; the lowest calculated text contrast was 5.50:1. This is not a scan of every rendered color pair.

Limits: Chromium only; browser checks ran in memory. Native file navigation was blocked by the environment. Preference restoration used a storage test double; real cross-page browser persistence remains a deployment test. No axe scan, external HTML validator, full zoom audit, screen-reader testing, real-device testing, user comprehension study, or live-domain validation was performed. The older PDFs are not part of this accessibility review.

## Standards references

- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- Evaluation methods and their limits: https://www.w3.org/WAI/test-evaluate/
- Cognitive accessibility guidance: https://www.w3.org/TR/coga-usable/

Use semantic HTML and native controls first. Keep actual content readable without JavaScript. Continue to distinguish sources, authorship, draft status, and permission. Before deployment, integrate the accepted controls into the existing build, update its script-related claims and tests, retain exact-source release approval, and repeat checks on the real host.
