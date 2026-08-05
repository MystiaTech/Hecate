# Step Zero exit gates

Step Zero turns product direction into testable local contracts. A numbered
step must not be marked complete, and work must not be promoted beyond it, until
its repository issue has every acceptance item checked and public-safe evidence
has been reviewed. Documentation alone never completes a gate.

GitHub stores public-safe planning and aggregate results only. Raw audio,
transcripts, biometric artifacts, household details, credentials, private logs,
device identifiers, and resolved local paths remain local and uncommitted.

## Step 0.0: governance and traceability

The foundation gate requires reviewed, maintainable records for:

- a concise charter covering mission, local-first boundary, intended users,
  non-goals, and measurable success;
- Definition of Ready and Definition of Done;
- architecture decision record structure and template;
- release, versioning, changelog, deprecation, compatibility, and rollback policy;
- security reporting, risk exceptions, and a lightweight threat model and data
  classification;
- test-evidence and reproducible development/environment expectations;
- ownership, review, code ownership, maintenance, and incident responsibilities;
- the GitHub-versus-local household-data boundary;
- issue-to-PR-to-release traceability and AI-use disclosure;
- open-source licensing, third-party attribution, and model/voice provenance;
  and
- accessibility and household-safety expectations.

The linked issue is the source of truth for exit status. Policies may share one
document when that avoids bureaucracy, but each criterion must remain auditable.

## Step 0.1: local knowledge boundary

The knowledge-boundary gate requires verification that:

- the live vault is WSL-native within the owner's visible projects area and can
  be opened from Windows Obsidian through the WSL filesystem;
- Obsidian-visible knowledge is Markdown-only reference material;
- configuration, state, logs, models, cache, diagnostics, and secrets remain
  outside the vault;
- notes cannot directly control Hecate; and
- the repository contains only a generic, fork-safe template with no household
  or identifying data.

Encrypted local backups are the recommended onboarding default with an explicit
opt-out. No backup is created until an authorized household administrator
confirms both a destination and recovery method. No cloud destination, upload,
or external transmission is enabled by default. The system must verify backup
encryption and a restoration test before reporting success, and clearly explain
lost-key and recovery consequences.

## Step 0.2: voice-stack validation

The voice-stack gate requires reproducible evidence for:

- a per-component/model provenance and license manifest; production-default
  engines and bundled models/voices must be freely redistributable and
  commercially usable without per-user fees;
- a complete offline voice loop with network access disabled;
- fully local CPU detection of the primary phrase `Hey Hecate`, with a
  push-to-talk fallback;
- accuracy-first local English speech recognition for Hecate and core terms;
- child-friendly supported wake-phrase reliability and false-activation tests
  using consented local child/adult samples;
- bounded audio queues with visible overflow and recovery behavior;
- natural, responsive local TTS on the CPU fallback path;
- local neutral-phrase speaker enrollment: adult profiles require explicit
  consent initiated by an authorized household administrator, and child
  profiles require caregiver authorization;
- immediate authorized suspension, revocation, and confirmed deletion of child
  profiles, with fresh caregiver authorization required for re-enrollment;
- an explicit ban on speaker identity as sensitive-action authorization;
- pre-rendered common phrases instead of training a voice model; and
- aggregate accuracy, latency, memory, CPU/GPU, and false-activation results.

A shorter configurable alias may be enabled only after it passes the same
license, reliability, and false-activation benchmark as the primary phrase.
Noncommercial or otherwise restricted assets may be clearly labeled optional
experiments only; they cannot be bundled by default, required for core operation,
or block a fully functional free path for users and forks.

## Step 0.3: hardware and power validation

The development baseline is an Intel Core Ultra 9 275HX, an NVIDIA RTX 5070 Ti
Laptop GPU, 32 GB RAM, and 410 GB free storage. This records the agreed test
baseline, not a minimum system requirement or endorsement.

The gate requires reproducible evidence for:

- WSL2/NVIDIA driver/CUDA GPU visibility and reliable default microphone and
  speaker behavior;
- responsive CPU wake and audio processing during representative GPU load;
- safe measured temperature and resource ceilings for AC-powered operation;
- controlled low-memory and low-storage degradation with clear status;
- compact starter and recommended storage tiers for the selected voice stack;
- AC-only full operation; battery transition stops wake listening, unloads
  heavy models, and never silently enables cloud fallback;
- health checks before resuming after AC returns;
- a future local, always-on, UPS-backed Linux/headless server role; and
- NPU use remaining optional, not a first-release dependency.

Storage tier sizes and safe thermal limits remain unresolved until the selected
stack and applicable hardware guidance can be measured.

## Step 0.4: configuration, secrets, and setup safety

The configuration gate requires reviewed implementations and tests for:

- a versioned YAML schema with safe defaults and a fork-safe example;
- development-only `.env` support excluded from Git, logs, status, and vaults;
- an optional encrypted secrets store using both an OS-protected local key for
  normal operation and a user-held recovery key, with no cloud key escrow;
- an optional, standards-compatible hardware-security-key factor that is
  explicitly enrolled, removable, revocable, and vendor-neutral, with clear
  lost-key and recovery behavior;
- a friendly setup flow, plain-language errors, and explicit reload/restart
  semantics;
- a first-run wizard that defaults to fully local-only operation with every
  cloud fallback disabled; cloud providers, budgets, and related security
  controls appear only in a separate, deliberately entered advanced path;
- explicit creation or selection of the first household administrator during
  setup, never silently inferred from the installing OS, root, or service
  account; the service identity remains separate and least-privileged;
- multiple household administrators, with authorized addition/removal and a
  safeguard against removing the final usable administrator;
- an explicitly configured recovery-only mechanism that can reset only the
  designated primary-admin credential, has no interactive login or routine
  permissions, ships with no default secret, and uses protected recovery
  material with local confirmation, rate limiting, audit, and lost-key guidance;
- authorized administrator approval plus a full service restart for any change
  that can materially affect operation, privacy, security, data handling, cloud
  fallback, secrets or key factors, integrations, profiles, or permissions;
- optional live reload only for low-risk cosmetic and ordinary UI preferences,
  with invalid changes rejected before activation and the current running
  configuration left undisturbed;
- local-only behavior by default, including a reliable cloud-fallback disable;
- unit, integration, security, and privacy evidence; and
- an optional HIPAA-readiness review only for enabled compliance-oriented
  deployments that may handle regulated ePHI.

Hecate must not claim HIPAA compliance. The optional review records risk,
access-control, audit, retention, encryption, backup/recovery, and cloud/BAA
considerations; it is not a generic blocker for every push.

## Step 0.5: household permissions and action safety

Hecate defaults to read-only and advisory behavior. Changing a physical home
device or external account requires explicit, contextual confirmation unless an
authorized household administrator has created a narrowly scoped, auditable
automation rule. Every rule names allowed action, allowed target(s), conditions
or schedule, and revocation or expiry; broad or hidden authority is prohibited.
Speaker identity is convenience context, never sensitive-action authorization.

Version-one automation is limited to low-impact controls. A direct, unambiguous
request may immediately change an approved named light without redundant
confirmation. A requested contextual lighting rule and an administrator-created
scheduled watering rule require clear preview and confirmation before creation,
then may execute exactly as stated. Rules require target disambiguation,
revocation/expiry, disabled-state visibility, local audit, and safe failure.
Hecate cannot infer, broaden, or retarget a rule. Watering cannot make autonomous
weather/model decisions in version one. Locks, cameras, purchases, permissions,
and account changes are excluded from automation.

Children and guests may use only approved direct low-impact controls allowed by
their profile. Only household administrators may create, change, enable,
disable, or delete schedules and automation rules, and may revoke child/guest
access. Unrecognized or ambiguous speakers fail safely; voice recognition never
grants action permission or high-impact authority.

The gate requires implementation and tests for:

- distinct notification, advisory/read-only, proposed-action, confirmed-action,
  and automation-rule permission classes;
- confirmation bound to a stated action, target, material effect, and expiry,
  with safe denial, cancellation, replay prevention, and failure behavior;
- stronger authorized-administrator approval for high-impact actions; Hecate
  never independently chooses such an action, and schedules/rules do not bypass
  confirmation without a later separate, test-gated safety design;
- local-first permission evaluation, minimized audit, immediate revocation, and
  fail-closed handling of ambiguous, stale, corrupt, or unavailable authority;
- local, administrator-visible, privacy-minimized activity history attributing
  every state change to a direct request, explicit confirmation, or named rule;
- rolling local history retention of 90 days by default, with bounded disk use,
  encrypted backup/protected export, no automatic cloud upload, and authorized
  administrator control of retention/export under the material-change boundary;
- brief, plain-language refusals and failure explanations with a safe next step,
  no blame or protected detail, plus an accessible non-voice status path;
- proactive reminders and package/delivery notices governed by transparent,
  revocable routing, cadence, rate-limit, and quiet-hours preferences; and
- optional severe-weather monitoring through an explicitly enabled external
  source, with source freshness and availability visible where practical.

Source-backed severe-weather alerts bypass quiet hours by default. Routine
notices and non-urgent forecasts remain quiet-hours aware unless an authorized
administrator narrowly elevates a transparent, revocable category. Weather is
not fully offline, emergency-grade, guaranteed, or a substitute for official
alerts and instructions; Hecate must not invent urgency or issue evacuation
instructions.

If enabled severe-weather coverage becomes stale or unavailable, Hecate must
announce the loss without panic or false authority, neutrally direct people to
official alert channels, use configurable non-spammy retry/notification behavior,
and announce verified recovery. The severe-alert quiet-hours bypass also applies
to this loss-of-coverage state. Local core behavior remains available throughout.

Source-backed severe alerts repeat at a controlled cadence until a household
member acknowledges hearing them; acknowledgement does not resolve the alert,
which remains visible and reannounces on source update or escalation. When the
source supplies an explicit deadline, first-run setup defaults to a 50-minute
preparation reminder that an authorized administrator may change or disable.
This is source-deadline arithmetic only: Hecate never calculates travel or safe-
distance time, infers clearance, or gives evacuation/shelter instructions.

Any unresolved safety, offline, audio, data-integrity, privacy, or power failure
keeps its gate open. Non-gating improvements may move to follow-up issues only
after review.
