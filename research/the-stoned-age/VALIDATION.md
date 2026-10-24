# Validation record

14 October 2026 · v0.1.1 · public draft review package.

- HTML/SVG/PDF build completed. Booklet: 16 pages; talk: 12 pages. Both PDFs contain extractable text. Layout builder rejects booklet text overflow.
- Rendered every PDF page to contact sheets and visually inspected the booklet and slides. No visible clipping or overlap found.
- Browser preview opened successfully; project navigation reached the illustrated essay and exposed working source anchors. Desktop layout inspected. Mobile-device, screen-reader and full keyboard usability testing remain unperformed.
- 158 local HTML links, assets and fragments checked with no missing targets (see revision check below). This does not establish every external destination is permanently accessible.
- All 16 sources now have a claim-focused appraisal. Main-text access expanded through Europe PMC and author repositories; explicit gaps remain, including S01 full text and supplements. Crossref returned 13 of 14 DOI records in this pass. No comprehensive retraction clearance or independent scholarly review is claimed.
- Repository website suite: 11 tests passed. Idea Trail graph valid and generated index current. PyYAML was installed only into a temporary task-local validation directory to run that check.
- Reader documentation checker: 15 errors on untouched base and exactly the same output after the addition. These pre-existing failures were not repaired by this scoped work.
- Git whitespace check passed. Repository patch includes only the new research area and its nearest research-index entry.
- Public draft PR #45 opened with user authorization; evidence revision added to the same branch. No merge or deployment.

Technical validation checks files and presentation. It does not validate historical interpretations, scientific conclusions or community representation.

## Revision checks

HTML and PDFs rebuilt after evidence corrections. Booklet and talk page counts remain 16 and 12. Source registry has 16 unique IDs; claim ledger has 19 unique claims. Updated PDF pages visually rechecked; full keyboard, screen-reader and mobile-device checks remain pending.

## Review checkpoint: 24 October 2026

Working edition v0.1.2, reconciled with repository main through merged PR #44. The earlier 15 reader-check errors describe the October 14 baseline; they are absent from the current main and this candidate.

- Reader documentation passed for 256 Markdown files. The Idea Trail graph is valid and its generated index is current. All 11 website tests passed; this package does not alter the website source or publication approval.
- All 165 local links, assets and fragments across seven HTML pages resolve. The register retains 16 unique sources and the ledger 19 unique claims. The placebo comparison is explicit in all four maintained editions and their reader output; S15 links pin the reviewed 2023 version.
- Two consecutive builds produced identical bytes for all 20 generated HTML, CSS, SVG and PDF files. Both PDFs contain extractable text. All 16 booklet pages and 12 talk pages were rendered and visually inspected after the changes, with no visible clipping or overlap found. The cover preview was refreshed from the current PDF.
- In the local browser, the skip link navigated to the main-content fragment. Evidence notes were reachable through edition navigation. The appraisal and talk pages fit a 390-pixel viewport without horizontal scrolling, and the talk's speaker-note disclosure opened with the keyboard and exposed the corrected comparison. The normal desktop viewport was restored. This is a scoped browser check, not a full keyboard, screen-reader or physical-device accessibility audit.
- Selected source passages were rechecked at the depths recorded in [appraisal.md](research/appraisal.md#review-follow-up-24-october-2026). The original scholarly and cultural review gates remain open. This pass did not repeat the full source appraisal or independently reproduce the studies.

This remains a repository draft for author review. No merge, website deployment, clinical guidance or cultural endorsement follows from these checks.
