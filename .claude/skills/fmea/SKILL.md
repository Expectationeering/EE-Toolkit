---
name: fmea
description: Method rules for the FMEA tables in the Expectationeering workbook — column semantics, severity and impact scales, and row-quality rules for the User DFMEA (USER_DFMEA_*) and Usability FMEA (UFMEA_*) — use errors, human-factors causes, and harm-based severity. Injected inline by execute-flow into the FMEA authoring/co-author steps and the usability-chain QA sub-audit — single source, no copies in agent files.
---

# FMEA Method Rules

The workbook contains two FMEA tables, both analysing how use of the product can fail — not how the product's internals can fail (system DFMEA is downstream and out of scope):

- **User DFMEA (`USER_DFMEA_*`)** — operation failures, analysed one per user requirement. Traces from **USER_DFMEA → UR**.
- **Usability FMEA (`UFMEA_*`)** — interaction failures, analysed per use scenario/task. Traces from **UFMEA → UT**.

Keep the two disjoint: an operation failure (wrong sensor site, skipped step) belongs in the User DFMEA; an interaction/perception failure (misread state, mis-touch, banner blindness, mode confusion) belongs in the Usability FMEA.

## Column semantics

- **`Item/Function`** (USER_DFMEA) — the user-facing function or interaction step being analysed (e.g. "sensor placement", "alarm acknowledgement"), not a product component. **`Requirement`** (USER_DFMEA) / **`Scenario Title`** (UFMEA) restate the traced upstream item in words so the row reads standalone.
- **Failure Mode / Use Error** — *what* goes wrong, stated as observable user behaviour, never as a design flaw or a consequence.
- **Failure Cause / Cause** — *why* it goes wrong: the concrete circumstance or design property that produces the error (time pressure, look-alike connectors, ambiguous state indication). Never a restatement of the failure mode.
- **HF Cause** (UFMEA) — the human-factors mechanism behind the cause: habituation, banner blindness, automation bias, attention tunnelling, mode confusion, premature task closure, working-memory overload, perceptual confusion, interrupted-task slip.
- **End-effect / Effect** — the *clinical* consequence for the patient or care process, followed through to harm, not merely the technical result (see the worked row).
- **Rationale** — why this row is credible in the real use context (name the setting, workload, or named input risk it derives from).
- **`Prevention`** (USER_DFMEA) — the design measures that control the mode, in one cell. Where a measure is additional to the current concept, prefix it `NEW:`; anything unprefixed is read as existing. Do not invent other markup (no "Existing:/New:" labels, no numbered lists of independent measures — split rows instead).
- **`Mitigation (existing)` / `Mitigation (new)`** (UFMEA) — *existing* = what the current concept already provides; *new* = the additional measure this row demands.
- Every mitigation must be a verifiable design property that a downstream `USR_*` or `RQ_*` can capture — never "training" or "instructions" alone for a Critical/High row (training may only supplement a design measure).

## Severity and impact scales

| USER_DFMEA `Severity` | UFMEA `Usability Impact Level` | Meaning |
|---|---|---|
| **Critical** | **High** | Can lead to death, serious injury, or wrong/missed/delayed treatment of the patient |
| **Major** | **Medium** | Degrades or delays care, recoverable before patient harm; or contaminates the clinical record |
| **Minor** | **Low** | Inconvenience or inefficiency without patient impact |

Rate the **uncontrolled** failure (before the new mitigation). Wrong-patient errors, silenced/missed alarms, undetected wrong data, and confusion between simulated and real data are Critical/High by default — downgrade only with an explicit rationale.

## One worked row

USER_DFMEA (template header, one filled row):

| ID | Item/Function | Requirement | Failure Mode | End-effect | Rationale | Failure Cause | Severity | Prevention | Classification | Traces |
|---|---|---|---|---|---|---|---|---|---|---|
| USER_DFMEA_01 | Sensor placement | UR_03 — correct SpO₂ probe attachment | User attaches the SpO₂ probe to the wrong body site | Wrong SpO₂ value accepted → wrong diagnostic candidate → wrong treatment | Night shift with float staff unfamiliar with the device; probes within reach look alike | Look-alike probe connectors and no site indication on the display | Critical | Site-keyed connectors; NEW: on-screen probe-site confirmation before values display | Critical | UR_03 |

UFMEA (template header, one filled row):

| ID | Scenario Title | Use Error | Cause | Effect | HF Cause | Rationale | Usability Impact Level | Mitigation (existing) | Mitigation (new) | Classification | Traces |
|---|---|---|---|---|---|---|---|---|---|---|---|
| UFMEA_01 | Acknowledge alarms during handover | Clinician silences the alarm and forgets to re-enable it | Frequent nuisance alarms at shift handover | Missed deterioration → delayed treatment | Habituation | Alarm fatigue at handover is a named input risk | High | Silence timeout auto-reactivates after 2 min | Persistent silenced-state banner on the main screen | Critical | UT_02 |

## Row-quality rules

1. One failure mode per row; a row that needs "and" between two distinct errors must be split.
2. Cause ≠ effect ≠ failure mode — the three columns must not restate each other.
3. Every Critical/High row has at least one **new** design-level mitigation (`NEW:`-prefixed in `Prevention`, or in `Mitigation (new)`) — or an explicit statement that the existing measure fully controls it.
4. UFMEA `Classification` inherits through the UT to the UT's underlying UR — the UT table itself carries no `Classification`; USER_DFMEA inherits it from the traced UR.
5. `Traces` cites the analysed artefact ID(s) — the UR (USER_DFMEA) or UT (UFMEA) whose failure is examined, never an invented downstream ID; the `Requirement`/`Scenario Title` column names it for the reader.
6. Ground causes in the real context: shift handover, night shift, alarm fatigue, transport noise/vibration/glare, gloves, float staff, simultaneous admissions — not laboratory conditions.
7. Coverage: every safety-relevant UR appears in at least one USER_DFMEA row; every use scenario appears in at least one UFMEA row.
8. Every **new** mitigation is realised by a downstream `USR_*`, `RQ_*`, or UI/UX artefact — an unrealised new mitigation is a finding.
