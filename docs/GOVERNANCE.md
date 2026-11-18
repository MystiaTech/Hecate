# Governance foundation

This document is Hecate's public-safe Step 0.0 contract. It governs planning and
review; it does not claim that roadmap capabilities are implemented.

## Charter

Hecate's mission is to become a calm, local-first home voice assistant whose
name, permissions, and optional cloud use remain under household control. It is
intended for people who value private, understandable local operation.

Non-goals for the initial release are unattended security-sensitive actions,
cloud-required operation, medical or emergency-service guarantees, regulatory
compliance claims, and replacing professional judgment. Success means the
agreed offline, privacy, usability, safety, compatibility, and resource gates
pass with reproducible public-safe evidence.

## Ready and Done

Work is Ready when its outcome, scope, privacy impact, dependencies, acceptance
checks, test plan, owner, and roadmap link are clear. Work is Done only after
implementation and documentation agree; required checks and review pass; test
evidence and AI use are disclosed; licenses and provenance are recorded; and
remaining risks, compatibility effects, and rollback steps are explicit.

## Decisions and traceability

Significant, durable choices use an architecture decision record in
[`docs/decisions`](decisions/0000-template.md). Number files sequentially,
review them by pull request, and supersede rather than silently rewrite accepted
decisions. Issues define outcomes and gates; pull requests link issues and
evidence; release notes link shipped pull requests, migrations, and rollback.

## Releases, support, and reproducibility

`Dev` is integration and `main` is production-ready release history. A release
must declare its version, supported platforms, known limitations, changelog,
upgrade/deprecation impact, and tested rollback. Until that declaration exists,
no production support promise applies.

Development and test evidence must record source revision, sanitized platform
and hardware class, tool/runtime versions, inputs or synthetic fixtures, exact
commands, expected result, and observed result. Dependency locks or equivalent
reproducible records must accompany dependencies once a build stack exists; this
policy does not select one prematurely.

## Licensing and provenance

Every third-party library, engine, model, model weight, voice, dataset, and
generated asset must record its name, version or digest, source, license,
attribution requirement, intended use, redistribution limits, and reviewer.
Unknown or incompatible provenance blocks release. Consent and lawful use are
required; Hecate does not train a household member's voice by default.

## Threat model and data classification

Review trust boundaries among microphones, local processes, models, the vault,
home integrations, backups, and optional external services. Record assets,
actors, entry points, misuse cases, mitigations, residual risk, and owner.

Classify data as:

- **Public:** safe for the repository and project;
- **Local private:** household notes, preferences, recordings, transcripts,
  device metadata, diagnostics, and backups; never committed;
- **Secret:** credentials, tokens, keys, lock codes, and recovery material;
  encrypted and never placed in notes or logs; or
- **Regulated:** data subject to deployment-specific legal controls; excluded
  from GitHub and allowed only under an explicitly reviewed profile.

Exceptions must identify scope, risk, owner, expiry, mitigation, and removal
plan. They cannot silently weaken local-only, confirmation, or data boundaries.

## Accessibility and household safety

Critical information must not rely on voice alone. Provide understandable text
or visual status and an accessible manual fallback where practical. Avoid
stereotypes, shame, and age-dependent assumptions. Security-sensitive actions
require scoped permission and explicit confirmation; speaker identity alone is
never authorization. Ambiguity, component failure, or loss of connectivity must
fail safely and visibly.

## Ownership, incidents, and rollback

CODEOWNERS identifies review ownership. Maintainers triage reports, assign an
incident owner, preserve public-safe evidence, contain impact, communicate known
limitations, and decide remediation or rollback. Every release-changing pull
request must identify a rollback path. Post-incident learning belongs in a
sanitized issue or decision record; household data and exploit details stay in
the appropriate private channel.
