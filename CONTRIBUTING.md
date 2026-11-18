# Contributing to Hecate

Thank you for helping build a calm, local-first assistant. Hecate is currently
pre-implementation: roadmap statements are plans, not shipped capabilities.

## Before you begin

- Read the [branching policy](docs/BRANCHING.md),
  [security policy](SECURITY.md), [AI-use policy](docs/AI_USE.md), and
  [governance foundation](docs/GOVERNANCE.md), plus the
  [local data boundary](docs/LOCAL_DATA_BOUNDARY.md).
- Use a supported Git client and the validation tools introduced by the change.
  Do not assume an unlisted runtime, model, or platform dependency.
- Start from `Dev`, use a valid topic branch, and link the relevant issue.

## Privacy and safety

GitHub is for public-safe code, documentation, aggregate evidence, and planning.
Never commit household content, recordings, transcripts, credentials, device
identifiers, private logs, health information, or resolved local paths. Security-
sensitive home actions require explicit permission boundaries and confirmation.

## Pull requests

Target `Dev` for features, fixes, documentation, tests, and maintenance. Do not
push directly to `Dev` or `main`. Promotion to `main` is a reviewed pull request
from exact-case `Dev` after release readiness is established.

Keep each pull request focused, link its issue, describe validation and test
evidence, complete the privacy checklist, and disclose project-relevant AI use.
Use `No AI assistance` when applicable. A checklist documents evidence; it does
not itself prove a Step Zero gate is complete.

Review must consider correctness, tests, privacy, security, licenses,
accessibility, household safety, and rollback impact where relevant. Maintainers
own merge and release decisions; repository rules and CODEOWNERS identify the
current review boundary.
