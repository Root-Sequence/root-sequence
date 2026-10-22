# Public licensing baseline — 2026-10-22

**Status:** source-based preliminary audit; not legal clearance or a file-by-file rights audit.  
**Method:** inspected connected GitHub repository metadata, top-level trees, selected license/README/contribution files, and relevant existing PR descriptions. Public observations only; no private repository contents are included here.

## Coverage and findings

| Public repository | Observed evidence | Finding / next action |
| --- | --- | --- |
| `root-sequence` | [`license`](../license), README, and contribution guidance at `a8b0f805d1c4bbd14c52845b4861854b9ebc6e8f` | CC0 declaration. Preserve existing grants; map any exceptions and distinguish code, prose, assets, and third-party work before changing future terms. |
| `liberated-intelligence` | [`license`](https://github.com/Root-Sequence/liberated-intelligence/blob/ad77e8b56178288ef12fa08e6e16c2c1393fa49a/license) and README | CC0 declaration. Citation requests must remain requests for this covered material. |
| `universal-coherence-framework` | [`LICENSE`](https://github.com/Root-Sequence/universal-coherence-framework/blob/e1c7b28803f58bea4a5b3a200063d5f579260b50/LICENSE), README, publication/model declarations | CC0, not MIT. Existing citation metadata should be preserved and checked at the item level. |
| `liberation-mass` | [`LICENSE`](https://github.com/Root-Sequence/liberation-mass/blob/4c791af6014a6ceedcb2e92cc4622f7a5076d485/LICENSE) versus [`CONTRIBUTING.md`](https://github.com/Root-Sequence/liberation-mass/blob/4c791af6014a6ceedcb2e92cc4622f7a5076d485/CONTRIBUTING.md) | **Conflict:** root license is CC0; contribution terms say CC BY-SA 4.0. Trace affected contributions and obtain a deliberate resolution. Do not assume all content can be re-dedicated. Existing [PR #7](https://github.com/Root-Sequence/liberation-mass/pull/7) also preserves this unresolved issue. |
| `beinghumane-guide` | [`LICENSE`](https://github.com/Root-Sequence/beinghumane-guide/blob/main/LICENSE), blob `463788c7f9f946e196e14630aa39d781e2cbae1f` | MIT declaration. Confirm intended scope for site code versus prose, letters, media, and later contributions; do not silently reinterpret existing permissions. |
| `.github` | Root directory listing and Project Stewardship | No top-level LICENSE/COPYING file observed. This does not establish that no terms appear elsewhere; review content-specific declarations. Do not inherit another repository's CC0 by association. |
| `wiki` | Root tree `f15a718d932c1571d85396b85250b93d8953c6a4` | No top-level LICENSE/COPYING file observed. Review entity source permissions and any text-level declarations separately. |
| `root-sequence-discussions` | Root tree `e93ec409bf3f490dbce47ae242921a5ccb276b1e` | No top-level LICENSE/COPYING file observed. Files, issue comments, and discussion contributions need separate rights analysis; no blanket contributor consent inferred. |
| `existential-euphoria` | Root tree `67382ef196390abcc498d9b504061e5b4f6cae6f` and README | No top-level LICENSE/COPYING file observed. Clarify intended permissions before adding a blanket license; cited media and references do not become project-owned works. |

The repository listing exposed nine public repositories in scope. This baseline does not certify the absence of per-file notices, dependency licenses, embedded copyrighted media, contributor rights, prior grants, secrets, or privacy issues. A missing root license file is a discoverability finding, not proof of complete absence of permission.

## Priority decisions

1. Resolve the Liberation Mass conflict by tracing provenance, not merely replacing one label.
2. Define whether new separable research prose should remain CC0 or use CC BY / CC BY-SA. The decision is not made here.
3. Clarify mixed code/content scope in Being Human(e) and any similar repositories.
4. Review the four repositories without a top-level license file for existing text-level grants and contributor rights before adding one.
5. Review third-party assets, datasets, and dependency licenses before any comprehensive licensing claim.

## What changed in this pass

Documentation, citation guidance, a publication-review procedure, and a decision checklist are proposed. **No license text, repository visibility, access membership, public release, or existing contributor grant was changed.** Existing unmerged commons and professional-presentation proposals remain separate. The proposed procedures are not evidence of completed legal review.

[Licensing decisions](licensing.md) · [Implementation checklist](implementation-checklist.md) · [Research stewardship](README.md)
