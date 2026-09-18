# Security Policy

## Scope

Security reports are appropriate for vulnerabilities involving:

- the public website or its build and deployment process;
- repository automation and GitHub Actions;
- scripts or tools in this repository;
- accidental exposure of credentials, tokens, private information, or unpublished material;
- a repository configuration that could allow unauthorized changes or disclosure.

Broken links, unclear writing, disputed claims, missing citations, accessibility problems without a security impact, and ordinary software bugs can use the public issue forms.

## Report a vulnerability privately

Use [GitHub private vulnerability reporting](https://github.com/Root-Sequence/root-sequence/security/advisories/new). Do not open a public issue for a vulnerability or include secrets, exploit details, or personal information in public discussions.

Include only the information needed to understand and reproduce the problem:

- the affected page, workflow, script, or configuration;
- a concise description of the potential impact;
- reproduction steps or a minimal proof of concept when safe;
- any conditions required for exploitation;
- a suggested mitigation, if known.

Avoid accessing, retaining, or sharing data that is not yours. Stop testing if it could disrupt the live site, alter repository content, expose private material, or affect another person.

## Supported version

The current `main` branch and the currently deployed public site are supported. Historical commits, abandoned branches, forks, and unmerged proposals are not maintained as supported releases.

## Handling and disclosure

Maintainers will validate the report, determine its scope, and coordinate a fix or documentation update when appropriate. Response timing is best-effort; this project does not promise a fixed service-level agreement.

Please allow time for investigation and remediation before publishing vulnerability details. If the problem primarily belongs to a third-party service or dependency, report it to that maintainer through their security process as well.
