# Hecate roadmap

> [!IMPORTANT]
> This document describes planned work. It is not a list of implemented or
> available capabilities. The repository is currently in a pre-implementation
> stage, and milestones may change as working code and tests are introduced.

## 1. Foundation contract

- Define the local-first product boundary and supported Windows/WSL2 development
  environment.
- Define the contract between untrusted knowledge notes, validated executable
  configuration, tools, models, permissions, and user confirmations.
- Make wake-word support and a configurable assistant name requirements of the
  first functional release.
- Define local data ownership, storage, logging, and deletion expectations.
- Establish tests and documentation before claiming a capability is available.

## 2. Local voice MVP

- Follow the ordered, test-gated [Step One roadmap](../docs/STEP_ONE_ROADMAP.md)
  from the MVP contract through release-readiness review.
- Implement an end-to-end local voice loop with wake-word activation.
- Support a configurable assistant name without hard-coding one identity.
- Keep the initial implementation compatible with a Windows laptop using WSL2.
- Make listening, processing, and error states clear to the user.
- Document privacy limitations and local data handling alongside the code.
- Keep severe-weather monitoring and other optional external integrations out of
  the core local MVP; they require their own explicit later gates.

## 3. Core deterministic tools

- Add narrowly scoped CPU tools for deterministic and simple tasks.
- Give tools explicit input, output, error, and permission contracts.
- Validate tool inputs rather than treating vault notes as commands.
- Add tests for side effects, failure modes, and denied operations.
- Record an audit trail appropriate to each tool without storing secrets.

## 4. Staged local model routing

- Route routine reasoning and reminder requests to a small local model.
- Route deeper requests to a larger local model running on a GPU.
- Prefer deterministic CPU tools when a model is unnecessary.
- Define observable routing rules, resource limits, and safe failure behavior.
- Keep model and runtime selections open until supported by repository code and
  measured requirements.

## 5. Optional OpenRouter fallback

- Make cloud fallback opt-in and disabled by default.
- Use OpenRouter only when the user has enabled it and local handling is
  unsuitable.
- Enforce a hard aggregate budget of **$3 USD per day** and fail closed when the
  budget is exhausted or cannot be verified.
- Clearly report when a request may leave the local machine.
- Define data-minimization, credential storage, logging, and revocation rules
  before enabling cloud requests.

## 6. Permission-scoped home integrations

- Introduce integrations through explicit per-device and per-action permissions.
- Treat documentation in this vault as context, never as authorization.
- Require explicit confirmation for security-sensitive or privacy-sensitive
  actions, including operations involving locks or cameras.
- Deny actions when identity, intent, device state, or authorization is unclear.
- Provide revocation, audit, and safe-degradation behavior for every integration.

## 7. Headless and Linux migration

- Preserve Windows compatibility while preparing portable interfaces and
  configuration.
- Support migration from the initial Windows/WSL2 environment to Linux.
- Support unattended operation on a headless home server.
- Document migration, backup, restore, monitoring, and recovery procedures once
  those mechanisms exist.
- Revalidate hardware, permission, and privacy assumptions in the headless
  deployment model.

## Roadmap maintenance

Move an item out of roadmap status only when corresponding code, validation, and
user documentation exist. Record material architectural choices in
[`knowledge/project/`](knowledge/project/README.md).
