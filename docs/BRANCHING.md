# Branching and release policy

Hecate uses `Dev` as the protected integration branch and `main` only for
production-ready releases.

```text
feat/*, fix/*, docs/*, ... -> pull request -> Dev -> pull request -> main
```

Routine work must not be pushed directly to either protected branch. A release
promotion to `main` must come from exact-case `Dev`, pass required checks, and
receive the review required by repository settings.

## Branch names

Use `<category>/<lowercase-kebab-case>`. For example, `FEAT: [NEW FEAT]`
becomes `feat/new-feature`. Version dots and useful nested segments are allowed,
such as `release/v1.2.0` and `feat/voice/wake-word`.

| Prefix | Purpose |
| --- | --- |
| `feat/` | New capability |
| `fix/` | Bug or regression |
| `docs/` | Documentation or policy |
| `chore/` | Maintenance or dependencies |
| `refactor/` | Internal restructuring without intended behavior change |
| `test/` | Test-only work |
| `ci/` | Automation and workflow work |
| `security/` | Security hardening or remediation |
| `release/` | Release preparation |
| `agent/` | Reserved approved automation work |

Spaces, colons, brackets, uppercase letters, and the unsupported `doc/` prefix
are invalid. Human contributors should not use the reserved `agent/` prefix.

Commit subjects should use the same conventional categories when practical,
for example `docs: explain the local data boundary`. This is a readability
standard, not a blocking syntax check.

## Enforcement and limits

The branch-name workflow validates pull-request source branches. The promotion
workflow validates that a pull request to `main` originates from `Dev`.
Repository branch protection supplies the actual pull-request, review, status
check, deletion, and force-push controls.

These controls preserve an auditable path but do not make every change safe,
prevent public forks, or replace human review. GitHub administrators may bypass
rules if repository settings permit it. GitHub does not provide a general
branch-protection switch that restricts `main` pull requests by source branch,
so Hecate enforces that rule with a required status check.
