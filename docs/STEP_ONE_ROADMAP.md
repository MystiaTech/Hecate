# Step One roadmap: Local Voice MVP

> [!IMPORTANT]
> This is a plan, not an implementation or capability claim. Step One cannot
> begin by bypassing Step Zero, and it cannot be marked complete until its code,
> tests, public-safe evidence, and human review pass.

## Objective and boundary

Step One delivers a small, dependable English-first local voice loop on the
initial Windows/WSL2 laptop target while preserving a later headless path. The
core loop remains offline. Optional network features are excluded unless a step
explicitly identifies and tests them; severe-weather monitoring is a later,
opt-in external integration and is not part of this MVP.

The MVP starts read-only and advisory. Its deterministic command set is narrow.
It does not introduce general home integrations or high-impact automatic actions.
Any approved named-light work remains behind the established permission and
confirmation contracts and is not required for the core voice-loop release.

The hero demonstration also includes one bounded local-AI route. The stable
showcase utterance is “tell me a short riddle,” classified deterministically as
a short creative response. The selected small local model—not canned content—
generates the answer within reviewed prompt, output, resource, and safety limits.
The bounded internal prompt/template is validated, versioned configuration, not
a hard-coded answer, and changes follow the material configuration boundary.
The route is non-sensitive, cannot authorize or invoke an action, is clearly
identified as local AI, and never falls back to cloud. If the local model is
unavailable, Hecate says so plainly while deterministic core commands remain
available. The model remains unselected until its Step Zero license, benchmark,
privacy, and resource gates pass.

## Ordered delivery steps

| Step | Deliverable | Depends on | Not done until |
| --- | --- | --- | --- |
| 1.0 | MVP contract, non-goals, deterministic-plus-bounded-local-AI hero scenario, and Step Zero dependency gate | Step 0.0–0.7 reviewed evidence | Scope, interfaces, risks, public-safe evidence plan, and promotion blockers are approved |
| 1.1 | Runtime skeleton, service lifecycle, YAML configuration loading, and local status/log baseline | 1.0 | Lifecycle, invalid-config, restart, privacy, and failure tests pass without selecting undocumented dependencies |
| 1.2 | Decoupled audio-device interface and push-to-talk diagnostic path across Windows/WSL | 1.1 | Capture/playback selection, disconnect, cancellation, and no-recording-retention tests pass |
| 1.3 | Fully local CPU wake-word path for `Hey Hecate` plus push-to-talk fallback | 1.2 and Step 0.2 evidence | Pre-wake audio safeguards, false-activation, child/adult usability, resource, restart, and optional-alias gates pass |
| 1.4 | Accuracy-first local English STT with silence/turn detection and controlled vocabulary | 1.2; 1.3 for wake integration | Offline accuracy, latency, queue, cancellation, privacy, and safe-transcript-lifecycle tests pass |
| 1.5 | Deterministic request/intent layer for core commands and one bounded local-AI creative route | 1.1 and 1.4; Step 0.2 model gate | Time, status, help, stop/cancel, local-generation provenance, unavailable-model, ambiguity, and no-side-effect tests pass |
| 1.6 | License-approved local TTS with interruption, bounded queueing, and fallback | 1.1 and Step 0.2 evidence; integrates with 1.2 | Voice provenance, naturalness/usability, latency, CPU fallback, ducking, interruption, and queue tests pass |
| 1.7 | End-to-end wake/PTT orchestration and interaction state machine | 1.3–1.6 | Offline happy-path, timeout, cancellation, barge-in, duplicate prevention, failure, restart, and plain-language feedback tests pass |
| 1.8 | Safe first-run onboarding, device selection, health/status, and accessible local troubleshooting | 1.1, 1.2, and 1.7 | Local-only defaults, YAML validation, secret/recovery boundaries, accessibility, and recovery guidance tests pass |
| 1.9 | Reproducible benchmark and integrated acceptance suite | 1.0–1.8 and applicable Step Zero gates | Offline, privacy, license, accuracy/latency, power/resource, fault/restart, and child/adult usability evidence is reviewed |
| 1.10 | Release-readiness and handoff record | 1.9 | Evidence is traceable, critical failures are closed, limitations/deferrals and rollback are documented, and humans sign off |

Each issue is independently pushable but not independently releasable. A step
may land behind disabled or diagnostic-only paths when its exit criteria are not
yet met. No issue closes solely because documentation, a stub, or a happy-path
demo exists.

## Requirements carried into every step

- The core path stays local and usable with network access disabled. Cloud
  fallback remains disabled unless separately and explicitly configured; it is
  never a hidden recovery path.
- `Hey Hecate` is the primary wake phrase and CPU detection is always-on only
  while full service is eligible under the AC-power policy. Push-to-talk remains
  available. An optional alias needs the same license, reliability, and false-
  activation evidence before enablement.
- The audio front end is decoupled from Windows/WSL device details and from later
  headless hosts. Loss of microphone, speaker, GPU, or local model degrades only
  affected features and remains visible.
- STT is local, English-first, and accuracy-led. TTS engine and voice selection
  remains separately license- and benchmark-gated. No model or voice is selected
  by this roadmap.
- One deterministic intent may invoke a selected small local model for a bounded
  harmless creative response. Generation is not canned, is labeled as local AI,
  cannot call tools or change state, and has a truthful deterministic unavailable
  fallback. Its engine/model remains subject to the same provenance, licensing,
  resource, privacy, and benchmark gates.
- Speaker profiles are convenience only. Adult enrollment needs explicit
  consent initiated by an authorized administrator; child enrollment needs
  caregiver authorization. Suspension, revocation, deletion, and fresh consent
  retain their Step Zero rules.
- Normal settings use validated, versioned YAML. First run defaults to local-
  only operation. Secrets, recovery keys, administrator identity, material
  restart requirements, backups, and optional hardware keys retain Step Zero
  boundaries.
- The MVP defaults to read-only/advisory behavior. No high-impact action runs
  automatically. Any later low-impact named-light action or narrow administrator-
  created rule must use the existing authorization, traceability, and failure
  contracts rather than broadening MVP scope.
- Local status and activity history remain privacy-minimized and role-scoped.
  Public evidence contains aggregates and synthetic examples only.

## Public evidence rule

GitHub may contain plans, sanitized configurations, reproducible test
instructions, and aggregate results. It must not contain household information,
locations, names, recordings, transcripts, biometric samples, credentials,
keys, tokens, private logs, device identifiers, hostnames, or resolved local
paths. Protected evidence remains local and is represented publicly only by the
minimum safe result needed for review.

Critical failed or unverified Step Zero or Step One requirements block
promotion. Risk acceptance follows the Step 0.7 time-bounded, owned, reviewed
process and cannot waive a critical local-first, privacy, authorization, action-
safety, licensing, data-integrity, or recovery boundary.
