# Branch naming policy

Hecate uses short, lowercase branch names that say what kind of change they
carry. Most pull requests should target the `Dev` branch.

## Format

Use a category, a forward slash, and a concise kebab-case description:

```text
<category>/<short-description>
```

For example, the idea `FEAT: [NEW FEAT]` becomes:

```text
feat/new-feature
```

Branch names must:

- use lowercase ASCII letters and numbers;
- start with one of the categories below;
- use `/` after the category;
- use hyphens between words;
- avoid spaces, colons, brackets, and uppercase letters; and
- remain descriptive without becoming a sentence.

Dots are allowed for version identifiers, such as `release/v1.2.0`. Additional
slash-separated path segments are allowed when they improve clarity, such as
`feat/voice/wake-word`.

## Categories

| Category | Use | Example |
| --- | --- | --- |
| `feat/` | New product behavior or capability | `feat/configurable-name` |
| `fix/` | Bug fixes and regressions | `fix/wake-word-timeout` |
| `docs/` | Documentation-only changes | `docs/knowledge-vault` |
| `chore/` | Maintenance, tooling, and dependency work | `chore/update-linting` |
| `release/` | Release preparation | `release/v1.2.0` |
| `agent/` | Branches created by approved automation | `agent/update-roadmap` |

The `agent/` prefix is reserved for automated tooling. Human-authored changes
should use the category that best describes the work.

## Pull request targets

- Feature, fix, documentation, and maintenance pull requests should target
  `Dev`.
- Do not target `main` for routine development work.
- Release and promotion mechanics are not yet defined; document that process
  before relying on a different target.

## Enforcement

The [branch-name workflow](../.github/workflows/branch-name.yml) checks every
pull request head branch against this policy. A mismatch produces a failing
GitHub Actions check with the accepted format.

The workflow reports policy violations, but it blocks merging only if repository
settings require the `Branch name` check. This repository does not claim that a
server-side branch protection rule is configured.
