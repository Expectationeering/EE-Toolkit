# Expectationeering Workbook

**Product**: <!-- product name -->
**Date**: <!-- date -->
**Workshop Team**: User Stakeholder, Customer Stakeholder, Business Stakeholder, Regulatory Stakeholder, Product Owner, System Architect, Usability Validation, Development Lead, Verification Lead, Quality Assurance

---

# Introduction

This workbook captures the expectations and requirements for the product, from informal stakeholder expectations through to verifiable system requirements. Every requirement item has a unique identifier, starting with the stakeholder expectations, and each item traces to the upstream item it is derived from.

## Intended users of the document

<!-- Users in scope -->

## Scope of the document

<!-- Product in scope -->

---

# Application

## Stakeholders (INFORMAL)

The stakeholder level is the start of the requirement approach. It captures the problem to be solved and the expectations of each stakeholder in a product-agnostic ("product-free") way.

### Problem

#### Domain Description

<!-- Describe the applicable domain where your product and competitor products provide a solution -->

#### Actual State

<!-- Describe the pros and cons of the actual situation -->

#### Desired State

<!-- Describe the pros and cons of the desired situation (keep the pros of the actual state) -->

#### Identified Gaps (DC_*)

The design changes needed to move from the actual state to the desired state.

| ID | Description |
|----|-------------|
| DC_01 | <!-- design change for the desired situation --> |

### Expectations

Stakeholder expectations are written "product-free": they apply to any product in the problem domain, including competitors. Format: *The \<stakeholder\> wants \<expectation\> to \<benefit driver\>.*

#### User Expectations (UE_*)

**Stakeholder**: <!-- concise name/role, e.g. Clinician -->

<!-- Description of User Stakeholder -->

| ID | Expectation | Traces |
|----|-------------|--------|
| UE_01 | <!-- expectation --> | |

#### Market Expectations (ME_*)

**Stakeholder**: <!-- concise name/role, e.g. Hospital Procurement -->

<!-- Description of Market/Customer Stakeholder -->

| ID | Expectation | Traces |
|----|-------------|--------|
| ME_01 | <!-- expectation --> | |

#### Business Expectations (BE_*)

**Stakeholder**: <!-- concise name/role, e.g. Legal Manufacturer -->

<!-- Description of Business Stakeholder -->

| ID | Expectation | Traces |
|----|-------------|--------|
| BE_01 | <!-- expectation --> | |

#### Regulatory Expectations (RE_*)

**Stakeholder**: <!-- concise name/role, e.g. Competent Authority / Notified Body -->

<!-- Description of Regulatory Stakeholder -->

| ID | Expectation | Traces |
|----|-------------|--------|
| RE_01 | <!-- expectation --> | |

### Ideal Product Model (KA_*)

The Ideal Product Model is the blueprint that aligns stakeholder expectations with product capabilities — the key proposition attributes, their priority, feasibility, and risk.

| ID | Benefit Driver | Expectation | Proposition Attributes | Superior to | Priority | Feasible | Risk | Rationale |
|----|----------------|-------------|------------------------|-------------|----------|----------|------|-----------|
| KA_01 | | | | | | | | |

### Business 'Requirements' (BR_*)

Conceptual project inputs from all business stakeholders that apply across the whole product lifecycle (development, launch, manufacturing, deployment, operation & use, end of life).

| ID | Description | Rationale | Stakeholder | Importance | Traces |
|----|-------------|-----------|-------------|------------|--------|
| BR_01 | | | | | |

## Context (FORMAL)

The context level is the start of the solution domain (DHF), based on the problem domain and the stakeholder expectations.

### Intended Use (IU_01)

Write the intended use as a single, flowing prose statement that naturally covers the five aspects — what the product is, what it does (medical indication), who uses it (user profile), where it is used (use environment), and how it works (operating principle). Do **not** add bold labels or headers for the aspects; weave them into the sentences.

| ID | Description |
|----|-------------|
| IU_01 | <!-- intended use --> |

### Medical Device Classification (MD_01)

| ID | Description | Traces |
|----|-------------|--------|
| MD_01 | <!-- assessed classification --> | |

### Context Diagram

The context diagram identifies the system of interest in relation to its context. The system of interest contains all elements that are part of the design.

_To be added_

#### Product Information

<!-- Short description of the product: what it is, what it delivers, and the principal way it operates -->

#### System of Interest

The part of the broader system this document is about — the product, subsystem, or component you are responsible for designing.

| System Element | Description |
|----------------|-------------|
| <!-- SOI --> | |

#### Context Elements

Essential elements for your product that are not part of the design.

| Context Element | Description |
|-----------------|-------------|
| <!-- Element --> | |

#### External Interfaces (IF_*)

Connections between the system of interest and the context elements (mechanical, chemical, electronic, digital, logical, etc.).

| ID | Name | Port 1 | Port 2 | ICD |
|----|------|--------|--------|-----|
| IF_01 | | | | |

#### Acquired Parameters / Signals

Whenever the product acquires, exchanges, or presents a **set** of parameters, signals, or data items from a set of source elements (measurement devices, sensors, sub-systems, services), enumerate that set here instead of leaving it as a collective phrase elsewhere. One row per source-element/parameter combination, taken from the input. If no such parameter set applies to this product, write `_Not applicable_`.

| Source Element | Parameter / Signal | Unit / Typical Range | Interface |
|----------------|--------------------|----------------------|-----------|
| <!-- e.g. a measurement device --> | <!-- the specific parameter it provides --> | | IF_ |

## Users

### User Groups

Collections of users who share common characteristics (a synonym is User Role).

| User | User Group | User Profile |
|------|------------|--------------|
| <!-- User 1 --> | <!-- Group 1 --> | <!-- Profile --> |

### User Requirements / Needs (UR_*)

The user expectations translated over the product context into requirements specific to YOUR product. They are SMARTER than the expectations and form the base for product validation. Format: *As a \<user group\> I want \<feature\> so that \<benefit\>.*

| ID | Description | Classification | Traces |
|----|-------------|----------------|--------|
| UR_01 | | <!-- inherited from KA/BR --> | |

### User DFMEA (USER_DFMEA_*)

A structured analysis of how users might misuse, misinterpret, or fail to operate the product, the consequences, and the mitigations the design must include.

| ID | Item/Function | Requirement | Failure Mode | End-effect | Rationale | Failure Cause | Severity | Prevention | Classification | Traces |
|----|---------------|-------------|--------------|------------|-----------|---------------|----------|------------|----------------|--------|
| USER_DFMEA_01 | | | | | | | | | | |

### Use Scenarios

Concrete narratives of how the product is used in the real world, walking from a triggering situation to a successful outcome. Each scenario contains use tasks (UT_*).

#### <!-- Scenario 1 -->

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_01 | | | UR_ |

### Usability FMEA (UFMEA_*)

An FMEA focused on usability: where the user interface, workflow, or interaction model can lead to errors, slow operation, or unsafe outcomes.

| ID | Scenario Title | Use Error | Cause | Effect | HF Cause | Rationale | Usability Impact Level | Mitigation (existing) | Mitigation (new) | Classification | Traces |
|----|----------------|-----------|-------|--------|----------|-----------|------------------------|-----------------------|------------------|----------------|--------|
| UFMEA_01 | | | | | | | | | | | |

### Usability Requirements (USR_*)

Measurable requirements for how the product must perform from a user perspective: task completion times, error rates, learnability, accessibility. Validated through usability testing.

| ID | Requirement | Classification | Traces |
|----|-------------|----------------|--------|
| USR_01 | | <!-- inherited from UR --> | |

## Concept

### UI/UX Design

Wireframes, interaction flows, navigation structures, and visual design principles that translate the user requirements into a tangible concept.

<!-- Add UX/UI designs -->

### Actors

Individuals, groups, or systems that perform roles or tasks within the system or process.

| Actor | Description |
|-------|-------------|
| <!-- Actor --> | |

### Use Cases (UC_*)

_To be added_

| ID | Title | Actor | Goal | Satisfies | Classification | Precondition | Main Success Scenario | Alternative Scenarios | Exception Scenarios | Post Condition | Traces |
|----|-------|-------|------|-----------|----------------|--------------|-----------------------|-----------------------|---------------------|----------------|--------|
| UC_01 | | | | UR_ | <!-- inherited from UR --> | | | | | | |

### Design Decisions (DD_*)

Choices made during design, with the considered alternatives and the rationale for the final choice.

| ID | Decision | Alternatives | Rationale | Traces |
|----|----------|--------------|-----------|--------|
| DD_01 | | | | |

---

# Development

## SOLUTION: <!-- name -->

### External Interfaces

The points where the system connects to context elements, sub-systems, or other systems — connection type, data/signals exchanged, and protocols/standards.

_To be added_

### Requirements

The full set of requirements the system must satisfy, derived from the user requirements and constrained by the context, regulatory requirements, and design decisions. Requirements are SMART and form the basis for verification.

#### Interface Requirements (RQ_IF_*)

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_IF_01 | | | | IF_ |

#### Functional Requirements (RQ_FN_*)

What the system must do — its functions, features, and behaviors. Each traces back to a use case or user requirement.

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_FN_01 | | | | UC_ |

#### Performance Requirements (RQ_PR_*)

Quantitative requirements on how well the system performs its functions: response times, throughput, accuracy, capacity, availability.

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_PR_01 | | | | RQ_FN_ |

#### Non-Functional Requirements (RQ_NF_*)

How the system should behave rather than what it does: reliability, maintainability, security, privacy, scalability. Compliance, labeling, and training requirements live here too.

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_NF_01 | | | | BR_ |

#### Constraint Requirements (RQ_CS_*)

External constraints the system must respect: regulatory rules, applicable standards, imposed technology choices, environmental conditions.

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_CS_01 | | | | RE_ |

### Verification (SV_*)

The **BDD feature files** that verify the functional requirements, defined jointly by the 3-Amigos (Product Owner, Development Lead, Verification Lead). Write **one feature file per functional requirement** as a `gherkin` fenced block, tagged `@ID:RQ_FN_xx` to trace it to the requirement it verifies. Each feature has a user story (`As a … I want … So that …`), a `Rule:` that captures the requirement's "shall" statement, and one or more concrete `Scenario`s with `Given / When / Then` steps and data tables for the expected values. Use measurable outcomes (e.g. "within 5 seconds"). Every RQ_FN_* must have a feature file and every RQ_* must be covered by at least one scenario. The converter records each feature file as one row (`SV_*`) in the workbook's Verification table.

```gherkin
@ID:RQ_FN_01
Feature: Show Vital Signs
    As a clinician I want to see the patient's current vital signs on the Monitor Display within 5 seconds of a valid sensor reading
    So that I can make safe, timely clinical decisions at the bedside

Rule: The MMSS shall show the vital signs on the Display Interface within 5 seconds after the sensor is correctly connected to the Device Interface.

Scenario: Show vital signs from ECG Electrodes on the Monitor Display
    Given the simulator is running
    And no sensors are connected in the simulator
    And the MMSS is running
    When the ECG Electrodes are connected in the simulator
    Then the following vital signs are visible on the Display Interface within 5 seconds
    | vital sign |
    | Heart Rate |
```

---

<!-- ============================================================
     The sections below are part of the workbook structure but are
     NOT produced by this flow (scope ends at Verification). They are
     left as empty template for downstream design work.
     ============================================================ -->

### Architecture

<!-- Not filled by this flow. Items, internal interfaces, white-box design. -->

### Detailed Design

<!-- Not filled by this flow. DS_*, sequence diagrams, design specifications. -->

### DFMEA

<!-- Not filled by this flow. System-level Design FMEA (SYS_DFMEA_*). -->

### Items

<!-- Not filled by this flow. Per-item decomposition. -->
