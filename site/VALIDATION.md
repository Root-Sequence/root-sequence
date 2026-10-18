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

The approval established permission to publish this exact source. GitHub Actions
run `36181565309` then completed successfully: all 11 tests passed, the
approved source/preview digests matched, the release build succeeded, the Pages
artifact uploaded, and GitHub reported the deployment successful for commit
`e795e2e19e38f0a613cc15d25d680b25467b7475`.

This is deployment evidence from GitHub Pages. An independent browser fetch of
the custom domain was not completed in this pass.


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


## Professional-refresh candidate: 2026-10-17

- All 11 offline site checks pass, including page fragments, duplicate IDs, self-contained resources, inline-script CSP hashes, English source edition, controls, exact preview output, and refusal to overwrite a nonempty output directory.
- Historical `approval.json` is unchanged. A direct release build is rejected for the current digest; test-only approval fixtures do not approve real source.
- Browser inspection covered the introduction and research disclosure at a wide desktop viewport and at 390 × 844 CSS pixels. No horizontal overflow was measured at either width. Existing green palette, embedded wordmark, and section order remain.
- The new native disclosure opens with Enter and can be closed from the keyboard. Section navigation reaches the intended heading. The existing Coherent Computing project panel retains its no-release wording; Escape closes it and returns focus to its trigger.
- The Idea Trail graph/index check passes using the existing isolated validation environment's PyYAML package. No repository dependency or graph changes were needed.
- Reader-document check reports the same 15 pre-existing errors as untouched `main`: one broken relative link and fourteen notes without inbound navigation. No new errors from the refresh. This is not a clean whole-repository result.
- Changed public GitHub file destinations and local Markdown links were checked. No private-project source URLs or content were added to the site.

This is selected browser and structural inspection, not a full WCAG audit, screen-reader assessment, real-device test, independent research review, or live-deployment verification. The preview is a local review artifact. Progress and remaining decisions live in [ROADMAP.md](../ROADMAP.md).

## Approved accessibility and contribution copy: 2026-10-17

Applied the exact approved short site copy and fuller README copy. The existing method, evidence, and working-paper limits remain alongside them; the organization profile uses the same approved short paragraphs. The main README routes to the fuller explanation in the research README.

- All 11 site tests and the Idea Trail graph/index check pass.
- HTML, English translation data, and organization-profile paragraphs match the approved site wording exactly. The research README contains the approved full paragraphs exactly.
- The native disclosure opens with Enter. Updated text was inspected at desktop width and 390 × 844 CSS pixels; no horizontal overflow was measured. Viewport overrides were reset after inspection.
- Preview output remains identical to canonical HTML, and a direct release build is rejected against unchanged `approval.json`. The Pages workflow is unchanged.
- Reader-document check remains at the same 15 pre-existing failures. No new errors were introduced, and whitespace checks pass.

This records selected browser/structural checks and passage-level approval. Full-source publication approval, independent research evaluation, and complete accessibility testing remain separate.

## Approved research-method introduction: 2026-10-17

Applied the two approved paragraphs verbatim to the existing site disclosure, research README, and organization profile. The detailed research-method source and unapproved evidence wording are unchanged.

All 11 site checks pass, including the release-approval gate and script hashes. Exact wording was checked across HTML, translation data, and README/profile text. Desktop and 390 × 844 browser inspection confirmed readable wrapping, native disclosure keyboard activation, and no measured horizontal overflow; viewport overrides were reset. Reader-document failures remain the same 15 pre-existing issues. Whitespace checks pass. This is selected structural/browser verification, not method validation or publication approval.

## Approved evidence wording: 2026-10-17

Applied the two approved evidence paragraphs verbatim to the existing site disclosure, research README, and organization profile. Nearby README introductions now use less repetitive prose. The previously approved mission, method, and accessibility/contribution passages remain verbatim.

All 11 site checks pass, and the Idea Trail index remains current. HTML and English translation data match the approved evidence wording. Desktop and 390 × 844 browser inspection showed readable wrapping and no measured horizontal overflow. The native disclosure opens and closes with Enter; viewport overrides were reset. The preview matches source HTML exactly, and the current source still fails the historical release-approval gate as intended. Reader-document checking reports the same 15 pre-existing errors. Whitespace checks pass in both repositories.

These checks cover the changed presentation and source structure. They do not establish scientific validity, a complete accessibility audit, or publication approval. The exact-source approval record and Pages workflow remain unchanged.

## Approved homepage research-method entry: 2026-10-17

Applied the approved title, description, and development-status sentence from writing block `92184` verbatim to the existing method entry and English translation data. Updated the existing required-copy assertion to expect the approved heading. The destination remains the canonical `research/method.md`.

All 11 site checks pass after that assertion update. Exact wording and translation parity were checked, and the preview matches source HTML byte for byte. The entry was inspected at desktop width and 390 × 844 CSS pixels with no measured horizontal overflow; viewport overrides were reset. The publication approval record and Pages workflow are unchanged, and the current candidate still fails the exact-source release gate as intended.

This pass changes one homepage entry and its review records. It does not alter the detailed research method, the paper, or other research descriptions. Browser inspection is limited to the changed entry; no new whole-repository documentation or scientific-validation result is claimed.

## Approved homepage working-paper entry: 2026-10-17

Applied the description and review-status sentence from writing block `68425` verbatim in the existing paper entry and English translation data. Its title and source destination remain unchanged; the existing source-details panel uses the same translated text.

All 11 site checks pass. Exact text and translation parity were checked, and preview HTML matches source byte for byte. Desktop and 390 × 844 browser inspection found readable wrapping and no measured horizontal overflow; viewport overrides were reset. The manuscript, paper-level review records, historical publication approval, and Pages workflow are unchanged. The current candidate still fails the exact-source release gate as intended.

These are presentation and structural checks for the changed entry, not scientific validation, a new whole-repository documentation audit, or publication approval.

## Approved homepage adaptive-continuity entry: 2026-10-17

Applied the description and status sentence from writing block `32716` verbatim in HTML and English translation data. The title and canonical source destination remain unchanged.

All 11 site checks pass. Exact text, translation parity, and byte-identical preview output were verified. Desktop and 390 × 844 browser inspection showed readable wrapping and no measured horizontal overflow; viewport overrides were reset. The underlying concept and lineage note, other research descriptions, publication approval, and Pages workflow are unchanged. The candidate still fails the exact-source release gate as intended.

These checks concern the changed presentation and structure. They do not establish scientific validity, complete accessibility, a new whole-repository audit, or publication approval.

## Approved homepage knowledge-routing entry: 2026-10-17

Applied the description and status sentence from writing block `74863` verbatim in HTML and English translation data. The title and canonical source destination remain unchanged.

All 11 site checks pass. Exact wording, translation parity, and byte-identical preview output were verified. Desktop and 390 × 844 browser inspection found readable wrapping and no measured horizontal overflow; viewport overrides were reset. The underlying concept, other research entries, historical publication approval, and Pages workflow remain unchanged. The current candidate still fails the exact-source release gate as intended.

These are checks of the changed presentation and structure, not a measured discovery result, complete accessibility audit, or publication approval.

## Approved homepage Legible Systems entry: 2026-10-17

Applied the description and status sentence from writing block `96184` verbatim in HTML and English translation data. The title and canonical source destination remain unchanged.

All 11 site checks pass. Exact wording, translation parity, and byte-identical preview output were verified. Desktop and 390 × 844 browser inspection found readable wrapping and no measured horizontal overflow; viewport overrides were reset. The underlying design principle, other research entries, historical publication approval, and Pages workflow are unchanged. The candidate still fails the exact-source release gate as intended.

These are presentation and structural checks, not usability evaluation, a complete accessibility audit, or publication approval.

## Completed homepage-description review: 2026-10-17

Applied the Reading Trails description and status sentence from writing block `50297` verbatim in HTML and English translation data. All six entries now match their individually approved wording. Titles and canonical source destinations are preserved except for the separately approved research-method title.

All 11 site checks and the Idea Trail index check pass. Exact wording, translation parity, and byte-identical preview output were checked. Reading Trails was inspected at desktop width and 390 × 844 CSS pixels with no measured horizontal overflow; viewport overrides were reset. The broader reader-document check still reports the same 15 pre-existing errors.

Tree-only compatibility checks against current PR heads found no textual conflict between the root refresh and each of #42–#45 individually. Organization #9 and #10 conflict in `profile/README.md`; the proposed resolution is recorded in the [audit](../AUDIT.md#refresh-compatibility-review-2026-10-17). No older PR was modified and no branch was merged by those calculations.

The historical publication approval and Pages workflow remain unchanged. The current candidate still fails the exact-source release gate. These results do not establish scientific validity, complete accessibility, or publication approval.

## Proposed opening layout: 2026-10-17

Rae requested clearer separation of the founder credit from reading instructions and a less text-heavy opening. The proposed revision moves the credit into About and the former opening explanation under “How the research works,” replacing overlapping prose. A ruled strip links to the everyday example and selected research. It uses two columns on wide screens and stacked rows below 35rem.

All 11 site checks pass on this source, including fragments, self-contained assets, unchanged executable-script CSP hashes, and the deliberately blocked publication gate. The preview matches source byte for byte. The full research section and both executable scripts match the preceding candidate exactly; previously approved research descriptions and disclosure text are preserved.

The opening and relocated About credit were inspected in the browser at desktop width and 390 × 844 CSS pixels. No horizontal overflow was measured. Both new reading routes were activated by keyboard and moved focus to their destination headings (`example-title` and `research-title`). The temporary viewport override was reset. These are selected presentation and interaction checks, not a full accessibility audit. No new whole-repository documentation check or research-validation result is claimed.

Source digest: `6e9ee3e687fdfe00cdbec648c5d7fefdbaf9cdcd45ebdba867eaadd92b7fa1df`.
Preview HTML SHA-256: `232d492ec94b0b4f8c9954e8a4137037354952ac73082a49c26fb275d8827231`.

The proposed layout awaits Rae’s review (ROADMAP P1-08). `approval.json` and the Pages workflow are unchanged. No merge, deployment, or live-settings change is included.

## About, research, and dark appearance refinement: 2026-10-17

The separate founder credit is replaced by an integrated About introduction. The research header has one native disclosure and a shorter introduction; the wider repository route follows the selected entries. The six entries and complete methods/evidence/AI-use disclosure were compared byte for byte with the preceding source and are unchanged.

All 11 site checks pass. The existing script-hash check now expects one executable script, following removal of the theme bootstrap; the remaining script’s CSP hash matches its new bytes. The required-copy check follows the revised About introduction. Source and preview are byte-identical; fragments and generated files pass. `approval.json` remains historical and the candidate fails the release gate as intended.

Desktop and 390 × 844 browser inspection found no horizontal overflow. The methods disclosure opens and closes by keyboard. Larger text and one-background mode were exercised at phone width without overflow, then reset. The reading menu retains four controls and has no theme selector. Viewport overrides were reset.

With browser scripts disabled and a light OS preference emulated, the page still rendered dark (`color-scheme: dark`, body RGB 11/36/27). Print emulation rendered the About section white with black text. Both emulation overrides and script disabling were cleared afterward. Existing forced-colors styles remain in the source; full system high-contrast and screen-reader audits were not performed.

Source digest: `1a0a5712569036d90c30dc3197fa2d5a8ba07340b00c2bb259c6b1134cdcfabd`.
Preview HTML SHA-256: `4403bb72e5975b137bf64260a50f1f071caa823d486ea642d2d831b92e507378`.

These are selected presentation and behavior checks. The revised wording and appearance await Rae’s review under ROADMAP P1-08; they are not publication approval or research validation.

## Accepted About wording and invitation: 2026-10-17

Applied the accepted two-sentence explanation from writing block `86204` verbatim, with the requested invitation in a separate paragraph immediately afterward. The founder credit and existing GitHub link now sit in Credits and reuse. Corrected the no-JavaScript notice’s outdated claim that colors follow the device; it now describes the dark palette accurately.

All 11 site checks pass. The existing required-copy assertion follows the accepted About lead. The entire research section and executable script were compared with the preceding source and are unchanged; CSP and fragments pass. Preview output matches source byte for byte. The historical approval record and builder are unchanged; the candidate remains blocked from release as intended.

Desktop and 390 × 844 browser inspection found readable wrapping with no horizontal overflow. The founder credit and link were checked in the native Credits and reuse disclosure. The temporary viewport override was reset. No new whole-repository audit, complete accessibility result, or research-validation result is claimed.

Source digest: `61272a6b01d96cd3f1dc10c4610dcbd9b4ea35c33262c7e903e955a81be68e7c`.
Preview HTML SHA-256: `d084ad7f4255c30f8943690b163f264f6df774d264c09c8c2a9b45334fbb3248`.

The explanation and invitation have passage approval. Broader layout review (ROADMAP P1-08) and exact-source publication approval remain separate.

## Shorter About layout proposal: 2026-10-17

The accepted About lead and invitation remain verbatim. Repeated topic/example/method framing is removed from this section. The existing name explanation and project background now sit in two native expandable sections. A route to the research and methods replaces About’s repeated process explanation; the full repair example still follows About. No canonical research document is changed.

All 11 site checks pass without changing the tests. The complete research section and executable script match the preceding source. CSP hashes, fragments, generated support files, and the blocked release gate pass; preview output matches source byte for byte. Active translation keys were checked against the English table.

Both About sections were exercised by keyboard. A Coherent World link inside the second section opens its existing context dialog; Escape closes it and returns focus to the trigger. With page scripts disabled, the name section still opens by keyboard. Script execution was restored afterward. Desktop and 390 × 844 inspection found no horizontal overflow, and the temporary viewport override was reset.

Source digest: `7465a292deee576b9d4f86495f3207d986acafeb6a1a94e3387cbed2dc3247e9`.
Preview HTML SHA-256: `f93c1620b93b06d2e8cb2569b5a7889eeccb5cfa0c930b82c909c9867c2b76cf`.

This is selected layout and interaction validation, not a complete accessibility audit or approval of the proposed grouping. The source remains in draft; historical publication approval is unchanged.

## About context and shared disclosures: 2026-10-17

The existing research-to-projects paragraph is visible again, adding context beyond the opening’s mission. Accepted About wording is unchanged. One native `content-disclosure` component now serves both optional About sections, the research disclosure, and four page-note sections. Competing style rules are removed; summary labels remain translated text, with decorative indicators hidden from assistive technology.

All 11 site checks pass without test changes. Approved About passages, the research entry list, methods/evidence/AI-use disclosure body, and executable script were compared with the previous source and are unchanged. Active translation keys, fragments, and preview/source byte parity pass. The historical approval and builder are unchanged; the release gate remains blocked.

Keyboard expansion was checked in About, research, and Credits and reuse; indicators switch to minus when open. Research and footer summaries have matching padding, and the research box background is removed. The visible Coherent World link opens its existing dialog. With scripts disabled, the name explanation still opens by keyboard. Script execution was restored. Desktop and 390 × 844 inspection, including larger text on the narrow view, found no horizontal overflow. Reading preferences and viewport overrides were reset.

Source digest: `663a06b04b26b6899a7ac1a76491fc95259991e7e8a918d50519ffe40941e75c`.
Preview HTML SHA-256: `c6fbb506a90047d1e8b8e48e8882cfd8ee6651a18c466fb5ad5a6760e503e9ac`.

These are selected presentation and interaction checks, not a full accessibility audit. The replacement layout awaits review under ROADMAP P1-08; no publication approval is inferred.

## Contextual name and Coherent World passages: 2026-10-17 (Pacific)

Applied the approved passages from writing blocks `30857` and `69418` to HTML and English translation data. Only the first AI/accessibility paragraph and the Coherent World description change in the site source. The existing novel context link, private/speculative status, founder credit, six research entries, executable script, builder, and historical publication approval remain unchanged. No One Noticed copy remains pending review.

All 11 site checks pass without test changes, including fragment/CSP checks, source/preview byte parity, and the blocked exact-source release gate. Desktop (1575 pixels) and 390 × 844 browser inspection found readable wrapping without horizontal overflow. The novel link inside the revised Coherent World paragraph opens its existing dialog by keyboard; Escape closes it and returns focus to that link. The revised AI paragraph was inspected at both widths, and the native methods disclosure opened by keyboard. Temporary viewport settings were reset and normal desktop dimensions confirmed.

Source digest: `dfb4b828ca7857d764c3b4a71ce286029f62a26fc561dc56ae2d070101aa67bd`.
Preview HTML SHA-256: `503a7fa2094f05a73975f9c799f517197db778b187c4255500c0cc12987ae29b`.

These are selected copy/presentation checks, not a complete accessibility audit or research validation. No new whole-repository check is claimed by this entry. The source remains draft-only; historical approval and publication settings are unchanged.

## Accepted No One Noticed passage: 2026-10-17 (Pacific)

Applied writing block `83520` verbatim to HTML and English translation data. All 11 site checks pass without test changes, including fragment/CSP checks, source/preview parity, and the deliberately blocked release gate. The executable script, builder, historical approval, and other project descriptions are unchanged.

Browser inspection at desktop width (1575 pixels) and 390 × 844 found readable wrapping and no horizontal overflow. The novel’s existing details panel opens by keyboard and shows the same new description; Escape closes it and returns focus to its trigger. The normal desktop viewport was restored. The private Coherent Computing context was read to check current status for the next proposed passage; no private project is edited or creative/implementation material exported. No broader repository check was rerun for this copy-only update; the last recorded reader-document result remains 15 pre-existing errors.

Source digest: `05d97621178f3cb83d98f306387c5853f7466fcc9ea0888bed39af9e9e759166`.
Preview HTML SHA-256: `ec4be517e22eac8d1672e59ca6aaed327596db2cc6ef390510e9edcf117ce0e8`.

These checks concern the selected copy and interactions, not full accessibility, scientific validation, or release approval. The candidate remains a draft.

## Accepted revised Coherent Computing passage: 2026-10-17 (Pacific)

Applied the revised writing block `46179` verbatim to HTML and English translation data. All 11 site checks pass without test changes, including fragment/CSP checks, preview/source byte parity, and the deliberately blocked release gate. The executable script, builder, historical approval, other project descriptions, status labels, and existing panel limits are unchanged.

Desktop (1575 pixels) and 390 × 844 browser inspection found readable wrapping without horizontal overflow. The existing Coherent Computing details panel opens by keyboard and displays the same revised description; Escape closes it and returns focus. Normal desktop viewport settings were restored and confirmed. The Community Infrastructure context and README were read for the next proposed passage; neither private repository is edited or its implementation material exported. No broader repository check was rerun for this copy-only update; the last recorded reader-document result remains 15 pre-existing errors.

Source digest: `e87e85303a7b725b9f131cd6121179a1f073ace69f62ade329de1bdc291ad8c0`.
Preview HTML SHA-256: `e5b783fa1a85c73ecc7391cf34b774d33146831b0a3a028de43fc8ec10aa391f`.

These are selected copy and interaction checks, not a complete accessibility audit, implementation evidence, research validation, or website release approval. The candidate remains a draft.

## Community Infrastructure and concise openings: 2026-10-17 (Pacific)

Applied the accepted Community Infrastructure passage with the requested “Explores” opening. Removed the repeated name from the Coherent Computing and Coherent World openings, using “Explores” and “Brings.” HTML and English translation data agree; the existing novel link and status labels remain. All 11 site checks pass without test changes, including fragment/CSP checks, preview/source byte parity, and the intentionally blocked exact-source release gate. The executable script, builder and historical publication approval are unchanged.

Desktop (1575 pixels) and 390 × 844 browser inspection found no horizontal overflow. The Community Infrastructure details panel opens by keyboard and displays the same new description; Escape closes it and returns focus. Normal desktop dimensions were restored. No broader repository check was rerun for this copy-only update; the last reader-document result remains 15 pre-existing errors. No private-project changes or implementation claims are introduced.

Source digest: `3fe458f15b80d7a88d37e0a46539071596de9b9426655dfce675203d3f7ae482`.
Preview HTML SHA-256: `bb984f6a88d4974b08ed3efb7f37c83dd3360304e739e90ca2efdb2719c22868`.

These are selected copy/presentation checks, not a complete accessibility audit or publication approval.

## Being Human(e) description and provisional status: 2026-10-17 (Pacific)

Applied writing block `72841` verbatim in HTML and English translation data. Changed the label to “Practical field guide · In development” and replaced the unverified website-not-built note with the statement that observations are provisional and open to disagreement and revision. No private Atlas material or unverified external link is added. Other project descriptions, executable script, builder, and historical publication approval remain unchanged.

The first site run found one stale required-copy expectation for “Its public website has not been built yet.” That existing expectation now requires the new provisional-observations sentence instead. All 11 site tests then passed, including fragment/CSP checks, preview/source byte parity, and the intentionally blocked release gate. No new test was added or assertion removed.

Desktop (1575 pixels) and 390 × 844 inspection found readable wrapping without document overflow. The guide’s panel opens by keyboard and shows the revised description, development status, and provisional note, with no old website-not-built claim or horizontal panel overflow. Escape closes it and returns focus; normal desktop viewport dimensions were restored. The Museum’s current public website was read to prepare its next proposed description; the Museum entry remains unchanged. No broader repository check was rerun; the last recorded reader-document result remains 15 pre-existing errors.

Source digest: `24544528259af9ee733fef47974387d50538bf96f177b830cf0a810051ab7241`.
Preview HTML SHA-256: `189905adf3af70bac8f33409eeb148e587247dd33b0bc546e4a04d0b18801d9e`.

These are selected copy and interaction checks, not full accessibility or research validation. The candidate remains a draft with no release authorization.

## Accepted Museum of Ordinary Life passage: 2026-10-17 (Pacific)

Applied writing block `60427` verbatim to HTML and English translation data. The independent-archive label and existing panel explanation of separate fictional-reuse permissions remain. All 11 site tests pass without test changes, including fragment/CSP checks, preview/source byte parity, and the intentionally blocked release gate. Other descriptions, executable script, builder, and historical publication approval are unchanged.

Desktop (1575 pixels) and 390 × 844 inspection found no horizontal document or panel overflow. The Museum panel opens by keyboard and shows the same revised summary plus the existing permission explanation. Escape closes it and returns focus; normal desktop dimensions were restored. The Wiki’s public README and context were read for its next proposed description; the Wiki entry remains unchanged. No broader repository check was rerun; the last reader-document result remains 15 pre-existing errors. No Museum, Wiki, private-project, or story-canon edit is included.

Source digest: `d708b584356587c6e45b55637f7c3ab69d1bad1767148e6b6d0fca8c49f2738f`.
Preview HTML SHA-256: `279e6dd5a959f94395d976297307f0cced9292d598cc506f1b31fbf34c822060`.

These are selected copy and interaction checks, not independent archival validation, complete accessibility, or website publication approval.

## Wiki description and accurate Reading help: 2026-10-17 (Pacific)

Applied writing block `81962` verbatim to HTML and English translation data. Removed an obsolete light/dark-control reference from the footer’s Reading instructions. All 11 site tests pass without test changes, including fragment/CSP checks, preview/source byte parity, and the intentionally blocked release gate. Other descriptions, executable script, builder, and historical approval are unchanged.

Desktop (1575 pixels) and 390 × 844 browser inspection found no horizontal document or panel overflow. The Wiki panel opens by keyboard and shows the same revised summary; Escape closes it and returns focus. The native Accessibility disclosure shows the corrected reading choices. Normal desktop dimensions were restored. The placement note’s stale approved-source claim is corrected, and its old hosting account is labelled historical. Public/private Wiki architecture and collaboration boundaries were read only to plan later work; no entity freshness comparison, synchronization, content transfer, or private-context export is claimed. No broader repository check was rerun; the last recorded reader-document result remains 15 pre-existing errors.

Source digest: `eef5e1a6d9b17556a25e6532a75e19b8fec45fa547800ad50d80182d924604ef`.
Preview HTML SHA-256: `cf10382a73f28b78e0ea5a929604df8a62337da33c768b1f391c6b3ba655667e`.

All seven related-project descriptions have completed passage review. These are selected presentation checks, not a complete accessibility audit, completed page review, Wiki-content validation, or website publication approval.

## Accepted Take part wording: 2026-10-17 (Pacific)

Applied writing block `36791` verbatim to HTML and English translation data. All 11 site tests pass without test changes, including fragments, CSP hashes, preview/source byte parity, and rejection of the unapproved candidate by the release gate. The executable script, builder, and historical approval are unchanged. Existing contribution routes and the nothing-is-submitted note remain.

Desktop (1575 pixels) and 390 × 844 browser inspection found readable wrapping without horizontal document overflow. Both Discussions and issue panels open by keyboard and show their revised description, public-posting note, and unchanged destination. Escape closes each panel and returns focus. The issue panel also fits the narrow viewport without horizontal overflow. Normal desktop dimensions were restored. No external continuation link was activated and no post was submitted. The footer’s working-paper link was compared with its source/history claim: it points to `main`, not a fixed revision; a correction is proposed for footer review. PR #6 was read as an earlier, closed, unmerged draft review record, not a current approval. Footer copy is unchanged in this pass.

Source digest: `db6cb6144c77b252276f75024a93a0ca3adf573b7b5dcfd1c5fee5f91c9822ee`.
Preview HTML SHA-256: `a7a3b51fb2c7f21b9488049244044c971156cfa19be1725551e2c49cb1e78f07`.

These are selected copy and interaction checks, not completed page or accessibility review. No broader repository check was rerun; the last recorded reader-document result remains 15 pre-existing errors. The candidate remains a draft without website release approval.

## Sources and page history: 2026-10-18 (Pacific)

Applied writing block `92508` verbatim as four paragraphs with inline links, in visible HTML and English translation data. The rendered prose matches all four approved paragraphs after excluding existing screen-reader-only link instructions. All three source destinations and their panel behavior remain. The builder maps the new preview sentence to a proposed hosted AI-assistance sentence; the existing release test now checks that unpublished wording is removed while AI disclosure remains. The source revision and sitemap dates are October 18. All 11 tests pass, including exact-source release rejection against unchanged historical approval, source/preview parity, fragments, and CSP. The executable page script is unchanged.

At 1575 pixels and 390 × 844, the disclosure opens by keyboard and wraps without horizontal document overflow. The earlier-review link opens its existing panel with the same PR #6 destination and incomplete-review status. Escape closes it and restores focus. No external continuation was activated. Normal desktop dimensions were restored. Current Reading controls and the reduced-motion rule were inspected for the next wording proposal; WCAG 2.2 and W3C cognitive guidance were read from their official URLs. Accessibility wording is unchanged pending review. This is not a full conformance, screen-reader, or real-device audit.

Source digest: `a3fb7f8133227f2dd6f092c4f8d6d0a441fc2b33ae6ef7e065dfaa83160e894a`.
Preview HTML SHA-256: `09cbbec8a46045ef392cf910a58103e4ab9d26f635108e99599625dff5114440`.

P1-08 remains in progress; 1/4 footer passages are applied. No broader repository check was rerun; the last reader-document result remains 15 pre-existing errors. No merge, deployment, approval-file update, or research-review change is included.

## Accessibility and reading choices: 2026-10-18 (Pacific)

Applied writing block `43872` verbatim to visible HTML and English translation data, with inline W3C references and emphasis on Reading. The rendered paragraphs match the approved wording after excluding screen-reader-only link instructions. All 11 site tests pass without changes to tests, the builder, or executable script. Source/preview byte parity and CSP checks pass; the candidate still fails release approval against unchanged `approval.json`. A previously occupied preview destination was left intact and a fresh output directory used.

At 1575 pixels and 390 × 844, the native disclosure opens by keyboard and wraps without horizontal document overflow. The reporting link opens the existing issues panel, showing its destination and public-posting note. Escape closes it and returns focus. No external continuation was activated. Normal desktop dimensions were restored. These selected checks do not complete screen-reader, real-device, or WCAG conformance review. The earlier no-JavaScript baseline remains recorded; it was not repeated for this copy-only change.

For the next Privacy proposal, source inspection confirmed browser-local reading preferences with a reset control. Existing self-contained-resource and CSP tests pass. No hosting-provider retention policy, external browser translation service, or live deployment was audited; no such claim is inferred from local page behavior. Privacy source remains unchanged pending prose review.

Source digest: `9a267217f70e73814323bf234cea420f08e9812dbf07c49e4eda37fbda024ccd`.
Preview HTML SHA-256: `d87cb1189c47070c6cf44afa6dcb82662bd7f57a204fb07c93eb25dbf0fb7b03`.

P1-08 remains in progress (2/4 footer passages applied). No broader repository check was rerun; the last reader-document result remains 15 pre-existing errors. No merge, deployment, approval-file update, or research-review change is included.

## Privacy and this preview: 2026-10-18 (Pacific)

Applied writing block `70629` verbatim to visible HTML and English data, retaining Reading emphasis. The rendered four paragraphs match the approved text. The builder’s two publication-state substitutions were updated for the revised preview status and hosting-policy note. The existing release test additionally checks that the local-preview sentence is removed and the unverified-policy qualification retained. All 11 tests pass, including self-contained resources, CSP, source/preview parity, and release rejection against unchanged historical approval. The executable page script is unchanged.

At 1575 pixels and 390 × 844, the native Privacy disclosure opens by keyboard and wraps without horizontal document overflow. Normal desktop dimensions were restored. No page preferences, external destinations, hosting settings, or privacy settings were changed. These are selected presentation checks, not a provider-policy or browser-service audit. The public repository’s actual CC0 file and Microsoft’s font license were inspected to prepare the next Credits proposal; Credits source remains unchanged.

Source digest: `1212848460f42f7e241f3c639a1e94e9cbd882f4b4f5ed6d783abb0d34261c8f`.
Preview HTML SHA-256: `81dac7ee1250c776a4aeb80dd455f37ae7f2e13e0db0f59a16c880e9dc14dded`.

P1-08 remains in progress (3/4 footer passages applied). No broader repository check was rerun; the last reader-document result remains 15 pre-existing errors. No merge, deployment, approval-file update, or research-review change is included.

## Credits and reuse: 2026-10-18 (Pacific)

Applied writing block `58216` verbatim to visible HTML and English data, with inline links and the founder credit retained. The rendered three paragraphs match the approved wording after excluding screen-reader-only instructions. All four destinations remain. The first test run found one stale required label, “Cascadia Mono license”; the existing expectation now checks the approved “SIL Open Font License 1.1” label. No assertion was removed or new test added. All 11 site tests then passed, including source/preview parity, CSP, embedded resources, fragments, and release rejection against unchanged historical approval. The executable script and builder are unchanged.

At 1575 pixels and 390 × 844, Credits opens by keyboard and wraps without horizontal document overflow. The font-license link opens its existing source panel with the same destination and new label; Escape closes it and returns focus. No external continuation or profile link was activated. Normal desktop dimensions were restored. The World panel was read to prepare its next copy proposal; its summary, extra paragraph, and availability note remain unchanged.

Source digest: `c81f4c16c583b53c096e1008ff5f61c0e39991f62caa903090dd03725766c1c0`.
Preview HTML SHA-256: `9be169975b902968ffa87930659866a7a79c6bcc192bd3eba341dbbd94a74ca9`.

Footer passage review is 4/4 complete. P1-08 remains in progress for panels and full-page review; no complete accessibility or research validation is implied. No broader repository check was rerun; the last reader-document result remains 15 pre-existing errors. No merge, deployment, approval-file update, license change, or permission change is included.

## Coherent World panel refinement: 2026-10-18 (Pacific)

Applied writing block `64930` verbatim to the English panel data, removed World’s extra paragraph, and retained its approved summary and type. The shared renderer now guards the optional extra field; its CSP hash was refreshed. A source comparison confirms these are the only executable-script changes, and only the World extra/status entries changed in translation data. The obsolete World preview/publication marker was removed from the builder. All 11 site tests pass without test changes, including CSP, fragments, source/preview parity, and release rejection against unchanged historical approval.

Desktop (1575 pixels) and 390 × 844 checks show exactly two World paragraphs with no empty row or horizontal panel overflow. The retained No One Noticed link switches to the novel panel, which still shows its unchanged summary, extra paragraph, and availability note. Escape closes the panel and returns focus to the original World trigger. Both panels fit the phone width. Normal desktop dimensions were restored. No external destination or private material was opened or added. These are scoped rendering and interaction checks, not complete accessibility or project-content validation.

Source digest: `7c80ad37d0122cae3908683d890240dd8978c47bbc9d90bf2933d5f332ec6a3c`.
Preview HTML SHA-256: `67feb900db54cb5f81a9bcc5f461a8353865f174c5ef793d11554369ec8d770b`.

P1-08 remains in progress; No One Noticed panel wording is next. No broader repository check was rerun; the last reader-document result remains 15 pre-existing errors. No merge, deployment, approval-file update, or project-status change is included.
