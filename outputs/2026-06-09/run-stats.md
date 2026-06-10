# Run Statistics — Expectationeering Flow

**Flow**: flows/expectationeering-flow/flow.md
**Workbook**: Project_Description_Workbook (.md / .docx)
**Date**: 2026-06-09
**AI model**: Claude Opus 4.8 (`claude-opus-4-8`) — orchestrator and all specialist subagents

> These figures are the **subagent** totals reported per agent invocation. They exclude the orchestrator's own token usage (reading template/inputs, sequencing, header/metadata edits) and the wall-clock spent waiting for user permissions (pandoc regeneration + docx conversion). Agents were run **sequentially** to protect the single live workbook from concurrent-write conflicts, so the summed duration approximates the compute wall-clock.

## Totals

| Metric | Value |
|---|---|
| AI model | Claude Opus 4.8 (`claude-opus-4-8`) |
| Subagent tokens | ≈ 2,636,700 |
| Agent invocations | 45 |
| Average tokens / invocation | ≈ 58,600 |
| Summed agent execution time | ≈ 4,327 s (≈ 72.1 min) |
| QA audit passes | 3 (final: PASS — zero findings) |

## Per-step breakdown

| Step | Role | Tokens | Duration (s) |
|------|------|-------:|-------------:|
| 1a | User Stakeholder — UE_* | 28,915 | 25.7 |
| 1b | Customer Stakeholder — ME_* | 29,614 | 28.0 |
| 1c | Business Stakeholder — BE_* | 31,355 | 41.6 |
| 1d | Regulatory Stakeholder — RE_* | 32,932 | 37.3 |
| 1e | Product Owner — Problem, DC_* & consolidation | 40,143 | 96.8 |
| 2a | Product Owner — KA_* | 42,307 | 64.1 |
| 2b | System Architect — KA_* co-author | 54,720 | 191.7 |
| 2c | Business Stakeholder — KA_* co-author | 52,478 | 135.2 |
| 2d | User Stakeholder — KA_* review | 51,047 | 80.7 |
| 3a | Product Owner — BR_* | 49,196 | 57.5 |
| 3b | System Architect — BR_* co-author | 51,606 | 56.6 |
| 3c | Customer Stakeholder — BR_* co-author | 51,916 | 75.8 |
| 4a | Usability Validation — IU_01/MD_01 | 51,084 | 55.5 |
| 4b | Regulatory Stakeholder — IU/MD co-author | 55,612 | 76.2 |
| 4c | User Stakeholder — IU/MD review | 50,395 | 67.6 |
| 5a | System Architect — Context, IF_* & acquired parameters | 32,760 | 69.6 |
| 6a | Usability Validation — User Groups | 48,493 | 47.4 |
| 6b | Usability Validation — UR_* | 58,342 | 51.1 |
| 6c | User Stakeholder — UR_* validation | 56,726 | 71.7 |
| 6d | Usability Validation — USER_DFMEA_* | 58,457 | 120.4 |
| 6e | User Stakeholder — USER_DFMEA_* review | 48,810 | 116.3 |
| 6f | Usability Validation — Use Scenarios/UT_* | 57,833 | 80.2 |
| 6g | User Stakeholder — Use Scenarios review | 34,724 | 82.1 |
| 6h | Usability Validation — UFMEA_* | 63,696 | 131.8 |
| 6i | User Stakeholder — UFMEA_* review | 36,511 | 79.6 |
| 6j | Usability Validation — USR_* | 49,592 | 71.6 |
| 7 | Usability Validation — UI/UX Design | 86,774 | 131.2 |
| 8a | System Architect — Actors | 39,168 | 44.9 |
| 8b | System Architect — UC_* | 62,005 | 98.2 |
| 8c | User Stakeholder — UC_* review | 80,680 | 132.7 |
| 8d | System Architect — DD_* | 56,576 | 88.0 |
| 9a | System Architect — Ext. interfaces & RQ_IF_* | 61,044 | 85.4 |
| 9b | Product Owner — RQ_FN_* | 92,751 | 89.2 |
| 9c | System Architect — RQ_PR_* | 61,607 | 57.0 |
| 9d | Regulatory Stakeholder — RQ_NF_*/RQ_CS_* | 62,701 | 130.7 |
| 9e | Development Lead — RQ_* co-author | 48,178 | 149.4 |
| 9f | Product Owner — SV_* BDD draft | 58,698 | 159.1 |
| 9g | Development Lead — SV_* co-author (implementability) | 81,581 | 333.9 |
| 9h | Verification Lead — SV_* finalise (coverage) | 75,377 | 230.4 |
| 10a | Quality Assurance — audit pass 1 | 153,732 | 195.6 |
| 10a | Product Owner — fix F-01..F-06 (KA_* traces, BR_* coverage) | 36,359 | 45.5 |
| 10a | System Architect — fix F-07 (RQ_PR_10 rationale) | 24,970 | 26.2 |
| 10a | Quality Assurance — audit pass 2 | 154,828 | 145.1 |
| 10a | System Architect — fix DD_08 rationale (ALGOS leak) | 24,318 | 17.0 |
| 10a | Quality Assurance — audit pass 3 (PASS) | 156,058 | 155.5 |

## Notes
- Heaviest single step by duration: **9g** (Development Lead making all 26 BDD feature files implementable — concrete preconditions, test data, external-element stubs) — ~334 s.
- Heaviest by tokens: the three **QA audit passes** (~154–156k each, ~464k combined, full-workbook traceability + INCOSE sweeps); heaviest single authoring step **9b** (RQ_FN_*) at ~92.8k.
- The pandoc input regeneration **was run this time** (user approved): `inputs/Project_Description.md` was regenerated fresh from the `.docx` before authoring.
- **3 QA passes** were needed: pass 1 raised **7** findings (6 KA→DC backwards-trace / BR-coverage issues → Product Owner; 1 internal-item-name leak in RQ_PR_10 rationale → System Architect); pass 2 confirmed those resolved but surfaced **1** sibling leak (DD_08 rationale naming "ALGOS") → System Architect; pass 3 returned **PASS — zero findings**.
- Artifact volume this run: 23 DC, 38 stakeholder expectations (10 UE, 9 ME, 9 BE, 10 RE), 14 KA, 19 BR, IU_01/MD_01, 10 IF + 11 acquired-parameter rows, 5 user groups, 17 UR, 20 USER_DFMEA, 29 UT, 17 UFMEA, 17 USR, 11 actors, 13 UC, 13 DD, 14 RQ_IF, 26 RQ_FN, 13 RQ_PR, 15 RQ_NF, 10 RQ_CS, and 26 SV BDD feature files (62 scenarios).
