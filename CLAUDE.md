# EEToolkit — Claude Project Instructions

## Collaboration Rules
- Ask for explicit user permission before executing any terminal command.
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

**1. Load all inputs.** Ingest input documents first. For each `<name>.docx` in `inputs/`, convert it to a markdown sibling with pandoc and use the markdown — never the `.docx`. On Windows, run pandoc in PowerShell prefixed with a registry PATH refresh (ask permission first, per Collaboration Rules):
```
$env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User'); pandoc "inputs/<name>.docx" -o "inputs/<name>.md" --wrap=none
```
Regenerate on every run. The generated `.md` keeps the exact stem of the `.docx` — the output-name derivation in step 2 relies on this stem. Then read `flows/<name>/flow.md` and all `.md` documents in `inputs/`. From `flow.md` extract the flow name (`#` heading) and the `## Metadata` keys: `Templates` (the only templates used), `Date in filename` (`true` default / `false` → omit the date suffix from filenames), `Source inputs` (optional comma-separated globs relative to project root pointing to other flows' outputs — read all matches and pass them to agents as source context), and `Docx template` / `Convert command` (optional, used at step 6). Read each `Templates` file from `flows/<name>/` — these are the output skeletons.

**2. Initialise the output workbook.** Derive the output base name from the flow's **primary input document** in `inputs/` by appending `_Workbook` to its filename stem, preserving original casing and separators (independent of the template's own name):
- `inputs/Project_Description.docx` → `Project_Description_Workbook`
- `inputs/Acme Robot.docx` → `Acme Robot_Workbook`

Apply the date suffix per `Date in filename` (`false` → `Project_Description_Workbook.md`; `true` → `Project_Description_Workbook-<YYYY-MM-DD>.md`). Output paths:
```
outputs/<YYYY-MM-DD>/<workbook-name>.md     ← live markdown workbook
outputs/<YYYY-MM-DD>/<workbook-name>.docx   ← final Word document (step 6)
```
Create `outputs/<YYYY-MM-DD>/` and copy each `Templates` file verbatim to `<workbook-name>.md` (for multiple templates, use the base name plus each template's distinguishing suffix). Preserve every section, heading, table, and placeholder exactly throughout — agents fill placeholders; they never add or remove sections.

**3. Execute each step.** Work through `## Steps` in order, respecting sequencing: **sequential after X** (don't start until X is complete and written to the workbook), **parallel with Y** (run the primary author first, then the co-author with the author's draft as context), **gates Z** (ensure this step is complete and written before starting Z). For each step, spawn the assigned specialist agent (`subagent_type` matching the role) with: the role and step ID, the artifact description from `flow.md`, the project inputs, any source context, **scoped workbook context** (see below), and the specific section(s) to fill. Instruct it to fill only its section(s), number IDs sequentially (`prefix_01`, …), trace each item to its upstream artifact ID, and edit in-place preserving all surrounding structure.

> **Scoped context — never pass the whole workbook to an authoring/co-author/review step.** The growing workbook is the single largest token cost when handed in full to every step, and most of it is irrelevant to any one artifact. Instead, pass only what the step needs:
> - **(a)** the template section(s) the step must fill, and
> - **(b)** the content of the upstream section(s) the step traces to — derive *which* sections from the trace targets already documented in `flow.md` (the `## Steps` artifact descriptions and the per-artifact `Traces from X → Y` lines in `## Artifact Authoring Guidance`). For example, an `RQ_FN_*` step (`Traces from RQ_FN → UC/UR`) receives only the UC and UR sections, not the FMEA/KA/BR tables.
> - For a **co-author or review** step, also pass the author's just-written draft of the same section.
> - Always include any small cross-cutting rules the artifact must obey (e.g. the PRODUCT-FREE / SOLUTION-LEVEL rules and `Classification` inheritance) — these live in `flow.md` guidance, not in other workbook sections, so scoping does not drop them.
>
> Extract these sections from the live workbook yourself and hand them to the agent inline. Instruct the agent to **Read only its own target section's line range** from the workbook (using Read `offset`/`limit`) before editing — never to read the full file — then edit that section in-place. If a step genuinely needs a section you did not anticipate, the agent can request it; pass it on demand rather than defaulting to the whole workbook.

**4. Update the workbook after each step.** The agent edits its section(s) in-place in the live workbook, preserving all surrounding headings, tables, and sections. The updated workbook is the **source from which you extract scoped context** (step 3) for subsequent steps — not a blob to hand to each step wholesale.

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

**6. Convert to .docx.** If a `Convert command` is defined, run it (ask permission first). Substitute `{md}`, `{docx}`, `{output_dir}` with the output paths. On Windows, prefix with the same registry PATH refresh. If no `Convert command` is defined, skip.

**7. Write run statistics.** Always, as the final step of every run, write `outputs/<YYYY-MM-DD>/run-stats.md` summarising the run. This is orchestrator-authored (no specialist agent), built from the per-invocation figures each subagent returns (`subagent_tokens`, `duration_ms`). It contains:
- A header: flow path, workbook name, date, and the AI model used (orchestrator and subagents).
- A one-line note that the figures are subagent totals (excluding the orchestrator's own usage and any wait-for-permission time) and that agents ran sequentially, so summed duration approximates wall-clock.
- A **Totals** table: AI model, total subagent tokens, agent invocations, average tokens/invocation, summed agent execution time, and number of QA audit passes (with the final verdict).
- A **Per-step breakdown** table (`Step | Role | Tokens | Duration (s)`), one row per agent invocation **including** every QA audit pass and every remediation fix.
- A short **Notes** list: heaviest step by duration and by tokens, whether pandoc regeneration ran, how many QA passes were needed, and the artifact volume produced.
Use `outputs/2026-06-09/run-stats.md` as the reference format. Add `Write run statistics` as the last todo item and mark it complete once the file is written.

**Co-author, gates, and audit modes.**
- **Co-author** (`parallel with` an author step): take the primary author's draft first, then spawn the co-author to review, challenge, and improve it — not replace it wholesale.
- **Gates**: before a gated step, verify the gating step's section is non-empty; if not, re-run it.
- **Audit** (`audit` mode): run as a loop, not one pass. Spawn the audit agent (e.g. Quality Assurance) on the complete workbook; it returns findings tagged with the **Owner** role. If zero findings, record PASS and finish. Otherwise group findings by Owner, re-spawn each owning agent to correct its artefact(s) in-place, then re-spawn the audit agent on the updated workbook (a fix can break a downstream trace). Repeat until zero findings. The audit produces no report section — its deliverable is the corrected workbook. Cap the loop at a reasonable number of cycles; if findings persist, surface them rather than looping indefinitely.
