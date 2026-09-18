# Root Sequence website

Website source for `rootsequence.systems`, saved on the repository's main branch. The latest copy pass explains the project for first-time visitors and uses the writing reference in [AGENTS.md](AGENTS.md). See [COPY-REVIEW.md](COPY-REVIEW.md) for changes and checks. **Not deployed or verified live.**

Existing research files remain the home of the full arguments. The standalone Wiki holds shared identities, project references, and relationships. This website introduces that work without moving or replacing it.

## Files

- `content.json`: the text and metadata for 11 pages, including five introductory guides and selected project relationships.
- `build.py`: offline static builder using the Python standard library.
- `style.css`: responsive light, dark, and print styles using local fonts.
- `test_site.py`: 17 checks for publishing controls, links, source boundaries, and selected writing patterns.
- [`AGENTS.md`](AGENTS.md): writing and page-structure instructions for future edits.
- [`COPY-REVIEW.md`](COPY-REVIEW.md): the latest copy and layout review.
- [`VALIDATION.md`](VALIDATION.md) and [`PLACEMENT.md`](PLACEMENT.md): historical records of the initial build and integration.

Maturity, evidence, and publication status remain separate. Page history and development labels are available under About this page. Source links remain below the reading text.

## Build and inspect

From the repository root, with Python 3.10 or later:

```sh
python site/test_site.py
python site/build.py --output /tmp/root-sequence-preview
python -m http.server 8000 --directory /tmp/root-sequence-preview
```

The last command serves a local preview at `http://localhost:8000`. Generated page and stylesheet links are relative, so the pages can also be opened from a downloaded directory. Choose a fresh empty output path; the builder refuses to replace an existing edition.

Output includes the pages, `feed.xml`, `sitemap.xml`, `robots.txt`, `project-map.json`, `build-manifest.json`, and `seed-archive.zip`. The archive is a portable snapshot, not an independently stored backup. Authoring files and internal documentation are not exported.

## Release approval

Preview is the default. Preview labels and `noindex` do not control access. This repository and its branches are public; keep private material elsewhere.

Print the digest of the exact source to review:

```sh
python site/build.py --digest
```

An authorised reviewer can then record it in `site/approval.json`:

```json
{
  "source_sha256": "THE_REVIEWED_DIGEST",
  "approved_by": "REVIEWER_NAME",
  "approved_at": "YYYY-MM-DD"
}
```

Build the approved edition into another empty directory:

```sh
python site/build.py --release --output /tmp/root-sequence-release
```

No approval is supplied. Changes to `build.py`, `content.json`, or `style.css` invalidate an existing approval. This record is an editorial check, not authenticated proof of identity.

Deploy only the approved generated output. Identify and preserve the existing hosting and DNS configuration before replacing a site. Building does not deploy anything.

## Remaining launch work

Connect the actual host, review the export, deploy, check live links and HTTPS, keep an independent preservation copy, and update existing Wiki navigation with verified entrypoints. A full accessibility and reader-comprehension review remains separate from the local checks. No new Wiki, inbox, domain purchase, or canon system is introduced.
