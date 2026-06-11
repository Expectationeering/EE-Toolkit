# Run Statistics — Expectationeering Flow

**Flow**: flows/expectationeering-flow/flow.md
**Workbook**: Project_Description_Workbook (.md / .docx)
**Date**: 2026-06-11
**AI model**: Claude Fable 5 (`claude-fable-5`) — orchestrator and all specialist subagents

> These figures are the **subagent** totals reported per agent invocation. They exclude the orchestrator's own token usage (reading template/inputs, sequencing, header/metadata edits) and the wall-clock spent waiting for user permissions (pandoc regeneration + docx conversion). Agents were run **sequentially** to protect the single live workbook from concurrent-write conflicts, so the summed duration approximates the compute wall-clock.

> **Optimisation note — scoped context (lever A) active**, per the orchestration procedure: each authoring/co-author/review step received only its own template section(s) plus the upstream section(s) it traces to, with Read offset/limit instructions; the QA audit reads the full workbook by design. The orchestrator additionally pre-filled the header/intro placeholders and SOLUTION name before the audit, avoiding the header-placeholder findings seen in earlier runs.

## Totals

| Metric | Value |
|---|---|
| AI model | Claude Fable 5 (`claude-fable-5`) |
| Subagent tokens | ≈ 1,760,700 |
| Agent invocations | 42 |
| Average tokens / invocation | ≈ 41,900 |
| Summed agent execution time | ≈ 9,431 s (≈ 157 min; ≈ 4,381 s / 73 min excluding QA pass 2 — see Notes) |
| QA audit passes | 2 (final: PASS — zero findings) |

**Baseline comparison (2026-06-11 Opus run, scoped context):** ≈ 1,693,000 tokens, 44 invocations, ≈ 38,500 avg/invocation, ≈ 3,800 s, 2 QA passes. This Fable 5 run used ≈ 4% more tokens with 2 fewer invocations and needed only **1 finding fixed** across the QA loop (vs 6 routed fixes in the Opus run).

## Per-step breakdown

| Step | Role | Tokens | Duration (s) |
|------|------|-------:|-------------:|
| 1a | User Stakeholder — UE_* | 26,456 | 31.7 |
| 1b | Customer Stakeholder — ME_* | 26,419 | 28.5 |
| 1c | Business Stakeholder — BE_* | 28,196 | 35.9 |
| 1d | Regulatory Stakeholder — RE_* | 28,833 | 38.2 |
| 1e | Product Owner — Problem, DC_* & consolidation | 49,067 | 186.4 |
| 2a | Product Owner — KA_* | 41,566 | 109.7 |
| 2b | System Architect — KA_* co-author | 43,238 | 98.7 |
| 2c | Business Stakeholder — KA_* co-author | 40,230 | 87.6 |
| 2d | User Stakeholder — KA_* review | 36,825 | 35.8 |
| 3a | Product Owner — BR_* | 38,613 | 87.6 |
| 3b | System Architect — BR_* co-author | 37,483 | 49.2 |
| 3c | Customer Stakeholder — BR_* co-author | 35,265 | 41.2 |
| 4a | Usability Validation — IU_01/MD_01 | 26,539 | 19.7 |
| 4b | Regulatory Stakeholder — IU/MD co-author | 28,289 | 41.9 |
| 4c | User Stakeholder — IU/MD review | 26,053 | 15.8 |
| 5a | System Architect — Context, IF_* & acquired parameters | 32,541 | 64.3 |
| 6a | Usability Validation — User Groups | 27,037 | 25.7 |
| 6b | Usability Validation — UR_* | 39,420 | 54.1 |
| 6c | User Stakeholder — UR_* validation | 31,588 | 55.2 |
| 6d | Usability Validation — USER_DFMEA_* | 35,074 | 99.5 |
| 6e | User Stakeholder — USER_DFMEA_* review | 37,794 | 76.2 |
| 6f | Usability Validation — Use Scenarios/UT_* | 33,532 | 66.4 |
| 6g | User Stakeholder — Use Scenarios review | 35,901 | 72.9 |
| 6h | Usability Validation — UFMEA_* | 36,660 | 111.6 |
| 6i | User Stakeholder — UFMEA_* review | 38,150 | 65.3 |
| 6j | Usability Validation — USR_* | 39,396 | 72.2 |
| 7 | Usability Validation — UI/UX Design | 36,449 | 76.1 |
| 8a | System Architect — Actors | 29,498 | 27.4 |
| 8b | System Architect — UC_* | 41,327 | 91.6 |
| 8c | User Stakeholder — UC_* review | 37,160 | 64.8 |
| 8d | System Architect — DD_* | 41,443 | 77.9 |
| 9a | System Architect — Ext. interfaces & RQ_IF_* | 34,446 | 80.6 |
| 9b | Product Owner — RQ_FN_* | 46,793 | 131.5 |
| 9c | System Architect — RQ_PR_* | 32,849 | 47.4 |
| 9d | Regulatory Stakeholder — RQ_NF_*/RQ_CS_* | 40,324 | 115.8 |
| 9e | Development Lead — RQ_* co-author | 50,535 | 159.9 |
| 9f | Product Owner — SV_* BDD draft | 46,020 | 168.2 |
| 9g | Development Lead — SV_* co-author (implementability) | 66,097 | 293.8 |
| 9h | Verification Lead — SV_* finalise (coverage) | 77,714 | 330.4 |
| 10a | Quality Assurance — audit pass 1 | 135,729 | 1,021.0 |
| 10a | Product Owner — fix F-01 (RQ_FN_22 trace UR_04 → UR_22) | 24,220 | 23.3 |
| 10a | Quality Assurance — audit pass 2 (PASS) | 119,913 | 5,050.3 |

## Notes
- Heaviest by tokens: the two **QA audit passes** (≈ 135.7k + 119.9k ≈ 256k combined — full-workbook by design); heaviest authoring step **9h** (Verification Lead coverage finalisation, ≈ 77.7k), then **9g** (≈ 66.1k).
- Heaviest by duration: **QA pass 2** at ≈ 5,050 s wall-clock — far above its compute profile (similar token count to pass 1 at ≈ 1,021 s), so most of it is presumed API wait/retry time rather than work; the summed-duration total is therefore quoted with and without it.
- The pandoc input regeneration **was run** (user approved): `inputs/Project_Description.md` regenerated fresh from the `.docx` before authoring.
- **2 QA passes**, with only **1 finding** in pass 1 (RQ_FN_22 traced UR_04 instead of UR_22) — routed to the Product Owner, fixed as a one-cell change, and pass 2 returned **PASS — zero findings**. The orchestrator pre-filling header/intro/SOLUTION placeholders eliminated the placeholder findings seen in earlier runs.
- Artifact volume this run: 17 DC, 48 stakeholder expectations (12 UE, 12 ME, 12 BE, 12 RE), 16 KA, 24 BR, IU_01/MD_01, 11 IF + 11 acquired-parameter rows, 6 user groups, 22 UR, 19 USER_DFMEA, 29 UT (7 use scenarios), 20 UFMEA, 20 USR, 16 actors, 14 UC, 13 DD, 12 RQ_IF, 26 RQ_FN, 10 RQ_PR, 11 RQ_NF, 8 RQ_CS, and 26 SV BDD feature files plus one `@verification:by-review` coverage feature.
