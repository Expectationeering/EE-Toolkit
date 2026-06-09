# Run Statistics — Expectationeering Flow

**Flow**: flows/expectationeering-flow/flow.md
**Workbook**: Project_Description_Workbook (.md / .docx)
**Date**: 2026-06-09
**AI model**: Claude Opus 4.8 (`claude-opus-4-8`) — orchestrator and all specialist subagents

> These figures are the **subagent** totals reported per agent invocation. They exclude the orchestrator's own token usage (reading template/inputs, sequencing, header edits) and the wall-clock spent waiting for user permissions (pandoc regeneration + docx conversion). Agents were run **sequentially** to protect the single live workbook from concurrent-write conflicts, so the summed duration approximates the compute wall-clock.

## Totals

| Metric | Value |
|---|---|
| AI model | Claude Opus 4.8 (`claude-opus-4-8`) |
| Subagent tokens | ≈ 2,105,000 |
| Agent invocations | 42 |
| Average tokens / invocation | ≈ 50,100 |
| Summed agent execution time | ≈ 3,306 s (≈ 55.1 min) |
| QA audit passes | 2 (final: PASS — zero findings) |

## Per-step breakdown

| Step | Role | Tokens | Duration (s) |
|------|------|-------:|-------------:|
| 1a | User Stakeholder — UE_* | 28,312 | 23.5 |
| 1b | Customer Stakeholder — ME_* | 28,953 | 28.0 |
| 1c | Business Stakeholder — BE_* | 30,801 | 28.6 |
| 1d | Regulatory Stakeholder — RE_* | 32,270 | 32.7 |
| 1e | Product Owner — Problem, DC_* & consolidation | 43,941 | 138.3 |
| 2a | Product Owner — KA_* | 37,507 | 43.6 |
| 2b | System Architect — KA_* co-author | 44,056 | 97.4 |
| 2c | Business Stakeholder — KA_* co-author | 45,465 | 110.4 |
| 2d | User Stakeholder — KA_* review | 37,756 | 40.7 |
| 3a | Product Owner — BR_* | 42,113 | 39.8 |
| 3b | System Architect — BR_* co-author | 45,673 | 67.6 |
| 3c | Customer Stakeholder — BR_* co-author | 45,710 | 71.9 |
| 4a | Usability Validation — IU_01/MD_01 | 44,251 | 20.7 |
| 4b | Regulatory Stakeholder — IU/MD co-author | 45,911 | 42.7 |
| 4c | User Stakeholder — IU/MD review | 41,356 | 24.0 |
| 5a | System Architect — Context & diagram | 51,311 | 659.6 |
| 6a+6b | Usability Validation — User Groups & UR_* | 51,232 | 54.1 |
| 6c | User Stakeholder — UR_* validation | 24,991 | 29.3 |
| 6d | Usability Validation — USER_DFMEA_* | 55,010 | 68.5 |
| 6e | User Stakeholder — USER_DFMEA_* review | 53,351 | 48.9 |
| 6f | Usability Validation — Use Scenarios/UT_* | 58,213 | 52.5 |
| 6g | User Stakeholder — Use Scenarios review | 30,335 | 41.2 |
| 6h | Usability Validation — UFMEA_* | 60,901 | 104.2 |
| 6i | User Stakeholder — UFMEA_* review | 28,867 | 48.7 |
| 6j | Usability Validation — USR_* | 66,633 | 46.5 |
| 7 | Usability Validation — UI/UX Design | 70,614 | 77.4 |
| 8a+8b | System Architect — Actors & UC_* | 79,152 | 110.1 |
| 8c | User Stakeholder — UC_* review | 33,237 | 42.2 |
| 8d | System Architect — DD_* | 74,098 | 83.4 |
| 9a | System Architect — Ext. interfaces & RQ_IF_* | 74,037 | 96.3 |
| 9b | Product Owner — RQ_FN_* | 87,370 | 76.4 |
| 9c | System Architect — RQ_PR_* | 28,201 | 37.1 |
| 9d | Regulatory Stakeholder — RQ_NF_*/RQ_CS_* | 53,363 | 80.8 |
| 9e | Development Lead — RQ_* co-author | 63,751 | 87.6 |
| 9f | Product Owner — SV_* BDD draft | 43,638 | 105.2 |
| 9g | Development Lead — SV_* co-author | 63,246 | 261.2 |
| 9h | Verification Lead — SV_* finalise | 75,263 | 52.6 |
| 10a | Quality Assurance — audit pass 1 | 113,232 | 77.5 |
| 10a | Product Owner — fix F-01/F-02/F-03 (RQ_FN, SV) | 26,985 | 42.9 |
| 10a | System Architect — fix F-03 (RQ_IF/RQ_PR datum) | 21,307 | 23.4 |
| 10a | Usability Validation — fix F-04 (UR_11 trace) | 20,282 | 20.1 |
| 10a | Quality Assurance — audit pass 2 (PASS) | 102,777 | 68.1 |

## Notes
- Heaviest single step by duration: **5a** (System Architect authoring **and rendering** the Graphviz context diagram to validate it) — ~660 s.
- Heaviest by tokens: the two **QA audit passes** combined — ~216k tokens; heaviest single authoring step **9b** (RQ_FN_*) at ~87k.
- The pandoc input regeneration **was run this time** (user approved): `inputs/Project_Description.md` was regenerated fresh from the `.docx`.
- Only **2 QA passes** were needed (pass 1 raised 4 trace/consistency findings → corrected by their owners → pass 2 PASS), one fewer than the prior run, reflecting the artifact-authoring guidance now baked into the agents and `flow.md`.
- Artifact volume this run: 7 DC, 40 stakeholder expectations (UE/ME/BE/RE), 10 KA, 14 BR, IU_01/MD_01, 10 IF, 16 UR, 13 USER_DFMEA, 20 UT, 13 UFMEA, 14 USR, 10 actors, 11 UC, 11 DD, 23 RQ_IF, 27 RQ_FN, 13 RQ_PR, 14 RQ_NF, 8 RQ_CS, 27 SV feature files.
