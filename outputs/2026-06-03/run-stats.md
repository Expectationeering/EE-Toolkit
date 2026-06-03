# Run Statistics — Expectationeering Flow

**Flow**: flows/expectationeering-flow/flow.md
**Workbook**: Project_Description_Workbook (.md / .docx)
**Date**: 2026-06-03
**AI model**: Claude Opus 4.8 (`claude-opus-4-8`) — orchestrator and all specialist subagents

> These figures are the **subagent** totals reported per agent invocation. They exclude the orchestrator's own token usage (reading template/inputs, sequencing, header edits) and the wall-clock spent waiting for user permissions (pandoc skip + docx conversion). Agents were run **sequentially** to protect the single live workbook from concurrent-write conflicts, so the summed duration approximates the compute wall-clock.

## Totals

| Metric | Value |
|---|---|
| AI model | Claude Opus 4.8 (`claude-opus-4-8`) |
| Subagent tokens | ≈ 2,391,000 |
| Agent invocations | 43 |
| Average tokens / invocation | ≈ 55,600 |
| Summed agent execution time | ≈ 3,409 s (≈ 56.8 min) |
| QA audit passes | 3 (final: PASS — zero findings) |

## Per-step breakdown

| Step | Role | Tokens | Duration (s) |
|------|------|-------:|-------------:|
| 1a | User Stakeholder — UE_* | 27,742 | 27.7 |
| 1b | Customer Stakeholder — ME_*/BE_* | 29,584 | 34.3 |
| 1c | Business Stakeholder — DC_* | 30,087 | 22.9 |
| 1d | Regulatory Stakeholder — RE_* | 31,186 | 30.8 |
| 1e | Product Owner — Problem & consolidation | 40,305 | 106.3 |
| 2a | Product Owner — KA_* | 35,304 | 48.9 |
| 2b | System Architect — KA_* co-author | 42,895 | 122.6 |
| 2c | Business Stakeholder — KA_* co-author | 43,880 | 105.8 |
| 2d | User Stakeholder — KA_* review | 43,729 | 85.6 |
| 3a | Product Owner — BR_* | 41,803 | 46.5 |
| 3b | System Architect — BR_* co-author | 46,730 | 81.3 |
| 3c | Customer Stakeholder — BR_* co-author | 51,559 | 98.1 |
| 4a | Usability Validation — IU_01/MD_01 | 44,412 | 24.3 |
| 4b | Regulatory Stakeholder — IU/MD co-author | 46,787 | 42.2 |
| 4c | User Stakeholder — IU/MD review | 46,399 | 41.8 |
| 5 | System Architect — Context & diagram | 50,505 | 76.5 |
| 6a+6b | Usability Validation — User Groups & UR_* | 52,387 | 77.9 |
| 6c | User Stakeholder — UR_* validation | 45,353 | 50.7 |
| 6d | Usability Validation — USER_DFMEA_* | 49,379 | 67.9 |
| 6e | User Stakeholder — USER_DFMEA_* review | 26,445 | 51.1 |
| 6f | Usability Validation — Use Scenarios/UT_* | 58,797 | 60.2 |
| 6g | User Stakeholder — Use Scenarios review | 27,535 | 35.8 |
| 6h | Usability Validation — UFMEA_* | 53,137 | 82.3 |
| 6i | User Stakeholder — UFMEA_* review | 63,852 | 71.9 |
| 6j | Usability Validation — USR_* | 63,122 | 47.1 |
| 7 | Usability Validation — UI/UX Design | 42,769 | 95.9 |
| 8a+8b | System Architect — Actors & UC_* | 76,552 | 108.1 |
| 8c | User Stakeholder — UC_* review | 37,992 | 47.5 |
| 8d | System Architect — DD_* | 55,275 | 73.5 |
| 9a | System Architect — Ext. interfaces & RQ_IF_* | 87,717 | 98.7 |
| 9b | Product Owner — RQ_FN_* | 91,100 | 70.6 |
| 9c | System Architect — RQ_PR_* | 28,963 | 45.7 |
| 9d | Regulatory Stakeholder — RQ_NF_*/RQ_CS_* | 79,962 | 96.4 |
| 9e | Development Lead — RQ_* co-author | 71,627 | 145.3 |
| 9f | Product Owner — SV_* BDD draft | 65,312 | 112.6 |
| 9g | Development Lead — SV_* co-author | 94,482 | 240.0 |
| 9h | Verification Lead — SV_* finalise | 82,378 | 146.9 |
| 10a | Quality Assurance — audit pass 1 | 125,086 | 129.5 |
| 10a | Development Lead — fix F-03 | 23,224 | 18.3 |
| 10a | Verification Lead — fix F-01/F-02 | 50,895 | 122.7 |
| 10a | Quality Assurance — audit pass 2 | 123,441 | 139.9 |
| 10a | Verification Lead — fix F-04 | 36,538 | 64.9 |
| 10a | Quality Assurance — audit pass 3 (PASS) | 124,968 | 111.6 |

## Notes
- Heaviest single step by duration: **9g** (Development Lead refining the 18 BDD feature files) — ~240 s.
- Heaviest by tokens: the three **QA audit passes** combined — ~373k tokens.
- The pandoc input regeneration was skipped at the user's request; the existing `inputs/Project_Description.md` was used.
