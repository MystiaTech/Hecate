# Local data boundary

This document defines a reusable Step 0.1 layout for Windows with WSL2. It is a
local deployment convention, not an implemented Hecate runtime feature.

## Path template

Choose values for `<username>`, `<distro>`, and `<projects-directory>` on each
workstation. Do not commit the resolved personal paths.

| Purpose | Generic path |
| --- | --- |
| Windows Git checkout | `C:\<projects-directory>\Hecate` |
| Same checkout from WSL2 | `/mnt/c/<projects-directory>/Hecate` |
| WSL2 project area | `/home/<username>/<projects-directory>` |
| Local Obsidian vault | `/home/<username>/<projects-directory>/Hecate/knowledge-vault` |
| Vault from Windows | `\\wsl.localhost\<distro>\home\<username>\<projects-directory>\Hecate\knowledge-vault` |

The local Obsidian vault should be a WSL-native copy of the approved Markdown
template, not a link to the complete Git checkout. This keeps repository
internals and future runtime data outside the notes Obsidian can index.

## Access boundary

Copy only these template items into the local vault:

- `vault/README.md` as `README.md`;
- `vault/ROADMAP.md` as `ROADMAP.md`; and
- `vault/knowledge/` as `knowledge/`.

Do not put configuration, state, logs, models, cache files, diagnostics,
credentials, lock codes, camera tokens, API keys, or other secrets inside the
local vault.

No private runtime path is selected by this template. Its location,
permissions, retention rules, and backup behavior must be chosen separately
before runtime data exists, and it must remain outside the Obsidian-visible
path.

## Fork initialization

1. Choose a WSL-native local vault path outside the repository checkout.
2. Copy only the three approved template items listed above.
3. Open the copied directory in Obsidian.
4. Add non-sensitive notes, keeping personal household data local and
   uncommitted.
5. Review any backup or synchronization destination before enabling it.

For an unused empty vault, reset by making a fresh copy from the template. Once
personal notes exist, back up the vault and compare template changes manually;
never overwrite the entire local vault during a repository update.

There is no automatic synchronization between the repository template and a
local vault. This prevents local notes from being silently committed and
template updates from overwriting personal data.
