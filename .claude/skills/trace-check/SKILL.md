---
name: trace-check
description: >-
  Deterministically validate Expectationeering workbook traceability and structure.
  Checks that every Traces reference exists and points to an allowed upstream
  prefix, every RQ_FN has an SV feature file, every DC gap is addressed, ID
  sequences have no duplicates/gaps, and no fill-in placeholders remain. Use during
  the Quality Assurance audit (step 10a) and after any authoring step that adds
  traced rows — run it BEFORE spending model tokens on a full-workbook QA read.
---

# Trace check

Run the mechanical traceability and structure sweep as a script — it costs
**zero model tokens** and finds the whole class of structural defects a
full-workbook QA read otherwise burns six figures of tokens on. The LLM audit
is for meaning; this script is for structure.

## How to run

On Windows use the project venv interpreter directly; `uv run python` or plain
`python` works elsewhere:

```
.venv\Scripts\python.exe scripts/check_traces.py "<path-to-workbook>.md" --json
```

Exit code `0` = no errors (warnings may still be present), `1` = at least one
error, `2` = bad invocation (no workbook path) — fix the command, do not route
it as a finding. With `--json` it prints a list of `{severity, id, msg}`
objects; without it, one human-readable line per finding. Example output:

```json
[{"severity": "error", "id": "RQ_FN_07", "msg": "traces to UR_44 which does not exist in the workbook"}]
```

`id` is an item ID for item-level findings, a bare prefix (e.g. `KA_`) for
duplicate/gap findings, and the literal `template` for placeholder warnings.

## What it validates

| Check | Severity |
|---|---|
| `Traces` cites an ID that does not exist | error |
| Item traces to a disallowed upstream prefix (wrong direction in the DAG) | error |
| Item that must trace upstream has no trace | error |
| `RQ_FN_*` with no `SV` feature file (`@ID:RQ_FN_xx`) covering it | error |
| `DC_*` gap that nothing traces to | warning |
| Duplicate IDs within a prefix | error |
| ID sequence gaps within a prefix | warning |
| Leftover `<!-- ... -->` fill-in placeholder | warning |

The allowed-upstream DAG is encoded in `RULES` inside the script and mirrors the
`Traces from X → Y` lines in `flows/ee-flow/flow.md`.
`_To be added_` diagram markers and the out-of-scope template comment block are
intentional and already filtered (`INTENTIONAL_COMMENT` in the script) — they
never appear in output.

### Expected findings during a partial run

Unauthored sections still hold the template's stub rows (`UR_01`, `KA_01`, …
with empty cells), so mid-flow the script reports findings that only exist
because a step has not run yet. **Defer any finding on a section whose
authoring step has not run** — typical shapes:

- `has no upstream trace` errors on the template stub rows of unauthored
  sections (the script flags every empty stub row's missing trace);
- `RQ_FN_* → no SV feature file`: expected until steps 9f–9h;
- `UE_*/ME_*/BE_*/RE_* → has no upstream trace`: expected until step 1e;
- `DC_*` gap that nothing traces to: expected until step 1e;
- `template` (unfilled placeholder): expected for any section whose authoring
  step has not run.

Every finding in an **already-authored** section is real — in particular, an
item that traces to a non-existent ID: fix it now; deferring it lets later
steps build on a broken trace.

## How to use the result in the QA loop

1. Run this script **first**, before any LLM audit. Parse the JSON.
2. Route each finding to the single owner by ID prefix:

   | Finding `id` starts with | Owner |
   |---|---|
   | `UE_`, `ME_`, `BE_`, `RE_`, `DC_`, `KA_`, `BR_`, `RQ_FN_` | **Product Owner** |
   | `UC_`, `DD_`, `IF_`, `RQ_IF_`, `RQ_PR_` | **System Architect** |
   | `IU_`, `MD_`, `UR_`, `USR_`, `UT_`, `UFMEA_`, `USER_DFMEA_` | **Usability Validation** |
   | `RQ_NF_`, `RQ_CS_` | **Regulatory Stakeholder** |
   | `template` | **orchestrator** — fill or delete the placeholder yourself |

   A missing-SV finding is reported against the `RQ_FN_*` id — the fix is a new
   feature file, still Product Owner. Fix in-place, then **re-run the script**
   (a fix can break another trace).
3. Only once the script returns no errors, start the semantic QA audit — this
   script proves nothing about clarity, atomicity, or verifiability.
