# Website copy review: September 16, 2026

## Review candidate: name explanation — September 18, 2026

The current candidate adds a short **Why “Root Sequence”?** passage to the
About section. It explains the two parts of the name, states the question they
form together, and links to the canonical concept page in the research
repository. It does not add a new numbered section or change the site's wider
structure.

The candidate HTML has SHA-256
`08a1ce67f37f3db55e235cb3703bcdb552deead2ffd4aafd6cd732f69b384356`.
The combined publisher-and-page source digest is
`cdf268f194aea69f1bee65dfdb6f3b1afd8e52a0dcff4a1069cfb1cbc419997d`.

This candidate has not yet been approved. The prior receipt remains in
`approval.json`, so the release safety check is expected to block publication
until Rae approves this exact wording and digest.

## Approval update: expanded Selected Research — September 18, 2026

The review candidate expands **Selected research and writing** from three to
six entry points. It adds:

- **Intelligence Ecology** as a developing conceptual framework;
- **Events, patterns, and scale** as a systems method; and
- **Resilience and graceful degradation** as a developing systems note.

The existing entries now use more specific role labels: working paper,
conceptual framework, design principle, systems method, systems note, and
historical analysis. Each new link has a plain-language description and a
local context panel. The candidate HTML has SHA-256
`0fe3a3a228e75c7d30d73061a48409a971c0070b46e20f907c6d1e8979d5ca62`.

Rae Lovejoy approved the current six-item Selected Research section for
publication on 2026-09-18. `approval.json` is tied to this exact candidate.

## Approval update: Legible Systems route — September 18, 2026

Rae Lovejoy approved moving Legible Systems out of the obsolete `core/` path
and updating the website accordingly. The source link and its contextual
overlay now route directly to `concepts/legible-systems.md`. No visible copy,
layout, project description, or interaction changed. The updated approved HTML
has SHA-256
`24224b29f6f049fa28409b9d785433997e1331d5c66659da648a1da41c97d526`.

## Approval update: September 18, 2026

Rae Lovejoy initially approved the single-file website preview with SHA-256
`9e5bb0eade87e488410baf4fb42ce812efbe5f013c517603edb448337d78f56e`.

Rae Lovejoy approved a follow-up addition on 2026-09-18: section 6 now lists
**Being Human(e): An Incomplete Guide** as a developing practical field
guide. Its project panel says that the public website has not been built yet
and therefore offers no external website link. The updated approved HTML has
SHA-256
`d9f46f55c483cb9147bce6ece637f63f660f50a21f239b4ab43598008d72d36c`.

Publication changes are limited to state-dependent labels: search indexing,
local-preview wording, the publication date, and references that say "this
preview" when the page is hosted. Apart from the approved Being Human(e)
addition, the headline, body copy, sections, existing project descriptions,
links, overlays, accessibility controls, English source edition, palette,
logo, and embedded Cascadia Mono wordmark are unchanged.

The prior review below describes the superseded 11-page candidate and remains
as project history.

## Request

Make both websites understandable to first-time visitors and edit the machine-sounding prose using Rae's repeated Rossmann writing reference.

## Changes

Rewrote project introductions, descriptive headings, guide copy, and navigation labels. Explained specialist vocabulary using everyday examples. Kept all existing page URLs, source destinations, and project relationships. Moved development labels and dates into native details below the reading text. Technical downloads moved to footer details. Sources remain available. The research site now uses a system sans-serif body face; the story site retains its serif reading face.

No One Noticed now states that it is a science-fiction novel in progress by Rae Lovejoy and introduces the AI premise directly. Edited stiff wording and abstract commentary in the three scene drafts while retaining their events and questions. AI assistance and pending author review remain disclosed. Scene status remains outside the established book. No World Bible, source research, or real Museum material was edited.

Added site-scoped `AGENTS.md` instructions pointing to `realrossmanngroup/no_ai_slop_writing_rules`. Selected phrase and first-visit checks are part of the tests. They are editing checks, not an AI detector. The full Slop Filter application was not run.

## Checks performed

- Root Sequence: 17 local automated tests passed, including the original 13 publication tests.
- No One Noticed: 14 local automated tests passed. The old preview equality test was replaced by a current-manifest check because the requested edits intentionally change the old output. The historical recovery receipt remains separate.
- 80 in-memory Chromium checks: all 20 pages at 375 and 1280 pixels, in light and dark modes. No horizontal document overflow; one main heading per page; About this page opened and closed using the keyboard.
- Visually inspected the rendered mobile story homepage and desktop research homepage.

The browser checks loaded HTML and CSS in memory. They do not test live hosting, network delivery, actual mobile devices, comprehension with readers, or full accessibility. The wording still needs Rae's editorial judgment.

## Publication boundary

No release approval, deployment, DNS update, repository-visibility change, or story-canon change. Existing source history remains in Git. These changes update the staged websites, not a verified live domain.
