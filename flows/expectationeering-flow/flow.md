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
| 1e | Product Owner | author | Problem (Domain Description, Actual State, Desired State, Identified Gaps DC_*) and consolidation: fill each UE/ME/BE/RE expectation's `Traces` with the DC gap(s) it addresses (DC_* is the top-level root) | sequential after 1a–1d; gates 2a |
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
| 5a | System Architect | author | Product Information, System of Interest, Context Elements, IF_*, the Acquired Parameters / Signals table (each source element → the parameters it provides, from the input), and a `_To be added_` placeholder for the context diagram (no graphic is produced) | sequential after 4c; gates 6a |
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
| 10a | Quality Assurance | audit | Full workbook (DC → UE/ME/BE/RE → KA → BR → IU_01/MD_01 → IF → UR → USER_DFMEA → UT → UFMEA → USR → UC → DD → RQ_IF/FN/PR/NF/CS → SV); route every finding back to its authoring agent, correct in-place, and re-audit until zero findings remain | sequential after 9h |

## Artifact Authoring Guidance

This is the authoritative guidance for **what content goes in each artifact and how to trace it**. It mirrors the section descriptions in the workbook template and adds the column meanings and tracing targets. Each authoring agent carries the same conventions for the artifacts it owns; this section is the single cross-flow reference.

**Universal conventions (apply to every artifact):**
- Fill **only** the section(s) assigned to the step. Never add, remove, rename, or reorder sections, headings, tables, or columns; preserve all surrounding structure and placeholders verbatim.
- Every item has a **unique ID**, numbered sequentially within its prefix (`PREFIX_01`, `PREFIX_02`, …).
- Every item except the top-level **Identified Gaps `DC_*`** records the **upstream ID(s)** it is derived from in its `Traces` column. Cited IDs must already exist in the workbook. The stakeholder expectations `UE/ME/BE/RE` are **not** top-level: each traces to the `DC_*` gap(s) it addresses. Because the gaps are authored after the expectations (Step 1e), the expectation authors leave `Traces` blank and the Product Owner completes it during the Step 1e consolidation.
- `Classification` columns are **inherited from the traced upstream item** (e.g. a UR inherits from the KA/BR it traces to; a USR inherits from its UR; a UC inherits from its UR).
- From the Context level onward (the solution domain / DHF) requirements are **SMART** and form the basis for verification.
- **Enumerate sets, never leave them collective.** Whenever an artifact would refer to a *set* of parameters, signals, measurements, data items, or inputs provided by a *set* of source elements (devices, sensors, sub-systems, services) — e.g. "the parameters from the connected devices" — do NOT leave the set implicit or vaguely named. Capture the concrete mapping (each source element → the specific parameters it provides, with units/range and interface, from the input) in the **Acquired Parameters / Signals** table in the Context section, and have every downstream artifact **reference that table** rather than repeating or vaguely naming the set. This is a generic rule about parameters/signals — never hard-code the actual domain values into the flow or agents; they come from the input.

> **PRODUCT-FREE RULE — the entire Stakeholder (INFORMAL) domain.** Everything under `## Stakeholders (INFORMAL)` — the **Problem** (Domain Description, Actual State, Desired State, Identified Gaps `DC_*`), **all Expectations** (`UE_*`/`ME_*`/`BE_*`/`RE_*`), the **Ideal Product Model** (`KA_*`), and the **Business Requirements** (`BR_*`) — MUST be written purely from the **problem domain** and be completely **solution- and product-free**. It describes the problem and the needs, never a chosen solution.
> - **Never** name the product, its brand or working name, its architecture, or any internal element/subsystem/component/module/software-item name, and **never** name a specific chosen vendor or commercial product. Describe a chosen component by its capability class — what it does for any product in the domain — not by its product or vendor brand.
> - Phrase every need, benefit, gap, proposition attribute, and constraint so it applies to **any** product that could solve the problem, including competitors.
> - Generic **domain constraints** that bind every product in the domain (laws, regulations, applicable standards, regulatory obligations) MAY be referenced — they are problem-domain facts, not a solution choice. Specific solution, vendor, or architecture names MAY NOT.
> - The product is named for the **first time** at the **Context (FORMAL)** level (`IU_01` onward), which is the start of the solution domain (DHF). Everything before it stays product-free.

### Problem & Identified Gaps (DC_*) — Product Owner
- **Product-free** (problem domain only — see the rule above): describe the problem, never a chosen solution; do not name the product, its architecture, or internal elements.
- **Domain Description**: the applicable domain where any product (yours and competitors') provides a solution.
- **Actual State**: pros and cons of the current situation.
- **Desired State**: pros and cons of the target situation — keep the pros of the actual state. State desired *capabilities and outcomes*, not a specific product or design.
- **Identified Gaps (DC_*)**: the design changes needed to move from the actual state to the desired state, expressed as solution-neutral capability gaps. Columns: `ID`, `Description`. The gaps are the **top-level root** of the informal domain — derived from the Problem analysis, they carry no upstream trace and the DC table has no `Traces` column.
- **Consolidation (UE/ME/BE/RE → DC):** after authoring the gaps, complete the traceability by filling each stakeholder expectation's `Traces` cell with the `DC_*` gap(s) it addresses (the expectation authors left it blank because the gaps did not yet exist). Ensure every expectation traces to at least one gap and every gap is addressed by at least one expectation. Record the mapping **only** in the expectation `Traces` columns — do not restate it inline inside the DC descriptions.

### Stakeholder Expectations — UE_* / ME_* / BE_* / RE_*
- Written **product-free**: they apply to any product in the problem domain, including competitors — never reference your specific product.
- Format: *The \<stakeholder\> wants \<expectation\> to \<benefit driver\>.*
- Each block names its **Stakeholder** (concise role) and a short stakeholder description.
- Columns: `ID`, `Expectation`, `Traces`. Each expectation traces to the Identified Gap(s) `DC_*` it addresses. The gaps are authored after the expectations (Step 1e), so the stakeholder author leaves `Traces` blank and the Product Owner fills it during the Step 1e consolidation.
- `UE_*` = User Stakeholder; `ME_*` = Customer Stakeholder; `BE_*` = Business Stakeholder; `RE_*` = Regulatory Stakeholder.

### Ideal Product Model (KA_*) — Product Owner (author); System Architect & Business Stakeholder (co-author); User Stakeholder (review)
- **Product-free** (problem domain only — see the rule above). The Ideal Product Model is the blueprint that aligns stakeholder expectations with the *kind of capabilities* any product in the domain would offer — NOT a description of your specific product. Describe **Proposition Attributes** as solution-neutral capability classes (what the capability does for any product in the domain), never as named architecture, internal elements/components, or product/vendor brands. "Superior to" compares against the current/competitor baseline, also product-free.
- The blueprint that aligns stakeholder expectations with product capabilities: the key proposition attributes, their priority, feasibility, and risk.
- Columns: `ID`, `Benefit Driver`, `Expectation`, `Proposition Attributes`, `Superior to`, `Priority`, `Feasible`, `Risk`, `Rationale`.
- Traces from **KA → UE/ME/BE/RE**.

### Business Requirements (BR_*) — Product Owner (author); System Architect & Customer Stakeholder (co-author)
- **Product-free** (problem domain only — see the rule above). State each business input as a solution-neutral need or constraint that applies to any product in the domain. Reference generic domain constraints (laws, standards, regulatory obligations) freely, but do NOT name the product, its architecture/internal elements, or a specific chosen vendor/commercial product — phrase those as their capability class (describe a chosen component by what it does, not by its vendor or product brand).
- Conceptual project inputs from all business stakeholders that apply across the whole product lifecycle (development, launch, manufacturing, deployment, operation & use, end of life).
- Columns: `ID`, `Description`, `Rationale`, `Stakeholder`, `Importance`, `Traces`.
- Traces from **BR → KA**.

### Intended Use (IU_01) & Medical Device Classification (MD_01) — Usability Validation (author); Regulatory Stakeholder (co-author); User Stakeholder (review)
- **IU_01**: a single, flowing **prose** statement that naturally covers the five aspects — what the product is, what it does (medical indication), who uses it (user profile), where it is used (use environment), and how it works (operating principle). Do **not** add bold labels or headers for the aspects; weave them into the sentences. Columns: `ID`, `Description`.
- **MD_01**: the assessed medical device classification. Columns: `ID`, `Description`, `Traces`. Traces from **MD_01 → IU_01**.

### Context — Product Information, System of Interest, Context Elements, External Interfaces (IF_*), Context Diagram — System Architect
- **Context Diagram**: no graphic is produced — leave the `_To be added_` placeholder in the Context Diagram section exactly as it appears in the template. Do not author a Graphviz/DOT block or any other diagram here.
- **Product Information**: short description — what the product is, what it delivers, and the principal way it operates.
- **System of Interest**: the part of the broader system this document is about (product/subsystem/component you design). Columns: `System Element`, `Description`.
- **Context Elements**: essential elements for your product that are **not** part of the design. Columns: `Context Element`, `Description`.
- **External Interfaces (IF_*)**: connections between the SOI and the context elements (mechanical, chemical, electronic, digital, logical, etc.). Columns: `ID`, `Name`, `Port 1`, `Port 2`, `ICD`.
- **Acquired Parameters / Signals**: if the product acquires/exchanges/presents a *set* of parameters or signals from a set of source elements, enumerate each source-element/parameter pair here (from the input). Columns: `Source Element`, `Parameter / Signal`, `Unit / Typical Range`, `Interface` (the `IF_*` it arrives on). Write `_Not applicable_` if no such set applies. Downstream artifacts that mention "the parameters/signals" must reference this table rather than naming the set vaguely.

### User Groups — Usability Validation
- Collections of users who share common characteristics (synonym: User Role). Columns: `User`, `User Group`, `User Profile`.

### User Requirements / Needs (UR_*) — Usability Validation (author); User Stakeholder (co-author)
- The user expectations translated over the product context into requirements specific to **your** product. They are SMARTER than the expectations and form the base for product **validation**.
- Format: *As a \<user group\> I want \<feature\> so that \<benefit\>.*
- Columns: `ID`, `Description`, `Classification` (inherited from KA/BR), `Traces`. Traces from **UR → IU_01/BR**.

### User DFMEA (USER_DFMEA_*) — Usability Validation (author); User Stakeholder (co-author)
- A structured analysis of how users might misuse, misinterpret, or fail to operate the product, the consequences, and the mitigations the design must include.
- Columns: `ID`, `Item/Function`, `Requirement`, `Failure Mode`, `End-effect`, `Rationale`, `Failure Cause`, `Severity`, `Prevention`, `Classification`, `Traces`. Traces from **USER_DFMEA → UR**.

### Use Scenarios / Use Tasks (UT_*) — Usability Validation (author); User Stakeholder (co-author)
- Concrete narratives of how the product is used in the real world, walking from a triggering situation to a successful outcome. Each scenario contains use tasks.
- Columns: `ID`, `Use Task`, `Task Description`, `Traces`. Traces from **UT → UR**.

### Usability FMEA (UFMEA_*) — Usability Validation (author); User Stakeholder (co-author)
- An FMEA focused on usability: where the UI, workflow, or interaction model can lead to errors, slow operation, or unsafe outcomes.
- Columns: `ID`, `Scenario Title`, `Use Error`, `Cause`, `Effect`, `HF Cause`, `Rationale`, `Usability Impact Level`, `Mitigation (existing)`, `Mitigation (new)`, `Classification`, `Traces`. Traces from **UFMEA → UT**.

### Usability Requirements (USR_*) — Usability Validation
- Measurable requirements for how the product must perform from a user perspective: task completion times, error rates, learnability, accessibility. Validated through usability testing.
- Columns: `ID`, `Requirement`, `Classification` (inherited from UR), `Traces`. Traces from **USR → UR/UFMEA**.

### UI/UX Design — Usability Validation
- Wireframes, interaction flows, navigation structures, and visual design principles that translate the user requirements into a tangible concept.

### Actors & Use Cases (UC_*) — System Architect (author); User Stakeholder (co-author on UC_*)
- **Actors**: individuals, groups, or systems that perform roles or tasks within the system or process. Columns: `Actor`, `Description`.
- **Use Cases (UC_*)**: leave the `_To be added_` placeholder for the use-case diagram (no graphic is produced). Columns: `ID`, `Title`, `Actor`, `Goal`, `Satisfies` (UR_), `Classification` (inherited from UR), `Precondition`, `Main Success Scenario`, `Alternative Scenarios`, `Exception Scenarios`, `Post Condition`, `Traces`. Traces from **UC → UT/UR**.

### Design Decisions (DD_*) — System Architect
- Choices made during design, with the considered alternatives and the rationale for the final choice. Columns: `ID`, `Decision`, `Alternatives`, `Rationale`, `Traces`. Traces from **DD → UC/BR**.

### System Requirements (RQ_*) — SMART, the basis for verification
All requirement tables share the columns `ID`, `Description`, `Rationale`, `Classification`, `Traces`.

> **SOLUTION-LEVEL RULE — write every requirement at the system/product level.** Every requirement in `### Requirements` (`RQ_IF_*`, `RQ_FN_*`, `RQ_PR_*`, `RQ_NF_*`, `RQ_CS_*`) is written against the **solution as a whole** — the product named in the `## SOLUTION:` heading — treated as a **black box** observable at its external boundary. The subject of every "shall" statement is the system/product itself (e.g. "The system shall …"), never an internal part. Do **NOT** write requirements about, allocate them to, or even name any internal sub-system, item, module, or component. Decomposition and allocation to internal items is the **Architecture / Items** level, which is downstream and **out of scope** for this flow. If the input gives internal/item-level detail (e.g. a per-module budget or a named software item), capture only the **boundary-observable** requirement it implies (e.g. the end-to-end latency the user sees), and leave the internal split to Architecture. The `SV_*` feature files inherit this: each `Rule:` and `Scenario` exercises the system at its external boundary, not an internal part.

- **External Interfaces (development) & Interface Requirements (RQ_IF_*)** — System Architect: External Interfaces are the points where the system connects to context elements, sub-systems, or other systems — connection type, data/signals exchanged, protocols/standards; describe them in prose/table and leave the `_To be added_` placeholder for the black-box diagram (no graphic is produced). RQ_IF_* trace from **RQ_IF → IF**.
- **Functional Requirements (RQ_FN_*)** — Product Owner: what the system must do — its functions, features, behaviours. Trace from **RQ_FN → UC/UR**.
- **Performance Requirements (RQ_PR_*)** — System Architect: quantitative requirements on how well the system performs its functions — response times, throughput, accuracy, capacity, availability. Trace from **RQ_PR → RQ_FN**.
- **Non-Functional Requirements (RQ_NF_*)** — Regulatory Stakeholder: how the system should behave rather than what it does — reliability, maintainability, security, privacy, scalability; compliance, labeling, and training requirements live here too. Trace from **RQ_NF → BR/RE**.
- **Constraint Requirements (RQ_CS_*)** — Regulatory Stakeholder: external constraints the system must respect — regulatory rules, applicable standards, imposed technology choices, environmental conditions. Trace from **RQ_CS → RE**.
- **Development Lead** co-authors all RQ_* for implementation constraints and technical feasibility.

### Verification (SV_*) — Product Owner (author); Development Lead & Verification Lead (co-author) — the 3-Amigos session
- **Follow the reference file [`Example.feature`](Example.feature) in this flow folder** for the structure, style, and layout of every feature file: the leading `@ID:` tag, the `Feature:` line, the `As a … I want … So that …` user story, a `Rule:` capturing the "shall" statement, and concrete `Scenario`s with `Given / When / Then` steps and aligned `| … |` data tables — including its indentation. Use `Example.feature` as the format template; keep this flow's tagging/tracing rules below.
- **Exact indentation (must match `Example.feature`):** put `@ID:…`, `Feature:`, `Rule:`, and `Scenario:` / `Scenario Outline:` flush at **column 0**; indent **everything else by exactly 4 spaces** — the `As a … / So that …` user story, every `Given / When / Then / And / But` step, any `# comment` line, `Examples:`, and every `| … |` data-table row. Put one blank line before each `Rule:` and before each `Scenario:`. Do **not** nest `Rule:`/`Scenario:` under `Feature:` (no 2-space "tree" indentation).
- Write **one Gherkin BDD feature file per functional requirement** as a `gherkin` fenced block, tagged `@ID:RQ_FN_xx` to trace it to the requirement it verifies.
- Each feature opens with a user story (`As a … I want … So that …`), states a `Rule:` that captures the requirement's "shall" statement, and contains one or more concrete `Scenario`s with `Given / When / Then` steps and data tables for the expected values. Use **measurable** outcomes (e.g. "within 5 seconds").
- Every `RQ_FN_*` must have a feature file and every `RQ_*` must be covered by at least one scenario. The converter records each feature file as one `SV_*` row in the Verification table and renders it in a fixed monospace font (**Consolas 9 pt**) with **Gherkin syntax colouring** (keywords, step keywords, tags, comments, `"strings"`, `<parameters>`, and `| data | table |` rows are colour-coded) so the Gherkin indentation and data-table columns stay aligned — keep the data-table pipes aligned in the markdown. Traces from **SV → RQ_FN**.
