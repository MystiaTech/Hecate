# GitHub planning boundary

GitHub is Hecate's public planning and repository-automation space. It is
**never a home-data store**.

## Keep GitHub public-safe

Issues, pull requests, Projects, Actions output, and committed files must not
contain:

- household notes, addresses, schedules, or personal preferences;
- voice recordings, transcripts, private prompts, or camera media;
- device names, identifiers, private network details, or access history;
- credentials, tokens, lock codes, API keys, or private logs; or
- resolved usernames, hostnames, or identifying local paths.

Use public facts, synthetic examples, and generic placeholders. Keep personal
knowledge in the local Obsidian vault and private runtime data outside Git.

## Issue intake

Repository issue forms cover four kinds of work:

- features;
- bugs;
- research and benchmarks; and
- documentation and policy.

Each form includes a public-data reminder and gathers only the context needed
to plan the work. Blank issues are disabled to keep intake consistent.

## Labels

Labels use three small dimensions:

- priority: `priority:critical`, `priority:high`, `priority:medium`, or
  `priority:low`;
- area: `area:voice`, `area:local-runtime`, `area:integrations`,
  `area:privacy`, or `area:docs`; and
- state: `state:backlog`, `state:ready`, `state:in-progress`, or
  `state:blocked`.

Existing GitHub labels such as `bug`, `enhancement`, and `documentation` remain
the issue type. `type:research` identifies investigation and benchmark work.

## Milestones

Milestones provide the high-level delivery map without inventing dates:

1. **Step Zero** - contracts, boundaries, repository policy, and foundations.
2. **Local Voice MVP** - the first local wake-word and voice loop.
3. **Core Assistant** - deterministic tools and staged local routing.
4. **Future Integrations** - permission-scoped home integrations and later
   deployment work.

## Project layout

When GitHub Projects access is configured, use one project with these fields:

- `Status`: Backlog, Ready, In progress, Blocked, Done;
- `Priority`: Critical, High, Medium, Low;
- `Area`: Voice, Local runtime, Integrations, Privacy, Docs;
- `Milestone`: the four roadmap milestones; and
- `Target date`: optional and unset until a real commitment exists.

Recommended views:

- **Backlog:** table grouped by milestone, then priority;
- **Board:** board grouped by status; and
- **Roadmap:** roadmap using milestone and target date.

The project mirrors public issue metadata only. Never paste local-vault content
into a project item.

## Cost posture

The documentation workflow is event-driven, dependency-free, and capped at
three minutes. It performs local Markdown, link, required-file, and public-data
boundary checks. It has no schedule, model download, hosted model call, or paid
service dependency.
