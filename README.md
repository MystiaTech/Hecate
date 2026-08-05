# Hecate

> A local-first voice assistant for the home, designed to know when to act,
> when to ask, and when to keep the door closed.

Hecate is a planned home voice assistant that keeps everyday interactions on
hardware you control. The name gives the project a useful image: a calm keeper
at the crossroads, choosing the right path for each request and treating every
threshold with care.

That is a design direction, not a claim of magic—or even a working assistant.

> [!IMPORTANT]
> **Hecate is currently in the pre-implementation stage.** This repository does
> not yet contain an application, installation process, dependency manifest, or
> runnable release. Everything under [Roads not yet taken](#roads-not-yet-taken)
> is planned direction, not functionality available today.

## Where Hecate stands today

Right now, Hecate is a map rather than a journey in progress. The repository
contains:

- this project overview;
- a starter [local knowledge vault](vault/README.md) for non-secret reference
  notes;
- an Apache License 2.0 file; and
- a general-purpose `.gitignore`.

There is no application code yet. No language, runtime, speech engine, model,
automation platform, or hardware integration has been selected in the
repository. Setup and usage instructions will arrive only after working code
makes them real.

## The compass

A few principles point the way:

- **Stay local by default.** Prefer on-device processing for privacy,
  resilience, and control.
- **Begin with voice.** Treat wake-word operation as a foundation, not a later
  flourish.
- **Make it personal.** Let people choose the assistant's spoken name rather
  than hard-coding an identity.
- **Use the smallest suitable path.** Reach for deterministic CPU tools before
  models, and smaller local models before larger ones.
- **Put a gate on the cloud.** Keep remote processing optional, visible, and
  strictly budgeted.
- **Ask before crossing a boundary.** Require clear permissions and explicit
  confirmation for sensitive home actions.
- **Travel well.** Start on Windows through WSL2, remain Windows-compatible,
  and leave a clear route to Linux and headless deployment.

## Roads not yet taken

Everything in this section is a **roadmap** and is **not implemented**. The
longer version lives in the [knowledge vault roadmap](vault/ROADMAP.md).

### 1. Light the first lamp: local voice on Windows

- Target development on a Windows laptop using WSL2.
- Maintain Windows compatibility as the project evolves.
- Support wake-word activation from the first functional version.
- Make the assistant name configurable rather than hard-coded.
- Establish clear boundaries between local knowledge, executable
  configuration, and application behavior.

### 2. Choose the path: tiered request routing

The intended routing order is deliberately practical:

1. Send deterministic or simple tasks to CPU-based tools.
2. Send routine reasoning and reminder requests to a small local model.
3. Send deeper requests to a larger local model running on a GPU.
4. When explicitly enabled, allow OpenRouter as a cloud fallback with a hard
   daily budget of **$3 USD**.

The concrete tools, models, routing rules, and budget-enforcement mechanism are
still to be designed and selected. Until code and tests exist, none of these
paths should be read as available.

### 3. Carry the lantern: deployment portability

- Support migration from the initial Windows/WSL2 environment to Linux.
- Support unattended operation on a headless home server.
- Preserve configuration portability and local-first behavior across hosts.

### 4. Guard the threshold: carefully scoped home automation

- Explore home integrations, potentially including locks and cameras.
- Define explicit permission boundaries for devices, people, and actions.
- Require confirmation before security-sensitive or privacy-sensitive actions.
- Deny by default when identity, intent, or authorization is uncertain.

## Guardrails at the door

Local-first is a direction, not a security guarantee. Before Hecate gains access
to home devices or remote services, the project intends to define:

- what data may leave the local machine;
- how cloud fallback is enabled, disabled, and clearly reported;
- how the daily cloud budget fails closed when exhausted;
- which actions always require explicit confirmation; and
- how credentials, recordings, logs, and permissions are stored and revoked.

The knowledge vault is untrusted reference material. It cannot directly control
Hecate, grant permission, or execute actions, and it must never contain
credentials, lock codes, camera tokens, API keys, or other secrets.

These are requirements for future implementation, not claims about security
features available today.

## Joining the journey

Hecate is not yet ready for implementation-specific contribution guidance.
Until an initial architecture and development workflow are committed, proposed
changes should avoid assuming a language, framework, model, or service that the
repository has not selected.

When code arrives, its documentation should arrive with it. Status, setup,
usage, tests, configuration, limitations, and safety boundaries all belong in
the same change that makes a capability real.

## License

Hecate is licensed under the [Apache License 2.0](LICENSE).
