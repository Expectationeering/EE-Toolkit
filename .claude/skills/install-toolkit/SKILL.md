---
name: install-toolkit
description: >-
  One-time environment setup for the EE-Toolkit: install uv and pandoc, create
  the Python environment with uv sync, and verify docx/pandoc tooling works.
  Use when the user types "install toolkit", "set up the toolkit", or "setup".
---

# Install toolkit

Perform a one-time environment setup, then tell the user they're ready to run a flow:

1. Check whether **uv** and **pandoc** are installed; install any that are missing using the right installer for the operating system:
   - Windows: `winget install astral-sh.uv`, `winget install JohnMacFarlane.Pandoc`
   - macOS: `brew install uv pandoc`
   - Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh` for uv, plus `pandoc` from the package manager
2. **Windows — use just-installed tools without a terminal restart.** winget updates `PATH` in the registry, but the already-running session does not see it. So run every command that uses `uv`/`pandoc` in PowerShell, prefixed with a registry PATH refresh:
   ```
   $env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User'); <command>
   ```
3. Run `uv sync` (with the prefix on Windows) to create the environment and install the pinned Python dependencies.
4. Verify (with the prefix on Windows): `uv run python -c "import docx, lxml; print('ok')"` and `pandoc --version`.
5. Confirm the user is ready — **no terminal restart is needed**; a flow can be run immediately.
