---
name: requirements-quality
description: The INCOSE requirements-quality criteria (10 checks with definitions and common defects) used across the Expectationeering workbook. The orchestrator injects this body inline into every requirement-authoring/co-author step (BR_*, UR_*, USR_*, RQ_*) so defects are prevented at the source, and into the Quality Assurance sub-audits as the audit checklist — single source, no copies in agent files.
---

# INCOSE Requirements Quality Criteria

Every requirement statement in the workbook (`BR_*`, `UR_*`, `USR_*`, `RQ_IF_*`, `RQ_FN_*`, `RQ_PR_*`, `RQ_NF_*`, `RQ_CS_*`) must satisfy all ten criteria. **When authoring, check each statement against this table before returning it** — a defect prevented here is a QA finding, a remediation round, and a re-audit avoided.

| # | Criterion | Definition | Common defects |
|---|-----------|------------|----------------|
| 1 | **Unambiguous** | Only one interpretation possible; no vague qualifiers | "appropriate", "adequate", "sufficient", "easy", "fast", "user-friendly", "representative" without a defined condition, passive voice without subject |
| 2 | **Complete** | All conditions and responses specified; no TBDs or placeholders | Missing error conditions, TBD/TBC markers, unstated assumptions, incomplete ranges, unbounded detection ("upon detecting X" without a maximum detection time) |
| 3 | **Consistent** | No contradictions within the set or with referenced documents | Conflicting values, duplicate IDs with different text, incompatible priorities, the same budget or clock-start defined differently in two places |
| 4 | **Verifiable** | Can be objectively tested or measured within available resources | Unmeasurable criteria, "maximize", "minimize", "as much as possible", subjective pass/fail, quantified thresholds under unquantified test conditions |
| 5 | **Traceable** | Linked to an upstream stakeholder need, regulation, or design input | Missing source reference, orphaned requirements, a trace whose upstream item does not actually contain the cited intent |
| 6 | **Feasible** | Achievable within known constraints (technical, cost, schedule) | Contradicts known physical limits, ignores stated constraints (e.g. the fixed platform envelope) |
| 7 | **Necessary** | Represents a real stakeholder need; no gold-plating | Requirements without rationale, nice-to-have without justification |
| 8 | **Atomic** | Expresses exactly one requirement; no conjunctions creating multiple obligations | "and", "or", "but also", "as well as" joining two independently verifiable obligations in one statement (split them) |
| 9 | **Correct** | Accurately reflects the stakeholder's actual need | Misinterpretation of the source artefact, wrong unit, wrong threshold |
| 10 | **Conformant** | Uses "shall" for mandatory, "should" for desired, "may" for optional; active voice with defined subject | Mixed modal verbs, passive constructions without subject, inconsistent verb forms |

## Authoring quick-check

Before returning a requirements table, verify per row: one obligation per row (8); a number, bound, or objectively checkable condition on every claim **and** on its test condition (1, 4); no TBD and no unbounded "upon detection" (2); the same figures and clock-starts as neighbouring artefacts (3); the cited upstream ID really contains this intent (5); "shall" + the system as subject (10).

## Audit usage

The Quality Assurance sub-audits evaluate every requirement statement in their scope against all ten criteria and tag each finding with the violated criterion by name. Criteria are independent: a requirement that uses "shall" but is untestable fails Verifiable while passing Conformant.
