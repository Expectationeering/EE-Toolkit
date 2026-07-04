---
name: fmea
description: Method rules for the FMEA tables in the Expectationeering workbook — column semantics, severity and impact scales, and row-quality rules for the User DFMEA (USER_DFMEA_*) and Usability FMEA (UFMEA_*). The orchestrator injects this body inline into the FMEA authoring/co-author steps (6d, 6e, 6h, 6i) and the usability-chain QA sub-audit — single source, no copies in agent files.
---

# FMEA Method Rules

The workbook contains two FMEA tables, both analysing how use of the product can fail — not how the product's internals can fail (system DFMEA is downstream and out of scope):

- **User DFMEA (`USER_DFMEA_*`)** — how users might misuse, misinterpret, or fail to operate the product: operation failures analysed per user requirement. Traces from **USER_DFMEA → UR**.
- **Usability FMEA (`UFMEA_*`)** — where the UI, workflow, or interaction model itself leads to errors, slow operation, or unsafe outcomes: interaction failures analysed per use scenario/task. Traces from **UFMEA → UT**.

Keep the two disjoint: an operation failure (wrong sensor site, skipped step) belongs in the User DFMEA; an interaction/perception failure (misread state, mis-touch, banner blindness, mode confusion) belongs in the Usability FMEA.

## Column semantics

- **Failure Mode / Use Error** — *what* goes wrong, stated as observable user behaviour ("user attaches the sensor to the wrong body site"), never as a design flaw or a consequence.
- **Failure Cause / Cause** — *why* it goes wrong: the concrete circumstance or design property that produces the error (time pressure, look-alike connectors, ambiguous state indication). Never a restatement of the failure mode.
- **HF Cause** (UFMEA) — the human-factors mechanism behind the cause: habituation, banner blindness, automation bias, attention tunnelling, mode confusion, premature task closure, working-memory overload, perceptual confusion, interrupted-task slip.
- **End-effect / Effect** — the *clinical* consequence for the patient or care process, followed through to harm ("wrong diagnostic candidate → wrong treatment"), not merely the technical result ("wrong value displayed").
- **Rationale** — why this row is credible in the real use context (name the setting, workload, or named input risk it derives from).
- **Prevention / Mitigation (existing / new)** — design measures. *Existing* = what the current concept already provides; *new* = the additional measure this row demands. Every mitigation must be a verifiable design property that a downstream `USR_*` or `RQ_*` can capture — never "training" or "instructions" alone for a Critical/High row (training may only supplement a design measure).

## Severity and impact scales

| USER_DFMEA `Severity` | UFMEA `Usability Impact Level` | Meaning |
|---|---|---|
| **Critical** | **High** | Can lead to death, serious injury, or wrong/missed/delayed treatment of the patient |
| **Major** | **Medium** | Degrades or delays care, recoverable before patient harm; or contaminates the clinical record |
| **Minor** | **Low** | Inconvenience or inefficiency without patient impact |

Rate the **uncontrolled** failure (before the new mitigation). Wrong-patient errors, silenced/missed alarms, undetected wrong data, and confusion between simulated and real data are Critical/High by default — downgrade only with an explicit rationale.

## Row-quality rules

1. One failure mode per row; a row that needs "and" between two distinct errors must be split.
2. Cause ≠ effect ≠ failure mode — the three columns must not restate each other.
3. Every Critical/High row has at least one **new** design-level mitigation (or an explicit statement that the existing measure fully controls it).
4. `Classification` is inherited from the traced upstream item (UR for USER_DFMEA, the UT's underlying UR for UFMEA).
5. `Traces` cites the analysed artefact ID(s) — the UR (USER_DFMEA) or UT (UFMEA) whose failure is examined; the `Requirement`/`Scenario Title` column names it for the reader.
6. Ground causes in the real context: shift handover, night shift, alarm fatigue, transport noise/vibration/glare, gloves, float staff, simultaneous admissions — not laboratory conditions.
7. Coverage: every safety-relevant UR appears in at least one USER_DFMEA row; every use scenario appears in at least one UFMEA row.

## Audit usage

The usability-chain QA sub-audit checks each FMEA row against the column semantics, the scales (severity consistent with the stated end-effect), and the row-quality rules above, and verifies that new mitigations are realised by downstream `USR_*`/`RQ_*`/UI-UX artefacts.
