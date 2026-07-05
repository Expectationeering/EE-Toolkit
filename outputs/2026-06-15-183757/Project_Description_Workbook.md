---
Executed by: orchestration (CLAUDE.md)
Flow: flows/expectationeering-flow/flow.md
Templates: flows/expectationeering-flow/expectationeering-workbook.md
Inputs: inputs/
Date: 2026-06-15
---

# Expectationeering Workbook

**Product**: Mobile Monitoring Software Solution (MMSS)
**Date**: 2026-06-15
**Workshop Team**: User Stakeholder, Customer Stakeholder, Business Stakeholder, Regulatory Stakeholder, Product Owner, System Architect, Usability Validation, Development Lead, Verification Lead, Quality Assurance

---

# Introduction

This workbook captures the expectations and requirements for the product, from informal stakeholder expectations through to verifiable system requirements. Every requirement item has a unique identifier, starting with the stakeholder expectations, and each item traces to the upstream item it is derived from.

## Intended users of the document

This workbook is intended for the product development team and stakeholders responsible for specifying, designing, verifying, and approving the Mobile Monitoring Software Solution (MMSS): product management, system architecture, usability engineering, development, verification, and quality/regulatory affairs.

## Scope of the document

This document covers the Mobile Monitoring Software Solution (MMSS): medical device software that transforms a portable patient monitor into an active clinical decision-support tool. It captures the requirement approach from informal stakeholder expectations through to verifiable system requirements and their BDD verification. Scope is software only; the host platform, measurement devices, monitor display, and physical enclosure are fixed external elements accessed through defined interfaces. Architecture, detailed design, system DFMEA, and item-level decomposition are out of scope for this workbook.

---

# Application

## Stakeholders (INFORMAL)

The stakeholder level is the start of the requirement approach. It captures the problem to be solved and the expectations of each stakeholder in a product-agnostic ("product-free") way.

### Problem

#### Domain Description

The domain is real-time monitoring of critically ill patients combined with diagnostic decision support, across both fixed critical-care environments (intensive care units, emergency rooms) and mobile or pre-hospital settings (ambulances, mobile medical units, point of incident). In this domain a solution continuously acquires a set of non-invasive vital-signs measurements from patient-attached devices, presents the patient's physiological state to a trained medical professional, alerts that professional to abnormal conditions and to faults that would invalidate the measurements, and increasingly is expected to actively support the clinical reasoning that turns observed vital signs into a working diagnosis. Solutions in this domain operate under time pressure and high clinical stakes, must remain dependable in environments with interruptions and limited operator attention, and are bound by medical-device safety legislation and applicable standards (e.g. IEC 62304, ISO 14971, IEC 62366-1, IEC 60601-1-8) and by patient data-protection obligations. Any product in this domain — the one developed here and competing offerings alike — provides a solution by addressing some combination of continuous monitoring, alarming, fault detection, diagnostic decision support, and integration with the wider hospital care setting.

#### Actual State

Today, critically ill patients are monitored predominantly with passive vital-signs monitors that acquire and display physiological measurements and raise alarms when a value crosses a threshold.

**Pros**

- Continuous, reliable, real-time display of key vital signs gives the clinician uninterrupted awareness of the patient's measured condition.
- Threshold-based alarms draw attention to individual abnormal vital signs.
- Non-invasive measurement keeps continuous monitoring comfortable and low-harm for the patient.
- The behaviour is well understood, well established, and trusted by trained clinicians.

**Cons**

- Monitoring is passive: the device displays measurements but offers no active support in interpreting them into a diagnosis, leaving the clinician to integrate multiple signals unaided.
- Under time pressure and with limited attention, unaided interpretation risks delay and misinterpretation, particularly in pre-hospital and mobile settings where expert support may be remote.
- Faults that invalidate the data — sensor disconnection, misplacement, or loss of valid signal — are not always reliably detected, so the clinician can act on missing or misleading information.
- There is no transparent indication of when diagnostic reasoning is unavailable or has not produced a result in the expected time.
- Integration with the wider hospital care setting is limited, so obtaining a timely second opinion or sharing patient data is slow or manual.

#### Desired State

The desired state retains everything dependable about today's monitoring and adds active diagnostic decision support, trustworthy fault detection, and integration with the hospital care setting.

**Pros**

- Continuous, reliable, real-time display of key vital signs, clearly and legibly presented for interpretation at a glance (retained from the actual state).
- Timely audible and visual alarms when a vital sign becomes abnormal (retained and reinforced from the actual state).
- Non-invasive, comfortable monitoring of the patient (retained from the actual state).
- Active, ranked diagnostic candidates derived from the patient's data, so the clinician is supported rather than left to integrate the signals unaided.
- Fast convergence to a candidate diagnosis shortly after the patient is connected, so appropriate treatment can begin without delay.
- Reliable detection of, and alerting on, sensor disconnection, misplacement, or loss of valid signal, so the clinician never unknowingly acts on invalid data.
- Transparent notification when diagnostic support is unavailable or has not produced a result in the expected time, so the clinician can fall back on clinical judgement without losing time.
- Clear separation and transparency of measured vital signs versus inferred diagnostic suggestions, with the basis and confidence of each suggestion exposed, keeping the clinician in control.
- Integration with hospital information systems so relevant patient and diagnostic data can be shared for a timely expert second opinion.

**Cons**

- Adding diagnostic decision support raises the safety stakes: incorrect or misinterpreted candidates could mislead clinical decisions, so stronger risk control, validation, and human-in-the-loop safeguards are required.
- Greater capability and integration increase complexity, regulatory burden, and the validation and lifecycle-support effort needed to keep the solution dependable and compliant.

#### Identified Gaps (DC_*)

The design changes needed to move from the actual state to the desired state.

| ID | Description |
|----|-------------|
| DC_01 | Add active diagnostic decision support that derives ranked diagnostic candidates from the patient's data, instead of leaving the clinician to interpret raw vital signs unaided. |
| DC_02 | Make the diagnostic candidates converge quickly after the patient is connected so that appropriate treatment can begin without delay. |
| DC_03 | Make the basis and confidence of each diagnostic suggestion transparent, and keep the clinician in control of the decision (human-in-the-loop), so that algorithmic output is judged rather than blindly trusted. |
| DC_04 | Clearly separate and distinguish measured (observed) vital signs from inferred (AI-generated) diagnostic suggestions so that facts are not confused with conclusions. |
| DC_05 | Provide reliable detection of, and timely alerting on, sensor disconnection, misplacement, or loss of valid signal so that the clinician never unknowingly acts on invalid data. |
| DC_06 | Provide transparent notification when diagnostic support is unavailable or has not produced a result within the expected time so that the clinician can fall back on clinical judgement without losing time. |
| DC_07 | Provide integration with hospital information systems so that relevant patient and diagnostic data can be shared for a timely expert second opinion, replacing slow or manual exchange. |
| DC_08 | Preserve and reinforce continuous, real-time, clearly legible display of key vital signs and timely audible/visual alarms for abnormal conditions, retained from the current passive monitoring baseline. |
| DC_09 | Preserve fast readiness for use after activation and simple, low-effort operation at the bedside and on the move, so attention stays on the patient. |
| DC_10 | Provide a safe simulated practice mode so that clinicians can build competence in operating the solution and interpreting its diagnostic output before relying on it with real patients. |
| DC_11 | Preserve non-invasive, comfortable monitoring of the patient while adding the new capabilities. |
| DC_12 | Source the diagnostic capability as a commercially validated, off-the-shelf component and confine development scope to software accessing fixed physical components through defined interfaces, to reduce development, validation, and time-to-market risk. |
| DC_13 | Develop, validate, and document the solution under a compliant medical-device software life-cycle, quality management system, and risk-management process appropriate to its safety classification, with traceable evidence, to satisfy market-access and audit obligations. |
| DC_14 | Provide and justify a defensible software safety classification, supported where reduced by demonstrated independent external risk-control measures, so that residual risk from software failure is acceptable. |
| DC_15 | Provide clinical evaluation and validation evidence for the diagnostic decision-support function demonstrating analytical and clinical performance for the intended population and use environment. |
| DC_16 | Apply a usability-engineering process addressing use-related hazards and use errors, and provide complete labelling and instructions for use, so that foreseeable misinterpretation does not compromise patient safety. |
| DC_17 | Ensure alarm signals conform to applicable alarm-system safety standards for prioritisation, distinctiveness, and reliable clinician notification of abnormal physiological conditions and faults. |
| DC_18 | Process personal health data in compliance with applicable data-protection and privacy law, with lawful basis, data minimisation, security, and access controls, throughout monitoring, processing, and hospital exchange. |
| DC_19 | Provide a documented post-market surveillance and vigilance system, with maintainability and timely safety/security updates, so that emerging safety signals are detected and the solution stays dependable and compliant over its service life. |
| DC_20 | Contain residual liability through documented risk mitigation and clear allocation of responsibility, and provide clear liability and safety assurances to the procuring organisation. |
| DC_21 | Provide a transparent, predictable acquisition cost and a low total cost of ownership across the lifecycle, with assured supplier support and maintenance. |
| DC_22 | Provide demonstrable, differentiated clinical and operational value beyond passive vital-signs display, with measurable advantage over competing offerings. |
| DC_23 | Provide interoperability with the organisation's existing installed base of non-invasive measurement devices and the ability to scale across multiple care settings and fleet units without per-site re-engineering. |
| DC_24 | Ensure the solution fits the legal manufacturer's portfolio and strategy and is developable within its competency, capacity, and budget, with internal-department interests aligned across the lifecycle. |
| DC_25 | Ensure the solution is producible and deployable repeatably at the required quality and scale, supportable and serviceable (including complaint handling and training), with a defined end-of-life and decommissioning approach. |

### Expectations

Stakeholder expectations are written "product-free": they apply to any product in the problem domain, including competitors. Format: *The \<stakeholder\> wants \<expectation\> to \<benefit driver\>.*

#### User Expectations (UE_*)

**Stakeholder**: Clinician

A trained medical professional (e.g. critical-care nurse, emergency physician, or paramedic) who monitors and treats critically ill patients at the bedside in intensive care units, emergency rooms, and mobile or pre-hospital settings. They work under time pressure, often with interruptions and limited hands, and rely on the monitor to keep them aware of the patient's condition and to support fast, safe clinical decisions.

| ID | Expectation | Traces |
|----|-------------|--------|
| UE_01 | The Clinician wants continuous, real-time visibility of the patient's key vital signs to maintain uninterrupted awareness of the patient's condition. | DC_08 |
| UE_02 | The Clinician wants the displayed vital signs to be presented clearly and legibly to read and interpret the patient's status at a glance under time pressure. | DC_08 |
| UE_03 | The Clinician wants ranked diagnostic candidates derived from the patient's data to support faster and better-informed clinical decisions. | DC_01 |
| UE_04 | The Clinician wants the diagnostic output to arrive quickly after the patient is connected to begin appropriate treatment without delay. | DC_02 |
| UE_05 | The Clinician wants timely audible and visual alarms when a vital sign becomes abnormal to intervene before the patient's condition deteriorates. | DC_08, DC_17 |
| UE_06 | The Clinician wants to be alerted when a sensor is disconnected, misplaced, or no longer providing valid data to avoid acting on missing or misleading information. | DC_05 |
| UE_07 | The Clinician wants to be notified when diagnostic support is unavailable or has not produced a result in the expected time to fall back on clinical judgement without losing time. | DC_06 |
| UE_08 | The Clinician wants the basis and confidence of each diagnostic suggestion to be transparent to judge how much to trust the AI output and retain clinical control. | DC_03 |
| UE_09 | The Clinician wants to distinguish raw measured vital signs from AI-generated diagnostic suggestions to avoid confusing observed facts with inferred conclusions. | DC_04 |
| UE_10 | The Clinician wants the monitor to be ready for use quickly after activation to begin monitoring a patient in an emergency without waiting. | DC_09 |
| UE_11 | The Clinician wants to operate the monitor easily and with minimal steps at the bedside and on the move to keep attention on the patient rather than on the device. | DC_09 |
| UE_12 | The Clinician wants to practise using the monitor and interpreting its diagnostic output in a safe simulated mode to build competence before relying on it with real patients. | DC_10 |
| UE_13 | The Clinician wants monitoring of the patient to be non-invasive and comfortable to track vital signs continuously without adding harm or distress to the patient. | DC_11 |
| UE_14 | The Clinician wants relevant patient and diagnostic data to be sharable with the hospital for a second opinion to obtain timely expert input on critical cases. | DC_07 |

#### Market Expectations (ME_*)

**Stakeholder**: Hospital & EMS Procurement and clinical-engineering decision makers

Healthcare-organisation buyers (hospital procurement, biomedical/clinical-engineering departments, and EMS fleet managers) who evaluate, fund, and authorise the acquisition of critical-care monitoring solutions. They weigh clinical value, total cost of ownership, regulatory market access, interoperability, and ongoing support against budget and risk before committing to a purchase.

| ID | Expectation | Traces |
|----|-------------|--------|
| ME_01 | The procuring healthcare organisation wants a transparent and predictable acquisition and licensing cost to justify the investment within a constrained capital and operating budget. | DC_21 |
| ME_02 | The procuring healthcare organisation wants a low total cost of ownership across the product lifecycle, covering deployment, maintenance, updates, and support, to protect long-term operating margins. | DC_21 |
| ME_03 | The procuring healthcare organisation wants demonstrable clinical and operational value such as faster, better-informed diagnostic decisions to improve patient outcomes and justify the purchase to clinical and financial stakeholders. | DC_01, DC_22 |
| ME_04 | The procuring healthcare organisation wants valid regulatory market clearance for the applicable jurisdiction as a precondition of any purchase to ensure the solution is lawful to deploy and use in clinical care. | DC_13 |
| ME_05 | The procuring healthcare organisation wants demonstrated conformance to recognised medical device software standards such as IEC 62304 to satisfy internal compliance, audit, and risk-governance obligations. | DC_13 |
| ME_06 | The procuring healthcare organisation wants the solution to integrate with hospital information systems through recognised health-data interoperability standards such as HL7/FHIR to avoid costly bespoke integration and data silos. | DC_07 |
| ME_07 | The procuring healthcare organisation wants interoperability with its existing installed base of non-invasive measurement devices to protect prior equipment investment and avoid forced hardware replacement. | DC_23 |
| ME_08 | The procuring healthcare organisation wants high reliability and availability in critical-care use to minimise clinical disruption and avoid risk to patients and reputation. | DC_19 |
| ME_09 | The procuring healthcare organisation wants assured supplier support, maintenance, and timely security and safety updates throughout the service life to keep the solution dependable and compliant over time. | DC_19, DC_21 |
| ME_10 | The procuring healthcare organisation wants differentiated diagnostic decision-support capability beyond passive vital-signs display to gain measurable clinical advantage over competing offerings. | DC_22 |
| ME_11 | The procuring healthcare organisation wants low-effort training and rapid clinician adoption to limit deployment cost and reach operational benefit quickly. | DC_09, DC_10 |
| ME_12 | The procuring healthcare organisation wants clear liability allocation and documented safety assurances from the supplier to manage organisational risk and protect against clinical and legal exposure. | DC_20 |
| ME_13 | The procuring healthcare organisation wants the solution to scale across multiple care settings and fleet units without per-site re-engineering to support phased and enterprise-wide deployment. | DC_23 |

#### Business Expectations (BE_*)

**Stakeholder**: Legal Manufacturer (internal departments — Executive/Strategy, R&D, Quality & Regulatory Affairs, Manufacturing/Operations, Service & Support, Commercial)

The organisation that designs, produces, and places the medical device software on the market and bears full legal-manufacturer responsibility for it. Its voice consolidates the constraints, liability exposure, and strategic priorities of all internal departments that must be able to develop, certify, produce, support, and stand behind the product across its lifecycle.

| ID | Expectation | Traces |
|----|-------------|--------|
| BE_01 | The legal manufacturer wants the product to fit the organisation's portfolio and strategic direction to protect long-term investment priorities and deliver an acceptable return. | DC_24 |
| BE_02 | The legal manufacturer wants the product to be developable within the organisation's available competency, capacity, and budget to keep the business case viable and avoid over-extending internal resources. | DC_24 |
| BE_03 | The legal manufacturer wants the diagnostic capability to be sourced as a commercially validated, off-the-shelf component rather than developed in-house to reduce development risk, validation burden, and time-to-market. | DC_12 |
| BE_04 | The legal manufacturer wants the development scope limited to software only, with physical components treated as fixed and accessed through defined interfaces, to avoid the cost, liability, and timeline of hardware development. | DC_12 |
| BE_05 | The legal manufacturer wants the product developed under a compliant software lifecycle and quality management system aligned with applicable safety standards to ensure audit readiness and defensible design control. | DC_13 |
| BE_06 | The legal manufacturer wants residual liability exposure contained through documented risk mitigation and clear allocation of responsibility to external and independent systems to limit the organisation's post-market liability. | DC_14, DC_20 |
| BE_07 | The legal manufacturer wants the product to be maintainable and updatable throughout its lifecycle to control the cost of corrections, changes, and obsolescence management over time. | DC_19 |
| BE_08 | The legal manufacturer wants the product to be supportable and serviceable at the required scale, including complaint handling and user training, to keep post-market support obligations within the organisation's capacity. | DC_25 |
| BE_09 | The legal manufacturer wants the product to be producible and deployable repeatably at the required quality level to ensure scalable release and consistent conformity of each delivered unit. | DC_25 |
| BE_10 | The legal manufacturer wants a defined end-of-life and decommissioning approach for the product to manage withdrawal, data handling, and continued-support obligations responsibly. | DC_25 |
| BE_11 | The legal manufacturer wants the interests and obligations of all internal departments to remain aligned across the lifecycle to prevent inter-departmental conflicts from becoming downstream project and compliance risks. | DC_24 |

#### Regulatory Expectations (RE_*)

**Stakeholder**: Competent Authority / Notified Body

The governmental competent authorities, notified bodies, and surveillance agencies that determine whether medical device software for critical-care monitoring and AI diagnostic decision-support may lawfully be placed on and remain on the market. They enforce mandatory market-access legislation, applicable harmonised standards, and post-market obligations, and may approve, defer, refuse, or withdraw a product.

| ID | Expectation | Traces |
|----|-------------|--------|
| RE_01 | The competent authority wants the medical device software to be developed, maintained, and documented under a compliant software life-cycle process (per IEC 62304) appropriate to its assigned software safety class to demonstrate that life-cycle activities, risk control, and configuration management satisfy the conditions for market access. | DC_13 |
| RE_02 | The competent authority wants the software safety classification to be justified and any reduction in class to be supported by demonstrated, independent external risk-control measures to ensure that residual risk from software failure is mitigated to an acceptable level before approval. | DC_14 |
| RE_03 | The competent authority wants a documented risk management process applied across the product life cycle (per ISO 14971) with identified hazards, estimated and controlled risks, and a benefit-risk determination to ensure that overall residual risk is acceptable and that risk control is traceable to evidence. | DC_13, DC_14 |
| RE_04 | The notified body wants a usability engineering process applied to the user interface (per IEC 62366-1) addressing use-related hazards and use errors in the intended use environment to ensure that foreseeable misinterpretation of vital signs and diagnostic output does not compromise patient safety. | DC_16 |
| RE_05 | The competent authority wants clinical evaluation and validation evidence for the diagnostic decision-support function to be provided, demonstrating analytical and clinical performance for the intended population and use environment, to ensure that ranked diagnostic candidates are sufficiently safe and effective to be relied upon by clinicians. | DC_15 |
| RE_06 | The notified body wants the manufacturer to operate a certified quality management system (per ISO 13485) covering design, development, production, and post-market activities to ensure that the product is produced under controlled, auditable, and reproducible conditions. | DC_13, DC_25 |
| RE_07 | The competent authority wants complete labelling and instructions for use to be provided in the required languages, including intended use, indications, warnings, contraindications, training prerequisites, and residual-risk information, to ensure that trained professional users can operate the device safely and within its validated scope. | DC_16 |
| RE_08 | The surveillance authority wants a documented post-market surveillance and vigilance system to be in place, including incident and serious-incident reporting and periodic safety reporting, to ensure that emerging safety signals are detected, reported, and acted upon after market access is granted. | DC_19 |
| RE_09 | The competent authority wants personal health data to be processed in compliance with applicable data-protection and privacy law, with lawful basis, data minimisation, security, and access controls, to ensure that patient confidentiality and data integrity are protected during monitoring, processing, and hospital information exchange. | DC_18 |
| RE_10 | The competent authority wants clinical alarm signals to conform to applicable alarm-system safety standards (per IEC 60601-1-8) for prioritisation, distinctiveness, and clinician notification to ensure that abnormal physiological conditions and sensor or connection faults are reliably communicated to the user. | DC_05, DC_17 |
| RE_11 | The notified body wants a complete and traceable technical file to be assembled and maintained, providing design, verification, validation, and risk evidence with full traceability from requirements to test results, to ensure that conformity with applicable requirements can be independently audited and certified. | DC_13 |
| RE_12 | The competent authority wants the AI/ML diagnostic function to use a validated model with defined performance characteristics, documented intended-use boundaries, change-control over the model, and a clinician-in-the-loop decision pathway to ensure that autonomous algorithmic output does not determine patient care without qualified human oversight. | DC_03, DC_12, DC_15 |

### Ideal Product Model (KA_*)

The Ideal Product Model is the blueprint that aligns stakeholder expectations with product capabilities — the key proposition attributes, their priority, feasibility, and risk.

| ID | Benefit Driver | Expectation | Proposition Attributes | Superior to | Priority | Feasible | Risk | Rationale |
|----|----------------|-------------|------------------------|-------------|----------|----------|------|-----------|
| KA_01 | Continuous situational awareness | UE_01, UE_02, UE_13, ME_08 | Continuous, real-time acquisition and clearly-legible presentation of a patient's key non-invasive vital signs, reliably and comfortably, so the clinician keeps uninterrupted at-a-glance awareness of the patient's condition. | Passive vital-signs monitors that display measurements but without the dependability and at-a-glance legibility expected under time pressure. | High | Yes — established capability class in the domain. | Low | The dependable, trusted core of monitoring that must be retained; foundational to every other capability and to clinical trust. |
| KA_02 | Active diagnostic decision support | UE_03, ME_03, ME_10, RE_05 | Capability to derive ranked diagnostic candidates from the acquired patient data and present them to the clinician, turning observed vital signs into actively supported clinical reasoning. | Passive monitoring that leaves the clinician to integrate multiple signals unaided into a diagnosis. | High | Partial — feasible for v1 only by interfacing to a commercially validated, off-the-shelf decision-support capability; deriving candidates in-house is not feasible within the first-release validation and clearance window. | High | The central differentiator over passive monitoring and the core strategic capability that justifies the investment, but also the highest-stakes capability clinically and for regulatory clearance; the dominant risk drivers are algorithmic-clearance delay and model-validation complexity, which the off-the-shelf sourcing strategy directly mitigates. From the legal-manufacturer view this is the largest liability concentration: as the party placing the device on the market the manufacturer remains accountable for the safety of decision-support output even when the diagnostic capability is externally sourced, so it must be wrapped in supplier qualification, validated-use boundaries, human-in-the-loop control (KA_04) and post-market surveillance to keep residual liability contained. |
| KA_03 | Rapid time-to-diagnosis | UE_04, ME_03 | Capability to converge to a candidate diagnosis quickly after the patient is connected, so appropriate treatment can begin without delay. | Unaided interpretation where reaching a working diagnosis is slow, especially in mobile/pre-hospital settings with remote expert support. | High | Partial — the system reliably meets its own sub-second presentation budget once candidates are received, but end-to-end convergence time is set by the external diagnostic capability's budget (a two-minute maximum that is not within the system's control) rather than by the system. | Medium | Time-criticality is a defining clinical value in critical care; the binding constraint is the external diagnostic capability's convergence budget (KA_02), so the system can only guarantee prompt display of whatever the capability returns, not the convergence itself. |
| KA_04 | Trustworthy, controllable AI output | UE_08, RE_12 | Capability to expose the basis and confidence of each diagnostic suggestion and to keep the clinician in the decision loop, so algorithmic output is judged rather than blindly trusted. | Opaque or autonomous algorithmic output that cannot be calibrated or overridden by the clinician. | High | Yes — transparency and human-in-the-loop are achievable presentation/workflow capabilities. | Medium | Mandatory regulatory expectation and essential to clinician trust and safe adoption; mitigates misinterpretation risk. |
| KA_05 | Separation of fact from inference | UE_09, RE_04 | Capability to clearly distinguish and separate measured (observed) vital signs from inferred (algorithm-generated) diagnostic suggestions in the presentation, so facts are not confused with conclusions. | Presentations that blur observed measurements with inferred conclusions, inviting misinterpretation. | High | Yes — a presentation/UX capability. | Low | Directly addresses a use-related hazard; low cost, high safety value, and a usability-engineering expectation. |
| KA_06 | Reliable fault detection and alerting | UE_05, UE_06, RE_10 | Capability to detect and timely alert on abnormal vital signs and on sensor disconnection, misplacement, or loss of valid signal, with prioritised, distinctive, standards-conformant alarm signalling. | Threshold alarms that flag abnormal values but do not reliably detect data-invalidating faults such as misplacement or signal loss. | High | Partial — abnormal-value and disconnection/loss-of-valid-signal alerting within sub-second display budgets is feasible, but reliable misplacement detection depends on the measurement devices auto-detecting misplacement and signalling it across the defined interface; the system can alert only on what those devices and signals expose. | High | Prevents the clinician acting on missing or misleading data; the dominant risk driver is undetected sensor misplacement leading to a wrong diagnosis, whose impact is critical and whose detection is shared with the external measurement devices, so the residual risk is higher than a pure in-system alarm capability. From the legal-manufacturer view the shared detection boundary must be governed by documented interface assumptions and supplier responsibility allocation, since liability for a missed-fault hazard cannot be transferred away by the choice to rely on an external device — the manufacturer must evidence the interface contract and design the safe-state fallback for whatever the devices fail to expose. |
| KA_07 | Transparent diagnostic availability | UE_07, RE_12 | Capability to transparently notify the clinician when diagnostic support is unavailable or has not produced a result within the expected time, so they can fall back on clinical judgement without losing time. | Solutions giving no indication that diagnostic reasoning is unavailable or overdue, causing silent delay. | High | Yes — a notification/workflow capability. | Low | A safety-critical notification: a silent failure to flag that diagnosis is overdue directly causes treatment delay in a critically ill patient (a critical-impact hazard), so providing the notification is a high-priority capability on a par with the other safety alerting (KA_06); residual risk stays low because the probability is contained by an independent timeout notification and the capability itself is low-complexity. |
| KA_08 | Fast, low-effort operation | UE_10, UE_11, ME_11 | Capability for rapid readiness after activation and simple, low-step operation at the bedside and on the move, so clinician attention stays on the patient. | Solutions slow to ready or demanding attention away from the patient during operation. | High | Yes — readiness and interaction efficiency are achievable design properties. | Low | Essential in emergencies and mobile settings; also drives rapid adoption and lower training/deployment cost. |
| KA_09 | Safe practice and training | UE_12, ME_11, RE_04 | Capability to provide a safe simulated practice mode so clinicians can build competence in operating the solution and interpreting its diagnostic output before relying on it with real patients. | Solutions offering no safe rehearsal environment, so competence is built on live patients. | Medium | Yes — a simulation/training capability. | Low | Mitigates misinterpretation risk, supports usability-engineering obligations, and reduces deployment friction. |
| KA_10 | Hospital integration and second opinion | UE_14, ME_06 | Capability to share relevant patient and diagnostic data with hospital information systems through recognised health-data interoperability standards, enabling a timely expert second opinion. | Limited integration where obtaining a second opinion or sharing data is slow or manual. | Medium | Partial — feasible via established health-data interoperability standards, but the exact protocol and interface control documents are still to be defined, and the share path remains subject to the broader connectivity/real-time integration risk. | Medium | Extends clinical value and avoids bespoke integration and data silos; the dominant risk driver is connectivity and real-time integration uncertainty, mitigated by prioritising early definition of the external interface control documents. |
| KA_11 | Affordable, predictable cost of ownership | ME_01, ME_02, ME_09 | Capability to offer transparent, predictable acquisition/licensing cost and low total cost of ownership across the lifecycle, with assured support and maintenance. | Offerings with opaque pricing or high lifecycle cost that strain constrained healthcare budgets. | Medium | Yes — a commercial/lifecycle property. | Low | A primary procurement decision driver; commercial rather than technical, but essential to purchase. |
| KA_12 | Protected investment and scalability | ME_07, ME_13, ME_11 | Capability to interoperate with the organisation's existing installed base of non-invasive measurement devices and to scale across multiple care settings and fleet units without per-site re-engineering. | Solutions that force hardware replacement or require per-site re-engineering to deploy. | Medium | Yes — real-time acquisition from the defined set of non-invasive measurement device types with sub-second presentation is an achievable, in-scope target; interoperability breadth is bounded by the device interfaces and standards supported. | Medium | Protects prior equipment investment and enables phased, enterprise-wide deployment; the dominant risk driver is real-time multi-device integration, mitigated by early prototyping and prioritised interface-control-document definition. From the legal-manufacturer view, scaling across a heterogeneous installed base widens the validated-configuration matrix the manufacturer must verify, qualify, and stand behind; supporting unbounded device variants raises QMS, regression-testing, and post-market burden, so interoperability is deliberately bounded to a defined, validated set of device interfaces to keep the supportability and liability envelope manageable. |
| KA_13 | Regulatory market access and assurance | ME_04, ME_05, ME_12, RE_01, RE_02, RE_03, RE_06, RE_07, RE_08, RE_09, RE_11 | Capability to be developed, validated, and documented under a compliant medical-device software lifecycle, QMS, and risk-management process appropriate to its safety classification, with traceable evidence, justified safety classification, clinical evaluation, usability engineering, complete labelling, data-protection compliance, post-market surveillance, and clear liability allocation. | Offerings lacking demonstrable conformance, traceable evidence, or clear liability assurances required for lawful clinical deployment. | High | Yes — established (if demanding) regulatory capability class for the domain. | High | A non-negotiable precondition of market access and a key procurement assurance; broad, demanding, and central to the benefit-risk case. |
| KA_14 | Reduced-risk sourcing and scope | BE_03, BE_04, RE_12 | Capability to source the diagnostic function as a commercially validated, off-the-shelf component and to confine development scope to software accessing fixed physical components through defined interfaces, reducing development, validation, and time-to-market risk. | In-house diagnostic development and broader hardware/software scope that increase risk, cost, and time-to-market. | High | Yes — a sourcing and scope-confinement strategy that is realisable within the domain, contingent on continued availability of a validated off-the-shelf diagnostic capability with a defined interface. | Medium | Materially lowers development and validation risk and accelerates market entry; this strategy is itself the primary mitigation for the algorithmic-clearance and model-validation risks, so its residual risk is the dependency on the validated component remaining available and interface-stable. From the legal-manufacturer view the trade-off is a strategic supplier dependency: the manufacturer offloads in-house development risk but takes on supplier-qualification, change-control, and continuity obligations, and remains the responsible party for the integrated device regardless of where the diagnostic capability originates — so the sourcing decision must be backed by supplier agreements, second-source/exit contingency, and contractual liability and interface-stability assurances to keep the residual business risk contained. |
| KA_15 | Dependable lifecycle support | ME_08, ME_09, BE_07, BE_08, BE_09, BE_10, RE_08 | Capability to be reliable and available in critical-care use, maintainable and updatable with timely safety/security updates, supportable and serviceable at scale (including complaint handling and training), producible/deployable repeatably at quality, with a defined end-of-life and post-market surveillance. | Offerings with weak post-market support, slow updates, or no defined end-of-life, eroding dependability over the service life. | High | Yes — established lifecycle/operational capability class, contingent on the manufacturer committing the standing service, quality, and regulatory-affairs capacity to sustain post-market obligations over the full service life. | Medium | Keeps the solution dependable and compliant over its whole service life; spans reliability, maintenance, production, and end-of-life. From the legal-manufacturer view these are not optional nice-to-haves but binding post-market obligations the manufacturer must resource and stand behind — complaint handling, vigilance, security patching, and supplier change-tracking are recurring lifecycle cost and liability commitments that must be staffed and budgeted up front, not deferred, or the residual compliance and dependability risk rises sharply. |
| KA_16 | Viable, aligned business fit | BE_01, BE_02, BE_05, BE_06, BE_11 | Capability for the solution to fit the legal manufacturer's portfolio and strategy, be developable within its competency, capacity, and budget, under a compliant lifecycle/QMS with contained residual liability and aligned internal-department interests. | Initiatives that over-extend the manufacturer or create misaligned internal obligations and downstream compliance risk. | High | Yes — an organisational/strategic capability, contingent on a validated business case clearing the manufacturer's investment threshold and the R&D, quality, and regulatory competencies being available rather than newly built. | Medium | Ensures the solution can actually be developed, certified, and stood behind; internal viability underpins all other capabilities. From the legal-manufacturer view this is the gating capability: without strategic portfolio fit, a financeable business case, sufficient competency and capacity, and resolved internal-department tensions (R&D flexibility versus design-freeze and compliance lock-down), every downstream capability is at risk regardless of technical feasibility — so the residual risk is organisational over-reach and misaligned obligations rather than technology. |

### Business 'Requirements' (BR_*)

Conceptual project inputs from all business stakeholders that apply across the whole product lifecycle (development, launch, manufacturing, deployment, operation & use, end of life).

| ID | Description | Rationale | Stakeholder | Importance | Traces |
|----|-------------|-----------|-------------|------------|--------|
| BR_01 | The solution shall be developed, validated, and documented under a compliant medical-device software lifecycle, QMS, and risk-management process appropriate to its safety classification, with full traceable evidence sufficient to obtain and retain market access in the target jurisdictions. | Demonstrable conformance and a certified quality system are a non-negotiable precondition of lawfully placing a medical device on the market; without it nothing else can be sold or deployed. | Quality/Regulatory | High | KA_13 |
| BR_02 | The solution shall be classified according to the applicable medical-device software safety standard, with its safety classification justified and any class-reducing risk-control measures documented and traced. | A justified, documented safety classification governs the rigour of the entire lifecycle and is required evidence for regulatory review; mis-classification invalidates the conformance argument. | Quality/Regulatory | High | KA_13 |
| BR_03 | The solution shall implement a documented software development lifecycle conforming to the applicable medical-device software standard (planning, requirements, architecture, implementation, integration, verification, release, and maintenance), with bidirectional traceability across all artefacts. | A conformant, traceable lifecycle is the core obligation of the standard for the software's safety class and the basis of the technical file; it is what auditors and notified bodies examine. | R&D | High | KA_13 |
| BR_04 | The diagnostic decision-support function shall be sourced as a commercially validated, off-the-shelf capability integrated as a black box across a defined interface that exchanges structured patient data and structured ranked diagnostic candidates, rather than developed in-house for the first release. | An off-the-shelf validated diagnostic capability is the primary mitigation for algorithmic-clearance delay and model-validation complexity, materially lowering development and validation risk and accelerating market entry; treating it as a black box at a defined data interface is what keeps the integration feasible without inheriting the capability's internal model-validation burden. Commercially, the decision-support capability is the headline differentiator over passive monitoring that justifies the purchase premium, so sourcing a clinically credible, already-validated capability is also what makes the value proposition defensible to a buyer at point of sale. | Management | High | KA_14, KA_02 |
| BR_05 | The use of an externally sourced diagnostic capability shall be governed by supplier qualification, change-control, interface-stability assurance, and a second-source/exit contingency, with a documented allocation of responsibility and liability. | As the party placing the device on the market, the manufacturer remains accountable for the integrated device regardless of where the diagnostic capability originates; the strategic supplier dependency must be contained contractually and technically. | Legal | High | KA_14, KA_02 |
| BR_06 | The development scope shall be confined to software that accesses fixed physical components solely through their published interface control documents; the internal design, behaviour, and physical characteristics of those components shall be treated as fixed and external, and no hardware design, selection, or modification shall be undertaken. | Confining scope to software, with every physical component reached only through its published interface, reduces development, validation, and time-to-market risk and keeps the validated-configuration matrix bounded; the components' fixed behaviour is a precondition the software builds on rather than something it may change. | Management | High | KA_14 |
| BR_07 | Interoperability with measurement and display components shall be bounded to a defined, validated set of component interfaces and to the defined set of non-invasive measurement device types the solution is validated against. | Supporting unbounded device variants would inflate QMS, regression-testing, and post-market burden; bounding interoperability to the validated device-type set and their interfaces keeps the supportability and liability envelope manageable while still protecting the installed-base investment. | Quality/Regulatory | High | KA_12, KA_15 |
| BR_08 | The solution shall be brought to market within a competitive time-to-market window for a first release, with risk-reduction strategies (off-the-shelf sourcing, scope confinement) selected to protect that schedule. | Time-criticality of clinical value and competitive positioning make schedule a primary business driver; the chosen sourcing and scope strategy exists in large part to protect first-release timing. | Management | High | KA_14, KA_03 |
| BR_09 | The solution shall be maintainable and updatable over its service life, with the capacity to deliver timely safety and security updates and to track and re-validate changes in the externally sourced diagnostic capability and component interfaces, every such update itself being released through the conformant lifecycle and re-verified before deployment. | Maintainability and timely patching are binding post-market obligations and essential to keeping a safety-critical device dependable and compliant; because the software is itself regulated, an update is not deployable until it has passed the same lifecycle and verification as the original release, so supplier and interface changes must be absorbed through that controlled change path rather than ad hoc. | Operations/Service | High | KA_15 |
| BR_10 | The manufacturer shall resource and operate the post-market obligations of the device — complaint handling, vigilance/adverse-event reporting, and post-market surveillance — over the full service life. | These are mandatory recurring lifecycle obligations and a concentration of liability; they must be staffed and budgeted up front, not deferred, or compliance and dependability risk rises sharply. | Quality/Regulatory | High | KA_15, KA_13 |
| BR_11 | The solution shall be supportable and serviceable at scale, including the enablement of training so that trained clinical users can build and maintain competence before relying on the diagnostic output with real patients. | Supportability at scale and clinician competence reduce deployment friction and directly mitigate the critical risk of misinterpreting diagnostic candidates; training enablement is both a usability-engineering and a service obligation. | Operations/Service | Medium | KA_15, KA_09 |
| BR_12 | The solution shall integrate with hospital information systems through recognised health-data interoperability standards as a commercial requirement, with the exact protocol and interface control documents selected and defined early, before the interface design is committed. | Standards-based HIS integration extends clinical value, avoids bespoke integration and data silos, and is a hard procurement gate: hospital IT and clinical-engineering buyers will not approve a device that cannot exchange data over their established interoperability standards, so absence of credible standards-based integration is a typical buying showstopper rather than a nice-to-have. The protocol is not yet fixed, so resolving it and its interface control documents early is the dominant mitigation for the connectivity/real-time integration risk and a precondition for designing the share path to its timing budget. | Commercial | High | KA_10, KA_12 |
| BR_13 | The solution shall offer transparent, predictable acquisition/licensing cost and a low, quantifiable total cost of ownership over the service life, supporting a defensible return-on-investment case for the buying organisation, and the programme shall be backed by a validated business case clearing the manufacturer's investment threshold. | Affordable, predictable cost of ownership is a primary procurement decision driver; constrained healthcare buyers justify capital purchases on a demonstrable return — clinician time saved, faster time-to-diagnosis, and reuse of the existing installed base rather than hardware replacement — so a quantifiable TCO/ROI argument is what unlocks budget approval. A financeable business case is in turn the gating condition for the manufacturer to commit to development at all. | Commercial | Medium | KA_11, KA_16 |
| BR_14 | The solution shall fit the legal manufacturer's portfolio and strategy and be developable within its existing R&D, quality, and regulatory competency, capacity, and budget, with internal-department interests aligned. | Strategic portfolio fit and available competencies are the gating organisational condition; without them every downstream capability is at risk, and unresolved internal tensions (development flexibility versus design-freeze and compliance lock-down) jeopardise delivery. | Management | High | KA_16 |
| BR_15 | Residual liability arising from safety-critical decision-support output shall be contained through validated-use boundaries, human-in-the-loop control, supplier qualification, and post-market surveillance. | The decision-support function is the largest liability concentration; the manufacturer stays accountable for its safety even when externally sourced, so liability containment measures are a standing business constraint. | Legal | High | KA_16, KA_02, KA_04 |
| BR_16 | The solution shall be producible and deployable repeatably at quality across multiple care settings and fleet units without per-site re-engineering. | Repeatable, scalable deployment protects prior equipment investment, enables phased enterprise-wide rollout, and keeps production/deployment within the validated, supportable envelope. | Operations/Service | Medium | KA_12, KA_15 |
| BR_17 | The solution shall have a defined end-of-life, including the discontinuation, decommissioning, and data-handling obligations consistent with its regulatory and data-protection duties. | A defined end-of-life is part of the post-market lifecycle the manufacturer must plan and stand behind; uncontrolled discontinuation creates compliance, dependability, and data-protection exposure. | Quality/Regulatory | Medium | KA_15, KA_13 |
| BR_18 | The solution shall be offered with committed, contractable reliability/availability and support-responsiveness terms — including assured update and complaint-response timeframes — appropriate to a continuously relied-upon critical-care device. | Clinical-engineering and procurement buyers do not purchase a critical-care device on capability alone; they contract on dependability and supplier responsiveness, so explicit, contractable reliability and support-response commitments are a baseline competitive expectation and a frequent buying gate. Without committed terms the buyer carries un-quantified operational risk and will favour an offering that provides them. | Commercial | High | KA_15 |

## Context (FORMAL)

The context level is the start of the solution domain (DHF), based on the problem domain and the stakeholder expectations.

### Intended Use (IU_01)

Write the intended use as a single, flowing prose statement that naturally covers the five aspects — what the product is, what it does (medical indication), who uses it (user profile), where it is used (use environment), and how it works (operating principle). Do **not** add bold labels or headers for the aspects; weave them into the sentences.

| ID | Description |
|----|-------------|
| IU_01 | The Mobile Monitoring Software Solution (MMSS) is medical device software (SaMD) that transforms a portable patient monitor into an active clinical decision-support tool, providing trained medical professionals with continuous, real-time monitoring of patient vital signs together with AI-driven, ranked diagnostic candidates and clinical alarms to support — but not replace — their independent clinical assessment and treatment of critically ill patients in critical-care and mobile or pre-hospital settings such as intensive care units, emergency rooms, and mobile medical units. The diagnostic candidates are presented as ranked decision support intended to inform, not to autonomously determine, the diagnosis or course of treatment, which remain the responsibility of the trained professional user. In operation, MMSS acquires data from a defined set of non-invasive measurement devices through standardised interfaces, processes that data through an AI-driven diagnostic capability to derive ranked diagnostic candidates, presents the vital signs and diagnostic output on a connected monitor display, raises clinical alarms for abnormal patient conditions and sensor or connection faults, and optionally shares data with hospital information systems for second-opinion support. |

### Medical Device Classification (MD_01)

| ID | Description | Traces |
|----|-------------|--------|
| MD_01 | Under IEC 62304, MMSS is initially assessed as software safety Class C, because a failure or malfunction of the software could contribute to a hazardous situation that may result in death of the patient. The architectural design mitigates this to a residual software safety Class B: the safety-critical alarming and diagnostic functions are also served by external systems that are independent of MMSS — measurement devices raise their own audible connection alarms and the diagnosis algorithm signals independently on timeout — so that no single MMSS software fault is the sole cause of a serious or fatal outcome. Because these independent systems provide a non-software risk-control measure for the same hazards, the residual harm contribution of an MMSS software failure is reduced to a level consistent with Class B (possible non-serious injury rather than death or serious injury). | IU_01 |

### Context Diagram

The context diagram identifies the system of interest in relation to its context. The system of interest contains all elements that are part of the design.

_To be added_

#### Product Information

The Mobile Monitoring Software Solution (MMSS) is a regulated medical device software product (Software as a Medical Device, IEC 62304 Class C mitigated to Class B) that transforms an existing portable patient monitor from a passive vital-signs display into an active clinical decision-support tool. MMSS delivers real-time, continuous vital-signs monitoring together with AI-driven, ranked diagnostic decision support, clinical alarms for abnormal physiological conditions and sensor/connection faults, and optional sharing of diagnostic output with a Hospital Information System for a second opinion.

It operates by acquiring patient data from a defined set of non-invasive measurement devices through standardised interface control documents, processing that data through an AI analysis engine built on the externally validated Open Evidence diagnostic capability, and presenting raw vital signs, alarms, and ranked diagnostic candidates on a connected monitor display. The software runs on an existing host CPU platform and treats all physical components as fixed, external elements accessed through published interfaces.

#### System of Interest

The part of the broader system this document is about — the product, subsystem, or component you are responsible for designing.

| System Element | Description |
|----------------|-------------|
| MMSS Application Software | The complete Mobile Monitoring Software Solution — the software-only system of interest. Acquires data from non-invasive measurement devices, processes it through the AI diagnostic engine, presents vital signs, alarms and ranked diagnostic candidates on the monitor display, and optionally shares output with the HIS. Composed of the five software items below. |
| AC — Acquisition | Software item responsible for acquiring raw vital-signs data from the connected measurement devices through their interface control documents and polling logic. |
| DAC — Device Abstraction | Software item that abstracts the six device types behind a uniform internal interface, handling device drivers, polling and normalisation so the rest of MMSS is independent of device specifics. |
| DEC — Diagnostic Engine Coordination | Software item that coordinates the diagnostic flow with the external Open Evidence AI capability, submitting prepared vital-signs data and receiving ranked diagnostic candidates. |
| DPREC — Presentation | Software item that renders vital signs, clinical alarms and ranked diagnostic candidates on the monitor display and drives the timer-based UI update. |
| DPROC — Processing | Software item that processes and prepares acquired vital-signs data (within the DPROC latency budget) for presentation and for submission to the diagnostic engine. |

#### Context Elements

Essential elements for your product that are not part of the design.

| Context Element | Description |
|-----------------|-------------|
| Host CPU Platform | The existing compact embedded CPU with real-time OS capabilities that hosts and executes the MMSS software. Fixed hardware, accessed through the platform/OS interface; its internal design is out of scope. |
| ECG Monitor | Non-invasive electrocardiograph measurement device providing heart-rate data via ECG electrodes. Existing device accessed through a published ICD. |
| Pulse Oximeter | Non-invasive SpO₂ measurement device providing oxygen saturation and pulse rate via an SpO₂ probe. Existing device accessed through a published ICD. |
| BP / NIBP Monitor | Non-invasive (cuff-based) blood-pressure measurement device providing systolic, diastolic and mean arterial pressure. Existing device accessed through a published ICD. |
| Thermal / Temperature Probe | Non-invasive temperature measurement device providing patient body temperature. Existing device accessed through a published ICD. |
| Capnometer | Non-invasive end-tidal CO₂ measurement device providing respiratory rate and EtCO₂ via an EtCO₂ sampling line. Existing device accessed through a published ICD. |
| EEG Monitor | Non-invasive electroencephalograph measurement device providing the bispectral index (BIS) via EEG electrodes. Existing device accessed through a published ICD. |
| Monitor Display | The existing connected display on which MMSS presents vital signs, clinical alarms and ranked diagnostic candidates. Fixed hardware accessed through the display/presentation interface. |
| Open Evidence AI Diagnostic Capability | The external, commercially validated off-the-shelf AI diagnostic library that returns structured, ranked diagnostic candidates from submitted vital-signs data. Used as a validated component; its internal model is out of scope. |
| Hospital Information System (HIS) | The external hospital information system to which MMSS optionally shares diagnostic candidates for a second opinion. Integration protocol (HL7/FHIR) is to be defined. |

#### External Interfaces (IF_*)

Connections between the system of interest and the context elements (mechanical, chemical, electronic, digital, logical, etc.).

| ID | Name | Port 1 | Port 2 | ICD |
|----|------|--------|--------|-----|
| IF_01 | ECG Acquisition Interface | MMSS | ECG Monitor | ICD_ECG (device acquisition ICD) |
| IF_02 | Pulse Oximeter Acquisition Interface | MMSS | Pulse Oximeter | ICD_SpO2 (device acquisition ICD) |
| IF_03 | BP / NIBP Acquisition Interface | MMSS | BP / NIBP Monitor | ICD_NIBP (device acquisition ICD) |
| IF_04 | Temperature Acquisition Interface | MMSS | Thermal / Temperature Probe | ICD_TEMP (device acquisition ICD) |
| IF_05 | Capnometer Acquisition Interface | MMSS | Capnometer | ICD_EtCO2 (device acquisition ICD) |
| IF_06 | EEG Acquisition Interface | MMSS | EEG Monitor | ICD_EEG (device acquisition ICD) |
| IF_07 | Display / Presentation Interface | MMSS | Monitor Display | ICD_DISPLAY (presentation ICD) |
| IF_08 | AI Diagnostic Capability Interface | MMSS | Open Evidence AI Diagnostic Capability | ICD_OPENEVIDENCE (structured diagnostic candidates ICD) |
| IF_09 | HIS Integration Interface | MMSS | Hospital Information System (HIS) | ICD_HIS (HL7/FHIR — TBD) |
| IF_10 | Host Platform / OS Interface | MMSS | Host CPU Platform | ICD_PLATFORM (host OS / runtime ICD) |

#### Acquired Parameters / Signals

Whenever the product acquires, exchanges, or presents a **set** of parameters, signals, or data items from a set of source elements (measurement devices, sensors, sub-systems, services), enumerate that set here instead of leaving it as a collective phrase elsewhere. One row per source-element/parameter combination, taken from the input. If no such parameter set applies to this product, write `_Not applicable_`.

| Source Element | Parameter / Signal | Unit / Typical Range | Interface |
|----------------|--------------------|----------------------|-----------|
| ECG Monitor (ECG Electrodes) | Heart Rate | bpm, 30–250 | IF_01 |
| BP / NIBP Monitor (NIBP Cuff) | Systolic BP | mmHg, 40–260 | IF_03 |
| BP / NIBP Monitor (NIBP Cuff) | Diastolic BP | mmHg, 20–200 | IF_03 |
| BP / NIBP Monitor (NIBP Cuff) | Mean Arterial Pressure (MAP) | mmHg, 30–220 | IF_03 |
| Pulse Oximeter (SpO₂ Probe) | SpO2 | %, 0–100 | IF_02 |
| Pulse Oximeter (SpO₂ Probe) | Pulse Rate | bpm, 30–250 | IF_02 |
| Capnometer (EtCO₂ Sampling Line) | Respiratory Rate | breaths/min, 0–80 | IF_05 |
| Capnometer (EtCO₂ Sampling Line) | EtCO2 | mmHg, 0–100 | IF_05 |
| Thermal / Temperature Probe | Temperature | °C, 25–45 | IF_04 |
| EEG Monitor (EEG Electrodes) | BIS (Bispectral Index) | index, 0–100 | IF_06 |

## Users

### User Groups

Collections of users who share common characteristics (a synonym is User Role).

| User | User Group | User Profile |
|------|------------|--------------|
| ICU nurse / bedside clinician | Bedside Clinician | Trained, registered critical-care nurse working at the patient bedside in an intensive care unit. Skilled in continuous vital-signs monitoring, sensor placement (ECG, pulse oximeter, BP, thermal, capnometry, EEG), and rapid response to clinical alarms. Operates the MMSS for prolonged shifts in a high-acuity, multi-patient environment, often managing several monitors at once. Key needs: at-a-glance vital-signs readability, unambiguous alarm differentiation (vital vs. connection/misplacement), low false-alarm fatigue, and clear, ranked AI diagnostic candidates that support rather than replace clinical judgement. |
| Emergency physician / ER physician | Emergency Physician | Trained, licensed physician working in the emergency room. Makes time-critical diagnostic and treatment decisions on undifferentiated, acutely ill patients. Uses the MMSS to obtain real-time vital signs plus AI-driven ranked diagnostic candidates within two minutes of patient connection to accelerate triage and treatment. Works under time pressure with frequent interruptions. Key needs: fast system activation, trustworthy and interpretable diagnostic output with clear uncertainty cues, timely notification when diagnosis does not converge, and seamless second-opinion sharing to the hospital information system. |
| Paramedic / pre-hospital clinician | Pre-hospital Clinician | Trained paramedic or emergency medical professional operating in a mobile medical unit or at the pre-hospital scene. Often works single-handed or in small crews, in noisy, moving, low-light, and physically constrained conditions (ambulance, field). Connects sensors quickly to a portable patient and relies on the MMSS for continuous monitoring, abnormal-condition and sensor-fault alarms, and early diagnostic support en route to definitive care. Key needs: rugged, glanceable display, robust audible alarms in noisy environments, fast non-invasive sensor setup, reliable misplacement/connection detection, and confidence in AI candidates when expert backup is unavailable. |
| Clinical / biomedical engineer | Clinical / Biomedical Engineer | Trained biomedical or clinical engineering technician responsible for commissioning, configuring, calibrating, and maintaining the MMSS and its connected measurement devices and monitor display. Sets up device interfaces (ICDs), configures alarm thresholds and hospital information system (HL7/FHIR) integration, performs periodic checks, and resolves technical faults. Works in service/maintenance contexts rather than at the live bedside. Key needs: clear configuration and diagnostics interfaces, verifiable interface and alarm settings, controlled access to safety-critical parameters, and traceable maintenance/logging. |
| Clinical trainer / simulation instructor | Clinical Trainer | Trained clinician or designated educator who delivers hands-on and simulation-based training on the MMSS, including the mandatory simulation training mode that mitigates clinician misinterpretation of AI candidates. Familiar with both the clinical workflow and the system's operating principle. Operates the MMSS in a controlled, non-patient training environment to build competence and correct-use habits in bedside, ER, and pre-hospital users. Key needs: a clearly separated, safe simulation mode that cannot be confused with live patient use, realistic scenario playback, and the ability to demonstrate correct interpretation of ranked diagnostic candidates and alarm handling. |

### User Requirements / Needs (UR_*)

The user expectations translated over the product context into requirements specific to YOUR product. They are SMARTER than the expectations and form the base for product validation. Format: *As a \<user group\> I want \<feature\> so that \<benefit\>.*

| ID | Description | Classification | Traces |
|----|-------------|----------------|--------|
| UR_01 | As a Bedside Clinician I want MMSS to continuously display, in real time, each enumerated vital-sign parameter acquired from the connected measurement devices (the parameters listed in the Acquired Parameters / Signals table) so that I keep uninterrupted at-a-glance awareness of the patient's condition. | Safety-related | IU_01 |
| UR_02 | As a Bedside Clinician I want each enumerated vital-sign parameter (per the Acquired Parameters / Signals table) presented clearly and legibly with its value, unit and source so that I can read and interpret the patient's status at a glance under time pressure and with limited attention. | Safety-related | IU_01 |
| UR_03 | As an Emergency Physician I want MMSS to present the AI-derived diagnostic candidates as a ranked, ordered list so that I can use the most probable candidates first to support faster, better-informed triage and treatment decisions. | Safety-critical | IU_01, BR_04 |
| UR_04 | As a Pre-hospital Clinician I want the ranked diagnostic candidates to be displayed promptly once received from the diagnostic capability so that I can begin appropriate treatment without delay while en route to definitive care. | Safety-critical | IU_01, BR_04 |
| UR_05 | As a Bedside Clinician I want MMSS to raise a timely, distinctive audible and visual alarm whenever any enumerated vital-sign parameter (per the Acquired Parameters / Signals table) crosses its abnormal-condition threshold so that I can intervene before the patient deteriorates. | Safety-critical | IU_01 |
| UR_06 | As a Pre-hospital Clinician I want MMSS to raise a clearly differentiated audible and visual alarm when a measurement device is disconnected, misplaced, or no longer providing a valid signal so that I never unknowingly act on missing or misleading data, even in noisy, moving conditions. | Safety-critical | IU_01 |
| UR_07 | As an Emergency Physician I want MMSS to notify me explicitly when diagnostic support is unavailable or has not produced a result within the expected time so that I can fall back on my clinical judgement without losing time waiting silently. | Safety-critical | IU_01 |
| UR_08 | As an Emergency Physician I want each diagnostic candidate to be shown with the basis and confidence/uncertainty on which it rests so that I can judge how far to trust the AI output and retain clinical control of the decision. | Safety-critical | IU_01, BR_15 |
| UR_09 | As a Bedside Clinician I want MMSS to visually separate and distinguish measured (observed) vital signs from AI-inferred diagnostic suggestions so that I never confuse observed facts with inferred conclusions. | Safety-critical | IU_01 |
| UR_10 | As a Pre-hospital Clinician I want MMSS to be ready for monitoring quickly after activation so that I can begin monitoring a patient in an emergency without waiting on a slow startup. | Standard | IU_01 |
| UR_11 | As a Pre-hospital Clinician I want to operate MMSS at the bedside and on the move with minimal, low-effort steps and a rugged, glanceable display so that my attention stays on the patient rather than on the device. | Standard | IU_01 |
| UR_12 | As a Clinical Trainer I want MMSS to provide a clearly separated, safe simulation/training mode that cannot be confused with live patient use so that clinicians can build competence in operating MMSS and interpreting its diagnostic output before relying on it with real patients. | Safety-related | IU_01, BR_11 |
| UR_13 | As an Emergency Physician I want to share the relevant patient vital signs and ranked diagnostic candidates with the Hospital Information System so that I can obtain a timely expert second opinion on critical cases. | Essential | IU_01, BR_12 |
| UR_14 | As a Clinical / Biomedical Engineer I want to configure and commission MMSS — including device interfaces, alarm thresholds, and HIS integration settings — through a controlled configuration interface so that the system is correctly and safely set up for the care environment before clinical use. | Safety-related | IU_01, BR_07 |
| UR_15 | As a Clinical / Biomedical Engineer I want safety-critical configuration parameters (alarm thresholds, device and interface settings) to be access-controlled and traceably logged so that only authorised changes are made and every change can be audited. | Safety-related | IU_01, BR_01 |
| UR_16 | As a Bedside Clinician I want alarms differentiated by priority and type (vital-sign abnormality versus connection/misplacement fault) with low false-alarm burden so that I can recognise and respond to the correct condition without alarm fatigue. | Safety-critical | IU_01 |
| UR_17 | As a Pre-hospital Clinician I want the diagnostic output to be labelled and worded as decision support that informs, rather than determines, the diagnosis so that I remain accountable for the clinical decision and am not led to defer to the AI when expert backup is unavailable. | Safety-critical | IU_01, BR_15 |
| UR_18 | As a Bedside Clinician I want MMSS to show the recent trend (direction and rate of change over time) of each enumerated vital-sign parameter (per the Acquired Parameters / Signals table), not only its instantaneous value, so that I can recognise gradual deterioration early and intervene before an alarm threshold is crossed. | Safety-related | IU_01 |

### User DFMEA (USER_DFMEA_*)

A structured analysis of how users might misuse, misinterpret, or fail to operate the product, the consequences, and the mitigations the design must include.

| ID | Item/Function | Requirement | Failure Mode | End-effect | Rationale | Failure Cause | Severity | Prevention | Classification | Traces |
|----|---------------|-------------|--------------|------------|-----------|---------------|----------|------------|----------------|--------|
| USER_DFMEA_01 | AI diagnostic candidate display | UR_03 — ranked diagnostic candidates | Clinician over-trusts the top-ranked AI candidate and treats it as a confirmed diagnosis, skipping independent clinical assessment | Wrong or anchored treatment pathway pursued; correct condition missed or delayed | Automation bias toward a confident-looking ranked list can override clinical judgement and harm the patient | Ranked list visually reads as an authoritative verdict; no salient framing that it is probabilistic support | Critical | Persistently label output as decision support, suppress any "winner" styling, require the candidate basis/confidence to be co-displayed, and word headings as suggestions not diagnoses | Safety-critical | UR_03 |
| USER_DFMEA_02 | AI candidate confidence/basis display | UR_08 — candidate basis and confidence | Clinician acts on a candidate without registering its low confidence or weak supporting basis | High-risk treatment initiated on a poorly-supported AI suggestion | Acting on low-confidence output without recognising the uncertainty defeats the safeguard of clinician oversight | Confidence/basis shown but de-emphasised, off-screen, or in uniform styling that does not scale with risk | Critical | Render confidence and supporting basis adjacent to each candidate with salient, graded visual encoding; make low-confidence candidates visibly distinct | Safety-critical | UR_08 |
| USER_DFMEA_03 | Measured vs inferred presentation | UR_09 — separate measured from inferred | Clinician mistakes an AI-inferred suggestion for a directly measured vital sign (or vice versa) | Inferred conclusion treated as observed fact; clinical reasoning corrupted | Confusing observed facts with inferred conclusions can lead to unjustified or omitted interventions | Insufficient visual/spatial separation, shared styling, or co-located zones for measured and inferred data | Critical | Enforce distinct, spatially separated zones and visual language for measured vs inferred; label each region explicitly | Safety-critical | UR_09 |
| USER_DFMEA_04 | Decision-support framing | UR_17 — decision support, not determination | Clinician defers fully to MMSS output and abandons accountability for the clinical decision | Diagnostic responsibility abdicated to software; errors propagate unchecked | The user must remain accountable; deferring to the AI when expert backup is unavailable is unsafe | Wording or layout implies the system "decides"; no language reinforcing clinician ownership | Critical | Use decision-support wording throughout, present candidates as informing not determining, and avoid imperative/diagnostic phrasing | Safety-critical | UR_17 |
| USER_DFMEA_05 | Vital-sign alarm | UR_05 — timely vital-sign alarm | Clinician fails to notice or perceive an active vital-sign alarm | Patient deterioration goes unaddressed; intervention delayed | Missing an abnormal-condition alarm removes the primary deterioration safeguard | Alarm not distinctive enough, masked by ambient noise/motion, or visually subtle on a glanceable display | Critical | Provide distinctive, attention-grabbing audible plus visual alarms designed for noisy mobile use; persist until acknowledged | Safety-critical | UR_05 |
| USER_DFMEA_06 | Alarm differentiation | UR_16 — alarms differentiated, low false-alarm burden | Clinician suffers alarm fatigue and ignores or silences a genuine alarm, or misidentifies which condition is alarming | Real abnormality or fault disregarded; wrong corrective action taken | Alarm fatigue and ambiguous alarms erode timely, correct response | Undifferentiated alarm signals, high false-alarm rate, no priority/type encoding | Critical | Differentiate alarms by priority and type, minimise false alarms, and make alarm source unambiguous at a glance | Safety-critical | UR_16 |
| USER_DFMEA_07 | Sensor disconnection/misplacement alarm | UR_06 — disconnection/misplacement alarm | Clinician does not notice a sensor has disconnected or been misplaced and keeps acting on missing/invalid data | Decisions made on absent or misleading readings; wrong diagnosis (R_04/R_07) | Unknowingly acting on missing or misleading data is a critical patient-safety hazard | Connection/misplacement alarm not clearly differentiated from vital-sign alarms; subtle in noisy, moving conditions | Critical | Raise a clearly differentiated audible and visual connection/misplacement alarm; visibly flag affected parameter as invalid | Safety-critical | UR_06 |
| USER_DFMEA_08 | Stale-data interpretation | UR_06 — never act on missing/misleading data | Clinician reads a last-known value as a current live reading after the signal has been lost | Treatment based on outdated vital signs; deterioration masked | Stale values appearing live conceal loss of monitoring and mislead the clinician | Frozen value retained on screen without visible staleness/invalidity indication | Critical | Visibly mark parameters as stale/invalid when signal is lost rather than displaying the last value as current | Safety-critical | UR_06 |
| USER_DFMEA_09 | Diagnostic timeout notification | UR_07 — notify when diagnosis unavailable/late | Clinician keeps waiting silently for a diagnostic result and does not notice the 2-minute timeout | Treatment delayed while clinician expects an imminent result (R_06) | Not noticing the timeout delays fallback to clinical judgement and treatment | Timeout indication absent, silent, or visually subtle; no explicit "unavailable" state | Critical | Explicitly notify on timeout with audible and visual cues; show a clear "diagnosis unavailable — use clinical judgement" state | Safety-critical | UR_07 |
| USER_DFMEA_10 | Simulation/training mode | UR_12 — separated, unmistakable simulation mode | Clinician operates in training/simulation mode while believing it is a live patient session | Real patient monitored by a non-live session; alarms/diagnosis not acting on real data | Simulation mistaken for live use means a real patient is effectively unmonitored | Training mode not unmistakably distinct from live mode; weak or absent persistent mode indicator | Critical | Make simulation mode unmistakably and persistently distinct (banner, colour, watermark); block accidental entry and warn on mode | Safety-related | UR_12 |
| USER_DFMEA_11 | Live vs simulation distinction | UR_12 — cannot be confused with live use | Clinician dismisses real live data as a simulation and does not act on genuine alarms or candidates | Genuine deterioration or diagnosis ignored as "just practice" | Live data mistaken for simulation suppresses real clinical response | Insufficient affirmative indication of the live state; mode cues only present in simulation | Critical | Affirmatively and persistently indicate the live monitoring state; ensure live mode is the visually dominant default | Safety-related | UR_12 |
| USER_DFMEA_12 | Device configuration / commissioning | UR_14 — controlled configuration interface | Biomedical engineer misconfigures a device interface or assigns the wrong device/parameter mapping | Wrong or mislabelled data presented as a patient's vital sign | Misconfiguration silently corrupts every downstream reading and alarm | Configuration interface lacks validation, confirmation, or clear device-to-parameter feedback | Critical | Provide a controlled configuration interface with validation, explicit confirmation, and readback of device-parameter mapping | Safety-related | UR_14 |
| USER_DFMEA_13 | Alarm threshold configuration | UR_14 / UR_15 — threshold config, access-controlled and logged | Engineer or unauthorised user sets an alarm threshold incorrectly (too wide/narrow) | Alarms suppressed or spurious; deterioration missed or alarm fatigue induced | Incorrect thresholds directly defeat the deterioration-detection safeguard | Free-text/unbounded threshold entry, no range checks, no access control or change traceability | Critical | Constrain threshold entry to safe ranges, require confirmation, and enforce access control with traceable change logging | Safety-related | UR_14, UR_15 |
| USER_DFMEA_14 | System activation / startup | UR_10 — ready quickly after activation | Clinician begins relying on the display before MMSS has fully started and all parameters are live | Acts on an incomplete picture; absent parameters mistaken for normal | In an emergency a partially-initialised display can be misread as complete monitoring | No clear "ready/initialising" state; blank parameter fields indistinguishable from normal values | High | Show an explicit initialising-vs-ready state and clearly mark not-yet-live parameters until acquisition is confirmed | Standard | UR_10 |
| USER_DFMEA_15 | Bedside / on-the-move operation | UR_11 — low-effort, glanceable mobile operation | Clinician makes a slip or mis-tap during a high-stress, moving transport and triggers an unintended action | Wrong setting changed, alarm silenced, or workflow disrupted while attention is on the patient | Mobile, high-attention conditions make accidental inputs likely and consequential | Small/ambiguous controls, no confirmation on consequential actions, layout not optimised for motion | High | Design large, unambiguous, glanceable controls; require confirmation on consequential actions; minimise step count | Standard | UR_11 |
| USER_DFMEA_16 | HIS second-opinion sharing | UR_13 — share data for second opinion | Clinician shares the wrong patient's data or mis-selects the case sent to the Hospital Information System | Second opinion rendered on incorrect data; wrong patient associated | Sharing the wrong patient context can misdirect critical decisions | No clear patient/case confirmation before transmission; ambiguous selection in the sharing workflow | High | Require explicit patient/case confirmation and readback before HIS transmission; show what is being shared | Essential | UR_13 |
| USER_DFMEA_17 | Care hand-over / shift change | UR_16 / UR_05 — alarm priority and timely alarm | Receiving clinician takes over the device mid-session at a crew change or ED hand-off and is unaware that alarm thresholds were altered, an alarm was silenced, or specific AI candidates were already reviewed and dismissed | Genuine alarm stays suppressed, an unsafe threshold persists unnoticed, or a previously dismissed but now-relevant candidate is overlooked after the transition | Hand-over is a known high-incidence point of care; silent session state carried across a clinician change defeats the alarm and diagnostic safeguards | No visible session/hand-over state; silenced alarms, non-default thresholds, and candidate-review history are not surfaced to the incoming clinician | Critical | Surface current alarm/silence state, any non-default thresholds, and candidate-review history at hand-over; require an explicit acknowledgement of session state by the incoming clinician and time-limit alarm silences | Safety-critical | UR_16, UR_05 |
| USER_DFMEA_18 | Motion-artifact interpretation in transport | UR_02 / UR_06 — legible parameters; never act on misleading data | In a moving ambulance the clinician reads a motion- or vibration-corrupted parameter (e.g. artifactual SpO2, ECG, or BP) as a true physiological value, because the signal is present and not a disconnection | Treatment or non-treatment decision made on artifactual data; spurious values trusted or genuine deterioration masked | Motion artifact yields plausible-but-false readings that disconnection/staleness alarms do not catch, and is one of the most common pre-hospital data-quality failures | No signal-quality indication; artifact-degraded values rendered identically to clean, valid readings | Critical | Display a per-parameter signal-quality/validity indication and visibly flag low-quality or artifact-suspect values rather than presenting them as clean readings | Safety-critical | UR_02, UR_06 |

### Use Scenarios

Concrete narratives of how the product is used in the real world, walking from a triggering situation to a successful outcome. Each scenario contains use tasks (UT_*).

#### Scenario 1 — Pre-hospital arrival and rapid assessment

A paramedic crew reaches a collapsed patient in the field. The portable monitor running MMSS is powered on and sensors are applied so monitoring and early diagnostic support can begin en route to definitive care.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_01 | Activate MMSS | The Pre-hospital Clinician powers on the portable monitor; MMSS reaches the ready-for-monitoring state quickly and shows an explicit initialising-then-ready indication. | UR_10 |
| UT_02 | Apply sensors to patient | The clinician connects the non-invasive measurement devices (ECG electrodes, SpO₂ probe, NIBP cuff, EtCO₂ line, temperature probe) to the patient with minimal, low-effort steps while attention stays on the patient. | UR_11 |
| UT_03 | Confirm live vital signs | MMSS displays each acquired vital-sign parameter (Heart Rate, SpO2, Pulse Rate, Systolic/Diastolic BP, MAP, Respiratory Rate, EtCO2, Temperature, per the Acquired Parameters / Signals table) with value, unit and source; the clinician reads the patient's status at a glance. | UR_01, UR_02 |
| UT_29 | Verify signal quality before trusting readings | Before acting on the displayed values, the clinician checks the per-parameter signal-quality/validity indication and waits for or corrects any low-quality, motion-corrupted, or not-yet-live parameter (e.g. poor SpO2 perfusion, ECG motion artifact in the moving vehicle) so that early treatment decisions rest on valid rather than artifactual data. | UR_02, UR_06 |
| UT_04 | Read ranked diagnostic candidates | Within two minutes of patient connection MMSS presents the AI-derived ranked diagnostic candidates, each shown with its supporting basis and confidence, clearly framed as decision support. | UR_04, UR_08, UR_17 |
| UT_05 | Begin treatment en route | Using the most probable candidates and the live vitals, the clinician begins appropriate treatment without delay while transporting the patient to definitive care. | UR_04, UR_17 |

#### Scenario 2 — ICU bedside continuous monitoring with diagnostic support

A registered critical-care nurse runs continuous monitoring on an admitted ICU patient across a shift, using trend awareness and ranked diagnostic support while distinguishing observed data from inferred conclusions.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_06 | Maintain continuous vital-signs watch | MMSS continuously displays in real time each enumerated vital-sign parameter (per the Acquired Parameters / Signals table) so the Bedside Clinician keeps uninterrupted at-a-glance awareness. | UR_01, UR_02 |
| UT_07 | Monitor parameter trends | The clinician reviews the recent trend (direction and rate of change over time) of each vital-sign parameter to recognise gradual deterioration early, before any alarm threshold is crossed. | UR_18 |
| UT_08 | Distinguish measured from inferred data | The clinician relies on MMSS's visual separation of measured (observed) vital signs from AI-inferred diagnostic suggestions so observed facts are never confused with inferred conclusions. | UR_09 |
| UT_09 | Review ranked diagnostic candidates | The clinician consults the ranked AI candidates with their basis and confidence to support — not replace — clinical judgement on the patient's evolving condition. | UR_03, UR_08, UR_09 |
| UT_10 | Respond to a vital-sign alarm | When a parameter crosses its abnormal-condition threshold, MMSS raises a timely, distinctive, priority- and type-differentiated audible and visual alarm; the clinician recognises the source and intervenes. | UR_05, UR_16 |
| UT_30 | Hand over the active session at shift change | At a crew change or ICU shift hand-off the incoming clinician takes over the running session; MMSS surfaces the current alarm/silence state, any non-default alarm thresholds, and which diagnostic candidates were already reviewed or dismissed, and the receiving clinician explicitly acknowledges the session state so no silenced alarm, altered threshold, or prior candidate decision is carried across unseen. | UR_16, UR_05 |

#### Scenario 3 — Sensor disconnection / misplacement during transport

While moving a patient, a sensor becomes disconnected or misplaced. MMSS must make this unmistakable so the clinician never acts on missing or invalid data.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_11 | Detect connection/misplacement fault | A measurement device is disconnected, misplaced, or stops providing a valid signal; MMSS raises a clearly differentiated audible and visual connection/misplacement alarm distinct from vital-sign alarms, even in noisy, moving conditions. | UR_06, UR_16 |
| UT_12 | Identify affected parameter as invalid | MMSS visibly flags the affected parameter (per the Acquired Parameters / Signals table) as stale/invalid rather than showing the last value as current, so the Pre-hospital Clinician does not read a frozen value as live. | UR_06 |
| UT_13 | Restore the signal and resume valid monitoring | The clinician reseats or replaces the affected sensor; MMSS confirms valid signal acquisition and clears the fault state, returning the parameter to a live, trusted reading. | UR_06, UR_01 |

#### Scenario 4 — Diagnostic timeout / support unavailable

The AI diagnostic engine does not converge within the expected time. The clinician must be told explicitly so no time is lost waiting silently.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_14 | Receive explicit timeout notification | When diagnostic support has not produced a result within the expected time, MMSS notifies the Emergency Physician explicitly with audible and visual cues and shows a clear "diagnosis unavailable — use clinical judgement" state. | UR_07 |
| UT_15 | Fall back to clinical judgement | The physician proceeds on the live vital signs and clinical judgement without waiting further, retaining accountability for the decision. | UR_07, UR_17 |
| UT_16 | Resume diagnostic support when available | If the diagnostic capability later returns a result, MMSS presents the ranked candidates with basis and confidence, clearly framed as decision support, for the physician to consider alongside the decision already in progress. | UR_03, UR_08, UR_17 |

#### Scenario 5 — Simulation / training session

A clinical trainer runs a hands-on simulation session in a controlled, non-patient environment to build correct-use competence, with the training mode unmistakably separated from live use.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_17 | Enter simulation/training mode | The Clinical Trainer deliberately enters the separated simulation/training mode; MMSS makes the mode unmistakably and persistently distinct from live patient use (banner, colour, watermark) and guards against accidental entry. | UR_12 |
| UT_18 | Play a clinical scenario | The trainer plays a realistic scenario; MMSS reproduces vital-sign behaviour and AI diagnostic candidates so trainees practise interpretation in a safe setting. | UR_12, UR_03 |
| UT_19 | Demonstrate correct candidate interpretation | The trainer demonstrates reading ranked candidates with their basis and confidence as decision support, and correct handling of vital-sign and connection/misplacement alarms. | UR_08, UR_16, UR_17 |
| UT_20 | Exit to live mode | The trainer exits simulation; MMSS affirmatively and persistently returns to the visually dominant live monitoring state so the next session cannot be mistaken for practice. | UR_12 |

#### Scenario 6 — HIS second-opinion sharing

An emergency physician shares a critical case with the Hospital Information System to obtain a timely expert second opinion.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_21 | Select case to share | The Emergency Physician selects the relevant patient vital signs and ranked diagnostic candidates to share with the Hospital Information System. | UR_13 |
| UT_22 | Confirm patient/case before transmission | MMSS requires explicit patient/case confirmation and shows a readback of exactly what will be shared, so the correct patient context is sent. | UR_13 |
| UT_23 | Transmit and obtain second opinion | MMSS transmits the selected vital signs and ranked candidates to the Hospital Information System promptly, enabling a timely expert second opinion on the critical case. | UR_13 |

#### Scenario 7 — Device setup / configuration by clinical engineer

A clinical/biomedical engineer commissions MMSS for a care environment, configuring device interfaces, alarm thresholds and HIS integration under controlled, access-controlled conditions before clinical use.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_24 | Authenticate to configuration interface | The Clinical / Biomedical Engineer signs in to the controlled configuration interface; MMSS enforces access control so only authorised changes to safety-critical parameters are permitted. | UR_14, UR_15 |
| UT_25 | Configure device interfaces and mappings | The engineer configures each measurement-device interface (IF_01–IF_06) and its device-to-parameter mapping; MMSS validates entries and reads back the device-parameter mapping for confirmation. | UR_14 |
| UT_26 | Set alarm thresholds within safe ranges | The engineer sets vital-sign alarm thresholds for the enumerated parameters; MMSS constrains entry to safe ranges and requires explicit confirmation. | UR_14, UR_15 |
| UT_27 | Configure HIS integration | The engineer configures the Hospital Information System integration settings (HL7/FHIR) needed for second-opinion sharing. | UR_14, UR_13 |
| UT_28 | Confirm, log and commission | MMSS records every configuration change in a traceable, access-controlled log and confirms the system is correctly and safely set up before release for clinical use. | UR_15, UR_14 |

### Usability FMEA (UFMEA_*)

An FMEA focused on usability: where the user interface, workflow, or interaction model can lead to errors, slow operation, or unsafe outcomes.

| ID | Scenario Title | Use Error | Cause | Effect | HF Cause | Rationale | Usability Impact Level | Mitigation (existing) | Mitigation (new) | Classification | Traces |
|----|----------------|-----------|-------|--------|----------|-----------|------------------------|-----------------------|------------------|----------------|--------|
| UFMEA_01 | Read ranked diagnostic candidates (Scenario 1) | Clinician taps/reads the top-ranked MMSS candidate and treats it as the confirmed diagnosis | The ranked-list interaction model presents the highest candidate as the visually dominant "answer", inviting one-glance acceptance | Anchored or wrong treatment pathway begun; correct condition delayed or missed (R_05) | Automation bias plus visual saliency of rank 1; the layout shortcuts deliberate appraisal of the full list | Over-trust of a confident-looking ranked candidate is the central AI-misinterpretation hazard for MMSS | Critical | MMSS labels output as decision support and co-displays basis/confidence; mandatory simulation-mode training | Suppress any "winner"/highlighted-first styling; render candidates as a peer set with equal visual weight and persistent "suggestion, not diagnosis" framing on the candidate panel | Safety-critical | UT_04 |
| UFMEA_02 | Read ranked diagnostic candidates (Scenario 1) | Clinician acts on a candidate without registering that its confidence is low or its basis is weak | Confidence/basis is shown in uniform styling that does not scale visually with risk, so low-confidence reads the same as high | High-risk treatment initiated on a poorly-supported AI suggestion | Inattentional blindness to a de-emphasised secondary attribute under time pressure | Acting on low-confidence output defeats the clinician-oversight safeguard MMSS depends on | Critical | Confidence and basis rendered adjacent to each candidate | Graded, salient visual encoding of confidence (e.g. colour band + explicit low-confidence flag) that makes weakly-supported candidates visibly distinct before they can be selected | Safety-critical | UT_04 |
| UFMEA_03 | Distinguish measured from inferred data (Scenario 2) | Clinician reads an AI-inferred suggestion as a directly measured vital sign, or vice versa | Measured values and inferred outputs share styling or sit in adjacent/co-located zones on the MMSS display | Inferred conclusion treated as observed fact; clinical reasoning corrupted | Visual grouping/proximity cues lead the eye to treat co-located items as the same data class | Confusing observed facts with inferred conclusions causes unjustified or omitted interventions | Critical | Distinct labelled regions intended for measured vs inferred | Enforce spatially separated zones with distinct visual language (typography, border, iconography) and explicit region labels that persist; never interleave inferred items into the measured-vitals grid | Safety-critical | UT_08 |
| UFMEA_04 | Respond to a vital-sign alarm (Scenario 2) | Clinician does not perceive an active vital-sign alarm | On a glanceable display in a noisy, vibrating environment the alarm cue is not distinctive enough to break attention from the patient | Deterioration goes unaddressed; intervention delayed | Limited attentional capacity under high workload; weak salience fails to capture attention | Missing an abnormal-condition alarm removes the primary deterioration safeguard | Critical | Distinctive audible plus visual alarm designed for noisy mobile use; alarm persists until acknowledged | Multi-modal escalating alarm (audible + high-contrast visual + optional tactile) tuned for ambient ambulance/ICU noise and motion; ensure alarm overrides non-critical screen content | Safety-critical | UT_10 |
| UFMEA_05 | Respond to a vital-sign alarm (Scenario 2) | Clinician cannot tell which parameter or condition is alarming, or silences the wrong one | Alarms are not differentiated by priority/type, so the alarm signal does not encode its source | Wrong corrective action taken; or a genuine alarm silenced while another persists | Cognitive load and ambiguous mapping between signal and source under stress | Ambiguous alarms erode timely, correct response and drive alarm fatigue | Critical | Alarms differentiated by priority and type; false-alarm burden minimised | Make alarm source unambiguous at a glance (parameter highlighted in-place, source named on the alarm banner) and require source-specific acknowledgement rather than a global silence | Safety-critical | UT_10 |
| UFMEA_06 | Detect connection/misplacement fault (Scenario 3) | Clinician does not notice a connection/misplacement alarm and keeps acting on missing or invalid data | The connection/misplacement alarm is not clearly differentiated from vital-sign alarms and is subtle in moving conditions | Decisions made on absent or misleading readings; wrong diagnosis (R_04/R_07) | Mode/signal confusion — fault alarms blend with physiological alarms; weak salience under motion | Unknowingly acting on missing data is a critical patient-safety hazard | Critical | Clearly differentiated audible and visual connection/misplacement alarm distinct from vital-sign alarms | Give fault alarms a distinct signature (icon, colour, tone family) reserved exclusively for data-validity faults so they are never confused with physiological alarms | Safety-critical | UT_11 |
| UFMEA_07 | Identify affected parameter as invalid (Scenario 3) | Clinician reads a frozen last-known value as a current live reading after signal loss | On signal loss MMSS retains the last value on screen without an obvious staleness/invalidity indication | Treatment based on outdated vital signs; deterioration masked | Change blindness — a static value that previously updated is assumed still live | Stale values appearing live conceal loss of monitoring and mislead the clinician | Critical | Affected parameter intended to be flagged stale/invalid rather than shown as current | Visibly invalidate the parameter on signal loss (grey-out, strike, "no signal" overlay, stop the value animation) so a stale reading can never be mistaken for a live one | Safety-critical | UT_12 |
| UFMEA_08 | Verify signal quality before trusting readings (Scenario 1) | Clinician trusts a motion- or artifact-corrupted parameter as a true physiological value | Artifact-degraded values are rendered identically to clean readings, with no signal-quality indication | Treatment or non-treatment decision made on artifactual data; spurious value trusted or deterioration masked | Surface-level perception — a present, plausible value is accepted without quality appraisal | Motion artifact yields plausible-but-false readings that disconnection/staleness alarms do not catch | Critical | Per-parameter signal-quality/validity indication; artifact-suspect values flagged | Always-visible per-parameter signal-quality indicator and visible degradation of artifact-suspect values (e.g. dimmed value + quality icon) so low-quality data cannot read as clean | Safety-critical | UT_29 |
| UFMEA_09 | Receive explicit timeout notification (Scenario 4) | Clinician keeps waiting silently and does not notice the 2-minute diagnostic timeout | The "diagnosis unavailable" state is silent or visually subtle, with no explicit transition out of the waiting state | Treatment delayed while the clinician expects an imminent result (R_06) | Attention sustained on an implicit "pending" expectation; absence of a signal is not noticed | Not noticing the timeout delays fallback to clinical judgement and treatment | Critical | ALGOS and MMSS both notify on timeout; explicit "diagnosis unavailable — use clinical judgement" state | Replace the silent pending state with an explicit audible+visual timeout notification and a persistent, unmistakable "unavailable — use clinical judgement" banner | Safety-critical | UT_14 |
| UFMEA_10 | Enter simulation/training mode (Scenario 5) | Clinician operates in simulation mode while believing it is a live patient session | The training mode is not unmistakably and persistently distinct from live mode; the mode indicator is weak or transient | A real patient is monitored by a non-live session; alarms/diagnosis not acting on real data | Mode confusion — insufficient persistent cue to maintain correct mental model of system state | Simulation mistaken for live use means a real patient is effectively unmonitored | Critical | Separated simulation mode with banner/colour/watermark; accidental entry guarded; mandatory training | Persistent full-screen mode signature (border, watermark, colour theme) that cannot be dismissed, plus an explicit live-vs-simulation confirmation on every mode entry | Safety-related | UT_17 |
| UFMEA_11 | Exit to live mode (Scenario 5) | Clinician dismisses real live data as "just a simulation" and ignores genuine alarms or candidates | Live state is not affirmatively indicated; mode cues exist only for simulation, so live reads as ambiguous | Genuine deterioration or diagnosis ignored as practice | Mode confusion in the opposite direction — absence of a live cue defaults to a "practice" assumption | Live data mistaken for simulation suppresses real clinical response | Critical | Affirmative, persistent, visually dominant live monitoring state on exit from simulation | Make the live state the unmistakable visual default with its own persistent affirmative indicator, so a session is never ambiguous as to whether it is real | Safety-related | UT_20 |
| UFMEA_12 | Hand over the active session at shift change (Scenario 2) | Receiving clinician takes over without seeing that an alarm was silenced, a threshold altered, or candidates already dismissed | No visible session/hand-over state; silenced alarms, non-default thresholds and candidate-review history are not surfaced at the transition | Genuine alarm stays suppressed, unsafe threshold persists, or a relevant dismissed candidate is overlooked | Memory/handoff gap — incoming clinician lacks the prior clinician's session context; invisible state is forgotten | Hand-over is a high-incidence point of care; silent carried-over state defeats alarm and diagnostic safeguards | Critical | Hand-over state surfaced; explicit acknowledgement of session state required; alarm silences time-limited | Dedicated hand-over view that surfaces current silence state, non-default thresholds and candidate-review history, gated by an explicit incoming-clinician acknowledgement before monitoring continues | Safety-critical | UT_30 |
| UFMEA_13 | Confirm patient/case before transmission (Scenario 6) | Clinician shares or confirms the wrong patient's case to the Hospital Information System | The sharing workflow allows transmission without a clear patient/case confirmation, or selection is ambiguous | Second opinion rendered on incorrect data; wrong patient associated | Slip/selection error under stress; weak feedback on what is selected | Sharing the wrong patient context can misdirect critical decisions | High | Explicit patient/case confirmation and readback of exactly what will be shared before transmission | Two-step confirm with a readback summary (patient identity + listed items) that must be affirmed before the transmit control is enabled | Essential | UT_22 |
| UFMEA_14 | Configure device interfaces and mappings (Scenario 7) | Engineer assigns the wrong device-to-parameter mapping during commissioning | The configuration UI lacks validation, confirmation, or clear device-to-parameter readback | Wrong or mislabelled data later presented as a patient's vital sign | High cognitive load over many similar interface entries; no closed-loop confirmation of intent | Misconfiguration silently corrupts every downstream reading and alarm | Critical | Controlled configuration interface with validation and device-parameter readback | Structured mapping UI with per-channel validation, an explicit readback-and-confirm step, and a visual device→parameter map the engineer must verify before commit | Safety-related | UT_25 |
| UFMEA_15 | Set alarm thresholds within safe ranges (Scenario 7) | Engineer sets an alarm threshold too wide or too narrow | Free-text or unbounded threshold entry with no range checks | Alarms suppressed or spurious; deterioration missed or alarm fatigue induced | Data-entry slip plus absence of a constraining affordance | Incorrect thresholds directly defeat the deterioration-detection safeguard | Critical | Threshold entry constrained to safe ranges; explicit confirmation; access-controlled and logged | Bounded input controls (sliders/steppers) with safe-range limits and out-of-range warnings, plus a confirmation summary of all changed thresholds before commit | Safety-related | UT_26 |
| UFMEA_16 | Activate MMSS (Scenario 1) | Clinician relies on the display before MMSS has fully started and all parameters are live | No clear initialising-vs-ready state; blank parameter fields are indistinguishable from normal values | Acts on an incomplete picture; absent parameters mistaken for normal | A partially-initialised display is misread as complete monitoring under emergency time pressure | In an emergency a not-yet-ready display can be taken as a full, normal picture | High | Explicit initialising-then-ready indication on activation | Distinct visual treatment for not-yet-live parameters (placeholder + "acquiring" state) and a clear system-ready confirmation, so empty fields never read as normal values | Standard | UT_01 |
| UFMEA_17 | Apply sensors to patient (Scenario 1) | Clinician makes a slip or mis-tap on a small control in a moving vehicle and triggers an unintended action | Controls are small/ambiguous and consequential actions lack confirmation; layout not optimised for motion | Wrong setting changed, alarm silenced, or workflow disrupted while attention is on the patient | Motor-control degradation under vibration plus divided attention; small target size | Mobile, high-attention conditions make accidental inputs likely and consequential | High | Glanceable mobile operation intended; low step count | Large, well-spaced touch targets sized for in-motion use, confirmation on consequential/destructive actions, and guarding of safety-critical controls against accidental activation | Standard | UT_02 |
| UFMEA_18 | Maintain continuous vital-signs watch (Scenario 2) | Clinician misreads a parameter because value, unit, or source is ambiguous or cramped on the display | Dense layout, small type, or missing/unclear unit and source labelling on the vital-signs grid | A value is read against the wrong unit, scale, or source, leading to a misjudged clinical state | Perceptual error from low legibility and missing disambiguating context | At-a-glance monitoring depends on every value being unambiguously legible with its unit and source | Medium | Each parameter shown with value, unit and source for at-a-glance reading | Enforce a legibility standard (minimum type size, contrast, persistent unit + source per parameter) validated for typical viewing distance and motion | Standard | UT_06 |
| UFMEA_19 | Respond to a vital-sign alarm (Scenario 2) | Clinician habitually silences or repeatedly pauses alarms and a genuine alarm stays suppressed | A high burden of false/nuisance alarms trains the clinician to reflexively silence; a global or easily-repeated silence control makes blanket suppression effortless | A true deterioration alarm is silenced or never re-presented; intervention delayed or missed | Alarm fatigue and learned habituation under sustained high alarm load; reflexive motor response silences before appraisal | Alarm fatigue from over-silencing is a leading real-world cause of missed critical alarms and is distinct from failing to perceive a single alarm | Critical | Alarms differentiated by priority/type; false-alarm burden minimised; alarm silences time-limited | Time-bounded, source-specific silence only (no indefinite global mute); auto re-annunciation of an unresolved critical alarm after timeout, escalation if repeatedly silenced, and a persistent visible indication that an alarm is currently silenced | Safety-critical | UT_10 |
| UFMEA_20 | Resume diagnostic support when available (Scenario 4) | Clinician reverses or abruptly changes an in-progress treatment on a late-arriving AI candidate, or anchors to it as confirmation | After a timeout fallback, returning ranked candidates appear without clearly marking that a clinical decision is already in progress, inviting unconsidered course-change or confirmation bias | Sound fallback treatment disrupted, or a wrong late candidate over-weighted; care destabilised mid-treatment | Recency and confirmation bias — a freshly presented "answer" displaces a decision already committed under uncertainty | Late-arriving decision support during active treatment is a real interaction hazard not covered by the initial-presentation rows | Critical | MMSS frames candidates as decision support with basis/confidence; explicit "diagnosis unavailable — use clinical judgement" fallback state | Present returning candidates non-intrusively as supplementary input (no modal interrupt, no auto-focus), clearly time-stamped and flagged as arriving after fallback, so they support rather than override the decision already underway | Safety-critical | UT_16 |



### Usability Requirements (USR_*)

Measurable requirements for how the product must perform from a user perspective: task completion times, error rates, learnability, accessibility. Validated through usability testing.

| ID | Requirement | Classification | Traces |
|----|-------------|----------------|--------|
| USR_01 | MMSS shall render each updated vital-sign value on the display within 1 second of acquisition, such that in ≥ 95% of validation trials a trained clinician confirms the displayed value matches the current acquired reading. | Safety-related | UR_01, UR_02, UFMEA_18 |
| USR_02 | On the MMSS vital-signs display, each parameter's value, unit and source shall be legible (minimum character height and a luminance contrast ratio of ≥ 4.5:1 against background) such that a trained clinician correctly reads value, unit and source in ≥ 98% of trials at the specified viewing distance (≤ 1 m) under simulated motion, with no unit/scale misread errors deemed clinically significant. | Standard | UR_02, UFMEA_18 |
| USR_03 | A trained clinician shall correctly identify and act on the highest-priority active vital-sign alarm within 5 seconds of its onset in ≥ 95% of validation trials conducted under simulated ambulance/ICU ambient noise (≥ 80 dB(A)) and motion. | Safety-critical | UR_05, UR_16, UFMEA_04, UFMEA_05 |
| USR_04 | A trained clinician shall correctly identify which parameter or condition is alarming and which alarm priority/type applies (vital-sign abnormality vs connection/misplacement fault) in ≥ 95% of trials, with 0 instances of silencing or acting on the wrong alarm source in validation testing. | Safety-critical | UR_06, UR_16, UFMEA_05, UFMEA_06 |
| USR_05 | A trained clinician shall correctly distinguish a connection/misplacement fault alarm from a physiological vital-sign alarm in ≥ 95% of trials, with < 2% of users confusing the two alarm classes in validation testing. | Safety-critical | UR_06, UFMEA_06 |
| USR_06 | When a measurement device signal is lost or invalid, MMSS shall display the affected parameter in a visibly invalidated state within 1 second of trigger, such that < 2% of users in validation testing read the last-known value as a current live reading. | Safety-critical | UR_06, UFMEA_07 |
| USR_07 | Artifact-suspect or low-signal-quality vital-sign values shall be visually degraded and accompanied by a signal-quality indicator such that < 5% of users in validation testing trust an artifact-corrupted value as a clean physiological reading. | Safety-critical | UR_05, UFMEA_08 |
| USR_08 | Measured (observed) vital signs shall be visually and spatially distinguishable from AI-inferred diagnostic candidates such that < 2% of users in validation testing confuse an inferred candidate for a measured value or vice versa. | Safety-critical | UR_09, UFMEA_03 |
| USR_09 | The MMSS diagnostic-candidate panel shall present candidates as a peer set with persistent "suggestion, not diagnosis" framing such that, in validation testing, ≥ 90% of clinicians describe the output as decision support and < 5% treat the top-ranked candidate as a confirmed diagnosis without independent appraisal. | Safety-critical | UR_03, UR_17, UFMEA_01 |
| USR_10 | Each diagnostic candidate's confidence and supporting basis shall be displayed with graded, salient visual encoding such that, in validation testing, a clinician correctly identifies a low-confidence candidate as such in ≥ 95% of trials before selecting it. | Safety-critical | UR_08, UFMEA_02 |
| USR_11 | MMSS shall display ranked diagnostic candidates within 1 second of receipt from the diagnostic capability, confirmed in ≥ 95% of validation trials. | Safety-critical | UR_04, UFMEA_01 |
| USR_12 | On diagnostic timeout, MMSS shall present an explicit audible-and-visual "diagnosis unavailable — use clinical judgement" notification that a trained clinician notices and correctly interprets within 5 seconds in ≥ 95% of validation trials, with 0 silent-timeout misses. | Safety-critical | UR_07, UFMEA_09 |
| USR_13 | The live versus simulation/training mode of MMSS shall be identifiable by a trained clinician within 1 second of viewing the display in 100% of validation trials, with 0 mode-confusion errors (neither operating simulation as live nor dismissing live as simulation). | Safety-related | UR_12, UFMEA_10, UFMEA_11 |
| USR_14 | MMSS shall reach a clearly indicated monitoring-ready state within 10 seconds of activation, and until ready shall mark not-yet-live parameters distinctly such that < 2% of users in validation testing mistake an initialising display for complete, normal monitoring. | Standard | UR_10, UFMEA_16 |
| USR_15 | All consequential and safety-critical MMSS touch controls shall use targets of at least 9 mm sized and spaced for in-motion use, such that under simulated vehicle motion the unintended-activation (mis-tap) rate is < 1% and all consequential/destructive actions require confirmation. | Standard | UR_11, UFMEA_17 |
| USR_16 | A new trained clinician shall, after no more than 30 minutes of structured training in simulation mode, complete the core monitoring, alarm-response and diagnostic-review tasks unaided with a ≥ 90% first-attempt success rate. | Standard | UR_11, UR_12, UFMEA_10 |
| USR_17 | The MMSS alarm-silence interaction shall permit only time-bounded, source-specific silencing (no indefinite global mute) with a persistent visible "alarm silenced" indication, such that no unresolved critical alarm remains silenced beyond its time limit and 0 genuine critical alarms are permanently suppressed in validation testing. | Safety-critical | UR_16, UFMEA_19 |
| USR_18 | Before any transmission to the Hospital Information System, MMSS shall require a two-step patient/case confirmation with readback such that the wrong-patient or wrong-content transmission rate is 0 in validation testing. | Essential | UR_13, UFMEA_13 |
| USR_19 | The MMSS device-interface configuration workflow shall require per-channel validation and an explicit device-to-parameter readback-and-confirm step such that the rate of undetected wrong device-to-parameter mappings committed by an engineer is 0 in validation testing. | Safety-related | UR_14, UFMEA_14 |
| USR_20 | Alarm-threshold entry in MMSS shall use bounded controls limited to safe ranges with out-of-range warnings and a change-confirmation summary, such that no out-of-safe-range threshold can be committed and the wrong-threshold commit rate is 0 in validation testing. | Safety-related | UR_14, UR_15, UFMEA_15 |
| USR_21 | At care hand-over MMSS shall present a persistent, visible session-state summary (silenced alarms with remaining silence time, any non-default alarm thresholds, and unacknowledged diagnostic candidates) that the receiving clinician shall correctly read within 15 seconds in ≥ 95% of validation trials, with 0 instances of an inherited silenced alarm or altered threshold going unnoticed. | Safety-critical | UR_16, UFMEA_12 |

## Concept

### UI/UX Design

Wireframes, interaction flows, navigation structures, and visual design principles that translate the user requirements into a tangible concept. The design below realises the MMSS user requirements (UR_*) and is shaped by the usability hazards in the Usability FMEA (UFMEA_*) and the measurable targets in the Usability Requirements (USR_*); the relevant IDs are cited inline so each design decision is traceable.

#### Design overview and screen map

MMSS presents a single, always-on **Monitoring Screen** as its home state — the screen a clinician sees throughout a live patient session. All other screens are reached from it without ever hiding the monitoring data when a live patient is connected. The navigation is deliberately shallow (one to two levels deep) so attention stays on the patient rather than on the device (UR_11).

```
                         ┌─────────────────────────────┐
                         │   STARTUP / INITIALISING    │  (USR_14, UFMEA_16)
                         └──────────────┬──────────────┘
                                        ▼
   ┌───────────────┐         ┌─────────────────────────────┐         ┌───────────────┐
   │  SIMULATION   │◀───────▶│      MONITORING SCREEN      │◀───────▶│ HAND-OVER VIEW│
   │     MODE      │  mode   │   (home / always-on live)   │ session │  (session     │
   │ (UFMEA_10/11) │  switch │                             │  state  │   summary)    │
   └───────────────┘         └───┬───────────┬──────────┬──┘         │ (USR_21)      │
                                 │           │          │            └───────────────┘
                                 ▼           ▼          ▼
                         ┌───────────┐ ┌──────────┐ ┌────────────────┐
                         │ DIAGNOSTIC│ │   HIS     │ │ CONFIGURATION  │
                         │  DETAIL   │ │  SHARING  │ │  / SETUP       │
                         │ (drill-in)│ │ (USR_18)  │ │ (engineer,     │
                         │           │ │           │ │  access-gated) │
                         └───────────┘ └──────────┘ └────────────────┘
```

The Configuration/Setup area is access-gated and intended for the Clinical/Biomedical Engineer (UR_14, UR_15); it is not reachable during normal bedside operation without authentication.

#### Main Monitoring Screen layout

The Monitoring Screen is divided into four persistent, spatially fixed zones whose **positions never change**, so a clinician builds a stable spatial mental model and can read any region by glance and muscle memory (UR_01, UR_02, UFMEA_18):

1. **Top — Alarm Banner + Mode/Status bar** (full width, highest priority).
2. **Left/centre — Measured Vital Signs zone** (the largest area; observed facts only).
3. **Right — Diagnostic Candidates zone** (inferred suggestions only, clearly walled off from measured data).
4. **Bottom — Status/context strip** (patient/session id, time, connectivity, silence state).

The measured zone and the inferred zone are **never interleaved** — measured values are never placed inside the candidate panel and candidates are never placed inside the vitals grid (UR_09, UFMEA_03, USR_08).

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│ ⛑ LIVE        ◤◤◤ ALARM: SpO₂ LOW 84%  ▸ HIGH PRIORITY ◢◢◢      [⏱ 14:22:07]      │ ← Alarm banner + Mode bar
├───────────────────────────────────────────────┬──────────────────────────────────┤
│  MEASURED VITAL SIGNS  (observed)             │  DIAGNOSTIC SUGGESTIONS          │
│                                               │  (AI decision support —          │
│  ┌─────────────┐ ┌─────────────┐ ┌──────────┐ │   not a diagnosis)               │
│  │ HEART RATE  │ │   SpO₂      │ │  RESP RR │ │ ──────────────────────────────── │
│  │   118       │ │ ⚠ 84  ◣low  │ │   24     │ │  · Sepsis            conf ●●●○  │
│  │   bpm  ↑    │ │  %    ░░░░   │ │  /min  ↑ │ │    basis: ↑HR ↑RR ↑Temp ↓SpO₂   │
│  │ src: ECG    │ │ src: SpO₂   │ │ src: CO₂ │ │  · Pneumonia        conf ●●○○  │
│  └─────────────┘ └─────────────┘ └──────────┘ │    basis: ↑RR ↓SpO₂ ↑Temp       │
│  ┌─────────────┐ ┌─────────────┐ ┌──────────┐ │  · PE               conf ●○○○ ◣ │
│  │ BP (NIBP)   │ │ EtCO₂       │ │  TEMP    │ │    basis: ↓SpO₂  [LOW CONFIDENCE]│
│  │ 86 / 52     │ │   31        │ │  38.9    │ │ ──────────────────────────────── │
│  │ MAP 63 mmHg │ │  mmHg       │ │  °C    ↑ │ │  Suggestions inform, they do     │
│  │ src: NIBP   │ │ src: CO₂    │ │ src:Temp │ │  not determine the diagnosis.    │
│  └─────────────┘ └─────────────┘ └──────────┘ │  [Updated 14:21:58] [Detail ▸]   │
│  ┌─────────────┐ ┌─────────────┐              │                                  │
│  │ PULSE RATE  │ │ BIS (EEG)   │              │                                  │
│  │ 116 bpm     │ │   42        │              │                                  │
│  │ src: SpO₂   │ │  src: EEG   │              │                                  │
│  └─────────────┘ └─────────────┘              │                                  │
├───────────────────────────────────────────────┴──────────────────────────────────┤
│ Patient: A. DOE (M, 54) │ Session 11:04→ │ ◼ 6/6 devices │ 🔇 none silenced │ HIS ✓│ ← Status strip
└──────────────────────────────────────────────────────────────────────────────────┘
```

**Measured Vital Signs zone.** One tile per enumerated parameter from the **Acquired Parameters / Signals** table — Heart Rate (ECG/IF_01), Systolic/Diastolic BP and MAP (NIBP/IF_03), SpO2 and Pulse Rate (Pulse Oximeter/IF_02), Respiratory Rate and EtCO2 (Capnometer/IF_05), Temperature (Thermal Probe/IF_04), and BIS (EEG/IF_06). Each tile shows **value, unit and source device** persistently (UR_02, USR_02), plus a small **trend arrow/sparkline** for direction and rate of change so gradual deterioration is visible before a threshold is crossed (UR_18). Values update on the 1 s UI timer and are confirmed displayed within 1 s of acquisition (USR_01). A subtle update animation (e.g. a value "tick") signals liveness; when that animation stops the parameter is no longer live (see staleness below).

**Diagnostic Candidates zone.** Candidates are rendered as a **peer set with equal visual weight** — no enlarged, highlighted, or "winner" rank-1 styling — under a persistent header "AI decision support — not a diagnosis" (UR_03, UR_17, USER_DFMEA_01/04, UFMEA_01, USR_09). Ordering still reflects ranking, but the visual language deliberately avoids implying an authoritative verdict. Each candidate carries, adjacent to it, its **confidence** (graded dot/segment encoding) and a one-line **basis** of the contributing parameters (UR_08, UFMEA_02, USR_10). Low-confidence candidates are additionally tagged with an explicit `[LOW CONFIDENCE]` flag and visibly de-emphasised, so they read as weak **before** they can be acted upon (USER_DFMEA_02, USR_10). `[Detail ▸]` opens the Diagnostic Detail drill-in (basis breakdown, history, time-stamps) without leaving the live context.

#### Alarm presentation and noticeability

The **Alarm Banner** spans the full top width and is the screen's highest-saliency element; an active alarm overrides non-critical content there (UFMEA_04). Alarms are encoded on three independent channels so they survive noisy, vibrating, low-light conditions (UR_05, UR_16, USR_03):

- **Priority by colour + motion + tone family.** High-priority physiological alarms use a saturated red banner with motion (pulsing chevrons) and a distinct, escalating audible pattern; medium priority uses amber. Colour is never the sole cue (it is paired with text, icon and tone) for accessibility (see Visual principles).
- **Source named in-place.** The banner names the alarming parameter and condition (e.g. "SpO₂ LOW 84%") and the corresponding **vital tile is highlighted in place**, so the clinician knows at a glance *which* parameter and *which* priority/type is alarming and does not silence the wrong one (UR_16, UFMEA_05, USR_03, USR_04).
- **Connection/misplacement (data-validity) faults have a reserved signature** — a dedicated icon, colour, and tone family used **exclusively** for data-validity faults, so they are never confused with physiological alarms (UR_06, UFMEA_06, USR_05). The affected tile is badged with a "no/!signal" marker.

```
PHYSIOLOGICAL ALARM (red, pulsing):   ◤◤◤ ALARM: SpO₂ LOW 84%  ▸ HIGH PRIORITY ◢◢◢   ♪ escalating
DATA-VALIDITY FAULT  (cyan, distinct): ⚇⚇  FAULT: NIBP DISCONNECTED — reading invalid    ♪ fault tone
```

**Alarm silencing** is time-bounded and source-specific only — there is no indefinite global mute. A silenced alarm shows a persistent "🔇 silenced — re-annunciates in mm:ss" indicator in the status strip and on the affected tile; an unresolved critical alarm auto-re-annunciates after its timeout and escalates if repeatedly silenced (UR_16, UFMEA_19, USR_17). This directly counters reflexive over-silencing and alarm fatigue.

**Stale-data indication.** On signal loss MMSS **invalidates** the affected parameter within 1 s rather than freezing the last value: the tile is greyed/struck, the update animation stops, and a "NO SIGNAL / stale" overlay appears, so a last-known value can never read as live (UR_06, USER_DFMEA_08, UFMEA_07, USR_06).

**Signal-quality / motion-artifact indication.** Every tile carries an always-visible **signal-quality indicator**; when a value is artifact-suspect (e.g. motion-corrupted SpO₂ or ECG in a moving vehicle) the value is visibly degraded (dimmed + quality icon) so plausible-but-false readings cannot read as clean physiological data (UR_02, UR_06, USER_DFMEA_18, UFMEA_08, USR_07).

```
 Clean:     [ HEART RATE  118 bpm ↑  ▮▮▮▮ quality good ]
 Artifact:  [ HEART RATE  ~118 bpm   ▮▯▯▯ ⚠ low quality ]   ← dimmed value + quality icon
 No signal: [ HEART RATE   ---  ░░ NO SIGNAL / STALE   ]   ← invalidated, animation stopped
```

#### Live vs Simulation mode indication

Mode is communicated by a **persistent, unmistakable, non-dismissable full-screen signature** so the clinician's mental model of system state cannot drift (UR_12, USER_DFMEA_10/11, UFMEA_10/11, USR_13):

- **Live mode** is the visually dominant default: neutral clinical theme, a persistent green `⛑ LIVE` chip at top-left, no watermark. Its presence is *affirmative* — live is never merely "the absence of a simulation cue" — so live data is never dismissed as practice (UFMEA_11).
- **Simulation/training mode** applies a distinct colour theme, a thick patterned screen border, a persistent diagonal `SIMULATION — NOT A LIVE PATIENT` watermark across the monitoring area, and a `▶ SIMULATION` mode chip. The watermark and border cannot be dismissed while in the mode.

Entering or leaving simulation requires an **explicit live-vs-simulation confirmation dialog** ("You are entering SIMULATION. No real patient is being monitored."), guarding against accidental entry (UFMEA_10). Target mode-recognition is within 1 s with zero mode-confusion errors (USR_13).

```
LIVE:        ┌ ⛑ LIVE ─────────────────────────────────┐      SIMULATION: ╔════════════════════════════════╗
             │  (neutral theme, no watermark)          │                 ║▶ SIMULATION  ╲  NOT A LIVE   ║
             └─────────────────────────────────────────┘                 ║  (amber theme) ╲ PATIENT ╲   ║
                                                                          ╚════════════════════════════════╝
```

#### Diagnostic timeout / unavailable notification

When the diagnostic capability does not return a result within the expected window, the candidate panel does not sit silently "pending". MMSS raises an **explicit audible + visual notification** and replaces the panel body with a persistent, unmistakable banner: **"Diagnosis unavailable — use clinical judgement"** (UR_07, USER_DFMEA_09, UFMEA_09, USR_12). The clinician is thereby cued to fall back without losing time.

If a result later arrives **after** a timeout fallback, the returning candidates appear **non-intrusively** (no modal interrupt, no auto-focus), clearly time-stamped and flagged as "arriving after fallback", so they support rather than override a treatment decision already underway (UFMEA_20).

```
┌ DIAGNOSTIC SUGGESTIONS ───────────────────┐        ┌ DIAGNOSTIC SUGGESTIONS ───────────────────┐
│                                           │        │ ⚠ Diagnosis UNAVAILABLE                   │
│   …acquiring…  (within expected window)   │  ──▶   │   Use clinical judgement.                 │
│                                           │ timeout│   Support did not converge in time.       │
└───────────────────────────────────────────┘   ♪    └───────────────────────────────────────────┘
```

#### Startup / initialising state

On activation MMSS shows an explicit **INITIALISING** screen and reaches a clearly indicated monitoring-ready state within 10 s (UR_10, USR_14). Until each parameter is acquired, its tile shows a distinct **"acquiring…" placeholder** that is visually unmistakable from a normal value — empty/blank fields are never shown for not-yet-live parameters, so a partially-started display can never read as complete, normal monitoring (USER_DFMEA_14, UFMEA_16, USR_14). A "System ready" confirmation marks the transition.

```
┌ INITIALISING MMSS … ───────────────────────────────────────────┐
│  ECG ▣ acquiring   SpO₂ ▣ acquiring   NIBP ◻ waiting            │
│  CO₂ ◻ waiting     Temp ▣ acquiring   EEG  ◻ waiting            │
│  ── parameters not yet live are marked; do not rely on display ──│
│                         [ ● System ready in ~6 s ]              │
└─────────────────────────────────────────────────────────────────┘
```

#### Configuration / setup screens (engineer)

The Configuration area is **access-gated**: the engineer authenticates before any safety-critical parameter can be changed, and every change is written to a traceable, access-controlled log (UR_14, UR_15, USER_DFMEA_13). Three guarded workflows:

- **Device interface & mapping** — a structured per-channel UI (IF_01–IF_06) with input validation, an explicit **device→parameter readback-and-confirm** step, and a visual map the engineer must verify before commit, so a wrong device-to-parameter mapping cannot be silently committed (USER_DFMEA_12, UFMEA_14, USR_19).
- **Alarm thresholds** — entered with **bounded controls (steppers/sliders) limited to safe ranges**, with out-of-range warnings and a change-confirmation summary before commit; out-of-safe-range values cannot be committed (USER_DFMEA_13, UFMEA_15, USR_20).
- **HIS integration** — configures the HL7/FHIR endpoint and credentials used for second-opinion sharing (UR_13, UR_14).

```
┌ CONFIG ▸ Device Mapping  (engineer — signed in as BME-204)  🔒 logged ─────────────┐
│ Channel  Interface  Device              → Parameter(s)            Validate         │
│  1       IF_01      ECG Monitor         → Heart Rate              ✓ ok             │
│  3       IF_03      NIBP Monitor        → Sys / Dia / MAP         ✓ ok             │
│  5       IF_05      Capnometer          → Resp Rate / EtCO₂       ✓ ok             │
│  ──────────────────────────────────────────────────────────────────────────────  │
│  Readback: confirm the map above reflects the physical wiring.   [ Confirm & Commit]│
└─────────────────────────────────────────────────────────────────────────────────┘
```

#### HIS second-opinion sharing flow

Sharing is a guarded, two-step confirm flow (UR_13, USER_DFMEA_16, UFMEA_13, USR_18). The physician selects the vital signs and ranked candidates to share, then MMSS presents a **readback summary — patient identity plus the exact items being sent** — that must be affirmed before the transmit control is enabled, so the wrong patient/content can never be transmitted.

```
Select items ──▶  ┌ CONFIRM SHARE TO HIS ─────────────────────┐ ──▶ Transmit (≤1s)
                  │ Patient:  A. DOE (M, 54)  — ID 0099-A      │
                  │ Sending:  9 vital signs + 3 candidates     │
                  │ ⚠ Verify this is the correct patient.      │
                  │            [ Cancel ]   [ Confirm & Send ] │  (Send disabled until confirmed)
                  └────────────────────────────────────────────┘
```

#### Care hand-over session-state summary

At a crew change or ED/ICU hand-off, MMSS surfaces a dedicated, persistent **Hand-over View** without interrupting live monitoring (UR_16, USER_DFMEA_17, UFMEA_12, USR_21). It summarises the otherwise-invisible session state — **silenced alarms with remaining silence time, any non-default alarm thresholds, and diagnostic candidates already reviewed/dismissed** — and requires the **incoming clinician's explicit acknowledgement** before monitoring continues, so no silenced alarm, altered threshold, or prior candidate decision is carried across unseen.

```
┌ HAND-OVER — confirm before taking the session ────────────────────────────┐
│ 🔇 Silenced alarms:   SpO₂ low  (re-annunciates in 01:12)                  │
│ ⚙ Non-default thresholds:  HR high 140→160 (changed 11:48 by NUR-7)        │
│ 🧠 Candidates dismissed:    "PE" dismissed 12:03                            │
│ ───────────────────────────────────────────────────────────────────────── │
│   Incoming clinician must acknowledge:   [ I have reviewed session state ✓ ]│
└────────────────────────────────────────────────────────────────────────────┘
```

#### Navigation & interaction model (bedside and moving-vehicle use)

The interaction model is tuned for divided attention under motion (UR_11, USER_DFMEA_15, UFMEA_17):

- **Large, well-spaced touch targets** of at least 9 mm, sized and spaced for in-motion use, keeping the mis-tap rate under 1% under simulated vehicle motion (USR_15).
- **Confirmation on every consequential or destructive action** (mode change, alarm silence beyond a tap, commit of config, HIS send), and safety-critical controls guarded against accidental activation (UFMEA_17, USR_15).
- **Shallow navigation** — the monitoring screen is home; drill-ins (Diagnostic Detail, Hand-over, Sharing) overlay or sit one level deep and always offer a single, obvious return to monitoring. The vitals and alarm zones remain visible or one glance away at all times.
- **Glanceable, low-step workflows** so a trained clinician completes core monitoring, alarm-response and diagnostic-review tasks unaided after ≤ 30 min training (USR_16).

#### Visual design principles and accessibility

- **Spatial hierarchy & stable layout.** Alarm > measured vitals > inferred candidates > status, in fixed positions, so the eye is drawn first to safety-critical information and the layout is learnable (UR_01, UFMEA_18).
- **Measured-vs-inferred visual language.** The measured zone and the inferred zone use deliberately **different typography, borders, and iconography** in addition to spatial separation, reinforcing the observed-vs-inferred distinction beyond position alone (UR_09, UFMEA_03, USR_08).
- **Safety colour use, never colour-alone.** Red = high-priority physiological alarm, amber = medium, a reserved distinct hue (e.g. cyan) = data-validity fault, green = live/normal. Every colour cue is **redundantly paired** with text, icon, shape and (for alarms) tone, so the encoding is robust for colour-vision-deficient users and in poor lighting (UR_05, UR_06, UR_16).
- **Legibility & typography.** Minimum character height and a luminance contrast ratio of **≥ 4.5:1** against background for all values, units, sources and alarm text, validated at ≤ 1 m viewing distance under simulated motion (UR_02, UFMEA_18, USR_02).
- **Multi-modal alarms.** Audible + high-contrast visual (+ optional tactile) so alarms are perceivable in ≥ 80 dB(A) ambient noise and under motion (UR_05, UFMEA_04, USR_03).
- **Plain, decision-support language.** Diagnostic output uses suggestion-framed, non-imperative wording throughout, reinforcing clinician accountability and never implying the system "decides" (UR_17, USER_DFMEA_04, USR_09).

### Actors

Individuals, groups, or systems that perform roles or tasks within the system or process.

| Actor | Description |
|-------|-------------|
| Bedside Clinician | Trained, registered critical-care (ICU) nurse who operates MMSS at the patient bedside — continuous vital-signs watch, trend monitoring, sensor placement, alarm response, and review of ranked diagnostic candidates as decision support. Primary human actor for continuous monitoring, alarming, and hand-over. |
| Emergency Physician | Trained, licensed ER physician who uses MMSS to obtain real-time vital signs plus AI-driven ranked diagnostic candidates within two minutes of patient connection, makes time-critical triage/treatment decisions, handles diagnostic-timeout fallback, and shares cases to the HIS for a second opinion. |
| Pre-hospital Clinician | Trained paramedic operating MMSS in a mobile medical unit or at the pre-hospital scene, often single-handed in noisy, moving conditions. Activates the system, applies sensors, monitors continuously, responds to vital-sign and connection/misplacement alarms, and uses early diagnostic support en route to definitive care. |
| Clinical / Biomedical Engineer | Trained biomedical/clinical engineering technician who commissions, configures, and maintains MMSS in a service context — device interfaces and mappings, alarm thresholds, and HIS integration — under access-controlled, traceably logged conditions, before clinical release. |
| Clinical Trainer | Clinician or designated educator who delivers hands-on and simulation-based training, operating MMSS in the separated simulation/training mode in a controlled, non-patient environment to build correct-use competence in interpreting ranked candidates and handling alarms. |
| Measurement Devices | The defined set of non-invasive measurement devices (ECG monitor, pulse oximeter, BP/NIBP monitor, thermal probe, capnometer, EEG monitor) that supply the enumerated vital-sign parameters (Acquired Parameters / Signals table) to MMSS across the device acquisition interfaces (IF_01–IF_06) and signal disconnection / loss-of-valid-signal. External non-human actor. |
| Monitor Display | The existing connected display (IF_07) on which MMSS renders vital signs, clinical alarms, and ranked diagnostic candidates. External non-human actor that presents output to the human clinicians. |
| AI Diagnostic Capability | The external, commercially validated off-the-shelf Open Evidence diagnostic capability (IF_08) that returns structured, ranked diagnostic candidates from submitted vital-signs data and signals timeout/unavailability. External non-human actor. |
| Hospital Information System (HIS) | The external hospital information system (IF_09, HL7/FHIR) to which MMSS shares vital signs and ranked diagnostic candidates for a second opinion. External non-human actor. |

### Use Cases (UC_*)

_To be added_

| ID | Title | Actor | Goal | Satisfies | Classification | Precondition | Main Success Scenario | Alternative Scenarios | Exception Scenarios | Post Condition | Traces |
|----|-------|-------|------|-----------|----------------|--------------|-----------------------|-----------------------|---------------------|----------------|--------|
| UC_01 | Start up MMSS and self-check | Pre-hospital Clinician | Bring MMSS to a ready-for-monitoring state quickly and know unambiguously when it is ready. | UR_10 | Standard | Host platform powered; MMSS installed and configured. | 1. Clinician powers on the portable monitor. 2. MMSS runs its startup self-check on the host platform (IF_10). 3. MMSS shows an explicit initialising state, marking not-yet-live parameters distinctly. 4. On reaching ready, MMSS confirms a clearly indicated monitoring-ready state within the activation budget. | Configuration loaded from a prior session restores device mappings and thresholds before ready. | Self-check fails or a required configuration is missing → MMSS shows a fault/not-ready state and does not present a normal monitoring picture. | MMSS is in a clearly indicated ready (or explicit not-ready) state; no empty field reads as a normal value. | UT_01, UR_10 |
| UC_02 | Acquire and display vital signs | Bedside Clinician | Keep continuous, real-time, legible at-a-glance awareness of each enumerated vital-sign parameter. | UR_01, UR_02, UR_18 | Safety-related | MMSS ready; measurement devices applied to the patient and connected (IF_01–IF_06). | 1. Measurement Devices stream the enumerated parameters (Acquired Parameters / Signals table) to MMSS. 2. MMSS acquires, processes, and renders each parameter with value, unit, and source on the Monitor Display (IF_07) within the display budget. 3. MMSS updates values on the timer-based UI interval. 4. MMSS shows the recent trend (direction and rate of change) of each parameter. | Subset of devices connected → only the available parameters are shown live, the rest marked not-yet-live. | A device signal is artifact-degraded → the affected parameter is shown with a signal-quality/validity indication rather than as a clean reading. | Current vital signs and their trends are continuously and legibly displayed. | UT_03, UT_06, UT_07, UR_01, UR_02, UR_18 |
| UC_03 | Generate and display ranked diagnostic candidates | Emergency Physician | Obtain AI-derived ranked diagnostic candidates, with basis and confidence, framed as decision support, to support faster triage and treatment. | UR_03, UR_04, UR_08, UR_09, UR_17 | Safety-critical | MMSS acquiring valid vital signs; AI Diagnostic Capability interface available (IF_08). | 1. MMSS submits prepared vital-signs data to the AI Diagnostic Capability. 2. The capability returns structured, ranked diagnostic candidates with supporting basis/confidence. 3. MMSS renders the candidates promptly in the inferred zone, walled off from measured data, each with basis and graded confidence. 4. MMSS frames the output persistently as decision support that informs, not determines, the diagnosis. | Updated candidates arrive during a session → MMSS refreshes the ranked list and timestamps it. | No valid vital-signs data available to submit → MMSS withholds candidates and indicates diagnostic input is incomplete. | Ranked diagnostic candidates are displayed as clearly-framed decision support, separated from measured data. | UT_04, UT_09, UT_16, UR_03, UR_04, UR_08, UR_09, UR_17 |
| UC_04 | Raise vital-sign alarm | Bedside Clinician | Be alerted, in time and unambiguously, when any vital-sign parameter crosses its abnormal-condition threshold. | UR_05, UR_16 | Safety-critical | MMSS monitoring live vital signs; alarm thresholds configured. | 1. MMSS detects an enumerated parameter crossing its abnormal-condition threshold. 2. MMSS raises a timely, distinctive, priority- and type-differentiated audible and visual alarm, naming the source parameter. 3. The alarm persists until acknowledged. 4. The clinician recognises the source and intervenes. | Multiple simultaneous alarms → MMSS presents them prioritised by clinical severity. | Clinician silences the alarm → only time-bounded, source-specific silence is permitted, with a persistent "silenced" indication and auto re-annunciation if unresolved. | The abnormal condition is annunciated and either acknowledged/acted on or re-annunciated. | UT_10, UR_05, UR_16 |
| UC_05 | Detect and alarm sensor disconnection / misplacement | Pre-hospital Clinician | Never unknowingly act on missing or invalid data when a sensor is disconnected, misplaced, or loses a valid signal. | UR_06, UR_16 | Safety-critical | MMSS monitoring at least one connected measurement device. | 1. A Measurement Device is disconnected, misplaced, or stops providing a valid signal (detected by the device and/or by loss of valid input on IF_01–IF_06). 2. MMSS raises a clearly differentiated connection/misplacement audible and visual alarm, distinct from vital-sign alarms. 3. MMSS visibly flags the affected parameter as stale/invalid rather than showing the last value as current. 4. The clinician reseats/replaces the sensor; MMSS confirms valid acquisition and clears the fault. | Signal restored before acknowledgement → fault state auto-clears once valid acquisition is confirmed. | Device cannot re-establish a valid signal → the parameter remains flagged invalid and the fault alarm persists. | The data-validity fault is annunciated and the affected parameter is unmistakably marked invalid until restored. | UT_11, UT_12, UT_13, UR_06, UR_16 |
| UC_06 | Notify diagnostic timeout / unavailable | Emergency Physician | Be told explicitly when diagnostic support is unavailable or overdue, so as to fall back on clinical judgement without losing time. | UR_07, UR_17 | Safety-critical | A diagnostic request is in progress against the AI Diagnostic Capability (IF_08). | 1. The expected time elapses without a diagnostic result (AI Diagnostic Capability signals timeout/unavailable, or no result within the budget). 2. MMSS notifies the physician explicitly with audible and visual cues. 3. MMSS shows a persistent "diagnosis unavailable — use clinical judgement" state. 4. The physician proceeds on vital signs and clinical judgement, retaining accountability. | A late result later arrives → presented non-intrusively as supplementary, timestamped input (UC_03) without overriding the decision in progress. | AI Diagnostic Capability interface is unreachable from the outset → MMSS indicates diagnostic support unavailable rather than waiting silently. | The clinician is explicitly aware diagnostic support is unavailable/overdue and has fallen back to clinical judgement. | UT_14, UT_15, UT_16, UR_07, UR_17 |
| UC_07 | Run simulation / training mode | Clinical Trainer | Build correct-use competence in a safe simulated mode that cannot be confused with live patient use. | UR_12, UR_03 | Safety-related | MMSS not connected to a live patient session; trainer authorised to enter training mode. | 1. The trainer deliberately enters the separated simulation/training mode. 2. MMSS makes the mode unmistakably and persistently distinct (banner, colour, watermark) and guards against accidental entry. 3. The trainer plays a realistic scenario; MMSS reproduces vital-sign behaviour and ranked candidates. 4. The trainer demonstrates correct candidate interpretation and alarm handling. 5. On exit, MMSS affirmatively returns to the visually dominant live state. | Multiple scenarios run in sequence within one training session. | Accidental attempt to enter simulation during a live session → blocked with a live-vs-simulation confirmation. | Training completed in an unmistakably simulated session; MMSS returned to an affirmatively-indicated live state. | UT_17, UT_18, UT_19, UT_20, UR_12, UR_03 |
| UC_08 | Share data to HIS for second opinion | Emergency Physician | Share the correct patient's vital signs and ranked candidates with the HIS for a timely expert second opinion. | UR_13 | Essential | HIS integration configured (IF_09); a case with vital signs and candidates available. | 1. The physician selects the relevant vital signs and ranked diagnostic candidates to share. 2. MMSS requires a two-step patient/case confirmation with a readback of exactly what will be shared. 3. On confirmation, MMSS transmits the selected data to the HIS promptly. 4. The case is available in the HIS for an expert second opinion. | Physician edits the selection before confirming → readback updates to match. | HIS unreachable or transmission fails → MMSS reports the failure and does not falsely indicate the case was shared; patient confirmation must precede any retry. | The correct patient case is transmitted to the HIS, or the failure is clearly reported with nothing wrongly shared. | UT_21, UT_22, UT_23, UR_13 |
| UC_09 | Configure devices and alarm thresholds | Clinical / Biomedical Engineer | Commission MMSS for the care environment — device interfaces, mappings, and alarm thresholds — correctly and safely. | UR_14, UR_15 | Safety-related | Engineer authenticated to the access-gated configuration interface; MMSS not in live clinical use. | 1. The engineer authenticates to the controlled configuration interface (access enforced). 2. The engineer configures each device interface (IF_01–IF_06) and its device-to-parameter mapping; MMSS validates and reads back the mapping. 3. The engineer sets vital-sign alarm thresholds; MMSS constrains entry to safe ranges and requires confirmation. 4. MMSS records every change in a traceable, access-controlled log and confirms safe setup before clinical release. | Editing an existing configuration → prior values shown and changes diffed before commit. | Out-of-range threshold or invalid mapping entered → rejected with an out-of-range/validation warning; not committed. | MMSS is correctly and safely configured, with all changes logged, and released for clinical use. | UT_24, UT_25, UT_26, UT_28, UR_14, UR_15 |
| UC_10 | Configure HIS integration | Clinical / Biomedical Engineer | Set up the HIS integration so second-opinion sharing works correctly and securely. | UR_14, UR_13 | Safety-related | Engineer authenticated to the configuration interface; HIS endpoint/protocol details available. | 1. The engineer authenticates to the controlled configuration interface. 2. The engineer configures the HIS integration settings (HL7/FHIR, IF_09). 3. MMSS validates the settings and reads them back for confirmation. 4. MMSS logs the change traceably and confirms the integration is ready for clinical use. | Connectivity test run as part of setup before commit. | HIS settings invalid or endpoint unreachable on test → flagged; integration not marked ready until corrected. | HIS integration is configured, validated, and logged, ready for second-opinion sharing. | UT_27, UT_24, UR_14, UR_13 |
| UC_11 | Hand over active session at shift change | Bedside Clinician | Transfer a running session at a crew/shift change without silenced alarms, altered thresholds, or dismissed candidates being carried across unseen. | UR_16, UR_05 | Safety-critical | A live monitoring session is in progress; an incoming clinician is taking over. | 1. At hand-over MMSS surfaces the current alarm/silence state, any non-default alarm thresholds, and which diagnostic candidates were reviewed/dismissed. 2. The incoming clinician reviews the session-state summary. 3. The incoming clinician explicitly acknowledges the session state. 4. Monitoring continues with no carried-over state hidden. | Hand-over occurs mid-transport (pre-hospital crew change) → same session-state summary surfaced for the receiving pre-hospital clinician. | Incoming clinician does not acknowledge → unacknowledged session state and any silenced alarm remain visibly flagged; alarm silences are time-limited and re-annunciate. | The incoming clinician has acknowledged the full session state; no silenced alarm, altered threshold, or prior candidate decision is hidden. | UT_30, UR_16, UR_05 |
| UC_12 | Verify signal quality before trusting readings | Pre-hospital Clinician | Ensure early treatment decisions rest on valid rather than artifactual or not-yet-live data. | UR_02, UR_06 | Safety-critical | MMSS acquiring vital signs, possibly under motion/low-perfusion conditions. | 1. Before acting, the clinician checks the per-parameter signal-quality/validity indication. 2. MMSS displays a signal-quality indicator per parameter and visibly degrades artifact-suspect or low-quality values. 3. The clinician waits for or corrects any low-quality, motion-corrupted, or not-yet-live parameter (e.g. reseats SpO₂ probe, steadies the lead). 4. The clinician acts only on parameters confirmed valid. | Quality recovers on its own as motion settles → the indicator clears and the value renders as clean. | Quality cannot be recovered → the value stays visibly degraded and is not treated as a clean reading; falls back to UC_05 if the signal is lost. | Only valid, quality-confirmed readings are relied upon; artifact-suspect values remain visibly flagged. | UT_29, UR_02, UR_06 |
| UC_13 | Silence and re-annunciate an alarm safely | Bedside Clinician | Quiet a known or nuisance alarm momentarily to manage the patient without ever permanently suppressing a genuine, still-unresolved critical alarm. | UR_16, UR_05 | Safety-critical | MMSS monitoring live vital signs; one or more alarms active or recently active. | 1. An alarm is active and the clinician, already aware of the condition (or judging it a nuisance/known alarm), needs to silence it briefly to attend to the patient or reduce noise. 2. MMSS permits only a time-bounded, source-specific silence — not an indefinite or global mute — and shows a persistent "silenced — re-annunciates in mm:ss" indication on the affected parameter and in the status strip. 3. If the underlying condition is still unresolved when the silence period expires, MMSS automatically re-annunciates the alarm. 4. The clinician either resolves the condition or re-evaluates on re-annunciation. | The condition resolves while silenced → the alarm clears and the silenced indication is removed without re-annunciating a non-existent condition. | Clinician reflexively/repeatedly silences the same unresolved critical alarm → MMSS escalates (e.g. shortens the silence window, raises priority/audibility, or surfaces the persistent silenced state more prominently) rather than allowing habitual suppression; no critical alarm can be left permanently silenced. | No unresolved critical alarm remains silenced beyond its time limit; every still-active condition is re-annunciated or escalated, and the current silence state is always visible. | UT_10, UR_16, UR_05 |

### Design Decisions (DD_*)

Choices made during design, with the considered alternatives and the rationale for the final choice.

| ID | Decision | Alternatives | Rationale | Traces |
|----|----------|--------------|-----------|--------|
| DD_01 | Source the diagnostic capability from the commercially validated, off-the-shelf Open Evidence AI library, integrated as a black-box component, rather than developing a custom diagnostic model for the first release. | (a) Develop a custom/in-house diagnostic AI model; (b) integrate a commercially validated off-the-shelf model (Open Evidence) as a black box; (c) hybrid — off-the-shelf for v1.0, custom later. | A custom model carries high validation complexity (R_02) and serious risk of regulatory-clearance delay (R_01), both of which threaten the competitive first-release window. An already-validated off-the-shelf capability is mandated by constraint and is the primary mitigation: MMSS inherits a clinically credible, pre-validated capability without owning its internal model-validation burden, materially lowering development/validation risk and protecting time-to-market, while leaving a later custom path open. | UC_03, BR_04, BR_08 |
| DD_02 | Treat Open Evidence as a black box reached only across a defined data interface that submits structured vital-signs data and receives structured ranked diagnostic candidates with basis and confidence — no coupling to its internal model. | (a) Deep integration coupled to the model internals; (b) black-box integration across a defined structured data interface; (c) loosely-coupled file/batch exchange. | Black-box integration at a stable, structured interface keeps MMSS independent of the capability's internals, makes supplier change-control and a second-source/exit contingency feasible, and contains the integration so MMSS does not inherit the model's validation burden. A structured ranked-candidate contract is also what lets MMSS render basis/confidence and frame the output as decision support. | UC_03, BR_04, BR_05 |
| DD_03 | Deliver MMSS as a software-only solution that accesses all fixed physical components (host CPU, six device types, monitor display) solely through their published interface control documents, undertaking no hardware design, selection, or modification. | (a) Co-design or modify hardware alongside software; (b) software-only against published ICDs with hardware treated as fixed/external; (c) abstract hardware behind an internally re-specified interface. | Confining scope to software reached only through published ICDs bounds the validated-configuration matrix, reduces development/validation effort and time-to-market risk, and matches the stated scope. The components' fixed behaviour becomes a precondition MMSS builds on rather than something it changes, keeping the supportability and liability envelope manageable. | UC_02, BR_06, BR_07 |
| DD_04 | Abstract the six measurement device types behind a single uniform internal acquisition interface (device abstraction layer), with per-device drivers/polling normalising each device's ICD into a common parameter model. | (a) Bespoke per-device handling threaded through the whole stack; (b) a uniform device-abstraction layer with per-device drivers below it; (c) a single generic driver assuming homogeneous devices. | A device-abstraction layer keeps the rest of MMSS independent of device specifics, bounds interoperability to the defined, validated device-type set, and confines per-device ICD differences to swappable drivers — reducing regression and post-market burden when devices vary, while still acquiring the enumerated parameters uniformly. | UC_02, UC_09, BR_07 |
| DD_05 | Allocate the 1-second end-to-end display latency budget across the internal processing chain so the boundary-observable display target is met (processing within its sub-budget, presentation within its sub-budget). | (a) No explicit allocation — best-effort end-to-end; (b) split the 1 s budget into processing and presentation sub-budgets within the system; (c) relax the display target. | The user-observable requirement is sub-second display after acquisition; meeting it predictably requires the end-to-end budget to be partitioned within the system so each stage has a verifiable share. Treating the 1 s as a boundary budget that the internal stages must sum to keeps the timing testable and the at-a-glance display dependable. | UC_02, UC_04 |
| DD_06 | Keep MMSS's safety-critical alarming and diagnostic-timeout functions backed by independent external systems (devices raise their own audible connection alarms; the diagnosis algorithm signals independently on timeout), so no single MMSS software fault is the sole cause of a fatal outcome. | (a) MMSS as sole annunciator for all alarms and timeouts (no independent backup); (b) MMSS alarming/diagnosis mitigated by independent external systems serving the same hazards. | This independence is the architectural risk-control that reduces the residual software safety class from C to B: because non-software systems cover the same hazards, an MMSS software failure is no longer the sole cause of serious or fatal harm. It directly mitigates undetected connection failure (R_07) and uncommunicated diagnostic timeout (R_06). | UC_05, UC_06, BR_02 |
| DD_07 | Provide a persistent, unmistakable separation between live patient mode and simulation/training mode, guarding against accidental entry and blocking simulation during a live session. | (a) A single mode with sample data loaded ad hoc; (b) a switchable mode with a subtle indicator; (c) a persistently and dominantly differentiated simulation mode that cannot be confused with live use. | The critical risk is clinicians misinterpreting AI candidates or acting on simulated data as if live (R_05). A mandatory, clearly separated training mode builds correct-use competence safely, and a persistent live/simulation distinction with accidental-entry guards prevents simulated data ever being mistaken for a real patient. | UC_07, BR_11 |
| DD_08 | Integrate with hospital information systems over a recognised health-data interoperability standard (HL7/FHIR), with the exact protocol and its interface control documents selected and defined early — before the share-path design is committed — given the ICDs are currently TBD. | (a) Bespoke point-to-point HIS integration; (b) standards-based HL7/FHIR integration with ICDs defined early; (c) defer HIS integration entirely. | Standards-based integration is a hard procurement gate (hospital IT will reject a device that cannot exchange over their established standards) and avoids bespoke silos. Because the protocol/ICDs are TBD, resolving them early is the dominant mitigation for the connectivity/real-time integration risk (R_03) and a precondition for designing the share path to its 1-second timing budget. | UC_08, UC_10, BR_12 |
| DD_09 | Provide diagnostic output strictly as human-in-the-loop decision support — ranked candidates with basis and confidence that inform, never autonomously determine, the diagnosis — with the clinician retaining accountability. | (a) Autonomous/automated diagnosis acted on without clinician judgement; (b) ranked candidates as advisory decision support that informs but does not determine; (c) hide candidates and surface only on request. | The decision-support function is the largest liability concentration; keeping a trained professional in the loop, with the candidates framed persistently as advisory, contains residual liability through validated-use boundaries and human control. It mirrors the intended use and is what makes the safety-critical output defensible. | UC_03, UC_06, BR_15 |
| DD_10 | Detect sensor disconnection and misplacement by combining device-reported fault status (from the ICDs) with MMSS-side loss-of-valid-input detection, and flag the affected parameter as stale/invalid rather than displaying a last value as current. | (a) Rely solely on the device to detect misplacement; (b) rely solely on MMSS loss-of-signal detection; (c) combine device-reported status with MMSS-side input-validity detection. | Sensor misplacement going undetected can drive a wrong diagnosis (R_04, Critical). Combining the device's own detection with MMSS-side validity checks gives defence in depth, and explicitly marking parameters stale/invalid (never showing a stale value as live) ensures clinicians never unknowingly act on missing or invalid data. | UC_05, UC_12, BR_07 |
| DD_11 | Provide per-parameter signal-quality/validity indication and visibly degrade artifact-suspect or not-yet-live values, so early treatment decisions rest on confirmed-valid rather than artifactual data. | (a) Show all acquired values uniformly with no quality indication; (b) per-parameter signal-quality indicators with visible degradation of low-quality/not-yet-live values. | In pre-hospital settings under motion/low-perfusion, raw values can mislead. Per-parameter quality indication lets the clinician trust only confirmed-valid readings and corrects or waits out degraded ones, reducing the risk of acting on artifactual data and reinforcing the misplacement defence. | UC_12, UC_02, BR_07 |
| DD_12 | Persist and surface safety-relevant session state (alarm/silence state, non-default thresholds, reviewed/dismissed candidates) across shift/crew hand-over, requiring explicit acknowledgement by the incoming clinician, and permit only time-bounded, source-specific alarm silencing with automatic re-annunciation and escalation. | (a) Stateless hand-over with no carried-state summary; allow indefinite/global mute; (b) explicit session-state hand-over with acknowledgement, and time-bounded source-specific silencing that auto-re-annunciates/escalates. | Silenced alarms, altered thresholds, or dismissed candidates carried across a hand-over unseen are a direct path to missed deterioration. Surfacing and acknowledging session state, and forbidding indefinite/global mute in favour of time-limited silencing with re-annunciation and escalation, ensures no unresolved critical alarm is ever permanently suppressed. | UC_11, UC_13, UC_04 |
| DD_13 | Gate the configuration/commissioning interface behind authentication and out-of-live-use enforcement, with safe-range constraint on threshold entry, mapping read-back, and a traceable access-controlled change log. | (a) Open, unauthenticated configuration editable during live use; (b) access-gated, out-of-live-use configuration with validation, read-back, and a traceable change log. | Device mappings and alarm thresholds are safety-relevant; allowing unconstrained or live-session edits risks unsafe setup. Access-gating, safe-range validation, mapping read-back, and a traceable log ensure commissioning is correct, safe, and auditable before clinical release, supporting the conformant lifecycle and supportability obligations. | UC_09, UC_10, BR_03 |
| DD_14 | Protect patient data on the second-opinion share path with a two-step patient/case confirmation and explicit read-back of exactly what will be shared, transmitting only over the secured standards-based HIS interface and never falsely indicating success on failure. | (a) One-click share with no patient confirmation; (b) two-step patient/case confirmation with read-back, secured transmission, and honest failure reporting. | Sharing the wrong patient's data, or believing a failed transmission succeeded, are serious privacy and safety failures. A two-step confirmation with read-back, secured standards-based transmission, and truthful failure reporting upholds data-protection duties and ensures nothing is wrongly shared or falsely reported as shared. | UC_08, BR_12, BR_17 |

---

# Development

## SOLUTION: Mobile Monitoring Software Solution (MMSS)

### External Interfaces

The points where the system connects to context elements, sub-systems, or other systems — connection type, data/signals exchanged, and protocols/standards.

The MMSS is treated as a black box at its external boundary. All connections are digital/logical software interfaces governed by published Interface Control Documents (ICDs); no physical or electrical interface is in MMSS scope (hardware is fixed and out of scope). The MMSS boundary comprises three classes of connection: **inbound device acquisition** (IF_01–IF_06), **outbound presentation** (IF_07), and **bidirectional service / integration / runtime** interfaces (IF_08–IF_10).

| IF | Connects to | Direction | Connection type | Data / signals exchanged | Protocol / standard (ICD) |
|----|-------------|-----------|-----------------|--------------------------|---------------------------|
| IF_01 | ECG Monitor | Inbound (acquire) | Digital device-driver / polling channel | Heart Rate; per-channel validity / sensor-fault & misplacement status | ICD_ECG |
| IF_02 | Pulse Oximeter | Inbound (acquire) | Digital device-driver / polling channel | SpO2, Pulse Rate; validity / sensor-fault & misplacement status | ICD_SpO2 |
| IF_03 | BP / NIBP Monitor | Inbound (acquire) | Digital device-driver / polling channel | Systolic BP, Diastolic BP, MAP; validity / sensor-fault status | ICD_NIBP |
| IF_04 | Thermal / Temperature Probe | Inbound (acquire) | Digital device-driver / polling channel | Temperature; validity / sensor-fault status | ICD_TEMP |
| IF_05 | Capnometer | Inbound (acquire) | Digital device-driver / polling channel | Respiratory Rate, EtCO2; validity / sensor-fault status | ICD_EtCO2 |
| IF_06 | EEG Monitor | Inbound (acquire) | Digital device-driver / polling channel | BIS (Bispectral Index); validity / sensor-fault & misplacement status | ICD_EEG |
| IF_07 | Monitor Display | Outbound (present) | Digital presentation / rendering channel | Vital-sign values (value/unit/source), trends, alarm states, diagnostic candidates, mode & status indications | ICD_DISPLAY |
| IF_08 | Open Evidence AI Diagnostic Capability | Bidirectional (exchange) | Digital service interface (off-the-shelf AI library/service) | Outbound: prepared vital-signs data set; Inbound: ranked structured diagnostic candidates | ICD_OPENEVIDENCE |
| IF_09 | Hospital Information System (HIS) | Outbound (share) | Digital integration interface | Vital-sign data and diagnostic candidates for second opinion | ICD_HIS (HL7/FHIR — TBD) |
| IF_10 | Host CPU Platform | Bidirectional (run on) | Host OS / runtime interface | Execution services, timing/clock, I/O scheduling on real-time-capable embedded OS | ICD_PLATFORM |

A black-box boundary diagram of the MMSS and these external interfaces:

_To be added_

### Requirements

The full set of requirements the system must satisfy, derived from the user requirements and constrained by the context, regulatory requirements, and design decisions. Requirements are SMART and form the basis for verification.

#### Interface Requirements (RQ_IF_*)

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_IF_01 | The MMSS shall acquire Heart Rate, together with its per-channel validity / sensor-fault and misplacement status, from the ECG Monitor across the ECG Acquisition Interface in accordance with ICD_ECG, at an input rate of at least 0.1 Hz. | Heart Rate is a safety-relevant vital sign and its validity / misplacement status is required to avoid presenting an invalid value as live; the device interface must conform to its published ICD. | Safety-critical | IF_01 |
| RQ_IF_02 | The MMSS shall acquire SpO2 and Pulse Rate, together with their validity / sensor-fault and misplacement status, from the Pulse Oximeter across the Pulse Oximeter Acquisition Interface in accordance with ICD_SpO2, at an input rate of at least 0.1 Hz. | Oxygenation and pulse are safety-relevant vitals; validity/misplacement status prevents a frozen or invalid reading being shown as current. | Safety-critical | IF_02 |
| RQ_IF_03 | The MMSS shall acquire Systolic BP, Diastolic BP and Mean Arterial Pressure (MAP), together with their validity / sensor-fault status, from the BP / NIBP Monitor across the BP / NIBP Acquisition Interface in accordance with ICD_NIBP, at an input rate of at least 0.1 Hz. | Blood-pressure parameters are safety-relevant and must be acquired with validity status over the conformant device interface. | Safety-critical | IF_03 |
| RQ_IF_04 | The MMSS shall acquire Temperature, together with its validity / sensor-fault status, from the Thermal / Temperature Probe across the Temperature Acquisition Interface in accordance with ICD_TEMP, at an input rate of at least 0.1 Hz. | Temperature is a monitored vital sign; the interface must conform to its published ICD and convey signal validity. | Safety-related | IF_04 |
| RQ_IF_05 | The MMSS shall acquire Respiratory Rate and EtCO2, together with their validity / sensor-fault status, from the Capnometer across the Capnometer Acquisition Interface in accordance with ICD_EtCO2, at an input rate of at least 0.1 Hz. | Respiratory rate and end-tidal CO2 are safety-relevant vitals; validity status prevents misreading invalid data. | Safety-critical | IF_05 |
| RQ_IF_06 | The MMSS shall acquire BIS (Bispectral Index), together with its validity / sensor-fault and misplacement status, from the EEG Monitor across the EEG Acquisition Interface in accordance with ICD_EEG, at an input rate of at least 0.1 Hz. | BIS supports depth-of-sedation monitoring; its validity / misplacement status must be conveyed over the conformant device interface. | Safety-related | IF_06 |
| RQ_IF_07 | The MMSS shall detect loss of a valid signal on any device acquisition interface (IF_01–IF_06) within 5 seconds, measured from the last successfully received valid sample/update on that interface, and flag the affected parameter's status accordingly across that interface's ICD. | Undetected connection failure or misplacement can lead to a missed vital sign or a wrong diagnosis (R_04, R_07). The 5-second budget is measured from the timestamp of the last valid sample to the moment the status flag is set, and is boundary-observable. Because the guaranteed input rate is ≥ 0.1 Hz (one sample per 10 s), the 5-second inactivity window must be interpreted against each interface's actual nominal cadence per its ICD, not a fixed 5 s poll. | Safety-critical | IF_01, IF_02, IF_03, IF_04, IF_05, IF_06 |
| RQ_IF_08 | The MMSS shall present each acquired vital-sign parameter (value, unit and source), its trend and its validity/alarm state on the Monitor Display across the Display / Presentation Interface in accordance with ICD_DISPLAY, within 1 second measured from receipt of the sample at the device acquisition interface boundary to its appearance on the display. | Clinicians require real-time at-a-glance vitals; the 1-second end-to-end display latency is the boundary-observable budget the user experiences. The 1 second is the roll-up of the internal acquisition-to-render budget (the input's DPREC ≤ 800 ms + DPROC ≤ 200 ms decomposition is an internal allocation and is verified at this 1-second black-box boundary, not separately). | Safety-critical | IF_07 |
| RQ_IF_09 | The MMSS shall present the ranked diagnostic candidates received from the Open Evidence AI Diagnostic Capability on the Monitor Display across the Display / Presentation Interface in accordance with ICD_DISPLAY, within 1 second of receipt. | Diagnostic decision support must be rendered promptly after the AI capability returns candidates; the 1-second budget is observable at the display boundary. | Safety-related | IF_07 |
| RQ_IF_10 | The MMSS shall present vital-sign alarm and connection / misplacement alarm states on the Monitor Display across the Display / Presentation Interface in accordance with ICD_DISPLAY, within 1 second of the corresponding detection. | Timely alarm presentation is required for intervention before deterioration; the 1-second budget is boundary-observable at the display. | Safety-critical | IF_07 |
| RQ_IF_11 | The MMSS shall send the prepared vital-signs data set to, and receive ranked structured diagnostic candidates from, the Open Evidence AI Diagnostic Capability across the AI Diagnostic Capability Interface in accordance with ICD_OPENEVIDENCE, and shall not impose any internal time bound on the AI capability's own response. | Diagnostic support depends on a conformant, structured exchange with the off-the-shelf AI capability (R_03); the interface must conform to its published ICD. The AI capability's response/convergence time (the 2-minute ALGOS budget) is external and outside MMSS control — MMSS only owns the request preparation and the bounded handling of the returned or timed-out result; absent or malformed candidates must be detectable at this interface for the timeout/unavailable handling (RQ_FN_12) to trigger. | Safety-related | IF_08 |
| RQ_IF_12 | The MMSS shall share vital-sign data and diagnostic candidates with the Hospital Information System across the HIS Integration Interface in accordance with ICD_HIS (HL7/FHIR, to be confirmed), emitting the transmission onto the HIS interface within 1 second of the clinician's sharing confirmation. | Second-opinion sharing requires a conformant HIS integration; the 1-second budget is measured from the clinician's confirmation to the message being handed to the HIS interface (it covers MMSS-side preparation and emission, not HIS-side acknowledgement or network transit, which depend on the external system). The HIS protocol/ICD (HL7/FHIR) is still to be defined (R_03), so the exact message encoding is a TBD dependency for implementation. | Standard | IF_09 |
| RQ_IF_13 | The MMSS shall execute on the Host CPU Platform across the Host Platform / OS Interface in accordance with ICD_PLATFORM, using only the runtime, timing and I/O services published by the real-time-capable embedded host operating system. | The host platform is a fixed, out-of-scope element; MMSS must interface only through published OS runtime services to meet its timing budgets. | Standard | IF_10 |
| RQ_IF_14 | The MMSS shall complete system activation and present the initialised monitoring state on the Monitor Display across the Display / Presentation Interface in accordance with ICD_DISPLAY within 10 seconds, measured from MMSS process start (application launch on the host OS) to the initialised state being rendered. | A bounded, boundary-observable activation time is required so the clinician has live monitoring quickly after power-on. The 10-second budget is measured from MMSS start (not host hardware/OS boot, which is out of scope) to the ready/not-ready state appearing on the display. | Safety-related | IF_07 |

#### Functional Requirements (RQ_FN_*)

What the system must do — its functions, features, and behaviors. Each traces back to a use case or user requirement.

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_FN_01 | The MMSS shall, on start-up, perform a self-check of its acquisition, presentation and alarm functions and present an explicit initialising-then-ready (or not-ready/fault) state on the Monitor Display, marking any not-yet-live parameter distinctly so that no empty field reads as a normal value, and shall not present a normal monitoring picture if the self-check fails. | A bounded, unambiguous ready/not-ready indication after activation ensures the clinician knows when monitoring is live and never mistakes an unstarted parameter for a valid reading. | Safety-related | UC_01, UR_10 |
| RQ_FN_02 | The MMSS shall acquire each enumerated vital-sign parameter (Heart Rate, SpO2, Pulse Rate, Systolic BP, Diastolic BP, MAP, Respiratory Rate, EtCO2, Temperature, BIS — per the Acquired Parameters / Signals table) from its connected measurement device and continuously display each parameter in real time with its value, unit and source on the Monitor Display, updating on the timer-based 1-second UI interval. | Continuous, legible, at-a-glance display of every enumerated vital sign is the core monitoring function clinicians depend on. | Safety-related | UC_02, UR_01, UR_02 |
| RQ_FN_03 | The MMSS shall display, for each enumerated vital-sign parameter, its recent trend (direction and rate of change over time) in addition to its instantaneous value. | Showing the trend lets clinicians recognise gradual deterioration early and intervene before an alarm threshold is crossed. | Safety-related | UC_02, UR_18 |
| RQ_FN_04 | The MMSS shall submit the prepared vital-signs data set to the Open Evidence AI Diagnostic Capability and present the ranked diagnostic candidates it returns as an ordered list on the Monitor Display, ordered by the AI-supplied ranking, each candidate shown with its supporting basis and graded confidence/uncertainty as supplied by the AI capability, within 1 second of receipt of the candidates from the AI capability. | Ranked candidates with basis and confidence, rendered promptly, support faster, better-informed triage while letting the clinician judge how far to trust each candidate. The 1-second budget is measured from receipt of the candidate set at the AI interface to its appearance on the display and covers only MMSS rendering; the AI's own response time is external (RQ_IF_11). The ranking, basis text and confidence/uncertainty grading are taken from the AI's structured output — MMSS renders and does not re-compute them. | Safety-critical | UC_03, UR_03, UR_04, UR_08 |
| RQ_FN_05 | The MMSS shall withhold diagnostic candidates and indicate that diagnostic input is incomplete whenever no valid vital-signs data is available to submit to the AI Diagnostic Capability. | Presenting candidates derived from absent or invalid input would be misleading; the clinician must be told the input is incomplete rather than shown an unsupported result. | Safety-critical | UC_03, UR_07 |
| RQ_FN_06 | The MMSS shall visually separate measured (observed) vital-sign data from AI-inferred diagnostic candidates, rendering inferred output in a distinct, walled-off zone, and shall persistently frame and word the diagnostic output as decision support that informs, not determines, the diagnosis. | Clinicians must never confuse observed facts with inferred conclusions and must retain accountability for the clinical decision rather than defer to the AI. | Safety-critical | UC_03, UR_09, UR_17 |
| RQ_FN_07 | The MMSS shall raise a timely, distinctive, priority- and type-differentiated audible and visual alarm naming the source parameter whenever any enumerated vital-sign parameter crosses its configured abnormal-condition threshold, within 1 second measured from the acquisition of the sample that first satisfies the threshold condition, and the alarm shall persist until acknowledged or until the condition resolves. | Timely, unambiguous, source-identified vital-sign alarming lets the clinician intervene before the patient deteriorates. The threshold condition is evaluated per parameter against its configured limits (set per RQ_FN_19); detection is defined as the first acquired sample that satisfies the limit, fixing an unambiguous start point for the 1-second budget. Alarm distinctiveness/priority is realised per IEC 60601-1-8 (RQ_CS_05). | Safety-critical | UC_04, UR_05, UR_16 |
| RQ_FN_08 | The MMSS shall, when multiple vital-sign alarms are active simultaneously, present them prioritised by clinical severity. | Prioritised presentation lets the clinician recognise and respond to the most critical condition first under alarm load. | Safety-critical | UC_04, UR_16 |
| RQ_FN_09 | The MMSS shall detect disconnection, misplacement, or loss of a valid signal on any device acquisition interface within 5 seconds of inactivity and raise a clearly differentiated connection/misplacement audible and visual alarm, distinct from vital-sign alarms, within 1 second of the trigger. | A distinct, timely data-validity fault alarm ensures the clinician never unknowingly acts on missing or misleading data, even in noisy, moving conditions (R_04, R_07). | Safety-critical | UC_05, UR_06, UR_16 |
| RQ_FN_10 | The MMSS shall, on detecting disconnection, misplacement or loss of valid signal for a parameter, visibly flag that parameter as stale/invalid rather than continuing to show its last value as current, and shall clear the flag only once valid acquisition is confirmed. | Showing a frozen value as live can drive a wrong clinical action or diagnosis; an unmistakable invalid flag prevents this until the signal is restored. | Safety-critical | UC_05, UR_06 |
| RQ_FN_11 | The MMSS shall display a per-parameter signal-quality/validity indication and visibly degrade artifact-suspect, low-quality, or not-yet-live values so that they are not presented as clean confirmed readings. | Under motion or low-perfusion, raw values can mislead; per-parameter quality indication lets the clinician rely only on confirmed-valid readings. | Safety-critical | UC_12, UR_02, UR_06 |
| RQ_FN_12 | The MMSS shall notify the clinician explicitly with audible and visual cues, and present a persistent "diagnosis unavailable — use clinical judgement" state, whenever the AI Diagnostic Capability signals a timeout or is unavailable, or no diagnostic result is received within a configured expected-response window, including on expiry of the 2-minute convergence timeout measured from submission of the data set to the AI capability. | The clinician must be told explicitly when diagnostic support is overdue or unavailable so as to fall back on clinical judgement without losing time waiting silently (R_06). The 2-minute convergence window is the external ALGOS budget that MMSS observes (it does not control AI response time, RQ_IF_11); MMSS implements its own timeout timer starting at data submission, and the trigger conditions are (a) explicit AI timeout/unavailable signal, (b) no result by the configured window, or (c) expiry of the 2-minute window — whichever occurs first. | Safety-critical | UC_06, UR_07, UR_17 |
| RQ_FN_13 | The MMSS shall present any diagnostic result that arrives after a timeout notification non-intrusively as supplementary, timestamped input, without overriding a decision in progress. | A late result must inform without silently superseding the clinician's accountable decision. | Safety-critical | UC_06, UR_07 |
| RQ_FN_14 | The MMSS shall provide a simulation/training mode that is entered only by deliberate, authorised action, is made persistently and dominantly distinct from live patient use (e.g. banner, colour, watermark), reproduces vital-sign behaviour and ranked candidates for played scenarios, and on exit affirmatively returns the system to a visually dominant live state. | A clearly separated, unmistakable simulation mode builds correct-use competence safely and prevents simulated data ever being mistaken for a live patient (R_05). | Safety-related | UC_07, UR_12 |
| RQ_FN_15 | The MMSS shall block entry to simulation/training mode during a live monitoring session, requiring an explicit live-vs-simulation confirmation, so that a live patient session cannot be accidentally placed into simulation. | Accidental entry to simulation during live care would suppress real monitoring; an explicit guard prevents it. | Safety-critical | UC_07, UR_12 |
| RQ_FN_16 | The MMSS shall allow the clinician to select relevant vital signs and ranked diagnostic candidates and share them with the Hospital Information System, requiring a two-step patient/case confirmation with a read-back of exactly what will be shared before transmission, and shall transmit the confirmed data to the HIS within 1 second of confirmation. | Second-opinion sharing must send the correct patient's data promptly while preventing the wrong patient's data from being shared. | Essential | UC_08, UR_13 |
| RQ_FN_17 | The MMSS shall report a clear failure and not falsely indicate that a case was shared when HIS transmission fails or the HIS is unreachable, and shall require renewed patient/case confirmation before any retry. | Believing a failed transmission succeeded is a serious safety and privacy failure; failure must be reported honestly with nothing wrongly shared. | Essential | UC_08, UR_13 |
| RQ_FN_18 | The MMSS shall provide a configuration interface, gated behind authentication and enforced to be unavailable during live clinical use, through which an authorised engineer can configure each device interface and its device-to-parameter mapping and the HIS integration settings, with MMSS validating and reading back each configuration before it is committed. | Commissioning of device mappings and HIS integration must be controlled, validated and confirmed so the system is correctly and safely set up before clinical use. | Safety-related | UC_09, UC_10, UR_14 |
| RQ_FN_19 | The MMSS shall constrain vital-sign alarm-threshold entry to the per-parameter configurable safe range defined for that parameter, reject any threshold or device-to-parameter mapping that is out of range, non-numeric, or otherwise invalid without committing it, surface the reason for rejection, and require explicit confirmation before any valid threshold change is committed. | Unsafe or invalid threshold/mapping values must never be committed; safe-range validation and confirmation prevent unsafe setup. For implementability the per-parameter min/max permissible bounds are a defined, validated configuration data set (one range per enumerated parameter), not a free-form input, giving a deterministic accept/reject test. | Safety-critical | UC_09, UR_14 |
| RQ_FN_20 | The MMSS shall restrict changes to safety-critical configuration parameters (alarm thresholds, device and interface settings) to authenticated, authorised users and record every change in a traceable, access-controlled change log. | Access control and a traceable log ensure only authorised changes are made and that every change can be audited. | Safety-related | UC_09, UR_15 |
| RQ_FN_21 | The MMSS shall, at care hand-over, surface a session-state summary comprising the current alarm/silence state, any non-default alarm thresholds, and which diagnostic candidates were reviewed or dismissed, and shall require the incoming clinician to explicitly acknowledge that session state, keeping any unacknowledged state visibly flagged. | Silenced alarms, altered thresholds, or dismissed candidates carried across a hand-over unseen are a direct path to missed deterioration; explicit acknowledgement prevents hidden carried-over state. | Safety-critical | UC_11, UR_16, UR_05 |
| RQ_FN_22 | The MMSS shall permit only time-bounded, source-specific alarm silencing — never an indefinite or global mute — display a persistent "silenced — re-annunciates in mm:ss" indication on the affected parameter and in the status strip, and automatically re-annunciate the alarm if the underlying condition remains unresolved when the silence period expires. | Silencing must let the clinician manage the patient briefly without ever permanently suppressing a genuine, still-unresolved critical alarm. | Safety-critical | UC_13, UR_16, UR_05 |
| RQ_FN_23 | The MMSS shall escalate (e.g. shorten the silence window, raise priority/audibility, or surface the silenced state more prominently) when the same unresolved critical alarm is repeatedly silenced, such that no critical alarm can be left permanently silenced. | Habitual reflexive silencing of an unresolved critical alarm must be countered by escalation so a genuine condition is never suppressed indefinitely. | Safety-critical | UC_13, UR_16 |
| RQ_FN_24 | The MMSS shall validate HIS integration settings on configuration, including a connectivity test, and shall not mark the integration as ready for clinical use until the settings are valid and the endpoint is reachable. | Second-opinion sharing must work correctly and securely; an unvalidated or unreachable HIS integration must not be presented as ready. | Safety-related | UC_10, UR_14, UR_13 |

#### Performance Requirements (RQ_PR_*)

Quantitative requirements on how well the system performs its functions: response times, throughput, accuracy, capacity, availability.

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_PR_01 | The MMSS shall complete its activation and start-up self-check and reach the ready (or explicit not-ready/fault) state within 10 seconds of being powered on or started. | A bounded start-up time ensures the clinician knows promptly when monitoring is live and is not left waiting indefinitely on an undetermined state. | Safety-related | RQ_FN_01 |
| RQ_PR_02 | The MMSS shall display each acquired vital-sign parameter on the Monitor Display within 1 second, measured from receipt of the sample at the device acquisition interface boundary to its appearance on the display. | A boundary-observable display latency of 1 second ensures clinicians see current values without perceptible lag. The 1 second is the system black-box roll-up of the internal acquisition-to-render allocation (internally budgeted as ≤ 800 ms preparation + ≤ 200 ms processing); that internal split is an architecture allocation and is verified only at this 1-second boundary. | Safety-related | RQ_FN_02 |
| RQ_PR_03 | The MMSS shall refresh the vital-signs display on a timer-based interval of 1 second. | A fixed 1-second refresh cadence gives a steady, predictable at-a-glance monitoring picture. | Safety-related | RQ_FN_02 |
| RQ_PR_04 | The MMSS shall sustain acquisition of vital-sign data at a rate of at least 0.1 Hz (one sample or update at least every 10 seconds) per connected parameter. | A guaranteed minimum input rate ensures displayed and trended values remain current enough to be clinically reliable. | Safety-related | RQ_FN_02 |
| RQ_PR_05 | The MMSS shall update each parameter's displayed trend within 1 second of the corresponding vital-sign value being acquired. | Trend rendering must keep pace with acquisition so gradual deterioration is visible in near real time. | Safety-related | RQ_FN_03 |
| RQ_PR_06 | The MMSS shall present the ranked diagnostic candidates on the Monitor Display within 1 second of receiving them from the Open Evidence AI Diagnostic Capability. | The MMSS's own observable rendering latency must be bounded to 1 second once candidates are received; AI convergence time is the external AI budget and is excluded from this requirement. | Safety-critical | RQ_FN_04 |
| RQ_PR_07 | The MMSS shall annunciate a vital-sign alarm, both audibly and visually, within 1 second of detecting that a parameter has crossed its configured abnormal-condition threshold. | A bounded detection-to-annunciation latency ensures the clinician is alerted in time to intervene before patient deterioration. | Safety-critical | RQ_FN_07 |
| RQ_PR_08 | The MMSS shall detect disconnection, misplacement, or loss of valid signal on any device acquisition interface within 5 seconds of input inactivity. | A bounded inactivity window ensures data-validity faults are caught quickly so the clinician never unknowingly acts on missing data. | Safety-critical | RQ_FN_09 |
| RQ_PR_09 | The MMSS shall annunciate the connection/misplacement alarm, both audibly and visually, within 1 second of the trigger condition being established. | Once a connection fault is triggered it must be made known to the clinician without perceptible delay. | Safety-critical | RQ_FN_09 |
| RQ_PR_10 | The MMSS shall notify the clinician of a diagnosis timeout or AI unavailability within 1 second of detecting the timeout or unavailable condition, including on expiry of the 2-minute convergence window. | The MMSS observes the external 2-minute AI convergence budget and must promptly surface the overdue/unavailable condition so the clinician falls back on judgement without silent waiting. | Safety-critical | RQ_FN_12 |
| RQ_PR_11 | The MMSS shall transmit the confirmed vital-signs and diagnostic-candidate data set to the Hospital Information System within 1 second of the clinician's transmission confirmation. | Prompt transmission ensures second-opinion sharing is responsive while the confirmation gate prevents wrong-patient sharing. | Essential | RQ_FN_16 |
| RQ_PR_12 | The MMSS shall concurrently acquire from, and display in real time, all six supported device types — ECG, Pulse Oximeter, BP Monitor, Thermal Probe, Capnometer, and EEG — without exceeding the per-parameter display-latency and refresh targets. | The system must carry the full concurrent device load specified for clinical use while still meeting its timing budgets. | Safety-related | RQ_FN_02 |
| RQ_PR_13 | The MMSS shall raise the per-parameter stale/invalid flag within 1 second of detecting loss of valid acquisition for that parameter. | A bounded flagging latency prevents a frozen last value being read as current during the gap before the connection alarm. | Safety-critical | RQ_FN_10 |
| RQ_PR_14 | The MMSS shall update the per-parameter signal-quality/validity indication on the timer-based 1-second UI interval, in step with the value it qualifies. | Quality indication must track each value as it refreshes so the clinician relies only on confirmed-valid readings. | Safety-critical | RQ_FN_11 |
| RQ_PR_15 | The MMSS shall be available for clinical monitoring at least 99.9% of intended operating time, excluding scheduled maintenance, measured as the ratio of time the MMSS is in a monitoring-capable state to total intended operating time over a defined measurement period. | High operational availability is required of a continuous patient-monitoring system so that monitoring is not lost during care. For verifiability the 99.9% is assessed over a defined measurement period (e.g. monthly) against a defined "monitoring-capable" up-state, excluding scheduled maintenance windows; this fixes an unambiguous, testable availability metric rather than an abstract target. | Safety-critical | RQ_FN_02 |
| RQ_PR_16 | The MMSS shall present each acquired vital-sign value at a numerical accuracy and resolution no coarser than that delivered by its source measurement device, introducing no additional rounding or transformation error in display. | Displayed values must faithfully represent the device measurement so clinical decisions are not made on degraded data. | Safety-critical | RQ_FN_02 |

#### Non-Functional Requirements (RQ_NF_*)

How the system should behave rather than what it does: reliability, maintainability, security, privacy, scalability. Compliance, labeling, and training requirements live here too.

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_NF_01 | The MMSS shall be developed, maintained, and documented under a software development life-cycle conforming to IEC 62304 for its assigned software safety class, with bidirectional traceability maintained from requirements through architecture, implementation, verification, validation, and release. | A conformant, fully traceable life-cycle is the core market-access obligation for medical device software and is the technical basis a notified body audits; without it the device cannot lawfully be placed on the market. | Safety-critical | BR_01, BR_03, RE_01, RE_11 |
| RQ_NF_02 | The MMSS shall be available for clinical monitoring for at least 99.9% of intended operating time (measured per RQ_PR_15 over a defined measurement period, excluding scheduled maintenance), and on any unplanned interruption shall enter its defined safe-state behaviour rather than silently lose vital-signs presentation. | A continuously relied-upon critical-care device must remain dependable; high availability is both a contracted procurement expectation and a safety property since loss of monitoring endangers the patient. The quantitative target and its measurement method are the same as RQ_PR_15; this requirement adds the qualitative dependability obligation (safe-state on interruption) that the procurement and risk view require. | Safety-critical | BR_18, BR_09 |
| RQ_NF_03 | The MMSS shall be maintainable and updatable over its full service life such that safety and security updates, and re-validation of changes in the externally sourced AI capability or component interfaces, can be delivered through the conformant IEC 62304 life-cycle and re-verified before deployment. | Timely patching and controlled change are binding post-market obligations; because the software is regulated, every update must pass the same life-cycle and verification as the original release rather than being deployed ad hoc. | Safety-critical | BR_09, RE_01 |
| RQ_NF_04 | The MMSS shall protect patient health data it acquires, processes, displays, and exchanges through cybersecurity controls — including authenticated access, protection of data in transit and at rest, and resistance to unauthorised modification — appropriate to a networked medical device. | Cybersecurity is a mandatory market-access expectation for connected medical devices; unprotected health data and exploitable interfaces create both patient-safety and data-protection hazards. | Safety-related | RE_09, BR_10 |
| RQ_NF_05 | The MMSS shall process personal health data in compliance with applicable data-protection and privacy law, applying lawful basis, data minimisation, and role-based access control to monitoring, processing, and hospital-information-system exchange. | Lawful processing of patient data is a precondition of market access; non-compliance with data-protection law independently blocks deployment regardless of clinical performance. | Safety-related | RE_09 |
| RQ_NF_06 | The MMSS shall maintain a tamper-evident audit log of safety-relevant events — including alarms, diagnostic-candidate presentation, clinician acknowledgements, configuration changes, and data transmissions to the hospital information system — with reliable time-stamping. | Auditable event records are required for post-market vigilance, incident investigation, and demonstrating safe operation; they also support data-integrity and accountability obligations. | Safety-related | RE_08, RE_09, BR_10 |
| RQ_NF_07 | The MMSS shall preserve the integrity of acquired, processed, and displayed clinical data such that no value is silently corrupted, reordered, or mis-associated with the wrong patient or parameter from acquisition through presentation and transmission. | Data integrity is foundational to patient safety; a corrupted or mis-attributed value can drive a wrong clinical decision and is a core concern of both risk management and regulatory review. | Safety-critical | RE_03, BR_01 |
| RQ_NF_08 | The MMSS shall be accompanied by complete labelling and instructions for use in the required languages, stating intended use, indications, contraindications, warnings, the decision-support (non-autonomous) nature of the diagnostic output, training prerequisites, and residual-risk information. | Complete, compliant labelling and IFU are a mandatory condition of market access and the means by which trained users operate the device within its validated scope and understand residual risk. | Safety-related | RE_07, BR_01 |
| RQ_NF_09 | The MMSS shall clearly and persistently present the diagnostic output as ranked decision support that informs, and does not autonomously determine, the diagnosis or treatment, keeping the clinician in the decision loop. | Clinician-in-the-loop framing is a mandatory regulatory expectation for AI diagnostic functions and directly mitigates the critical risk of over-reliance on algorithmic output. | Safety-critical | RE_12, BR_15 |
| RQ_NF_10 | The MMSS shall provide a clearly delineated simulation/training mode, segregated from live clinical use, that enables clinicians to build and maintain competence in operating the system and interpreting diagnostic candidates before relying on it with real patients. | Mandatory simulation training is a documented risk control for clinician misinterpretation of AI candidates and a usability-engineering and service obligation. | Safety-related | BR_11, RE_04, RE_07 |
| RQ_NF_11 | The MMSS shall be designed and validated under a usability engineering process conforming to IEC 62366-1, addressing use-related hazards and foreseeable use errors for trained professional users in the intended critical-care and mobile use environments. | A documented usability engineering process is required by the notified body to demonstrate that misinterpretation of vital signs or diagnostic output does not compromise patient safety. | Safety-critical | RE_04, BR_11 |
| RQ_NF_12 | The MMSS shall capture and retain the post-market surveillance and vigilance data needed to detect, report, and investigate safety signals and serious incidents over its service life, supporting incident and periodic safety reporting. | A functioning post-market surveillance and vigilance capability is a mandatory ongoing obligation after market access; the device must yield the data needed to fulfil it. | Safety-related | RE_08, BR_10 |
| RQ_NF_13 | The MMSS shall be reproducibly producible and deployable at quality across multiple care settings and fleet units within its validated configuration, without per-site re-engineering and without deployment outside the validated device-type and interface set. | Repeatable, in-envelope deployment keeps every installed instance within the validated, supportable, and certified configuration, protecting both compliance and the installed-base investment. | Safety-related | BR_16, BR_07 |
| RQ_NF_14 | The MMSS shall be developed, certified, and supported under a manufacturer quality management system conforming to ISO 13485, covering design, development, production, and post-market activities. | A certified QMS is required for the product to be produced under controlled, auditable, reproducible conditions and is a precondition of notified-body certification. | Safety-critical | RE_06, BR_01 |
| RQ_NF_15 | The MMSS shall have a defined end-of-life encompassing discontinuation, decommissioning, and secure patient-data handling consistent with its regulatory and data-protection obligations. | A planned end-of-life is part of the post-market life-cycle the manufacturer must stand behind; uncontrolled discontinuation creates compliance, dependability, and data-protection exposure. | Safety-related | BR_17, RE_09 |
| RQ_NF_16 | The MMSS shall be safety-classified per IEC 62304 with its classification, and any class-reducing risk controls, justified, documented, and traceable to the independent external risk-control measures relied upon. | A justified, documented safety classification governs the rigour of the whole life-cycle and is required evidence for regulatory review; an unsupported class reduction invalidates the conformance argument. | Safety-critical | RE_02, BR_02 |

#### Constraint Requirements (RQ_CS_*)

External constraints the system must respect: regulatory rules, applicable standards, imposed technology choices, environmental conditions.

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_CS_01 | The MMSS shall comply with ANSI/AAMI IEC 62304 as software safety Class C mitigated to Class B, applying the life-cycle process rigour required for that classification. | The mandated software safety classification fixes the life-cycle obligations the device must meet for market access; it is an externally imposed regulatory constraint, not a design choice. | Safety-critical | RE_01, RE_02 |
| RQ_CS_02 | The MMSS shall be developed under a risk management process conforming to ISO 14971, with identified hazards, estimated and controlled risks, and a documented benefit-risk determination across the product life cycle. | A conformant ISO 14971 risk management process is a mandatory market-access requirement and the basis on which residual risk acceptability is judged. | Safety-critical | RE_03 |
| RQ_CS_03 | The MMSS shall be developed under a usability engineering process conforming to IEC 62366-1. | Conformity with the applicable usability engineering standard is a mandatory expectation of the notified body for the user interface of the device. | Safety-critical | RE_04 |
| RQ_CS_04 | The MMSS shall be developed, produced, and supported under a quality management system conforming to ISO 13485. | A certified ISO 13485 QMS is an externally imposed precondition of producing and certifying the regulated device. | Safety-critical | RE_06 |
| RQ_CS_05 | The MMSS shall generate clinical alarm signals conforming to IEC 60601-1-8 for alarm prioritisation, distinctiveness, and clinician notification. | Conformity with the applicable alarm-system safety standard is a mandatory constraint ensuring abnormal conditions and sensor/connection faults are reliably communicated. | Safety-critical | RE_10 |
| RQ_CS_06 | The MMSS shall use, for its first release, the commercially validated off-the-shelf Open Evidence AI diagnostic model as a black-box capability accessed only across the defined ICD_OPENEVIDENCE interface, and shall not incorporate, retrain, or modify a diagnostic model. | The off-the-shelf validated model is a mandated constraint that mitigates algorithmic-clearance and model-validation risk; a custom model is out of scope for the first release. Treating the AI strictly as a black box reached only through its published interface bounds the implementation: MMSS owns request formatting, result handling, ranking/basis/confidence rendering, and timeout behaviour, but not the model's inference, response time, or accuracy — those are external dependencies the design must not assume control over. | Safety-related | RE_12 |
| RQ_CS_07 | The MMSS shall maintain documented intended-use boundaries, change control over the AI model, and a clinician-in-the-loop decision pathway for the diagnostic function. | These are mandatory regulatory conditions for an AI/ML diagnostic function so that algorithmic output does not determine patient care without qualified human oversight. | Safety-critical | RE_12 |
| RQ_CS_08 | The MMSS shall support exactly the six specified non-invasive measurement device types — ECG, Pulse Oximeter, BP Monitor, Thermal Probe, Capnometer, and EEG — and shall be validated against that defined device-type set. | The supported device-type set is an externally fixed scope constraint that bounds the validated configuration the device is certified and supported against. | Safety-related | RE_01 |
| RQ_CS_09 | The MMSS shall exchange data with hospital information systems through a recognised health-data interoperability standard (HL7/FHIR), once the protocol and its interface control documents are defined. | Standards-based interoperability is the mandated, auditable basis for clinical-data exchange; the specific protocol and ICDs are an external constraint still to be fixed. | Safety-related | RE_09 |
| RQ_CS_10 | The MMSS shall process and exchange personal health data in compliance with applicable data-protection and privacy legislation. | Compliance with the governing data-protection legislation is a non-negotiable legal constraint on any processing or transfer of patient data. | Safety-related | RE_09 |
| RQ_CS_11 | The MMSS shall operate within the fixed resource and timing envelope of its host platform — a compact embedded CPU with real-time operating system capabilities — using only the runtime, scheduling, timing, and I/O services published by that platform, without dependence on hardware design, selection, or modification. | The fixed embedded real-time host platform is an externally imposed environmental and technology constraint the software must respect, as no hardware development is in scope. For implementability this means MMSS must achieve all timing budgets (display, alarm, activation) using the platform's published real-time scheduling/timing services and within its available compute/memory envelope; the platform capabilities are an inherited assumption (per ICD_PLATFORM) the software cannot change. | Safety-related | RE_01 |
| RQ_CS_12 | The MMSS shall maintain a complete, traceable technical file providing design, verification, validation, and risk evidence with full traceability from requirements to test results. | A complete, traceable technical file is the mandatory artefact through which conformity is independently audited and certified for market access. | Safety-critical | RE_11 |

### Verification (SV_*)

The **BDD feature files** that verify the functional requirements, defined jointly by the 3-Amigos (Product Owner, Development Lead, Verification Lead). Write **one feature file per functional requirement** as a `gherkin` fenced block, tagged `@ID:RQ_FN_xx` to trace it to the requirement it verifies. Each feature has a user story (`As a … I want … So that …`), a `Rule:` that captures the requirement's "shall" statement, and one or more concrete `Scenario`s with `Given / When / Then` steps and data tables for the expected values. Use measurable outcomes (e.g. "within 5 seconds"). Every RQ_FN_* must have a feature file and every RQ_* must be covered by at least one scenario. The converter records each feature file as one row (`SV_*`) in the workbook's Verification table.

```gherkin
@ID:RQ_FN_01
Feature: Start-up Self-Check and Ready State
    As a Bedside Clinician I want the MMSS to perform a start-up self-check and show an explicit ready or not-ready state
    So that I know when monitoring is live and never mistake an unstarted parameter for a valid reading

Rule: The MMSS shall, on start-up, perform a self-check of its acquisition, presentation and alarm functions and present an explicit initialising-then-ready (or not-ready/fault) state, marking any not-yet-live parameter distinctly, and shall not present a normal monitoring picture if the self-check fails.

Scenario: Successful self-check reaches the ready state
    Given the simulator is running in live mode
    And no sensors are connected in the simulator
    When the MMSS is started
    Then the Display Interface shows an "initialising" state within 1 second of start-up
    And the Display Interface shows the "ready" state within 10 seconds of start-up
    And every not-yet-live parameter is marked distinctly so no empty field reads as a normal value
    | parameter        | shown as           |
    | Heart Rate       | not-yet-live       |
    | SpO2             | not-yet-live       |
    | Temperature      | not-yet-live       |

Scenario: Failed self-check withholds the normal monitoring picture
    Given the simulator is running in live mode
    And no sensors are connected in the simulator
    And the MMSS acquisition self-check is configured to return a fault result
    When the MMSS is started
    Then the Display Interface shows an explicit not-ready/fault state within 10 seconds of start-up
    And the Display Interface does not present a normal monitoring picture
```

```gherkin
@ID:RQ_FN_02
Feature: Acquire and Display Vital Signs
    As a Bedside Clinician I want the MMSS to continuously display each enumerated vital-sign parameter with value, unit and source
    So that I keep uninterrupted at-a-glance awareness of the patient's condition

Rule: The MMSS shall acquire each enumerated vital-sign parameter from its connected measurement device and continuously display each parameter in real time with its value, unit and source on the Monitor Display, updating on the timer-based 1-second UI interval.

Scenario: Show vital signs from ECG Electrodes on the Monitor Display
    Given the simulator is running
    And no sensors are connected in the simulator
    And the MMSS is running
    When the ECG Electrodes are connected in the simulator
    Then the following vital signs are visible on the Display Interface within 1 second
    | vital sign |
    | Heart Rate |

Scenario: Show vital signs from NIBP Cuff on the Monitor Display
    Given the simulator is running
    And no sensors are connected in the simulator
    And the MMSS is running
    When the NIBP Cuff is connected in the simulator
    Then the following vital signs are visible on the Display Interface within 1 second
    | vital sign   |
    | Systolic BP  |
    | Diastolic BP |
    | MAP          |

Scenario: Show vital signs from SpO₂ Probe on the Monitor Display
    Given the simulator is running
    And no sensors are connected in the simulator
    And the MMSS is running
    When the SpO₂ Probe is connected in the simulator
    Then the following vital signs are visible on the Display Interface within 1 second
    | vital sign |
    | SpO2       |
    | Pulse Rate |

Scenario: Show vital signs from EtCO₂ Sampling Line on the Monitor Display
    Given the simulator is running
    And no sensors are connected in the simulator
    And the MMSS is running
    When the EtCO₂ Sampling Line is connected in the simulator
    Then the following vital signs are visible on the Display Interface within 1 second
    | vital sign       |
    | Respiratory Rate |
    | EtCO2            |

Scenario: Show vital signs from Temperature Probe on the Monitor Display
    Given the simulator is running
    And no sensors are connected in the simulator
    And the MMSS is running
    When the Temperature Probe is connected in the simulator
    Then the following vital signs are visible on the Display Interface within 1 second
    | vital sign  |
    | Temperature |

Scenario: Show vital signs from EEG Electrodes on the Monitor Display
    Given the simulator is running
    And no sensors are connected in the simulator
    And the MMSS is running
    When the EEG Electrodes are connected in the simulator
    Then the following vital signs are visible on the Display Interface within 1 second
    | vital sign |
    | BIS        |

Scenario: Each displayed parameter shows value, unit and source
    Given the simulator is running in live mode
    And no sensors are connected in the simulator
    And the MMSS is running
    When all sensors are connected in the simulator
    And the simulator supplies the following acquired values at 1 Hz
    | vital sign       | value | unit         | source           |
    | Heart Rate       | 72    | bpm          | ECG Monitor      |
    | Systolic BP      | 120   | mmHg         | BP / NIBP Monitor|
    | SpO2             | 98    | %            | Pulse Oximeter   |
    | Respiratory Rate | 16    | breaths/min  | Capnometer       |
    | EtCO2            | 38    | mmHg         | Capnometer       |
    | Temperature      | 37.0  | °C           | Thermal Probe    |
    | BIS              | 50    | index        | EEG Monitor      |
    Then within 1 second of acquisition the Display Interface shows each acquired parameter with its value, unit and source as supplied
    And the displayed values refresh on the timer-based 1-second UI interval

Scenario: Displayed value matches the source-device value without added rounding (RQ_PR_16)
    Given the simulator is running in live mode
    And the MMSS is running
    And the Thermal Probe is connected in the simulator
    When the Thermal Probe supplies the following acquired values
    | source value | unit | resolution |
    | 37.05        | °C   | 0.01       |
    | 41.27        | °C   | 0.01       |
    Then within 1 second of acquisition the Display Interface shows each value exactly as supplied
    | displayed value | unit |
    | 37.05           | °C   |
    | 41.27           | °C   |
    And no value is shown at a resolution coarser than the 0.01 °C delivered by the source device

Scenario: Acquisition is sustained at the minimum input rate (RQ_PR_04, RQ_IF_01-06)
    Given the simulator is running in live mode
    And the MMSS is running
    And all sensors are connected in the simulator
    When each connected device supplies one valid sample every 10 seconds (0.1 Hz) for 60 seconds
    Then for each connected parameter the MMSS acquires at least 6 samples over the 60-second window
    And each acquired parameter remains displayed as a current value and is never flagged stale during the window

Scenario: Show all vital signs when all sensors are connected (RQ_PR_12 concurrent six-device load)
    Given the simulator is running
    And no sensors are connected in the simulator
    And the MMSS is running
    When the ECG Electrodes are connected in the simulator
    And the NIBP Cuff is connected in the simulator
    And the SpO₂ Probe is connected in the simulator
    And the EtCO₂ Sampling Line is connected in the simulator
    And the Temperature Probe is connected in the simulator
    And the EEG Electrodes are connected in the simulator
    Then the following vital signs are visible on the Display Interface within 1 second
    | vital sign       |
    | Heart Rate       |
    | Systolic BP      |
    | Diastolic BP     |
    | MAP              |
    | SpO2             |
    | Pulse Rate       |
    | Respiratory Rate |
    | EtCO2            |
    | Temperature      |
    | BIS              |
```

```gherkin
@ID:RQ_FN_03
Feature: Display Vital-Sign Trend
    As a Bedside Clinician I want the MMSS to show the recent trend of each vital-sign parameter in addition to its instantaneous value
    So that I can recognise gradual deterioration early and intervene before an alarm threshold is crossed

Rule: The MMSS shall display, for each enumerated vital-sign parameter, its recent trend (direction and rate of change over time) in addition to its instantaneous value.

Scenario: Trend appears alongside the instantaneous value
    Given the simulator is running in live mode
    And the MMSS is running
    And the ECG Electrodes are connected in the simulator
    When the simulator supplies Heart Rate rising at 5 bpm per minute over 3 minutes
    | t (s) | Heart Rate (bpm) |
    | 0     | 70               |
    | 60    | 75               |
    | 120   | 80               |
    | 180   | 85               |
    Then the Display Interface shows the instantaneous Heart Rate value 85 bpm
    And the Display Interface shows the recent Heart Rate trend with direction and rate of change
    | parameter  | trend direction | rate of change   |
    | Heart Rate | rising          | +5 bpm/min       |
    And the displayed trend updates within 1 second of each new acquired value
```

```gherkin
@ID:RQ_FN_04
Feature: Present Ranked Diagnostic Candidates
    As an Emergency Physician I want the MMSS to present ranked diagnostic candidates with basis and confidence
    So that I can accelerate triage while judging how far to trust each candidate

Rule: The MMSS shall submit the prepared vital-signs data set to the AI Diagnostic Capability and present the ranked diagnostic candidates it returns as an ordered list, each with its supporting basis and graded confidence/uncertainty, within 1 second of receipt of the candidates from the AI capability.

Scenario: Render ranked candidates received from the AI capability
    Given the simulator is running in live mode
    And the MMSS is running
    And all sensors are connected in the simulator supplying valid vital-signs data
    And the AI Diagnostic Capability is simulated by a stub returning a scripted response
    When the simulated AI Diagnostic Capability returns the following ranked candidates to the MMSS
    | rank | candidate         | basis                  | confidence |
    | 1    | Sepsis            | HR↑, Temp↑, RR↑        | High       |
    | 2    | Hypovolaemia      | BP↓, HR↑               | Medium     |
    | 3    | Cardiac ischaemia | ECG changes            | Low        |
    Then within 1 second of receipt from the AI capability the Display Interface shows the candidates as an ordered list
    And each candidate is shown with its supporting basis and graded confidence/uncertainty
    And the list order matches the AI-supplied ranking 1, 2, 3
```

```gherkin
@ID:RQ_FN_05
Feature: Withhold Candidates Without Valid Input
    As an Emergency Physician I want the MMSS to withhold diagnostic candidates when no valid vital-signs data is available
    So that I am never shown a result that is unsupported by actual measurements

Rule: The MMSS shall withhold diagnostic candidates and indicate that diagnostic input is incomplete whenever no valid vital-signs data is available to submit to the AI Diagnostic Capability.

Scenario: No valid data withholds candidates
    Given the simulator is running in live mode
    And the MMSS is running
    And no sensors are connected in the simulator
    When the MMSS attempts to produce diagnostic candidates
    Then the MMSS does not submit any data set to the AI Diagnostic Capability
    And the Display Interface shows no diagnostic candidates
    And the Display Interface shows an explicit "diagnostic input incomplete" indication within 1 second
```

```gherkin
@ID:RQ_FN_06
Feature: Separate Observed Data from Inferred Candidates
    As a Bedside Clinician I want measured vital signs visually walled off from AI-inferred candidates
    So that I never confuse observed facts with inferred conclusions and retain clinical accountability

Rule: The MMSS shall visually separate measured (observed) vital-sign data from AI-inferred diagnostic candidates in a distinct walled-off zone, and shall persistently frame the diagnostic output as decision support that informs, not determines, the diagnosis.

Scenario: Observed and inferred output are visually segregated
    Given the simulator is running in live mode
    And the MMSS is running
    And the ECG Electrodes are connected in the simulator supplying Heart Rate 72 bpm
    And the simulated AI Diagnostic Capability has returned ranked candidates "Sepsis (High)" and "Hypovolaemia (Medium)"
    When the Display Interface renders the current monitoring picture
    Then the measured Heart Rate value 72 bpm is shown within the observed-data zone and not within the inferred zone
    And the diagnostic candidates "Sepsis (High)" and "Hypovolaemia (Medium)" are shown within a distinct, walled-off inferred zone and not within the observed-data zone
    And the inferred zone persistently displays a "decision support — informs, does not determine the diagnosis" frame label
```

```gherkin
@ID:RQ_FN_07
Feature: Vital-Sign Abnormal-Condition Alarm
    As a Bedside Clinician I want a distinctive alarm naming the source parameter when a vital sign crosses its threshold
    So that I can intervene before the patient deteriorates

Rule: The MMSS shall raise a timely, distinctive, priority- and type-differentiated audible and visual alarm naming the source parameter whenever any enumerated vital-sign parameter crosses its configured abnormal-condition threshold, within 1 second measured from acquisition of the first sample satisfying the threshold, and the alarm shall persist until acknowledged or until the condition resolves.

Scenario Outline: Threshold breach raises a source-named alarm within 1 second
    Given the simulator is running in live mode
    And the MMSS is running
    And the <device> is connected in the simulator
    And the abnormal-condition threshold for <parameter> is configured to <threshold> <unit>
    And <parameter> is reading a normal value within range
    When the simulator supplies a <parameter> value of <breach> <unit> that crosses the threshold
    Then within 1 second of acquisition of the first breaching sample the Display Interface raises an audible and visual vital-sign alarm
    And the alarm names <parameter> as the source
    And the alarm persists until acknowledged or until the condition resolves

    Examples:
    | device            | parameter   | unit | threshold | breach |
    | ECG Electrodes    | Heart Rate  | bpm  | 150       | 165    |
    | SpO₂ Probe        | SpO2        | %    | 90        | 85     |
    | Temperature Probe | Temperature | °C   | 38.5      | 39.2   |
```

```gherkin
@ID:RQ_FN_08
Feature: Prioritise Concurrent Vital-Sign Alarms
    As a Bedside Clinician I want simultaneous alarms presented by clinical severity
    So that I respond to the most critical condition first under alarm load

Rule: The MMSS shall, when multiple vital-sign alarms are active simultaneously, present them prioritised by clinical severity.

Scenario: Multiple active alarms are ordered by severity
    Given the simulator is running in live mode
    And the MMSS is running
    And all sensors are connected in the simulator
    And the abnormal-condition thresholds are configured per the table below
    When the simulator supplies, within the same 1-second UI interval, values that breach all three thresholds
    | parameter   | unit | threshold | breach value | severity |
    | SpO2        | %    | 90        | 80           | high     |
    | Heart Rate  | bpm  | 150       | 160          | medium   |
    | Temperature | °C   | 38.5      | 39.0         | low      |
    Then the Display Interface presents the three active alarms ordered by clinical severity SpO2, Heart Rate, Temperature
    And the highest-severity alarm (SpO2) is presented most prominently
```

```gherkin
@ID:RQ_FN_09
Feature: Connection / Misplacement Alarm
    As a Pre-hospital Clinician I want a distinct alarm when a device disconnects, is misplaced, or loses a valid signal
    So that I never unknowingly act on missing or misleading data

Rule: The MMSS shall detect disconnection, misplacement, or loss of a valid signal on any device acquisition interface within 5 seconds of inactivity and raise a clearly differentiated connection/misplacement audible and visual alarm, distinct from vital-sign alarms, within 1 second of the trigger.

Scenario: Sensor disconnection raises a connection alarm
    Given the simulator is running in live mode
    And the MMSS is running
    And the SpO₂ Probe is connected in the simulator supplying SpO2 98 % and Pulse Rate 72 bpm
    When the SpO₂ Probe stops supplying samples in the simulator
    Then the MMSS detects the loss of valid signal within 5 seconds of inactivity
    And within 1 second of that trigger the Display Interface raises a connection/misplacement audible and visual alarm
    And the connection alarm is clearly differentiated from vital-sign alarms
```

```gherkin
@ID:RQ_FN_10
Feature: Flag Stale or Invalid Parameter
    As a Pre-hospital Clinician I want a lost parameter flagged as stale/invalid rather than showing its last value
    So that I do not read a frozen value as a live reading

Rule: The MMSS shall, on detecting disconnection, misplacement or loss of valid signal for a parameter, visibly flag that parameter as stale/invalid rather than continuing to show its last value as current, and shall clear the flag only once valid acquisition is confirmed.

Scenario: Lost parameter is flagged stale and later cleared
    Given the simulator is running in live mode
    And the MMSS is running
    And the Temperature Probe is connected in the simulator
    And Temperature is displayed as 37.0 °C with a valid signal
    When the Temperature Probe stops supplying samples in the simulator for at least 5 seconds
    Then the Display Interface visibly flags Temperature as stale/invalid within 1 second of the loss being detected
    And the Display Interface does not present the last Temperature value (37.0 °C) as current
    When the Temperature Probe resumes supplying a valid 37.2 °C signal in the simulator
    Then the Display Interface clears the stale/invalid flag for Temperature and shows 37.2 °C
```

```gherkin
@ID:RQ_FN_11
Feature: Per-Parameter Signal-Quality Indication
    As a Pre-hospital Clinician I want a per-parameter signal-quality indication and degraded display of suspect values
    So that I rely only on confirmed-valid readings under motion or low perfusion

Rule: The MMSS shall display a per-parameter signal-quality/validity indication and visibly degrade artifact-suspect, low-quality, or not-yet-live values so that they are not presented as clean confirmed readings.

Scenario: Low-quality value is visibly degraded
    Given the simulator is running in live mode
    And the MMSS is running
    And the SpO₂ Probe is connected in the simulator
    When the simulator supplies an SpO2 reading of 94 % with the signal-quality status set to "low / artifact-suspect"
    Then the Display Interface shows a low-quality signal-quality/validity indication for SpO2
    And the Display Interface visibly degrades the SpO2 value (e.g. dimmed value with a warning icon) so it is not shown as a clean confirmed reading

Scenario: Quality indication refreshes in step with the value on the 1-second UI interval (RQ_PR_14)
    Given the simulator is running in live mode
    And the MMSS is running
    And the SpO₂ Probe is connected in the simulator
    When the simulator changes the SpO2 signal-quality status across successive 1-second UI intervals
    | t (s) | SpO2 value | signal-quality status |
    | 0     | 98         | good                  |
    | 1     | 94         | low / artifact-suspect|
    | 2     | 97         | good                  |
    Then at each 1-second UI interval the Display Interface updates the SpO2 signal-quality/validity indication to match the supplied status for that interval
    And the quality indication for SpO2 is refreshed within the same 1-second UI interval as the value it qualifies
```

```gherkin
@ID:RQ_FN_12
Feature: Notify Diagnosis Timeout or AI Unavailability
    As an Emergency Physician I want explicit notification when diagnostic support is overdue or unavailable
    So that I fall back on clinical judgement without losing time waiting silently

Rule: The MMSS shall notify the clinician with audible and visual cues and present a persistent "diagnosis unavailable — use clinical judgement" state whenever the AI Diagnostic Capability signals a timeout or is unavailable, or no result is received within the configured window, including on expiry of the 2-minute convergence timeout measured from submission.

Scenario: AI timeout signal triggers explicit notification
    Given the simulator is running in live mode
    And the MMSS is running
    And the AI Diagnostic Capability is simulated by a stub
    And valid vital-signs data has been submitted to the simulated AI Diagnostic Capability
    When the simulated AI Diagnostic Capability returns a timeout signal
    Then within 1 second of receipt of the timeout signal the Display Interface raises an audible and visual notification
    And the Display Interface shows a persistent "diagnosis unavailable — use clinical judgement" state

Scenario: Convergence window expires with no result
    Given the simulator is running in live mode
    And the MMSS is running
    And the AI Diagnostic Capability is simulated by a stub that never returns a result
    And the configured convergence window is set to 120 seconds (the 2-minute timeout)
    When valid vital-signs data is submitted to the simulated AI Diagnostic Capability
    And no diagnostic result is received before the configured window elapses
    Then within 1 second of window expiry the Display Interface raises an audible and visual notification
    And the Display Interface shows a persistent "diagnosis unavailable — use clinical judgement" state
```

```gherkin
@ID:RQ_FN_13
Feature: Handle Late Diagnostic Result
    As an Emergency Physician I want a late diagnostic result presented non-intrusively as supplementary input
    So that it informs without silently overriding my accountable decision

Rule: The MMSS shall present any diagnostic result that arrives after a timeout notification non-intrusively as supplementary, timestamped input, without overriding a decision in progress.

Scenario: Result arriving after timeout is shown as supplementary
    Given the simulator is running in live mode
    And the MMSS is running
    And the AI Diagnostic Capability is simulated by a stub
    And a diagnosis-timeout notification has already been shown for the current submission
    When the simulated AI Diagnostic Capability returns the candidate "Sepsis (High)" after the timeout
    Then the Display Interface presents the late result non-intrusively as supplementary input (not as a modal that interrupts the clinician)
    And the late result is shown with a receipt timestamp
    And the MMSS does not replace or override the in-progress diagnostic decision
```

```gherkin
@ID:RQ_FN_14
Feature: Simulation / Training Mode
    As a Clinical Trainer I want a deliberately entered, dominantly distinct simulation mode
    So that simulated data can never be mistaken for a live patient

Rule: The MMSS shall provide a simulation/training mode entered only by deliberate authorised action, made persistently and dominantly distinct from live patient use, that reproduces vital-sign behaviour and ranked candidates for played scenarios, and on exit affirmatively returns the system to a visually dominant live state.

Scenario: Entering and exiting simulation mode
    Given the MMSS is running in live mode with no live monitoring session active
    And an authorised trainer is authenticated
    When the trainer enters simulation/training mode by deliberate authorised action and selects scenario "Sepsis progression"
    Then the Display Interface shows a persistent, dominant simulation indication (banner, colour or watermark)
    And the simulation reproduces the scenario's vital-sign behaviour and ranked candidates
    When the trainer exits simulation/training mode
    Then the Display Interface affirmatively returns to a visually dominant live state with no residual simulation indication
```

```gherkin
@ID:RQ_FN_15
Feature: Block Simulation During Live Monitoring
    As a Bedside Clinician I want simulation entry blocked during a live session
    So that a live patient session cannot be accidentally placed into simulation

Rule: The MMSS shall block entry to simulation/training mode during a live monitoring session, requiring an explicit live-vs-simulation confirmation, so that a live patient session cannot be accidentally placed into simulation.

Scenario: Simulation entry blocked during live session
    Given the simulator is running
    And the MMSS is running a live monitoring session with connected sensors
    When a user attempts to enter simulation/training mode
    Then the MMSS blocks entry to simulation/training mode
    And the Display Interface requires an explicit live-vs-simulation confirmation before any change
```

```gherkin
@ID:RQ_FN_16
Feature: Share Data with the Hospital Information System
    As an Emergency Physician I want to share selected vital signs and candidates to the HIS with confirmed read-back
    So that the correct patient's data is sent promptly for a second opinion

Rule: The MMSS shall allow the clinician to select relevant vital signs and ranked diagnostic candidates and share them with the Hospital Information System, requiring a two-step patient/case confirmation with read-back of exactly what will be shared, and shall transmit the confirmed data to the HIS within 1 second of confirmation.

Scenario: Confirmed sharing transmits within 1 second
    Given the simulator is running in live mode
    And the MMSS is running
    And the HIS integration is configured and the HIS endpoint stub is reachable
    And the case identifier is "CASE-12345"
    When the clinician selects the following items to share for case "CASE-12345"
    | item type   | value                  |
    | vital sign  | Heart Rate 72 bpm      |
    | vital sign  | SpO2 98 %              |
    | candidate   | Sepsis (High)          |
    Then the Display Interface presents a two-step patient/case confirmation with read-back of exactly those items for "CASE-12345"
    When the clinician confirms both steps
    Then within 1 second of confirmation the MMSS transmits exactly the confirmed items to the HIS
```

```gherkin
@ID:RQ_FN_17
Feature: Report HIS Transmission Failure Honestly
    As an Emergency Physician I want a clear failure report when HIS sharing fails
    So that I never believe a failed transmission succeeded

Rule: The MMSS shall report a clear failure and not falsely indicate that a case was shared when HIS transmission fails or the HIS is unreachable, and shall require renewed patient/case confirmation before any retry.

Scenario: Unreachable HIS reports a clear failure
    Given the simulator is running in live mode
    And the MMSS is running
    And the HIS endpoint stub is configured to be unreachable (connection refused)
    And the clinician has selected and completed the two-step confirmation for case "CASE-12345"
    When the MMSS attempts to transmit the confirmed data to the HIS
    Then the Display Interface reports a clear transmission failure within 1 second of the failed attempt
    And the Display Interface does not indicate that the case was shared
    And the MMSS requires renewed patient/case confirmation before any retry
```

```gherkin
@ID:RQ_FN_18
Feature: Authenticated Configuration Interface
    As a Clinical / Biomedical Engineer I want a gated configuration interface for device mappings and HIS settings
    So that commissioning is controlled, validated and confirmed before clinical use

Rule: The MMSS shall provide a configuration interface, gated behind authentication and unavailable during live clinical use, through which an authorised engineer can configure each device interface and its device-to-parameter mapping and the HIS integration settings, with MMSS validating and reading back each configuration before it is committed.

Scenario: Authorised engineer configures a device mapping with read-back
    Given the MMSS is not in a live clinical session
    And an authorised engineer is authenticated
    When the engineer maps interface IF_01 to device "ECG Monitor" producing parameter "Heart Rate"
    Then the MMSS validates the configuration and reads back "IF_01 → ECG Monitor → Heart Rate" before committing
    When the engineer confirms the read-back
    Then the MMSS commits the configuration

Scenario: Configuration interface unavailable during live use
    Given the simulator is running in live mode
    And the MMSS is running a live clinical session with connected sensors
    When a user attempts to open the configuration interface
    Then the MMSS keeps the configuration interface unavailable
```

```gherkin
@ID:RQ_FN_19
Feature: Validate Alarm-Threshold Entry Against Safe Range
    As a Clinical / Biomedical Engineer I want threshold and mapping entries validated against the per-parameter safe range
    So that unsafe or invalid values are never committed

Rule: The MMSS shall constrain vital-sign alarm-threshold entry to the per-parameter configurable safe range, reject any threshold or device-to-parameter mapping that is out of range, non-numeric, or otherwise invalid without committing it, surface the reason for rejection, and require explicit confirmation before any valid threshold change is committed.

Scenario Outline: Threshold entries are accepted or rejected per safe range
    Given the MMSS configuration interface is open
    And an authorised engineer is authenticated
    And the safe range for <parameter> is <min> to <max>
    When the engineer enters a threshold of <entry> for <parameter>
    Then the MMSS <outcome> the threshold
    And on rejection the MMSS surfaces the reason and does not commit the value
    And on acceptance the MMSS requires explicit confirmation before committing

    Examples:
    | parameter   | min | max | entry      | outcome  |
    | Heart Rate  | 30  | 250 | 180        | accepts  |
    | Heart Rate  | 30  | 250 | 400        | rejects  |
    | SpO2        | 0   | 100 | non-numeric| rejects  |
    | Temperature | 25  | 45  | 39         | accepts  |
```

```gherkin
@ID:RQ_FN_20
Feature: Access-Controlled Safety-Critical Configuration Log
    As a Clinical / Biomedical Engineer I want safety-critical configuration changes restricted to authorised users and logged
    So that only authorised changes are made and every change can be audited

Rule: The MMSS shall restrict changes to safety-critical configuration parameters (alarm thresholds, device and interface settings) to authenticated, authorised users and record every change in a traceable, access-controlled change log.

Scenario: Authorised change is logged
    Given the MMSS configuration interface is open
    And an authorised engineer is authenticated
    When the engineer commits a change to an alarm threshold
    Then the MMSS records the change in a traceable, access-controlled change log
    And the log entry identifies the user, the parameter, the old and new values, and a timestamp

Scenario: Unauthenticated change is refused
    Given the MMSS configuration interface is open
    And no user is authenticated
    When a user attempts to change a safety-critical configuration parameter
    Then the MMSS refuses the change
```

```gherkin
@ID:RQ_FN_21
Feature: Care Hand-over Session-State Summary
    As a Bedside Clinician I want a hand-over summary of alarm state, thresholds and reviewed candidates that I must acknowledge
    So that no silenced alarm, altered threshold, or dismissed candidate is carried across unseen

Rule: The MMSS shall, at care hand-over, surface a session-state summary of the current alarm/silence state, any non-default alarm thresholds, and which diagnostic candidates were reviewed or dismissed, and shall require the incoming clinician to explicitly acknowledge that session state, keeping any unacknowledged state visibly flagged.

Scenario: Hand-over requires explicit acknowledgement
    Given the simulator is running in live mode
    And the MMSS is running a live monitoring session with all sensors connected
    And the SpO2 alarm is silenced
    And Heart Rate has a non-default threshold of 150 bpm
    And the diagnostic candidate "Hypovolaemia" was dismissed
    When the incoming clinician initiates a care hand-over
    Then the Display Interface shows a session-state summary
    | item                   | state                  |
    | alarm/silence state    | SpO2 alarm silenced    |
    | non-default thresholds | Heart Rate 150 bpm     |
    | dismissed candidates   | Hypovolaemia dismissed |
    And the unacknowledged session state remains visibly flagged
    When the incoming clinician explicitly acknowledges the session state
    Then the Display Interface clears the unacknowledged flag
```

```gherkin
@ID:RQ_FN_22
Feature: Time-Bounded Source-Specific Alarm Silencing
    As a Bedside Clinician I want alarm silencing to be time-bounded and source-specific with automatic re-annunciation
    So that a genuine unresolved critical alarm is never permanently suppressed

Rule: The MMSS shall permit only time-bounded, source-specific alarm silencing — never an indefinite or global mute — display a persistent "silenced — re-annunciates in mm:ss" indication, and automatically re-annunciate the alarm if the underlying condition remains unresolved when the silence period expires.

Scenario: Silenced alarm re-annunciates when the condition persists
    Given the simulator is running in live mode
    And the MMSS is running
    And the simulator supplies Heart Rate 165 bpm, breaching the configured 150 bpm threshold
    And an active Heart Rate alarm is present
    When the clinician silences the Heart Rate alarm for a bounded period of 60 seconds
    Then the Display Interface shows a persistent "silenced — re-annunciates in mm:ss" indication on Heart Rate and in the status strip
    And no indefinite or global mute is offered
    When the 60-second silence period expires while Heart Rate is still 165 bpm (unresolved)
    Then within 1 second of expiry the MMSS automatically re-annunciates the Heart Rate alarm
```

```gherkin
@ID:RQ_FN_23
Feature: Escalate Repeatedly Silenced Critical Alarm
    As a Bedside Clinician I want escalation when the same unresolved critical alarm is repeatedly silenced
    So that no critical alarm can be left permanently silenced

Rule: The MMSS shall escalate when the same unresolved critical alarm is repeatedly silenced, such that no critical alarm can be left permanently silenced.

Scenario: Repeated silencing triggers escalation
    Given the simulator is running in live mode
    And the MMSS is running
    And the simulator supplies SpO2 80 %, breaching the configured 90 % threshold
    And an unresolved critical SpO2 alarm is present
    When the clinician silences the SpO2 alarm 3 consecutive times while SpO2 remains 80 % (unresolved)
    Then on the 3rd silence the MMSS escalates the SpO2 alarm by shortening the silence window, raising priority/audibility, or surfacing the silenced state more prominently
    And the SpO2 alarm is not left permanently silenced
```

```gherkin
@ID:RQ_FN_24
Feature: Validate HIS Integration Settings
    As a Clinical / Biomedical Engineer I want HIS integration settings validated with a connectivity test before they are marked ready
    So that an unvalidated or unreachable HIS integration is never presented as ready

Rule: The MMSS shall validate HIS integration settings on configuration, including a connectivity test, and shall not mark the integration as ready for clinical use until the settings are valid and the endpoint is reachable.

Scenario: Valid and reachable HIS settings are marked ready
    Given the MMSS configuration interface is open
    And an authorised engineer is authenticated
    And the HIS endpoint stub is configured to be reachable and to accept the connectivity test
    When the engineer enters valid HIS integration settings (host, port, protocol) and runs the connectivity test
    Then the connectivity test passes
    And the MMSS marks the HIS integration as ready for clinical use

Scenario: Unreachable HIS endpoint is not marked ready
    Given the MMSS configuration interface is open
    And an authorised engineer is authenticated
    And the HIS endpoint stub is configured to be unreachable (connection refused)
    When the engineer enters HIS integration settings and runs the connectivity test
    Then the connectivity test fails
    And the MMSS does not mark the HIS integration as ready for clinical use
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
