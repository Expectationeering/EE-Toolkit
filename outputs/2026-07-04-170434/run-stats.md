# Run Statistics — Expectationeering Flow

**Flow**: flows/expectationeering-flow/flow.md
**Workbook**: Project_Description_Workbook (.md / .docx)
**Date**: 2026-07-04
**AI model**: Claude Fable 5 (`claude-fable-5`) — orchestrator and all specialist subagents

> These figures are the **subagent** totals reported per agent invocation. They exclude the orchestrator's own token usage (scoped-context extraction, section pasting, mechanical fixes, trace-checks, docx conversion) and any wait-for-permission time. **Optimisations active this run:** scoped context, **return-content protocol** (agents return sections; the orchestrator pastes — no agent file edits), **parallel groups** (1a–1d, 9c∥9d, QA sub-audits, remediation fixers), per-phase trace-checks, gherkin-sv skill injection (steps 9f–9h + SV sub-audit only), and the **QA audit split into four parallel scoped sub-audits**. Steps 6a+6b and 8a+8b ran as combined invocations; review steps 2d and 4c were folded into co-author steps 2c and 4b.

## Totals

| Metric | Value |
|---|---|
| AI model | Claude Fable 5 (`claude-fable-5`) |
| Subagent tokens | ≈ 1,890,000 |
| Agent invocations | 44 |
| Average tokens / invocation | ≈ 43,000 |
| Summed agent execution time | ≈ 4,915 s (≈ 82 min); wall-clock ≈ 63 min thanks to the parallel groups |
| QA audit passes | 2 (final: **PASS — zero findings**); trace-check ran clean per phase and at close |

**Baseline comparison (2026-06-15 Opus run, scoped context only):** ≈ 1,714,600 tokens, 41 invocations, ≈ 48 min, 1 QA pass with 0 findings.
- **Authoring (phases 1–9): ≈ 1,321,000 tokens vs ≈ 1,600,000 baseline → −17%**, and wall-clock per phase fell sharply where parallelism applied (phase 1: 107 s vs 282 s).
- **QA (phase 10): ≈ 569,000 tokens vs ≈ 114,500 baseline** — the four scoped sub-audits were far more thorough: they raised **34 findings** (31 accepted and fixed, 3 rejected as intentional template placeholders) where the baseline full-workbook pass found none, at the cost of a remediation round (4 parallel fixers + 1 focused re-audit).
- Net: ≈ +10% tokens vs baseline, traded for a materially deeper audit and 31 fixed defects.

## Per-step breakdown

| Step | Role | Tokens | Duration (s) |
|------|------|-------:|-------------:|
| 1a ∥ | User Stakeholder — UE_* | 26,930 | 30.0 |
| 1b ∥ | Customer Stakeholder — ME_* | 27,132 | 33.5 |
| 1c ∥ | Business Stakeholder — BE_* | 28,269 | 37.3 |
| 1d ∥ | Regulatory Stakeholder — RE_* | 28,044 | 35.9 |
| 1e | Product Owner — Problem, DC_* & consolidation | 34,651 | 69.8 |
| 2a | Product Owner — KA_* | 32,738 | 76.6 |
| 2b | System Architect — KA_* co-author | 35,835 | 79.5 |
| 2c | Business Stakeholder — KA_* co-author (+ US review checklist) | 36,036 | 122.7 |
| 3a | Product Owner — BR_* | 32,702 | 78.4 |
| 3b | System Architect — BR_* co-author | 33,129 | 65.7 |
| 3c | Customer Stakeholder — BR_* co-author | 33,341 | 74.9 |
| 4a | Usability Validation — IU_01/MD_01 | 25,437 | 13.5 |
| 4b | Regulatory Stakeholder — IU/MD co-author (+ US clinical checklist) | 27,477 | 28.5 |
| 5a | System Architect — Context, IF_* & acquired parameters | 28,985 | 34.0 |
| 6a+6b | Usability Validation — User Groups + UR_* (combined) | 36,723 | 267.0 |
| 6c | User Stakeholder — UR_* validation | 29,602 | 52.6 |
| 6d | Usability Validation — USER_DFMEA_* | 30,832 | 83.3 |
| 6e | User Stakeholder — USER_DFMEA_* review | 37,200 | 89.5 |
| 6f | Usability Validation — Use Scenarios/UT_* | 29,115 | 55.3 |
| 6g | User Stakeholder — Use Scenarios review | 37,990 | 70.4 |
| 6h | Usability Validation — UFMEA_* | 40,246 | 128.2 |
| 6i | User Stakeholder — UFMEA_* review | 41,717 | 108.2 |
| 6j | Usability Validation — USR_* | 40,955 | 51.8 |
| 7 | Usability Validation — UI/UX Design | 46,119 | 125.1 |
| 8a+8b | System Architect — Actors + UC_* (combined) | 61,877 | 169.3 |
| 8c | User Stakeholder — UC_* review | 29,265 | 127.5 |
| 8d | System Architect — DD_* | 76,734 | 118.4 |
| 9a | System Architect — Ext. interfaces & RQ_IF_* | 40,314 | 66.8 |
| 9b | Product Owner — RQ_FN_* | 79,715 | 122.4 |
| 9c ∥ | System Architect — RQ_PR_* | 35,818 | 60.9 |
| 9d ∥ | Regulatory Stakeholder — RQ_NF_*/RQ_CS_* | 40,912 | 96.5 |
| 9e | Development Lead — RQ_* co-author | 38,664 | 179.5 |
| 9f | Product Owner — SV_* BDD draft | 44,789 | 104.9 |
| 9g | Development Lead — SV_* co-author (returned only changed features) | 31,627 | 153.2 |
| 9h | Verification Lead — SV_* finalise (coverage + by-review block) | 40,036 | 211.3 |
| 10a ∥ | Quality Assurance — sub-audit 1: informal domain (4 findings) | 45,432 | 174.5 |
| 10a ∥ | Quality Assurance — sub-audit 2: usability chain (10 findings) | 95,210 | 302.9 |
| 10a ∥ | Quality Assurance — sub-audit 3: requirements (13 findings, 3 rejected) | 117,782 | 416.2 |
| 10a ∥ | Quality Assurance — sub-audit 4: SV verification (7 findings) | 85,443 | 240.7 |
| 10a ∥ | Product Owner — remediation (BR splits, RQ_FN bounds, new RQ_FN_19/20, SV) | 18,518 | 107.3 |
| 10a ∥ | Usability Validation — remediation (user group, USR quantification) | 12,572 | 39.4 |
| 10a ∥ | System Architect — remediation (UC_02/09, RQ_PR_07) | 49,733 | 89.6 |
| 10a ∥ | Verification Lead — remediation (SV coverage scenarios, by-review rows) | 29,901 | 109.4 |
| 10a | Quality Assurance — focused re-audit (3 residual propagation fixes, then PASS) | 114,703 | 213.2 |

∥ = ran in a parallel group; group wall-clock equals the slowest member, not the column sum.

## Notes

- **QA loop:** trace-check ran clean per phase and returned **PASS with zero errors before the semantic audit** — the per-phase checks prevented all mechanical traceability remediation. The four parallel sub-audits raised 34 findings; 3 were rejected by the orchestrator as known non-findings (the flow-mandated `_To be added_` diagram placeholders); 12 prescribed single-cell/wording corrections were applied directly by the orchestrator; 19 substantive corrections were authored by four parallel owner-fixers; a focused re-audit confirmed closure and surfaced 3 residual propagation defects (fixed per its prescribed corrections, trace-check PASS). Final verdict: **PASS**.
- Heaviest by tokens: QA sub-audit 3 (requirements, ≈ 117.8k) and the focused re-audit (≈ 114.7k); heaviest authoring step: **9b** RQ_FN (≈ 79.7k) and **8d** DD (≈ 76.7k) — both driven by agents reading broad upstream context from the workbook.
- Biggest authoring savings vs baseline: 6a+6b combined (36.7k vs 82.9k, −56%), phase 4 (52.9k vs 85.7k, −38%), phase 2 (104.6k vs 166.9k, −37%); the return-content protocol eliminated all agent Read/Edit round-trips on the workbook (0 file edits by agents).
- The 9g/9h "return only changed features" pattern halved the 3-Amigos co-author cost (31.6k + 40.0k vs baseline 66.1k + 77.7k).
- Pandoc input regeneration **was run**: `inputs/Project_Description.md` regenerated fresh from the `.docx` before authoring. The .docx conversion (`populate_docx.py`) succeeded (563 KB).
- Artifact volume this run: 14 DC, 60 stakeholder expectations (15 UE, 15 ME, 15 BE, 15 RE), 17 KA, 26 BR, IU_01/MD_01, 10 IF + 12 acquired-parameter rows, 7 user groups, 21 UR, 19 USER_DFMEA, 32 UT (8 use scenarios), 20 UFMEA, 21 USR, 12 actors, 13 UC, 13 DD, 12 RQ_IF, 20 RQ_FN, 10 RQ_PR, 12 RQ_NF, 8 RQ_CS, and 20 SV BDD feature files plus one `@verification:by-review` coverage feature.
