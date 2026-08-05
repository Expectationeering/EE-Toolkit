---
name: requirements-quality
description: The INCOSE requirements-quality criteria (10 checks with definitions and common defects) used across the Expectationeering workbook. The orchestrator injects this body inline into every requirement-authoring/co-author step (BR_*, UR_*, USR_*, RQ_*) so defects are prevented at the source, and into the Quality Assurance sub-audits as the audit checklist — single source, no copies in agent files.
---

# INCOSE Requirements Quality Criteria (SMART requirement checks)

Every requirement statement in the workbook (`BR_*`, `UR_*`, `USR_*`, `RQ_IF_*`, `RQ_FN_*`, `RQ_PR_*`, `RQ_NF_*`, `RQ_CS_*`) must satisfy all ten criteria — these are the SMART/INCOSE checks referenced by the flow's requirement guidance. **When authoring, check each statement against this table before returning it** — a defect prevented here is a QA finding, a remediation round, and a re-audit avoided.

| # | Criterion | Definition | Common defects |
|---|-----------|------------|----------------|
| 1 | **Unambiguous** | Only one interpretation possible; no vague qualifiers | "appropriate", "adequate", "sufficient", "easy", "fast", "user-friendly", "representative" without a defined condition, passive voice without subject |
| 2 | **Complete** | All conditions and responses specified; no TBDs or placeholders | Missing error conditions, TBD/TBC markers, unstated assumptions, incomplete ranges, unbounded detection ("upon detecting X" without a maximum detection time) — but the template's flow-mandated placeholders (`_To be added_` diagram stubs, "Not filled by this flow" notes) are required by the flow and are not Complete defects |
| 3 | **Consistent** | No contradictions within the set or with referenced documents | Conflicting values, duplicate IDs with different text, incompatible priorities, the same budget or clock-start defined differently in two places |
| 4 | **Verifiable** | Can be objectively tested or measured within available resources | Unmeasurable criteria, "maximize", "minimize", "as much as possible", subjective pass/fail, quantified thresholds under unquantified test conditions |
| 5 | **Traceable** | Linked to an upstream stakeholder need, regulation, or design input | Missing source reference, orphaned requirements, a trace whose upstream item does not actually contain the cited intent |
| 6 | **Feasible** | Achievable within known constraints (technical, cost, schedule) | Contradicts known physical limits, ignores stated constraints (e.g. the fixed platform envelope) |
| 7 | **Necessary** | Represents a real stakeholder need; no gold-plating | Requirements without rationale, nice-to-have without justification |
| 8 | **Atomic** | Expresses exactly one requirement; no conjunctions creating multiple obligations | "and", "or", "but also", "as well as" joining two independently verifiable obligations in one statement (split them) |
| 9 | **Correct** | Accurately reflects the stakeholder's actual need | Misinterpretation of the source artefact, wrong unit, wrong threshold |
| 10 | **Conformant** | Uses "shall" for mandatory, "should" for desired, "may" for optional; active voice with a defined subject. **`UR_*` exception:** user requirements keep the flow's mandated user-story form (*As a \<user group\> I want \<feature\> so that \<benefit\>*) — Conformant there means the named user group is explicit and the form is used consistently, not that "shall" appears | Mixed modal verbs, passive constructions without subject, inconsistent verb forms, a `UR_*` flagged for lacking "shall" |

## Compliant shape

`<When/While <trigger or condition>,> the <subject> shall <one observable action> <quantified bound + unit> <under <stated measurement condition>>.`

**Defective:** "The system shall detect occlusion quickly and alert the user appropriately." — fails 1 ("quickly", "appropriately"), 2 (no detection bound), 4 (untestable), 8 (detect + alert).

**Compliant (split into two rows):** "When line pressure exceeds 2.0 bar, the system shall raise an audible occlusion alarm within 5 s." · "The occlusion alarm shall be audible at ≥ 65 dB(A) at 1 m in a 45 dB(A) ambient."

(`UR_*` rows instead use the mandated user-story form — see criterion 10.)

## Authoring quick-check

Before returning a requirements table, verify **per row**:

- [ ] one obligation — no "and"/"or" joining two verifiable claims (8)
- [ ] a number, bound, or objectively checkable condition on the claim **and** on its test condition (1, 4)
- [ ] no TBD, no unbounded "upon detecting X" (2)
- [ ] same figures and clock-starts as neighbouring artefacts (3)
- [ ] the cited upstream ID really contains this intent (5)
- [ ] mandated statement form for the prefix — "shall" + the system as the explicit subject, or for `UR_*` the mandated user-story form with a named user group (10)

**Rationalizations that produce findings:** "the threshold is already in the input document" → repeat it in the statement; the requirement is read standalone. · "splitting this row would duplicate the trace" → duplicate the trace, not the obligation. · "the test condition is obvious" → if it is obvious, it is cheap to write; if it is not written, it is not verifiable.

## Audit usage

Criteria are independent: a requirement that uses "shall" but is untestable fails Verifiable while passing Conformant. Tag each finding with the violated criterion by name.
