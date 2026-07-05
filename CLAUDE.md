# EEToolkit — Claude Project Instructions

## Collaboration Rules
- Terminal commands may run without asking for confirmation (the environment is configured for unattended runs). Still avoid destructive commands (e.g. deleting or overwriting files you did not create) unless the user asked for them.
- Do not install dependencies unless the user explicitly requests it.
- Do exactly what the user asked, and nothing more.
- Offer extra improvements only as optional questions, never as automatic work.
- If a request is ambiguous, ask one concise blocking question before editing.
- Before edits, state exactly what will be changed and which files will be touched.
- After edits, report only what changed and confirm no extra files were modified.
- When running a flow, show progress as a live Update Todos list (one item per phase, kept up to date as work proceeds). Do not open the run by printing the full flow overview / step table.

---

## Agent Registry

Each agent is defined as a standalone character in `.claude/agents/`. Agents have no dependencies on each other or on any workflow document. They are invoked by the orchestration procedure (see `## Orchestration`) based on the task at hand. There is no separate orchestrator agent — the main assistant orchestrates flows directly per that procedure.

**Specialists**

| Agent | File | Role |
|---|---|---|
| User Stakeholder | [.claude/agents/user-stakeholder.md](.claude/agents/user-stakeholder.md) | End-user voice, user goals, pain mapping, usage context |
| Customer Stakeholder | [.claude/agents/customer-stakeholder.md](.claude/agents/customer-stakeholder.md) | Buyer voice, procurement criteria, business value, market expectations |
| Business Stakeholder | [.claude/agents/business-stakeholder.md](.claude/agents/business-stakeholder.md) | Legal manufacturer voice, internal departments, organisational constraints, liability |
| Regulatory Stakeholder | [.claude/agents/regulatory-stakeholder.md](.claude/agents/regulatory-stakeholder.md) | Government & authority voice, market access criteria, compliance obligations, approval readiness |
| System Architect | [.claude/agents/system-architect.md](.claude/agents/system-architect.md) | System decomposition, interface definition, design derivation |
| Usability Validation | [.claude/agents/usability-validation.md](.claude/agents/usability-validation.md) | Use scenarios, UFMEA, safety interaction review, UX/UI design |
| Product Owner | [.claude/agents/product-owner.md](.claude/agents/product-owner.md) | Need consolidation, value translation, traceability authoring, BDD feature files, acceptance criteria, backlog shaping, release gates |
| Development Lead | [.claude/agents/development-lead.md](.claude/agents/development-lead.md) | Implementability review, technical specs, feasibility, architecture compliance |
| Verification Lead | [.claude/agents/verification-lead.md](.claude/agents/verification-lead.md) | Verification strategy, coverage matrix, evidence review, readiness call |
| Quality Assurance | [.claude/agents/quality-assurance.md](.claude/agents/quality-assurance.md) | INCOSE requirements quality evaluation, defect identification, comparative verdict |

---

## Project Structure

```
EEToolkit/
├── CLAUDE.md                              # project instructions and orchestration rules
├── inputs/                                # input documents — shared by all flows, never duplicated
├── flows/                                 # one folder per flow: flow.md + flow-specific templates
└── outputs/                               # reports and workbooks written after each run (one dated folder per run)
```

## Setup

**To install the toolkit:**
```
install toolkit
```

When the user types `install toolkit` (or "set up the toolkit", "setup"), perform a one-time environment setup, then tell them they're ready to run a flow:

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

## Orchestration

You — the main assistant — orchestrate flows directly; there is no separate orchestrator agent. You drive the specialist agents step by step, accumulate their output into one live workbook, and show progress with a todo list. The specialist agents author the content; you sequence them and assemble the workbook.

### Execute a flow — produce a workbook

**To execute a flow:**
```
Execute flows/<name>
```

**Accepted start commands.** Treat all of the following as a request to execute the matching flow under `flows/`. Match loosely: ignore case, the `-flow` suffix, and filler words like "start", "run", "the". For the expectationeering flow, any of these work:
- `Execute flows/expectationeering-flow`
- `start expectationeering`
- `run expectationeering`
- `start the expectationeering flow`
- `expectationeering`

### Procedure

**Always show progress with a todo list.** Before loading anything, call `TodoWrite` to create a progress checklist and keep it updated throughout — the user relies on it to follow progress live. Create one item per phase (or per step) covering the flow's `## Steps`, plus `Ingest input documents`, `Quality Assurance audit`, `Convert to .docx`, and `Write run statistics`. Keep exactly one item `in_progress`; mark it `completed` the moment that step's output is written to the workbook. Do not open a run by printing the full step table — the todo list is the progress view.

**1. Load all inputs.** Ingest input documents first. For each `<name>.docx` in `inputs/`, convert it to a markdown sibling with pandoc and use the markdown — never the `.docx`. On Windows, run pandoc in PowerShell prefixed with a registry PATH refresh:
```
$env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User'); pandoc "inputs/<name>.docx" -o "inputs/<name>.md" --wrap=none
```
Regenerate on every run. The generated `.md` keeps the exact stem of the `.docx` — the output-name derivation in step 2 relies on this stem. Then read `flows/<name>/flow.md` and all `.md` documents in `inputs/`. From `flow.md` extract the flow name (`#` heading) and the `## Metadata` keys: `Templates` (the only templates used), `Date in filename` (`true` default / `false` → omit the date suffix from filenames), `Source inputs` (optional comma-separated globs relative to project root pointing to other flows' outputs — read all matches and pass them to agents as source context), and `Docx template` / `Convert command` (optional, used at step 6). Read each `Templates` file from `flows/<name>/` — these are the output skeletons.

**2. Initialise the output workbook.** Derive the output base name from the flow's **primary input document** in `inputs/` by appending `_Workbook` to its filename stem, preserving original casing and separators (independent of the template's own name):
- `inputs/Project_Description.docx` → `Project_Description_Workbook`
- `inputs/Acme Robot.docx` → `Acme Robot_Workbook`

Apply the date suffix per `Date in filename` (`false` → `Project_Description_Workbook.md`; `true` → `Project_Description_Workbook-<YYYY-MM-DD>.md`). The run's output folder is named with the date **plus the run's start time** (`HHMMSS`, local time, taken once at folder creation) so folders sort chronologically. Output paths:
```
outputs/<YYYY-MM-DD>-<HHMMSS>/<workbook-name>.md     ← live markdown workbook
outputs/<YYYY-MM-DD>-<HHMMSS>/<workbook-name>.docx   ← final Word document (step 6)
```
Create `outputs/<YYYY-MM-DD>-<HHMMSS>/` and copy each `Templates` file verbatim to `<workbook-name>.md` (for multiple templates, use the base name plus each template's distinguishing suffix). Preserve every section, heading, table, and placeholder exactly throughout — agents fill placeholders; they never add or remove sections.

**3. Execute each step.** Work through `## Steps` in order, respecting sequencing: **sequential after X** (don't start until X is complete and written to the workbook), **parallel with Y** (see the parallel groups below), **gates Z** (ensure this step is complete and written before starting Z). For each step, spawn the assigned specialist agent (`subagent_type` matching the role) with a prompt containing:
- the role, step ID, and the artifact description from `flow.md`;
- this conventions preamble (verbatim): *"Fill only your assigned section(s), number IDs sequentially (`PREFIX_01`, `PREFIX_02`, …), record the upstream ID(s) each item derives from in its `Traces` column, and preserve every heading, table, column, and placeholder of the given template exactly. Return the completed section(s) as markdown in your final message — do not edit any file."*;
- the project inputs and any source context;
- **scoped workbook context** (see below);
- for steps 9f–9h and the SV sub-audit: the body of the **`gherkin-sv`** skill (`.claude/skills/gherkin-sv/SKILL.md`);
- for every requirement-authoring/co-author step (`BR_*`, `UR_*`, `USR_*`, `RQ_*`) and every QA sub-audit: the body of the **`requirements-quality`** skill (`.claude/skills/requirements-quality/SKILL.md`) — the INCOSE criteria, injected at the source so defects are prevented rather than found in audit;
- for the FMEA steps (6d, 6e, 6h, 6i) and the usability-chain QA sub-audit: the body of the **`fmea`** skill (`.claude/skills/fmea/SKILL.md`) — column semantics, severity/impact scales, and row-quality rules.

> **Return-content protocol — agents never edit the workbook.** Each agent returns its filled (or improved) section(s) as markdown in its final message. You — the orchestrator — paste each returned section into the live workbook with a single Edit, replacing exactly that section and nothing else. Content passes through the model once instead of three times (no Read + old_string + new_string round-trips), and agents can safely run in parallel because only you write to the file. After each paste, confirm the surrounding headings and sections are untouched.

> **Scoped context — never pass the whole workbook to an authoring/co-author/review step.** The growing workbook is the single largest token cost when handed in full to every step, and most of it is irrelevant to any one artifact. Instead, pass only what the step needs:
> - **(a)** the template section(s) the step must fill, and
> - **(b)** the content of the upstream section(s) the step traces to — derive *which* sections from the trace targets already documented in `flow.md` (the `## Steps` artifact descriptions and the per-artifact `Traces from X → Y` lines in `## Artifact Authoring Guidance`). For example, an `RQ_FN_*` step (`Traces from RQ_FN → UC/UR`) receives only the UC and UR sections, not the FMEA/KA/BR tables.
> - For a **co-author or review** step, also pass the author's just-written draft of the same section.
> - Always include any small cross-cutting rules the artifact must obey (e.g. the PRODUCT-FREE / SOLUTION-LEVEL rules and `Classification` inheritance) — these live in `flow.md` guidance, not in the agent files or other workbook sections, so scoping does not drop them.
>
> Extract these sections from the live workbook yourself and hand them to the agent inline. If a step genuinely needs a section you did not anticipate, the agent can request it; pass it on demand rather than defaulting to the whole workbook.

> **Parallel groups.** Run these as concurrent agent invocations (one message, multiple Agent calls); everything else runs sequentially:
> - **1a ∥ 1b ∥ 1c ∥ 1d** — four different sections, no mutual dependency;
> - **9c ∥ 9d** — `RQ_PR → RQ_FN` and `RQ_NF/RQ_CS → BR/RE` are mutually independent;
> - the **QA sub-audits** (see the audit mode below).
> Co-authors on the **same** artifact stay sequential (e.g. 2b → 2c, 9f → 9g → 9h): each builds on the previous revision.

**4. Update the workbook after each step.** Paste the returned section(s) in-place, preserving all surrounding headings, tables, and sections. The updated workbook is the **source from which you extract scoped context** (step 3) for subsequent steps — not a blob to hand to each step wholesale. **After each numbered phase** (1, 2, 3, …), run the `trace-check` script (`.venv\Scripts\python.exe scripts/check_traces.py "<workbook>.md" --json` on Windows — ~0 tokens) and immediately fix any `error` that concerns already-authored artefacts by re-spawning the owning agent with a precise correction request. Ignore findings that only exist because later steps haven't run yet (e.g. blank expectation `Traces` before step 1e, missing SV coverage before steps 9f–9h, placeholder warnings for unfilled sections). Catching trace breakage per phase is far cheaper than remediating it in step 10.

**5. Finalise the workbook.** When all steps are complete, prepend this header block:
```
---
Executed by: orchestration (CLAUDE.md)
Flow: flows/<name>/flow.md
Templates: flows/<name>/<template-1>.md, …
Inputs: inputs/
Date: <YYYY-MM-DD>
---
```

**6. Convert to .docx.** If a `Convert command` is defined, run it. Substitute `{md}`, `{docx}`, `{output_dir}` with the output paths. On Windows, prefix with the same registry PATH refresh. If no `Convert command` is defined, skip.

**7. Write run statistics.** Always, as the final step of every run, write `outputs/<YYYY-MM-DD>-<HHMMSS>/run-stats.md` (in the run's own output folder) summarising the run. This is orchestrator-authored (no specialist agent), built from the per-invocation figures each subagent returns (`subagent_tokens`, `duration_ms`). It contains:
- A header: flow path, workbook name, date, and the AI model used (orchestrator and subagents).
- A one-line note that the figures are subagent totals (excluding the orchestrator's own usage and any wait-for-permission time) and that agents ran sequentially, so summed duration approximates wall-clock.
- A **Totals** table: AI model, total subagent tokens, agent invocations, average tokens/invocation, summed agent execution time, and number of QA audit passes (with the final verdict).
- A **Per-step breakdown** table (`Step | Role | Tokens | Duration (s)`), one row per agent invocation **including** every QA audit pass and every remediation fix.
- A short **Notes** list: heaviest step by duration and by tokens, whether pandoc regeneration ran, how many QA passes were needed, and the artifact volume produced.
Use `outputs/2026-07-04-170434/run-stats.md` as the reference format, and note in the header which orchestration optimisations were active (scoped context, return-content, parallel groups, QA sub-audits). Add `Write run statistics` as the last todo item and mark it complete once the file is written.

**Co-author, gates, and audit modes.**
- **Co-author** (`parallel with` an author step): take the primary author's returned draft first, then spawn the co-author with that draft inline to review, challenge, and improve it — not replace it wholesale. The co-author returns the improved section; paste it over the previous version. When a step's description folds a review perspective into a co-author step, include that review checklist in the same prompt — do not spawn a separate reviewer.
- **Gates**: before a gated step, verify the gating step's section is non-empty; if not, re-run it.
- **Audit** (`audit` mode): run as a loop, not one pass.
  - **Structural pre-check first (cheap, no model tokens).** Before spawning any audit agent, run the **`trace-check`** skill — `python scripts/check_traces.py "<workbook>.md" --json` (use `.venv\Scripts\python.exe` on Windows) — which deterministically validates traceability and structure (dangling/wrong-direction traces, missing `SV_*` coverage, unaddressed `DC_*` gaps, ID gaps/duplicates, leftover placeholders). Route each `error` finding to its owning agent by ID prefix (see the skill's routing table), apply the returned fix, and **re-run the script until it returns no errors**. If the per-phase checks of step 4 were done, this pass is normally already clean.
  - **Then the semantic audit — four parallel scoped sub-audits.** Once the script is clean, spawn **four Quality Assurance sub-audits concurrently**, each with only its own sections, the ID lists of their direct upstream artefacts (for trace-intent context), and the cross-cutting rules that apply to that scope:
    1. **Informal domain** — Problem/DC, UE/ME/BE/RE, KA, BR — with the PRODUCT-FREE rule;
    2. **Usability chain** — IU/MD, User Groups, UR, USER_DFMEA, UT, UFMEA, USR, UI/UX;
    3. **Requirements** — Context/IF, Actors/UC, DD, all RQ_* — with the SOLUTION-LEVEL and enumerated-set rules;
    4. **Verification** — the SV feature files — with the `gherkin-sv` skill body and the coverage rule.
  - Each sub-audit returns findings tagged with the **Owner** role, or PASS. If all four return zero findings, record PASS and finish. Otherwise group findings by Owner, re-spawn each owning agent with a precise correction request (return-content; you apply the fix), re-run the `trace-check` script (a fix can break a trace), and re-run **only the sub-audit(s) whose scope was touched** — not all four. Repeat until zero findings.
  - The audit produces no report section — its deliverable is the corrected workbook. Cap the loop at a reasonable number of cycles; if findings persist, surface them rather than looping indefinitely.
