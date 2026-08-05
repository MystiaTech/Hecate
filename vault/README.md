# Hecate knowledge vault

This directory is an Obsidian-compatible Markdown vault for Hecate's future
local knowledge base. It contains documentation and reference material only.
Nothing in this vault is an implemented Hecate capability.

## Trust boundary

Treat every note as **untrusted reference material**. Notes may be incomplete,
outdated, or incorrect. Hecate must validate a request through its own tools,
permissions, and confirmation rules before taking any action.

Vault notes cannot directly control Hecate, execute commands, grant permission,
or change runtime behavior. Executable configuration and all private runtime
data must remain outside the Obsidian-visible vault. No runtime location or
configuration format is selected by this template.

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

## Working with the vault

Open only the deployed `knowledge-vault` directory in Obsidian, or edit its
Markdown files in any text editor. Keep notes small, link to sources where
practical, record when information was last verified, and label uncertain
claims clearly.

## Start from a fork

1. Keep this repository directory as the non-secret template.
2. Choose a local vault location outside the Git checkout, such as
   `/home/<username>/<projects-directory>/Hecate/knowledge-vault`.
3. Copy only `README.md`, `ROADMAP.md`, and `knowledge/` into that location.
4. Open the copied `knowledge-vault` folder in Obsidian.
5. Add only non-sensitive starter notes. Keep personal household details local
   and uncommitted.

First-use check:

- [ ] The deployed vault is outside the repository checkout.
- [ ] No credentials, codes, tokens, or private keys are present.
- [ ] No config, state, logs, models, cache, or diagnostics are inside it.
- [ ] Any sync or backup destination has been reviewed for privacy.

If the deployed vault is still empty, reset it by making a fresh copy from the
template. After personal notes exist, never replace the whole vault; back it up
and compare template changes file by file.
