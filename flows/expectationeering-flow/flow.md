# Expectationeering Flow

## Metadata

| Key | Value |
|-----|-------|
| Templates | expectationeering-workbook.md |
| Date in filename | false |
| Docx template | Expectationeering-Workbook.docx |
| Convert command | uv run python scripts/populate_docx.py "{md}" "flows/expectationeering-flow/Expectationeering-Workbook.docx" "{docx}" |

## Stakeholders

This flow considers input from all four stakeholders.

| Stakeholder | Role in this flow |
|---|---|
| User Stakeholder | Voices end-user goals, daily context, pain points, and acceptance perspective — primary input for UE_*, UR_*, USER_DFMEA_*, UT_*, UFMEA_*, USR_*, UC_* |
| Customer Stakeholder | Voices buying criteria, business value, and commercial constraints — primary input for ME_*, BE_*, BR_* |
| Business Stakeholder | Voices organisational strategy, internal constraints, liability, and manufacturability — primary input for DC_*, KA_*, DD_* |
| Regulatory Stakeholder | Voices mandatory market access requirements, approval criteria, and evidence obligations — primary input for RE_*, IU_01, MD_01, RQ_NF_*, RQ_CS_* |

## Scope

This flow fills the workbook from the informal stakeholder expectations through to verifiable system requirements (Verification, `SV_*`). The Architecture, Detailed Design, system DFMEA, and Items sections are left as empty template for downstream design work and are out of scope for this flow.

## 3-Amigos session

Steps 9f–9h form a **3-Amigos session**: the **Product Owner** (business intent), **Development Lead** (feasibility), and **Verification Lead** (testability) jointly define **one Gherkin BDD feature file per functional requirement**. Each feature file is tagged `@ID:RQ_FN_xx` (tracing it to the requirement), opens with a user story (As a / I want / So that) and a `Rule:` capturing the "shall" statement, and contains concrete `Scenario`s with `Given / When / Then` steps and data tables for the expected values, using measurable outcomes. The feature files are recorded directly in the workbook's **Verification** section (`SV_*`) — one feature file per `SV_*` row — so the verification entries *are* the executable specification of the functional requirements. The Product Owner drafts each feature, the Development Lead refines it for implementability, and the Verification Lead finalises it for testability and full requirement coverage.

## Steps

| Step | Role | Mode | Artifact | Sequencing |
|------|------|------|----------|------------|
| 1a | User Stakeholder | author | UE_* — user expectations, daily context, pain points | parallel with 1b–1d |
| 1b | Customer Stakeholder | author | ME_*, market expectations, commercial constraints | parallel with 1a |
| 1c | Business Stakeholder | author | BE_* — business expectations, organisational strategy and liability | parallel with 1a |
| 1d | Regulatory Stakeholder | author | RE_* — mandatory regulatory expectations and approval criteria | parallel with 1a |
| 1e | Product Owner | author | Problem (Domain Description, Actual State, Desired State, Identified Gaps) and consolidation: tracing UE/ME/BE/RE to DC | sequential after 1a–1d; gates 2a |
| 2a | Product Owner | author | KA_* — Ideal Product Model, tracing from KA to UE/ME/BE/RE | sequential after 1e |
| 2b | System Architect | co-author | KA_* — feasibility, proposition attributes, and risk validation | parallel with 2a |
| 2c | Business Stakeholder | co-author | KA_* — organisational, manufacturability and liability view | parallel with 2a |
| 2d | User Stakeholder | review | KA_* — domain review | sequential after 2b; gates 3a |
| 3a | Product Owner | author | BR_* — Business Requirements, tracing from BR to KA | sequential after 2d |
| 3b | System Architect | co-author | BR_* — technical and architectural alignment | parallel with 3a |
| 3c | Customer Stakeholder | co-author | BR_* — buying criteria and commercial alignment | parallel with 3a; gates 4a |
| 4a | Usability Validation | author | IU_01, MD_01 — Intended Use and Medical Device Classification, tracing from MD_01 to IU_01 | sequential after 3c |
| 4b | Regulatory Stakeholder | co-author | IU_01, MD_01 — market access and approval criteria | parallel with 4a |
| 4c | User Stakeholder | review | IU_01, MD_01 — clinical review | parallel with 4a; gates 5a |
| 5a | System Architect | author | Product Information, System of Interest, Context Elements, IF_*, and the context diagram authored as Graphviz DOT (SOI cluster + context nodes + IF_* edges) | sequential after 4c; gates 6a |
| 6a | Usability Validation | author | User Groups | sequential after 5a |
| 6b | Usability Validation | author | UR_* — User Requirements, tracing from UR to IU_01/BR | sequential after 6a |
| 6c | User Stakeholder | co-author | UR_* — clinical validation of user requirements | parallel with 6b; gates 6d |
| 6d | Usability Validation | author | USER_DFMEA_* — User DFMEA, tracing from USER_DFMEA to UR | sequential after 6c |
| 6e | User Stakeholder | co-author | USER_DFMEA_* — clinical review of user failure modes | parallel with 6d; gates 6f |
| 6f | Usability Validation | author | UT_* — Use Scenarios / use tasks, tracing from UT to UR | sequential after 6e |
| 6g | User Stakeholder | co-author | UT_* — clinical review of use scenarios | parallel with 6f; gates 6h |
| 6h | Usability Validation | author | UFMEA_* — Usability FMEA, tracing from UFMEA to UT | sequential after 6g |
| 6i | User Stakeholder | co-author | UFMEA_* — clinical review of usability failure modes | parallel with 6h; gates 6j |
| 6j | Usability Validation | author | USR_* — Usability Requirements, tracing from USR to UR/UFMEA | sequential after 6i; gates 7 |
| 7 | Usability Validation | author | UI/UX Design — wireframes and interaction flows | sequential after 6j; gates 8a |
| 8a | System Architect | author | Actors | sequential after 7 |
| 8b | System Architect | author | UC_* — Use Cases, tracing from UC to UT/UR | sequential after 8a |
| 8c | User Stakeholder | co-author | UC_* — clinical review of use cases | parallel with 8b; gates 8d |
| 8d | System Architect | author | DD_* — Design Decisions, tracing from DD to UC/BR | sequential after 8c; gates 9a |
| 9a | System Architect | author | Development external interfaces (black-box design) and RQ_IF_* — Interface Requirements, tracing from RQ_IF to IF | sequential after 8d |
| 9b | Product Owner | author | RQ_FN_* — Functional Requirements, tracing from RQ_FN to UC/UR | sequential after 9a |
| 9c | System Architect | author | RQ_PR_* — Performance Requirements, tracing from RQ_PR to RQ_FN | sequential after 9b |
| 9d | Regulatory Stakeholder | author | RQ_NF_*, RQ_CS_* — Non-Functional and Constraint Requirements, tracing to BR/RE | sequential after 9c |
| 9e | Development Lead | co-author | RQ_IF_*, RQ_FN_*, RQ_PR_*, RQ_NF_*, RQ_CS_* — implementation constraints and technical feasibility | sequential after 9d |
| 9f | Product Owner | author | SV_* — one Gherkin BDD feature file per functional requirement (`@ID:RQ_FN_xx` tag, Feature + As a/I want/So that, `Rule:`, Scenarios with Given/When/Then + data tables), tracing from SV to RQ_FN | sequential after 9e |
| 9g | Development Lead | co-author | SV_* — implementability of each scenario: preconditions, test data, and technical feasibility | parallel with 9f |
| 9h | Verification Lead | co-author | SV_* — testability and verification coverage; finalise so every RQ_* is covered by at least one scenario | parallel with 9f; gates Step 10a |
| 10a | Quality Assurance | audit | Full workbook (DC/UE/ME/BE/RE → KA → BR → IU_01/MD_01 → IF → UR → USER_DFMEA → UT → UFMEA → USR → UC → DD → RQ_IF/FN/PR/NF/CS → SV); route every finding back to its authoring agent, correct in-place, and re-audit until zero findings remain | sequential after 9h |
