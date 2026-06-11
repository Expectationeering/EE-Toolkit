# Run Statistics — Expectationeering Flow

**Flow**: flows/expectationeering-flow/flow.md
**Workbook**: Project_Description_Workbook (.md / .docx)
**Date**: 2026-06-11
**AI model**: Claude Opus 4.8 (`claude-opus-4-8`) — orchestrator and all specialist subagents

> These figures are the **subagent** totals reported per agent invocation. They exclude the orchestrator's own token usage (reading template/inputs, sequencing, header/metadata edits) and the wall-clock spent waiting for user permissions (pandoc regeneration + docx conversion). Agents were run **sequentially** to protect the single live workbook from concurrent-write conflicts, so the summed duration approximates the compute wall-clock.

> **Optimisation note — this run used "scoped context" (lever A).** Per the updated orchestration procedure, each authoring/co-author/review step received only its own template section(s) plus the specific upstream section(s) it traces to (extracted from the live workbook), instead of the full growing workbook. Agents read only their own section's line range before editing. The QA audit still reads the full workbook by design (lever B was not adopted). Net effect vs the 2026-06-09 baseline: **≈ 1.69M vs ≈ 2.64M subagent tokens (≈ 36% reduction)**, with the same artifact coverage and a defect-free result.

## Totals

| Metric | Value |
|---|---|
| AI model | Claude Opus 4.8 (`claude-opus-4-8`) |
| Subagent tokens | ≈ 1,693,000 |
| Agent invocations | 44 |
| Average tokens / invocation | ≈ 38,500 |
| Summed agent execution time | ≈ 3,800 s (≈ 63.3 min) |
| QA audit passes | 2 (final: PASS — zero findings) |

**Baseline comparison (2026-06-09 run):** ≈ 2,636,700 tokens, 45 invocations, ≈ 58,600 avg/invocation, ≈ 4,327 s, 3 QA passes. Scoped context cut **≈ 944,000 tokens (≈ 36%)** and one QA pass.

## Per-step breakdown

| Step | Role | Tokens | Duration (s) |
|------|------|-------:|-------------:|
| 1a | User Stakeholder — UE_* | 24,165 | 33.0 |
| 1b | Customer Stakeholder — ME_* | 23,967 | 29.4 |
| 1c | Business Stakeholder — BE_* | 24,415 | 26.5 |
| 1d | Regulatory Stakeholder — RE_* | 25,362 | 37.0 |
| 1e | Product Owner — Problem, DC_* & consolidation | 39,957 | 127.1 |
| 2a | Product Owner — KA_* | 28,697 | 50.0 |
| 2b | System Architect — KA_* co-author | 34,472 | 108.9 |
| 2c | Business Stakeholder — KA_* co-author | 31,538 | 72.8 |
| 2d | User Stakeholder — KA_* review | 28,333 | 27.7 |
| 3a | Product Owner — BR_* | 28,343 | 58.8 |
| 3b | System Architect — BR_* co-author | 31,304 | 81.4 |
| 3c | Customer Stakeholder — BR_* co-author | 30,533 | 69.3 |
| 4a | Usability Validation — IU_01/MD_01 | 22,696 | 27.8 |
| 4b | Regulatory Stakeholder — IU/MD co-author | 22,156 | 38.9 |
| 4c | User Stakeholder — IU/MD review | 20,021 | 15.1 |
| 5a | System Architect — Context, IF_* & acquired parameters | 35,369 | 74.3 |
| 6a | Usability Validation — User Groups | 21,165 | 28.9 |
| 6b | Usability Validation — UR_* | 35,845 | 42.6 |
| 6c | User Stakeholder — UR_* validation | 24,088 | 30.9 |
| 6d | Usability Validation — USER_DFMEA_* | 26,116 | 67.1 |
| 6e | User Stakeholder — USER_DFMEA_* review | 28,192 | 61.5 |
| 6f | Usability Validation — Use Scenarios/UT_* | 29,990 | 52.3 |
| 6g | User Stakeholder — Use Scenarios review | 30,487 | 33.7 |
| 6h | Usability Validation — UFMEA_* | 31,229 | 94.1 |
| 6i | User Stakeholder — UFMEA_* review | 29,815 | 38.8 |
| 6j | Usability Validation — USR_* | 43,762 | 47.9 |
| 7 | Usability Validation — UI/UX Design | 46,615 | 92.4 |
| 8a | System Architect — Actors | 27,629 | 24.7 |
| 8b | System Architect — UC_* | 51,741 | 87.8 |
| 8c | User Stakeholder — UC_* review | 46,082 | 58.4 |
| 8d | System Architect — DD_* | 36,620 | 73.5 |
| 9a | System Architect — Ext. interfaces & RQ_IF_* | 26,402 | 56.9 |
| 9b | Product Owner — RQ_FN_* | 49,091 | 68.6 |
| 9c | System Architect — RQ_PR_* | 28,915 | 45.3 |
| 9d | Regulatory Stakeholder — RQ_NF_*/RQ_CS_* | 40,603 | 80.6 |
| 9e | Development Lead — RQ_* co-author | 37,453 | 92.2 |
| 9f | Product Owner — SV_* BDD draft | 48,960 | 140.6 |
| 9g | Development Lead — SV_* co-author (implementability) | 71,166 | 658.1 |
| 9h | Verification Lead — SV_* finalise (coverage) | 66,282 | 189.3 |
| 10a | Quality Assurance — audit pass 1 | 131,343 | 516.1 |
| 10a | Product Owner — fix F-01/F-02 (header/intro, BR ID order) | 25,822 | 40.5 |
| 10a | Verification Lead — fix F-05/F-06/F-07 (RQ_IF/CS/NF coverage) | 46,072 | 53.6 |
| 10a | Usability Validation — fix F-09 (alarm UR traces) | 35,963 | 48.0 |
| 10a | Quality Assurance — audit pass 2 (PASS) | 124,269 | 97.5 |

## Notes
- Heaviest single step by duration: **9g** (Development Lead making all 28 BDD feature files implementable — concrete preconditions, injectable test data, ~14 added exception scenarios) — ~658 s.
- Heaviest by tokens: the two **QA audit passes** (~131k + ~124k ≈ 255k combined, full-workbook traceability + INCOSE sweeps — the one step deliberately NOT scoped); heaviest single authoring step **9g** (SV implementability) at ~71.2k, then **9h** (~66.3k).
- **Scoped context** was the active optimisation this run: authoring/co-author/review steps read only their target section + traced upstream sections. Most-improved steps vs baseline: 4c (50.4k→20.0k), 8c (80.7k→46.1k), 9a (61.0k→26.4k), 6d (58.5k→26.1k), 6a (48.5k→21.2k). The QA passes were unchanged (full-workbook by design).
- The pandoc input regeneration **was run this time** (user approved): `inputs/Project_Description.md` was regenerated fresh from the `.docx` before authoring.
- **2 QA passes** were needed (one fewer than baseline): pass 1 raised **9** findings, of which **3** (`_To be added_` diagram placeholders for Context/UC/black-box) were rejected as false positives — the flow requires those placeholders to remain — and **6** were routed and fixed (header/intro placeholders + BR ID order → Product Owner; RQ_IF_14/RQ_CS_04/RQ_CS_09 + ten RQ_NF_* verification coverage → Verification Lead; alarm/fault UR traces → Usability Validation); pass 2 returned **PASS — zero findings**.
- Artifact volume this run: 14 DC, 42 stakeholder expectations (11 UE, 10 ME, 10 BE, 11 RE), 16 KA, 22 BR, IU_01/MD_01, 6 IF + 17 acquired-parameter rows, 5 user groups, 20 UR, 22 USER_DFMEA, 30 UT (7 use scenarios), 21 UFMEA, 20 USR, 10 actors, 15 UC, 14 DD, 14 RQ_IF, 28 RQ_FN, 15 RQ_PR, 16 RQ_NF, 11 RQ_CS, and 28 SV BDD feature files plus one `@verification:by-review` coverage feature.
