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

Run the mechanical traceability and structure sweep as a script. It costs **zero
model tokens** and catches exactly the class of findings the QA audit loop
otherwise burns ~250k tokens per pass on: dangling traces, wrong-direction
traces, missing SV coverage, unaddressed gaps, ID gaps/duplicates, and leftover
placeholders.

## How to run

On Windows use the project venv Python (see the `venv-python-for-docx` memory);
otherwise `uv run python` or plain `python` is fine:

```
.venv\Scripts\python.exe scripts/check_traces.py "<path-to-workbook>.md" --json
```

Exit code `0` = no errors (warnings may still be present), `1` = at least one
error. With `--json` it prints a list of `{severity, id, msg}` objects; without
it, one human-readable line per finding.

## What it validates

| Check | Severity |
|---|---|
| `Traces` cites an ID that does not exist | error |
| Item traces to a disallowed upstream prefix (wrong direction in the DAG) | error |
| Item that must trace upstream has no trace | error |
| `RQ_FN_*` with no `SV` feature file (`@ID:RQ_FN_xx`) covering it | error |
| `DC_*` gap addressed by no expectation | warning |
| Duplicate IDs within a prefix | error |
| ID sequence gaps within a prefix | warning |
| Leftover `<!-- ... -->` fill-in placeholder | warning |

The allowed-upstream DAG is encoded in `RULES` inside the script and mirrors the
`Traces from X → Y` lines in `flows/expectationeering-flow/flow.md`.

## How to use the result in the QA loop

1. Run this script **first**, before any LLM audit. Parse the JSON.
2. Route each finding to the owning authoring agent by ID prefix:
   - `RQ_FN_*`, `SV_*`, `BR_*`, `KA_*`, `DC_*` → **Product Owner**
   - `RQ_PR_*`, `RQ_IF_*`, `IF_*`, `UC_*`, `DD_*`, `KA_*` (feasibility) → **System Architect**
   - `UR_*`, `USR_*`, `UFMEA_*`, `USER_DFMEA_*`, `UT_*`, `IU_*`, `MD_*` → **Usability Validation**
   - `RQ_NF_*`, `RQ_CS_*` → **Regulatory Stakeholder**
   Fix in-place, then **re-run the script** (a fix can break another trace).
3. Only once the script returns no errors, spawn the **Quality Assurance** agent
   for the **semantic** INCOSE review (clarity, atomicity, verifiability,
   SMART-ness). It no longer needs to do mechanical trace-counting, so scope it
   to quality only.

## Known non-findings (do not act on these)

- `_To be added_` markers for the Context, Use Case, and black-box diagrams are
  **required** by the flow — they are plain text, not `<!-- -->` comments, so the
  script already does not flag them.
- The trailing template comment block for the out-of-scope Architecture /
  Detailed Design / DFMEA / Items sections is filtered out by design.
