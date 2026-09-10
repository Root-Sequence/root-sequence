# Root Sequence Thought Routing (`RS?`)

**Document role:** Organization-wide capture and routing convention<br>
**Status:** Working convention / v0.1<br>
**Canonical scope:** How a thought moves from conversation into the existing Root Sequence ecosystem without becoming duplicate substance, automatic publication, or accidental canon

Root Sequence already has project repositories, local inboxes, Wiki entities and Seeds, Idea Trails, project queues, and a private Console. `RS?` is the small invocation that makes those pieces behave like one intake system.

> **Capture once. Choose one canonical home. Link or transform everywhere else.**

## Invoke it

End a thought with **`RS?`**, or say **“route this”** or **“put this places.”**

That means:

1. preserve the thought and its source before rewriting it;
2. inspect the current ecosystem and search for existing treatments;
3. classify the thought without pretending classification proves it true;
4. choose one canonical substantive home, or keep it explicitly unrouted;
5. add only the links, project-specific transformations, queue entries, or graph edges that are genuinely useful;
6. return a routing receipt saying exactly what changed and what did not.

`RS?` does **not** mean “publish this everywhere,” “make this canon,” or “create a repository.” Private material stays private unless publication is separately and explicitly requested.

Narrower prompts remain narrow. For example, **`BHIG?`** asks for Being Human(e) / Atlas capture and mapping. It should not trigger an organization-wide propagation pass unless the thought clearly needs a wider home or the user also invokes `RS?`.

## The routing pass

### 1. Capture the source once

Keep the smallest durable formulation that still preserves the thought's meaning. Record the exact user wording when the wording itself matters, along with enough provenance to find the source again.

Do not archive an entire conversation merely because one idea is useful.

### 2. Search before placing

Check, as relevant:

- the ecosystem map and repository READMEs;
- the Wiki's public identities and private overlays/entities;
- project-local indexes, inboxes, Seeds, backlogs, research, canon ledgers, and decision records;
- Idea Trails and their document graph;
- the Console's routed items and local capture queue.

Search for the mechanism and question, not only the exact phrase. Similar wording may hide different ideas; different wording may describe the same one.

### 3. Classify on separate axes

Do not collapse these into one vague status.

**Kind**

- observation;
- question;
- phrase or motif;
- connection;
- source;
- hypothesis;
- proposal;
- decision;
- narrative seed;
- implementation note.

**Epistemic status**

- `OBSERVATION`;
- `INTERPRETATION`;
- `HYPOTHESIS`;
- `NORMATIVE`;
- `SOURCE_SUPPORTED`;
- `CONTESTED`;
- `OPEN_QUESTION`.

**Capture state**

- `CAPTURED` — preserved, not yet routed;
- `TRIAGED` — compared with current homes and relationships;
- `ROUTED` — one canonical destination or explicit holding queue chosen;
- `INTEGRATED` — durable destination and necessary links updated;
- `PARKED` — intentionally retained without current development;
- `RETIRED` — no longer current, preserved when history matters.

Project-local development or canon statuses remain authoritative inside their projects. A routing state never overrides `CANON`, `PROVISIONAL`, `OPEN`, `CONTESTED`, or other local vocabularies.

### 4. Choose a disposition

Reuse the existing orphan-reconciliation dispositions:

- `CONNECT` — the home already exists; add a missing relationship or pointer;
- `ALIAS` — preserve alternate wording for retrieval;
- `MERGE` — incorporate the durable addition into an existing record instead of creating a duplicate;
- `PROMOTE` — create a durable entity or project record only when stable identity warrants it;
- `ROUTE` — move the substance to the correct existing project;
- `KEEP AS SEED` — preserve it as intentionally immature;
- `PAUSE`, `REFERENCE`, `SUPERSEDE`, `RETIRE`, or `INVESTIGATE` — retain an explicit lifecycle decision;
- `REMOVE` — only after deliberate review establishes that preservation has no value.

More than one disposition may be needed, such as `MERGE` for the substance and `ALIAS` for the original phrase.

### 5. Assign one canonical substantive home

Use the routing guide in [`ECOSYSTEM.md`](ECOSYSTEM.md). The Wiki owns identity, naming, provenance, relationships, and findability; it does not absorb a project's full argument, design, implementation, research, or canon.

When an idea matters to several projects, record a project-specific question or transformation rather than copying the source note:

```text
one canonical source
    ├── project A: tests a bounded real-world claim
    ├── project B: develops a human-scale implication
    ├── project C: explores a speculative system
    └── project D: translates a lived or narrative consequence
```

If no adequate home exists, keep the item `CAPTURED` or `TRIAGED` in an existing private inbox/Seed surface. Do not create a repository merely to make the map look complete.

### 6. Update only the useful projections

Depending on the result:

- add or merge substance in the canonical project;
- add a project-local queue item when review remains;
- add a Wiki Seed or entity when stable identity or cross-project retrieval warrants it;
- add an Idea Trail relationship when the question materially recurs across at least three projects;
- let the Console surface those existing records and relationships;
- update nearest READMEs, indexes, maps, generated outputs, and change-impact documentation when their scope actually changed.

Not every thought deserves every projection.

## Minimum routing record

Use this shape in a Console export, issue, note, or agent handoff. Projects may translate it into their own templates.

```yaml
id: stable-id-or-capture-id
captured_at: YYYY-MM-DDTHH:MM:SSZ
trigger: RS? | route this | put this places | manual
source:
  type: conversation | observation | book | article | media | project-work | other
  pointer: durable URL, conversation ID, citation, or local source reference
  exact_words: "preserve when wording matters"
visibility: private-until-reviewed | public-safe | restricted
kind: observation | question | phrase | connection | source | hypothesis | proposal | decision | narrative-seed | implementation-note
epistemic_status: [OBSERVATION]
capture_state: CAPTURED
disposition: INVESTIGATE
canonical_home: null
related_existing: []
project_routes: []
canon_effect: none
publication_effect: none
next_review: null
```

For each `related_existing` match, say whether it is a likely duplicate, alias, precursor, contradiction, supporting source, or merely adjacent. Similarity is a review signal, not permission to merge.

## Routing receipt

An `RS?` pass should end with:

- **Captured:** the durable formulation and source;
- **Canonical home:** exact repository/path, or `UNRESOLVED`;
- **Disposition:** what happened to the thought;
- **Related existing material:** matches checked and how they differ;
- **Cross-project routes:** links or transformations actually added;
- **Status effects:** explicit canon, publication, and visibility consequences;
- **Changed:** exact files, issues, or records changed;
- **Not changed:** relevant surfaces deliberately left alone;
- **Next:** the highest-leverage unresolved action.

## Automation boundary

Safe deterministic assistance includes validating required fields, checking links, regenerating indexes, surfacing unresolved captures, detecting exact duplicate IDs, and reporting drift between explicit metadata and generated views.

Human or agent review remains necessary for semantic equivalence, canonical-home selection, canon changes, publication, visibility changes, deletion, and whether a cross-project transformation is faithful.

> **Automate memory, not judgment.**

The shared maintenance boundary is documented in [`Root-Sequence/.github/PROJECT_STEWARDSHIP.md`](https://github.com/Root-Sequence/.github/blob/main/PROJECT_STEWARDSHIP.md). The private Root Sequence Console is a capture and orientation surface; it must not silently become the canonical destination.
