# Licensing decisions and limits

**Status:** decision framework, not a license change; AI-assisted; author/legal review pending.  
**Prepared:** 2026-10-22.

## Existing permissions remain

The main repository, Liberated Intelligence, and UCF currently declare CC0; other projects differ or need clarification. The [audit](licensing-audit-2026-10-22.md) records the inspected evidence and its limits.

CC0 is intended as an irrevocable dedication/waiver with a fallback license. It permits commercial reuse of covered material without an attribution requirement. Changing a label now does not recapture rights already relinquished. A later, independently copyrightable contribution can have separate terms only to the extent the contributor holds the relevant rights; this does not restrict the older material inside it.[^cc0]

Copyright protects qualifying expression rather than the underlying idea, system, or method. A license is therefore not a general veto over learning, independent implementation, or lawful exceptions.[^ideas] A public GitHub repository is not automatically open-source licensed.[^github]

## Choose by material and purpose

These are candidates for a separate decision, **not newly applied defaults**.

| Material / purpose | Candidate | Principal tradeoff |
| --- | --- | --- |
| Material deliberately given to the public without reuse conditions | CC0 | Maximum reuse; no attribution obligation. |
| New research prose or diagrams where credit matters and broad uptake is desired | CC BY 4.0 | Commercial reuse remains allowed; qualifying sharing requires attribution and change/license information. |
| New prose or diagrams where keeping distributed adaptations in a commons matters | CC BY-SA 4.0 | Adds ShareAlike for shared adaptations; does not require independent implementations of ideas to be published. |
| New material where noncommercial reuse is a deliberate priority | CC BY-NC-SA 4.0 | Restricts covered commercial uses, but is not an ethical-use test; it may exclude beneficial uses too. |
| Software | Evaluate a software license separately, including permissive or copyleft choices | Review dependencies, contribution rights, distribution and service models, compatibility, and desired obligations before selecting. |
| Confidential collaboration | Limited disclosure plus an appropriate express agreement | Terms must be agreed; a README request is not a negotiated contract. |

See the CC license summaries and software guidance in [references](references.md). CC advises against using its content licenses for software. Do not append an improvised harmful-use clause to an established license while retaining its standard name. Open-source software licenses cannot discriminate against persons/groups or fields of endeavor; a use-restricted approach must be described honestly rather than labeled OSI-compatible open source.[^osi]

## Proposed decision order

1. Keep existing grants and release history intact.
2. Resolve conflicting declarations and distinguish third-party material before publishing a new blanket statement.
3. For **future separable writing**, compare CC BY and CC BY-SA first; retain CC0 where unrestricted reuse is truly intended. Do not automatically choose NC or impose commercial permissions across the ecosystem.
4. Evaluate software, data, media, and third-party contributions on their own terms.
5. Before applying a new choice, record exact paths, rights holders, effective revision, treatment of legacy material, contributor consent, and the compatibility check. Update the license notice, README, and contribution guidance together in a dedicated reviewed change.

No repository visibility change, rights assignment, relicensing, contributor agreement, patent filing, or defensive publication is authorized by this document. Potential patent or confidentiality decisions need qualified advice before disclosure; a timestamp is not a legal opinion.

## Decision record

```yaml
status: proposed
material_and_paths: []
rights_holders_verified: false
existing_terms_and_versions: []
new_candidate: null
reason_and_tradeoffs: null
legacy_material_treatment: "Preserve previously granted rights."
third_party_and_contributor_review: pending
approval: null
effective_revision: null
```

## References

[^cc0]: Creative Commons, [CC0 legal code](https://creativecommons.org/publicdomain/zero/1.0/legalcode.en) and [FAQ](https://creativecommons.org/faq/), checked 2026-10-22.
[^ideas]: U.S. Copyright Office, [What does copyright protect?](https://www.copyright.gov/help/faq/faq-protect.html), checked 2026-10-22.
[^github]: GitHub, [Licensing a repository](https://docs.github.com/articles/licensing-a-repository), checked 2026-10-22.
[^osi]: Open Source Initiative, [Open Source Definition](https://opensource.org/osd), especially sections 5–6, checked 2026-10-22.

[Research stewardship](README.md)
