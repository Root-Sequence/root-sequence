# Publication review

**Status:** proposed procedure; AI-assisted; author review pending.  
**Scope:** review before first disclosure, including public branches, pull requests, issues, attachments, releases, and deployment artifacts.

## Three disclosure levels

| Level | What belongs here | Handling |
| --- | --- | --- |
| Public commons | Public-safe questions, reviewed explanations, selected examples, and deliberately shareable drafts | Record sources, evidence status, authorship, scope, and applicable permissions. A public draft may still be unfinished. |
| Limited review | Unpublished research, draft implementations, or collaboration material needing review | Use a genuinely access-controlled location; share only the smallest useful excerpt with identified reviewers. Record any agreed confidentiality and reuse terms. |
| Restricted | Personal or participant information, credentials, security-sensitive details, contractual confidences, or details with a concrete serious-harm pathway | Do not publish by default. Obtain the relevant person's consent or specialist review where appropriate; produce a safer abstract only when justified. |

These are handling decisions, not badges of importance. Incompleteness alone is not dangerousness, and an interesting idea is not automatically a sensitive invention. Assess the harm mechanism, affected people, likelihood, severity, and incremental enabling detail.

**Private material must never be placed in a public branch for review.** The existing [research publication boundary](../research/README.md#publication-boundary) already makes this distinction. A label, `.gitignore`, or unmerged PR is not an access control. Making a public repository private later does not make its existing public forks private.[^visibility]

## Before sharing: the smallest sufficient review

1. **Identify the exact artifact.** Record repository/file, revision or hash, intended audience, purpose, and whether it is already public. Do not backdate approval.
2. **Separate content types and rights.** Distinguish writing, code, images, data, quotations, third-party contributions, and generated material. Check the relevant [licensing decision](licensing.md); unresolved ownership is not permission.
3. **Check people and obligations.** Remove unnecessary personal details, private identifiers, unpublished collaborator material, employer/client confidences, and secrets. Consent to one use is not consent to every use.
4. **Assess concrete risks and alternatives.** Consider harmful enablement, misleading claims, decontextualization, confidentiality, and premature disclosure. Compare full release with a summary, synthetic example, redaction, delay, or no release. Do not assume attribution fixes harm.
5. **Record provenance and limits.** Identify human contributions, AI assistance, prior work, evidence status, known weaknesses, and the exact version. See [attribution](attribution-provenance.md).
6. **Authorize the boundary crossing.** The responsible person explicitly approves the exact public-safe version and destination. Unresolved serious risk or missing permission means hold. Research approval and website deployment approval remain separate.
7. **Verify the actual release.** Inspect the rendered files, links, attachments, commit history exposed by the chosen sharing method, and automation outputs. Record what was actually published, not merely what was planned.

## Minimal release record

Use this block in the artifact's own maintained record; keep confidential reasons in an access-controlled record, not a public issue.

```yaml
artifact: "repository/path"
revision: "exact commit or file hash"
current_access: "public | limited-review | restricted"
proposed_audience: "specific audience"
purpose: "why this disclosure is useful"
rights_and_consent: "checked sources, applicable terms, unresolved items"
risk_and_alternative: "specific pathway and safer alternative considered"
evidence_status: "hypothesis | normative | tested | other, with details"
human_and_ai_contributions: "documented roles; no inferred authorship"
approved_by: null
approved_on: null
approved_scope: null
publication_destination: null
verification_record: null
```

A blank approval is not approval. Record an owner and an event-based review point for a hold, such as completed rights review; do not invent an expiry that automatically releases material.

## An accidental disclosure

Stop further dissemination, preserve a private incident record, and use the existing [security process](../SECURITY.md) for security issues or [private concern route](../contributing.md#choose-the-right-contribution-path) for other sensitive matters. Rotate exposed credentials where relevant. Deletion is not proof that copies no longer exist. Obtain help before rewriting shared history or making legal demands; retain the evidence needed to understand the event.

## References

[^visibility]: GitHub, [Setting repository visibility](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility), checked 2026-10-22.

[Research stewardship](README.md)
