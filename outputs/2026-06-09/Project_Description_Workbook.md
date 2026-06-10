---
Executed by: orchestration (CLAUDE.md)
Flow: flows/expectationeering-flow/flow.md
Templates: flows/expectationeering-flow/expectationeering-workbook.md
Inputs: inputs/
Date: 2026-06-09
---

# Expectationeering Workbook

**Product**: Mobile Monitoring Software Solution (MMSS)
**Date**: 2026-06-09
**Workshop Team**: User Stakeholder, Customer Stakeholder, Business Stakeholder, Regulatory Stakeholder, Product Owner, System Architect, Usability Validation, Development Lead, Verification Lead, Quality Assurance

---

# Introduction

This workbook captures the expectations and requirements for the product, from informal stakeholder expectations through to verifiable system requirements. Every requirement item has a unique identifier, starting with the stakeholder expectations, and each item traces to the upstream item it is derived from.

## Intended users of the document

This workbook is intended for the product development and assurance community responsible for the MMSS: the product owner and business stakeholders, system architects and developers, usability and human-factors engineers, verification and validation engineers, quality and regulatory affairs, and the clinical stakeholders consulted throughout. It serves as the shared requirements baseline and traceability record from informal stakeholder expectations through to verifiable system requirements.

## Scope of the document

The product in scope is the Mobile Monitoring Software Solution (MMSS) — regulated medical device software that turns an existing portable patient monitor into an active clinical decision-support tool. The workbook covers the requirement chain from the problem domain and stakeholder expectations through to verifiable system requirements and their BDD verification specifications. Hardware design, internal architecture decomposition, detailed design, and per-item allocation are out of scope; physical components and the diagnostic AI are treated as fixed, externally-supplied elements accessed through defined interfaces.

---

# Application

## Stakeholders (INFORMAL)

The stakeholder level is the start of the requirement approach. It captures the problem to be solved and the expectations of each stakeholder in a product-agnostic ("product-free") way.

### Problem

#### Domain Description

The domain is the real-time monitoring of critically ill or unstable patients in critical-care and pre-hospital settings — intensive care units, emergency rooms, and mobile medical units such as ambulances and on-scene emergency response. In this domain, trained medical professionals (paramedics, emergency physicians, ICU/ER nurses) must continuously track a patient's vital signs from a set of non-invasive measurement devices and act quickly on the patient's changing condition, frequently under time pressure and in noisy, moving, poorly lit, or chaotic environments where attention is split across multiple tasks and patients.

Beyond passive observation of vital signs, the domain increasingly extends to clinical decision support: aiding the clinician toward a working diagnosis early in the patient encounter, when information is incomplete and expert consultation may be unavailable. Because monitoring failures, missed alarms, or misleading diagnostic guidance can directly cause patient harm or death, every solution in this domain is a safety-critical, regulated medical device. It is therefore subject to the full body of applicable medical-device law and harmonised standards — software lifecycle rigour (e.g. IEC 62304), risk management (e.g. ISO 14971), usability engineering (e.g. IEC 62366), alarm safety (e.g. IEC 60601-1-8), quality management (e.g. ISO 13485), data-protection law (e.g. GDPR/HIPAA class), and post-market surveillance obligations.

The domain also has a commercial and organisational dimension: solutions are bought by healthcare-provider organisations that weigh clinical value against total cost of ownership, interoperability with the existing care and IT estate, vendor dependability, and institutional liability; and they are placed on the market by legal manufacturers who must demonstrate conformity to competent authorities and notified bodies before and after launch. Any product in this domain — the product under development and its competitors alike — solves the same underlying problem: delivering trustworthy, timely, safe, and lawfully marketable critical-care monitoring with diagnostic support.

#### Actual State

Today, critical-care and pre-hospital monitoring in this domain is dominated by patient monitors that acquire and display vital signs from non-invasive measurement devices and raise alarms when a measured value crosses a threshold. They give clinicians a real-time window onto the patient's condition, but they are essentially passive: they show numbers and waveforms and signal abnormal readings, leaving all interpretation and diagnosis to the clinician.

**Pros**

- Continuous, real-time acquisition and at-a-glance display of vital signs from established measurement devices is mature and widely deployed.
- Threshold-based alarming for abnormal vital signs is well understood and governed by recognised alarm-safety standards.
- The clinician retains full diagnostic and treatment authority, so responsibility for patient care rests unambiguously with a qualified professional.
- The regulatory, quality, and risk-management framework for such devices is established and well-trodden by manufacturers.
- An installed base of monitors, measurement devices, and clinical IT exists, representing significant prior capital investment.

**Cons**

- Monitoring is passive: the clinician must form a diagnosis unaided, which is slow and error-prone under time pressure, in chaotic settings, or when no colleague can be consulted.
- No early, ranked diagnostic guidance is offered alongside the raw vital signs to shorten the time to a working diagnosis.
- Sensor disconnection, misplacement, or unreliable readings may go undetected, risking decisions made on false data.
- When automated guidance is absent or cannot be produced in time, the clinician has no clear, timely signal to fall back on their own assessment rather than wait.
- Diagnostic support, where it exists, may not adequately explain its reasoning or confidence, encouraging either mistrust or unsafe automation bias.
- Cross-environment use (fixed clinical and mobile/pre-hospital) often requires different equipment, increasing fleet complexity and cost.
- Data exchange with hospital information systems for second opinion and handover is frequently bespoke, costly, or absent.
- Realistic, risk-free training on the monitoring is limited, so clinicians may first encounter unfamiliar behaviour on a real patient.

#### Desired State

The desired state keeps everything good about today's monitoring and adds active, trustworthy clinical decision support. The monitoring still acquires and displays vital signs in real time and alarms on abnormal conditions, but it now also presents ranked, real-time diagnostic candidates alongside the raw data — converging quickly toward a working diagnosis — while keeping the clinician firmly in control and the device demonstrably safe and lawful to deploy.

**Pros (retained from the actual state)**

- Continuous, real-time acquisition and at-a-glance display of vital signs from established measurement devices.
- Recognised, standards-conformant alarming for abnormal vital signs.
- The clinician retains final diagnostic and treatment authority.
- An established regulatory, quality, and risk-management framework is satisfied.
- Compatibility with the existing installed base of monitors, measurement devices, and clinical IT, protecting prior investment.

**Pros (newly added)**

- Ranked, real-time diagnostic candidates are presented alongside vital signs, converging early so the clinician reaches a working diagnosis faster, even without a colleague to consult.
- Each diagnostic suggestion carries its reasoning and confidence, so the clinician can judge whether to trust it and automation bias is mitigated.
- The clinician is clearly and promptly told when a diagnosis cannot be produced in the expected time, so they can fall back on their own assessment without waiting indefinitely.
- Sensor disconnection, misplacement, and unreliable readings are detected and signalled distinctly, so decisions are not made on false data.
- The monitoring is ready for use within seconds of switching on and is operable one-handed and glanceably in mobile, noisy, poorly lit conditions.
- A realistic, risk-free training mode lets clinicians build competence before using the device on a real patient.
- Patient data and diagnostic findings can be shared with hospital information systems over recognised interoperability standards for second opinion and smooth handover.
- One solution fits both fixed and mobile/pre-hospital settings, reducing fleet complexity and total cost of ownership.
- The solution is developed and maintained under a controlled, standards-conformant lifecycle with audit-ready evidence, defensible residual risk, validated diagnostic performance, protected patient data, and credible post-market surveillance — making it lawfully marketable, safe to update, and defensible to governance and authorities.

**Cons (newly introduced, to be controlled)**

- Adding AI-driven diagnostic support introduces new clinical-safety, validation, evidence, and liability burdens that must be reduced to a defensible, documented residual level with independent safeguards for safety-critical functions.
- Greater capability and interoperability increase development, integration, and data-protection effort, which must be contained within budget, time-to-market, and the manufacturer's existing competencies and capacity.

#### Identified Gaps (DC_*)

The design changes needed to move from the actual state to the desired state.

| ID | Description |
|----|-------------|
| DC_01 | Provide continuous, real-time acquisition and at-a-glance display of patient vital signs from the connected non-invasive measurement devices, available within seconds of switching the monitoring on, so the clinician can act on the patient's real condition without start-up delay. |
| DC_02 | Add active diagnostic decision support that presents ranked, real-time diagnostic candidates alongside the raw vital signs and converges early toward a working diagnosis, going beyond passive vital-signs display — using a commercially validated, ready-made diagnostic capability rather than a proprietary one in the first release. |
| DC_03 | Present each diagnostic suggestion with its supporting reasoning and confidence, and frame and label the output as decision support that informs rather than replaces the clinician, who retains final diagnostic and treatment authority — keeping residual clinical risk defensible and mitigating automation bias. |
| DC_04 | Clearly and promptly signal to the clinician when a diagnostic result cannot be produced within the expected time, so they can fall back on their own assessment instead of waiting indefinitely. |
| DC_05 | Detect abnormal vital-sign conditions and raise immediate, unmistakable, distinguishable alarms that conform to recognised alarm-safety practice, signalling clinically significant conditions without unsafe alarm fatigue or missed-alarm risk. |
| DC_06 | Detect and clearly warn the clinician when a sensor is disconnected, misplaced, or producing unreliable readings, so decisions are not made on false or missing data. |
| DC_07 | Make the monitoring operable one-handed and glanceably and reliable in adverse conditions (movement, poor light, noise), supported by a usability-engineering process that identifies and mitigates foreseeable use errors so it can be operated safely by its intended users. |
| DC_08 | Provide a realistic, risk-free training mode together with the training provisions appropriate to the device's safety class, so clinicians build competence before using the monitoring on a real patient and the deployed fleet is competently operated. |
| DC_09 | Enable sharing of patient data and diagnostic findings with hospital information systems over recognised healthcare interoperability standards (e.g. HL7/FHIR class), so the clinician can obtain a second opinion and hand over care smoothly and the buyer avoids bespoke integration cost. |
| DC_10 | Make a single monitoring solution fit both fixed clinical settings and the constraints of mobile and pre-hospital deployment, so providers can standardise across care environments and reduce fleet complexity. |
| DC_11 | Ensure the monitoring integrates with the buyer's existing patient monitors, measurement devices, and clinical IT estate, protecting prior capital investment and avoiding costly rip-and-replace. |
| DC_12 | Demonstrate readiness for regulatory clearance and lawful market access in the target markets as a precondition of release, evidenced by a complete, audit-ready technical file, so the device may be lawfully deployed and reimbursed without market-access delay. |
| DC_13 | Deliver a favourable total cost of ownership across licensing, deployment, support, and lifecycle updates, within the manufacturer's committed budget, cost targets, and time-to-market window, so the investment is justified for the buyer and the business case stays viable. |
| DC_14 | Achieve demonstrated high reliability and availability for continuous critical-care use, so the monitor is not unavailable at the point of care and clinical downtime is avoided. |
| DC_15 | Make the solution producible, serviceable, and supportable at the required scale and quality with the manufacturer's existing competencies and capacity, providing dependable support, maintenance, and lifecycle updates throughout the product's service life. |
| DC_16 | Reduce the clinical risk of the monitoring — covering AI mis-diagnosis, false or missed alarms, sensor-fault propagation, and use error — to an acceptable, documented residual level through a complete lifecycle risk-management process with verified controls and independent safeguards for safety-critical functions, providing the validated-safety and liability assurance buyers and authorities require. |
| DC_17 | Develop, maintain, and change the monitoring software under a documented, standards-conformant software lifecycle with a justified, traceable safety classification, so it can be safely updated, patched, and supported without re-incurring full re-validation each change and is engineered to a rigour commensurate with the harm it can cause. |
| DC_18 | Generate and retain design-control, quality-management, and risk-management evidence as a complete, current, audit-ready technical file under a certified quality management system, so notified-body, authority, and internal-governance audits can be satisfied and the declaration of conformity defended. |
| DC_19 | Make post-market surveillance, vigilance, complaint handling, and incident reporting feasible to operate, with end-to-end traceability from a field event back to the responsible design element, so emerging safety signals are detected, reported within mandated timelines, and corrected through field safety actions where required. |
| DC_20 | Architect the solution for reuse and configurability across deployment settings and future product lines, so the development investment yields maximum return and the portfolio can be extended at lower cost. |
| DC_21 | Produce documented clinical evidence and validation of the diagnostic decision-support performance — including the validation status, intended-use boundaries, performance characteristics, and known limitations of any off-the-shelf AI component — confirming the diagnostic output is safe and effective for its stated indication and patient population. |
| DC_22 | Acquire, process, display, and exchange personal health data in conformance with applicable data-protection and privacy law (e.g. GDPR/HIPAA class) and secure interoperability practice, protecting patient confidentiality, integrity, and rights throughout the data flow. |
| DC_23 | Provide compliant labelling and instructions for use appropriate to the device's safety class, so intended users understand its capabilities, limitations, and safe operation and mandatory information-for-safety obligations are met. |

### Expectations

Stakeholder expectations are written "product-free": they apply to any product in the problem domain, including competitors. Format: *The \<stakeholder\> wants \<expectation\> to \<benefit driver\>.*

#### User Expectations (UE_*)

**Stakeholder**: Critical-Care Clinician

The frontline trained medical professional (paramedic, emergency physician, ICU/ER nurse) who connects the patient, watches the vital signs, and decides on treatment — frequently in time-pressured, noisy, mobile, or chaotic settings (ambulance, accident scene, ER, ICU) where they must act fast on incomplete information, often with their hands occupied and their attention split across multiple tasks and patients.

| ID | Expectation | Traces |
|----|-------------|--------|
| UE_01 | The clinician wants to see the patient's current vital signs at a glance the moment a sensor is connected to act on the patient's real condition without delay. | DC_01 |
| UE_02 | The clinician wants ranked, real-time diagnostic suggestions presented alongside the raw vital signs to reach a working diagnosis faster, especially when they cannot consult a colleague. | DC_02 |
| UE_03 | The clinician wants to be alerted immediately and unmistakably when a vital sign crosses an abnormal threshold to intervene before the patient deteriorates. | DC_05 |
| UE_04 | The clinician wants to be warned when a sensor is disconnected, misplaced, or producing unreliable readings to avoid trusting or acting on false data. | DC_06 |
| UE_05 | The clinician wants the monitoring to be ready for use within seconds of switching it on at the bedside to start caring for the patient without waiting through start-up. | DC_01 |
| UE_06 | The clinician wants to understand why a diagnostic suggestion was made and how confident it is to keep clinical judgement in control and decide whether to trust the suggestion. | DC_03 |
| UE_07 | The clinician wants to operate the monitoring one-handed, glanceably, and reliably in moving vehicles, poor light, and noise to keep working when conditions are far from ideal. | DC_07 |
| UE_08 | The clinician wants to be clearly told if a diagnosis cannot be produced within the expected time to fall back on their own assessment instead of waiting indefinitely. | DC_04 |
| UE_09 | The clinician wants to practise with the monitoring in a realistic, risk-free training mode to build competence and avoid misreading the device on a real patient. | DC_08 |
| UE_10 | The clinician wants to share the patient's data and diagnostic findings with the receiving hospital to secure a second opinion and a smooth handover of care. | DC_09 |

#### Market Expectations (ME_*)

**Stakeholder**: Healthcare Provider Procurement (Hospital / EMS)

The buying organisation that acquires monitoring solutions for critical-care settings — hospital procurement and clinical engineering departments, ambulance services, and EMS fleet operators. They evaluate and select on behalf of the clinicians who will use the product, balancing clinical value against total cost of ownership, regulatory market access, integration with the existing IT and care estate, vendor reliability, and institutional liability. They sign the purchase only when the solution is demonstrably safe to deploy, affordable to own and operate, and defensible to their own governance, accreditation, and risk-management boards.

| ID | Expectation | Traces |
|----|-------------|--------|
| ME_01 | The procurement organisation wants a critical-care monitoring solution that is cleared for sale and use in its target markets before purchase to ensure the device may be lawfully deployed and reimbursed without market-access delay. | DC_12 |
| ME_02 | The procurement organisation wants a favourable total cost of ownership across licensing, deployment, support, and lifecycle updates to justify the investment against budget and demonstrate value for money. | DC_13 |
| ME_03 | The procurement organisation wants the monitoring solution to integrate with its existing patient monitors, measurement devices, and clinical IT estate to protect prior capital investment and avoid costly rip-and-replace. | DC_11 |
| ME_04 | The procurement organisation wants the monitoring solution to exchange patient data with hospital information systems over recognised healthcare interoperability standards (e.g. HL7/FHIR class) to fit its records and handover workflows without bespoke integration cost. | DC_09 |
| ME_05 | The procurement organisation wants demonstrated high reliability and availability in continuous critical-care use to avoid clinical downtime and the operational risk of an unavailable monitor at the point of care. | DC_01, DC_14 |
| ME_06 | The procurement organisation wants dependable vendor support, maintenance, and clinician training to be available throughout the product's service life to keep the deployed fleet safe, current, and competently operated. | DC_08, DC_15 |
| ME_07 | The procurement organisation wants the solution to offer diagnostic decision support beyond passive vital-signs display to differentiate it from baseline monitors and justify replacing or upgrading existing equipment. | DC_02 |
| ME_08 | The procurement organisation wants clear assurance of clinical safety, validated performance, and the supplier's liability and quality commitments to defend the purchase to its governance and risk boards and limit institutional exposure. | DC_16 |
| ME_09 | The procurement organisation wants the solution to fit the constraints of mobile and pre-hospital deployment as well as fixed clinical settings to standardise on one solution across its care environments and reduce fleet complexity. | DC_10 |

#### Business Expectations (BE_*)

**Stakeholder**: Legal Manufacturer

The organisation legally responsible for designing, producing, and placing the critical-care monitoring solution on the market, and for it throughout its lifecycle. It speaks for its internal departments — Executive/Strategy, Legal & Compliance, Finance, Operations & Manufacturing, R&D, Quality Management, Regulatory Affairs, Sales & Commercial, Customer Support & Service, and HR. Its expectations are shaped by organisational strategy, budget and capacity limits, liability exposure, the quality and regulatory obligations it must carry as legal manufacturer, and what it can realistically produce, support, and stand behind over the product's service life.

| ID | Expectation | Traces |
|----|-------------|--------|
| BE_01 | The legal manufacturer wants a critical-care monitoring solution that is demonstrably ready for regulatory approval in its target markets as a precondition of release to make lawful market entry possible and protect planned revenue from market-access delay. | DC_12 |
| BE_02 | The legal manufacturer wants the residual clinical risk of AI-driven diagnostic support to be reduced to a defensible, documented level — with the clinician retaining decision authority and independent safeguards for safety-critical functions — to keep its product-liability exposure controlled and acceptable. | DC_03, DC_16 |
| BE_03 | The legal manufacturer wants to incorporate a commercially validated, ready-made diagnostic AI capability rather than develop a proprietary model in the first release to limit its own validation, evidence, and liability burden and shorten the path to market. | DC_02 |
| BE_04 | The legal manufacturer wants the solution to be developed and maintained under a controlled, standards-conformant software lifecycle (e.g. IEC 62304 commensurate with its safety class) to ensure it can be safely updated, patched, and supported over its service life without re-incurring full re-validation cost each change. | DC_17 |
| BE_05 | The legal manufacturer wants design-control, quality-management (e.g. ISO 13485 class), and risk-management evidence to be generated and retained as a complete, audit-ready technical file to satisfy notified-body, authority, and internal-governance audits and to defend its declaration of conformity. | DC_18 |
| BE_06 | The legal manufacturer wants the solution delivered within its committed budget, cost targets, and time-to-market window to keep the business case viable and protect the planned margin and portfolio investment priorities. | DC_13 |
| BE_07 | The legal manufacturer wants post-market surveillance, complaint handling, and end-to-end traceability from field event back to the responsible design item to be feasible to operate to meet its post-market legal obligations and contain the cost and exposure of field issues. | DC_19 |
| BE_08 | The legal manufacturer wants the solution to be producible and serviceable at the required scale and quality with the organisation's existing competencies, capacity, and supply arrangements to deliver and support the deployed fleet reliably without overrunning operational capability. | DC_15 |
| BE_09 | The legal manufacturer wants the solution architected for reuse and configurability across deployment settings and future product lines to maximise return on the development investment and reduce the cost of extending the portfolio. | DC_20 |

#### Regulatory Expectations (RE_*)

**Stakeholder**: Competent Authority / Notified Body

The regulatory system that decides whether a medical device may lawfully be placed on, and remain on, the market — national competent authorities (e.g. FDA, EMA national authorities, TGA, Swissmedic, PMDA, CDSCO), the notified bodies that assess technical documentation and issue conformity certificates for regulated software-as-a-medical-device, the standards organisations whose published standards (ISO/IEC/CEN) define the presumption of conformity, and the post-market surveillance and vigilance authorities that monitor devices in the field. This stakeholder does not advocate for the product; it holds it to account against applicable law, harmonised standards, and enforcement practice. It grants, defers, or refuses market access on the basis of demonstrated conformity, validated safety and clinical performance, an auditable quality system, and credible post-market obligations — applying these criteria equally to any product or competitor seeking access to the same market.

| ID | Expectation | Traces |
|----|-------------|--------|
| RE_01 | The competent authority wants any diagnostic-support medical device software to be developed, maintained, and changed under a documented, standards-conformant software lifecycle (e.g. IEC 62304) with its safety classification justified by a traceable rationale to confirm the software is engineered to a rigour commensurate with the harm it can cause before market access is granted. | DC_17 |
| RE_02 | The competent authority wants a complete risk-management process (e.g. ISO 14971) applied across the device lifecycle — explicitly addressing AI mis-diagnosis, false or missed alarms, sensor-fault propagation, and use error — with each hazard reduced to an acceptable residual level through verified risk controls, including independent safeguards for safety-critical functions, to ensure the benefit-risk balance is favourable and defensible. | DC_16 |
| RE_03 | The competent authority wants a usability engineering process (e.g. IEC 62366) that identifies use-related hazards and demonstrates through formative and summative evaluation that foreseeable use errors are mitigated to ensure the device can be operated safely by its intended users in its intended use environments without introducing clinical harm. | DC_07 |
| RE_04 | The competent authority wants documented clinical evidence and validation of the AI-driven diagnostic decision-support performance — including the validation status, intended-use boundaries, performance characteristics, and known limitations of any off-the-shelf AI component — to confirm the diagnostic output is safe and effective for its stated medical indication and patient population. | DC_21 |
| RE_05 | The competent authority wants the diagnostic output to be designed and labelled as decision support that informs rather than replaces the qualified clinician, with the clinician retaining final diagnostic and treatment authority, to ensure ultimate responsibility for patient care remains with a competent professional and automation bias is mitigated. | DC_03 |
| RE_06 | The competent authority wants any alarm and alarm-system behaviour to conform to recognised alarm-safety standards (e.g. IEC 60601-1-8) so that clinically significant conditions and technical faults are signalled correctly, distinguishably, and without unsafe alarm fatigue or missed-alarm risk. | DC_05 |
| RE_07 | The competent authority wants personal health data acquired, processed, displayed, or exchanged with hospital systems to be handled in conformance with applicable data-protection and privacy law (e.g. GDPR / HIPAA class) and secure interoperability practice to protect patient confidentiality, integrity, and rights throughout the data flow. | DC_22 |
| RE_08 | The competent authority wants the manufacturer to operate a certified quality management system (e.g. ISO 13485) and to maintain a complete, current, audit-ready technical file or design dossier to enable the notified body and authority to assess conformity and to support the declaration of conformity and lawful market placement. | DC_12, DC_18 |
| RE_09 | The competent authority wants the device to carry compliant labelling, instructions for use, and demonstrable user-training provisions appropriate to its safety class to ensure intended users understand the device's capabilities, limitations, and safe operation, and to satisfy mandatory information-for-safety obligations. | DC_08, DC_23 |
| RE_10 | The competent authority wants a credible post-market surveillance, vigilance, and incident-reporting system with end-to-end traceability from a field event back to the responsible design element to ensure emerging safety signals are detected, reported within mandated timelines, and corrected through field safety actions or recalls where required. | DC_19 |

### Ideal Product Model (KA_*)

The Ideal Product Model is the blueprint that aligns stakeholder expectations with product capabilities — the key proposition attributes, their priority, feasibility, and risk.

| ID | Benefit Driver | Expectation | Proposition Attributes | Superior to | Priority | Feasible | Risk | Rationale |
|----|----------------|-------------|------------------------|-------------|----------|----------|------|-----------|
| KA_01 | Act on the patient's real condition instantly | UE_01, UE_05, ME_05 | Continuous real-time acquisition, low-latency processing, and at-a-glance presentation of multi-parameter vital signs from the connected non-invasive measurement devices, with end-to-end acquisition-to-display latency in the sub-second range and readiness for use within a few seconds of power-on. | A passive monitor that displays vital signs but may take longer to become usable after power-on, with no guarantee of glanceable readiness at the bedside. | High | Yes | Low — acquisition and display is an established capability and the latency and activation targets (sub-second display, sub-10-second activation) are comfortably achievable on a real-time-capable embedded platform; the only material exposure is the real-time integration effort across multiple device interfaces (R_03), addressed by early prototyping and ICD definition. | This is the baseline clinical value of the domain; without immediate, trustworthy vital-signs presentation the clinician cannot act on the patient's true state and every downstream capability is moot. The latency and activation budgets are well within reach of the assumed real-time-OS embedded host. |
| KA_02 | Reach a working diagnosis faster, even alone | UE_02, ME_07, BE_03 | Active diagnostic decision support that integrates a commercially validated, off-the-shelf diagnostic AI capability and presents its ranked diagnostic candidates alongside the raw vital signs, rendering each result promptly on receipt; convergence toward a working diagnosis is the responsibility of the external diagnostic capability, while the product owns reliable acquisition-to-AI feed and prompt candidate presentation. | Passive vital-signs display that leaves all interpretation to the clinician and offers no ranked diagnostic guidance. | High | Partial | High — the dominant exposures are regulatory clearance of the AI-driven diagnostic function (R_01) and AI model validation complexity (R_02), both substantially mitigated by mandating an off-the-shelf, already-validated capability for the first release; diagnostic accuracy and time-to-converge are properties of that external capability, not of the integrating product, so the product-level risk is concentrated in real-time interface integration (R_03) rather than algorithm performance. **Business/liability note**: reliance on an off-the-shelf AI does not transfer product liability away from the legal manufacturer — as the entity placing the integrated device on the market it remains accountable for the diagnostic output's intended-use boundaries and fitness for the indication; this creates a supplier-dependency exposure (continuity of supply, the supplier's own validation maintenance, model updates/versioning, and contractual flow-down of validation evidence) that must be controlled by contract and supplier qualification or it becomes an uncontained liability and market-continuity risk. | This is the central differentiator that turns passive monitoring into active decision support and the core reason a buyer would upgrade. Using a mandated off-the-shelf validated capability is a deliberate de-risking choice: it removes proprietary-model validation from the programme's critical path and bounds the product's responsibility to integration and presentation, limiting Finance's validation spend and Regulatory's evidence burden. The early-convergence target is a budget on the external capability, not on the integrating product. The strategic trade is faster, cheaper market entry in exchange for a managed dependency on the AI supplier, which the business accepts only with enforceable contractual safeguards on validation evidence, change notification, and supply continuity. |
| KA_03 | Keep clinical judgement in control and trust the output | UE_06, RE_05, BE_02 | Diagnostic candidates presented as ranked, confidence-bearing suggestions whose supporting reasoning and confidence are absorbable at a glance under time pressure (not requiring the clinician to stop and read at length), framed and labelled by design as decision support that informs rather than replaces the clinician, who retains final diagnostic and treatment authority and is never prevented from acting on their own judgement ahead of or against a suggestion. | Diagnostic guidance that offers little or no explanation or confidence, encouraging either mistrust or unsafe automation bias. | High | Partial | High — clinician misinterpretation of AI candidates (R_05) is rated a critical hazard: it depends both on what reasoning and confidence the off-the-shelf capability exposes (not under the product's control) and on disciplined presentation and labelling that resist automation bias; mitigated by clear decision-support framing, presentation design, and the mandated training mode (KA_08). **Business/liability note**: clinician-in-control is the central liability firewall for the legal manufacturer — it is what keeps ultimate responsibility for patient care with a qualified professional and the device defensible as decision support rather than an autonomous diagnostic agent. If the off-the-shelf capability exposes too little reasoning or confidence to make that framing credible, the manufacturer cannot adequately discharge this liability control, so the depth and labelling fidelity of the supplied output is itself a contractual/supplier-qualification requirement, not merely a design constraint. | Trust and controlled liability hinge on transparency and on the clinician staying in control; without reasoning, confidence, and unambiguous decision-support framing the diagnostic output is neither safe to rely on nor defensible to authorities, and the misinterpretation hazard escalates to critical patient impact. The decision-support framing is the manufacturer's primary defence against product-liability claims arising from a wrong AI candidate, so Legal & Compliance treat it as non-negotiable. Feasibility is Partial because the depth of available reasoning/confidence is bounded by the external capability and must be secured from the supplier. |
| KA_04 | Fall back on own assessment without waiting | UE_08 | Clear, prompt signalling to the clinician when a diagnostic result cannot be produced within the expected convergence time, delivered through two independent paths so the cue does not depend on the diagnostic path that has failed to converge. | Solutions that go silent or stall when no result is available, giving the clinician no timely cue to proceed unaided. | High | Yes | Low — diagnosis-timeout-not-communicated (R_06) is a critical hazard but is rated low probability because two independent notifications cover it: the external diagnostic capability raises its own audible notification on the convergence-time-out, and the product additionally shows a timeout indication, leaving no residual single-point exposure on the product side. | Prevents treatment delay when guidance cannot be produced in time. The two-minute convergence target is a budget on the external diagnostic capability, not on the product; the safety value here is the redundant, independent timeout notification that keeps the clinician acting rather than waiting on an absent result. |
| KA_05 | Intervene before the patient deteriorates | UE_03, RE_06 | Detection of abnormal vital-sign conditions with immediate, unmistakable, distinguishable alarms — clear about which parameter and how urgent — presented within the sub-second display budget after detection, perceptible in noisy and mobile conditions, and conforming to recognised alarm-safety practice, with alarming realised as a safety-critical function with independent safeguards so a single fault cannot suppress a clinically significant alarm. | Threshold alarming that may be indistinct, prone to fatigue, or not fully aligned with recognised alarm-safety practice. | High | Yes | Medium — the sub-second alarm-display latency is readily met; the residual effort is alarm-safety-standard conformance, avoiding alarm fatigue through human-factors design, and engineering the independent-safeguard architecture that justifies the Class C-to-B safety mitigation. | Timely, trustworthy alarming is essential to act before deterioration and is a regulated, safety-critical expectation of every product in the domain; the independence of the alarm safeguard is what underpins the mitigated safety classification. |
| KA_06 | Avoid acting on false or missing data | UE_04 | Distinct, clearly differentiated warning — readily distinguishable from a genuine clinical alarm so a sensor fault is not mistaken for real patient deterioration (or vice versa) — when a sensor is disconnected, misplaced, or producing unreliable readings, with the affected parameter no longer presented as if it were trustworthy; disconnection inferred from loss of input over a short inactivity window and misplacement/unreliability surfaced from the measurement device's own fault signalling at the interface, presented within the sub-second display budget. | Monitoring where sensor disconnection, misplacement, or unreliable readings may go undetected, risking decisions on false data. | High | Partial | High — sensor misplacement not detected (R_04) is a critical hazard and connection failure not detected (R_07) a critical one; feasibility is Partial because reliable misplacement detection depends on the measurement devices auto-detecting and reporting it at the interface (outside the product's control), whereas disconnection detection from input inactivity and distinct fault presentation are squarely within the product and well-bounded, supported by the devices' own independent audible alarms as a safeguard. | Sensor-fault propagation is a critical hazard: a wrong or absent reading silently trusted can drive a wrong diagnosis or a missed deterioration, so distinct, prompt fault signalling — and reliance on device-side detection for misplacement — is indispensable. |
| KA_07 | Keep working when conditions are far from ideal | UE_07, RE_03 | One-handed, glanceable operation that stays legible and reliable in movement, poor light, and noise, underpinned by a usability-engineering process that identifies and mitigates foreseeable use errors through formative and summative evaluation. | Interfaces optimised for fixed, calm clinical settings that are hard to operate one-handed or glanceably in mobile, noisy, poorly lit conditions. | High | Yes | Medium — the interaction design is achievable, but generating summative usability-validation evidence for safety-critical interactions in the mobile environment requires dedicated human-factors effort and is the basis for mitigating use-related hazards including clinician misinterpretation (R_05). | Pre-hospital and mobile use is a defining environment of the domain; usability under adverse conditions is both a clinical-safety and a market-fit necessity, and the usability-engineering evidence is a precondition of the safety case. |
| KA_08 | Build competence before treating a real patient | UE_09, ME_06, RE_09 | A realistic, risk-free simulated training mode plus the training and labelling provisions appropriate to the device's safety class, with unambiguous, fail-safe separation between training and live clinical operation — including a persistent, glanceable indication of which mode is active at all times — so simulated data can never be mistaken for a real patient and a clinician returning to a device cannot unknowingly treat a live patient in training mode. | Limited or absent risk-free training, so clinicians may first encounter unfamiliar device behaviour on a real patient. | High | Yes | Medium — a simulated training mode is well within reach technically, but because it is the *named* risk-control mitigation for the critical clinician-misinterpretation hazard (R_05) it becomes part of the safety case and must be developed, verified, and documented to that rigour; the fail-safe training/live mode separation is itself a safety-critical requirement (a training scenario mistaken for a real patient is a new critical hazard), and the supplier's clinician-training provision over the service life (ME_06) is an ongoing organisational commitment for Customer Support and HR. | A mandated training mode is the named mitigation for clinician misinterpretation of AI candidates, so from a liability standpoint it is not an optional convenience feature but a documented risk control the manufacturer must stand behind; it reduces use-error before live use, supports safe fleet operation, and helps satisfy the training-provision and information-for-safety obligations for the safety class. Priority is raised to High because its omission directly weakens the safety case for a critical hazard and the device's defensibility to authorities. |
| KA_09 | Secure a second opinion and smooth handover | UE_10, ME_04 | Standards-based, secure exchange of patient data and diagnostic findings with hospital information systems over recognised healthcare interoperability standards (e.g. HL7/FHIR class), delivering findings within the sub-second outbound budget and fitting existing records and handover workflows. | Bespoke, costly, or absent data exchange with hospital systems for second opinion and handover. | Medium | Partial | Medium — the interoperability protocol is not yet fixed (HL7/FHIR to be confirmed, ICDs still to be defined) and this exchange sits within the broader real-time/connectivity integration challenge (R_03); conformance plus secure handling of personal health data add integration effort that is bounded once the ICD is settled. | Standards-based data sharing enables second opinion and continuity of care while sparing the buyer bespoke integration cost. Feasibility is Partial chiefly because the protocol and interface contract are still open, not because the capability is in doubt. |
| KA_10 | Standardise across care environments | ME_09, ME_03 | A single monitoring solution whose behaviour and interfaces fit both fixed clinical settings and mobile/pre-hospital constraints, integrating through defined interface contracts with the buyer's existing monitors, measurement devices, and clinical IT estate across the mandated set of six device types. | Different equipment for fixed versus mobile use and rip-and-replace integration, increasing fleet complexity and cost. | Medium | Partial | Medium — cross-environment fit and integration with a heterogeneous installed base across six device types raise compatibility and ICD-definition effort (part of R_03); physical portability constraints (R_08) sit with the host hardware and are outside the software scope, so they do not bear on this capability's feasibility. | One cross-environment, integration-friendly solution reduces fleet complexity and total cost of ownership and protects prior capital investment; the cross-environment fit is achieved through interface compatibility, the physical-form aspects being a hardware concern beyond scope. |
| KA_11 | Deploy lawfully without market-access delay | ME_01, BE_01, RE_08, RE_01, RE_04 | Demonstrated readiness for regulatory clearance and lawful market access — a complete, audit-ready technical file produced under a standards-conformant software lifecycle (medical-device software-lifecycle class) with a justified safety classification and documented clinical/diagnostic validation evidence covering the off-the-shelf AI capability's validation status, intended-use boundaries, performance, and known limitations. | Solutions lacking demonstrable conformity readiness, exposing the buyer and manufacturer to market-access delay. | High | Partial | High — AI algorithm regulatory clearance delays (R_01) and AI model validation complexity (R_02) are the dominant programme risks; both are deliberately mitigated by mandating a commercially validated off-the-shelf capability for the first release and engaging the authorities early, which shifts much of the validation evidence onto the supplier of the AI capability. **Business/liability note**: that shift is only as strong as the manufacturer's contractual right to obtain, reference, and rely on the supplier's validation evidence in its own technical file — if the supplier will not flow that evidence down, or its scope does not cover the device's intended use and patient population, the validation burden reverts to the manufacturer and the market-access timeline (and the planned revenue it protects) is at risk; per-market variation in clearance pathways and reimbursement also makes this a Regulatory Affairs and Sales/Commercial dependency, not a single binary event. | Regulatory clearance is a precondition of release and reimbursement; without it the product cannot lawfully reach the clinician regardless of clinical merit, and slipped clearance directly erodes the business case and planned launch revenue. The off-the-shelf-validated-AI constraint is the principal lever that keeps this from being an open-ended programme risk, but the lever only holds if supplier validation evidence is contractually secured and demonstrably covers the device's intended use. |
| KA_12 | Keep liability and clinical risk defensible | ME_08, BE_02, RE_02, RE_04 | Reduction of clinical risk — AI mis-diagnosis, false or missed alarms, sensor-fault propagation, use error — to an acceptable, documented residual level through a full lifecycle risk-management process, with the highest-criticality functions (alarming and diagnosis) mitigated by allocation to independent safeguards so that the overall safety classification is reduced from the initial worst-case to the mitigated level. | Solutions with weaker or undocumented residual-risk control and few independent safeguards for safety-critical functions. | High | Partial | High — the critical hazards (R_04 sensor misplacement, R_05 clinician misinterpretation, R_06 timeout, R_07 connection failure) plus AI mis-diagnosis must all be driven to a defensible residual level; feasibility is Partial but the path is credible because the safety-classification mitigation is achieved by independence — alarming and diagnosis are mitigated to independent systems, and several hazards already carry independent safeguards (device-side fault alarms, dual timeout notification). **Business/liability note**: the validity of the safety-class reduction (worst-case to mitigated) hinges on the *demonstrated genuine independence* of those safeguards — if an audit or a field event later shows the safeguards share a common-cause failure with the function they protect, the mitigated classification collapses, re-opening the higher-rigour obligations and exposing the manufacturer to enforcement and liability; some safeguards also reside in elements outside the software scope (device-side detection, supplier-side timeout notification), so the manufacturer's safety case depends on assured behaviour it does not itself build, which must be verified and contractually underwritten. | Validated-safety and controlled-liability assurance is what governance boards and authorities require to approve and defend a safety-critical diagnostic device, and it is the manufacturer's principal shield against product-liability claims. The independence-based mitigation that lowers the safety class is the central architectural commitment underpinning the whole safety case; because the lower class also reduces lifecycle and re-validation cost, the business has a strong incentive to protect that independence rigorously rather than let it erode over the product's life. |
| KA_13 | Justify the investment and stay viable | ME_02, BE_06, BE_09 | A favourable total cost of ownership across licensing, deployment, support, and lifecycle updates, delivered within committed budget and time-to-market, and architected for reuse and configurability across settings and future lines, including a modular software structure aligned with the device-driver and processing decomposition. | Higher-cost or single-purpose solutions that are costly to own, update, and extend across the portfolio. | High | Partial | Medium — cost, schedule, and reuse targets compete directly with the heavy regulatory and safety-evidence effort (R_01, R_02) and the integration effort (R_03), and must be balanced against the manufacturer's existing capacity; the software-only scope and reuse of an off-the-shelf AI capability help contain cost. **Business note**: the off-the-shelf AI is a double-edged TCO lever — it cuts up-front validation and development cost, but it introduces an ongoing licensing cost and a pricing/continuity dependency on a single external supplier whose fee changes, end-of-life decisions, or model updates (each potentially triggering re-validation) flow straight into lifetime cost and margin; the business case is viable only if those terms are fixed contractually over the service life, so this is a Finance and Sales/Commercial dependency as much as an engineering one. | Affordable ownership and a reusable, configurable architecture keep the buyer's business case and the manufacturer's investment return viable across the portfolio; the software-only scope and mandated off-the-shelf AI are the main cost-containment levers. Priority is raised to High because business-case viability is the gating condition for the whole investment — without a defensible TCO and protected margin the programme is not financeable regardless of clinical merit, and reuse/configurability is what amortises the regulatory and safety-evidence spend across future lines. |
| KA_14 | Stay safe, current, and supportable over its life | ME_06, BE_04, BE_05, BE_07, BE_08, RE_10, RE_07 | High reliability and availability for continuous critical-care use, a controlled standards-conformant software lifecycle enabling safe, modular updates without full re-validation of unchanged parts, dependable support and serviceability, operable post-market surveillance with end-to-end field-to-design traceability, and personal health data handled in conformance with applicable data-protection and secure-interoperability practice. | Solutions that are hard to update safely, with weaker support, surveillance, traceability, or data-protection posture over the service life. | High | Partial | Medium — no single dominant risk, but sustaining reliability, modular lifecycle controls, surveillance, traceability, and data protection together is a broad, ongoing organisational commitment; a traceable, decomposed software structure and the controlled lifecycle make change-scoped re-validation and field-to-design traceability achievable. **Business/liability note**: post-market surveillance, vigilance, and mandated incident-reporting timelines are direct legal obligations of the legal manufacturer with their own enforcement and recall exposure, and they must extend to the off-the-shelf AI component — the manufacturer must receive timely notice of the supplier's model changes and field issues to keep its own surveillance and field-to-design traceability complete, another supplier-dependency that has to be contractually secured. Data-protection non-conformance (GDPR/HIPAA class) carries standalone regulatory and financial liability independent of clinical safety. Sustaining this over the service life is a standing capacity commitment for Quality, Regulatory Affairs, and Customer Support that must be staffed and budgeted, not a one-off project cost. | A safety-critical device must remain available, supportable, updatable, surveilled, and privacy-compliant throughout its service life, or it cannot be trusted or lawfully maintained in the field; modular change control is what keeps update cost and re-validation scope bounded and the lower mitigated safety class affordable to maintain. The ongoing post-market and data-protection obligations are unavoidable lifecycle liabilities the business must resource for the full service life. |

### Business 'Requirements' (BR_*)

Conceptual project inputs from all business stakeholders that apply across the whole product lifecycle (development, launch, manufacturing, deployment, operation & use, end of life).

| ID | Description | Rationale | Stakeholder | Importance | Traces |
|----|-------------|-----------|-------------|------------|--------|
| BR_01 | The solution shall be developed, maintained, and changed under a documented, standards-conformant medical-device software lifecycle (software-lifecycle class commensurate with its safety class), with planning, configuration management, and change control applied from project start. | A controlled lifecycle is a precondition of lawful market access and is what allows the device to be safely updated and patched over its service life without re-incurring full re-validation each change; it is mandated by applicable medical-device software law and harmonised standards. | R&D / Quality Management | High | KA_11, KA_14 |
| BR_02 | The solution's safety classification shall be assessed and recorded with a traceable rationale, and the design shall reduce that classification from its initial worst-case level to a lower mitigated level by allocating the highest-criticality functions (alarming and diagnosis) to safeguards that are demonstrably independent of the function they protect, including safeguards realised in elements outside the software boundary (the measurement devices and the external diagnostic capability). | A justified classification scales development rigour to the harm the software can cause; the independence-based mitigation lowers the class, which bounds lifecycle and re-validation cost. Because the software-only scope places part of each safeguard in fixed external elements accessed through their interfaces, the mitigated class holds only if that genuine, common-cause-free independence is verified and contractually underwritten — otherwise the higher-rigour obligations re-open. | Regulatory Affairs / R&D | High | KA_05, KA_12 |
| BR_03 | The first release shall incorporate a commercially validated, ready-made diagnostic capability rather than a proprietary in-house model, used as an off-the-shelf component. | Mandating an already-validated capability removes proprietary-model validation from the critical path, limits the manufacturer's validation, evidence, and liability burden, and shortens the path to market — the principal de-risking lever for the programme. | Executive / Strategy | High | KA_02 |
| BR_04 | The clinical risk of the solution — covering AI mis-diagnosis, false or missed alarms, sensor-fault propagation, and use error — shall be reduced to an acceptable, documented residual level through a complete lifecycle risk-management process (risk-management standard class) with verified risk controls and independent safeguards for safety-critical functions. | Validated-safety and controlled-liability assurance is required by governance boards and authorities to approve and defend a safety-critical diagnostic device, and is the manufacturer's principal shield against product-liability claims; the documented residual risk underpins the favourable benefit-risk balance. | Quality Management / Legal & Compliance | High | KA_12, KA_05, KA_06, KA_07 |
| BR_05 | The diagnostic output shall be designed and labelled as decision support that informs rather than replaces the clinician, who retains final diagnostic and treatment authority, with the supporting reasoning and confidence of each suggestion made available. | Clinician-in-control is the central liability firewall that keeps ultimate responsibility for patient care with a qualified professional and keeps the device defensible as decision support rather than an autonomous diagnostic agent; it also mitigates automation bias. | Legal & Compliance | High | KA_03 |
| BR_06 | The solution shall demonstrate readiness for regulatory clearance and lawful market access in the target markets as a precondition of release, evidenced by a complete, audit-ready technical file. | Regulatory clearance is a precondition of release and reimbursement; without it the product cannot lawfully reach the clinician regardless of clinical merit, and slipped clearance directly erodes the planned launch revenue and business case. | Regulatory Affairs | High | KA_11 |
| BR_07 | The manufacturer shall operate a certified quality management system (quality-management standard class) and generate and retain design-control, quality, and risk-management evidence as a complete, current, audit-ready technical file throughout the lifecycle. | Notified-body, authority, and internal-governance audits must be satisfied and the declaration of conformity defended; a certified QMS and current technical file are the basis for assessing conformity and supporting lawful market placement. | Quality Management | High | KA_11, KA_14 |
| BR_08 | The solution shall be delivered within the manufacturer's committed budget, cost targets, and time-to-market window, and shall achieve a favourable, demonstrable total cost of ownership for the buyer across licensing, deployment, integration, support, training, and lifecycle updates over the service life — including the recurring licensing and update cost of the off-the-shelf diagnostic capability. | Business-case viability is the gating condition for the whole investment; without a defensible TCO and protected margin the programme is not financeable regardless of clinical merit, and time-to-market protects planned revenue. From the buyer's side, TCO is a primary purchasing criterion evaluated over the whole service life — not just acquisition price — and procurement will discount or reject a solution whose recurring licensing, integration, and support costs are unclear or unbounded, so the buyer-facing TCO must be demonstrable, not merely asserted. | Finance / Executive | High | KA_13 |
| BR_09 | The reliance on an off-the-shelf diagnostic capability shall be governed by contractual supplier safeguards covering validation-evidence flow-down, change and field-issue notification, version/model management, supply continuity, and licensing terms fixed over the service life. | Off-the-shelf reliance does not transfer product liability away from the legal manufacturer; the de-risking, cost, and market-continuity benefits only hold if the supplier dependency is contractually secured, otherwise the validation burden, liability, and lifetime cost revert to the manufacturer. | Legal & Compliance / Sales & Commercial | High | KA_02, KA_11, KA_13, KA_14 |
| BR_10 | The solution shall exchange patient data and diagnostic findings with hospital and EMS information systems over a recognised healthcare interoperability standard (interoperability-standard class, e.g. HL7/FHIR class) to be confirmed and fixed in a defined interface contract before development of the exchange completes, and shall interface with the buyer's existing measurement devices and clinical estate strictly through their published interface contracts across the mandated set of measurement-device types, without modifying those external elements. | Standards-based interoperability and compatibility with the installed base enable second opinion and smooth handover, protect prior capital investment, and spare the buyer bespoke integration cost. Integration fit with the existing IT and device estate is a make-or-break purchasing criterion: a solution that forces rip-and-replace of monitors, devices, or records integration, or that demands bespoke per-site interfacing, raises TCO and deployment risk to the point of rejection, so standards-based exchange and published-contract compatibility are commercial preconditions, not just technical ones. The exact interoperability standard is not yet fixed and the interface contracts are still to be defined, so the requirement commits to the standard *class* and to settling the contract before completion rather than to a specific protocol; the software-only scope means external elements are reached only through published contracts, not adapted to. | Sales & Commercial / Operations | High | KA_09, KA_10 |
| BR_11 | The solution shall be producible, serviceable, and supportable at the required scale and quality using the organisation's existing competencies and capacity, with dependable support, maintenance, and lifecycle updates available throughout the product's service life, on service terms (response times, availability commitments, escalation, and update cadence) that the buyer can rely on and contract for. | The manufacturer must deliver and support the deployed fleet reliably without overrunning operational capability; dependable lifecycle support keeps the deployed fleet safe, current, and competently operated. Vendor dependability and contractable service commitments are a core procurement selection criterion for a safety-critical fleet — buyers assess supplier viability and committed service levels before purchase and will not accept open-ended or best-effort support for equipment used at the point of care. | Operations & Manufacturing / Customer Support & Service | High | KA_13, KA_14 |
| BR_12 | The solution shall include a realistic, risk-free simulated training mode with fail-safe separation between training and live clinical operation, and the manufacturer shall provide clinician training and labelling/instructions-for-use provisions appropriate to the device's safety class over the service life. | The training mode is the named risk control for the critical clinician-misinterpretation hazard and so forms part of the safety case; mandatory information-for-safety and training-provision obligations for the safety class must also be met to support safe fleet operation. | Customer Support & Service / Regulatory Affairs / HR | High | KA_08, KA_03 |
| BR_13 | The manufacturer shall operate a credible post-market surveillance, vigilance, complaint-handling, and incident-reporting capability with end-to-end traceability from a field event back to the responsible design element, extending to field issues and changes in the off-the-shelf diagnostic component. | Post-market surveillance and mandated incident-reporting timelines are direct legal obligations of the legal manufacturer with enforcement and recall exposure; field-to-design traceability is what lets emerging safety signals be detected, reported, and corrected through field safety actions. | Regulatory Affairs / Quality Management | High | KA_14 |
| BR_14 | The solution shall acquire, process, display, and exchange personal health data in conformance with applicable data-protection and privacy law (data-protection-law class, e.g. GDPR/HIPAA class) and secure interoperability practice throughout the data flow. | Data-protection non-conformance carries standalone regulatory and financial liability independent of clinical safety, and patient confidentiality, integrity, and rights must be protected wherever personal health data is handled or exchanged. | Legal & Compliance / Quality Management | High | KA_14, KA_09 |
| BR_15 | The solution shall be architected for reuse and configurability across deployment settings and future product lines, with a modular software structure aligned to the device-acquisition and processing decomposition. | A reusable, configurable architecture amortises the heavy regulatory and safety-evidence spend across the portfolio, maximises return on the development investment, and lowers the cost of extending the product line and of change-scoped re-validation. | R&D / Executive | Medium | KA_13, KA_14 |
| BR_16 | The solution shall demonstrate high reliability and availability for continuous critical-care use, including readiness for use within seconds of switching on, so the monitor is not unavailable at the point of care. | An unavailable monitor at the point of care is an operational and clinical risk that buyers will not accept; demonstrated reliability and rapid readiness avoid clinical downtime and underpin the baseline clinical value of the device. | Operations & Manufacturing / Quality Management | High | KA_14, KA_01 |
| BR_17 | The solution shall produce documented clinical and diagnostic-performance validation evidence — including the validation status, intended-use boundaries, performance characteristics, and known limitations of the off-the-shelf diagnostic component — covering the device's stated indication and patient population. | Authorities require documented clinical evidence to confirm the diagnostic output is safe and effective for its stated indication; the validation evidence for the off-the-shelf component must demonstrably cover the device's intended use or the validation burden and market-access risk revert to the manufacturer. | Regulatory Affairs / R&D | High | KA_11, KA_02 |
| BR_18 | The solution shall meet the boundary-observable timeliness the clinician relies on — sub-second presentation of vital signs, alarms, sensor-fault warnings, and received diagnostic candidates after the system has the data — while the time to converge on a diagnosis is owned by the external diagnostic capability and is not a commitment of the solution. | At-a-glance, low-latency presentation is the baseline clinical value and a safety property: a delayed alarm or stale reading can cause harm. The input fixes a sub-second display budget at the system boundary, whereas diagnosis-convergence time is explicitly an external-capability budget, so the business commitment must be drawn at the boundary the clinician actually observes and must not absorb the external convergence time. | R&D / Quality Management | High | KA_01, KA_05, KA_04 |
| BR_19 | The solution shall deliver active diagnostic decision support beyond passive vital-signs display as a demonstrable clinical-value differentiator over baseline monitoring, with a value proposition (improved time-to-working-diagnosis and decision support where expert consultation is unavailable) that the buyer can evidence and defend when justifying upgrade or replacement of existing equipment to its clinical, finance, and governance boards. | A buyer with a functioning installed base will only invest in replacement or upgrade if the new capability delivers clear, defensible incremental clinical value over what it already owns; diagnostic decision support is the differentiator that justifies that spend, and procurement must be able to substantiate the value case internally. Without an articulated, evidenced upgrade justification the solution competes only on price against adequate incumbents and the purchase is hard to defend — making this a distinct commercial buying criterion not fully captured by the safety, validation, or cost requirements. | Sales & Commercial / Executive | High | KA_02 |

## Context (FORMAL)

The context level is the start of the solution domain (DHF), based on the problem domain and the stakeholder expectations.

### Intended Use (IU_01)

Write the intended use as a single, flowing prose statement that naturally covers the five aspects — what the product is, what it does (medical indication), who uses it (user profile), where it is used (use environment), and how it works (operating principle). Do **not** add bold labels or headers for the aspects; weave them into the sentences.

| ID | Description |
|----|-------------|
| IU_01 | The Mobile Monitoring Software Solution (MMSS) is regulated medical device software (software as part of a medical device under IEC 62304) that turns an existing portable patient monitor into an active clinical decision-support tool for the continuous, real-time monitoring of critically ill or unstable patients, intended to support the early detection of patient deterioration and the formation of a working diagnosis by presenting the patient's vital signs at a glance, raising clinical alarms for abnormal vital-sign conditions and sensor faults, and offering ranked, real-time diagnostic candidates alongside the raw data as decision support that informs but does not replace the clinician; the diagnostic output is adjunctive and non-autonomous, is not intended to be used as the sole basis for any diagnostic or treatment decision, and does not control therapy or actuate any treatment. It is intended for use only by trained, qualified medical professionals — paramedics, emergency physicians, and ICU/ER nurses competent to interpret vital signs and diagnostic information — in fixed critical-care and pre-hospital settings such as intensive care units, emergency rooms, and mobile medical units including ambulances and on-scene emergency response, where it must be operable one-handed and glanceably under time pressure and in moving, noisy, or poorly lit conditions; it is not intended for unsupervised use by lay users or for home use. It works by acquiring data through standardised interfaces from a defined set of non-invasive measurement devices (ECG, pulse oximeter, blood-pressure monitor, thermal probe, capnometer, and EEG), processing that data through its acquisition, conversion, and decision software items and feeding it to a commercially validated off-the-shelf diagnostic AI capability used within the validated scope of its own intended use, then presenting the vital signs and the AI's ranked diagnostic candidates with their supporting reasoning and confidence on the connected monitor display, distinctly signalling sensor disconnection, misplacement, or unreliable readings and diagnosis time-outs, and optionally exchanging patient data and diagnostic findings with hospital information systems over recognised interoperability standards, while the clinician retains final diagnostic and treatment authority at all times. |

### Medical Device Classification (MD_01)

| ID | Description | Traces |
|----|-------------|--------|
| MD_01 | MMSS is regulated medical device software whose safety is classified under IEC 62304 (software safety classification, Clause 4.3). The software system's **initial** classification is **Class C** — failure or latent fault of the software could contribute to a hazardous situation that, absent further risk control, could result in **death or serious injury** — because erroneous, missed, or delayed vital-signs presentation, alarming, or diagnostic output in critical-care use is a foreseeable sequence to severe patient harm. Per IEC 62304 Clause 4.3 the classification is determined from the worst-case harm that could result from the software contributing to the hazardous situation **assuming the hazardous situation occurs**, and may be reduced where external risk-control measures — hardware or other software outside the software item — prevent that hazardous situation from leading to the worst-case harm. On this basis the worst-case contribution of the two highest-criticality functions — alarming and diagnosis — is mitigated so that no single MMSS failure can, on its own, lead to death or serious injury: for sensor disconnection, misplacement, and unreliable-reading conditions the measurement devices raise their own independent audible connection/fault alarms, and the external diagnostic capability raises an independent audible time-out notification on convergence failure; combined with the clinician retaining final diagnostic and treatment authority over non-autonomous, adjunctive output, the residual worst-case harm of an MMSS-only failure in these functions is reduced to a non-serious level. The abnormal-vital-sign threshold alarm, by contrast, has no equivalent device-side independent re-annunciation — a measurement device signals its own connection or fault state but does not independently re-raise a missed out-of-range physiological alarm — so the safety of that function is assured not by an external safeguard but by engineering it to the rigour commensurate with its criticality and by the clinician's continuous observation of the at-a-glance vital-signs display. The resulting software safety classification is therefore **Class B**. This reduction is admissible only because the safeguards are **segregated from and demonstrably independent of MMSS** — they reside in the measurement devices and the external diagnostic capability, outside the MMSS software boundary, and do not share a common-cause failure with the function they protect (consistent with the IEC 62304 segregation expectation that risk controls relied upon to lower a classification be independent of the item they protect). The Class B classification holds only while that genuine, common-cause-free independence is verified through the ISO 14971 risk-management process and contractually underwritten with the device and AI suppliers; if independence cannot be demonstrated, or is eroded by a design or supplier change, the higher-rigour Class C lifecycle obligations re-open and the residual-risk and benefit-risk argument supporting market access must be re-established. | IU_01 |

### Context Diagram

The context diagram identifies the system of interest in relation to its context. The system of interest contains all elements that are part of the design.

_To be added_

#### Product Information

The Mobile Monitoring Software Solution (MMSS) is regulated medical device software (IEC 62304) that runs on an existing portable patient monitor and turns it from a passive vital-signs display into an active clinical decision-support tool for critical-care and pre-hospital use. It delivers three things to the clinician: a real-time at-a-glance presentation of the patient's vital signs, clinical alarms for abnormal vital-sign conditions and sensor faults, and ranked, real-time diagnostic candidates with their supporting reasoning and confidence. MMSS operates by acquiring measurement data through standardised interfaces from a defined set of six non-invasive measurement device types, processing and conditioning that data on the host platform, feeding it to a commercially validated off-the-shelf diagnostic AI capability that returns structured diagnostic candidates, then rendering the vital signs, alarms, and diagnostic output on the connected monitor display — and, optionally, exchanging patient data and diagnostic findings with a hospital information system over recognised interoperability standards. The diagnostic output is adjunctive and non-autonomous; the clinician retains final diagnostic and treatment authority at all times.

#### System of Interest

The part of the broader system this document is about — the product, subsystem, or component you are responsible for designing.

| System Element | Description |
|----------------|-------------|
| MMSS | The Mobile Monitoring Software Solution as a whole — the complete application software stack treated as a single black box at its external boundary. MMSS acquires data from the six measurement device types via published device interfaces, conditions and processes it on the host platform, exchanges data with the external diagnostic AI capability to obtain ranked diagnostic candidates, presents vital signs, alarms, and diagnostic output on the monitor display, and optionally shares data with the hospital information system. This is the only element being designed in this project; its internal software decomposition is addressed at the Architecture level and is out of scope here. |

#### Context Elements

Essential elements for your product that are not part of the design.

| Context Element | Description |
|-----------------|-------------|
| Host CPU platform | The existing compact embedded CPU platform with real-time OS capabilities on which MMSS executes. Fixed hardware/OS accessed via published interface; provides the runtime, timing services, and resources for MMSS but is not designed in this project. |
| ECG monitor | Existing measurement device acquiring cardiac electrical activity via electrodes. Fixed device accessed through a published interface; provides Heart Rate to MMSS and raises its own independent connection/fault alarms. |
| Pulse oximeter | Existing measurement device acquiring peripheral oxygen saturation via an SpO₂ probe. Fixed device accessed through a published interface; provides SpO2 and Pulse Rate to MMSS and raises its own independent connection/fault alarms. |
| Blood pressure (BP) monitor | Existing measurement device acquiring non-invasive blood pressure via an NIBP cuff. Fixed device accessed through a published interface; provides Systolic BP, Diastolic BP, and MAP to MMSS and raises its own independent connection/fault alarms. |
| Thermal probe | Existing measurement device acquiring body temperature. Fixed device accessed through a published interface; provides Temperature to MMSS and raises its own independent connection/fault alarms. |
| Capnometer | Existing measurement device acquiring respiratory parameters via an EtCO₂ sampling line. Fixed device accessed through a published interface; provides Respiratory Rate and EtCO2 to MMSS and raises its own independent connection/fault alarms. |
| EEG monitor | Existing measurement device acquiring cortical electrical activity via electrodes and deriving a bispectral index. Fixed device accessed through a published interface; provides BIS to MMSS and raises its own independent connection/fault alarms. |
| Monitor display | The existing connected display of the portable patient monitor on which MMSS renders vital signs, alarms, and diagnostic candidates. Fixed hardware accessed via a published display interface. |
| External diagnostic AI capability | A commercially validated, off-the-shelf diagnostic AI service (Open Evidence class) external to MMSS, used within the validated scope of its own intended use. Receives conditioned patient data from MMSS and returns structured, ranked diagnostic candidates with reasoning and confidence; raises its own independent audible time-out notification on convergence failure. Not designed in this project. |
| Hospital information system (HIS) | An external clinical information system with which MMSS optionally exchanges patient data and diagnostic findings for a second opinion. Interoperability over HL7/FHIR-class standards; protocol and ICD to be defined. Not designed in this project. |
| Patient | The critically ill or unstable patient to whom the measurement devices are non-invasively attached and whose physiological signals are the ultimate source of all acquired parameters. Outside the MMSS software boundary; interacts with MMSS only indirectly through the measurement devices. |

#### External Interfaces (IF_*)

Connections between the system of interest and the context elements (mechanical, chemical, electronic, digital, logical, etc.).

| ID | Name | Port 1 | Port 2 | ICD |
|----|------|--------|--------|-----|
| IF_01 | Host platform / OS interface | MMSS | Host CPU platform | Host platform/RTOS ICD — defined by host vendor (existing) |
| IF_02 | ECG acquisition interface | MMSS | ECG monitor | Device ICD — defined (existing, published) |
| IF_03 | Pulse oximeter acquisition interface | MMSS | Pulse oximeter | Device ICD — defined (existing, published) |
| IF_04 | BP monitor acquisition interface | MMSS | Blood pressure (BP) monitor | Device ICD — defined (existing, published) |
| IF_05 | Thermal probe acquisition interface | MMSS | Thermal probe | Device ICD — defined (existing, published) |
| IF_06 | Capnometer acquisition interface | MMSS | Capnometer | Device ICD — defined (existing, published) |
| IF_07 | EEG acquisition interface | MMSS | EEG monitor | Device ICD — defined (existing, published) |
| IF_08 | Display interface | MMSS | Monitor display | Display ICD — defined (existing, published) |
| IF_09 | Diagnostic AI interface | MMSS | External diagnostic AI capability | Diagnostic AI library API ICD — defined by supplier (Open Evidence class) |
| IF_10 | Hospital information system (HIS) interface | MMSS | Hospital information system (HIS) | HIS interoperability ICD — TBD (HL7/FHIR class) |

#### Acquired Parameters / Signals

Whenever the product acquires, exchanges, or presents a **set** of parameters, signals, or data items from a set of source elements (measurement devices, sensors, sub-systems, services), enumerate that set here instead of leaving it as a collective phrase elsewhere. One row per source-element/parameter combination, taken from the input. If no such parameter set applies to this product, write `_Not applicable_`.

| Source Element | Parameter / Signal | Unit / Typical Range | Interface |
|----------------|--------------------|----------------------|-----------|
| ECG monitor (electrodes) | Heart Rate | bpm; typical 40–180 (adult 60–100 normal) | IF_02 |
| Blood pressure (BP) monitor (NIBP cuff) | Systolic BP | mmHg; typical 70–200 (adult ~120 normal) | IF_04 |
| Blood pressure (BP) monitor (NIBP cuff) | Diastolic BP | mmHg; typical 40–120 (adult ~80 normal) | IF_04 |
| Blood pressure (BP) monitor (NIBP cuff) | MAP (Mean Arterial Pressure) | mmHg; typical 50–130 (adult 70–105 normal) | IF_04 |
| Pulse oximeter (SpO₂ probe) | SpO2 | % saturation; typical 70–100 (normal ≥ 95) | IF_03 |
| Pulse oximeter (SpO₂ probe) | Pulse Rate | bpm; typical 40–180 | IF_03 |
| Capnometer (EtCO₂ sampling line) | Respiratory Rate | breaths/min; typical 5–40 (adult 12–20 normal) | IF_06 |
| Capnometer (EtCO₂ sampling line) | EtCO2 (end-tidal CO₂) | mmHg; typical 20–60 (normal 35–45) | IF_06 |
| Thermal probe | Temperature | °C; typical 30–42 (normal ~37) | IF_05 |
| EEG monitor (electrodes) | BIS (Bispectral Index) | dimensionless index 0–100 (40–60 typical for general anaesthesia) | IF_07 |
| External diagnostic AI capability | Ranked diagnostic candidates (with supporting reasoning and confidence) | Structured list; each candidate with confidence/likelihood score (0–1 or %) | IF_09 |

## Users

### User Groups

Collections of users who share common characteristics (a synonym is User Role).

| User | User Group | User Profile |
|------|------------|--------------|
| Paramedic / pre-hospital clinician | Pre-hospital Clinician | Trained, certified paramedic or pre-hospital emergency clinician who connects the patient and operates MMSS at the scene and in a moving ambulance. Highly competent at acquiring vital signs and stabilising patients, but typically works alone or in a small crew with no physician on hand and limited ability to consult a colleague. Operates under severe time pressure, often one-handed with attention split across driving/transport, patient handling, and the device, in moving vehicles, poor light, noise, vibration, and cramped space. Needs MMSS to be ready within seconds of power-on, glanceable, operable one-handed, to surface ranked diagnostic candidates with reasoning/confidence to compensate for the absence of expert backup, to alarm unmistakably on abnormal vital signs and sensor faults, and to share data ahead of arrival with the receiving hospital. Is the primary intended user for whom the mobile/pre-hospital usability and safety case must be demonstrated. |
| Emergency physician | Emergency Physician | Trained, qualified physician (ER / emergency medicine, or transport/critical-care physician) who uses MMSS in the emergency room and on incoming critically ill patients, and who carries final diagnostic and treatment authority. Deep clinical knowledge; uses the AI diagnostic candidates as adjunctive decision support and is expected to critically appraise reasoning and confidence rather than defer to them, so MMSS must reinforce decision-support framing and resist automation bias. Works in a busy, interruption-rich ER, frequently managing several patients at once, and needs at-a-glance vital signs, trustworthy alarms, clear timeout signalling when no diagnosis can be produced, and smooth data exchange/handover with the hospital information system for second opinion and continuity of care. |
| ICU / ER nurse | Critical-Care Nurse | Trained, registered critical-care or emergency nurse who provides continuous bedside monitoring in the ICU or ER, the user most often watching MMSS over extended shifts. Sets up sensors, responds first to alarms, tracks trends, and escalates to a physician. Needs distinguishable, fatigue-resistant alarms (clinically significant condition vs sensor fault), clear sensor disconnection/misplacement warnings so care is not based on false data, glanceable continuous display while attending to other tasks and patients, and reliable, available operation throughout the shift. Interprets vital signs and diagnostic information within their scope of practice but escalates diagnostic and treatment decisions; primary user for sustained-use alarm-safety and sensor-fault interactions. |
| Clinical trainer / super-user | Clinical Trainer / Super-User | Experienced clinician (often a senior nurse, paramedic educator, or clinical specialist) designated as the local expert who trains colleagues and champions safe use of MMSS within the deploying organisation. Primary user of the risk-free simulated training mode: runs realistic scenarios to build competence before live patient use, and is responsible for ensuring trainees never confuse simulated data with a real patient. Needs unambiguous, fail-safe, persistently indicated separation between training and live clinical operation, realistic scenario behaviour, and the ability to demonstrate and explain AI candidate reasoning/confidence and correct interpretation. Because the training mode is the named risk control for the critical clinician-misinterpretation hazard, this user is central to mitigating use error across the deployed fleet. |
| Biomedical / clinical engineer | Biomedical / Clinical Engineer | Trained biomedical or clinical engineering technician within the hospital/EMS clinical-engineering department responsible for installing, configuring, integrating, verifying, and maintaining MMSS on the host platform across the fleet. Not a clinical user during patient care; works in a calm technical or workshop setting (and occasionally at the point of care for commissioning/servicing). Connects MMSS to the six measurement-device types and to the hospital information system through their defined interface contracts, validates correct acquisition, alarming, and data exchange, applies controlled software updates, and supports troubleshooting and serviceability over the service life. Needs reliable configuration/diagnostic tooling, clear interface and fault feedback, and update procedures that fit a standards-conformant lifecycle without disrupting deployed devices. |

### User Requirements / Needs (UR_*)

The user expectations translated over the product context into requirements specific to YOUR product. They are SMARTER than the expectations and form the base for product validation. Format: *As a \<user group\> I want \<feature\> so that \<benefit\>.*

| ID | Description | Classification | Traces |
|----|-------------|----------------|--------|
| UR_01 | As a Pre-hospital Clinician I want MMSS to present, within 1 second of acquisition, an at-a-glance real-time display of every acquired vital-sign parameter listed in the Acquired Parameters / Signals table (Context) refreshed at least once per second and showing each value with its unit and clearly flagged as out-of-range when abnormal, so that I can read the patient's true current condition correctly at a glance without searching, mental conversion, or delay. | High; Safety-critical (Class B) | IU_01, BR_18, BR_16 |
| UR_02 | As a Pre-hospital Clinician I want MMSS to become ready for clinical use within 10 seconds of switching on, so that I can start caring for the patient at the scene without waiting through a slow start-up. | High; Availability | IU_01, BR_16 |
| UR_03 | As a Critical-Care Nurse I want MMSS to remain reliably available and continue presenting vital signs throughout an extended shift of continuous monitoring, so that the monitor is not unavailable at the point of care when I am attending to other patients and tasks. | High; Availability | IU_01, BR_16 |
| UR_04 | As an Emergency Physician I want MMSS to present, within 1 second of receipt from the external diagnostic AI capability, ranked real-time diagnostic candidates (the diagnostic-candidates parameter in the Acquired Parameters / Signals table) alongside the raw vital signs, so that I can reach a working diagnosis faster, including when no colleague is available to consult. | High; Differentiator | IU_01, BR_19, BR_18 |
| UR_05 | As an Emergency Physician I want each diagnostic candidate presented with its confidence and its supporting reasoning — including which of the patient's vital signs drove it — in a form absorbable at a glance under time pressure yet available in more detail when I choose to look, so that I can judge whether the suggestion fits the patient in front of me, keep my clinical judgement in control, and recognise when a candidate rests on a parameter I already distrust. | High; Safety-critical / Liability | IU_01, BR_05 |
| UR_06 | As an Emergency Physician I want MMSS to frame and label the diagnostic output unambiguously as decision support that informs rather than replaces me, and to never prevent me from acting on my own judgement ahead of or against a suggestion, so that final diagnostic and treatment authority remains with me and automation bias is mitigated. | High; Safety-critical / Liability | IU_01, BR_05 |
| UR_07 | As a Pre-hospital Clinician I want MMSS to clearly and promptly signal to me when a diagnostic result cannot be produced within the expected convergence time — through a positive, perceptible indication independent of the diagnostic path that has failed, rather than leaving the candidate area simply blank — so that I know not to keep waiting and can fall back on my own assessment without delaying care. | High; Safety-critical (Class B) | IU_01, BR_05, BR_18 |
| UR_08 | As a Critical-Care Nurse I want MMSS to raise, within 1 second of detection, an immediate, unmistakable, and distinguishable alarm identifying which acquired vital-sign parameter (per the Acquired Parameters / Signals table) is abnormal and how urgent it is, perceptible in noisy and mobile conditions and remaining active until the condition resolves or I acknowledge it, so that I can intervene before the patient deteriorates and a clinically significant alarm is never missed because I was attending to another patient. | High; Safety-critical (Class B) | IU_01, BR_18, BR_04 |
| UR_09 | As a Critical-Care Nurse I want MMSS alarms to conform to recognised alarm-safety practice and to be distinguishable from sensor-fault warnings without causing alarm fatigue, so that clinically significant conditions are signalled correctly over sustained use and are never mistaken for a technical fault or vice versa. | High; Safety-critical / Regulatory | IU_01, BR_04 |
| UR_10 | As a Critical-Care Nurse I want MMSS to detect and clearly warn me, within 1 second, when any measurement device in the Acquired Parameters / Signals table is disconnected, misplaced, or producing unreliable readings, and to visibly mark the affected parameter as untrustworthy rather than continue showing a stale or implausible value as if it were live, with the warning readily distinguishable from a genuine clinical alarm, so that I do not act on false or missing data or mistake a sensor fault for real patient deterioration. | High; Safety-critical (Class B) | IU_01, BR_04 |
| UR_11 | As a Pre-hospital Clinician I want MMSS to be operable one-handed and to stay glanceable and legible in movement, poor light, noise, and vibration, so that I can keep working safely when conditions in the ambulance or at the scene are far from ideal. | High; Safety-critical / Usability | IU_01, BR_04, BR_12 |
| UR_12 | As a Clinical Trainer / Super-User I want MMSS to provide a realistic, risk-free simulated training mode in which I can run scenarios and demonstrate AI candidate reasoning, confidence, and correct interpretation, so that clinicians build competence before using the device on a real patient. | High; Safety-critical (named risk control) | IU_01, BR_12 |
| UR_13 | As a Clinical Trainer / Super-User I want MMSS to enforce fail-safe separation between training and live clinical operation, with a persistent, glanceable indication of which mode is active at all times, so that simulated data can never be mistaken for a real patient and a clinician returning to a device cannot unknowingly treat a live patient in training mode. | High; Safety-critical (Class B) | IU_01, BR_12 |
| UR_14 | As an Emergency Physician I want MMSS to exchange the patient's vital-sign data and diagnostic findings with the hospital information system over a recognised interoperability standard, delivering diagnostic candidates within 1 second of availability, so that I can secure a second opinion and hand over care smoothly and securely. | High; Interoperability | IU_01, BR_10, BR_18 |
| UR_15 | As an Emergency Physician I want MMSS to handle and exchange the patient's personal health data in conformance with applicable data-protection and privacy law throughout the data flow, so that patient confidentiality, integrity, and rights are protected when data is displayed or shared with the hospital. | High; Regulatory / Privacy | IU_01, BR_14, BR_10 |
| UR_16 | As a Biomedical / Clinical Engineer I want MMSS to connect to each of the six measurement-device types and to the hospital information system strictly through their published interface contracts, and to give clear interface and fault feedback during commissioning, so that I can install, integrate, and verify correct acquisition, alarming, and data exchange across the fleet without modifying the external elements. | High; Integration | IU_01, BR_10, BR_11 |
| UR_17 | As a Biomedical / Clinical Engineer I want MMSS to support controlled software updates that fit a standards-conformant lifecycle without disrupting deployed devices, so that I can keep the fleet safe, current, and serviceable over the product's service life. | High; Lifecycle / Maintainability | IU_01, BR_01, BR_11 |

### User DFMEA (USER_DFMEA_*)

A structured analysis of how users might misuse, misinterpret, or fail to operate the product, the consequences, and the mitigations the design must include.

Severity scale: **Critical** = use error can plausibly contribute to patient death or serious irreversible harm; **Serious** = can contribute to serious but recoverable harm or significant treatment delay; **Moderate** = limited or transient harm, or notable inefficiency; **Minor** = inconvenience or minor inefficiency with no clinical harm.

| ID | Item/Function | Requirement | Failure Mode | End-effect | Rationale | Failure Cause | Severity | Prevention | Classification | Traces |
|----|---------------|-------------|--------------|------------|-----------|---------------|----------|------------|----------------|--------|
| USER_DFMEA_01 | Vital-signs display (at-a-glance reading of acquired parameters) | MMSS shall present, within 1 s of acquisition, an at-a-glance display of every acquired vital-sign parameter (Acquired Parameters / Signals table) with unit and out-of-range flag (UR_01). | Clinician reads a vital sign and misses or misreads an abnormal value (e.g. SpO2, HR, EtCO2 from the Acquired Parameters / Signals table), failing to recognise deterioration. | Abnormal condition not acted on; patient deteriorates before intervention. | The display is the clinician's primary window onto the patient's true state; a misread or overlooked abnormal value drives a missed or delayed life-saving intervention. | Small/dense numerals, no per-parameter unit, weak out-of-range distinction, glanceable read in poor light/movement, attention split across patients. | Critical | High-contrast glanceable layout with consistent placement; each value shown with its unit; abnormal values made visually unmistakable (colour + shape/icon, not colour alone) and reinforced by the parameter alarm (UR_08); 1 s refresh so values are never stale; summative usability validation in mobile conditions. | High; Safety-critical (Class B) | UR_01 |
| USER_DFMEA_02 | Vital-signs display (start-up readiness) | MMSS shall become ready for clinical use within 10 s of switch-on (UR_02). | Clinician begins reading and acting on the display before all parameters are actually live, treating not-yet-acquired channels as if confirmed. | Decision made on incomplete data; a yet-to-appear abnormal value is missed. | During the start-up window the clinician under time pressure may assume a blank or zero channel is "normal" rather than "not yet acquired". | No explicit "acquiring / not ready" state per channel; absence of a value read as a normal value; pressure to act within seconds. | Serious | Persistent per-channel acquisition state (acquiring / live / no-data) that is visually distinct from a real measured value; clear "ready" indication when activation completes; never render an unacquired channel as a plausible normal number. | High; Availability | UR_02 |
| USER_DFMEA_03 | Diagnostic decision support (AI candidate presentation) | MMSS shall present ranked real-time diagnostic candidates alongside the raw vital signs within 1 s of receipt (UR_04). | Clinician over-trusts the top-ranked AI candidate and adopts it as the diagnosis without independent appraisal (automation bias). | Wrong working diagnosis pursued; correct condition missed or delayed; potential serious patient harm. | R_05: clinician misinterpretation of AI candidates is a critical hazard; automation bias is the dominant human-factors driver of acting on a wrong AI suggestion. | Ranking presented as authority; high apparent confidence; time pressure; fatigue; reasoning/confidence not absorbed; trust built up over prior correct suggestions. | Critical | Present candidates as ranked *suggestions* with confidence and supporting reasoning at a glance (UR_05); unambiguous decision-support framing/labelling that informs rather than replaces (UR_06); never gate or pre-select treatment on a candidate; mandatory simulation training mode covering automation bias (UR_12). | High; Safety-critical / Liability | UR_04, UR_05, UR_06 |
| USER_DFMEA_04 | Diagnostic decision support (confidence & reasoning) | MMSS shall present each candidate with confidence and supporting reasoning, including which vital signs drove it, absorbable at a glance (UR_05). | Clinician misinterprets the confidence score or the ranking — reads a low-confidence or low-ranked candidate as a firm finding, or dismisses a clinically relevant lower-ranked candidate. | Misdirected or prematurely narrowed diagnostic reasoning; appropriate differential not considered; a treatable time-critical condition (e.g. a low-ranked but life-threatening differential) acted on too late. | Confidence and rank are easily misread under pressure; a number without clear framing invites over- or under-weighting, escalating the R_05 misinterpretation hazard; dismissing a low-ranked but lethal differential can be as harmful as over-trusting the top candidate. | Confidence shown as a bare percentage without interpretive framing; ranking implies certainty; reasoning/driving parameters not visible at a glance; no training on reading confidence. | Serious | Express confidence with clear, consistent interpretive framing (not a bare number alone); show the driving vital-sign parameters so the clinician can see whether a candidate rests on a parameter they distrust; expandable detail on demand; cover confidence/ranking interpretation explicitly in the training mode (UR_12). | High; Safety-critical / Liability | UR_05, UR_06 |
| USER_DFMEA_05 | Sensor-fault detection (acting on faulty/misplaced sensor data) | MMSS shall detect and clearly warn, within 1 s, when any measurement device is disconnected, misplaced, or unreliable, and mark the affected parameter as untrustworthy (UR_10). | Clinician acts on a value from a misplaced or faulty sensor, trusting it as a true reading. | Decision made on false data — e.g. a falsely reassuring SpO2 or BP — leading to a wrong diagnosis or missed deterioration. | R_04 (sensor misplacement) is a critical hazard: a silently-trusted wrong reading can drive a wrong diagnosis or mask a real deterioration. | Misplacement not detected/reported by the device at the interface; affected parameter still shown as a plausible live value; fault warning not noticed or not distinguishable; clinician unaware the channel is suspect. | Critical | Reliance on device-side misplacement/fault signalling at the interface plus disconnection inference from input inactivity; affected parameter visibly marked untrustworthy (not shown as a normal live value); distinct sensor-fault warning readily distinguishable from a clinical alarm (UR_09); device-side independent audible alarms as safeguard. | High; Safety-critical (Class B) | UR_10, UR_09 |
| USER_DFMEA_06 | Sensor-fault detection (stale value mistaken for live) | MMSS shall mark the affected parameter as untrustworthy rather than continue showing a stale or implausible value as if live (UR_10). | Clinician reads a frozen/stale parameter value as the patient's current reading after a sensor has silently failed. | Care based on out-of-date data; a real change in the patient's condition goes unnoticed. | A stale value indistinguishable from a live one is more dangerous than a blank, because it positively misleads. | Last-good value retained on screen with no staleness/no-data indication; disconnection not yet detected; clinician assumes continuously updating display. | Serious | On loss of input over the short inactivity window, replace the value with an explicit no-data/untrustworthy state; never persist a stale value as if live; timestamp or freshness cue; couple with the connection/disconnection warning. | High; Safety-critical (Class B) | UR_10 |
| USER_DFMEA_07 | Vital-sign alarm (missed alarm in noisy/mobile setting) | MMSS shall raise within 1 s an unmistakable, distinguishable alarm identifying the abnormal parameter and urgency, perceptible in noisy/mobile conditions and active until resolved or acknowledged (UR_08). | Clinician misses a vital-sign alarm in a noisy, moving, multi-patient environment. | Clinically significant deterioration not acted on in time; patient harm. | A missed alarm defeats the core safety function; the pre-hospital/ER environment (noise, vibration, attention split) is exactly where alarms are most likely to be missed. | Insufficient loudness/contrast for the environment; non-latching alarm self-clears before notice; alarm not distinguishable from background; alarm fatigue desensitisation. | Critical | Multi-modal, conspicuous alarms (audible + visual) tuned for noisy/mobile use and conforming to alarm-safety practice (UR_09); latching until resolved or explicitly acknowledged; distinct urgency encoding; alarm-fatigue mitigation through prioritisation; device-side independent audible alarms as safeguard. | High; Safety-critical (Class B) | UR_08, UR_09 |
| USER_DFMEA_08 | Vital-sign alarm vs sensor-fault warning (confusion) | MMSS alarms shall be distinguishable from sensor-fault warnings without alarm fatigue (UR_09). | Clinician confuses a sensor-fault warning with a genuine clinical alarm (or vice versa) and responds inappropriately. | Real deterioration treated as a "false alarm" and ignored, or a technical fault triggers unnecessary clinical intervention. | Mistaking a fault for deterioration (or the reverse) is an explicit alarm-safety hazard (R_06/R_07 family) that leads directly to wrong or omitted action. | Clinical alarm and fault warning share similar tone/colour/wording; high alarm load erodes discrimination; ambiguous labelling of which condition is signalled. | Serious | Clearly differentiated alarm vs technical-fault signalling (distinct tone, colour, icon, and text per IEC 60601-1-8 class practice); explicit statement of which parameter/device and what kind of condition; consistent encoding reinforced in training (UR_12). | High; Safety-critical / Regulatory | UR_09, UR_10 |
| USER_DFMEA_09 | Diagnosis-timeout signalling (not noticing no result) | MMSS shall clearly and promptly signal when a diagnostic result cannot be produced in the expected convergence time, via a positive perceptible indication independent of the failed path, not a blank area (UR_07). | Clinician does not notice that no diagnosis was produced and keeps waiting for a result that will not arrive. | Treatment delayed while the clinician waits instead of falling back on their own assessment. | R_06: diagnosis timeout not communicated is a critical hazard; a blank candidate area is read as "still computing" rather than "no result". | Empty candidate area indistinguishable from "in progress"; timeout cue absent or too subtle; reliance on the same path that failed to converge. | Serious | Positive, perceptible timeout indication delivered independently of the diagnostic path (UR_07), reinforced by the external capability's own independent audible timeout notification; explicit "no diagnosis available — proceed on your own assessment" message; never leave the area silently blank. | High; Safety-critical (Class B) | UR_07 |
| USER_DFMEA_10 | Training/live mode separation (live patient in training mode) | MMSS shall enforce fail-safe separation between training and live operation with a persistent glanceable indication of the active mode (UR_13). | Clinician unknowingly operates MMSS on a live patient while it is still in simulated training mode (or treats simulated data as a real patient). | Simulated data acted on as real, or a real patient monitored by a non-clinical simulation — directly endangering the patient. | A training scenario mistaken for a real patient is itself a critical hazard and the named risk control (training mode) becomes a hazard source if mode is ambiguous. | Mode indication absent, subtle, or not persistent; device left in training mode by a previous user; no fail-safe default to live; glanceable cue missed in poor light. | Critical | Persistent, unmistakable, always-visible mode indicator (distinct colour/banner) that cannot be dismissed; fail-safe behaviour on return/restart; explicit confirmation when entering/leaving training mode; clear watermarking of simulated data; covered as a safety task in training (UR_12). | High; Safety-critical (Class B) | UR_13, UR_12 |
| USER_DFMEA_11 | Decision-support authority (over-reliance / loss of control) | MMSS shall frame the diagnostic output as decision support that informs rather than replaces the clinician and never prevent the clinician from acting on their own judgement (UR_06). | Clinician defers final diagnostic/treatment authority to MMSS, withholding or delaying their own action pending or against the AI output. | Clinician's superior contextual judgement is not applied; correct action delayed or not taken; liability firewall undermined. | Clinician-in-control is the central liability and safety control; if the workflow nudges the clinician to defer, the device drifts toward an unsafe autonomous role. | Output presented authoritatively; workflow appears to require the AI result before proceeding; no clear affordance to override or act independently. | Serious | Design the workflow so the clinician can always act ahead of or against a suggestion; explicit decision-support framing and labelling (UR_06); no hard dependency on an AI result to deliver care; reinforce clinician authority in training (UR_12). | High; Safety-critical / Liability | UR_06, UR_05 |
| USER_DFMEA_12 | One-handed glanceable operation (use error in adverse conditions) | MMSS shall be operable one-handed and stay glanceable and legible in movement, poor light, noise, and vibration (UR_11). | Clinician makes a slip or selection error (e.g. wrong control, mis-acknowledged alarm) while operating one-handed in a moving vehicle. | Unintended action — e.g. an alarm silenced or a setting changed inadvertently — degrading monitoring safety. | Pre-hospital/mobile use is a defining environment; controls not designed for adverse conditions invite use errors that can suppress safety functions. | Small/closely-spaced targets; controls needing two hands or precise input; legibility lost in poor light/vibration; no confirmation on safety-significant actions. | Serious | Large, well-spaced, one-handed-operable controls; confirmation or guarding on safety-significant actions (e.g. alarm-off); high legibility under movement and poor light; formative and summative usability evaluation in the mobile environment. | High; Safety-critical / Usability | UR_11, UR_08 |
| USER_DFMEA_13 | Continuous availability (assuming live monitoring during a gap) | MMSS shall remain reliably available and continue presenting vital signs throughout an extended shift (UR_03). | Nurse assumes continuous monitoring is active and unattended during a display freeze, restart, or availability gap. | A deterioration occurring during the gap is not detected while the clinician believes the patient is being monitored; an unattended patient can arrest unobserved. | A silent availability gap on an unattended critical patient gives a false sense of safety and removes the very surveillance the patient depends on — realistically capable of contributing to an unwitnessed deterioration or arrest, so rated Critical. | Display freeze or restart not signalled; no heartbeat/health indication; clinician attending other patients trusts the monitor is live. | Critical | Continuous self-monitoring with an explicit, perceptible alert on any monitoring interruption or restart; visible system-health/heartbeat indication; never present a frozen screen as if live; device-side independent alarms as safeguard. | High; Availability | UR_03 |
| USER_DFMEA_14 | Data sharing / handover (wrong or incomplete transfer) | MMSS shall exchange vital-sign data and diagnostic findings with the HIS over a recognised standard, delivering candidates within 1 s of availability (UR_14). | Clinician believes data/findings were shared with the receiving hospital when the exchange failed, was partial, or went to the wrong record. | Receiving team acts without (or on incomplete/mismatched) information; second opinion and handover compromised. | Handover is a known high-risk transition; a silent transfer failure leaves both ends with a false belief that information is in hand. | No confirmation of successful transfer; partial transfer not flagged; ambiguous patient/record association; connectivity failure (R_03) unsurfaced. | Serious | Explicit success/failure confirmation of the exchange; clear flag on partial or failed transfer with retry; unambiguous patient-record association; secure, standards-based exchange handled per data-protection requirements (UR_15). | High; Interoperability | UR_14, UR_15 |
| USER_DFMEA_15 | Patient-data privacy (unintended disclosure during use) | MMSS shall handle and exchange personal health data in conformance with data-protection law throughout the data flow (UR_15). | Clinician inadvertently exposes or mis-shares patient data (e.g. shares to an unintended recipient, leaves identifiable data visible). | Breach of patient confidentiality; regulatory and liability exposure independent of clinical safety. | Data-protection non-conformance carries standalone regulatory/financial liability; use error is a common breach pathway. | Sharing targets not clearly confirmed; identifiable data persistently displayed; no safeguards on the exchange/recipient selection. | Moderate | Confirm recipient/target before exchange; minimise and protect identifiable data on display; secure-by-default exchange with access controls per UR_15; cover privacy-safe handling in training. | High; Regulatory / Privacy | UR_15, UR_14 |
| USER_DFMEA_16 | Commissioning / integration (mis-configured device mapping) | MMSS shall connect to each device type and the HIS through their published interface contracts and give clear interface and fault feedback during commissioning (UR_16). | Biomedical engineer mis-maps or mis-configures a device channel during commissioning (e.g. a parameter routed to the wrong display field) and it goes unnoticed. | A parameter is displayed/alarmed against the wrong channel in clinical use, propagating to wrong clinical decisions. | A configuration error made once at commissioning silently affects every subsequent patient until detected. | Unclear commissioning feedback; no verification step confirming each channel maps to the correct device/parameter; ambiguous interface status. | Serious | Clear per-channel interface and fault feedback during commissioning; a guided verification/confirmation step that each parameter maps to the correct device before clinical release; unambiguous interface status indicators. | High; Integration | UR_16 |
| USER_DFMEA_17 | Software update (update applied to a deployed in-use device) | MMSS shall support controlled software updates that fit a standards-conformant lifecycle without disrupting deployed devices (UR_17). | Engineer applies an update to a device that is (or is about to be) in clinical use, or returns it to service without confirming monitoring is restored. | Monitoring unavailable during patient care, or device returned to service in an unverified state. | An update that disrupts an in-use safety-critical monitor, or an unverified return-to-service, directly removes monitoring from a patient. | No safeguard against updating an in-use device; no post-update verification/confirmation before return to service; unclear device-state visibility to the engineer. | Serious | Update workflow that prevents/guards updating a device in active clinical use; required post-update verification of correct operation before return to service; clear device-state visibility; controlled, standards-conformant lifecycle procedure. | High; Lifecycle / Maintainability | UR_17 |
| USER_DFMEA_18 | Diagnostic decision support (anchoring on an early candidate) | MMSS shall present ranked real-time diagnostic candidates that converge over time as evidence accumulates (UR_04), each with confidence and reasoning (UR_05). | Clinician anchors on the first diagnostic candidate shown early in the encounter and stops re-appraising as the candidate list updates, converges, or is revised by later data. | Premature diagnostic closure: the working diagnosis is fixed on an early, low-evidence candidate; a condition the AI later up-ranks (or that the clinician's own assessment would catch) is pursued late or missed. | Anchoring and premature closure are among the best-documented diagnostic errors in emergency and critical care; an early ranked suggestion shown before convergence is a powerful anchor, and a clinician who has mentally committed rarely revisits as the list changes. | Early, still-converging candidates not visibly distinguished from a settled result; ranking changes not made salient; no cue that the list has materially revised since the clinician last looked; time pressure rewards early commitment; reasoning/driving parameters not re-checked. | Critical | Visibly distinguish a still-converging/provisional list from a settled one and signal materially changed ranking so a revision is noticed rather than missed; show the driving vital-sign parameters and confidence so a candidate can be re-appraised against current data (UR_05); decision-support framing that invites continued differential thinking rather than early closure (UR_06); explicitly cover anchoring and premature closure in the training mode (UR_12). | High; Safety-critical / Liability | UR_04, UR_05, UR_06 |
| USER_DFMEA_19 | Vital-sign alarm (deliberate silence during resuscitation not restored) | MMSS shall raise distinguishable alarms active until resolved or acknowledged (UR_08) and conform to alarm-safety practice without alarm fatigue (UR_09). | Clinician deliberately silences or suspends alarms during a busy, noisy resuscitation to reduce distraction and then does not re-enable them, leaving the patient effectively unmonitored afterward. | Subsequent deterioration goes unalarmed because the safety function was intentionally suppressed and never restored; harm occurs in a window the team believes is covered. | Audio-off / alarm-suspend during a code is normal, justified clinical behaviour, but failing to restore it is one of the most frequently reported real alarm-safety incidents; a permanent or forgotten silence is far more dangerous than a missed individual alarm. | Silence/suspend has no automatic time limit or auto-reactivation; no persistent, conspicuous reminder that alarms are currently off; the suppressed state is not glanceable amid the resus; no handover prompt that alarms remain disabled. | Critical | Time-limited alarm suspend that auto-restores after a bounded interval rather than indefinite silence; a persistent, conspicuous, glanceable indication whenever alarms are suspended that cannot be lost amid activity; escalating reminder as the suspend window expires; conform to IEC 60601-1-8 audio-pause practice (UR_09); device-side independent audible alarms as a safeguard; cover safe alarm-suspend/restore in training (UR_12). | High; Safety-critical (Class B) | UR_08, UR_09 |
| USER_DFMEA_20 | Handover / shift change (working state not carried across) | MMSS shall present and exchange vital-sign data and diagnostic findings to support second opinion and handover (UR_14), and persistently indicate trustworthiness and alarm/mode state (UR_03, UR_09, UR_10). | At shift change or patient transfer the oncoming clinician does not pick up the current working diagnosis, which channels are flagged untrustworthy, or that alarms/limits were adjusted or suspended, because that state is not surfaced at handover. | Care continues on stale assumptions: a suspect channel is trusted again, an adjusted/suspended alarm is not noticed, or the prior reasoning is lost — leading to a wrong decision or a missed deterioration after handover. | Clinical handover is a recognised high-risk transition where most information loss and downstream error originates; a monitor that holds critical state silently (suspect channels, modified alarm limits, suspended alarms, current candidates) lets that state fall through the gap between two clinicians. | Current trust/alarm/mode state not glanceable to an arriving clinician; modified alarm limits or suspended alarms not flagged on screen; working diagnostic state not summarisable for handover; reliance on verbal handover alone. | Serious | Make the safety-relevant working state persistently glanceable to any clinician arriving at the device — which channels are flagged untrustworthy (UR_10), whether alarms/limits are modified or suspended (UR_09), and the current candidate state; support a concise handover summary/exchange to the receiving clinician or HIS (UR_14); cover structured handover with the device in training (UR_12). | High; Safety-critical (Class B) | UR_14, UR_03, UR_09, UR_10 |

### Use Scenarios

Concrete narratives of how the product is used in the real world, walking from a triggering situation to a successful outcome. Each scenario contains use tasks (UT_*).

#### Scenario 1 — Pre-hospital patient pickup and connection in an ambulance

A paramedic crew reaches a collapsed patient at a roadside. Working alone in a cramped, moving ambulance with no physician on hand, the paramedic powers on MMSS, attaches the non-invasive sensors, and needs the patient's true condition and early diagnostic guidance within seconds to begin stabilising during transport.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_01 | Power on and reach readiness | The paramedic switches on the host platform; MMSS starts and reaches clinical readiness within 10 seconds, showing an explicit "ready" indication and a per-channel acquisition state so the paramedic knows which channels are live versus still acquiring. | UR_02 |
| UT_02 | Attach priority sensors and confirm acquisition | Working alone, the paramedic attaches sensors in clinical priority order — the SpO₂ probe and ECG electrodes first to capture oxygenation and rhythm, then the NIBP cuff, capnometer line, thermal probe, and EEG leads as the situation allows (the source devices in the Acquired Parameters / Signals table); MMSS marks each channel as live only once valid acquisition is confirmed and flags any not-yet-connected, still-acquiring, or unreliable channel rather than showing a plausible normal value, so the paramedic does not trust a value before its sensor is confirmed seated. | UR_01, UR_10 |
| UT_03 | Read vital signs at a glance one-handed | While managing the patient one-handed in the moving vehicle and poor light, the paramedic glances at MMSS and reads each acquired vital-sign parameter (Acquired Parameters / Signals table) with its unit, refreshed at least once per second, with abnormal values unmistakably flagged, and cross-checks each reading against the patient's clinical appearance before relying on it. | UR_01, UR_11 |
| UT_04 | Receive early diagnostic candidates | Having already begun stabilising on the vital signs, the paramedic receives — within seconds of stable acquisition — ranked real-time diagnostic candidates with confidence and supporting reasoning presented alongside the raw vital signs, giving the lone paramedic decision support in the absence of a colleague to consult without holding up immediate care. | UR_04, UR_05 |
| UT_05 | Act on own judgement during transport | The paramedic appraises the candidates as adjunctive decision support, retains authority to begin and adjust treatment on their own assessment, and continues monitoring the glanceable display throughout transport. | UR_06, UR_11 |

#### Scenario 2 — ICU bedside continuous monitoring with an abnormal-condition alarm

A critical-care nurse is responsible for several ICU patients across an extended shift. MMSS continuously monitors one ventilated patient at the bedside while the nurse attends to others; a vital sign deteriorates and the alarm must reach the nurse reliably.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_06 | Maintain continuous bedside monitoring | MMSS remains reliably available throughout the shift, continuously presenting the patient's acquired vital signs (Acquired Parameters / Signals table) with a visible system-health indication so the nurse can trust that monitoring is live while attending to other patients. | UR_03 |
| UT_07 | Detect deterioration and alarm | A vital-sign parameter crosses an abnormal threshold; within 1 second MMSS raises an immediate, unmistakable, distinguishable alarm identifying which parameter is abnormal and its urgency, perceptible across the noisy unit and latching until resolved or acknowledged. | UR_08, UR_09 |
| UT_08 | Distinguish clinical alarm from technical fault | The nurse recognises from the alarm's tone, colour, icon, and text that this is a genuine clinical condition and not a sensor-fault warning, and responds clinically rather than dismissing it. | UR_09, UR_10 |
| UT_09 | Verify the patient, intervene, and acknowledge | The nurse returns to the bedside, reads the flagged parameter and current candidates at a glance, confirms against the patient that the alarm reflects a true clinical change rather than motion artefact, intervenes, and acknowledges the alarm; MMSS keeps the alarm active until the condition resolves or it is explicitly acknowledged. | UR_08, UR_01 |

#### Scenario 3 — Sensor disconnection or misplacement during transport

During a bumpy inter-facility transfer a sensor is jostled loose or misplaced. MMSS must keep the clinician from acting on false or stale data and clearly distinguish the technical fault from a real clinical alarm.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_10 | Detect sensor disconnection or misplacement | A measurement device (from the Acquired Parameters / Signals table) becomes disconnected, misplaced, or starts producing unreliable readings; within 1 second MMSS detects the condition from device-side fault signalling and input inactivity and raises a sensor-fault warning distinguishable from a clinical alarm. | UR_10, UR_09 |
| UT_11 | Mark the affected parameter untrustworthy | MMSS visibly marks the affected parameter as untrustworthy and replaces the value with an explicit no-data/untrustworthy state rather than continuing to show a stale or implausible value as if it were live. | UR_10 |
| UT_12 | Re-seat the sensor and restore trust | The clinician identifies the affected channel from the warning, re-seats or repositions the sensor, and MMSS returns the channel to a live, trusted state once valid acquisition resumes. | UR_10, UR_01 |

#### Scenario 4 — AI diagnostic candidate review and clinician decision in the ER

An emergency physician receives a critically ill patient handed over from the ambulance. The physician uses MMSS's diagnostic candidates as decision support while retaining final authority, guarding against automation bias and premature closure.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_13 | Review ranked candidates with reasoning | Alongside their own primary survey of the handed-over patient, the physician reviews the ranked diagnostic candidates presented within 1 second of receipt, reading each candidate's confidence and the driving vital-sign parameters at a glance, with expandable detail on demand. | UR_04, UR_05 |
| UT_14 | Appraise against the patient | The physician judges whether each candidate fits the patient in front of them, recognising when a candidate rests on a parameter they already distrust, and keeps the wider differential open as the still-converging list updates. | UR_05, UR_06 |
| UT_15 | Decide and retain authority | The physician forms a working diagnosis, acting ahead of or against a suggestion as their judgement dictates; MMSS frames the output as decision support that informs rather than replaces and never gates treatment on a candidate. | UR_06 |
| UT_16 | Share findings for second opinion | The physician shares the vital-sign data and diagnostic findings with the hospital information system over the recognised interoperability standard to obtain a second opinion, with explicit confirmation of successful, secure transfer. | UR_14, UR_15 |

#### Scenario 5 — Diagnosis timeout handling

The patient's presentation is ambiguous and the external diagnostic capability cannot converge on candidates within the expected time. MMSS must tell the clinician clearly so they do not wait indefinitely.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_17 | Recognise the timeout positively | When no diagnostic result can be produced within the expected convergence time, MMSS presents a positive, perceptible timeout indication delivered independently of the failed diagnostic path — never leaving the candidate area silently blank — reinforced by the external capability's own independent audible notification. | UR_07 |
| UT_18 | Fall back on own assessment | Reading the explicit "no diagnosis available — proceed on your own assessment" indication, the clinician stops waiting and proceeds on their own clinical judgement without delaying care, while continuing to monitor the vital signs. | UR_07, UR_06 |

#### Scenario 6 — Handover to the receiving hospital

The ambulance arrives at the receiving hospital and care is transferred to the ED team. MMSS surfaces the working state and shares data so nothing critical falls through the gap between clinicians.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_19 | Surface the working state for handover | At handover MMSS makes the safety-relevant working state glanceable to the arriving clinician — which channels are flagged untrustworthy, whether alarms or limits are modified or suspended, and the current diagnostic candidate state. | UR_10, UR_09, UR_03 |
| UT_20 | Share data and findings to HIS | MMSS exchanges the patient's vital-sign data and diagnostic findings with the hospital information system over the recognised interoperability standard, delivering candidates within 1 second of availability, with explicit confirmation of a successful, complete transfer to the correct patient record. | UR_14 |
| UT_21 | Hand over securely and privately | The clinician confirms the receiving recipient before exchange and MMSS handles the personal health data in conformance with data-protection law throughout, so confidentiality and integrity are preserved through the transfer. | UR_15, UR_14 |
| UT_29 | Confirm continuous monitoring is taken over | Before the ambulance crew disconnects, the receiving clinician transfers the patient onto the ED's monitoring and confirms vital-sign acquisition and alarming are live there; MMSS keeps presenting the patient's vital signs and active alarm state until this handover is complete, so monitoring never lapses in the gap between the two clinicians. | UR_03, UR_08 |

#### Scenario 7 — Training-mode practice session

A clinical trainer runs a risk-free simulated session to build clinician competence — particularly in interpreting AI candidates and avoiding automation bias — with fail-safe separation from live clinical use.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_22 | Enter training mode safely | The trainer enters the simulated training mode with explicit confirmation; MMSS displays a persistent, unmistakable, always-visible mode indicator and watermarks all simulated data so it can never be mistaken for a real patient. | UR_13, UR_12 |
| UT_23 | Run a realistic scenario | The trainer runs realistic scenarios in which simulated vital signs, alarms, sensor faults, and AI candidates behave as in live use, letting clinicians practise reading the display, responding to alarms, and handling timeouts risk-free. | UR_12 |
| UT_24 | Demonstrate AI interpretation and bias avoidance | The trainer demonstrates AI candidate reasoning and confidence and correct interpretation, explicitly coaching against automation bias, anchoring, and premature closure so clinicians keep their judgement in control. | UR_12, UR_05 |
| UT_25 | Exit to live with fail-safe separation | The trainer exits training mode with explicit confirmation; MMSS enforces fail-safe separation and defaults to live operation on return or restart, so a clinician arriving at the device cannot unknowingly treat a live patient in training mode. | UR_13 |

#### Scenario 8 — Commissioning and lifecycle update by clinical engineering

A biomedical engineer installs and verifies MMSS on the host platform across the fleet and, later, applies a controlled software update without disrupting devices in clinical use.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_26 | Connect and verify device interfaces | The engineer connects MMSS to each of the six measurement-device types and to the hospital information system strictly through their published interface contracts, using clear per-channel interface and fault feedback during commissioning. | UR_16 |
| UT_27 | Confirm correct parameter mapping | The engineer completes a guided verification step confirming that each acquired parameter (Acquired Parameters / Signals table) maps to the correct device and display field, and that acquisition, alarming, and data exchange behave correctly, before releasing the device for clinical use. | UR_16 |
| UT_28 | Apply a controlled software update | The engineer applies a software update through the controlled, standards-conformant lifecycle workflow, which prevents updating a device in active clinical use and verifies correct operation before the device is returned to service. | UR_17 |

### Usability FMEA (UFMEA_*)

An FMEA focused on usability: where the user interface, workflow, or interaction model can lead to errors, slow operation, or unsafe outcomes. Where the User DFMEA above asks *how a user might misuse or misinterpret the product*, this UFMEA asks *where the concrete UI, display, alarm, and interaction design lets a competent, motivated user err or slow down* — and is anchored to the use tasks (UT_*) in which the error actually occurs.

**Usability Impact Level (UIL) scale** — combines the clinical consequence of the use error with how readily the interaction provokes it:

- **UIL-4 (Critical)**: an interaction failure that can plausibly contribute to patient death or serious irreversible harm (e.g. a safety-critical signal not perceived, false data trusted as real).
- **UIL-3 (High)**: an interaction failure that can contribute to serious but recoverable harm, a significant treatment delay, or a wrong clinical decision.
- **UIL-2 (Medium)**: an interaction failure causing notable inefficiency, slow task completion, or a recoverable error with limited/transient clinical impact.
- **UIL-1 (Low)**: minor friction or inconvenience with no clinical consequence.

| ID | Scenario Title | Use Error | Cause | Effect | HF Cause | Rationale | Usability Impact Level | Mitigation (existing) | Mitigation (new) | Classification | Traces |
|----|----------------|-----------|-------|--------|----------|-----------|------------------------|-----------------------|------------------|----------------|--------|
| UFMEA_01 | Pre-hospital pickup and connection | Paramedic overlooks an abnormal vital-sign value (e.g. SpO2, HR, EtCO2 from the Acquired Parameters / Signals table) while glancing at the display one-handed in a moving, poorly lit ambulance. | Cluttered or low-contrast layout; many parameters competing for attention; out-of-range distinction carried by colour alone and washed out by glare/vibration; sub-second glance time. | Deterioration not recognised; intervention delayed; patient harm. | Limited attention and a brief glance under motion and poor light; pre-attentive search fails when abnormal values are not visually segregated from normal ones. | A glanceable display is the paramedic's primary window; if an abnormal value does not "pop out" in a one-second glance the safety value of real-time display is lost — exactly the high-workload, low-light condition where this is most likely. | High-contrast glanceable layout with consistent fixed placement per parameter; value shown with unit; abnormal values encoded by colour + shape/icon (not colour alone) and reinforced by the parameter alarm; 1 s refresh. | Validate maximum at-a-glance read time and abnormal-value detection rate in a representative moving/low-light rig during summative testing; tune luminance/contrast and abnormal-value salience to that rig; redundant non-colour coding verified for colour-vision-deficient users. | High; Safety-critical (Class B) | UT_03 |
| UFMEA_02 | Pre-hospital pickup and connection | Paramedic reads a not-yet-acquired channel as a confirmed normal value during the start-up / sensor-attachment window. | A blank, zero, or placeholder rendering is not visually distinct from a real measured value; pressure to act within seconds of power-on; sensors attached in sequence so some channels lag. | Decision made on incomplete data; a yet-to-appear abnormal value missed. | Absence of information read as "normal" rather than "not yet measured" (a classic absence-vs-zero confusion) under time pressure. | The 10 s readiness and staggered sensor attachment create a window where some channels are live and others are not; an undistinguished placeholder positively misleads the user about which data is trustworthy. | Explicit "ready" indication on activation; per-channel acquisition state (acquiring / live / no-data) shown; unacquired channels never rendered as a plausible normal number. | Make the acquiring / no-data state visually unmistakable and never numeric; require valid acquisition before a channel shows a value; verify in formative testing that users correctly classify each channel's state at a glance during the start-up window. | High; Availability | UT_01, UT_02 |
| UFMEA_03 | Pre-hospital pickup and connection | Paramedic trusts and acts on a value from a sensor that is attached but misplaced/poorly seated, which the display shows as a normal live reading. | Misplacement signalled (if at all) only subtly; affected parameter still rendered as a plausible live value; no glanceable per-channel trust cue. | Wrong or falsely reassuring reading drives a wrong diagnosis or masks deterioration (R_04). | Trust calibration fails: a value that looks identical to a good reading carries no perceptual cue that it is suspect. | Sensor misplacement is a Critical risk-register hazard; if the interaction does not surface "this channel is suspect" the clinician cannot calibrate trust and acts on false data. | MMSS marks not-yet-connected / still-acquiring / unreliable channels rather than showing a plausible normal value; reliance on device-side misplacement signalling plus input-inactivity inference; distinct sensor-fault warning. | Add a persistent per-channel trust/quality cue alongside each value (not only an event warning) so suspect channels are continuously visible at a glance; validate that users do not act on a channel marked suspect in formative testing. | High; Safety-critical (Class B) | UT_02 |
| UFMEA_04 | AI diagnostic candidate review | Clinician adopts the top-ranked AI candidate as the diagnosis without independent appraisal (automation bias). | Ranking and a high confidence number presented with the visual authority of a result; reasoning/confidence not absorbed at a glance; time pressure; trust built from prior correct suggestions. | Wrong working diagnosis pursued; correct condition missed or delayed (R_05). | Automation bias — a confident, ranked machine output is over-weighted relative to the clinician's own assessment, especially under load. | R_05 is a Critical hazard; the interaction model (how authoritatively the candidate is rendered) is the lever that either provokes or resists over-trust. | Candidates shown as ranked *suggestions* with confidence and supporting reasoning at a glance; unambiguous decision-support framing/labelling; treatment never gated/pre-selected on a candidate; simulation training covers automation bias. | Use non-authoritative visual framing for candidates (suggestion styling, persistent "decision support — not a diagnosis" affordance); measure automation-bias incidence with seeded plausible-but-wrong candidates in summative testing and set an acceptance threshold. | High; Safety-critical / Liability | UT_13, UT_15 |
| UFMEA_05 | AI diagnostic candidate review | Clinician misreads a confidence score or rank — treats a low-confidence/low-ranked candidate as firm, or dismisses a clinically critical lower-ranked differential. | Confidence shown as a bare percentage without interpretive framing; ranking implies certainty; driving vital-sign parameters not visible at a glance. | Diagnostic reasoning misdirected or narrowed; a treatable time-critical differential acted on late (R_05). | Bare numbers invite mis-weighting; without framing the user cannot tell what a confidence value operationally means. | Mis-reading confidence/rank escalates the R_05 misinterpretation hazard in both directions (over- and under-weighting), so it is a distinct interaction failure from raw over-trust. | Confidence expressed with consistent interpretive framing (not a bare number alone); driving vital-sign parameters shown; expandable detail on demand; confidence/ranking interpretation covered in training. | Standardise a tested confidence-framing scheme (e.g. banded + worded) and verify in formative testing that users interpret high/low confidence correctly; show driving parameters inline so a candidate can be judged against data the user distrusts. | High; Safety-critical / Liability | UT_13, UT_14 |
| UFMEA_06 | AI diagnostic candidate review | Clinician anchors on an early, still-converging candidate and does not notice the ranked list materially revise as evidence accumulates. | Provisional/converging list not visibly distinguished from a settled result; ranking changes not made salient; no cue the list changed since the user last looked. | Premature diagnostic closure; a later up-ranked or self-assessed condition pursued late or missed. | Anchoring and premature closure — once committed, clinicians rarely revisit a changing list, especially under time pressure that rewards early commitment. | An early ranked suggestion shown before convergence is a powerful anchor; the interaction must signal change, not silently update, or the convergence behaviour itself becomes a hazard. | Decision-support framing inviting continued differential thinking; reasoning and driving parameters available for re-appraisal; anchoring/premature closure covered in training. | Visibly distinguish a provisional/converging list from a settled one and make a materially changed ranking salient (change indication) so a revision is noticed rather than missed; verify in testing that users detect a seeded mid-encounter ranking change. | High; Safety-critical / Liability | UT_13, UT_14 |
| UFMEA_07 | ICU bedside continuous monitoring | Nurse does not perceive a vital-sign alarm in a noisy, multi-patient unit while attending another patient away from the bedside. | Insufficient loudness/visual contrast for the environment; alarm not distinguishable from background noise/other alarms; desensitisation from alarm load; nurse out of line-of-sight and earshot of this bed. | Deterioration of a ventilated, dependent patient goes unrescued in the critical first minutes; respiratory/cardiac arrest or irreversible harm before anyone responds (R_07 family). | Auditory/visual signal detection fails under high ambient noise and divided attention across several patients; the nurse is physically remote from the alarming bed; alarm fatigue erodes responsiveness. | A missed alarm defeats the core safety function; perceptibility in noise is a usability/HF property of the alarm design itself, distinct from whether an alarm is raised. | Multi-modal conspicuous alarms (audible + visual) tuned for noisy/mobile use and conforming to alarm-safety practice; latching until resolved/acknowledged; distinct urgency encoding; device-side independent audible alarms as safeguard. | Validate alarm detectability at representative ambient noise levels and viewing distances/angles in summative testing; apply alarm-burden/prioritisation design to limit fatigue and verify detection rate stays acceptable under sustained load. | High; Safety-critical (Class B) | UT_07 |
| UFMEA_08 | ICU bedside continuous monitoring | Nurse confuses a sensor-fault warning with a genuine clinical alarm (or vice versa) and responds inappropriately. | Clinical alarm and fault warning share similar tone/colour/wording; high alarm load erodes discrimination; ambiguous statement of which condition is signalled. | Real deterioration dismissed as a "false alarm", or a technical fault triggers unnecessary clinical intervention. | Signal discrimination fails when two categories of signal are perceptually similar, compounded by alarm fatigue. | Mistaking fault for deterioration (or the reverse) is an explicit alarm-safety hazard leading directly to wrong or omitted action. | Differentiated alarm vs technical-fault signalling (distinct tone, colour, icon, text per IEC 60601-1-8 class); explicit statement of which parameter/device and what condition; consistent encoding reinforced in training. | Validate that users reliably and quickly categorise clinical alarm vs sensor-fault warning (low confusion rate) in summative testing across the full alarm/warning set; lock the distinguishing encoding as a design rule. | High; Safety-critical / Regulatory | UT_08, UT_10 |
| UFMEA_09 | Sensor disconnection or misplacement | Nurse/clinician reads a frozen last-good value as the patient's current reading after a sensor silently fails. | Last-good value retained on screen with no staleness/no-data cue; disconnection not yet inferred; display assumed to be continuously updating. | A deterioration occurring behind the frozen value is actively masked — the reassuring stale number suppresses any clinical suspicion — so a treatable change is missed until the patient is overtly compromised. | A stale value is perceptually identical to a live one, so the user has no cue to distrust it — more dangerous than a blank. | The interaction's handling of input loss (persist vs replace) directly determines whether the user is positively misled. | On input loss over the short inactivity window the value is replaced with an explicit no-data/untrustworthy state; never persists a stale value as live; coupled with the connection/disconnection warning. | Add a freshness/last-updated cue per parameter so even a momentary stall is visible; verify in formative testing that users detect a silently stalled channel before acting on it. | High; Safety-critical (Class B) | UT_11, UT_10 |
| UFMEA_10 | Diagnosis timeout handling | Clinician does not notice that no diagnosis was produced and keeps waiting for a result that will not arrive. | Empty candidate area indistinguishable from "still computing"; timeout cue absent or too subtle; reliance on the same display path that failed to converge. | Treatment delayed while the clinician waits instead of falling back on their own assessment (R_06). | A blank area is read as "in progress" — absence of a result interpreted as work continuing rather than as failure. | R_06 is a Critical hazard; the failure is purely an interaction one — a silent blank versus a positive "no result" signal. | Positive, perceptible timeout indication delivered independently of the failed diagnostic path; explicit "no diagnosis available — proceed on your own assessment" message; reinforced by the external capability's own independent audible timeout notification; never silently blank. | Verify in summative testing that users recognise the timeout and switch to their own assessment within an acceptable time, with no user reading the timeout state as "still computing". | High; Safety-critical (Class B) | UT_17, UT_18 |
| UFMEA_11 | Training-mode practice session | Clinician unknowingly operates MMSS on a live patient while it is still in simulated training mode (or treats simulated data as real). | Mode indication absent, subtle, or not persistent; device left in training mode by a previous user; glanceable mode cue missed in poor light. | Simulated data acted on as real, or a real patient monitored by a simulation — directly endangering the patient. | Mode error / loss of mode awareness — the user's mental model of the device state diverges from the actual state, a classic mode-confusion failure. | The training mode is the named risk control for the Critical clinician-misinterpretation hazard; if mode is ambiguous the control itself becomes a hazard source. | Persistent, unmistakable, always-visible mode indicator (distinct colour/banner) that cannot be dismissed; fail-safe default to live on return/restart; explicit confirmation entering/leaving training; simulated data watermarked. | Validate that every user correctly identifies the active mode at a glance in all lighting conditions, and that a user arriving at a device left in training mode cannot begin live monitoring without an unmistakable cue; set zero-tolerance acceptance for undetected mode. | High; Safety-critical (Class B) | UT_22, UT_25 |
| UFMEA_12 | Pre-hospital transport (one-handed mobile use) | Clinician makes a slip/selection error one-handed in a moving vehicle — e.g. silences an alarm, changes a setting, or mis-acknowledges — unintentionally. | Small/closely-spaced targets; controls needing precise input or two hands; legibility lost in vibration/poor light; no confirmation/guard on safety-significant actions. | Unintended action degrades monitoring safety (e.g. alarm silenced, limit changed) or slows the task. | Motor slips and reduced precision under vibration and one-handed operation; small targets exceed achievable pointing accuracy. | Mobile/pre-hospital one-handed use is a defining environment; controls not designed for it invite slips that can suppress safety functions or slow time-critical tasks. | Large, well-spaced, one-handed-operable controls; confirmation/guarding on safety-significant actions (e.g. alarm-off); high legibility under movement/poor light; usability evaluation in the mobile environment. | Specify and verify minimum touch-target size/spacing and confirm acceptable error/slip rate and task time for safety-significant actions in a representative moving rig; guard destructive/safety actions against single accidental activation. | High; Safety-critical / Usability | UT_05, UT_03 |
| UFMEA_13 | ICU resuscitation (alarm suspend) | Clinician silences/suspends alarms during a busy resuscitation and the suspended state is not noticed afterward, leaving the patient effectively unmonitored. | Suspend has no visible time limit or auto-restore; no persistent conspicuous "alarms off" reminder; the suppressed state not glanceable amid resus activity; the silence often set by one clinician but inherited by another after the team disperses. | Subsequent deterioration goes entirely unalarmed because the safety function stays suppressed indefinitely; harm or arrest occurs in a window the whole team falsely believes is actively monitored. | Prospective-memory failure — the intention to re-enable alarms is lost amid high workload and the post-resus handoff; the suppressed state lacks a salient persistent cue and no one owns its restoration. | Forgotten alarm suspension is among the most frequently reported real alarm-safety incidents; the interaction (time-limited vs indefinite, salient vs hidden) determines whether the lapse is caught. | Time-limited suspend with auto-restore; persistent conspicuous glanceable "alarms suspended" indication that cannot be lost; escalating reminder as the window expires; conform to IEC 60601-1-8 audio-pause practice; device-side independent audible alarms as safeguard. | Verify in summative testing that users always perceive the suspended-alarm state and that auto-restore/escalating reminders prevent an indefinitely silenced monitor; bound the maximum suspend interval. | High; Safety-critical (Class B) | UT_07, UT_09 |
| UFMEA_14 | Handover to the receiving hospital | Arriving clinician misses safety-relevant working state at handover — which channels are untrustworthy, that alarms/limits are modified or suspended, or the current candidate state. | Trust/alarm/mode state not glanceable to an arriving clinician; modified limits or suspended alarms not flagged on screen; working diagnostic state not summarised; reliance on verbal handover alone. | Care continues on stale assumptions — a suspect channel re-trusted, a suspended alarm unnoticed, prior reasoning lost — causing a wrong decision or missed deterioration after handover. | Information transfer loss at a handover boundary — state held silently by the device falls through the gap between two clinicians. | Clinical handover is a recognised high-risk transition where most information loss originates; surfacing held state is an interaction-design responsibility. | Safety-relevant working state made persistently glanceable to any arriving clinician (untrustworthy channels, modified/suspended alarms/limits, current candidate state); concise handover summary/exchange to the receiving clinician or HIS; structured handover covered in training. | Provide and validate a concise at-a-glance handover view that the arriving clinician can absorb in seconds; verify in summative testing that arriving users correctly identify modified/suspended alarms and suspect channels before resuming care. | High; Safety-critical (Class B) | UT_19, UT_29 |
| UFMEA_15 | Handover to the receiving hospital | Clinician believes data/findings were shared with the receiving hospital when the exchange silently failed, was partial, or went to the wrong record. | No (or unnoticed) confirmation of successful transfer; partial transfer not flagged; ambiguous patient/record association; connectivity failure (R_03) unsurfaced. | Receiving team acts without, or on incomplete/mismatched, information; second opinion and handover compromised. | A silent or weak feedback signal leaves the user with a false belief the action succeeded (completion/feedback gap). | Handover is a high-risk transition; without explicit positive confirmation the user cannot tell a failed transfer from a successful one. | Explicit success/failure confirmation of the exchange; partial/failed transfer flagged with retry; unambiguous patient-record association; secure standards-based exchange. | Require an unmistakable transfer-confirmation step the user must perceive (success vs failure vs partial) and verify recipient/record before send; validate that users never proceed believing a failed/partial transfer succeeded. | High; Interoperability | UT_20, UT_16 |
| UFMEA_16 | Commissioning and lifecycle update | Biomedical engineer mis-maps a device channel during commissioning (a parameter routed to the wrong display field) and it goes unnoticed before clinical release. | Unclear commissioning feedback; no enforced verification confirming each channel maps to the correct device/parameter; ambiguous interface status. | A parameter is displayed/alarmed against the wrong channel in clinical use, propagating to wrong clinical decisions for every subsequent patient. | A setup error made once is not caught because the verification interaction does not force per-channel confirmation; the consequence is latent and silent. | A configuration error at commissioning silently affects every patient until detected, so the commissioning interaction must make mis-mapping impossible to miss. | Clear per-channel interface and fault feedback during commissioning; a guided verification/confirmation step that each parameter (Acquired Parameters / Signals table) maps to the correct device before clinical release; unambiguous interface status. | Make the guided per-channel verification mandatory and self-evidencing (engineer confirms each parameter against its source device with a visible cross-check) before the device can be released; verify the workflow blocks release on any unconfirmed channel. | High; Integration | UT_26, UT_27 |
| UFMEA_17 | ICU bedside continuous monitoring | Clinician reflexively dismisses a genuine clinical alarm as motion artefact (or, conversely, intervenes on an artefactual alarm) without the display affording a quick way to distinguish the two at the bedside. | Alarm presents only the breached value with no signal-quality/waveform context to support an artefact-vs-real judgement; high prevalence of artefact alarms in mobile/agitated patients trains a "dismiss first" habit; verification against the patient is rushed under load. | A true deterioration is waved off as "just artefact" and intervention is omitted, or scarce resuscitation effort is spent on a non-event — both eroding trust in the monitor and the alarm system over time. | Cry-wolf / habituation — repeated artefact alarms condition the clinician to disbelieve the alarm category, so signal-vs-noise discrimination defaults to dismissal exactly when a real alarm arrives. | Motion-artefact alarms are the dominant source of clinical alarm burden in transport and agitated ICU patients; if the interaction gives no fast, trustworthy basis to separate artefact from a real change, clinicians rationally but dangerously default to ignoring the alarm. | Alarm identifies the specific abnormal parameter and urgency and presents alongside the live value/waveform so the clinician can sanity-check against signal quality; UT_09 requires confirming the alarm against the patient before acting/dismissing; sensor-fault vs clinical-alarm differentiation (UFMEA_08) reduces miscategorisation; artefact handling covered in training. | Present a glanceable signal-quality/plausibility cue with each alarm so artefact and true change are quickly separable at the bedside, and apply artefact-rejection/alarm-burden design to cut nuisance alarms; verify in summative testing that users neither dismiss a seeded genuine alarm as artefact nor intervene on a seeded artefact alarm. | High; Safety-critical (Class B) | UT_08, UT_09 |

### Usability Requirements (USR_*)

Measurable requirements for how the product must perform from a user perspective: task completion times, error rates, learnability, accessibility. Validated through usability testing.

| ID | Requirement | Classification | Traces |
|----|-------------|----------------|--------|
| USR_01 | In summative usability testing in a representative moving / low-light ambulance rig, at least 95% of trained clinicians shall correctly read each displayed vital-sign parameter (Acquired Parameters / Signals table, Context) — value and unit — within a single 2-second glance, with no misread of a parameter's value or unit. | High; Safety-critical (Class B) | UR_01, UFMEA_01 |
| USR_02 | In summative testing, at least 95% of trained clinicians shall correctly recognise an abnormal (out-of-range) vital-sign value (any parameter in the Acquired Parameters / Signals table) within 3 seconds of looking at the display, under representative motion, glare, and noise, with a missed-abnormal-value rate of ≤ 2% across the test corpus; abnormal-value salience shall remain effective for colour-vision-deficient users (redundant non-colour coding verified). | High; Safety-critical (Class B) | UR_01, UFMEA_01 |
| USR_03 | In summative testing, when a vital-sign alarm is raised, at least 99% of trained clinicians shall perceive the alarm within 5 seconds and correctly identify which acquired parameter (Acquired Parameters / Signals table) is abnormal and its urgency, at representative ambient noise levels (validated up to the specified worst-case dB(A)) and at representative viewing distances and angles, including when attending another patient. | High; Safety-critical (Class B) | UR_08, UFMEA_07, UFMEA_17 |
| USR_04 | In summative testing, at least 95% of trained clinicians shall correctly distinguish a clinical vital-sign alarm from a sensor-fault warning across the full alarm/warning set, with a category-confusion rate of ≤ 2%, sustained under representative alarm-load conditions. | High; Safety-critical / Regulatory | UR_09, UFMEA_08 |
| USR_05 | In summative testing using seeded plausible-but-incorrect AI candidates, the proportion of trained clinicians who adopt the top-ranked candidate as their working diagnosis without independent appraisal (automation-bias incidence) shall not exceed 10%; at least 90% shall correctly state that the diagnostic output is decision support that does not replace their judgement. | High; Safety-critical / Liability | UR_05, UR_06, UFMEA_04 |
| USR_06 | In summative testing, at least 90% of trained clinicians shall correctly interpret a candidate's confidence and rank (correctly classifying high- vs low-confidence candidates and not dismissing a seeded clinically critical lower-ranked differential), and shall correctly identify the driving vital-sign parameters shown for that candidate. | High; Safety-critical / Liability | UR_05, UFMEA_05 |
| USR_07 | In summative testing with a seeded mid-encounter change to the converging candidate list, at least 90% of trained clinicians shall notice the materially changed ranking and re-appraise, rather than anchoring on the earlier candidate (premature-closure incidence ≤ 10%). | High; Safety-critical / Liability | UR_04, UR_05, UFMEA_06 |
| USR_08 | In summative testing where a diagnostic result fails to converge, 100% of trained clinicians shall recognise the timeout state as "no result" (no user reading it as "still computing") and switch to their own assessment within 10 seconds of the timeout indication. | High; Safety-critical (Class B) | UR_07, UFMEA_10 |
| USR_09 | In summative testing across all lighting conditions, 100% of trained clinicians shall correctly identify the active operating mode (training vs live) at a glance, and no clinician arriving at a device left in training mode shall begin live monitoring without an unmistakable cue — zero undetected mode errors. | High; Safety-critical (Class B) | UR_13, UFMEA_11 |
| USR_10 | In summative testing where a sensor is silently disconnected, misplaced, or stalled, at least 95% of trained clinicians shall recognise the affected parameter (Acquired Parameters / Signals table) as untrustworthy and not act on it within 5 seconds, with no clinician acting on a frozen/stale value as if it were a current live reading. | High; Safety-critical (Class B) | UR_10, UFMEA_03, UFMEA_09 |
| USR_11 | In a representative moving-vehicle rig, at least 95% of trained clinicians shall complete each safety-significant one-handed task (e.g. acknowledge an alarm, read all parameters, navigate to candidate detail) successfully within its target time, with an unintended-activation (slip) rate on safety-significant controls of ≤ 1%; touch-target size and spacing shall meet the specified minimum. | High; Safety-critical / Usability | UR_11, UFMEA_12 |
| USR_12 | In summative testing of the alarm-suspend function, 100% of trained clinicians shall correctly perceive that alarms are suspended whenever they are, and no test session shall end with the monitor left indefinitely silenced; the suspend interval shall auto-restore within the specified bounded maximum and an escalating reminder shall be perceived before it expires. | High; Safety-critical (Class B) | UR_08, UR_09, UFMEA_13 |
| USR_13 | At handover, at least 95% of arriving clinicians shall, within 15 seconds and before resuming care, correctly identify from the at-a-glance handover view which channels are flagged untrustworthy, whether alarms or limits are modified or suspended, and the current candidate state. | High; Safety-critical (Class B) | UR_14, UFMEA_14 |
| USR_14 | In summative testing of HIS data exchange, at least 98% of clinicians shall correctly perceive whether a transfer succeeded, failed, or was partial, and no clinician shall proceed believing a failed or partial transfer succeeded; recipient/patient-record association shall be confirmed before send. | High; Interoperability | UR_14, UFMEA_15 |
| USR_15 | The guided per-channel commissioning verification shall block release on any unconfirmed channel: in testing, 100% of biomedical engineers shall confirm each acquired parameter (Acquired Parameters / Signals table) against its correct source device before clinical release, and a seeded mis-mapping shall be detected and corrected in 100% of sessions. | High; Integration | UR_16, UFMEA_16 |
| USR_16 | A clinician trained on MMSS via the simulated training mode shall, within a single defined training session and with no prior MMSS exposure, achieve the per-task success and time targets (USR_01–USR_13) on their first live-equivalent attempt, demonstrating learnability for a trained medical professional. | High; Safety-critical (named risk control) | UR_12, UFMEA_11 |
| USR_17 | The vital-sign display shall be legible — all parameter values, units, and out-of-range flags correctly read — across the full specified range of ambient illumination (from direct glare to darkness) and at the specified viewing distance, and alarms shall remain perceptible up to the specified worst-case ambient noise level, verified in accessibility/legibility testing. | High; Safety-critical / Usability | UR_11, UFMEA_01, UFMEA_07 |

## Concept

### UI/UX Design

Wireframes, interaction flows, navigation structures, and visual design principles that translate the user requirements into a tangible concept.

This section translates the user requirements (UR_*), usability requirements (USR_*), and the use errors catalogued in the User DFMEA and UFMEA into a concrete, tangible MMSS interface concept. Because MMSS renders onto an *existing* portable patient-monitor display (Monitor display context element, IF_08) and is operated by a clinician whose hands and attention are mostly on the patient, every layout choice below is driven by one overriding goal: a safety-critical fact must be readable, and a safety-critical action performable, in a single glance and a single one-handed touch, under motion, glare, and noise.

#### Design Drivers and Governing Principles

The whole concept is shaped by a small set of governing principles, each tied to the requirements and use errors it serves:

- **Glanceability over density** — fixed, never-moving placement per parameter so the eye learns where to look; pre-attentive "pop-out" of anything abnormal (UR_01, USR_01, USR_02, UFMEA_01).
- **Redundant, non-colour-only coding** — every safety-significant state is encoded by at least two of {colour, shape/icon, position, text}, so it survives glare, vibration, and colour-vision deficiency (USR_02, USR_17, accessibility).
- **Absence is never silence** — a not-yet-acquired, stalled, lost, untrustworthy, or "no diagnosis" state is always shown as an *explicit positive state*, never as a blank, a zero, or a frozen last-good value (UR_07, UR_10, UFMEA_02, UFMEA_09, UFMEA_10).
- **Clinician-in-control framing** — diagnostic output is styled and labelled as non-authoritative *suggestion*, never as a result that gates care (UR_05, UR_06, UFMEA_04).
- **Distinct signal categories** — clinical alarm, sensor-fault warning, and timeout each have a unique, locked tone/colour/icon/text signature so they can never be confused (UR_08, UR_09, UFMEA_08).
- **One-handed, large-target interaction** — every safety-significant control is reachable and actuable one-handed with guarded confirmation against accidental activation (UR_11, USR_11, UFMEA_12).
- **Persistent mode and system-health truth** — operating mode (training vs live) and monitoring liveness are always-visible and unmistakable (UR_03, UR_13, UFMEA_11, UFMEA_13).

#### Screen Architecture and Navigation

MMSS is built around a single, always-resident **Main Monitoring Screen** that is never fully replaced — overlays and side panels expand *from* it without ever hiding the vital-signs tiles or the persistent status bars. This keeps the patient's true state and the alarm/mode state continuously visible no matter what the clinician is doing, which is what allows the glance-and-go interaction the pre-hospital and ICU environments demand.

```
NAVIGATION MODEL  (overlays/panels never hide the vital-signs tiles or status bars)

                 ┌──────────────────────────────────────┐
                 │        MAIN MONITORING SCREEN         │  ← always resident
                 │  (vital tiles + AI panel + bars)      │
                 └───┬──────────┬───────────┬────────────┘
       glance/tap    │          │           │
                     ▼          ▼           ▼
            ┌─────────────┐ ┌──────────┐ ┌─────────────────┐
            │ Candidate    │ │ Alarm    │ │ Handover view   │
            │ detail       │ │ ack /    │ │ (at-a-glance    │
            │ (reasoning,  │ │ suspend  │ │ working state)  │
            │ confidence,  │ │ overlay  │ │ + HIS share     │
            │ drivers)     │ │          │ │                 │
            └─────────────┘ └──────────┘ └─────────────────┘

  Engineering / commissioning + training-entry are reached only from a
  guarded menu; TRAINING mode, once active, is shown by a persistent banner
  on EVERY screen above (see Training/Live indicator).
```

All interaction is reversible and shallow: no safety-critical fact is ever more than one tap away, and the clinician can always return to the Main Monitoring Screen with a single large, fixed-position control. There is **no workflow path that requires an AI result before the clinician can act** — the decision to treat is always available directly from the main screen (UR_06, UFMEA_04).

#### Main Monitoring Screen Layout

The screen is divided into three persistent zones: a top **Status Bar** (mode, system health, time, alarm-state summary), a left/centre **Vital-Signs Tile Grid**, and a right **AI Diagnostic-Candidate Panel**. The tile grid enumerates exactly the parameters in the **Acquired Parameters / Signals** table (Context), one tile per parameter, in a fixed clinical-priority order.

```
┌─ STATUS BAR ───────────────────────────────────────────────────────────────┐
│ ● LIVE   ♥ system OK   12:04:31   [ALARMS: ON]        ⌁ HR alarm ACTIVE ⚠   │
├──────────────────────────────────────────┬─────────────────────────────────┤
│ VITAL-SIGNS TILES (fixed placement)      │ AI DIAGNOSTIC CANDIDATES        │
│                                          │ ─ decision support (not a        │
│ ┌───────────⚠──────────┐ ┌──────────────┐│   diagnosis) ────────────────┐  │
│ │ HEART RATE        ▲  │ │ SpO2         ││ │ 1 ▸ Septic shock      72% ▓▓▓│  │
│ │   148   bpm  OUT-HIGH │ │   97  %      ││ │      drivers: HR▲ Temp▲ RR▲  │  │
│ │   (red + ▲ + border) │ │   normal     ││ │ 2 ▸ Hypovolaemia      18% ▓  │  │
│ └──────────────────────┘ └──────────────┘│ │      drivers: BP▼ HR▲        │  │
│ ┌──────────────────────┐ ┌──────────────┐│ │ 3 ▸ Cardiogenic       …  6%  │  │
│ │ SYS/DIA BP    mmHg    │ │ RESP RATE    ││ │ ──────────────────────────── │  │
│ │   88 / 54            │ │   28 /min ▲  ││ │  ⟳ converging…  (provisional)│  │
│ │   MAP 65            │ │   OUT-HIGH   ││ │  ▸ tap a candidate for detail│  │
│ └──────────────────────┘ └──────────────┘│ └──────────────────────────────┘  │
│ ┌──────────────────────┐ ┌──────────────┐│                                 │
│ │ EtCO2   mmHg         │ │ TEMP   °C    ││  [ I'LL DECIDE ]  ← always-      │
│ │   31  ▼  OUT-LOW     │ │  39.1 ▲      ││   available; care never gated   │
│ └──────────────────────┘ └──────────────┘│   on an AI result               │
│ ┌──────────────────────┐ ┌──────────────┐│                                 │
│ │ PULSE RATE  bpm      │ │ BIS          ││                                 │
│ │   146               │ │   —  NO DATA ││  ← explicit no-data state,       │
│ └──────────────────────┘ │  (sensor?)   ││     never blank/zero            │
│                          └──────────────┘│                                 │
└──────────────────────────────────────────┴─────────────────────────────────┘
```

Each tile follows one fixed template so the eye always finds the same information in the same place (UFMEA_01):

```
┌─ PARAMETER TILE (anatomy) ──────────────┐
│ HEART RATE              ⟵ label (fixed)  │
│  148    bpm            ⟵ value + UNIT    │  unit always shown → USER_DFMEA_01
│  ▲  OUT-HIGH          ⟵ range flag       │  shape(▲/▼)+word+colour → USR_02
│ [██████ trust ████]   ⟵ trust/freshness  │  persistent per-channel cue → UFMEA_03
└─────────────────────────────────────────┘

  STATE RENDERINGS for the same tile (absence is never silence):
   • LIVE & normal   :  value, unit, calm neutral background
   • OUT-OF-RANGE    :  value + ▲/▼ + "OUT-HIGH/LOW" + red border + colour (USR_02)
   • ACQUIRING       :  "··· acquiring", animated, NOT a number (UFMEA_02)
   • NO DATA / LOST  :  "— NO DATA", hatched fill, never a stale number (UFMEA_09)
   • UNTRUSTWORTHY   :  value greyed + struck + "SENSOR?" + fault icon (UFMEA_03)
```

Key tile behaviours and the errors they defeat:

- Every value carries its **unit** inline (USER_DFMEA_01), refreshes at least once per second, and shows an **out-of-range flag using colour + an up/down arrow + the words OUT-HIGH/OUT-LOW** so abnormality survives glare and colour-blindness (UR_01, USR_01, USR_02, USR_17, UFMEA_01).
- A **persistent per-channel trust/freshness bar** sits under every value — not just an event warning — so a suspect or stalled channel is continuously visible at a glance, defeating silent trust in misplaced/stale data (UR_10, UFMEA_03, UFMEA_09, USR_10).
- During start-up and staggered sensor attachment, an unacquired channel renders an explicit, **non-numeric "acquiring" state**, never a plausible normal number, so absence is not read as "normal" (UR_02, UFMEA_02, USR_16).

#### AI Diagnostic-Candidate Panel

The candidate panel is deliberately styled to look like *advice*, not a verdict. It sits to the side of (never on top of) the vitals, carries a permanent "decision support — not a diagnosis" header, and lists ranked candidates each with a confidence band and the **driving vital-sign parameters** drawn from the Acquired Parameters / Signals set, so the clinician can immediately see whether a candidate rests on a parameter they already distrust (UR_05, USR_06).

```
┌─ AI DIAGNOSTIC CANDIDATES ───────────────────────────────┐
│  DECISION SUPPORT — informs, does not replace you   ⓘ     │  ← persistent framing (UR_06)
├──────────────────────────────────────────────────────────┤
│ 1 ▸ Septic shock        CONFIDENCE  HIGH  72% ▓▓▓▓▓░░     │  banded + worded + % (USR_06)
│       driving: Heart Rate ▲ · Temp ▲ · Resp Rate ▲        │  ← drivers inline (UFMEA_05)
│ 2 ▸ Hypovolaemia        CONFIDENCE  LOW   18% ▓░░░░░░     │
│       driving: Systolic BP ▼ · Heart Rate ▲               │
│ 3 ▸ Cardiogenic shock   CONFIDENCE  LOW    6% ▓░░░░░░     │
│ ─────────────────────────────────────────────────────────│
│ STATE:  ⟳ CONVERGING (provisional — ranking may change)   │  provisional ≠ settled (UFMEA_06)
│         ✔ SETTLED       or       ⚑ RANKING CHANGED ↑↓     │  change made salient (USR_07)
│ ▸ tap any candidate → reasoning / confidence / drivers    │  expandable detail (UR_05)
└──────────────────────────────────────────────────────────┘
```

Anti-bias and anti-anchoring design choices:

- Candidates use **non-authoritative "suggestion" styling** (lower visual weight than the vitals, no result-like emphasis) to resist automation bias (UR_06, UFMEA_04, USR_05).
- Confidence is shown as a **banded + worded + numeric** triple (e.g. "HIGH 72%"), never a bare percentage, so it cannot be mis-weighted (UFMEA_05, USR_06).
- A **provisional/converging list is visibly distinct from a settled one**, and any material re-ranking raises a salient "RANKING CHANGED" cue so a revision is noticed rather than missed — directly countering anchoring and premature closure (USER_DFMEA_18, UFMEA_06, USR_07).
- Tapping a candidate expands **reasoning + confidence + driving parameters** on demand, absorbable at a glance yet deeper when chosen (UR_05).

#### Alarm Presentation — Clinical vs Sensor-Fault vs Timeout

The three signal categories are given **locked, mutually distinct signatures** across tone, colour, icon, text, and position so they can never be confused, conforming to alarm-safety practice (UR_08, UR_09, UFMEA_08, USR_03, USR_04). Alarms are multi-modal (audible + visual), latch until resolved or acknowledged, and remain perceptible in noise and poor light.

```
┌─ ALARM / WARNING SIGNATURES (locked, never reused across categories) ───────┐
│ CLINICAL ALARM  │ ⚠ red, urgent pulsing tone, "⚠ HR 148 OUT-HIGH — URGENT" │
│  (vital sign)   │   border flash on the offending TILE + status-bar banner  │
│─────────────────┼──────────────────────────────────────────────────────────│
│ SENSOR-FAULT    │ 🔧 cyan/amber, distinct two-tone chirp, "SENSOR FAULT —   │
│  WARNING        │   SpO2 probe — check placement", wrench icon, on the tile  │
│─────────────────┼──────────────────────────────────────────────────────────│
│ DIAGNOSIS       │ ⌛ neutral, soft distinct tone, positive banner in the     │
│  TIMEOUT        │   candidate panel: "NO DIAGNOSIS — proceed on your own    │
│                 │   assessment" (also raised independently by the AI svc)    │
└─────────────────────────────────────────────────────────────────────────────┘

ALARM ACKNOWLEDGE / SUSPEND OVERLAY (one-handed, guarded)
┌───────────────────────────────────────────────┐
│  ⚠ HEART RATE 148 bpm  OUT-HIGH (URGENT)       │
│  [  ACKNOWLEDGE  ]      ← large, latches off    │
│  [  SUSPEND 2 min ]     ← time-limited only;    │
│        auto-restores; escalating reminder       │
│  ✕ cannot indefinitely silence (UFMEA_13)       │
└───────────────────────────────────────────────┘
```

- The alarm always **names the specific parameter and its urgency** and flashes the offending tile, so the clinician knows what and how urgent at a glance, perceptible in noise and at distance (UR_08, USR_03).
- Sensor-fault warnings are perceptually and textually **distinct from clinical alarms** ("SENSOR FAULT — check placement", wrench icon, different tone), so a fault is never treated as deterioration or vice versa (UR_09, UR_10, UFMEA_08, USR_04). An accompanying **signal-quality/plausibility cue** on the alarming tile lets the clinician quickly separate genuine change from motion artefact (UFMEA_17).
- Alarm **suspend is time-limited with auto-restore and an escalating reminder**, and an unmistakable "ALARMS SUSPENDED" banner persists whenever alarms are off — never an indefinite, forgotten silence (UFMEA_13, USR_12).

#### Diagnosis-Timeout Indication

When the external diagnostic capability cannot converge in time, the candidate panel shows a **positive "NO DIAGNOSIS — proceed on your own assessment" state**, delivered on a path independent of the failed diagnostic flow and reinforced by the AI service's own audible notification. The area is **never left blank** (a blank reads as "still computing"), so the clinician stops waiting and falls back on their own judgement (UR_07, UFMEA_10, USR_08).

#### Training / Live Mode Indicator

Operating mode is the single most safety-critical piece of state on the screen and is therefore made impossible to miss: a **full-width, persistent, non-dismissible banner** on every screen, with a distinct colour and pattern, plus a watermark across all simulated data. The system **fails safe to LIVE** on restart or when a user returns to the device, and entering/leaving training requires explicit confirmation (UR_13, UR_12, UFMEA_11, USR_09).

```
┌════════════════════════════════════════════════════════════════════════════┐
║  ▓▓ TRAINING MODE — SIMULATED DATA — NOT A REAL PATIENT ▓▓   (cannot dismiss)║
└════════════════════════════════════════════════════════════════════════════┘
   • distinct colour + diagonal-hatch pattern (survives poor light, USR_09)
   • watermark "SIMULATED" tiled across the vitals + candidate areas
   • LIVE mode: no banner, normal chrome → the two states are unmistakable
   • restart / new user → defaults to LIVE (fail-safe); entering TRAINING needs
     explicit confirm; leaving TRAINING needs explicit confirm
```

#### Interaction Flow — One-Handed, Glanceable

The interaction model is designed so the dominant loop — *glance → read → (optionally) acknowledge → return* — is achievable one-handed under motion. Controls for safety-significant actions are **large, well-spaced touch targets** with confirmation/guarding so a slip cannot silence an alarm or change a limit unintentionally (UR_11, USR_11, UFMEA_12). The primary clinical loop:

```
power on ──► [readiness ≤10s, per-channel acquiring state] ──► MAIN SCREEN
   │                                                              │
   │  glance ◄───────────────────────────────────────────────────┤
   │    ├─ all vitals + units + range flags read in one glance    │ (UR_01/USR_01)
   │    ├─ trust bar shows any suspect/stale channel              │ (UFMEA_03/09)
   │    └─ candidate panel = side advice, not a gate              │ (UR_06)
   │                                                              │
   │  ALARM? ─► offending tile flashes + named banner + tone ─►   │
   │            one big tap: ACKNOWLEDGE (latches) or SUSPEND 2m  │ (USR_03/12)
   │                                                              │
   │  need detail? ─► one tap → candidate reasoning/drivers ─► back│ (UR_05)
   │                                                              │
   │  hand over? ─► one tap → at-a-glance handover view + HIS share│ (UR_14/USR_13)
   └──────────────────────────────────────────────────────────────┘
```

A dedicated **handover view** surfaces the safety-relevant working state — which channels are flagged untrustworthy, whether alarms/limits are modified or suspended, and the current candidate state — absorbable in seconds by an arriving clinician, and offers a confirmed, success/failure-explicit HIS share so nothing falls through the gap at shift change or transfer (UR_14, UFMEA_14, UFMEA_15, USR_13, USR_14). For commissioning, a **guided per-channel verification** flow forces the biomedical engineer to confirm each acquired parameter against its correct source device and blocks clinical release on any unconfirmed channel (UR_16, UFMEA_16, USR_15).

#### Visual Design Principles

- **Legibility first.** Large numerals, high contrast, and a luminance/contrast scheme validated across the full ambient range from direct glare to darkness at the specified viewing distance; alarms perceptible up to the worst-case ambient noise (USR_17, UFMEA_01, UFMEA_07).
- **Colour with redundancy, never colour alone.** Red = clinical alarm/abnormal, amber/cyan = sensor fault, neutral = normal/timeout — but every such state is *also* carried by shape, icon, position, and text, so it remains correct for colour-vision-deficient users (USR_02, USR_04, accessibility).
- **Information hierarchy by clinical priority.** Vital signs and alarms dominate the visual field; AI candidates are deliberately secondary; chrome and navigation are quietest of all — so the eye is drawn first to what can harm the patient soonest (UR_01, UR_06, UFMEA_04).
- **Stability of layout.** Parameters never move; the same fact is always in the same place, so the clinician's learned glance pattern holds across patients and shifts (UFMEA_01).
- **Positive state always.** No safety-relevant fact is ever conveyed by absence — acquiring, no-data, untrustworthy, suspended-alarm, training-mode, and no-diagnosis are all explicit, named states (UR_07, UR_10, UR_13, UFMEA_02, UFMEA_09, UFMEA_10, UFMEA_11, UFMEA_13).

### Actors

Individuals, groups, or systems that perform roles or tasks within the system or process.

| Actor | Description |
|-------|-------------|
| Pre-hospital Clinician | Human actor. Paramedic or pre-hospital emergency clinician who connects the patient and operates MMSS at the scene and in a moving ambulance, typically alone or in a small crew with no physician on hand. Primary user driver of MMSS: powers it on and reads the at-a-glance vital-signs display, relies on its ranked diagnostic candidates and timeout signalling in place of expert backup, responds to its alarms and sensor-fault warnings one-handed under time pressure, and triggers sharing of patient data with the receiving hospital ahead of arrival. The actor for whom the mobile/pre-hospital usability and safety case is demonstrated. |
| Emergency Physician | Human actor. Qualified emergency/critical-care physician who uses MMSS in the emergency room and on incoming patients and holds final diagnostic and treatment authority. Reads MMSS vital signs and alarms, critically appraises the AI diagnostic candidates with their reasoning and confidence as adjunctive decision support rather than deferring to them, acts on the no-diagnosis timeout signal, and uses MMSS data exchange with the hospital information system for second opinion and handover. The actor against whom MMSS must reinforce decision-support framing and resist automation bias. |
| Critical-Care Nurse | Human actor. Registered ICU/ER nurse providing continuous bedside monitoring; the user most often watching MMSS over extended shifts. Sets up the sensors, responds first to MMSS alarms, distinguishes clinically significant alarms from sensor-fault warnings, tracks trends on the continuous display while attending to other patients, and escalates diagnostic and treatment decisions to a physician. The actor for whom MMSS sustained-use alarm-safety and sensor-fault interactions must be demonstrated. |
| Clinical Trainer / Super-User | Human actor. Senior clinician (educator, clinical specialist, or super-user) designated as the local expert who trains colleagues on MMSS and champions its safe use. Primary user of the risk-free simulated training mode: runs realistic scenarios, demonstrates and explains AI candidate reasoning and confidence and correct interpretation, and ensures trainees never confuse simulated data with a real patient. Because training mode is the named risk control for the clinician-misinterpretation hazard, this actor is central to mitigating use error across the deployed fleet. |
| Biomedical / Clinical Engineer | Human actor. Clinical-engineering technician who installs, configures, integrates, verifies, and maintains MMSS on the host platform across the fleet — not a clinical user during patient care. Connects MMSS to the measurement devices and the hospital information system through their defined interface contracts, validates correct acquisition, alarming, and data exchange, applies controlled software updates, and supports troubleshooting and serviceability over the service life. |
| Measurement Devices (ECG monitor, Pulse oximeter, BP monitor, Thermal probe, Capnometer, EEG monitor) | System actor. The six existing, externally-supplied measurement devices that acquire the patient's physiological signals and supply the vital-sign parameters listed in the Acquired Parameters / Signals table to MMSS over their published acquisition interfaces (IF_02–IF_07). Each device also raises its own independent connection/fault alarms. They are the upstream data sources MMSS conditions, displays, alarms on, and forwards for diagnosis; not designed in this project. |
| Monitor Display | System actor. The existing connected display of the portable patient monitor on which MMSS renders vital signs, alarms, and ranked diagnostic candidates over the published display interface (IF_08). The output endpoint through which MMSS presents all clinical information to the human actors; not designed in this project. |
| External Diagnostic AI Capability | System actor. The commercially validated, off-the-shelf diagnostic AI service (Open Evidence class) external to MMSS. Receives conditioned patient data from MMSS over the diagnostic AI interface (IF_09) and returns structured, ranked diagnostic candidates with reasoning and confidence within the validated scope of its own intended use; raises its own independent audible time-out notification on convergence failure. The decision-support engine MMSS integrates and frames for the clinician; not designed in this project. |
| Hospital Information System (HIS) | System actor. The external clinical information system with which MMSS optionally exchanges patient data and diagnostic findings over HL7/FHIR-class interoperability (IF_10) for second opinion and handover. The downstream clinical system MMSS interoperates with on clinician request; not designed in this project. |
| Host CPU Platform | System actor. The existing compact embedded CPU platform with real-time OS capabilities on which MMSS executes, accessed over the host platform/OS interface (IF_01). Provides the runtime, timing services, and resources MMSS depends on to acquire, process, and present data within its performance budgets; not designed in this project. |

### Use Cases (UC_*)

_To be added_

| ID | Title | Actor | Goal | Satisfies | Classification | Precondition | Main Success Scenario | Alternative Scenarios | Exception Scenarios | Post Condition | Traces |
|----|-------|-------|------|-----------|----------------|--------------|-----------------------|-----------------------|---------------------|----------------|--------|
| UC_01 | Activate and reach clinical readiness | Pre-hospital Clinician | Bring MMSS from power-off to a usable monitoring state at the point of care without waiting through start-up. | UR_02 | High; Availability | MMSS installed and commissioned on the host platform; host platform powered. | 1. Clinician switches on the host platform. 2. MMSS starts on the Host CPU Platform. 3. MMSS reaches clinical readiness within 10 s. 4. MMSS shows an explicit "ready" indication and a per-channel acquisition state (live / acquiring / no-data). 5. Clinician confirms readiness and begins use. | None — readiness is reported as soon as the system is operable. | E1. Readiness not reached within 10 s → MMSS keeps showing an explicit "still starting" state and never presents an unacquired channel as a plausible normal value; clinician waits or escalates rather than trusting blank channels. | MMSS is ready; each channel's acquisition state is explicitly indicated. | UT_01, UR_02 |
| UC_02 | Commission and configure device channels | Biomedical / Clinical Engineer | Connect MMSS to each measurement device and the HIS through their published interfaces and verify correct mapping before clinical release. | UR_16 | High; Integration | MMSS installed on the host platform; measurement devices and HIS available; published interface contracts known. | 1. Engineer connects MMSS to each of the six measurement-device types and to the HIS strictly through their published interface contracts (IF_02–IF_07, IF_10). 2. MMSS gives clear per-channel interface and fault feedback. 3. Engineer completes a guided verification step confirming each acquired parameter (Acquired Parameters / Signals table) maps to the correct device and display field. 4. Engineer confirms acquisition, alarming, and data exchange behave correctly. 5. Engineer releases the device for clinical use. | A1. A device type is not present at commissioning → engineer configures the available channels and the unconfigured channel is shown as not-configured, not as a normal value. | E1. A channel maps to the wrong device/parameter in the verification step → MMSS surfaces the mismatch via per-channel feedback; engineer corrects the configuration and re-verifies before release; device is not released until verification passes. | Channels verified and correctly mapped; device released for clinical use. | UT_26, UT_27, UR_16 |
| UC_03 | Acquire and display vital signs at a glance | Pre-hospital Clinician | Read the patient's true current condition correctly at a glance, one-handed, in adverse conditions. | UR_01, UR_11 | High; Safety-critical (Class B) | MMSS ready; sensors being attached or attached. | 1. Clinician attaches sensors in clinical priority order — SpO₂ and ECG first for oxygenation and rhythm, then NIBP, capnometer, thermal probe, EEG as the situation allows; MMSS marks a channel live only once valid acquisition is confirmed. 2. MMSS presents, within 1 s of acquisition, every acquired vital-sign parameter (Acquired Parameters / Signals table) with its unit. 3. Display refreshes at least once per second and stays glanceable and legible in movement and poor light. 4. Abnormal values are flagged unmistakably out-of-range. 5. Clinician reads each value one-handed and cross-checks against the patient's clinical appearance before relying on it. | A1. A sensor not yet connected or still acquiring → MMSS flags that channel as not-connected / acquiring rather than showing a plausible normal value. A2. Clinician must begin stabilising on a partial sensor set (full set not yet attachable while working alone) → MMSS lets the clinician read and act on the confirmed live channels while clearly showing which clinically-relevant channels are still absent, so a missing parameter is recognised as not-yet-measured rather than overlooked. | E1. A channel becomes unreliable → handled by UC_06 (sensor-fault detection). E2. A first-priority channel (SpO₂ or ECG) cannot be acquired at all → that channel stays in an explicit no-data state and the clinician proceeds on the remaining channels and clinical assessment, never on an assumed value. | Clinician has a correct, current at-a-glance picture of the acquired vital signs, with any absent channel explicitly indicated. | UT_02, UT_03, UR_01, UR_11 |
| UC_04 | Maintain continuous bedside monitoring | Critical-Care Nurse | Keep monitoring reliably live across an extended shift while attending to other patients. | UR_03 | High; Availability | MMSS ready and acquiring at the bedside. | 1. MMSS remains reliably available throughout the shift. 2. MMSS continuously presents the patient's acquired vital signs (Acquired Parameters / Signals table). 3. MMSS shows a visible system-health / heartbeat indication so the nurse can trust monitoring is live while away. 4. Nurse periodically glances and relies on continuous surveillance. | None for normal operation. | E1. Display freeze, restart, or availability gap → MMSS raises an explicit, perceptible alert on the interruption and never presents a frozen screen as if live; device-side independent alarms act as a safeguard. | Monitoring is continuously live and its health is visibly indicated. | UT_06, UR_03 |
| UC_05 | Raise abnormal-condition alarm | Critical-Care Nurse | Be alerted immediately and unmistakably when a vital sign becomes abnormal so the patient can be treated before deteriorating. | UR_08, UR_09 | High; Safety-critical (Class B) | MMSS acquiring; alarm limits configured; alarms enabled. | 1. A vital-sign parameter crosses an abnormal threshold. 2. Within 1 s MMSS raises an immediate, unmistakable, distinguishable alarm identifying which parameter is abnormal and its urgency. 3. The alarm is perceptible in noisy/mobile conditions and latches until the condition resolves or is acknowledged. 4. Nurse recognises it as a genuine clinical alarm (not a sensor fault) from tone/colour/icon/text. 5. Nurse returns to the bedside, reads the flagged parameter and current candidates, confirms against the patient that the alarm reflects a true clinical change rather than motion artefact, intervenes, and acknowledges. | A1. Alarms deliberately suspended during active treatment/resuscitation to cut distraction → suspension is time-limited and auto-restores, an escalating reminder fires as the window expires, and a persistent conspicuous "alarms suspended" reminder prevents the patient being left silently unmonitored after the team disperses. A2. Nurse is away from the bedside attending another patient when the alarm fires → the latching, multi-modal alarm remains perceptible at distance and active until reached and acknowledged. | E1. Alarm confused with a sensor-fault warning → distinct multi-modal encoding per alarm-safety practice keeps clinical alarm and technical fault distinguishable. E2. Nurse is inclined to dismiss the alarm as motion artefact (cry-wolf habituation) → the alarm presents the live value/waveform and a signal-quality/plausibility cue alongside it so a genuine change is quickly separable from artefact before any dismissal. | Abnormal condition signalled, correctly judged real, treated, and the alarm acknowledged or resolved; any suspension is restored. | UT_07, UT_08, UT_09, UR_08, UR_09 |
| UC_06 | Detect and signal sensor disconnection, misplacement, or fault | Critical-Care Nurse | Be kept from acting on false or stale data when a sensor disconnects, is misplaced, or becomes unreliable. | UR_10, UR_09 | High; Safety-critical (Class B) | MMSS acquiring from one or more measurement devices. | 1. A measurement device (Acquired Parameters / Signals table) becomes disconnected, misplaced, or unreliable. 2. Within 1 s MMSS detects the condition from device-side fault signalling and input inactivity. 3. MMSS raises a sensor-fault warning distinguishable from a clinical alarm. 4. MMSS visibly marks the affected parameter untrustworthy and replaces the value with an explicit no-data/untrustworthy state. 5. Clinician identifies the affected channel, re-seats/repositions the sensor; MMSS returns the channel to a live, trusted state once valid acquisition resumes. | A1. Multiple channels affected (e.g. several leads jostled at once during a bumpy transfer) → each affected parameter is independently flagged untrustworthy. A2. Sensor faults intermittently — readings flicker valid/invalid → MMSS marks the channel untrustworthy on each loss rather than alternating between a trusted value and a fault, so a flickering channel is not intermittently believed. | E1. Sensor cannot be restored → channel remains in the explicit no-data state; clinician proceeds aware the parameter is unavailable rather than trusting a stale value. E2. A sensor-fault warning coincides with a genuine clinical alarm on another channel → both are surfaced and remain distinguishable so neither masks the other. | Affected channel is marked untrustworthy and, if re-seated, restored to trusted live state. | UT_10, UT_11, UT_12, UR_10, UR_09 |
| UC_07 | Obtain and present AI diagnostic candidates | Emergency Physician | Reach a working diagnosis faster using ranked decision support presented alongside the raw vital signs. | UR_04, UR_05 | High; Differentiator | MMSS acquiring stable vital signs; External Diagnostic AI Capability reachable over IF_09. | 1. MMSS forwards conditioned patient data to the External Diagnostic AI Capability. 2. The capability returns ranked diagnostic candidates with confidence and supporting reasoning. 3. Within 1 s of receipt MMSS presents the ranked candidates alongside the raw vital signs. 4. Each candidate shows its confidence and the driving vital-sign parameters, absorbable at a glance with expandable detail on demand. 5. The list converges as evidence accumulates, with still-converging lists visibly distinguished from settled results. | A1. List materially revises as it converges → changed ranking is made salient so a revision is noticed rather than missed (anchoring mitigation). | E1. No candidates can be produced within the expected time → handled by UC_09 (diagnosis timeout). E2. Diagnostic AI unreachable over IF_09 → MMSS signals the diagnostic path as unavailable rather than leaving the area silently blank. | Ranked candidates with confidence and reasoning are presented for clinician appraisal. | UT_04, UT_13, UR_04, UR_05 |
| UC_08 | Appraise candidates and retain clinical authority | Emergency Physician | Judge whether candidates fit the patient and form a working diagnosis while keeping final authority. | UR_06, UR_05 | High; Safety-critical / Liability | Ranked diagnostic candidates presented (UC_07). | 1. MMSS frames and labels the output unambiguously as decision support that informs rather than replaces the clinician. 2. Physician appraises each candidate against the patient, recognising when one rests on a parameter they distrust, and keeps the differential open. 3. Physician forms a working diagnosis. 4. Physician acts ahead of or against a suggestion as judgement dictates; MMSS never gates treatment on a candidate. | A1. Clinician's assessment diverges from, or directly contradicts, the top candidate → clinician acts on their own judgement ahead of or against the suggestion; MMSS imposes no workflow dependency, confirmation, or override step that could delay care. A2. Clinician chooses not to use the candidates at all → care proceeds entirely on the clinician's own assessment with no degradation of vital-signs monitoring or alarming. | E1. Confidence/ranking misread (over- or under-trust) → interpretive framing of confidence, visible driving parameters, and training-mode coaching mitigate automation bias. E2. Clinician anchors on an early candidate and the converging list later revises → the materially changed ranking is made salient so the revision is noticed and premature closure is resisted. | A clinician-owned working diagnosis is formed; final authority remains with the clinician. | UT_05, UT_14, UT_15, UR_06, UR_05 |
| UC_09 | Handle diagnosis timeout | Pre-hospital Clinician | Be told clearly when no diagnosis can be produced in time, so as to fall back on own assessment without waiting. | UR_07, UR_06 | High; Safety-critical (Class B) | Diagnostic request in progress; convergence not achieved within the expected time. | 1. No diagnostic result is produced within the expected convergence time. 2. MMSS presents a positive, perceptible timeout indication delivered independently of the failed diagnostic path — never a silently blank candidate area. 3. The external capability's own independent audible notification reinforces the timeout. 4. MMSS shows an explicit "no diagnosis available — proceed on your own assessment" message. 5. Clinician stops waiting and proceeds on their own clinical judgement while continuing to monitor vital signs. | A1. Candidates arrive late after the timeout was shown and the clinician has already begun acting on their own assessment → the late list is presented as a fresh, clearly provisional suggestion to be appraised per UC_07/UC_08, without overriding or interrupting the treatment already in progress. | E1. Independent timeout path itself fails → vital-signs monitoring and alarming continue unaffected; clinician proceeds on own assessment. | Clinician is positively informed of the timeout and proceeds on own assessment; monitoring continues. | UT_17, UT_18, UR_07, UR_06 |
| UC_10 | Share patient data and findings with the HIS | Emergency Physician | Share vital-sign data and diagnostic findings with the receiving hospital securely for second opinion and handover. | UR_14, UR_15 | High; Interoperability | MMSS holding patient data/findings; HIS reachable over IF_10; recipient determinable. | 1. Clinician confirms the receiving recipient before exchange. 2. MMSS exchanges the patient's vital-sign data and diagnostic findings with the HIS over the recognised interoperability standard, delivering candidates within 1 s of availability. 3. MMSS handles the personal health data in conformance with data-protection law throughout. 4. MMSS gives explicit confirmation of a successful, complete transfer to the correct patient record. | A1. Partial transfer → MMSS flags the partial/failed transfer and offers retry rather than reporting success. | E1. HIS unreachable or transfer fails → MMSS reports the failure explicitly so the clinician does not assume data is in hand; handover proceeds verbally. E2. Recipient not confirmed → exchange does not proceed, protecting confidentiality. | Data and findings transferred and confirmed to the correct record, or failure explicitly reported. | UT_16, UT_20, UT_21, UR_14, UR_15 |
| UC_11 | Surface working state and confirm continuity at handover | Critical-Care Nurse | Hand over the patient so the arriving clinician inherits the full working state and monitoring never lapses. | UR_03, UR_09, UR_10, UR_08 | High; Safety-critical (Class B) | Patient being transferred between clinicians/facilities; MMSS active. | 1. At handover MMSS makes the safety-relevant working state glanceable to the arriving clinician — which channels are flagged untrustworthy, whether alarms or limits are modified or suspended, and the current diagnostic candidate state. 2. The arriving clinician reviews the surfaced state. 3. Before disconnection the receiving clinician transfers the patient onto the receiving monitoring and confirms acquisition and alarming are live there. 4. MMSS keeps presenting vital signs and active alarm state until handover is complete. | A1. Receiving monitoring not yet ready → MMSS continues monitoring and alarming until the receiving system is confirmed live. | E1. Modified/suspended alarm state or a channel flagged untrustworthy not noticed by the arriving clinician → all such working state is persistently surfaced on screen so it cannot fall through the gap between clinicians. E2. Crew disconnects before the receiving monitoring is confirmed live → MMSS gives no positive confirmation of continuity, so the gap is visible and the patient is not left unmonitored on the assumption that handover completed. | Working state inherited and continuous monitoring confirmed without a gap. | UT_19, UT_29, UR_03, UR_09, UR_10, UR_08 |
| UC_12 | Operate training mode | Clinical Trainer / Super-User | Build clinician competence risk-free, including AI interpretation and bias avoidance, without any chance of confusing simulation with a live patient. | UR_12, UR_13 | High; Safety-critical (Class B) | MMSS available for training; no live patient connected for the session. | 1. Trainer enters simulated training mode with explicit confirmation. 2. MMSS displays a persistent, unmistakable, always-visible mode indicator and watermarks all simulated data. 3. Trainer runs realistic scenarios in which simulated vital signs, alarms, sensor faults, and AI candidates behave as in live use. 4. Trainer demonstrates AI candidate reasoning and confidence and correct interpretation, coaching against automation bias, anchoring, and premature closure. 5. Trainer exits training mode with explicit confirmation; MMSS enforces fail-safe separation and defaults to live operation on return/restart. | A1. Session paused/resumed → mode indicator and watermarking remain persistent throughout. | E1. Device left in training mode by a previous user → fail-safe default to live on restart and the persistent indicator prevent a clinician unknowingly treating a live patient in training mode. | Competence built; device returned to live operation with fail-safe separation enforced. | UT_22, UT_23, UT_24, UT_25, UR_12, UR_13 |
| UC_13 | Apply a controlled software update | Biomedical / Clinical Engineer | Keep the fleet current and serviceable by updating devices safely without disrupting clinical use. | UR_17 | High; Lifecycle / Maintainability | Device commissioned; update package available; standards-conformant lifecycle workflow in place. | 1. Engineer initiates a software update through the controlled, standards-conformant lifecycle workflow. 2. The workflow prevents updating a device in active clinical use. 3. The update is applied. 4. MMSS verifies correct operation before the device is returned to service. 5. Engineer returns the verified device to service. | A1. Device is in clinical use → update is blocked/deferred until the device is out of clinical use. | E1. Post-update verification fails → the device is not returned to service until correct operation is confirmed; engineer remediates or rolls back. | Device updated, verified, and returned to service in a known-good state. | UT_28, UR_17 |

### Design Decisions (DD_*)

Choices made during design, with the considered alternatives and the rationale for the final choice.

| ID | Decision | Alternatives | Rationale | Traces |
|----|----------|--------------|-----------|--------|
| DD_01 | Use the commercially validated off-the-shelf diagnostic AI capability (Open Evidence class) as an external component reached through its supplier-defined API, rather than developing a proprietary diagnostic model in v1.0. | (a) Develop a custom/proprietary in-house diagnostic model; (b) Train and validate a model on the manufacturer's own clinical data; (c) Defer diagnostic support to a later release. | An already-validated capability removes proprietary-model validation, clinical-evidence generation, and the associated liability from the v1.0 critical path and shortens time to market — the programme's principal de-risking lever. The constraint mandates an off-the-shelf validated model for the first release; MMSS consumes it as a black-box service over IF_09 within the validated scope of its own intended use. | UC_07, BR_03 |
| DD_02 | Govern the off-the-shelf diagnostic dependency through contractual supplier safeguards (validation-evidence flow-down, change/field-issue notification, version and model management, supply continuity, fixed lifetime licensing) rather than relying on the supplier relationship informally. | (a) Best-effort/informal supplier relationship; (b) Internal re-validation of each supplier change with no flow-down clauses; (c) Multi-supplier abstraction layer in v1.0. | Off-the-shelf reliance does not transfer product liability away from the legal manufacturer; the de-risking, cost, and market-continuity benefits hold only if the dependency is contractually secured. The diagnostic-AI ICD is supplier-defined, so MMSS must treat the supplier contract as part of the safety and continuity case. | UC_07, BR_09 |
| DD_03 | Adopt an independent-safeguard architecture so that no single MMSS failure in the two highest-criticality functions (alarming and diagnosis) can alone lead to death or serious injury, reducing the software safety classification from Class C to Class B. | (a) Develop the whole system to full Class C rigour with no external-safeguard reliance; (b) Internal software-only redundancy within MMSS for alarming and diagnosis; (c) Accept Class C and absorb the higher lifecycle/re-validation cost. | The worst-case contribution of alarming and diagnosis is mitigated by safeguards segregated from and demonstrably independent of MMSS — device-side fault/connection alarms and the external capability's audible time-out — combined with the clinician retaining authority over non-autonomous output. This bounds lifecycle and re-validation cost, but holds only while common-cause-free independence is verified and contractually underwritten. | UC_05, UC_06, UC_09, BR_02, BR_04 |
| DD_04 | Rely on the measurement devices' own independent device-side detection and audible connection/fault alarms for sensor disconnection, misplacement, and unreliable readings; MMSS detects the same conditions from device-side fault signalling plus input inactivity and re-presents them as a distinct visual sensor-fault warning, but is not the sole annunciator. | (a) MMSS as the sole detector/annunciator of sensor faults; (b) MMSS independently re-deriving sensor health from raw signal analysis; (c) Add MMSS audible re-annunciation of device faults. | The devices are fixed, out-of-scope elements that already raise their own independent alarms; making the device the independent safeguard is what keeps the sensor-fault path out of MMSS's single-failure worst case and supports the Class C→B reduction. MMSS's role is to mark the affected channel untrustworthy and warn the clinician distinctly, not to be the only line of defence. | UC_06, BR_02, BR_04 |
| DD_05 | Connect to each of the six mandated measurement-device types (ECG, pulse oximeter, BP monitor, thermal probe, capnometer, EEG) strictly through their published interface contracts (IF_02–IF_07), acquiring the enumerated parameter set without modifying any external device. | (a) Custom/proprietary per-device integration negotiated outside published contracts; (b) A single generic acquisition path assuming uniform device behaviour; (c) Require device firmware changes to ease integration. | The scope is software-only and devices are fixed; integrating strictly through published, defined ICDs protects the buyer's installed base, avoids rip-and-replace, and keeps the external elements unmodified. Supporting the full mandated set through their contracts is a constraint and a commercial precondition for fleet-wide deployment. | UC_02, UC_03, BR_10 |
| DD_06 | Present vital signs, alarms, sensor-fault warnings, and ranked diagnostic candidates on the existing connected monitor display (via IF_08) using a glanceable, one-handed, timer-driven presentation that refreshes at least once per second and is legible under movement, poor light, and noise. | (a) Require a new/dedicated display surface; (b) Event-driven-only screen updates with no fixed refresh; (c) Dense, detail-first layout optimised for fixed-bedside reading. | The display is a fixed, out-of-scope element accessed through a published interface; MMSS renders to it rather than introducing new hardware. A glanceable, fixed-cadence presentation meets the boundary-observable sub-second timeliness and the adverse-condition usability the clinician relies on in mobile and pre-hospital use. | UC_03, UC_04, BR_18, BR_16 |
| DD_07 | Implement HIS interoperability against a recognised healthcare interoperability-standard class (HL7/FHIR class) over IF_10, committing to the standard class now and fixing the specific protocol and interface contract before the exchange function is completed, rather than building a bespoke per-site integration. | (a) Bespoke point-to-point integration per hospital/EMS site; (b) Commit to a single specific protocol immediately before ICDs are agreed; (c) Defer HIS exchange entirely. | Standards-based exchange enables second opinion and smooth handover, protects prior investment, and spares the buyer bespoke integration cost — a commercial precondition. The exact protocol and ICD are TBD per the constraints, so the decision commits to the standard class and to settling the contract before completion rather than prematurely fixing a protocol. | UC_10, BR_10 |
| DD_08 | Handle diagnosis time-out as a positive, perceptible MMSS indication delivered independently of the failed diagnostic path (never a silently blank candidate area), reinforced by the external capability's own independent audible notification on its 2-minute convergence budget; MMSS does not own or commit to the convergence time. | (a) MMSS owns and enforces a 2-minute convergence budget; (b) Leave the candidate area blank on time-out; (c) Rely solely on the external capability's audible notification with no MMSS-side indication. | The 2-minute convergence budget is the external diagnostic AI capability's budget, not the system's budget; absorbing it would mis-place the timeliness commitment. A positive, path-independent MMSS time-out indication plus the external audible notification provides the independent safeguard so the clinician falls back on their own assessment rather than waiting on a blank screen — supporting the Class B argument for the diagnosis function. | UC_09, BR_18, BR_05 |
| DD_09 | Frame and label diagnostic output unambiguously as non-autonomous, adjunctive decision support that informs but never replaces the clinician, surfacing each candidate's confidence and supporting reasoning and imposing no workflow gate, confirmation, or override that could delay treatment. | (a) Present candidates as authoritative diagnoses; (b) Require explicit accept/override of a candidate before proceeding; (c) Suppress reasoning/confidence to simplify the display. | Clinician-in-control is the central liability firewall keeping ultimate responsibility with a qualified professional and keeps the device defensible as decision support rather than an autonomous diagnostic agent; exposing reasoning and confidence mitigates automation bias, and imposing no gate ensures MMSS never delays care. | UC_08, BR_05 |
| DD_10 | Provide a simulated training mode within MMSS with fail-safe separation from live operation — explicit entry/exit confirmation, a persistent always-visible mode indicator, watermarked simulated data, and a default to live operation on restart/return. | (a) Separate external training simulator/build; (b) Training mode without a persistent live/training indicator; (c) No dedicated training mode (train on live devices only). | The training mode is the named risk control for the critical clinician-misinterpretation hazard and forms part of the safety case; building it into MMSS with fail-safe separation prevents simulated data ever being mistaken for a live patient and a clinician unknowingly treating a live patient in training mode — itself a Class B safety concern. | UC_12, BR_12 |
| DD_11 | Acquire, process, display, and exchange personal health data in conformance with applicable data-protection and privacy law (GDPR/HIPAA class) and secure interoperability practice throughout the data flow, including recipient confirmation and explicit transfer-outcome reporting at the HIS boundary. | (a) Treat data protection as a deployment/site responsibility only; (b) Apply security only at the HIS exchange, not across the internal data flow; (c) Transfer without recipient confirmation or outcome reporting. | Data-protection non-conformance carries standalone regulatory and financial liability independent of clinical safety; protecting confidentiality, integrity, and patient rights wherever personal health data is handled, and confirming the recipient and transfer outcome, is required at the system boundary and underpins lawful market access. | UC_10, BR_14 |
| DD_12 | Make MMSS report clinical readiness and per-channel acquisition state explicitly — reaching readiness within 10 seconds of switch-on and never presenting an unacquired or untrustworthy channel as a plausible normal value — as the boundary-observable availability and integrity behaviour of the system. | (a) Present a single global "ready" state without per-channel acquisition status; (b) Show default/placeholder values on channels not yet acquiring; (c) No explicit readiness indication. | Rapid, demonstrable readiness and high availability are baseline clinical value and a buyer precondition for point-of-care use; making every channel's acquisition state explicit prevents the clinician acting on assumed data, which is a safety property at the system boundary independent of internal item design. | UC_01, BR_16 |
| DD_13 | Apply software updates only through a controlled, standards-conformant lifecycle workflow that blocks or defers updating a device in active clinical use and verifies correct operation before returning the device to service, rather than ad-hoc field updates. | (a) Ad-hoc/manual field updates with no lifecycle gate; (b) Forced updates regardless of clinical-use state; (c) No in-field update capability (full re-commissioning per change). | A controlled lifecycle is a precondition of lawful market access and is what allows the device to be safely patched over its service life without re-incurring full re-validation each change; gating updates on clinical-use state and post-update verification keeps the deployed fleet safe, current, and serviceable. | UC_13, BR_01 |

---

# Development

## SOLUTION: Mobile Monitoring Software Solution (MMSS)

### External Interfaces

The points where the system connects to context elements, sub-systems, or other systems — connection type, data/signals exchanged, and protocols/standards.

At the development level MMSS is treated as a single black box bounded by ten external interfaces, the same set established in the Context (IF_01–IF_10). Every connection below is an outward boundary of the system as a whole; nothing is allocated to an internal element. MMSS executes on a fixed host platform, acquires the enumerated parameter set from six fixed measurement-device types over their published device contracts, renders to a fixed display, consumes a fixed external diagnostic-AI service, and optionally exchanges with an external hospital information system. All external elements are existing, out-of-scope, and reached only through published interface contracts — MMSS reads, conditions, presents, and exchanges across these boundaries but never modifies the elements behind them.

The data carried on each boundary is the parameter/signal set enumerated in the Context **Acquired Parameters / Signals** table; the rows below do not re-enumerate it but reference it, so that table remains the single source of truth for each parameter, unit/range, and originating interface.

| Interface | Direction (at MMSS boundary) | Connection type | Data / signals exchanged | Protocol / standard |
|-----------|------------------------------|-----------------|--------------------------|---------------------|
| IF_01 — Host platform / OS | Bidirectional (MMSS ↔ host) | Software runtime / OS service binding (digital, logical) | Process scheduling, timing/clock services, memory and compute resources, lifecycle and update control, system-health/readiness state | Host platform / RTOS ICD (vendor-defined, existing) |
| IF_02 — ECG acquisition | Inbound (device → MMSS) | Digital device link, polled | Heart Rate plus device-side connection/fault signalling (see Acquired Parameters / Signals) | Published ECG device ICD (existing) |
| IF_03 — Pulse oximeter acquisition | Inbound (device → MMSS) | Digital device link, polled | SpO2, Pulse Rate plus device-side connection/fault signalling | Published pulse-oximeter device ICD (existing) |
| IF_04 — BP monitor acquisition | Inbound (device → MMSS) | Digital device link, polled | Systolic BP, Diastolic BP, MAP plus device-side connection/fault signalling | Published BP-monitor device ICD (existing) |
| IF_05 — Thermal probe acquisition | Inbound (device → MMSS) | Digital device link, polled | Temperature plus device-side connection/fault signalling | Published thermal-probe device ICD (existing) |
| IF_06 — Capnometer acquisition | Inbound (device → MMSS) | Digital device link, polled | Respiratory Rate, EtCO2 plus device-side connection/fault signalling | Published capnometer device ICD (existing) |
| IF_07 — EEG acquisition | Inbound (device → MMSS) | Digital device link, polled | BIS plus device-side connection/fault signalling | Published EEG device ICD (existing) |
| IF_08 — Display | Outbound (MMSS → display) | Digital display / rendering link | Rendered vital-signs tiles, alarm and sensor-fault indications, ranked diagnostic candidates with confidence/reasoning, mode and system-health indicators | Published display ICD (existing) |
| IF_09 — Diagnostic AI | Bidirectional (MMSS ↔ AI service) | Software service API (digital, logical) | Outbound: conditioned patient parameter set for analysis. Inbound: ranked diagnostic candidates with confidence and supporting reasoning; independent convergence-time-out notification | Supplier-defined diagnostic-AI library API ICD (Open Evidence class) |
| IF_10 — Hospital information system (HIS) | Bidirectional (MMSS ↔ HIS) | Network messaging / interoperability link, secured | Outbound: patient data and diagnostic findings for second opinion / handover; recipient and transfer-outcome confirmation. Inbound: acknowledgement | HL7/FHIR-class interoperability ICD — protocol TBD, secured per data-protection law |

_To be added_

### Requirements

The full set of requirements the system must satisfy, derived from the user requirements and constrained by the context, regulatory requirements, and design decisions. Requirements are SMART and form the basis for verification.

#### Interface Requirements (RQ_IF_*)

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_IF_01 | The system shall execute on the host CPU platform and interact with it solely through the host platform/OS interface as defined in the host platform/RTOS ICD, requiring no modification to the host platform or its operating system. | The host platform is a fixed, out-of-scope element; the software-only scope requires MMSS to bind only to the published runtime, timing, and resource services exposed at IF_01. | Integration | IF_01 |
| RQ_IF_02 | The system shall acquire Heart Rate from the ECG monitor over the ECG acquisition interface strictly in accordance with the published ECG device ICD, without modifying the device. | The ECG monitor is a fixed device accessed only through its published contract; correct acquisition of the enumerated parameter on its defined interface is the precondition for displaying and analysing it. | Integration; Safety-related (Class B) | IF_02 |
| RQ_IF_03 | The system shall acquire SpO2 and Pulse Rate from the pulse oximeter over the pulse oximeter acquisition interface strictly in accordance with the published pulse-oximeter device ICD, without modifying the device. | The pulse oximeter is a fixed device accessed only through its published contract; the enumerated parameters must be acquired exactly as the interface defines them. | Integration; Safety-related (Class B) | IF_03 |
| RQ_IF_04 | The system shall acquire Systolic BP, Diastolic BP, and MAP from the blood pressure monitor over the BP monitor acquisition interface strictly in accordance with the published BP-monitor device ICD, without modifying the device. | The BP monitor is a fixed device accessed only through its published contract; all three enumerated pressure parameters must be acquired as defined. | Integration; Safety-related (Class B) | IF_04 |
| RQ_IF_05 | The system shall acquire Temperature from the thermal probe over the thermal probe acquisition interface strictly in accordance with the published thermal-probe device ICD, without modifying the device. | The thermal probe is a fixed device accessed only through its published contract; the enumerated parameter must be acquired as defined. | Integration | IF_05 |
| RQ_IF_06 | The system shall acquire Respiratory Rate and EtCO2 from the capnometer over the capnometer acquisition interface strictly in accordance with the published capnometer device ICD, without modifying the device. | The capnometer is a fixed device accessed only through its published contract; both enumerated respiratory parameters must be acquired as defined. | Integration; Safety-related (Class B) | IF_06 |
| RQ_IF_07 | The system shall acquire BIS from the EEG monitor over the EEG acquisition interface strictly in accordance with the published EEG device ICD, without modifying the device. | The EEG monitor is a fixed device accessed only through its published contract; the enumerated parameter must be acquired as defined. | Integration | IF_07 |
| RQ_IF_08 | The system shall, on each device acquisition interface (IF_02–IF_07), receive and make available the device's own connection and fault signalling as defined in that device's published ICD, without suppressing or overriding the device's independent alarms. | The Class C→B safety mitigation relies on the measurement devices remaining the independent safeguard for sensor disconnection, misplacement, and unreliable readings; MMSS must consume their fault signalling at the boundary without weakening that independent annunciation. | Safety-critical (Class B) | IF_02, IF_03, IF_04, IF_05, IF_06, IF_07 |
| RQ_IF_09 | The system shall render all clinical output — vital-signs tiles, alarm and sensor-fault indications, ranked diagnostic candidates with confidence and reasoning, and mode and system-health indicators — to the monitor display over the display interface in accordance with the published display ICD, without requiring any display surface other than the existing connected monitor. | The display is a fixed, out-of-scope element reached only through its published contract; presenting all boundary-observable output on the existing display is a software-only scope and installed-base-compatibility requirement. | Integration; Safety-related (Class B) | IF_08 |
| RQ_IF_10 | The system shall submit the conditioned patient parameter set to the external diagnostic AI capability and receive ranked diagnostic candidates with their confidence and supporting reasoning over the diagnostic AI interface, conforming to the supplier-defined diagnostic-AI library API ICD and consuming the service as a black box within its validated intended-use scope. | The diagnostic AI is a commercially validated off-the-shelf component reached only through its supplier-defined API; MMSS must exchange exactly the data the ICD defines and not exceed the supplier's validated scope. | Integration; Safety-related (Class B) | IF_09 |
| RQ_IF_11 | The system shall receive the external diagnostic AI capability's independent convergence-time-out notification over the diagnostic AI interface and shall not depend on the candidate-result path to detect or signal a diagnosis time-out. | The two-path timeout safeguard requires MMSS to obtain the supplier's independent time-out signal at the boundary so its own time-out indication does not share a common failure with the candidate-result path. | Safety-critical (Class B) | IF_09 |
| RQ_IF_12 | The system shall exchange patient data and diagnostic findings with the hospital information system over the HIS interface using a recognised HL7/FHIR-class healthcare interoperability standard, fixed in the defined HIS interoperability ICD before development of the exchange function is completed, and shall obtain, from the protocol-defined acknowledgement returned by the receiving system, both recipient identity and transfer-outcome (success/failure) confirmation at this boundary. | Standards-based, contracted interoperability enables second opinion and handover without bespoke per-site integration; the protocol is TBD so the requirement commits to the standard class and to settling the ICD before development completes. Transfer-outcome confirmation is only obtainable from the standard's own acknowledgement message, so the requirement is bound to that acknowledgement to be implementable and testable. | Integration | IF_10 |
| RQ_IF_13 | The system shall protect the confidentiality and integrity of personal health data exchanged over the HIS interface in conformance with applicable data-protection and privacy law (GDPR/HIPAA class) and secure interoperability practice. | Personal health data crossing the HIS boundary is subject to data-protection law carrying standalone regulatory and financial liability; the exchange interface must be secured at the system boundary. | Security; Regulatory | IF_10 |
| RQ_IF_14 | The system shall apply software updates and report system readiness only through the host platform/OS interface in accordance with the host platform/RTOS ICD, such that no update is applied to a device in active clinical use and readiness state is exposed to the host as defined. | A controlled, lifecycle-conformant update and readiness mechanism at the host boundary keeps the deployed fleet safely patchable without disrupting clinical use, consistent with the host as the runtime and lifecycle-control element. | Lifecycle; Safety-related (Class B) | IF_01 |

#### Functional Requirements (RQ_FN_*)

What the system must do — its functions, features, and behaviors. Each traces back to a use case or user requirement.

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_FN_01 | The system shall transition from switch-on to a clinically ready monitoring state within 10 seconds and present an explicit "ready" indication when that state is reached. | Rapid, demonstrable readiness is the baseline availability the clinician relies on to start caring for the patient at the point of care without waiting through start-up. | High; Availability | UC_01, UR_02 |
| RQ_FN_02 | The system shall, for every channel in the Acquired Parameters / Signals table, present a per-channel acquisition state of live, acquiring, or no-data, and shall never render an unacquired channel as a measured value. | An unacquired channel shown as a plausible number is read as "normal" rather than "not yet measured", so explicit per-channel state prevents the clinician acting on assumed data. | High; Safety-critical (Class B) | UC_01, UC_03, UR_01 |
| RQ_FN_03 | The system shall acquire every vital-sign parameter enumerated in the Acquired Parameters / Signals table from its source measurement device and present each value with its unit on the monitor display, marking a channel as live only once valid acquisition is confirmed. | At-a-glance presentation of the patient's true vital signs is the core clinical value of the device; a value must carry its unit and appear only when genuinely acquired so the clinician reads the patient's real condition without conversion or doubt. | High; Safety-critical (Class B) | UC_03, UR_01 |
| RQ_FN_04 | The system shall refresh the displayed vital-sign values at least once per second for every live channel. | A fixed sub-second refresh cadence keeps the at-a-glance picture current so the clinician never relies on a stale reading. | High; Safety-critical (Class B) | UC_03, UC_04, UR_01 |
| RQ_FN_05 | The system shall present each acquired vital-sign value with an unmistakable, distinguishable out-of-range indication whenever the value crosses its configured abnormal threshold. | Abnormal values must be visually unmistakable at a glance so deterioration is recognised before it is missed in adverse, attention-split conditions. | High; Safety-critical (Class B) | UC_03, UC_05, UR_01 |
| RQ_FN_06 | The system shall continuously present the acquired vital signs throughout sustained operation and display a perceptible system-health indication that monitoring is live. | A visible health indication lets the clinician trust continuous surveillance while attending to other patients and prevents a silent gap being mistaken for live monitoring. | High; Availability | UC_04, UR_03 |
| RQ_FN_07 | The system shall continuously emit, against an independent timing reference, a liveness indication that advances only while monitoring is actually running, such that any interruption, freeze, or restart of monitoring becomes perceptible at the boundary — the liveness indication stalling or the system restarting — and shall raise an explicit, perceptible alert on that condition; a frozen or stalled display shall never be presentable as if it were live. | A process that has itself frozen cannot self-detect the freeze, so detection must rest on an independent, advancing liveness reference whose stall is observable at the boundary; a silent availability gap on an unattended critical patient otherwise gives a false sense of safety. | High; Availability | UC_04, UR_03 |
| RQ_FN_08 | The system shall raise, within 1 second of detecting an abnormal vital-sign condition, an immediate alarm that identifies which parameter (per the Acquired Parameters / Signals table) is abnormal and its urgency level. | Timely, parameter-specific alarming is the safety function that lets the clinician intervene before the patient deteriorates. | High; Safety-critical (Class B) | UC_05, UR_08 |
| RQ_FN_09 | The system shall present abnormal-condition alarms multi-modally (audible and visual) such that they are perceptible in noisy and mobile conditions and shall keep each alarm latched until the condition resolves or the clinician acknowledges it. | A latching, conspicuous alarm cannot self-clear unnoticed and stays perceptible at distance, so a clinically significant condition is never missed while the clinician is away. | High; Safety-critical (Class B) | UC_05, UR_08 |
| RQ_FN_10 | The system shall make abnormal-condition clinical alarms distinguishable from sensor-fault warnings by distinct audible tone, colour, icon, and text, conforming to recognised alarm-safety practice. | A clinical alarm mistaken for a technical fault (or vice versa) leads directly to wrong or omitted action; distinct multi-modal encoding keeps the two unambiguous over sustained use. | High; Safety-critical / Regulatory | UC_05, UC_06, UR_09 |
| RQ_FN_11 | The system shall permit alarms to be suspended only for a bounded interval after which they automatically restore, shall display a persistent conspicuous indication for the whole period alarms are suspended, and shall raise an escalating reminder as the suspension window expires. | Deliberate alarm suspension during resuscitation is legitimate, but a forgotten or indefinite silence is a critical alarm-safety hazard; time-limited suspension with a persistent reminder prevents the patient being left silently unmonitored. | High; Safety-critical (Class B) | UC_05, UR_09 |
| RQ_FN_12 | The system shall detect, within 1 second, a measurement-device disconnection, misplacement, or unreliable-reading condition for any device in the Acquired Parameters / Signals table whenever (a) the device asserts the corresponding fault or quality flag defined in its published ICD, or (b) valid input from that channel is absent for the configured short inactivity window; the system relies on the device's own fault and signal-quality signalling for clinical-reliability judgements and shall not infer reliability beyond what the device interface reports together with input inactivity. | Sensor-fault propagation is a critical hazard; prompt detection from device-side fault/quality signalling and input inactivity is the precondition for warning the clinician before false data is trusted. The MMSS is software-only and cannot independently judge clinical signal reliability, so detection of "unreliable readings" must be bounded to what the device interface reports plus inactivity, keeping the requirement implementable and keeping the device the independent safeguard. | High; Safety-critical (Class B) | UC_06, UR_10 |
| RQ_FN_13 | The system shall, on detecting a sensor disconnection, misplacement, or fault, raise a sensor-fault warning distinguishable from a clinical alarm, visibly mark the affected parameter as untrustworthy, and replace its displayed value with an explicit no-data/untrustworthy state instead of a stale or implausible value. | A stale value shown as live positively misleads; marking the channel untrustworthy and removing the value keeps the clinician from acting on false or out-of-date data. | High; Safety-critical (Class B) | UC_06, UR_10 |
| RQ_FN_14 | The system shall return an affected channel to a live, trusted state once valid acquisition resumes, and shall mark the channel untrustworthy on each loss of valid acquisition for an intermittently faulting channel rather than alternating between trusted and fault states. | Restoring trust on re-acquisition supports re-seating the sensor, while marking a flickering channel untrustworthy on every loss prevents it being intermittently believed. | High; Safety-critical (Class B) | UC_06, UR_10 |
| RQ_FN_15 | The system shall submit the conditioned patient parameter set to the external diagnostic AI capability and, given a complete ranked-candidate response received at the diagnostic-AI interface, present those candidates alongside the raw vital signs within 1 second of the response being fully received at that boundary. | Prompt presentation of ranked candidates beside the vital signs is the decision-support differentiator that helps the clinician reach a working diagnosis faster, including when no colleague is available; tying the budget to the complete response arriving at the boundary makes it measurable and excludes the external capability's own compute time, which the system cannot control. | High; Differentiator | UC_07, UR_04 |
| RQ_FN_16 | The system shall present each diagnostic candidate with its confidence and its supporting reasoning — including the driving vital-sign parameters — absorbable at a glance, with fuller detail available on demand. | Confidence, reasoning, and driving parameters let the clinician judge whether a candidate fits the patient and recognise when it rests on a parameter they distrust, keeping clinical judgement in control. | High; Safety-critical / Liability | UC_07, UR_05 |
| RQ_FN_17 | The system shall visibly distinguish a still-converging (provisional) candidate list from a settled one and make a materially changed ranking salient so a revision is noticed rather than missed. | Distinguishing provisional from settled results and signalling revisions mitigates anchoring and premature closure on an early candidate. | High; Safety-critical / Liability | UC_07, UC_08, UR_04 |
| RQ_FN_18 | The system shall frame and label the diagnostic output unambiguously as decision support that informs rather than replaces the clinician, and shall impose no workflow gate, confirmation, or override on a candidate that could prevent or delay the clinician acting on their own judgement. | Clinician-in-control is the central liability firewall; non-gating, clearly-framed decision support keeps final authority with the clinician and never delays care. | High; Safety-critical / Liability | UC_08, UR_06 |
| RQ_FN_19 | The system shall, when no diagnostic result is produced within the expected convergence time, present a positive perceptible time-out indication delivered independently of the diagnostic candidate-result path and an explicit "no diagnosis available — proceed on your own assessment" message, and shall not leave the candidate area silently blank. | A blank area is read as "still computing"; a positive, path-independent time-out indication tells the clinician to fall back on their own assessment rather than wait indefinitely. | High; Safety-critical (Class B) | UC_09, UR_07 |
| RQ_FN_20 | The system shall exchange the patient's vital-sign data and diagnostic findings with the hospital information system over the recognised interoperability standard on clinician request, delivering diagnostic candidates within 1 second of their availability, and shall require the receiving recipient to be confirmed before the exchange proceeds. | Standards-based, recipient-confirmed exchange enables a second opinion and smooth, secure handover while protecting confidentiality. | High; Interoperability | UC_10, UR_14 |
| RQ_FN_21 | The system shall give explicit confirmation of a successful, complete transfer to the correct patient record and shall explicitly flag any partial or failed transfer with the option to retry, rather than reporting success. | Handover is a high-risk transition; explicit transfer-outcome reporting prevents both ends falsely believing information is in hand. | High; Interoperability | UC_10, UR_14 |
| RQ_FN_22 | The system shall persistently surface the safety-relevant working state to any clinician at the device — which channels are flagged untrustworthy, whether alarms or limits are modified or suspended, and the current diagnostic candidate state — and shall continue presenting vital signs and active alarm state until handover to receiving monitoring is confirmed complete. | Critical working state held silently falls through the gap between clinicians; surfacing it and sustaining monitoring until continuity is confirmed prevents a lapse at handover. | High; Safety-critical (Class B) | UC_11, UR_03, UR_09, UR_10 |
| RQ_FN_23 | The system shall provide a simulated training mode in which simulated vital signs, alarms, sensor faults, and diagnostic candidates behave as in live operation, allowing risk-free practice including AI candidate interpretation and bias avoidance. | A realistic risk-free training mode is the named risk control for the critical clinician-misinterpretation hazard and lets clinicians build competence before live use. | High; Safety-critical (named risk control) | UC_12, UR_12 |
| RQ_FN_24 | The system shall enforce fail-safe separation between training and live operation: requiring explicit confirmation to enter and exit training mode, displaying a persistent, always-visible mode indicator and watermarking all simulated data, and defaulting to live operation on restart or return to the device. | Simulated data mistaken for a real patient, or a live patient unknowingly monitored in training mode, is itself a critical hazard; fail-safe separation and a persistent indicator prevent it. | High; Safety-critical (Class B) | UC_12, UR_13 |
| RQ_FN_25 | The system shall connect to each of the six measurement-device types and to the hospital information system strictly through their published interface contracts and shall provide clear per-channel interface and fault feedback and a guided verification step confirming each acquired parameter maps to the correct device and display field before the device is released for clinical use. | Verified, contract-only commissioning lets the engineer integrate the fleet without modifying external elements and prevents a mis-mapped channel propagating to wrong clinical decisions. | High; Integration | UC_02, UR_16 |
| RQ_FN_26 | The system shall apply software updates only through the controlled lifecycle workflow, preventing or deferring any update to a device in active clinical use and verifying correct operation before the device is returned to service. | A controlled, use-aware update workflow keeps the deployed fleet safely patchable over its service life without disrupting monitoring or returning a device in an unverified state. | High; Lifecycle / Maintainability | UC_13, UR_17 |

#### Performance Requirements (RQ_PR_*)

Quantitative requirements on how well the system performs its functions: response times, throughput, accuracy, capacity, availability.

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_PR_01 | The system shall reach a clinically ready monitoring state, with the explicit "ready" indication shown, within 10 seconds of switch-on, measured from power-on to ready indication. | The clinician relies on the device being usable at the point of care within seconds; a bounded, measurable activation time is the baseline availability the start-up behaviour must guarantee. | High; Availability | RQ_FN_01 |
| RQ_PR_02 | The system shall present each acquired vital-sign value on the monitor display within 1 second of its acquisition from the source measurement device, measured at the system boundary from value receipt to display update, for every channel in the Acquired Parameters / Signals table. | Sub-second acquisition-to-display latency at the boundary is the at-a-glance clinical value the clinician sees; it is the end-to-end figure the user observes, independent of any internal processing budget. | High; Safety-critical (Class B) | RQ_FN_03 |
| RQ_PR_03 | The system shall update every live vital-sign channel on the display on a timer-based cadence of once per second (refresh interval ≤ 1 second). | A fixed 1-second refresh cadence keeps the displayed picture current so the clinician never relies on a stale reading; the cadence must be quantified and verifiable. | High; Safety-critical (Class B) | RQ_FN_04 |
| RQ_PR_04 | The system shall accept and process vital-sign input from each source measurement device at a sustained rate of at least 0.1 Hz (one update per 10 seconds or faster) per channel without loss of the most recent value. | The minimum input acquisition rate sets the floor at which the displayed and analysed data stays representative of the patient's current condition; below it the picture is no longer real-time. | High; Performance | RQ_FN_03, RQ_FN_04 |
| RQ_PR_05 | The system shall raise an abnormal-condition alarm within 1 second of detecting that a vital-sign value has crossed its configured abnormal threshold, measured from detection to alarm presentation. | Timely alarming is the safety function that lets the clinician intervene before deterioration; the 1-second detection-to-alarm budget is the boundary-observable figure that bounds the delay the patient is exposed to. | High; Safety-critical (Class B) | RQ_FN_08 |
| RQ_PR_06 | The system shall trigger a connection (sensor-inactivity) alarm when input from a measurement-device channel has been absent for a continuous 5 seconds of inactivity. | A defined 5-second inactivity window is the quantified threshold at which a lost connection is treated as a fault, balancing prompt detection against transient-gap false alarms. | High; Safety-critical (Class B) | RQ_FN_12 |
| RQ_PR_07 | The system shall detect a sensor disconnection, misplacement, or unreliable-reading fault within 1 second of the device's fault signalling at the interface, and present the corresponding sensor-fault warning within 1 second of detection. | Sensor-fault propagation is a critical hazard; bounding both detection and presentation to within 1 second limits how long false or missing data can be trusted before the clinician is warned. | High; Safety-critical (Class B) | RQ_FN_12, RQ_FN_13 |
| RQ_PR_08 | The system shall present the ranked diagnostic candidates returned by the external diagnostic AI capability alongside the raw vital signs within 1 second of their receipt at the system boundary. | Prompt presentation of received candidates is the decision-support figure the clinician observes; the budget is measured from receipt at the boundary, since time-to-converge belongs to the external capability, not to the system. | High; Differentiator | RQ_FN_15 |
| RQ_PR_09 | The system shall deliver the patient's vital-sign data and diagnostic findings to the hospital information system within 1 second of the clinician's confirmed exchange request (and within 1 second of candidate availability for diagnostic candidates), measured at the outbound system boundary. | Sub-second outbound delivery keeps second-opinion and handover exchange responsive; the budget is the boundary-observable transfer latency the user experiences, excluding downstream HIS processing. | High; Interoperability | RQ_FN_20 |
| RQ_PR_10 | The system shall present the diagnostic time-out indication when no diagnostic result has been received within the external capability's expected convergence time-out of 2 minutes, treating the 2-minute window as an observed external deadline rather than a system computation budget. | The 2-minute convergence is the external diagnostic AI capability's budget; the system's quantified obligation is to observe that deadline and signal the time-out so the clinician falls back on their own assessment without waiting indefinitely. | High; Safety-critical (Class B) | RQ_FN_19 |
| RQ_PR_11 | The system shall concurrently acquire, process, refresh, and display all parameters enumerated in the Acquired Parameters / Signals table from all six measurement-device types simultaneously, meeting every per-channel latency and refresh budget under full concurrent load. | Critical patients are monitored on multiple devices at once; the system must sustain its timing budgets at full channel capacity, not only for a single channel, or the at-a-glance picture degrades under realistic load. | High; Capacity | RQ_FN_03, RQ_FN_04, RQ_FN_08 |
| RQ_PR_12 | The system shall sustain continuous, uninterrupted monitoring over a defined continuous soak period of at least 24 hours without degradation of its acquisition, display-refresh, or alarm latency budgets — every such budget shall continue to be met at the end of the period as at the start — and without cumulative resource exhaustion (e.g. memory growth, handle/thread leakage) that would breach those budgets. | An unavailable or degrading monitor at the point of care is an operational and clinical risk; a quantified ≥24-hour soak period gives a measurable, testable basis for "sustained" operation and surfaces the resource-leak failure modes that erode timing budgets over long runs. | High; Availability / Reliability | RQ_FN_06 |
| RQ_PR_13 | The system shall raise the perceptible interruption alert within 1 second of an interruption, freeze, or restart of monitoring becoming observable — that is, within 1 second of the independent liveness indication stalling for longer than its configured liveness interval, or of the system returning to service after a restart. | A silent availability gap gives a false sense of safety; bounding the alert to within 1 second of the liveness stall (the only boundary-observable evidence of a freeze, since a frozen process cannot time its own stall) ensures the clinician learns of a lapse promptly while keeping the budget measurable. | High; Availability | RQ_FN_07 |

#### Non-Functional Requirements (RQ_NF_*)

How the system should behave rather than what it does: reliability, maintainability, security, privacy, scalability. Compliance, labeling, and training requirements live here too.

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_NF_01 | The system shall achieve a demonstrated availability of at least 99.9% of operating time during continuous critical-care operation, where unavailability is any interval in which vital-signs presentation is lost, and shall make every such loss explicitly perceptible to the clinician rather than silent; planned restart-recovery within the RQ_NF_02 bound counts toward unavailability and shall be annunciated. | An unavailable monitor at the point of care is an operational and clinical risk; a single quantified availability target, measured over the defined representative operating period, is verifiable, whereas pairing it with an unqualified "no loss exceeding 1 second" clause conflicted with the bounded restart recovery in RQ_NF_02. The decisive safety property — that no loss is silent — is stated explicitly instead. | Reliability / Availability; Safety-related (Class B) | BR_16, RE_02 |
| RQ_NF_02 | The system shall be restorable to a clinically ready monitoring state within 10 seconds following an unexpected software restart, without loss of acquisition configuration, and shall make any restart explicitly perceptible to the clinician. | Rapid, transparent recovery prevents a silent monitoring gap on an unattended critical patient and bounds the clinical exposure of a fault to a known, short interval. | Reliability / Availability; Safety-critical (Class B) | BR_16, RE_02 |
| RQ_NF_03 | The system shall be maintainable such that a change confined to one software concern can be released through the controlled software lifecycle without requiring full re-verification of unchanged, segregated parts, with the verified scope of each change documented and traceable. | Change-scoped re-verification keeps update and re-validation cost bounded over the service life and is a precondition of safely updating a deployed safety-critical fleet without re-incurring full re-validation each change. | Maintainability; Lifecycle (IEC 62304) | BR_01, BR_15, RE_01 |
| RQ_NF_04 | The system shall enforce access control, authenticated operation, and end-to-end protection of the confidentiality and integrity of personal health data at rest and in transit, in conformance with applicable data-protection and privacy law (e.g. GDPR / HIPAA class) and secure-interoperability practice, and shall maintain a tamper-evident audit record of access to and exchange of personal health data. | Personal health data handled or exchanged by the device is subject to data-protection law carrying standalone regulatory and financial liability independent of clinical safety; confidentiality, integrity, and auditability must be assured throughout the data flow. | Security / Privacy; Regulatory | BR_14, RE_07 |
| RQ_NF_05 | The system shall be developed, maintained, and changed under a documented IEC 62304 software lifecycle, applying the activities and deliverables required for its assigned software safety classification with planning, configuration management, problem resolution, and change control applied from project start. | A documented, classification-appropriate IEC 62304 lifecycle is mandated by applicable medical-device software law and is the rigour authorities require before granting market access; it is verifiable against the standard's process deliverables. | Compliance; Lifecycle (IEC 62304) | BR_01, RE_01 |
| RQ_NF_06 | The system shall be supported by a complete ISO 14971 risk-management process across the lifecycle that explicitly addresses AI mis-diagnosis, false or missed alarms, sensor-fault propagation, and use error, reducing each hazard to an acceptable, documented residual level through verified risk controls, with a maintained risk-management file demonstrating a favourable benefit-risk balance. | A complete ISO 14971 process with documented residual risk and a favourable benefit-risk conclusion is required for approval and is the manufacturer's principal defence of a safety-critical diagnostic device; the risk-management file is the auditable evidence. | Compliance; Risk Management (ISO 14971); Safety-critical | BR_04, RE_02 |
| RQ_NF_07 | The system shall be developed under a documented IEC 62366 usability-engineering process that identifies use-related hazards and demonstrates, through formative and summative evaluation in the intended use environments, that foreseeable use errors associated with safety-critical interactions are mitigated to an acceptable level. | A usability-engineering process with summative validation evidence is required to confirm the device can be operated safely by its intended users and is a precondition of the safety case for use-related hazards such as clinician misinterpretation. | Compliance; Usability Engineering (IEC 62366); Safety-critical | BR_04, BR_12, RE_03 |
| RQ_NF_08 | The system's alarm system shall conform to the applicable requirements of IEC 60601-1-8 for the generation, prioritisation, annunciation, and distinguishability of clinical alarm conditions and technical (sensor-fault) conditions, including audible and visual alarm characteristics appropriate to assigned priority. | Conformance to the recognised alarm-safety standard is the presumption of conformity authorities expect for alarm behaviour and ensures clinically significant conditions and technical faults are signalled correctly, distinguishably, and without unsafe alarm fatigue or missed-alarm risk. | Compliance; Alarm Safety (IEC 60601-1-8); Safety-critical | BR_04, RE_06 |
| RQ_NF_09 | The system shall be accompanied by labelling and instructions for use, appropriate to its safety class, that state its intended use, indications, user profile, use environment, capabilities, limitations and contraindications — including the adjunctive, non-autonomous nature of the diagnostic output and the validated intended-use boundaries of the off-the-shelf AI capability — and the warnings and information for safety required for safe operation. | Compliant labelling and information-for-safety are mandatory obligations for the device's safety class and ensure intended users understand the device's capabilities, limitations, and safe operation, including that diagnostic output must not be the sole basis for a clinical decision. | Compliance; Labeling / Information-for-Safety; Regulatory | BR_12, RE_09, RE_05 |
| RQ_NF_10 | The system shall provide a realistic, risk-free simulated training mode, with fail-safe and persistently indicated separation from live clinical operation, and the manufacturer shall provide user-training provisions appropriate to the device's safety class such that intended users can build competence before live use. | The training mode is the named risk control for the critical clinician-misinterpretation hazard and forms part of the safety case; mandatory training-provision obligations for the safety class must be met to support safe fleet operation. | Compliance; Training; Safety-critical (Class B) | BR_12, RE_09 |
| RQ_NF_11 | The system shall support post-market surveillance, vigilance, and incident reporting by recording, with end-to-end traceability, the events, conditions, configuration, and software version associated with a field occurrence, such that a field event can be traced back to the responsible design element and reported within mandated timelines. | Post-market surveillance and mandated incident-reporting timelines are direct legal obligations of the legal manufacturer with enforcement and recall exposure; field-to-design traceability is what lets emerging safety signals be detected, reported, and corrected through field safety actions. | Compliance; Post-Market Surveillance / Traceability; Regulatory | BR_13, RE_10 |
| RQ_NF_12 | The system shall ensure that the risk-control safeguards relied upon to reduce its software safety classification — the device-side independent connection/fault alarms and the external diagnostic capability's independent convergence-time-out notification — are obtained and acted upon through paths segregated from, and free of common-cause failure with, the functions they protect, such that no single system failure can simultaneously defeat a safety-critical function and its safeguard. | The reduction of the classification from Class C to Class B is admissible only while the safeguards are demonstrably independent and common-cause-free; verifiable segregation at the system boundary is what sustains the mitigated classification and the benefit-risk argument supporting market access. | Compliance; Safety Architecture (Class C→B); Safety-critical | BR_02, RE_02 |
| RQ_NF_13 | The system shall submit to the off-the-shelf diagnostic AI capability only inputs (parameter set, patient population, and operating conditions) that fall within that capability's supplier-declared validated intended-use scope, and shall, whenever the data it is about to submit or the returned output's supplier-provided scope/applicability flags fall outside that declared scope, withhold or accompany the diagnostic output with an explicit out-of-scope indication rather than presenting, relying on, or exchanging it as in-scope. | Reliance on an off-the-shelf AI does not transfer liability from the manufacturer; using it outside its validated intended use invalidates the clinical-performance evidence. The MMSS consumes the AI as a black box, so it can only enforce scope on what it controls — the inputs it submits — and on any scope/applicability flags the supplier returns; binding the requirement to those boundary-observable signals makes it implementable. | Compliance; Clinical Validation (SOUP/OTS); Safety-critical | BR_17, BR_03, RE_04 |
| RQ_NF_14 | The system shall, for every diagnostic candidate it presents, accompany it with the supporting reasoning and confidence supplied by the diagnostic AI capability and an unambiguous, persistent indication that the output is adjunctive decision support that does not replace the clinician's judgement. | Presenting reasoning, confidence, and decision-support framing is the central liability control that keeps responsibility with the clinician, mitigates automation bias, and keeps the device defensible as decision support rather than an autonomous diagnostic agent. | Compliance; Information-for-Safety; Safety-critical (Liability) | BR_05, RE_05 |
| RQ_NF_15 | The manufacturer shall operate a certified quality management system (e.g. ISO 13485 class) and maintain a complete, current, audit-ready technical file or design dossier covering design control, quality, risk management, and clinical validation evidence for the system throughout its lifecycle. | A certified QMS and a current, audit-ready technical file are the basis on which a notified body and competent authority assess conformity and the manufacturer defends its declaration of conformity and lawful market placement. | Compliance; Quality Management (ISO 13485); Regulatory | BR_06, BR_07, RE_08 |

#### Constraint Requirements (RQ_CS_*)

External constraints the system must respect: regulatory rules, applicable standards, imposed technology choices, environmental conditions.

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_CS_01 | The system shall be classified and developed in accordance with ANSI/AAMI/IEC 62304, with an initial software safety classification of Class C reduced to a mitigated Class B by independent external risk-control safeguards, and shall meet the lifecycle obligations of the mitigated classification while the independence of those safeguards remains demonstrated. | The imposed software-lifecycle standard and the mandated Class C-to-B mitigation define the development rigour and the conditions under which the lower class is admissible; this is a binding external constraint on how the system may lawfully be engineered and placed on the market. | Constraint; Lifecycle / Safety Classification (IEC 62304) | RE_01, RE_02, BR_02 |
| RQ_CS_02 | The system shall, for its first release, incorporate a commercially available, validated, off-the-shelf diagnostic AI capability (Open Evidence) as its diagnostic engine, and shall not incorporate a custom or proprietary in-house diagnostic model. | The first release is constrained by mandate to a validated off-the-shelf model to remove proprietary-model validation from the critical path and bound the manufacturer's validation and liability burden; this is an imposed technology constraint, not a design option. | Constraint; Imposed Technology (OTS/SOUP) | RE_04, BR_03 |
| RQ_CS_03 | The system shall acquire from, and operate with, all six mandated measurement-device types — ECG monitor, pulse oximeter, blood-pressure monitor, thermal probe, capnometer, and EEG monitor — through their published interface contracts, without modifying those devices. | Support for the full mandated device set across the existing installed base is an imposed scope constraint; the software-only scope requires the system to reach these fixed external elements only through their published contracts. | Constraint; Scope / Interoperability | RE_06, BR_10 |
| RQ_CS_04 | The system shall exchange patient data and diagnostic findings with hospital and EMS information systems over a recognised healthcare interoperability standard of the HL7/FHIR class, with the specific protocol to be confirmed and fixed in a defined interface control document before development of the exchange function completes. | Standards-based interoperability is required for second opinion and handover and to avoid bespoke integration cost; the exact protocol is not yet fixed, so the constraint binds the standard class and the requirement to settle the ICD before completion. | Constraint; Imposed Standard (HL7/FHIR class) | RE_07, BR_10 |
| RQ_CS_05 | The system shall conform to the applicable medical-device regulation of each target market (e.g. EU MDR / national device regulation) as a software medical device, and shall be placed on the market only under a valid declaration of conformity / clearance supported by the technical file. | Lawful market access is conditioned on conformity to the applicable medical-device regulation in each jurisdiction; this is a binding legal constraint that gates release independently of clinical merit. | Constraint; Regulatory (Medical Device Regulation) | RE_08, BR_06 |
| RQ_CS_06 | The system shall acquire, process, display, and exchange personal health data only in conformance with the applicable data-protection and privacy law (e.g. GDPR / HIPAA class) of each target market. | Data-protection law is an externally imposed legal constraint carrying standalone regulatory and financial liability; the system must respect it wherever personal health data is handled, independently of clinical-safety obligations. | Constraint; Regulatory (Data-Protection Law) | RE_07 |
| RQ_CS_07 | The system's alarm behaviour shall conform to IEC 60601-1-8 and its usability process to IEC 62366, as the recognised standards establishing the presumption of conformity for alarm safety and usability engineering in the target markets. | These harmonised standards are the externally imposed yardsticks against which authorities and notified bodies assess alarm-safety and usability conformity; conforming to them is the recognised route to demonstrate compliance. | Constraint; Applicable Standards (IEC 60601-1-8 / IEC 62366) | RE_06, RE_03 |
| RQ_CS_08 | The system shall operate within the constraints of its intended use environments — fixed critical-care settings and mobile/pre-hospital settings (ambulance, on-scene) subject to movement, noise, poor light, and vibration — and on the assumed compact embedded host platform with real-time-OS capabilities, accessed solely through that platform's published interface. | The dual fixed/mobile use environment and the fixed, out-of-scope embedded host are imposed operating-environment constraints the system must respect; it must remain safe and usable across these conditions and bind only to the published host interface. | Constraint; Operating Environment | RE_03, BR_16 |
| RQ_CS_09 | The system shall treat the diagnosis-convergence target (2 minutes) as a budget owned by the external diagnostic AI capability and shall not assume responsibility for that convergence time; the system's own timeliness constraint is bounded to the sub-second presentation budget at its external boundary. | The constraints explicitly assign the convergence time to the external capability and the sub-second presentation budget to the system; the system must not absorb an externally owned budget into its own conformance obligations. | Constraint; Imposed Performance Boundary | RE_04, BR_18 |
| RQ_CS_10 | The manufacturer shall maintain a certified quality management system (e.g. ISO 13485) under which the system is developed, produced, and supported, as the external quality-system precondition for conformity assessment and lawful market placement. | A certified QMS is an externally imposed precondition for notified-body and authority conformity assessment; the system must be produced within that controlled quality framework to be lawfully marketable. | Constraint; Regulatory (ISO 13485) | RE_08 |

### Verification (SV_*)

The **BDD feature files** that verify the functional requirements, defined jointly by the 3-Amigos (Product Owner, Development Lead, Verification Lead). Write **one feature file per functional requirement** as a `gherkin` fenced block, tagged `@ID:RQ_FN_xx` to trace it to the requirement it verifies. Each feature has a user story (`As a … I want … So that …`), a `Rule:` that captures the requirement's "shall" statement, and one or more concrete `Scenario`s with `Given / When / Then` steps and data tables for the expected values. Use measurable outcomes (e.g. "within 5 seconds"). Every RQ_FN_* must have a feature file and every RQ_* must be covered by at least one scenario. The converter records each feature file as one row (`SV_*`) in the workbook's Verification table.

```gherkin
@ID:RQ_FN_01
Feature: Become clinically ready within 10 seconds of switch-on
    As a Pre-hospital Clinician I want MMSS to become ready for clinical use within 10 seconds of switching on
    So that I can start caring for the patient at the scene without waiting through a slow start-up

Rule: The MMSS shall transition from switch-on to a clinically ready monitoring state within 10 seconds and present an explicit "ready" indication when that state is reached.

Scenario: MMSS reaches a clinically ready state within 10 seconds of switch-on
    Given the simulator is running
    And the MMSS is hosted on the host-platform stub exposing the host platform/OS interface per the host RTOS ICD
    And the MMSS is switched off
    When the MMSS is switched on
    Then the explicit "ready" indication is shown on the Display Interface within the following time (RQ_PR_01)
    | event              | maximum time |
    | switch-on to ready | 10 seconds   |
    And the MMSS exposes its readiness state to the host-platform stub over the host platform/OS interface, requiring no modification to the host (RQ_IF_01)

Scenario: No monitoring is presented as ready before the ready state is reached
    Given the simulator is running
    And the MMSS is switched off
    When the MMSS is switched on
    Then the MMSS does not present a clinically ready monitoring state until the "ready" indication is shown

Scenario: MMSS is restorable to a ready state within 10 seconds after an unexpected restart
    Given the simulator is running
    And the MMSS is running in a clinically ready state with the acquisition configuration set
    When the test harness forces an unexpected software restart of the MMSS process
    Then the MMSS makes the restart explicitly perceptible to the clinician
    And the explicit "ready" indication is shown again within the following time (RQ_NF_02)
    | event                | maximum time |
    | restart to ready     | 10 seconds   |
    And the acquisition configuration is preserved across the restart
```

```gherkin
@ID:RQ_FN_02
Feature: Present a per-channel acquisition state for every channel
    As a Pre-hospital Clinician I want every monitored channel to show whether it is live, acquiring, or has no data
    So that I never mistake an unmeasured channel for a normal patient reading

Rule: The MMSS shall, for every channel in the Acquired Parameters / Signals table, present a per-channel acquisition state of live, acquiring, or no-data, and shall never render an unacquired channel as a measured value.

Scenario: Unconnected channels show a no-data state, not a value
    Given the simulator is running
    And no sensors are connected in the simulator
    And the MMSS is running
    Then each of the following channels shows the acquisition state "no-data" and no measured value on the Display Interface
    | channel          |
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

Scenario: A channel transitions through acquiring to live as its sensor connects
    Given the simulator is running
    And no sensors are connected in the simulator
    And the MMSS is running
    When the ECG Electrodes are connected in the simulator
    Then the Heart Rate channel shows the acquisition state "acquiring" before valid acquisition is confirmed
    And the Heart Rate channel shows the acquisition state "live" only once valid acquisition is confirmed
    And the Heart Rate channel never renders a measured value while in the "acquiring" or "no-data" state
```

```gherkin
@ID:RQ_FN_03
Feature: Acquire and display every vital-sign parameter with its unit
    As a Pre-hospital Clinician I want every acquired vital sign shown with its unit and only when genuinely measured
    So that I read the patient's true condition without conversion or doubt

Rule: The MMSS shall acquire every vital-sign parameter enumerated in the Acquired Parameters / Signals table from its source measurement device and present each value with its unit on the monitor display, marking a channel as live only once valid acquisition is confirmed.

Scenario: Acquire and display Heart Rate from the ECG monitor
    Given the simulator is running
    And no sensors are connected in the simulator
    And the MMSS is running
    When the ECG Electrodes are connected in the simulator
    Then the following vital signs are displayed with their unit and marked live on the Display Interface within 1 second of acquisition (RQ_PR_02)
    | vital sign | unit |
    | Heart Rate | bpm  |

Scenario: Acquire and display the blood-pressure parameters from the NIBP cuff
    Given the simulator is running
    And no sensors are connected in the simulator
    And the MMSS is running
    When the NIBP Cuff is connected in the simulator
    Then the following vital signs are displayed with their unit and marked live on the Display Interface within 1 second of acquisition (RQ_PR_02)
    | vital sign   | unit |
    | Systolic BP  | mmHg |
    | Diastolic BP | mmHg |
    | MAP          | mmHg |

Scenario: Acquire and display the pulse-oximetry parameters from the SpO₂ probe
    Given the simulator is running
    And no sensors are connected in the simulator
    And the MMSS is running
    When the SpO₂ Probe is connected in the simulator
    Then the following vital signs are displayed with their unit and marked live on the Display Interface within 1 second of acquisition (RQ_PR_02)
    | vital sign | unit |
    | SpO2       | %    |
    | Pulse Rate | bpm  |

Scenario: Acquire and display the capnometry parameters from the EtCO₂ sampling line
    Given the simulator is running
    And no sensors are connected in the simulator
    And the MMSS is running
    When the EtCO₂ Sampling Line is connected in the simulator
    Then the following vital signs are displayed with their unit and marked live on the Display Interface within 1 second of acquisition (RQ_PR_02)
    | vital sign       | unit        |
    | Respiratory Rate | breaths/min |
    | EtCO2            | mmHg        |

Scenario: Acquire and display Temperature from the thermal probe
    Given the simulator is running
    And no sensors are connected in the simulator
    And the MMSS is running
    When the Temperature Probe is connected in the simulator
    Then the following vital signs are displayed with their unit and marked live on the Display Interface within 1 second of acquisition (RQ_PR_02)
    | vital sign  | unit |
    | Temperature | °C   |

Scenario: Acquire and display BIS from the EEG monitor
    Given the simulator is running
    And no sensors are connected in the simulator
    And the MMSS is running
    When the EEG Electrodes are connected in the simulator
    Then the following vital signs are displayed with their unit and marked live on the Display Interface within 1 second of acquisition (RQ_PR_02)
    | vital sign | unit          |
    | BIS        | index (0–100) |

Scenario: Acquire and display all parameters when all sensors are connected
    Given the simulator is running
    And no sensors are connected in the simulator
    And the MMSS is running
    When the ECG Electrodes are connected in the simulator
    And the NIBP Cuff is connected in the simulator
    And the SpO₂ Probe is connected in the simulator
    And the EtCO₂ Sampling Line is connected in the simulator
    And the Temperature Probe is connected in the simulator
    And the EEG Electrodes are connected in the simulator
    Then each of the following vital signs is acquired over its device's published interface contract and rendered to the Display Interface with its unit and marked live within 1 second of acquisition (RQ_PR_02, RQ_PR_11, RQ_IF_09, RQ_CS_03)
    | vital sign       | unit          |
    | Heart Rate       | bpm           |
    | Systolic BP      | mmHg          |
    | Diastolic BP     | mmHg          |
    | MAP              | mmHg          |
    | SpO2             | %             |
    | Pulse Rate       | bpm           |
    | Respiratory Rate | breaths/min   |
    | EtCO2            | mmHg          |
    | Temperature      | °C            |
    | BIS              | index (0–100) |
```

```gherkin
@ID:RQ_FN_04
Feature: Refresh live vital-sign values at least once per second
    As a Pre-hospital Clinician I want every live vital sign refreshed at least once a second
    So that I never rely on a stale reading at a glance

Rule: The MMSS shall refresh the displayed vital-sign values at least once per second for every live channel.

Scenario: Each live channel updates at least once per second
    Given the simulator is running
    And all sensors are connected in the simulator
    And the MMSS is running with every channel marked live
    When the simulator sets each channel to a distinct new value and holds it
    Then each live channel on the Display Interface updates to the new value within the following refresh interval (RQ_PR_03)
    | channel          | maximum refresh interval |
    | Heart Rate       | 1 second                 |
    | Systolic BP      | 1 second                 |
    | Diastolic BP     | 1 second                 |
    | MAP              | 1 second                 |
    | SpO2             | 1 second                 |
    | Pulse Rate       | 1 second                 |
    | Respiratory Rate | 1 second                 |
    | EtCO2            | 1 second                 |
    | Temperature      | 1 second                 |
    | BIS              | 1 second                 |

Scenario: Refresh cadence is sustained under low input rate
    Given the simulator is running
    And all sensors are connected in the simulator
    And the MMSS is running with every channel marked live
    When the simulator delivers input at a sustained rate of 0.1 Hz per channel
    Then every live channel continues to refresh at least once per second using the most recent value without loss of that value (RQ_PR_04)
```

```gherkin
@ID:RQ_FN_05
Feature: Flag out-of-range vital-sign values unmistakably
    As a Pre-hospital Clinician I want abnormal values to stand out unmistakably at a glance
    So that deterioration is recognised before it is missed in adverse conditions

Rule: The MMSS shall present each acquired vital-sign value with an unmistakable, distinguishable out-of-range indication whenever the value crosses its configured abnormal threshold.

Scenario Outline: An out-of-range value is flagged distinctly while an in-range value is not
    Given the simulator is running
    And the <sensor> is connected in the simulator
    And the MMSS is running with the <channel> channel marked live
    And the <channel> channel is configured with the abnormal threshold <threshold>
    When the simulator drives the <channel> value to the in-range value <normal value>
    Then the <channel> tile shows no out-of-range indication
    When the simulator drives the <channel> value to the out-of-range value <abnormal value>
    Then the <channel> tile shows an unmistakable, distinguishable out-of-range indication
    And the out-of-range indication is visually distinct from the in-range presentation

    Examples:
    | sensor            | channel     | threshold       | normal value | abnormal value |
    | SpO₂ Probe        | SpO2        | low < 90 %      | 98 %         | 82 %           |
    | ECG Electrodes    | Heart Rate  | high > 150 bpm  | 78 bpm       | 175 bpm        |
    | Temperature Probe | Temperature | high > 38.5 °C  | 37.0 °C      | 39.8 °C        |
    | NIBP Cuff         | Systolic BP | high > 180 mmHg | 122 mmHg     | 195 mmHg       |

Scenario: A value held just inside the threshold carries no out-of-range indication
    Given the simulator is running
    And the SpO₂ Probe is connected in the simulator
    And the MMSS is running with the SpO2 channel marked live
    And the SpO2 channel is configured with the abnormal threshold low < 90 %
    When the simulator drives the SpO2 value to 91 % which is just within its configured threshold
    Then the SpO2 tile shows no out-of-range indication
```

```gherkin
@ID:RQ_FN_06
Feature: Present continuous monitoring with a system-health indication
    As a Critical-Care Nurse I want continuous vital-signs presentation and a visible health indication
    So that I can trust monitoring is live while attending to other patients

Rule: The MMSS shall continuously present the acquired vital signs throughout sustained operation and display a perceptible system-health indication that monitoring is live.

Scenario: System-health indication shows monitoring is live during continuous operation
    Given the simulator is running
    And all sensors are connected in the simulator
    And the MMSS is running with every channel marked live
    When monitoring continues without interruption for a representative run of at least 10 minutes
    Then the acquired vital signs remain continuously presented on the Display Interface throughout the run
    And a perceptible system-health indication shows that monitoring is live throughout the run
    And no interval occurs in which vital-signs presentation is lost without an explicit perceptible indication to the clinician (RQ_NF_01)

Scenario: Timing budgets and resource use hold across a 24-hour soak
    Given the simulator is running
    And all sensors are connected in the simulator
    And the MMSS is running with every channel marked live
    When monitoring continues without interruption for a continuous soak period of at least 24 hours (RQ_PR_12)
    Then a perceptible system-health indication shows that monitoring is live throughout the period
    And the acquired vital signs remain continuously presented on the Display Interface throughout the period
    And every acquisition, refresh, and alarm-latency budget measured at the end of the period still meets the following limits as at the start (RQ_PR_12)
    | budget                  | limit at start | limit at end |
    | acquisition-to-display  | ≤ 1 second     | ≤ 1 second   |
    | display refresh interval| ≤ 1 second     | ≤ 1 second   |
    | detection-to-alarm      | ≤ 1 second     | ≤ 1 second   |
    And process memory and handle/thread counts at the end show no cumulative growth that would breach those budgets (RQ_PR_12)
```

```gherkin
@ID:RQ_FN_07
Feature: Detect and alert on a monitoring freeze via an independent liveness reference
    As a Critical-Care Nurse I want any freeze, interruption, or restart of monitoring to become perceptible
    So that a silent monitoring gap on an unattended patient never gives a false sense of safety

Rule: The MMSS shall continuously emit, against an independent timing reference, a liveness indication that advances only while monitoring is running, shall make any interruption, freeze, or restart perceptible at the boundary, and shall raise an explicit perceptible alert on that condition; a frozen or stalled display shall never be presentable as if it were live.

Scenario: Liveness indication advances while monitoring runs
    Given the simulator is running
    And the MMSS is running and monitoring with a configured liveness interval of 1 second
    When monitoring runs uninterrupted for at least 5 seconds
    Then the liveness indication advances against its independent timing reference at least once per liveness interval

Scenario: A monitoring freeze raises a perceptible interruption alert
    Given the simulator is running
    And the MMSS is running and monitoring with a configured liveness interval of 1 second
    When the test harness injects a monitoring freeze that stalls the liveness indication for longer than the configured liveness interval
    Then an explicit, perceptible interruption alert is raised within the following time (RQ_PR_13)
    | event                       | maximum time |
    | liveness stall to alert     | 1 second     |
    And the frozen display is not presentable as if it were live
    And the monitoring loss is made explicitly perceptible to the clinician rather than left silent (RQ_NF_01)

Scenario: The freeze alert is raised from the independent liveness path, not the monitoring path it protects
    Given the simulator is running
    And the MMSS is running and monitoring with a configured liveness interval of 1 second
    When the test harness freezes the monitoring path so it can neither advance nor self-report its own stall
    Then the interruption alert is still raised within 1 second from the independent liveness reference, demonstrating the safeguard does not share the failure of the frozen monitoring path (RQ_NF_12, RQ_PR_13)

Scenario: A restart of monitoring is made perceptible
    Given the simulator is running
    And the MMSS is running and monitoring
    When the MMSS restarts and returns to service
    Then an explicit, perceptible interruption alert is raised within 1 second of the system returning to service (RQ_PR_13)
```

```gherkin
@ID:RQ_FN_08
Feature: Raise a parameter-specific abnormal-condition alarm within 1 second
    As a Critical-Care Nurse I want an immediate alarm identifying which parameter is abnormal and how urgent it is
    So that I can intervene before the patient deteriorates

Rule: The MMSS shall raise, within 1 second of detecting an abnormal vital-sign condition, an immediate alarm that identifies which parameter is abnormal and its urgency level.

Scenario Outline: An abnormal value raises a parameter-specific alarm within 1 second
    Given the simulator is running
    And the <sensor> is connected in the simulator
    And the MMSS is running with the <channel> channel marked live showing the in-range value <normal value>
    When the simulator steps the <channel> value from <normal value> to <abnormal value>, crossing its configured abnormal threshold
    Then an alarm identifying the <channel> parameter and its urgency level is raised within the following time (RQ_PR_05)
    | event              | maximum time |
    | detection to alarm | 1 second     |

    Examples:
    | sensor              | channel     | normal value | abnormal value |
    | ECG Electrodes      | Heart Rate  | 78 bpm       | 175 bpm        |
    | SpO₂ Probe          | SpO2        | 98 %         | 82 %           |
    | EtCO₂ Sampling Line | EtCO2       | 40 mmHg      | 18 mmHg        |
    | NIBP Cuff           | Systolic BP | 122 mmHg     | 195 mmHg       |

Scenario: Concurrent abnormal conditions each raise their own alarm under full load
    Given the simulator is running
    And all sensors are connected in the simulator
    And the MMSS is running with every channel marked live
    When the simulator simultaneously steps Heart Rate to 175 bpm and SpO2 to 82 %, crossing both abnormal thresholds
    Then a parameter-specific alarm is raised for Heart Rate within 1 second (RQ_PR_05, RQ_PR_11)
    And a parameter-specific alarm is raised for SpO2 within 1 second (RQ_PR_05, RQ_PR_11)
```

```gherkin
@ID:RQ_FN_09
Feature: Annunciate abnormal-condition alarms multi-modally and latch them
    As a Critical-Care Nurse I want alarms I can perceive in noisy, mobile conditions and that do not self-clear unnoticed
    So that a clinically significant condition is never missed while I am away

Rule: The MMSS shall present abnormal-condition alarms multi-modally (audible and visual) such that they are perceptible in noisy and mobile conditions and shall keep each alarm latched until the condition resolves or the clinician acknowledges it.

Scenario: An abnormal-condition alarm is presented audibly and visually
    Given the simulator is running
    And the ECG Electrodes are connected in the simulator
    And the MMSS is running with the Heart Rate channel marked live showing 78 bpm
    When the simulator steps Heart Rate to 175 bpm, crossing its abnormal threshold
    Then the alarm is presented through both of the following modalities
    | modality |
    | audible  |
    | visual   |

Scenario: An unacknowledged alarm latches until acknowledged
    Given the simulator is running
    And the ECG Electrodes are connected in the simulator
    And the MMSS is running with the Heart Rate channel marked live showing 175 bpm with an abnormal-condition alarm active
    When the simulator returns Heart Rate to 78 bpm (within range)
    And the clinician has not acknowledged the alarm
    Then the alarm remains latched and perceptible until the clinician acknowledges it

Scenario: An alarm clears when the condition resolves and is acknowledged
    Given the simulator is running
    And the ECG Electrodes are connected in the simulator
    And the MMSS is running with the Heart Rate channel marked live showing 175 bpm with an abnormal-condition alarm active
    When the simulator returns Heart Rate to 78 bpm (within range)
    And the clinician acknowledges the alarm
    Then the alarm clears
```

```gherkin
@ID:RQ_FN_10
Feature: Distinguish clinical alarms from sensor-fault warnings
    As a Critical-Care Nurse I want clinical alarms and sensor-fault warnings to be unmistakably different
    So that I never take the wrong action by confusing a fault for a clinical condition

Rule: The MMSS shall make abnormal-condition clinical alarms distinguishable from sensor-fault warnings by distinct audible tone, colour, icon, and text, conforming to recognised alarm-safety practice.

Scenario: A clinical alarm and a sensor-fault warning differ across every channel
    Given the simulator is running
    And the SpO₂ Probe is connected in the simulator
    And the ECG Electrodes are connected in the simulator
    And the MMSS is running with the SpO2 channel marked live showing 98 %
    When the simulator steps SpO2 to 82 %, crossing its abnormal threshold and raising a clinical alarm
    And the simulator disconnects the ECG Electrodes raising a sensor-fault warning
    Then the clinical alarm and the sensor-fault warning differ in each of the following channels (RQ_NF_08)
    | channel      |
    | audible tone |
    | colour       |
    | icon         |
    | text         |
```

```gherkin
@ID:RQ_FN_11
Feature: Bound and conspicuously indicate alarm suspension
    As a Critical-Care Nurse I want alarm suspension to be time-limited, always visible, and to remind me before it ends
    So that the patient is never left silently unmonitored after a forgotten silence

Rule: The MMSS shall permit alarms to be suspended only for a bounded interval after which they automatically restore, shall display a persistent conspicuous indication for the whole period alarms are suspended, and shall raise an escalating reminder as the suspension window expires.

Scenario: Suspended alarms restore automatically after the bounded interval
    Given the simulator is running
    And the MMSS is running with alarms active
    And the bounded alarm-suspension interval is configured to 120 seconds
    When the clinician suspends alarms
    Then a persistent conspicuous "alarms suspended" indication is displayed for the whole suspension period
    And the system asserts the following over the suspension window
    | time after suspension | expected behaviour                                  |
    | 10 seconds            | suspension indication still displayed               |
    | 105 seconds           | an escalating reminder is raised before the window ends |
    | 120 seconds           | alarms automatically restore and the indication clears |

Scenario: Alarm suspension cannot be extended indefinitely
    Given the simulator is running
    And the MMSS is running with alarms suspended for the configured 120-second interval
    When no clinician action is taken before the interval ends
    Then alarms automatically restore at 120 seconds without requiring any clinician action
```

```gherkin
@ID:RQ_FN_12
Feature: Detect sensor disconnection, misplacement, or unreliable readings within 1 second
    As a Critical-Care Nurse I want sensor faults detected promptly from device signalling and input inactivity
    So that I am warned before false or missing data is trusted

Rule: The MMSS shall detect, within 1 second, a measurement-device disconnection, misplacement, or unreliable-reading condition for any device whenever the device asserts its ICD-defined fault or quality flag, or valid input is absent for the configured short inactivity window, relying only on the device's signalling plus inactivity.

Scenario: A device-asserted fault flag is detected within 1 second
    Given the simulator is running
    And the SpO₂ Probe is connected in the simulator
    And the MMSS is running with the SpO2 channel marked live
    When the simulator asserts the SpO₂ device fault flag at the interface
    Then the fault condition is detected within the following time (RQ_PR_07)
    | event                      | maximum time |
    | fault signalling to detect | 1 second     |

Scenario: Sustained input inactivity triggers a connection alarm at 5 seconds and not before
    Given the simulator is running
    And the ECG Electrodes are connected in the simulator
    And the MMSS is running with the Heart Rate channel marked live showing 78 bpm
    When the simulator stops delivering valid input on the Heart Rate channel
    Then the connection (sensor-inactivity) alarm behaves as follows over the inactivity window (RQ_PR_06)
    | elapsed inactivity | connection alarm |
    | 4 seconds          | not raised       |
    | 5 seconds          | raised           |
```

```gherkin
@ID:RQ_FN_13
Feature: Raise a sensor-fault warning and remove the untrustworthy value
    As a Critical-Care Nurse I want a faulted channel marked untrustworthy with no value shown
    So that I never act on a stale or implausible reading as if it were live

Rule: The MMSS shall, on detecting a sensor disconnection, misplacement, or fault, raise a sensor-fault warning distinguishable from a clinical alarm, visibly mark the affected parameter as untrustworthy, and replace its displayed value with an explicit no-data/untrustworthy state instead of a stale or implausible value.

Scenario: A faulted channel is marked untrustworthy and its value removed
    Given the simulator is running
    And the SpO₂ Probe is connected in the simulator
    And the MMSS is running with the SpO2 channel marked live showing 97 %
    When the simulator disconnects the SpO₂ Probe
    Then a sensor-fault warning distinguishable from a clinical alarm is raised within 1 second of detection (RQ_PR_07)
    And the SpO2 channel is visibly marked untrustworthy
    And the SpO2 channel shows an explicit no-data/untrustworthy state instead of the last value 97 %

Scenario: The device's own fault signalling is consumed at the boundary without suppressing the device's independent alarm
    Given the simulator is running
    And the SpO₂ Probe is connected in the simulator
    And the MMSS is running with the SpO2 channel marked live showing 97 %
    When the simulator asserts the SpO₂ device's ICD-defined fault signalling and the device emits its own independent fault alarm
    Then the MMSS receives and acts on the device fault signalling, marking the SpO2 channel untrustworthy (RQ_IF_08)
    And the simulator's device-side independent fault alarm remains asserted and is not suppressed or overridden by the MMSS (RQ_IF_08, RQ_NF_12)
```

```gherkin
@ID:RQ_FN_14
Feature: Restore a channel to trusted state on re-acquisition and re-flag on each loss
    As a Critical-Care Nurse I want a recovered channel to become trusted again and a flickering channel re-flagged on every loss
    So that I can re-seat a sensor yet never intermittently believe an unreliable channel

Rule: The MMSS shall return an affected channel to a live, trusted state once valid acquisition resumes, and shall mark the channel untrustworthy on each loss of valid acquisition for an intermittently faulting channel rather than alternating between trusted and fault states unsafely.

Scenario: A channel returns to trusted state when valid acquisition resumes
    Given the simulator is running
    And the SpO₂ Probe is connected in the simulator
    And the MMSS is running with the SpO2 channel marked live showing 97 %
    And the simulator has disconnected the SpO₂ Probe so the SpO2 channel is marked untrustworthy
    When the simulator reconnects the SpO₂ Probe and resumes valid acquisition at 96 %
    Then the SpO2 channel returns to a live, trusted state and displays 96 %

Scenario: An intermittently faulting channel is marked untrustworthy on each loss
    Given the simulator is running
    And the ECG Electrodes are connected in the simulator
    And the MMSS is running with the Heart Rate channel marked live showing 78 bpm
    When the simulator drops and restores valid acquisition on the Heart Rate channel 5 times in succession, each loss lasting at least 2 seconds
    Then the Heart Rate channel is marked untrustworthy on each of the 5 loss intervals
    And the Heart Rate channel is not displayed as trusted during any loss interval
    And the Heart Rate channel returns to trusted only while valid acquisition is present
```

```gherkin
@ID:RQ_FN_15
Feature: Present ranked diagnostic candidates within 1 second of receipt
    As an Emergency Physician I want ranked diagnostic candidates shown beside the vital signs promptly
    So that I can reach a working diagnosis faster, including when no colleague is available

Rule: The MMSS shall submit the conditioned patient parameter set to the external diagnostic AI capability and, given a complete ranked-candidate response received at the diagnostic-AI interface, present those candidates alongside the raw vital signs within 1 second of the response being fully received at that boundary.

Scenario: Ranked candidates are presented within 1 second of full receipt
    Given the simulator is running
    And the MMSS is running with vital signs being acquired
    And a diagnostic-AI stub stands in for the external capability at the diagnostic-AI interface (RQ_IF_10)
    When the diagnostic-AI stub returns the following complete ranked-candidate response at the interface
    | rank | candidate          | confidence |
    | 1    | Sepsis             | 0.74       |
    | 2    | Pulmonary embolism | 0.18       |
    | 3    | Pneumonia          | 0.08       |
    Then the ranked diagnostic candidates are presented alongside the raw vital signs within the following time (RQ_PR_08)
    | event                        | maximum time |
    | full receipt to presentation | 1 second     |
```

```gherkin
@ID:RQ_FN_16
Feature: Present each diagnostic candidate with confidence, reasoning, and driving parameters
    As an Emergency Physician I want each candidate's confidence, reasoning, and driving vital signs at a glance with detail on demand
    So that I can judge whether it fits the patient and recognise when it rests on a parameter I distrust

Rule: The MMSS shall present each diagnostic candidate with its confidence and its supporting reasoning — including the driving vital-sign parameters — absorbable at a glance, with fuller detail available on demand.

Scenario: Each candidate shows confidence, reasoning, and driving parameters
    Given the simulator is running
    And the MMSS is running with vital signs being acquired
    And a diagnostic-AI stub stands in for the external capability at the diagnostic-AI interface
    When the diagnostic-AI stub returns the following candidate with confidence, reasoning, and driving parameters
    | candidate | confidence | supporting reasoning                            | driving vital-sign params      |
    | Sepsis    | 0.74       | tachycardia with low EtCO2 and high temperature | Heart Rate, EtCO2, Temperature |
    Then the presented Sepsis candidate shows each of the following at a glance
    | element                   |
    | confidence                |
    | supporting reasoning      |
    | driving vital-sign params |

Scenario: Fuller candidate detail is available on demand
    Given the simulator is running
    And a diagnostic-AI stub has returned the Sepsis candidate and it is presented
    When the clinician requests fuller detail for the Sepsis candidate
    Then the fuller supporting detail for the Sepsis candidate is presented

Scenario Outline: Out-of-scope diagnostic output is withheld or marked out-of-scope rather than presented as in-scope
    Given the simulator is running
    And the MMSS is running with vital signs being acquired
    And a diagnostic-AI stub stands in for the external capability at the diagnostic-AI interface (RQ_IF_10)
    When the submitted input parameter set is <input vs scope> the supplier-declared validated intended-use scope
    And the returned output's supplier scope/applicability flag is <output flag>
    Then the diagnostic output is <expected handling> rather than presented or exchanged as in-scope (RQ_NF_13)

    Examples:
    | input vs scope | output flag  | expected handling                                              |
    | within         | in-scope     | presented normally with no out-of-scope indication            |
    | outside        | in-scope     | withheld or accompanied by an explicit out-of-scope indication |
    | within         | out-of-scope | withheld or accompanied by an explicit out-of-scope indication |
```

```gherkin
@ID:RQ_FN_17
Feature: Distinguish provisional from settled candidates and signal revisions
    As an Emergency Physician I want provisional candidate lists distinguished from settled ones and material ranking changes made salient
    So that I am not anchored on an early candidate or blind to a revision

Rule: The MMSS shall visibly distinguish a still-converging (provisional) candidate list from a settled one and make a materially changed ranking salient so a revision is noticed rather than missed.

Scenario: A still-converging candidate list is marked provisional
    Given the simulator is running
    And the MMSS is running with vital signs being acquired
    And a diagnostic-AI stub stands in for the external capability at the diagnostic-AI interface
    When the diagnostic-AI stub returns a response flagged as still-converging (provisional)
    Then the candidate list is visibly distinguished as provisional
    When the diagnostic-AI stub returns a subsequent response flagged as settled
    Then the candidate list is visibly distinguished as settled, not provisional

Scenario: A material ranking change is made salient
    Given the simulator is running
    And a diagnostic-AI stub has returned the following provisional ranking which is presented
    | rank | candidate          |
    | 1    | Pneumonia          |
    | 2    | Sepsis             |
    When the diagnostic-AI stub returns a revised response that reorders the ranking
    | rank | candidate          |
    | 1    | Sepsis             |
    | 2    | Pneumonia          |
    Then the new top-ranked candidate Sepsis is made salient so the revision is noticed
```

```gherkin
@ID:RQ_FN_18
Feature: Frame diagnostic output as non-gating decision support
    As an Emergency Physician I want the diagnostic output framed as decision support that never gates my action
    So that final diagnostic and treatment authority stays with me and automation bias is mitigated

Rule: The MMSS shall frame and label the diagnostic output unambiguously as decision support that informs rather than replaces the clinician, and shall impose no workflow gate, confirmation, or override on a candidate that could prevent or delay the clinician acting on their own judgement.

Scenario: Diagnostic output is persistently labelled as decision support
    Given the simulator is running
    And a diagnostic-AI stub has returned ranked candidates which are presented
    Then a persistent, unambiguous "decision support — not a diagnosis" indication is shown with the candidates (RQ_NF_14)

Scenario: The clinician can act on their own judgement without any gate
    Given the simulator is running
    And a diagnostic-AI stub has returned ranked candidates which are presented
    When the clinician proceeds with their own clinical decision without acknowledging a candidate
    Then the MMSS presents no blocking confirmation, override, or candidate-acknowledgement prompt
    And the clinician's action is accepted immediately with no MMSS-imposed delay
```

```gherkin
@ID:RQ_FN_19
Feature: Signal a diagnostic time-out independently of the candidate path
    As a Pre-hospital Clinician I want a positive time-out indication when no diagnosis is produced in the expected time
    So that I know not to keep waiting and can fall back on my own assessment without delaying care

Rule: The MMSS shall, when no diagnostic result is produced within the expected convergence time, present a positive perceptible time-out indication delivered independently of the diagnostic candidate-result path and an explicit "no diagnosis available — proceed on your own assessment" message, and shall not leave the candidate area silently blank.

Scenario: A diagnostic time-out is signalled positively after the convergence deadline
    Given the simulator is running
    And a diagnostic-AI stub stands in for the external capability with its convergence time-out configured to 2 minutes
    And the MMSS is running with a diagnostic request in progress
    When the diagnostic-AI stub returns no candidate result for the full 2-minute convergence window owned by the external capability (RQ_PR_10, RQ_CS_09)
    Then the candidate area shows a "diagnosis in progress" state and is not left silently blank before the deadline
    And after the 2-minute deadline a positive, perceptible time-out indication is presented
    And the explicit message "no diagnosis available — proceed on your own assessment" is shown

Scenario: The time-out indication is delivered independently of the candidate-result path
    Given the simulator is running
    And a diagnostic-AI stub stands in for the external capability at the diagnostic-AI interface
    And the MMSS is running with a diagnostic request in progress
    When the diagnostic-AI stub emits its independent convergence-time-out notification while the candidate-result path returns nothing (RQ_IF_11)
    Then the time-out indication is presented from that independent notification, not from the candidate-result path (RQ_IF_11, RQ_NF_12)
```

```gherkin
@ID:RQ_FN_20
Feature: Exchange vital-sign data and diagnostic findings with the HIS on request
    As an Emergency Physician I want to send vital signs and diagnostic findings to a confirmed recipient over a standard interface
    So that I can obtain a second opinion and hand over the patient smoothly and securely

Rule: The MMSS shall exchange the patient's vital-sign data and diagnostic findings with the hospital information system over the recognised interoperability standard on clinician request, delivering diagnostic candidates within 1 second of their availability, and shall require the receiving recipient to be confirmed before the exchange proceeds.

Scenario: Exchange requires a confirmed recipient before it proceeds
    Given the simulator is running
    And the MMSS is running with vital signs and diagnostic findings available
    And a HIS stub stands in for the hospital information system over a recognised HL7/FHIR-class interface (RQ_IF_12)
    When the clinician requests an exchange without confirming the recipient
    Then the exchange does not proceed and no message is sent to the HIS stub until the receiving recipient is confirmed

Scenario: Confirmed exchange delivers data within 1 second of request
    Given the simulator is running
    And the MMSS is running with vital signs and diagnostic findings available
    And a HIS stub stands in for the hospital information system over a recognised HL7/FHIR-class interface (RQ_IF_12)
    And the receiving recipient "Ward-A HIS" is confirmed
    When the clinician confirms the exchange request
    Then the vital-sign data and diagnostic findings are received at the HIS stub within the following time (RQ_PR_09)
    | event                         | maximum time |
    | confirmed request to delivery | 1 second     |
    And diagnostic candidates are delivered within 1 second of their availability (RQ_PR_09)
    And the exchange is carried over the recognised HL7/FHIR-class interoperability standard (RQ_CS_04)

Scenario: Personal health data is exchanged with confidentiality, integrity, and an audit record
    Given the simulator is running
    And the MMSS is running with vital signs and diagnostic findings available for patient record "MRN-00427"
    And a HIS stub stands in for the hospital information system over a recognised HL7/FHIR-class secured interface (RQ_IF_12)
    And the receiving recipient "Ward-A HIS" is confirmed
    When a passive network observer captures the traffic while the clinician confirms the exchange request
    Then the captured payload does not expose the personal health data in clear (confidentiality protected) (RQ_IF_13, RQ_NF_04)
    And the HIS stub validates the integrity of the received message and detects no tampering (RQ_IF_13, RQ_NF_04)
    And the MMSS records a tamper-evident audit entry for the access to and exchange of the personal health data (RQ_NF_04)
```

```gherkin
@ID:RQ_FN_21
Feature: Confirm transfer outcome and flag partial or failed transfers
    As an Emergency Physician I want explicit confirmation of a complete transfer and an explicit flag on any partial or failed one
    So that neither end falsely believes the information is in hand

Rule: The MMSS shall give explicit confirmation of a successful, complete transfer to the correct patient record and shall explicitly flag any partial or failed transfer with the option to retry, rather than reporting success.

Scenario: A complete transfer is explicitly confirmed to the correct record
    Given the simulator is running
    And a HIS stub stands in for the hospital information system over a recognised HL7/FHIR-class interface
    And the MMSS has sent an exchange to the confirmed HIS recipient "Ward-A HIS" for patient record "MRN-00427"
    When the HIS stub returns a protocol acknowledgement of a successful, complete transfer to "MRN-00427" (RQ_IF_12)
    Then the MMSS shows explicit confirmation of a successful, complete transfer to patient record "MRN-00427"

Scenario Outline: A failed or partial transfer is flagged with a retry option
    Given the simulator is running
    And a HIS stub stands in for the hospital information system over a recognised HL7/FHIR-class interface
    And the MMSS has sent an exchange to the confirmed HIS recipient "Ward-A HIS"
    When the HIS stub returns an acknowledgement indicating a <outcome> transfer (RQ_IF_12)
    Then the MMSS explicitly flags the transfer as <outcome>
    And the MMSS offers the option to retry
    And the MMSS does not report the transfer as successful

    Examples:
    | outcome |
    | partial |
    | failed  |
```

```gherkin
@ID:RQ_FN_22
Feature: Persistently surface safety-relevant working state and sustain monitoring to handover
    As a Critical-Care Nurse I want the device's safety-relevant working state always visible and monitoring sustained until handover is confirmed
    So that critical state and live monitoring never fall through the gap between clinicians

Rule: The MMSS shall persistently surface the safety-relevant working state to any clinician at the device — untrustworthy channels, modified or suspended alarms or limits, and the current diagnostic candidate state — and shall continue presenting vital signs and active alarm state until handover to receiving monitoring is confirmed complete.

Scenario: Safety-relevant working state is persistently surfaced
    Given the simulator is running
    And all sensors are connected in the simulator
    And the MMSS is running with the SpO2 channel flagged untrustworthy after a simulated probe disconnection
    And alarms are currently suspended
    And a diagnostic-AI stub has returned a provisional candidate list which is present
    Then the Display Interface persistently surfaces each of the following working-state items
    | working-state item            |
    | channels flagged untrustworthy|
    | alarms suspended/modified     |
    | current candidate state       |

Scenario: Monitoring is sustained until handover is confirmed complete
    Given the simulator is running
    And all sensors are connected in the simulator
    And the MMSS is running and monitoring with an active alarm state
    When the clinician initiates handover to receiving monitoring
    And the receiving monitoring has not yet returned a handover-complete confirmation
    Then the MMSS continues presenting vital signs and the active alarm state
    When the receiving monitoring returns a handover-complete confirmation
    Then the MMSS may release continuity
```

```gherkin
@ID:RQ_FN_23
Feature: Provide a realistic risk-free simulated training mode
    As a Clinical Trainer / Super-User I want a simulated mode that behaves like live operation
    So that clinicians can build competence — including AI candidate interpretation — before live patient use

Rule: The MMSS shall provide a simulated training mode in which simulated vital signs, alarms, sensor faults, and diagnostic candidates behave as in live operation, allowing risk-free practice including AI candidate interpretation and bias avoidance.

Scenario: Simulated elements behave as in live operation
    Given the MMSS is running in training mode
    When the training scenario drives simulated patient data including an abnormal value, a sensor fault, and a candidate response
    Then each of the following exhibits the same observable behaviour as in live operation
    | simulated element     | observable behaviour as in live operation        |
    | vital signs           | displayed with unit and refreshed at least once per second |
    | alarms                | abnormal value raises a multi-modal alarm        |
    | sensor faults         | faulted channel marked untrustworthy, value removed |
    | diagnostic candidates | ranked candidates presented with confidence       |

Scenario: Training mode supports AI candidate interpretation practice
    Given the MMSS is running in training mode
    When the training scenario presents the following simulated diagnostic candidate
    | candidate | confidence | supporting reasoning                  |
    | Sepsis    | 0.74       | tachycardia with low EtCO2            |
    Then the candidate shows its confidence and reasoning so the trainee can practise interpretation and bias avoidance
```

```gherkin
@ID:RQ_FN_24
Feature: Enforce fail-safe separation between training and live operation
    As a Clinical Trainer / Super-User I want unmistakable, fail-safe separation between training and live modes
    So that simulated data is never mistaken for a real patient and a real patient is never monitored in training mode

Rule: The MMSS shall enforce fail-safe separation between training and live operation: requiring explicit confirmation to enter and exit training mode, displaying a persistent always-visible mode indicator and watermarking all simulated data, and defaulting to live operation on restart or return to the device.

Scenario: Entering and exiting training mode requires explicit confirmation
    Given the MMSS is running in live operation
    When the user requests to enter training mode
    Then the MMSS requires explicit confirmation before entering training mode
    And on requesting to exit, the MMSS requires explicit confirmation before returning to live operation

Scenario: Simulated operation is persistently indicated and watermarked
    Given the MMSS is running in training mode
    Then a persistent, always-visible training-mode indicator is displayed
    And all simulated data is watermarked as simulated

Scenario: The MMSS defaults to live operation on restart
    Given the MMSS is running in training mode
    When the MMSS restarts or is returned to the device
    Then the MMSS defaults to live operation
```

```gherkin
@ID:RQ_FN_25
Feature: Commission devices through published contracts with guided verification
    As a Biomedical / Clinical Engineer I want contract-only connection with per-channel feedback and guided mapping verification
    So that I integrate the fleet without modifying external elements and prevent a mis-mapped channel reaching clinical use

Rule: The MMSS shall connect to each of the six measurement-device types and to the hospital information system strictly through their published interface contracts, shall provide clear per-channel interface and fault feedback, and shall provide a guided verification step confirming each acquired parameter maps to the correct device and display field before the device is released for clinical use.

Scenario: Each device connects through its published interface contract with per-channel feedback
    Given the simulator is running
    And the MMSS is in commissioning mode
    When the engineer connects each measurement-device type through its published interface contract
    Then the MMSS shows clear per-channel interface and fault feedback for each of the following devices (RQ_IF_02, RQ_IF_03, RQ_IF_04, RQ_IF_05, RQ_IF_06, RQ_IF_07)
    | device                | interface | expected per-channel feedback     |
    | ECG monitor           | IF_02     | Heart Rate channel: connected, no fault |
    | Blood pressure monitor| IF_04     | Systolic/Diastolic/MAP: connected, no fault |
    | Pulse oximeter        | IF_03     | SpO2/Pulse Rate: connected, no fault |
    | Capnometer            | IF_06     | Respiratory Rate/EtCO2: connected, no fault |
    | Thermal probe         | IF_05     | Temperature channel: connected, no fault |
    | EEG monitor           | IF_07     | BIS channel: connected, no fault  |

Scenario: A guided verification step blocks release on an unconfirmed mapping
    Given the simulator is running
    And the MMSS is in commissioning mode
    When the engineer runs the guided per-channel verification step
    And one acquired parameter is not confirmed against its correct device and display field
    Then the MMSS does not release the device for clinical use until every channel mapping is confirmed

Scenario: A seeded mis-mapping is detected during guided verification
    Given the simulator is running
    And the MMSS is in commissioning mode with a seeded channel mis-mapping
    When the engineer runs the guided per-channel verification step
    Then the MMSS surfaces the mis-mapped channel so it can be corrected before release
```

```gherkin
@ID:RQ_FN_26
Feature: Apply software updates only through a use-aware controlled lifecycle workflow
    As a Biomedical / Clinical Engineer I want updates applied only through a controlled workflow that never disrupts a device in use
    So that the deployed fleet stays patchable over its service life without disrupting monitoring or returning unverified

Rule: The MMSS shall apply software updates only through the controlled lifecycle workflow, preventing or deferring any update to a device in active clinical use and verifying correct operation before the device is returned to service.

Scenario: An update is prevented or deferred while a device is in active clinical use
    Given the simulator is running with all sensors connected
    And the MMSS is in live operation monitoring a patient with channels marked live
    When the host platform stub initiates a software update over the host platform/OS interface (RQ_IF_14, RQ_IF_01)
    Then the MMSS does not apply the update while monitoring is active
    And the MMSS defers the update and continues uninterrupted monitoring

Scenario: An update is verified before the device is returned to service
    Given the MMSS is in live operation with no patient being monitored and no channels live
    When a software update is applied through the controlled lifecycle workflow via the host platform stub (RQ_IF_14)
    Then the MMSS runs its post-update verification and reports a successful readiness check
    And the MMSS does not return to service until the verification reports success
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
