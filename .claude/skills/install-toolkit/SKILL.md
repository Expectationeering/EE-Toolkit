---
name: install-toolkit
description: >-
  One-time environment setup for the EE-Toolkit: install uv and pandoc, create
  the Python environment with uv sync, and verify docx/pandoc tooling works.
  Use when the user types "install toolkit", "set up the toolkit", or "setup".
---

# Install toolkit

Two tools and one environment: **uv** (runs the scripts), **pandoc** (reads the Word inputs), and `.venv` via `uv sync`. On Windows the only real failure mode is a stale `PATH` in the running session — never a needed reboot.

**Windows first — refresh PATH before every command in this procedure, including the step-1 checks.** winget writes `PATH` to the registry; the running session never sees it. Prefix every command below with:

```
$env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User'); <command>
```

(execute-flow uses this same prefix at run time.)

| If you catch yourself thinking | Reality | Do instead |
|---|---|---|
| "`uv` is not recognized, so the install failed" | winget succeeded; this session's PATH is stale | re-run with the refresh prefix before concluding anything |
| "I'll tell the user to restart the terminal" | a restart is never needed here | use the prefix |
| "the prefix is noise, I'll drop it for this one command" | every uv/pandoc call in this session needs it | prefix every command |

1. Check with `uv --version` and `pandoc --version` (with the Windows prefix); install only what is missing:

   | OS | uv | pandoc |
   |---|---|---|
   | Windows | `winget install astral-sh.uv` | `winget install JohnMacFarlane.Pandoc` |
   | macOS | `brew install uv` | `brew install pandoc` |
   | Linux | `curl -LsSf https://astral.sh/uv/install.sh \| sh` | `sudo apt install pandoc` (or `dnf install pandoc`) |

2. Run `uv sync` to create the environment and install the pinned Python dependencies.
3. Verify all three: (a) `uv run python -c "import docx, lxml; print('ok')"` prints `ok`; (b) `pandoc --version` prints a version line; (c) `.venv/Scripts/python.exe` (Windows) or `.venv/bin/python` exists — execute-flow calls it directly for trace-check. If a check fails, re-run it with the PATH prefix before re-installing anything; if it still fails, report the failing command and its full output and stop — do not add or change dependencies (they are pinned).
4. **Report completion** with exactly these four lines: (a) uv `<version>` and pandoc `<version>` installed or already present; (b) environment created at `.venv` by `uv sync`; (c) verification: `import docx, lxml` → ok; (d) next step: no terminal restart needed — run `Execute flows/ee-flow` now.
