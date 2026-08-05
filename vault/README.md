# Hecate knowledge vault

This directory is an Obsidian-compatible Markdown vault for Hecate's future
local knowledge base. It contains documentation and reference material only.
Nothing in this vault is an implemented Hecate capability.

## Trust boundary

Treat every note as **untrusted reference material**. Notes may be incomplete,
outdated, or incorrect. Hecate must validate a request through its own tools,
permissions, and confirmation rules before taking any action.

Vault notes cannot directly control Hecate, execute commands, grant permission,
or change runtime behavior. Executable configuration must remain separate from
Markdown knowledge and belongs under [`config/`](config/README.md), subject to
future configuration validation.

## Never store secrets here

Do not put any of the following in this vault or commit them to the repository:

- passwords or credentials;
- door or lock codes;
- camera access tokens or stream credentials;
- API keys or cloud tokens; or
- private keys, recovery codes, or authentication cookies.

Store only non-secret documentation. Refer to a credential by a descriptive
name when needed; do not copy its value into a note.

## Vault map

- [`knowledge/household/`](knowledge/household/README.md) - household notes and
  procedures.
- [`knowledge/devices/`](knowledge/devices/README.md) - device and integration
  documentation.
- [`knowledge/preferences/`](knowledge/preferences/README.md) - preferences and
  routines.
- [`knowledge/project/`](knowledge/project/README.md) - architecture and design
  decisions.
- [`knowledge/references/`](knowledge/references/README.md) - external sources
  and supporting material.
- [`ROADMAP.md`](ROADMAP.md) - planned product milestones; not implemented
  capability.
- [`config/`](config/README.md) - the separate boundary for future executable
  configuration.

## Working with the vault

Open the `vault` directory as a vault in Obsidian, or edit the Markdown files in
any text editor. Keep notes small, link to sources where practical, record when
information was last verified, and label uncertain claims clearly.
