# Hecate

Hecate is a planned local-first home voice assistant. The project aims to keep
everyday interactions on hardware you control while leaving room for a tightly
limited, optional cloud fallback.

> [!IMPORTANT]
> Hecate is currently in the pre-implementation stage. This repository does not
> yet contain an application, installation process, dependency manifest, or
> runnable release. Everything under [Roadmap](#roadmap) describes intended
> direction, not functionality available today.

## Project status

The repository currently contains project metadata only:

- this README;
- an Apache License 2.0 file; and
- a general-purpose `.gitignore`.

No language, runtime, speech engine, model, automation platform, or hardware
integration has been selected in the repository. Setup and usage instructions
will be added after those decisions are represented by working code.

## Goals

- **Local first:** Prefer on-device processing for privacy, resilience, and
  control.
- **Voice native:** Treat wake-word operation as a foundational requirement,
  not a later add-on.
- **Personal:** Allow the assistant's spoken name to be configured.
- **Proportionate compute:** Route requests to the least costly capable path.
- **Bounded cloud use:** Make remote processing optional and enforce a strict
  spending limit.
- **Safe by design:** Require clear permissions and confirmation for sensitive
  home actions.
- **Portable:** Begin on Windows through WSL2 without closing the door to a
  later Linux or headless deployment.

## Roadmap

The items in this section are planned and are **not implemented**.

### Phase 1: voice foundation on Windows

- Target development on a Windows laptop using WSL2.
- Maintain Windows compatibility as the project evolves.
- Support wake-word activation from the first functional version.
- Make the assistant name configurable rather than hard-coded.
- Establish clear local configuration and data boundaries.

### Phase 2: tiered request routing

Route each request according to its complexity and resource needs:

1. Send deterministic or simple tasks to CPU-based tools.
2. Send routine reasoning and reminder requests to a small local model.
3. Send deeper requests to a larger local model running on a GPU.
4. When explicitly enabled, allow OpenRouter as a cloud fallback with a hard
   daily budget of **$3 USD**.

The concrete tools, models, routing rules, and budget-enforcement mechanism are
still to be designed and selected.

### Phase 3: deployment portability

- Support migration from the initial Windows/WSL2 environment to Linux.
- Support unattended operation on a headless home server.
- Preserve configuration portability and local-first behavior across hosts.

### Phase 4: carefully scoped home automation

- Explore home integrations, potentially including locks and cameras.
- Define explicit permission boundaries for devices, users, and actions.
- Require confirmation before security-sensitive or privacy-sensitive actions.
- Prefer deny-by-default behavior when identity, intent, or authorization is
  uncertain.

## Safety and privacy direction

Local-first does not by itself guarantee privacy or safety. Before Hecate gains
access to home devices or remote services, the project intends to define:

- what data may leave the local machine;
- how cloud fallback is enabled, disabled, and visibly reported;
- how the daily cloud budget fails closed when exhausted;
- which actions always require explicit confirmation; and
- how credentials, recordings, logs, and permissions are stored and revoked.

These are design requirements for future implementation, not current security
claims.

## Contributing

The project is not yet ready for implementation-specific contribution guidance.
Until the initial architecture and development workflow are committed, proposed
changes should avoid assuming a language, framework, model, or service that the
repository has not selected.

When code is introduced, this README should be updated alongside it so that
status, setup, usage, tests, configuration, and limitations remain accurate.

## License

Hecate is licensed under the [Apache License 2.0](LICENSE).
