# Root Sequence — Public Seed site

Reader-facing source for the first `rootsequence.systems` edition. **Implemented as a review candidate; not merged, deployed, or verified live by this directory.** The existing research files remain canonical for their full arguments. The existing Wiki remains canonical for shared identities, project lenses, and relationship navigation.

## Contents

- `content.json` — the single source for 11 reader-facing pages, including five Atlas guides and selected project relationships.
- `build.py` — offline, standard-library-only static builder; no account or runtime service required.
- `style.css` — responsive, local-only light/dark/print presentation.
- `test_site.py` — 13 automated checks, including release gating and private-address exclusion.
- `VALIDATION.md` — dated local validation receipt and explicit limits.

These are intentional reader-facing transformations, not replacements for source arguments. Sources and provenance appear on the relevant pages. New guides are Seeds; their maturity does not override epistemic status.

## Build and inspect

From the repository root, using Python 3.10 or later:

```sh
python site/test_site.py
python site/build.py --output /tmp/root-sequence-preview
python -m http.server 8000 --directory /tmp/root-sequence-preview
```

Open `http://localhost:8000` in a browser. Alternatively, open the generated `index.html` directly: internal HTML and CSS links are relative. Choose a fresh empty output path for each build; the builder deliberately refuses to overwrite an existing edition.

The output includes the pages, `feed.xml`, `sitemap.xml`, `robots.txt`, `project-map.json`, `build-manifest.json`, and `seed-archive.zip`. The archive is a portable snapshot, not an independently stored backup.

## Publication is separate from building

Preview is the default. It has visible preview labels and `noindex`; **neither is access control**. This repository and its branches are public. Do not put private material in this site source.

A release requires a reviewed exact-source digest:

```sh
python site/build.py --digest
```

After reviewing the exact `build.py`, `content.json`, and `style.css`, an authorized reviewer can record that digest in `site/approval.json`:

```json
{
  "source_sha256": "THE_REVIEWED_DIGEST",
  "approved_by": "REVIEWER_NAME",
  "approved_at": "YYYY-MM-DD"
}
```

Then build into another empty directory:

```sh
python site/build.py --release --output /tmp/root-sequence-release
```

No approval is supplied with this candidate. The record is an editorial control, not authenticated proof of reviewer identity. Any change to the three source files invalidates the approval. Generated output omits source configuration, approval records, tests, and internal editorial notes.

**Deploy only the approved generated output.** Do not replace existing hosting or DNS settings until the authoritative deployment configuration is identified and preserved. A build command never deploys anything.

## Deferred

Deployment wiring, independently hosted preservation copies, live link/HTTPS checks, full accessibility review, and synchronization of verified entrypoints into existing Wiki navigation remain launch work. No new Wiki, inbox repository, domain purchase, or canon system is introduced.
