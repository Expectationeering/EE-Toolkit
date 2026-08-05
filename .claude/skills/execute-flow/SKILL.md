---
name: execute-flow
description: >-
  Use when the user asks to execute, run, or start an EE-Toolkit flow under
  flows/ — e.g. "Execute flows/ee-flow", "start ee-flow", "run ee", "run
  rte", or just a bare flow name matching a folder in flows/ (ignore case,
  the -flow suffix, and filler words). Also use when the user asks to
  (re)produce a flow's workbook, .docx output, or run statistics.
---

# Execute a flow — produce a workbook

You — the main assistant — orchestrate flows directly; there is no separate orchestrator agent. You drive the specialist agents step by step, accumulate their output into one live workbook, and show progress with a todo list. The specialist agents author the content; you sequence them and assemble the workbook.

## Procedure

**Always show progress with a todo list.** Per CLAUDE.md, show progress as a live todo list — resolve the flow name (step 1) first, then create the list with `TodoWrite` before loading anything else. Items: one per phase (or per step) of the flow's `## Steps`, plus `Ingest input documents`, `Quality Assurance audit`, `Convert to .docx`, and `Write run statistics`. Keep exactly one item `in_progress`; mark it `completed` the moment that step's output is written to the workbook.

**1. Load all inputs.** Resolve the flow first: if the requested name matches no folder under `flows/`, list the available flows and stop; if it matches several, ask which one. Then ingest input documents. For each `<name>.docx` in `inputs/`, convert it to a markdown sibling with pandoc and use the markdown — never the `.docx`. On Windows, run pandoc in PowerShell prefixed with a registry PATH refresh:
```
$env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User'); pandoc "inputs/<name>.docx" -o "inputs/<name>.md" --wrap=none
```
Regenerate on every run. The generated `.md` keeps the exact stem of the `.docx` — the output-name derivation in step 2 relies on this stem. Then read `flows/<name>/flow.md` and all `.md` documents in `inputs/`. From `flow.md` extract the flow name (`#` heading) and the `## Metadata` keys: `Templates` (the only templates used), `Date in filename` (`true` default / `false` → omit the date suffix from filenames), `Source inputs` (optional comma-separated globs relative to project root pointing to other flows' outputs — read all matches and pass them to agents as source context), and `Docx template` / `Convert command` (optional, used at step 6). Read each `Templates` file — paths are relative to the project root (e.g. `templates/<file>.md`) — these are the output skeletons.

**2. Initialise the output workbook.** Derive the output base name from the flow's **primary input document** in `inputs/` (the single `.docx` there; if there are several, the one the user named, else the largest — state your choice before creating the output folder) by appending `_Workbook` to its filename stem, preserving original casing and separators (independent of the template's own name):
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
- this conventions preamble (verbatim): *"Fill only your assigned section(s), number IDs sequentially (`PREFIX_01`, `PREFIX_02`, …), record the upstream ID(s) each item derives from in its `Traces` column (leave `Traces` blank if this step's artifact description says a later consolidation step completes it), and preserve every heading, table, column, and placeholder of the given template exactly. Return the completed section(s) as markdown in your final message — do not edit any file."* For steps 1a–1d, additionally state explicitly in the prompt: leave the `Traces` column empty; step 1e fills it;
- the project inputs and any source context;
- **scoped workbook context** (see below);
- the skill body (or bodies) for the step, per this injection table — single source, injected inline so defects are prevented at the source, no copies in agent files:

| Steps | Inject skill body |
|---|---|
| 9f–9h + the SV sub-audit | **`gherkin-sv`** (`.claude/skills/gherkin-sv/SKILL.md`) |
| 6d, 6e, 6h, 6i + the usability-chain sub-audit | **`fmea`** (`.claude/skills/fmea/SKILL.md`) |
| every `BR_*`/`UR_*`/`USR_*`/`RQ_*` authoring or co-author step + all four QA sub-audits | **`requirements-quality`** (`.claude/skills/requirements-quality/SKILL.md`) |

> **Return-content protocol — agents never edit the workbook.** Each agent returns its filled (or improved) section(s) as markdown in its final message. You — the orchestrator — paste each returned section into the live workbook with a single Edit, replacing exactly that section and nothing else. Content passes through the model once instead of three times (no Read + old_string + new_string round-trips), and agents can safely run in parallel because only you write to the file. After each paste, confirm the surrounding headings and sections are untouched.

> **Scoped context — never pass the whole workbook to an authoring/co-author/review step.** The growing workbook is the single largest token cost when handed in full to every step, and most of it is irrelevant to any one artifact. Instead, pass only what the step needs:
> - **(a)** the template section(s) the step must fill, and
> - **(b)** the content of the upstream section(s) the step traces to — derive *which* sections from the trace targets already documented in `flow.md` (the `## Steps` artifact descriptions and the per-artifact `Traces from X → Y` lines in `## Artifact Authoring Guidance`). For example, an `RQ_FN_*` step (`Traces from RQ_FN → UC/UR`) receives only the UC and UR sections, not the FMEA/KA/BR tables.
> - For a **co-author or review** step, also pass the author's just-written draft of the same section.
> - Always include any small cross-cutting rules the artifact must obey (e.g. the PRODUCT-FREE / SOLUTION-LEVEL rules and `Classification` inheritance) — these live in `flow.md` guidance, not in the agent files or other workbook sections, so scoping does not drop them.
>
> Extract these sections from the live workbook yourself and hand them to the agent inline. If a step genuinely needs a section you did not anticipate, the agent can request it; pass it on demand rather than defaulting to the whole workbook.

> **Red flags — if you catch yourself thinking:**
> | Thought | Reality |
> |---|---|
> | "This step is complex, safer to pass the whole workbook" | Scoping failures come from not reading flow.md's `Traces from X → Y` lines. Read them, then scope. |
> | "Just this once, let the agent edit the file" | Agents have `tools: Read` only — an edit request will fail and burn the invocation. |
> | "The agent asked for a section I did not plan for" | Pass that one section on demand. That is the designed path, not a reason to widen scope. |

> **Parallel groups.** Run these as concurrent agent invocations (one message, multiple Agent calls); everything else runs sequentially:
> - **1a ∥ 1b ∥ 1c ∥ 1d** — four different sections, no mutual dependency;
> - **9c ∥ 9d** — `RQ_PR → RQ_FN` and `RQ_NF/RQ_CS → BR/RE` are mutually independent;
> - the **QA sub-audits** (see the audit mode below).
> Co-authors on the **same** artifact stay sequential (e.g. 2b → 2c, 9f → 9g → 9h): each builds on the previous revision.

**4. Update the workbook after each step.** Paste the returned section(s) in-place, preserving all surrounding headings, tables, and sections. The updated workbook is the **source from which you extract scoped context** (step 3) for subsequent steps — not a blob to hand to each step wholesale. **After each numbered phase** (1, 2, 3, …), run the **`trace-check`** skill against the workbook (~0 tokens; command and output contract are in that skill) and immediately fix any `error` that concerns already-authored artefacts by re-spawning the owning agent with a precise correction request. Ignore findings that only exist because later steps haven't run yet — the trace-check skill's partial-run section lists them. Catching trace breakage per phase is far cheaper than remediating it in step 10.

**5. Finalise the workbook.** When all steps are complete, prepend this header block:
```
---
Executed by: execute-flow skill (.claude/skills/execute-flow/SKILL.md)
Flow: flows/<name>/flow.md
Templates: <the Templates paths from flow.md, e.g. templates/<template-1>.md>, …
Inputs: inputs/
Date: <YYYY-MM-DD>
---
```

**6. Convert to .docx.** If a `Convert command` is defined, run it. Substitute `{md}`, `{docx}`, `{output_dir}` with the output paths. On Windows, prefix with the same registry PATH refresh. If no `Convert command` is defined, skip.

**7. Write run statistics.** Always, as the final step of every run, write `outputs/<YYYY-MM-DD>-<HHMMSS>/run-stats.md` (in the run's own output folder). This is orchestrator-authored (no specialist agent), built from the per-invocation figures each subagent returns (`subagent_tokens`, `duration_ms`). Fill this skeleton:

````markdown
# Run Statistics — <flow name>

**Flow**: flows/<name>/flow.md · **Workbook**: <workbook-name>.md · **Date**: <YYYY-MM-DD> · **AI model**: <orchestrator and subagents> · **Optimisations active**: scoped context, return-content, parallel groups, QA sub-audits

> Figures are subagent totals (excluding the orchestrator's own usage and any wait-for-permission time). Parallel groups ran concurrently, so summed duration exceeds wall-clock — both are reported below.

## Totals
| Metric | Value |
|---|---|
| Total subagent tokens | … |
| Agent invocations | … |
| Average tokens / invocation | … |
| Summed agent execution time | … |
| Wall-clock duration | … |
| QA audit passes (final verdict) | … |

## Per-step breakdown
| Step | Role | Tokens | Duration (s) |
|---|---|---|---|
<one row per agent invocation, including every QA audit pass and every remediation fix>

## Notes
- <heaviest step by duration and by tokens>
- <whether pandoc regeneration ran; how many QA passes were needed>
- <artifact volume produced>
````

`outputs/2026-07-04-170434/run-stats.md` may be consulted for tone and the Notes style only — the skeleton above is the required shape where the two differ. Add `Write run statistics` as the last todo item and mark it complete once the file is written.

## Co-author, gates, and audit modes

- **Co-author** (`parallel with` an author step): take the primary author's returned draft first, then spawn the co-author with that draft inline to review, challenge, and improve it — not replace it wholesale. The co-author returns the improved section; paste it over the previous version. When a step's description folds a review perspective into a co-author step, include that review checklist in the same prompt — do not spawn a separate reviewer.
- **Gates**: before a gated step, verify the gating step's section is non-empty; if not, re-run it.
- **Audit** (`audit` mode): run as a loop, not one pass.
  - **Structural pre-check first (cheap, no model tokens).** Run the **`trace-check`** skill first and iterate to zero errors before spawning any audit agent: route each `error` to its owning agent by ID prefix per that skill's routing table, apply the returned fix, and re-run until clean. If the per-phase checks of step 4 were done, this pass is normally already clean.
  - **Then the semantic audit — four parallel scoped sub-audits.** Once the script is clean, spawn **four Quality Assurance sub-audits concurrently**, each with only its own sections, the ID lists of their direct upstream artefacts (for trace-intent context), and the cross-cutting rules that apply to that scope:
    1. **Informal domain** — Problem/DC, UE/ME/BE/RE, KA, BR — with the PRODUCT-FREE rule;
    2. **Usability chain** — IU/MD, User Groups, UR, USER_DFMEA, UT, UFMEA, USR, UI/UX;
    3. **Requirements** — Context/IF, Actors/UC, DD, all RQ_* — with the SOLUTION-LEVEL and enumerated-set rules;
    4. **Verification** — the SV feature files — with the coverage rule.
  - Inject skill bodies into each sub-audit per the injection table in step 3.
  - Each sub-audit returns findings tagged with the **Owner** role, or PASS. If all four return zero findings, record PASS and finish. Otherwise group findings by Owner, re-spawn each owning agent with a precise correction request (return-content; you apply the fix), re-run the `trace-check` script (a fix can break a trace), and re-run **only the sub-audit(s) whose scope was touched** — not all four. Repeat until zero findings.
  - The audit produces no report section — its deliverable is the corrected workbook. Cap the loop at 3 remediation cycles; if findings persist after the third, stop and surface the outstanding findings with their Owners in your final message.
