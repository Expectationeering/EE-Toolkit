# Run Statistics — Expectationeering Flow

**Flow**: flows/expectationeering-flow/flow.md
**Workbook**: Project_Description_Workbook (.md / .docx)
**Date**: 2026-06-15
**AI model**: Claude Opus 4.8 (`claude-opus-4-8[1m]`) — orchestrator and all specialist subagents

> These figures are the **subagent** totals reported per agent invocation. They exclude the orchestrator's own token usage (reading template/inputs, sequencing, header/metadata edits, trace-check + docx conversion) and the wall-clock spent waiting for user permissions. Agents were run **sequentially** to protect the single live workbook from concurrent-write conflicts, so the summed duration approximates the compute wall-clock — except where a step's reported duration includes idle/permission wait (see Notes on step 3c).

> **Optimisation note — this run used "scoped context" (lever A).** Each authoring/co-author/review step received only its own template section(s) plus the specific upstream section(s) it traces to (extracted from the live workbook), instead of the full growing workbook. Agents read only their own section's line range before editing. The QA audit still reads the full workbook by design (lever B not adopted).

## Totals

| Metric | Value |
|---|---|
| AI model | Claude Opus 4.8 (`claude-opus-4-8[1m]`) |
| Subagent tokens | ≈ 1,714,600 |
| Agent invocations | 41 |
| Average tokens / invocation | ≈ 41,800 |
| Summed agent execution time | ≈ 2,900 s (≈ 48.3 min) compute, excluding the step-3c idle outlier; ≈ 4,036 s raw incl. outlier |
| QA audit passes | 1 (PASS — zero findings; no remediation needed) |

## Per-step breakdown

| Step | Role | Tokens | Duration (s) |
|------|------|-------:|-------------:|
| 1a | User Stakeholder — UE_* | 27,401 | 24.7 |
| 1b | Customer Stakeholder — ME_* | 27,533 | 29.5 |
| 1c | Business Stakeholder — BE_* | 28,011 | 32.8 |
| 1d | Regulatory Stakeholder — RE_* | 28,697 | 38.0 |
| 1e | Product Owner — Problem, DC_* & consolidation | 51,414 | 157.2 |
| 2a | Product Owner — KA_* | 47,474 | 76.0 |
| 2b | System Architect — KA_* co-author | 40,826 | 84.0 |
| 2c | Business Stakeholder — KA_* co-author | 39,506 | 104.3 |
| 2d | User Stakeholder — KA_* review | 39,146 | 45.7 |
| 3a | Product Owner — BR_* | 36,646 | 55.8 |
| 3b | System Architect — BR_* co-author | 38,718 | 59.9 |
| 3c | Customer Stakeholder — BR_* co-author | 39,709 | 1,139.9 * |
| 4a | Usability Validation — IU_01/MD_01 | 28,001 | 21.2 |
| 4b | Regulatory Stakeholder — IU/MD co-author | 29,502 | 36.1 |
| 4c | User Stakeholder — IU/MD review | 28,179 | 22.7 |
| 5 | System Architect — Context, IF_* & acquired parameters | 35,286 | 73.4 |
| 6a | Usability Validation — User Groups | 27,848 | 35.9 |
| 6b | Usability Validation — UR_* | 55,064 | 44.1 |
| 6c | User Stakeholder — UR_* validation | 32,092 | 44.3 |
| 6d | Usability Validation — USER_DFMEA_* | 33,360 | 74.1 |
| 6e | User Stakeholder — USER_DFMEA_* review | 34,169 | 50.2 |
| 6f | Usability Validation — Use Scenarios/UT_* | 39,478 | 56.8 |
| 6g | User Stakeholder — Use Scenarios review | 38,723 | 49.4 |
| 6h | Usability Validation — UFMEA_* | 41,694 | 95.1 |
| 6i | User Stakeholder — UFMEA_* review | 37,311 | 49.6 |
| 6j | Usability Validation — USR_* | 43,361 | 80.7 |
| 7 | Usability Validation — UI/UX Design | 56,350 | 124.8 |
| 8a–8b | System Architect — Actors & UC_* | 80,387 | 119.3 |
| 8c | User Stakeholder — UC_* review | 63,593 | 52.3 |
| 8d | System Architect — DD_* | 43,788 | 75.5 |
| 9a | System Architect — Ext. interfaces & RQ_IF_* | 37,423 | 73.5 |
| 9b | Product Owner — RQ_FN_* | 53,609 | 88.1 |
| 9c | System Architect — RQ_PR_* | 33,153 | 80.2 |
| 9d | Regulatory Stakeholder — RQ_NF_*/RQ_CS_* | 45,819 | 75.2 |
| 9e | Development Lead — RQ_* co-author | 50,942 | 181.5 |
| 9f | Product Owner — SV_* BDD draft | 58,962 | 140.8 |
| 9g | Development Lead — SV_* co-author (implementability) | 63,237 | 250.3 |
| 9h | Verification Lead — SV_* finalise (coverage) | 63,678 | 94.5 |
| 10a | Quality Assurance — audit pass 1 (PASS) | 114,473 | 98.1 |

\* Step 3c's reported duration includes a long idle/permission wait, not compute; the compute total above excludes it.

## Notes
- **Single QA pass — PASS, zero findings.** The deterministic `trace-check` structural pre-check returned `[]` (zero errors) *before* the semantic audit — it had already been run clean inside the 3-Amigos session (steps 9g/9h) — so no mechanical-traceability remediation was needed. The semantic QA audit (pass 1) then found **0 defects** (product-free, solution-level, enumerated-set, INCOSE quality, classification inheritance, IU/MD all clean), so the audit loop closed in one pass with no remediation fixes.
- Heaviest single step by duration: **9g** (Development Lead making all 24 BDD feature files implementable — reproducible preconditions, stubbed AI/HIS endpoints, concrete test-data tables) — ~250 s (excluding the 3c idle outlier).
- Heaviest by tokens: the **QA audit** (~114.5k, the one full-workbook step deliberately NOT scoped), then **8a–8b** Actors+UC (~80.4k, combined into one invocation) and the three SV steps **9g/9h/9f** (~63.2k / ~63.7k / ~59.0k).
- **Scoped context** was the active optimisation: authoring/co-author/review steps read only their target section + traced upstream sections; the QA pass reads the full workbook by design.
- The pandoc input regeneration **was run this time**: `inputs/Project_Description.md` was regenerated fresh from the `.docx` before authoring.
- **Steps 8a and 8b were combined** into a single System Architect invocation (Actors + Use Cases are adjacent, same author), giving 41 invocations rather than the per-row 42.
- Artifact volume this run: 25 DC, 50 stakeholder expectations (14 UE, 13 ME, 11 BE, 12 RE), 16 KA, 18 BR, IU_01/MD_01, 10 IF + 10 acquired-parameter rows, 5 user groups, 18 UR, 18 USER_DFMEA, 30 UT (7 use scenarios), 20 UFMEA, 21 USR, 9 actors, 13 UC, 14 DD, 14 RQ_IF, 24 RQ_FN, 16 RQ_PR, 16 RQ_NF, 12 RQ_CS, and 24 SV BDD feature files (one per RQ_FN).
