# Root Sequence — Idea Trail Metadata Convention

**Document role:** Cross-project metadata convention  
**Status:** v0.1 / lightweight and optional

Idea Trails become most useful when individual documents can declare which recurring cross-project questions they participate in.

This convention is deliberately small. It should make conceptual relationships easier to navigate **without turning every document into taxonomy maintenance**.

The canonical trail definitions live in [`IDEA_TRAILS.md`](IDEA_TRAILS.md).

---

# The convention

A participating Markdown document may add this immediately below its title/status metadata:

```markdown
**Idea Trails:** [Discoverability & Belonging](https://github.com/Root-Sequence/root-sequence/blob/main/IDEA_TRAILS.md#trail-1--community-discoverability-and-belonging) · [Privacy vs. Coordination](https://github.com/Root-Sequence/root-sequence/blob/main/IDEA_TRAILS.md#trail-4--privacy-vs-coordination)  
**Trail role:** real-system design

<!-- idea-trails: discoverability-belonging, privacy-coordination -->
<!-- trail-role: real-system -->
```

The visible line is for humans.

The HTML comments are stable machine-searchable metadata for future indexing, scripts, visual maps, static-site generation, or repository-wide queries.

A document does **not** need Idea Trail metadata merely because a weak connection can be imagined.

---

# Stable trail IDs

Use these IDs in the hidden `idea-trails` comment even if the display title later evolves.

| ID | Display name |
|---|---|
| `discoverability-belonging` | Community Discoverability & Belonging |
| `stewardship-authority` | Stewardship, Authority & Power |
| `mutual-aid-need` | Mutual Aid, Reciprocity & Need |
| `privacy-coordination` | Privacy vs. Coordination |
| `accessibility-participation` | Accessibility, Dependence & Participation |
| `commons-shared-capacity` | Commons, Ownership & Shared Capacity |
| `federation-autonomy` | Federation, Autonomy & Networks of Networks |
| `maintenance-invisible-labor` | Maintenance, Repair & Invisible Labor |
| `intelligence-authority` | Intelligence, Automation & Legitimate Authority |
| `resilience-failure` | Resilience, Failure & Graceful Degradation |
| `memory-provenance` | Memory, Provenance & Continuity |
| `space-liberation` | Space, Mobility & Spatial Liberation |
| `right-to-stay-small` | Growth, Scale & the Right to Stay Small |
| `accountability-externalization` | Accountability, Consequences & Externalization |

The numeric trail ordering in `IDEA_TRAILS.md` is presentation-only. The slug is the stable identifier.

---

# Trail roles

`trail-role` describes **what kind of contribution this document makes** to the trail, not its importance.

Recommended values:

| Role | Meaning |
|---|---|
| `research` | broad inquiry, evidence, analysis, historical/contextual research |
| `human-practice` | ordinary human/relational observation or practical guidance |
| `real-system` | real-world system concept, specification, prototype, pilot, or implementation |
| `embodied-practice` | gathering, ritual, facilitation, mutual-aid, or other lived collective practice |
| `analytical-lens` | optional framework/language used to examine a trail |
| `speculative-design` | systemic worldbuilding / possibility-space design |
| `narrative` | story, character, scene, canon, or lived fictional treatment |
| `preservation` | archival, provenance, memory, collection, or ordinary-evidence treatment |
| `routing-map` | map/index that connects other treatments without owning the underlying idea |

A document may use more than one role only when it genuinely performs more than one job. Prefer the narrowest useful description.

---

# Canonicality is separate from trail role

Idea Trail metadata does **not** make a document the canonical source of the idea.

Example:

- Community Infrastructure's `community-discovery.md` is currently the canonical **real-system** treatment of its Community Discovery model.
- Being Human(e) may contain the canonical **human-practice** treatment of some barriers to belonging.
- Coherent World may later contain the canonical **speculative-design** treatment of society-scale Community discovery.

Those can all belong to the same Idea Trail without competing for one universal source of truth.

When canonicality matters, state it in prose or in the graph index rather than overloading the metadata header.

---

# What not to do

Do not:

- tag every document with every remotely related trail;
- use trails as categories that dictate where files live;
- duplicate a document into several repositories to make the graph look complete;
- treat trail membership as endorsement of another project's conclusions;
- allow an Idea Trail to override project-local canon, evidence, consent, or governance;
- add metadata to private/sensitive material if the metadata itself would reveal something that should remain private.

A useful trail is one where another project would genuinely benefit from finding the document.

---

# Future tooling

The hidden comments intentionally make simple future tooling possible.

For example, a script could search repositories for:

```text
idea-trails: stewardship-authority
```

and generate a page such as:

```text
Stewardship, Authority & Power
├── Root Sequence analysis
├── Being Human(e) field note
├── Liberation Mass roles/practice
├── Community Infrastructure groups-and-membership
├── Liberated Intelligence authority note
├── Coherent World infrastructure design
├── No One Noticed scene/canon note
└── Museum preservation artifact
```

The generated graph should point to canonical documents rather than copy their contents.

---

# Adoption strategy

Do not retrofit the entire ecosystem in one giant cleanup.

Prefer:

1. tag high-signal documents when they are actively touched;
2. maintain the central graph index for important existing documents;
3. add metadata during normal revision;
4. periodically generate/check trail maps once enough documents participate.

The convention succeeds if it makes connections easier to find while remaining cheap enough that contributors actually use it.