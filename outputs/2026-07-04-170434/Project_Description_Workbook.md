---
Executed by: orchestration (CLAUDE.md)
Flow: flows/expectationeering-flow/flow.md
Templates: flows/expectationeering-flow/expectationeering-workbook.md
Inputs: inputs/
Date: 2026-07-04
---

# Expectationeering Workbook

**Product**: Mobile Monitoring Software Solution (MMSS)
**Date**: 2026-07-04
**Workshop Team**: User Stakeholder, Customer Stakeholder, Business Stakeholder, Regulatory Stakeholder, Product Owner, System Architect, Usability Validation, Development Lead, Verification Lead, Quality Assurance

---

# Introduction

This workbook captures the expectations and requirements for the product, from informal stakeholder expectations through to verifiable system requirements. Every requirement item has a unique identifier, starting with the stakeholder expectations, and each item traces to the upstream item it is derived from.

## Intended users of the document

Product management, system architects, development and verification teams, usability and regulatory specialists, and quality assurance of the legal manufacturer; notified-body and competent-authority reviewers as external readers.

## Scope of the document

The Mobile Monitoring Software Solution (MMSS): medical device software that runs on an existing portable patient monitor and provides continuous vital-signs monitoring with adjunctive AI-based diagnostic decision support for critically ill patients in ICU, emergency-room, and mobile/pre-hospital settings. This workbook covers the product definition from informal stakeholder expectations through verifiable system requirements and their BDD verification specification; architecture and item-level design are downstream and out of scope.

---

# Application

## Stakeholders (INFORMAL)

The stakeholder level is the start of the requirement approach. It captures the problem to be solved and the expectations of each stakeholder in a product-agnostic ("product-free") way.

### Problem

#### Domain Description

The domain is the monitoring and clinical assessment of critically ill patients by trained medical professionals in acute-care settings: intensive care units, emergency rooms, and mobile or pre-hospital emergency care (at the scene of an incident and in moving vehicles). In this domain, non-invasive physiological measurements — such as cardiac electrical activity, blood oxygen saturation, blood pressure, body temperature, exhaled carbon dioxide, and brain electrical activity — are acquired continuously from the patient and used to detect deterioration, form a differential diagnosis, and initiate treatment as early as possible. Time is the dominant clinical factor: outcomes for critically ill patients depend heavily on correct intervention within the first minutes of care (the "golden hour"). Any solution in this domain operates under the medical device regulatory framework, including software lifecycle standards (IEC 62304), risk management (ISO 14971), usability engineering (IEC 62366-1), alarm-system standards (IEC 60601-1-8), health-data protection law (GDPR/HIPAA), and emerging legal requirements for AI in medical applications.

#### Actual State

**Pros:**

- Portable patient monitors with proven, familiar non-invasive sensor technology are widely deployed and trusted across ICU, ER, and mobile emergency settings.
- Vital signs are displayed continuously and in real time, giving clinicians an immediate view of the patient's physiological state.
- Standard non-invasive measurement devices are established in routine clinical use, requiring no invasive procedures and minimal patient burden.
- Existing monitoring hardware fleets are already procured, serviced, and integrated into clinical workflows, and their regulatory status is established.

**Cons:**

- Monitors are passive: they display raw measurements but offer no diagnostic interpretation, leaving the full cognitive burden of differential diagnosis on the clinician under extreme time pressure.
- In the critical first minutes, clinicians must mentally synthesise multiple independent signal streams while simultaneously treating the patient, which delays diagnosis and increases the risk of missed or wrong diagnoses.
- Sensor misplacement, unreliable readings, and silently failing measurement sources can go unnoticed, so clinical decisions may be based on wrong or missing data.
- There is no structured, immediate sharing of live patient data with the receiving hospital, so second opinions and handover preparation are delayed.
- Clinicians have no realistic, risk-free environment in which to practise interpreting machine-generated clinical guidance before relying on it with real patients.

#### Desired State

**Pros (retained from the actual state):**

- Portable, familiar monitoring equipment with proven non-invasive sensor technology remains in use across ICU, ER, and mobile emergency settings.
- Vital signs remain continuously visible in real time.
- Standard non-invasive measurement devices remain the physiological data source, with no added patient burden.
- Existing hardware fleets, clinical workflows, and procurement relationships are preserved.

**Pros (added in the desired state):**

- Clinicians receive automated diagnostic decision support — ranked diagnostic candidates presented alongside the raw vital signs within the first minutes of connecting to the patient — so the right treatment can start inside the golden hour, while diagnostic accountability stays with the clinician.
- Monitoring is operational within seconds of arrival and demands minimal operation and attention, keeping hands and focus on the patient.
- Abnormal vital signs, misplaced or unreliable sensors, silent measurement-source failures, and any inability to deliver diagnostic guidance in the expected time are all detected and annunciated immediately, so decisions are never unknowingly based on wrong, stale, or missing data.
- Critical alarm functions remain available even when other functions fail.
- Live patient data can be shared with hospital information systems over recognised interoperability standards for second opinion and handover preparation.
- Clinicians can train on realistic simulated cases in a risk-free setting before clinical use, and completion of that training is evidenced.
- The capability is delivered, cleared, and maintained under the applicable medical device regulatory framework, with managed cybersecurity, protected health data, full lifecycle documentation, and post-market monitoring of real-world diagnostic performance.

**Cons:**

- Machine-generated diagnostic guidance introduces new hazards — misinterpretation, over-reliance, wrong or delayed suggestions — that must be controlled through training, clear separation of measured data from interpretation, independent safety mitigations, and regulatory evidence.
- The added intelligence, connectivity, and compliance obligations increase development, validation, and lifecycle-maintenance effort compared with a passive display device.

#### Identified Gaps (DC_*)

The design changes needed to move from the actual state to the desired state.

| ID | Description |
|----|-------------|
| DC_01 | Provide continuous, real-time acquisition and display of a comprehensive set of standard non-invasive vital-sign measurements with sub-second presentation latency. |
| DC_02 | Add automated diagnostic decision support that presents ranked, likelihood-ordered diagnostic candidates alongside the raw vital signs within the first minutes of patient connection, clearly distinguished from measured values and always subordinate to clinician judgement. |
| DC_03 | Make monitoring operational within seconds of power-on and reduce required operation and attention to a minimum, so no time or focus is taken from the patient. |
| DC_04 | Provide immediate clinical alarming when a vital sign becomes abnormal, with sub-second alarm latency and conformity to applicable alarm-system standards. |
| DC_05 | Detect and immediately annunciate technical fault conditions — sensor misplacement or unreliable readings, a measurement source that stops delivering data, connection failures, and any inability to deliver diagnostic guidance within the expected time. |
| DC_06 | Support use of one and the same solution across ICU, emergency room, and mobile/pre-hospital settings, including at the scene and in moving vehicles. |
| DC_07 | Back safety-critical alarm and diagnosis functions with independent mitigations so that critical alarming remains available when other functions fail and the software safety classification can be justifiably reduced. |
| DC_08 | Enable live exchange of patient data with hospital information systems over recognised health-informatics interoperability standards for second opinion and handover preparation. |
| DC_09 | Provide a realistic, risk-free simulation training capability with mandatory training provisions and evidence that users complete the training before clinical use. |
| DC_10 | Establish medical device qualification and market access: documented intended use, a software lifecycle process compliant with IEC 62304 at a justified safety classification, and early engagement with regulatory authorities. |
| DC_11 | Establish the clinical and risk evidence base for the diagnostic capability: lifecycle risk management per ISO 14971, usability engineering per IEC 62366-1 covering misinterpretation hazards, clinical evaluation of diagnostic performance using pre-validated evidence-backed algorithm components, and compliance with AI-specific legal requirements for transparency, human oversight, and data governance. |
| DC_12 | Deliver the capability as software only on the existing, unchanged monitoring hardware fleet, with high-risk technical aspects and performance targets validated early against the fixed platform. |
| DC_13 | Protect the solution and its data: cybersecurity risk management per applicable standards and patient health data protection per data-protection law. |
| DC_14 | Establish lifecycle assurance: design-control documentation with end-to-end traceability, compliant labelling/UDI/instructions for use, in-operation observability and reconstructability of alarms, faults, and diagnostic outputs, committed support/maintenance/update service with predictable cost of ownership, post-market surveillance including monitoring of real-world diagnostic performance drift, and change control for post-market modifications. |

### Expectations

Stakeholder expectations are written "product-free": they apply to any product in the problem domain, including competitors. Format: *The \<stakeholder\> wants \<expectation\> to \<benefit driver\>.*

#### User Expectations (UE_*)

**Stakeholder**: Clinician

Trained medical professionals — emergency physicians, paramedics, intensive-care and emergency-room nurses — who monitor and treat critically ill patients in ICUs, emergency rooms, and mobile medical units. They work under severe time pressure, often at the scene or in a moving vehicle, with their hands and attention on the patient, and must make rapid diagnostic and treatment decisions from whatever information is available at the bedside.

| ID | Expectation | Traces |
|----|-------------|--------|
| UE_01 | The Clinician wants a continuous, real-time view of a critically ill patient's key vital signs to spot deterioration the moment it happens. | DC_01 |
| UE_02 | The Clinician wants diagnostic guidance ranked by likelihood presented alongside the raw vital signs to prioritise the differential diagnosis and choose treatment faster under time pressure. | DC_02 |
| UE_03 | The Clinician wants a usable diagnostic direction within the first minutes after connecting a patient to start the right treatment inside the pre-hospital "golden hour". | DC_02 |
| UE_04 | The Clinician wants monitoring to be up and running within seconds of arriving at the patient to lose no time during an emergency response. | DC_03 |
| UE_05 | The Clinician wants to be alerted immediately when a vital sign becomes abnormal to intervene before the patient's condition worsens. | DC_04 |
| UE_06 | The Clinician wants to be warned when a sensor is misplaced or producing unreliable readings to avoid basing decisions — or a diagnosis — on wrong data. | DC_05 |
| UE_07 | The Clinician wants to be alerted promptly when a measurement source stops delivering data to ensure deterioration is never missed unnoticed during a signal loss. | DC_05 |
| UE_08 | The Clinician wants to be told explicitly when diagnostic guidance cannot be delivered in the expected time to fall back on their own clinical judgment without delaying treatment. | DC_05 |
| UE_09 | The Clinician wants the monitoring capability to be portable and usable at the scene and in moving vehicles to deliver full monitoring and diagnostic support outside hospital walls. | DC_06 |
| UE_10 | The Clinician wants monitoring and diagnostic support to work with minimal operation and attention to keep their hands and focus on the patient rather than on equipment. | DC_03 |
| UE_11 | The Clinician wants a comprehensive physiological picture obtained through standard non-invasive measurement methods to assess the patient thoroughly without invasive procedures. | DC_01 |
| UE_12 | The Clinician wants to share live patient data with the receiving hospital to obtain a second opinion and prepare the handover before arrival. | DC_08 |
| UE_13 | The Clinician wants to practise interpreting diagnostic guidance in a realistic, risk-free training setting to build trust in the guidance and use it correctly in real emergencies. | DC_09 |
| UE_14 | The Clinician wants a clear distinction between measured values and machine-generated interpretation to retain their own clinical judgment and accountability for the final diagnosis. | DC_02 |
| UE_15 | The Clinician wants critical alarms to keep working even when other functions fail to ensure patient safety never depends on a single point of failure. | DC_07 |

#### Market Expectations (ME_*)

**Stakeholder**: Hospital & EMS Procurement

The buying organisations are hospitals and emergency medical service providers acquiring patient-monitoring and clinical decision-support capability for ICUs, emergency rooms, and mobile medical units. They evaluate on regulatory market access, patient-safety risk, clinical outcome value (faster time-to-diagnosis), integration with existing equipment and hospital information systems, total cost of ownership, training and support commitments, and liability exposure from AI-assisted diagnosis.

| ID | Expectation | Traces |
|----|-------------|--------|
| ME_01 | The Hospital & EMS Procurement wants the solution to hold regulatory clearance for its intended clinical use in the target market to make purchase and deployment legally possible without exposure to enforcement action. | DC_10 |
| ME_02 | The Hospital & EMS Procurement wants the solution to be deliverable as a software capability on the monitoring hardware fleet already in service to avoid new capital equipment expenditure and fleet replacement cost. | DC_12 |
| ME_03 | The Hospital & EMS Procurement wants real-time diagnostic decision support delivered at the point of care within minutes of patient connection to shorten time-to-treatment and improve outcomes for critically ill patients. | DC_02 |
| ME_04 | The Hospital & EMS Procurement wants the solution to work with the standard non-invasive measurement devices already in clinical use (ECG, pulse oximetry, blood pressure, temperature, capnography, EEG) to protect existing sensor investments and avoid consumable lock-in. | DC_01 |
| ME_05 | The Hospital & EMS Procurement wants integration with hospital information systems over recognised healthcare interoperability standards (e.g. HL7/FHIR) to fit the existing IT landscape and enable clinical second opinions without custom interface projects. | DC_08 |
| ME_06 | The Hospital & EMS Procurement wants the solution to be operational within seconds of power-on to be usable in emergency and pre-hospital scenarios where setup time directly affects patient survival. | DC_03 |
| ME_07 | The Hospital & EMS Procurement wants vital signs, clinical alarms, and sensor-fault alarms presented with sub-second latency to meet the clinical response expectations of critical care and satisfy clinical alarm practice standards. | DC_01, DC_04, DC_05 |
| ME_08 | The Hospital & EMS Procurement wants safety-critical alarm and diagnosis functions backed by independent mitigations to bound patient-safety risk and the organisation's liability if any single function fails. | DC_07 |
| ME_09 | The Hospital & EMS Procurement wants any AI-based diagnostic capability to be built on clinically validated, evidence-backed models to gain medical-staff acceptance and withstand clinical governance and regulatory scrutiny. | DC_11 |
| ME_10 | The Hospital & EMS Procurement wants diagnostic suggestions presented as ranked candidates alongside raw vital signs, never replacing clinician judgement, to keep diagnostic accountability with the treating professional and limit malpractice exposure. | DC_02 |
| ME_11 | The Hospital & EMS Procurement wants a supplier-provided training offering, including simulation-based practice of the diagnostic support, to ensure safe adoption by clinical staff and reduce misinterpretation risk before live use. | DC_09 |
| ME_12 | The Hospital & EMS Procurement wants one solution usable across ICU, emergency room, and mobile-unit settings to standardise the fleet, simplify training, and reduce per-setting procurement and maintenance overhead. | DC_06 |
| ME_13 | The Hospital & EMS Procurement wants development and maintenance of the software to comply with the recognised medical-device software lifecycle standard (IEC 62304) to satisfy the organisation's quality-system and audit obligations. | DC_10 |
| ME_14 | The Hospital & EMS Procurement wants a committed support, maintenance, and update service over the equipment's service life to protect the investment and keep the installed base clinically safe and compliant as regulations evolve. | DC_14 |
| ME_15 | The Hospital & EMS Procurement wants a predictable total cost of ownership, including licensing, integration, training, and updates, to justify the acquisition against measurable clinical and operational benefits in budget approval. | DC_12, DC_14 |

#### Business Expectations (BE_*)

**Stakeholder**: Legal Manufacturer

The Legal Manufacturer is the organisation that designs, produces, and places the product on the market and bears full legal responsibility for its safety, performance, and conformity. This stakeholder voices all internal departments — Executive/Strategy, Legal & Compliance, Finance, Operations, R&D, Quality Management, Regulatory Affairs, Sales & Commercial, Customer Support & Service, and Human Resources — whose strategy, constraints, liability exposure, and delivery capacity bound what the organisation can commit to.

| ID | Expectation | Traces |
|----|-------------|--------|
| BE_01 | The Legal Manufacturer wants the product to comply with ANSI AAMI IEC 62304 and all applicable medical device regulations to secure market access and fulfil its legal obligations as manufacturer. | DC_10 |
| BE_02 | The Legal Manufacturer wants safety-critical functions to be mitigated by independent means so that the software safety classification can be reduced from the highest class, to keep development, documentation, and verification effort proportionate to budget and schedule. | DC_07 |
| BE_03 | The Legal Manufacturer wants the first release to rely on commercially available, pre-validated diagnostic algorithm components rather than custom-developed ones to reduce validation complexity, regulatory clearance risk, and time to market. | DC_11 |
| BE_04 | The Legal Manufacturer wants diagnostic output to be positioned as decision support for trained medical professionals — never as an autonomous diagnosis — to limit product liability exposure for clinical outcomes. | DC_02 |
| BE_05 | The Legal Manufacturer wants mandatory training provisions, including a simulation mode and hands-on instruction, to be part of the offering to mitigate use-error liability, reduce complaint volume, and keep the support burden manageable. | DC_09 |
| BE_06 | The Legal Manufacturer wants foreseeable fault conditions — such as sensor misplacement, connection loss, and diagnosis timeout — to be reliably detected and annunciated to the user to limit liability exposure from undetected failures with critical patient harm potential. | DC_05 |
| BE_07 | The Legal Manufacturer wants the solution to be deliverable as software only, running on the organisation's existing and unchanged hardware platform, to protect prior hardware investment and avoid new production, supply chain, and manufacturing qualification effort. | DC_12 |
| BE_08 | The Legal Manufacturer wants integration to be limited to a defined, bounded set of non-invasive measurement device types via standardised interfaces to contain integration scope, vendor dependencies, and verification cost. | DC_01 |
| BE_09 | The Legal Manufacturer wants exchange with hospital information systems to use recognised healthcare interoperability standards to meet market expectations, avoid proprietary lock-in, and keep future integration commitments affordable. | DC_08 |
| BE_10 | The Legal Manufacturer wants all design decisions, risk mitigations, and verification evidence documented under design control in a traceable technical file to satisfy quality management system requirements and pass internal governance and external audits. | DC_14 |
| BE_11 | The Legal Manufacturer wants regulatory authorities to be engaged early in development to reduce the risk of clearance delays for AI-supported diagnostic functionality jeopardising the launch window. | DC_10 |
| BE_12 | The Legal Manufacturer wants high-risk technical aspects — in particular real-time connectivity and multi-device integration — to be validated early through prototyping to de-risk the schedule and avoid late, costly rework. | DC_12 |
| BE_13 | The Legal Manufacturer wants performance targets to be confirmed against the fixed hardware platform early in the project to prevent portability and performance ambitions from exceeding the approved budget. | DC_12 |
| BE_14 | The Legal Manufacturer wants alarms, fault conditions, and diagnostic outputs to be observable and reconstructable in operation to support complaint handling, incident investigation, and post-market surveillance obligations. | DC_14 |
| BE_15 | The Legal Manufacturer wants the offering to extend its established patient monitoring position into AI-supported clinical decision support to grow portfolio value and secure long-term competitiveness in acute and mobile care markets. | DC_02 |

#### Regulatory Expectations (RE_*)

**Stakeholder**: Competent Authority / Notified Body

The regulatory stakeholder represents the competent authorities (e.g. FDA, EU Member State authorities under EU MDR), notified bodies auditing technical documentation and issuing conformity certificates, standards organisations whose harmonised standards confer presumption of conformity, and post-market surveillance and vigilance agencies. This stakeholder does not advocate for any product; it determines whether software providing real-time patient monitoring with AI-driven diagnostic decision support for critically ill patients may legally be placed on the market and remain there, and holds the legal manufacturer accountable to mandatory obligations before and after market access.

| ID | Expectation | Traces |
|----|-------------|--------|
| RE_01 | The Competent Authority wants any software that monitors vital signs and provides diagnostic decision support for critically ill patients to be qualified and classified as a medical device under the applicable market-access legislation (e.g. EU MDR 2017/745, US FDA regulations), with a documented intended use covering indication, user profile, use environment, and operating principle, to ensure the correct conformity-assessment route is applied before the product is placed on the market. | DC_10 |
| RE_02 | The Notified Body wants the software to be developed under a documented software lifecycle process compliant with IEC 62304 at the safety classification justified by its hazard analysis — including a documented rationale for any classification mitigation through independent risk-control systems — to ensure the rigour of development, verification, and maintenance activities matches the harm failing software could cause, up to death of the patient. | DC_07, DC_10 |
| RE_03 | The Competent Authority wants a risk management process compliant with ISO 14971 applied across the entire product lifecycle, with all hazards — including wrong or delayed diagnosis, undetected sensor misplacement, missed alarms, and undetected connection loss — identified, evaluated, controlled, and the residual risk judged acceptable against the state of the art, to ensure patient safety is demonstrably managed before and after market access. | DC_11 |
| RE_04 | The Notified Body wants a usability engineering process compliant with IEC 62366-1 applied to all safety-related user interactions, with use-related hazards such as clinician misinterpretation of AI diagnostic output analysed and validated through summative evaluation with representative trained medical professionals in representative use environments, to ensure use errors that could lead to patient harm are controlled before market access. | DC_11 |
| RE_05 | The Competent Authority wants clinical evaluation evidence demonstrating that any AI-based diagnostic function achieves its claimed clinical performance, benefit, and safety for the intended patient population — including validation evidence for any third-party AI model incorporated into the device — to ensure diagnostic candidates presented to clinicians rest on scientifically valid evidence rather than manufacturer claims. | DC_11 |
| RE_06 | The Competent Authority wants AI-based functions to comply with applicable AI-specific legal requirements (e.g. the EU AI Act obligations for high-risk AI systems), including transparency to users, human oversight, data governance, and documented performance characteristics and limitations, to ensure clinicians retain informed control over AI-supported diagnostic decisions. | DC_11 |
| RE_07 | The Notified Body wants physiological alarm functions to conform to the applicable alarm-system standards (e.g. IEC 60601-1-8), including alarm prioritisation, latency, and clear indication of alarm conditions and technical faults, to ensure clinicians are reliably and consistently alerted to patient deterioration and equipment failure. | DC_04 |
| RE_08 | The Competent Authority wants secure product lifecycle processes and cybersecurity risk management applied in accordance with applicable requirements and standards (e.g. IEC 81001-5-1, MDR GSPR cybersecurity requirements, FDA premarket cybersecurity guidance), to ensure networked medical software connected to clinical information systems cannot be compromised in ways that endanger patients or expose health data. | DC_13 |
| RE_09 | The Surveillance Authority wants patient health data processed by the device to be protected in compliance with applicable data-protection law (e.g. GDPR, HIPAA), including lawful basis, data minimisation, and security of data shared with external health information systems, to ensure patients' fundamental rights are preserved when clinical data leaves the point of care. | DC_13 |
| RE_10 | The Notified Body wants data exchange with hospital information systems to use recognised health-informatics interoperability standards (e.g. HL7, FHIR) with documented interface specifications, to ensure clinical data shared for second opinions is complete, correctly interpreted, and traceable across the care chain. | DC_08 |
| RE_11 | The Notified Body wants a complete technical documentation file — including software requirements, architecture, verification evidence with traceability from requirements through test results, risk management file, usability engineering file, and clinical evaluation report — maintained and available for conformity assessment and unannounced audit, to enable an independent judgement that the device meets all general safety and performance requirements. | DC_14 |
| RE_12 | The Competent Authority wants the device to carry compliant labelling, unique device identification, and instructions for use that state the intended use, residual risks, performance limitations of the AI diagnostic function, and required user training, to ensure market-access marking is truthful and users are informed of the conditions for safe use. | DC_14 |
| RE_13 | The Competent Authority wants evidence that users receive and complete the training defined as a risk-control measure — including training on interpreting AI diagnostic output and on device limitations — before clinical use, to ensure risk controls that depend on user competence are actually effective in the field. | DC_09 |
| RE_14 | The Surveillance Authority wants a post-market surveillance system with vigilance reporting of serious incidents and field safety corrective actions within the legally mandated timelines, periodic safety update reporting, and continuous monitoring of the AI function's real-world diagnostic performance for degradation or drift, to ensure emerging risks are detected and corrected while the device is on the market. | DC_14 |
| RE_15 | The Notified Body wants all post-market software modifications — including updates to or replacement of any incorporated AI model — evaluated through a documented change-control process that determines whether the change is significant and requires new conformity assessment or regulatory submission before deployment, to ensure the device on the market always corresponds to the device that was approved. | DC_14 |

### Ideal Product Model (KA_*)

The Ideal Product Model is the blueprint that aligns stakeholder expectations with product capabilities — the key proposition attributes, their priority, feasibility, and risk.

| ID | Benefit Driver | Expectation | Proposition Attributes | Superior to | Priority | Feasible | Risk | Rationale |
|----|----------------|-------------|------------------------|-------------|----------|----------|------|-----------|
| KA_01 | Complete patient picture at a glance | UE_01, UE_11, ME_04, ME_07, BE_08 | Continuous, non-invasive acquisition of the standard vital-sign modalities in clinical use (ECG, oxygen saturation, blood pressure, temperature, capnography, EEG) from a bounded, fixed set of standard device types over published standard device interfaces, unified into one real-time display within a one-second end-to-end measurement-to-display latency budget | Fragmented single-parameter monitors that force clinicians to mentally correlate separate displays | Must | Yes | Low | Acquisition and display of standard modalities is mature practice; a fixed, bounded device set over published interfaces makes integration effort predictable and keeps the legal manufacturer's liability boundary clean — measurement accuracy remains with the source devices, while fidelity of the unified display is ours to verify and stand behind. The bounded set also caps service, training, and complaint-handling scope, but obliges supplier-monitoring agreements so third-party interface changes or obsolescence cannot silently invalidate the integration; residual platform-headroom uncertainty is carried and mitigated under KA_10 |
| KA_02 | Diagnostic direction inside the golden hour | UE_02, UE_03, ME_03, BE_15 | Ranked diagnostic decision support derived from the live vital-sign picture, converging to candidate directions within a bounded time on the order of two minutes — a budget owned by the diagnostic capability itself, not the measurement-and-display chain — presented alongside, never instead of, the raw measurements | Monitoring practice that leaves all diagnostic synthesis to the clinician under time pressure with no machine assistance | Must | Partly | High | Allocating the convergence budget to the diagnostic capability keeps the timing claim architecturally clean, and constraining the first release to a commercially validated, pre-existing diagnostic model class contains algorithm-development risk; what remains unproven is clinical-grade performance under emergency conditions — highest-value and highest-novelty attribute. The business must treat the two-minute figure as a verifiable labelled claim, not a marketing aspiration: it enters the instructions for use with its limitations stated, and the organisation must be prepared to defend it in incident and liability proceedings, so the claim is frozen only once evidence supports it |
| KA_03 | Trustworthy, clinician-subordinate interpretation | UE_14, ME_10, BE_04, RE_06 | Unambiguous, always-visible distinction between measured values and machine interpretation; guidance framed as ranked candidates supporting — never replacing or automating — clinical judgement, with transparency and human-oversight provisions meeting applicable AI legislation | Opaque scoring or advisory functions whose basis and status relative to measurements is unclear to the clinician | Must | Yes | Medium | Presentation and oversight design is feasible with established usability methods and adds no material technical load; the residual risk is regulatory interpretation of AI-transparency obligations, mitigated by early authority engagement. For the legal manufacturer this attribute is also the primary liability defence against foreseeable-misuse claims — the documented measured-versus-interpreted distinction and oversight rationale must be captured in the usability and risk files so it survives audit, not just implemented on screen |
| KA_04 | Clinically proven AI performance | ME_09, BE_03, RE_05 | Diagnostic algorithms built from commercially validated, clinically evidenced pre-existing components for the first release, with clinical evaluation of overall performance including independent third-party validation of the models before market release | Unvalidated or research-grade algorithms whose real-world diagnostic performance is undocumented | Must | Partly | High | Constraining the first release to a commercially validated off-the-shelf model class shifts effort from model development to integration verification and in-context clinical evaluation; integrated performance evidence in the intended emergency context still has to be generated and remains the longest-lead-time evidence item. Sourcing does not transfer responsibility: the legal manufacturer answers for the model's performance in full, so supply contracts must secure access to the supplier's validation evidence, change notification before any model update, and continuity provisions (e.g. escrow-class arrangements) against supplier failure or discontinuation |
| KA_05 | Immediate awareness of patient deterioration | UE_05, ME_07, RE_07 | Clinical alarming that annunciates any abnormal vital sign immediately, within the one-second end-to-end latency budget, conforming to the medical alarm-system standard (IEC 60601-1-8) | Alarm behaviour with perceptible delay or non-standard alarm semantics unfamiliar to clinical staff | Must | Yes | Low | Standards-conformant alarming on continuously acquired signals is well-understood engineering; the latency budget is demanding but fits the end-to-end display budget, and independent audible annunciation already present at the measurement sources provides a backstop that strengthens the safety case. Alarm behaviour is historically the dominant post-market complaint and vigilance category for monitoring products, so alarm events must be logged in a form the complaint-handling and vigilance processes can act on from day one |
| KA_06 | No silent failures | UE_06, UE_07, UE_08, BE_06 | Reliable detection and annunciation of technical fault conditions: misplaced or unreliable sensors, a measurement source that stops delivering, loss of connection, and an explicit notice whenever diagnostic guidance cannot be delivered within its promised time | Monitoring behaviour where a failed or misplaced sensor simply shows flat, stale, or plausible-but-wrong values without warning | Must | Yes | Medium | Fault detection heuristics per modality are established; the guidance-timeout notice is emitted by the diagnostic capability itself on an independent path, making it straightforward to realise — the residual risk is completeness of the fault-condition catalogue. That catalogue is a living risk-management-file artefact, not a one-off design input: post-market complaint and field data must feed back into it, so the surveillance process owns its upkeep across the product's life |
| KA_07 | Safety functions that survive failures | UE_15, ME_08, BE_02 | Independent mitigations for the safety-critical alarm and diagnosis functions, so that critical alarming keeps operating when other functions fail, and safety claims do not rest on a single point of failure — supporting a justified, reduced software safety classification | Monolithic designs where one software failure can silence alarms and guidance simultaneously, forcing the most onerous safety classification | Must | Yes | Medium | The independence claim is grounded in mechanisms that already exist — the measurement sources annunciate audibly on their own, and the diagnostic capability self-reports when guidance times out — so feasibility does not rest on new development; risk lies in convincing the authority that this mitigation rationale justifies the classification, addressed by early engagement. The classification argument carries the business case: if it fails, development cost and timeline escalate materially, so the rationale must be written as a formal, evidence-linked justification in the technical file — and the classification decision revisited whenever the mitigations change |
| KA_08 | Ready when the patient arrives | UE_04, UE_10, ME_06 | Operational readiness within seconds of power-on and near-zero operating burden: the clinician's attention stays on the patient, not the equipment | Equipment with boot, configuration, or interaction sequences that consume clinician attention during the critical first minutes | Must | Yes | Low | Rapid start-up is a native strength of real-time-capable embedded platform classes, and minimal-interaction operation is a proven capability class; primarily a usability-engineering discipline rather than a technical unknown. Near-zero operating burden also pays organisationally: it shrinks the training curriculum, lowers the customer-support call volume, and reduces the use-error surface the risk file must cover |
| KA_09 | One capability everywhere the patient goes | UE_09, ME_12 | A single, portable solution usable unchanged across ICU, emergency room, ambulance/vehicle, and at-scene settings | Setting-specific products that differ between hospital and mobile use, forcing retraining and data discontinuity at handover points | Must | Yes | Medium | Cross-setting uniformity is feasible because the solution runs unchanged on the fleet already deployed across those settings, and a single variant keeps production, verification, service, and documentation scope to one configuration — a direct manufacturability and support win. Environmental robustness of mobile use and network availability outside the hospital need early confirmation, and the ambulance/at-scene claim may pull additional environmental and transport-use requirements into the intended-use scope; that scope decision must be made deliberately before design freeze, since each added setting widens the evidence and liability envelope |
| KA_10 | Value from the installed base | ME_02, ME_15, BE_07, BE_13 | Delivery as software only, running on the customer's existing, unchanged equipment fleet, with real-time performance confirmed against that fixed platform early in development, and a predictable total cost of ownership with no new hardware investment | Offerings that require purchasing, deploying, and maintaining new dedicated hardware | Must | Partly | High | Software-only on a fixed existing platform is a strong economic proposition, and the platform's real-time capabilities give the determinism the latency budgets require; the fixed compute envelope offers no headroom escape, however, so whether the tight internal processing budgets fit is the key technical unknown — hence early performance confirmation on the actual platform, gated before major investment is committed. Because the legal manufacturer does not own the hardware baseline, the declared platform envelope (hardware revision, system-software versions, configuration) must be explicitly bounded in the technical file and customer contracts — our conformity claim holds only within it, and fleet drift outside it must be detectable and contractually excluded |
| KA_11 | Seamless hospital information exchange | UE_12, ME_05, BE_09, RE_10 | Live exchange of patient data with receiving-hospital information systems using recognised health-informatics interoperability standards (e.g. HL7/FHIR class) | Handover practice based on verbal reports and paper, or on proprietary interfaces requiring per-hospital custom integration | Should | Yes | High | The interoperability standard class is well-trodden, but the specific protocol choice and interface definitions are still open — an acknowledged high-probability, high-impact integration risk; contained by selecting the protocol and fixing interface definitions early and committing to the standard rather than custom links. Commercially this is a strong purchase criterion, but per-hospital custom integration would overwhelm support capacity, so the standard-only commitment is also a supportability boundary the sales organisation must not contract around; the Should priority stands only if the traced regulatory expectation (RE_10) permits phased delivery — confirm that reading with the authority before relying on it |
| KA_12 | Competence without patient risk | UE_13, ME_11, BE_05, RE_13 | Realistic, risk-free simulation-based training on the solution itself, mandatory before clinical use, with evidenced completion of training for every user | Training via manuals, classroom sessions, or first use on live patients, with no objective evidence of user competence | Must | Yes | Low | Simulation on the same software that runs clinically is inherently realistic and reuses the operational platform rather than requiring a separate training environment; evidencing completion is an established training-management capability. The "mandatory before clinical use" condition, however, is enforced inside customer organisations, not by us — so it must be anchored in the instructions for use and customer contracts, with completion records retained, because those records are the manufacturer's evidence in any use-error liability dispute |
| KA_13 | Assured market access | ME_01, ME_13, BE_01, BE_11, RE_01, RE_02 | Qualification as a medical device with a documented intended use, development under the medical-device software lifecycle standard (IEC 62304) at a justified safety classification including the mitigation rationale, and early engagement with the competent authority to secure clearance in the target market | Development approaches that defer regulatory strategy until late, risking rework, reclassification, or denied market access | Must | Yes | Medium | The regulatory pathway for AI-supported monitoring software exists and is achievable; the independent-mitigation architecture gives the classification argument technical substance, and residual risk is authority interpretation of the AI decision-support claims, mitigated by engaging early. Early engagement is also the cheapest insurance the business case has — an adverse late ruling on qualification or classification would strand the development investment — so authority interaction must be budgeted, scheduled before design freeze, and its outcomes minuted as governed decisions in the technical file |
| KA_14 | Demonstrated safety and usability | BE_12, RE_03, RE_04 | Lifecycle risk management per ISO 14971 and usability engineering per IEC 62366-1 including summative evaluation, with the highest-risk aspects prototyped and examined early rather than at the end | Compliance-on-paper approaches where risk and usability evidence is assembled retrospectively after design freeze | Must | Yes | Low | Both standards are established practice; early prototyping should target the identified highest-risk aspects — real-time integration performance and hospital-system connectivity — converting the main unknowns into evidence before they can derail the design. Front-loading this spend is a deliberate finance decision: it moves cost earlier but caps the write-off exposure, and it keeps the risk and usability files audit-ready as living documents rather than a retrospective assembly exercise the organisation cannot defend |
| KA_15 | Protected patients, protected data | RE_08, RE_09 | Cybersecurity engineered to the applicable medical-device security standards and personal-data protection compliant with the applicable data-protection legislation (e.g. GDPR/HIPAA) across all settings, including mobile and inter-facility data exchange | Solutions treating security and privacy as deployment-site responsibilities rather than built-in product properties | Must | Yes | Medium | Security and privacy engineering practices are mature; the mobile, multi-network usage context and the still-undefined hospital-exchange interfaces widen the attack surface and demand disciplined threat analysis before those interfaces are frozen. The organisation must also recognise that security is a committed lifecycle cost, not a design-phase deliverable: vulnerability monitoring, coordinated disclosure handling, and timely security patching through the controlled update path have to be staffed and funded for the full support life declared under KA_17 |
| KA_16 | Provable, reconstructable behaviour | BE_10, BE_14, RE_11, RE_12 | Design control producing a complete, traceable technical file; observability such that alarms, detected faults, and diagnostic outputs can be reconstructed after the fact; and compliant labelling, unique device identification, and instructions for use stating limitations and training prerequisites | Products whose behaviour in an incident cannot be reconstructed and whose documentation cannot withstand audit or liability scrutiny | Must | Yes | Low | Traceability, logging, and labelling are deterministic engineering disciplines; on-device logging must respect the constrained embedded storage and processing envelope, but the cost is effort, not uncertainty — and reconstructable behaviour is the manufacturer's first line of defence in incident investigation and product-liability proceedings. Log retention periods, extraction procedures, and the personal-data status of logged content must be governed decisions aligned with the data-protection obligations under KA_15, defined before release rather than improvised at the first incident |
| KA_17 | Dependable through life | ME_14, RE_14, RE_15 | Committed support, maintenance, and update service across the product's life, post-market surveillance including vigilance and monitoring of AI performance drift, and disciplined change control for every post-market modification | Ship-and-forget offerings without organised surveillance, drift monitoring, or controlled update paths | Must | Yes | Medium | Lifecycle processes are organisational commitments rather than technical unknowns; AI-drift monitoring is newer practice and — with the first release built on an externally sourced validated model — needs defined metrics, thresholds, and a controlled re-validation path for model updates from the outset. These commitments must be priced into the business case and staffed before launch, not promised and resourced later: the declared support period drives headcount, the supplier contract must guarantee model maintenance and update terms for that same period, and every post-market change routes through change control so the technical file, classification rationale, and clinical claims stay valid through life |
### Business 'Requirements' (BR_*)

Conceptual project inputs from all business stakeholders that apply across the whole product lifecycle (development, launch, manufacturing, deployment, operation & use, end of life).

| ID | Description | Rationale | Stakeholder | Importance | Traces |
|----|-------------|-----------|-------------|------------|--------|
| BR_01 | The solution shall be qualified as a medical device and hold the applicable market clearances/approvals in each target market before commercial launch in that market, with proof of clearance available to purchasing organisations at tender time. | Placing an unqualified diagnostic-support capability on the market is illegal and exposes the legal manufacturer to prohibition orders, recalls, and liability; buyers verify clearance as a first-pass tender gate and exclude bids that cannot evidence it. | Regulatory Affairs | High | KA_13 |
| BR_02 | Software development shall follow a recognised medical-device software lifecycle standard (IEC 62304 class), with the software safety classification formally justified before development commitment, including the rationale for any classification reduction based on demonstrably independent risk mitigations. | A justified, defensible classification bounds development and documentation effort while keeping the technical file audit-proof; an unjustified reduction is a rejection risk that surfaces late and expensively. | Regulatory Affairs | High | KA_13, KA_07 |
| BR_03 | Risk management shall be performed per ISO 14971 across the entire lifecycle, with mitigations for safety-critical functions such as alarming and diagnostic support demonstrated to be independent of the functions they protect. | Systematic risk management is a market-access precondition and the basis for defending the safety argument and the reduced software classification; non-independent mitigations invalidate that argument. | Quality Management | High | KA_14, KA_07 |
| BR_04 | Usability engineering shall be performed per IEC 62366-1, including a summative usability evaluation with representative users in each intended acute-care use environment before release. | Use-error in acute care is a dominant harm source; the use environments differ materially (fixed unit versus mobile/at-scene), so evidenced usability across all of them is required for approval, expected by clinical evaluation committees during selection, and limits liability. | Quality Management | High | KA_14 |
| BR_05 | Competent authorities and/or notified bodies shall be engaged early in development to confirm the qualification, classification, and clinical-evidence strategy before major design commitments are made. | Early alignment prevents late redesign, resubmission cost, and launch delay caused by divergent regulatory interpretation. | Regulatory Affairs | High | KA_13 |
| BR_06 | The highest-risk technical assumptions — that the committed real-time presentation and alarm timeliness budgets and the diagnostic-convergence time are achievable on the existing, unchanged target platform, and that hospital-information-system connectivity can be realised with the interface choice still open — shall be confirmed by prototype evidence before full development investment is committed. | These carry the largest feasibility risk: the target platform is fixed and cannot be resized to fit, and the connectivity approach is undecided; failing either late would invalidate the business case for the whole programme and the performance commitments made to customers. | R&D Management | High | KA_14, KA_10, KA_11 |
| BR_07 | The first release shall build on commercially available, clinically validated pre-existing decision-support components, integrated without modification of their validated behaviour, rather than on newly developed interpretive algorithms. | Reuse of validated components shortens time-to-market, reduces clinical-evidence burden, and de-risks the diagnostic claim in the eyes of clinical evaluation committees; modifying a validated component would void its validation and forfeit the benefit. | R&D Management | High | KA_04 |
| BR_08 | A clinical evaluation, including validation by an independent third party, shall be completed before release of the diagnostic-support capability, with the resulting clinical evidence available to purchasing organisations for tender evaluation. | Independent clinical evidence is required for approval and for clinical acceptance of interpretive output; hospital selection committees demand it before signing, and a bid without reviewable evidence loses to one with it. | Clinical Affairs | High | KA_04 |
| BR_09 | The solution shall be deliverable as software only onto the customers' existing, unchanged patient-monitoring installed base, operating within the processing, memory, and interface capacity that base already provides, with no hardware modification, no recertification of that base, and no clinical downtime beyond a planned software installation window. | A software-only proposition protects the customers' installed-base investment, unlocks that base as the sales channel, and avoids hardware logistics, field upgrades, and re-approval of existing devices; for buyers, avoided capital replacement and avoided ward downtime are decisive cost and continuity-of-care arguments, and the proposition only holds if the solution fits the fixed resource envelope of that base. | Product Management | High | KA_10 |
| BR_10 | Contracts with the platform and third-party component and device suppliers shall bind the supported platform envelope (hardware/OS versions, performance floor), the stability of published device and component interfaces with advance notification of changes, and component availability and support for the full committed customer service period. | Uncontrolled platform drift, silent interface changes on connected devices, or supplier withdrawal would invisibly invalidate performance and safety claims and break the multi-year service commitments customers contract for. | Vendor Management | High | KA_10, KA_17 |
| BR_11 | Physiological alarm behaviour shall conform to the applicable medical alarm-system standard (IEC 60601-1-8 class). | Alarm conformity is mandatory for market access, the accepted state of the art for alarm safety and alarm-fatigue control, and a standing conformity requirement in acute-care tender specifications. | Regulatory Affairs | High | KA_05 |
| BR_12 | The solution shall comply with applicable AI legislation, including transparency and human-oversight provisions, keeping interpreted output at all times visibly distinguishable from measured data and subordinate to clinician judgement. | AI-law compliance is a market-access condition in key regions, caps liability for interpretive output, and is increasingly a documented pass/fail criterion in hospital AI-procurement policies. | Legal Manufacturer | High | KA_03 |
| BR_13 | Cybersecurity shall be engineered and maintained per recognised medical-device security standards, with a committed vulnerability-management and security-update process, deliverable to fielded installations, for the whole marketed life, and with security documentation suitable for customer pre-purchase security risk assessments. | Connected clinical software is a mandated attack-surface concern; hospital IT security review is a gating step in every tender, and a lifecycle security commitment that can actually reach deployed units is required by regulators and hospital procurement alike. | IT Security Officer | High | KA_15 |
| BR_14 | Patient data shall be processed in compliance with applicable data-protection law (GDPR/HIPAA class) in every target market, with the corresponding data-processing terms contractually committed to the customer. | Data-protection breaches carry severe fines and are a hard exclusion criterion in hospital tenders; buyers will not sign without contractually binding data-processing terms. | Data Protection Officer | High | KA_15 |
| BR_15 | Development of the MMSS shall run under formal design control producing a complete, traceable technical file covering requirements, design, risk, verification, and release evidence. | Regulatory submission, audits, and post-market accountability require demonstrable design governance; a complete, traceable technical file is the precondition for market approval and for defending every released design decision. | Quality Management | High | KA_16 |
| BR_16 | The solution shall be delivered with compliant labelling, unique device identification, and instructions for use in the languages of each target market. | Labelling/UDI/IFU compliance is a legal placing-on-market condition, and missing local-language instructions for use is a hard exclusion criterion in public hospital tenders, not a post-award formality. | Regulatory Affairs | High | KA_16 |
| BR_17 | Mandatory simulation-based training on the solution itself, with evidenced completion per user and completion records made available to the customer organisation, shall be part of the deployment offering before clinical use, at a staff-time burden the buying organisation can roster without disrupting clinical operations. | Evidenced competence protects patients, satisfies usability-related regulatory expectations, and reduces support and liability exposure; hospitals additionally need the completion records for their own competency-compliance obligations, and an unaffordable training burden is a hidden cost that erodes the purchase case. | Training & Customer Support | High | KA_12 |
| BR_18 | A committed support, maintenance, and update service shall be offered for a defined multi-year support period from deployment, with response and resolution service levels contractually defined, measurable, and backed by remedies for non-achievement, all committed at tender time. | Hospitals purchase multi-year commitments with measurable, remedied service levels; an uncommitted or unquantified service model blocks tender participation, and service levels without remedies are treated by procurement as no commitment at all. | Customer Support | High | KA_17 |
| BR_19 | Post-market surveillance shall be operated for the marketed life, including monitoring of interpretive-algorithm performance against its validated baseline, feeding a formal change-control process that also governs model/algorithm updates, their re-validation, and advance notification of clinically relevant changes to customer organisations. | PMS is a legal obligation; drift monitoring against the validated baseline and controlled, re-validated updates keep the diagnostic claim valid after release, and hospitals require notice of clinically relevant changes to manage their own clinical governance. | Post-Market Surveillance | High | KA_17 |
| BR_20 | The commercial proposition shall be marketed as a single capability giving a complete real-time patient picture with timely diagnostic direction across ICU, ER, ambulance, and at-scene use, with any setting-dependent limitations (such as absence of hospital-network connectivity in mobile use) explicitly stated in the proposition before contract signature. | One consistent capability across all acute-care settings is the differentiating market claim against per-setting point solutions; an unqualified "identical everywhere" claim is technically indefensible where connectivity differs, would be exposed during customer acceptance, and undisclosed limitations discovered after signature poison the reference-customer relationships the market entry depends on. | Marketing & Product Management | Medium | KA_01, KA_02, KA_09 |
| BR_21 | The MMSS shall impose near-zero deployment and operating burden: monitoring shall be available within seconds of connection, routine operation shall require no dedicated operator effort, and the diagnostic stabilisation time shall be communicated to the user. | Hospitals will not adopt equipment that adds staffing load or workflow friction; immediate monitoring availability and a transparently communicated stabilisation time keep clinical workflow uninterrupted. | Hospital Procurement | High | KA_08 |
| BR_22 | The solution shall never fail silently: degraded, missing, or unreliable inputs and loss of interpretive guidance shall be actively annunciated to the clinical user at the point of care, promptly enough that clinical decisions are not based on stale or invalid information. | Undetected failure of a safety-relevant capability is the largest single liability exposure for the legal manufacturer and a walk-away finding in customer clinical risk assessments; annunciation that arrives after the decision is made offers no protection. | Legal Manufacturer | High | KA_06 |
| BR_23 | Exchange of data with hospital information systems shall use recognised healthcare interoperability standards (HL7/FHIR class), with the specific standard and interface specifications — a choice still open — agreed with reference customers and closed before major design commitments depend on them, and with the integration effort per customer site bounded and quantifiable at tender time. | Standards-based integration is a tender requirement and unbounded site-integration effort is a known deal-killer hospitals price into bid comparisons; the open protocol/interface choice is a flagged high-risk item whose late closure would force rework of everything built on it. | Hospital IT & Integration | High | KA_11 |
| BR_24 | An end-of-life process shall be defined covering controlled decommissioning, fulfilment of data-retention obligations, verified return or destruction of customer and patient data, and orderly customer transition at end of service, with these exit terms contractually committed at purchase. | Lifecycle obligations do not end at last sale; hospitals require contractual exit and data-return terms before signing to avoid vendor lock-in, and uncontrolled end of life creates data-protection and contractual liability. | Legal Manufacturer | Medium | KA_15, KA_16, KA_17 |
| BR_25 | The released MMSS shall make its runtime behaviour — including measured data, interpretive output, alarms, and user actions — observable and reconstructable within a governed log-retention policy. | Incident investigation, complaint handling, and liability defence depend on reconstructing what the device measured, concluded, and annunciated and what users did; a governed retention policy makes that evidence reliably available without unbounded storage. | Quality Management | High | KA_16 |
| BR_26 | The MMSS shall offer a predictable, fully disclosed total cost of ownership over its service life, with no unquantified cost lines for consumables, licences, maintenance, or updates. | Procurement decisions require complete cost transparency; hidden or unquantified cost lines block tender approval, distort budget planning, and erode buyer trust. | Hospital Procurement | High | KA_10 |
## Context (FORMAL)

The context level is the start of the solution domain (DHF), based on the problem domain and the stakeholder expectations.

### Intended Use (IU_01)

Write the intended use as a single, flowing prose statement that naturally covers the five aspects — what the product is, what it does (medical indication), who uses it (user profile), where it is used (use environment), and how it works (operating principle). Do **not** add bold labels or headers for the aspects; weave them into the sentences.

| ID | Description |
|----|-------------|
| IU_01 | The Mobile Monitoring Software Solution (MMSS) is medical device software that runs on a portable patient monitor and provides continuous vital-signs monitoring with real-time diagnostic decision support for critically ill patients. It is indicated for the continuous measurement and display of key vital signs and for adjunctive diagnostic support of critical conditions: it presents the measured vital signs together with ranked diagnostic candidates that converge within two minutes of the connected sensors delivering valid signals, and it generates clinical alarms for abnormal patient conditions and technical alarms for sensor faults; the diagnostic output supports, and does not replace, the clinical judgment of the treating professional. The software operates by acquiring physiological data from six non-invasive measurement devices — an ECG monitor, a pulse oximeter, a blood pressure monitor, a thermal probe, a capnometer, and an EEG monitor — through standardised interfaces, processing the data with an external, independently validated Artificial Intelligence analysis engine, displaying the results on the connected monitor display, and optionally transmitting data to hospital information systems for remote review and second opinion. The MMSS is intended to be used exclusively by trained medical professionals in critical care environments — intensive care units (ICU), emergency rooms, and mobile medical units — including time-critical and pre-hospital situations in which the patient is connected non-invasively and monitoring must be available immediately after connection. |

### Medical Device Classification (MD_01)

| ID | Description | Traces |
|----|-------------|--------|
| MD_01 | The MMSS is classified per IEC 62304 as software safety class C in its initial assessment, because a failure of its monitoring, alarming, or AI-based diagnostic functions could result in the death or serious deterioration of the health of a critically ill patient. After risk mitigation, the software is assessed as software safety class B, because both safety-critical functions are mitigated to systems independent of the MMSS software: (1) alarming — each of the six measurement devices generates its own independent audible alarm, so annunciation of an abnormal patient condition does not depend on the MMSS; and (2) diagnosis — the external AI diagnostic engine independently issues an audible notification when diagnosis has not converged within its two-minute budget, so a silent diagnostic failure cannot go unannounced. With these independent mitigations in place, a failure of the MMSS software alone can no longer directly result in death or serious injury. | IU_01 |

### Context Diagram

The context diagram identifies the system of interest in relation to its context. The system of interest contains all elements that are part of the design.

_To be added_

#### Product Information

The Mobile Monitoring Software Solution (MMSS) is medical device software that runs on a portable patient monitor and provides continuous vital-signs monitoring for critically ill patients. It acquires physiological parameters and signals from six connected measurement devices (ECG monitor, pulse oximeter, blood pressure monitor, thermal probe, capnometer, and EEG monitor), presents them on the monitor display, and generates clinical alarms for abnormal patient conditions and technical alarms for sensor faults. The MMSS delegates diagnostic interpretation to a commercially validated off-the-shelf AI diagnostic engine, which returns real-time ranked diagnostic candidates that converge within two minutes of the connected sensors delivering valid signals, giving trained medical professionals real-time decision support. Optionally, the MMSS transmits monitoring data to a hospital information system for second opinion. The software executes on a compact embedded CPU platform with a real-time operating system and is used exclusively by trained medical professionals in ICU, emergency room, and mobile medical unit environments. This document treats the MMSS as a black box at its external boundary; internal software decomposition is out of scope.

#### System of Interest

The part of the broader system this document is about — the product, subsystem, or component you are responsible for designing.

| System Element | Description |
|----------------|-------------|
| Mobile Monitoring Software Solution (MMSS) | The complete software application of the portable patient monitor, treated as a single black box. It acquires vital-sign parameters and signals from the connected measurement devices, presents monitoring data on the display, exchanges data with the AI diagnostic engine for ranked diagnostic candidates, raises clinical and technical alarms, and optionally transmits data to the hospital information system. |

#### Context Elements

Essential elements for your product that are not part of the design.

| Context Element | Description |
|-----------------|-------------|
| Host CPU platform | Compact embedded CPU platform with a real-time operating system on which the MMSS executes; provides computing resources, device connectivity, and OS services. Hardware and OS are not part of the MMSS design. |
| ECG monitor | Measurement device providing heart rate and the ECG waveform of the patient. |
| Pulse oximeter | Measurement device providing peripheral oxygen saturation (SpO2) and pulse rate of the patient. |
| Blood pressure monitor | Measurement device providing systolic, diastolic, and mean arterial blood pressure of the patient. |
| Thermal probe | Measurement device providing the patient's body temperature. |
| Capnometer | Measurement device providing end-tidal CO2 (etCO2) and respiration rate of the patient. |
| EEG monitor | Measurement device providing the EEG waveform and derived cerebral activity indices of the patient. |
| Monitor display | Display unit of the portable patient monitor on which the MMSS presents vital signs, waveforms, diagnostic candidates, and alarm annunciations to the medical professional. |
| AI diagnostic engine | Commercially validated off-the-shelf AI analysis engine/library that receives monitoring data from the MMSS and returns ranked diagnostic candidates; it independently issues an audible notification when its 2-minute convergence timeout expires. |
| Hospital information system (HIS) | External hospital system that optionally receives monitoring data from the MMSS for second opinion; communication standard (HL7/FHIR) is to be defined. |
| Patient | The critically ill person being monitored; the measurement subject from whom all physiological parameters and signals originate via the measurement devices. |

#### External Interfaces (IF_*)

Connections between the system of interest and the context elements (mechanical, chemical, electronic, digital, logical, etc.).

| ID | Name | Port 1 | Port 2 | ICD |
|----|------|--------|--------|-----|
| IF_01 | ECG data interface | MMSS | ECG monitor | ICD-ECG-001 (ECG Monitor Interface Control Document) |
| IF_02 | SpO2 data interface | MMSS | Pulse oximeter | ICD-SPO2-001 (Pulse Oximeter Interface Control Document) |
| IF_03 | Blood pressure data interface | MMSS | Blood pressure monitor | ICD-NIBP-001 (Blood Pressure Monitor Interface Control Document) |
| IF_04 | Temperature data interface | MMSS | Thermal probe | ICD-TEMP-001 (Thermal Probe Interface Control Document) |
| IF_05 | Capnometry data interface | MMSS | Capnometer | ICD-CO2-001 (Capnometer Interface Control Document) |
| IF_06 | EEG data interface | MMSS | EEG monitor | ICD-EEG-001 (EEG Monitor Interface Control Document) |
| IF_07 | Display presentation interface | MMSS | Monitor display | ICD-DISP-001 (Monitor Display Interface Control Document) |
| IF_08 | AI diagnostic engine interface | MMSS | AI diagnostic engine | ICD-AIE-001 (AI Diagnostic Engine API/Library Interface Control Document) |
| IF_09 | HIS communication interface | MMSS | Hospital information system (HIS) | ICD-HIS-001 — to be defined (HL7 or FHIR, TBD) |
| IF_10 | Host platform/OS services interface | MMSS | Host CPU platform | ICD-RTOS-001 (Real-Time OS and Platform Services Interface Control Document) |

#### Acquired Parameters / Signals

Whenever the product acquires, exchanges, or presents a **set** of parameters, signals, or data items from a set of source elements (measurement devices, sensors, sub-systems, services), enumerate that set here instead of leaving it as a collective phrase elsewhere. One row per source-element/parameter combination, taken from the input. If no such parameter set applies to this product, write `_Not applicable_`.

| Source Element | Parameter / Signal | Unit / Typical Range | Interface |
|----------------|--------------------|----------------------|-----------|
| ECG monitor | Heart rate | bpm, 30–250 | IF_01 |
| ECG monitor | ECG waveform | mV, continuous waveform | IF_01 |
| Pulse oximeter | SpO2 (peripheral oxygen saturation) | %, 70–100 | IF_02 |
| Pulse oximeter | Pulse rate | bpm, 30–250 | IF_02 |
| Blood pressure monitor | Systolic blood pressure | mmHg, 40–260 | IF_03 |
| Blood pressure monitor | Diastolic blood pressure | mmHg, 20–200 | IF_03 |
| Blood pressure monitor | Mean arterial pressure | mmHg, 30–220 | IF_03 |
| Thermal probe | Body temperature | °C, 30–43 | IF_04 |
| Capnometer | etCO2 (end-tidal CO2) | mmHg, 10–100 | IF_05 |
| Capnometer | Respiration rate | breaths/min, 4–60 | IF_05 |
| EEG monitor | EEG waveform | µV, continuous waveform | IF_06 |
| EEG monitor | Derived cerebral activity indices | dimensionless index | IF_06 |

Note: all vital-sign inputs are acquired at an input rate of at least 0.1 Hz, per the input specification.

## Users

### User Groups

Collections of users who share common characteristics (a synonym is User Role).

| User | User Group | User Profile |
|------|------------|--------------|
| ICU nurse / bedside critical-care nurse | Bedside Critical-Care Nurse | Trained, registered nurse working at the bedside in an intensive care unit for prolonged shifts, typically supervising several monitored patients simultaneously. Skilled in sensor application, continuous vital-signs surveillance, and first-line alarm response. Key needs: at-a-glance readability of vitals, unambiguous separation of clinical alarms from technical/sensor-fault alarms, low alarm fatigue, and diagnostic candidates that are clearly adjunctive to their own assessment. |
| Intensivist / ICU physician | Intensivist | Licensed physician specialised in intensive-care medicine, responsible for diagnostic and therapeutic decisions on critically ill patients. Uses trends and the ranked diagnostic candidates as a second perspective on complex, evolving conditions and tailors alarm limits to individual patients. Key needs: interpretable, visibly subordinate AI output, patient-specific alarm configuration within safe bounds, and reconstructable event history for case and incident review. |
| Emergency physician | Emergency Physician | Licensed physician making time-critical decisions on undifferentiated, acutely ill patients in the emergency room, under time pressure and frequent interruption. Relies on fast availability of vitals and early ranked diagnostic candidates to accelerate triage, and on HIS sharing for a second opinion. Key needs: monitoring within seconds of connection, candidate convergence within the stated two minutes, and an explicit notice when diagnosis does not converge. |
| ER nurse | Emergency-Room Nurse | Trained, registered nurse in the emergency department who connects patients to the monitor during intake, watches multiple bays, and hands patients over between care areas. Encounters the device across different physical setups and patient turnover far higher than in the ICU. Key needs: identical operation to the ICU/mobile configuration, minimal setup interaction, secure handling of patient data during handovers, and locally understandable instructions. |
| Paramedic / pre-hospital professional | Pre-hospital Professional | Trained paramedic operating in a mobile medical unit — moving vehicle, noise, vibration, variable lighting, small crew, no expert backup. Applies sensors rapidly on scene and monitors the patient en route to definitive care. Key needs: near-zero-interaction start-up, glanceable display and loud, distinct alarms under transport conditions, and dependable annunciation of sensor misplacement or disconnection while attention is divided. |
| Biomedical / clinical engineer | Biomedical / Clinical Engineer | Trained hospital technician responsible for deploying the software onto the existing monitor fleet, keeping it current, and maintaining it through its service life. Works in commissioning and maintenance contexts, not at the live bedside. Key needs: installation without hardware change or performance degradation, transparent version/update status, updates that never interrupt active monitoring, and access to logs supporting service and incident investigation. |
| Clinical educator | Clinical Educator | Registered clinical professional (e.g. senior nurse or resuscitation officer) who delivers the organisation's mandatory simulation-based training sessions directly on the device and maintains the competency files. Configures and runs training in simulation mode, injects clinical scenarios during sessions, and afterwards retrieves evidenced per-user training-completion records for the organisation's competency files. Needs unmistakable on-device simulation marking, flexible scenario injection, and reliable per-user completion evidence retrievable without specialist IT support. |
### User Requirements / Needs (UR_*)

The user expectations translated over the product context into requirements specific to YOUR product. They are SMARTER than the expectations and form the base for product validation. Format: *As a \<user group\> I want \<feature\> so that \<benefit\>.*

| ID | Description | Classification | Traces |
|----|-------------|----------------|--------|
| UR_01 | As a bedside critical-care nurse I want the monitor to continuously and simultaneously display the current values of all parameters enumerated in the Acquired Parameters / Signals table (Context section) in real time, without requiring any user interaction to bring a parameter into view, so that I can assess my patient's condition at a glance — including from the foot of the bed during rounds — throughout the shift. | High | IU_01 |
| UR_02 | As an emergency physician I want the system to present a ranked list of diagnostic candidates alongside — and never obscuring — the live vital signs so that I have an early second perspective that accelerates my differential diagnosis without interrupting my view of the patient's current state. | High | IU_01, BR_12 |
| UR_03 | As an intensivist I want every AI-derived diagnostic candidate to be visibly distinguishable from measured values and explicitly marked as adjunctive everywhere it appears — on screen, in logs, and in transmitted data — so that neither I nor my team, nor a remote colleague reading the shared data, can mistake interpreted output for a measurement or a confirmed diagnosis. | High | BR_12, IU_01 |
| UR_04 | As a pre-hospital professional I want live values for each parameter to appear within seconds of powering on the monitor and connecting that parameter's sensor — without waiting for the remaining sensors to be attached — so that no clinically relevant time is lost at the scene or during transport while sensors are applied one by one. | High | BR_21, IU_01 |
| UR_05 | As an emergency physician I want the ranked diagnostic candidates to converge within 2 minutes of the connected sensors delivering valid signals so that the diagnostic support arrives while it can still influence my time-critical decisions. | High | IU_01 |
| UR_06 | As an emergency physician I want the system to distinguish "still converging" from "cannot converge", and to give a clear notice as soon as it determines that diagnostic candidates will not converge within the expected time, so that I proceed on clinical judgment alone instead of waiting for output that will not come. | High | IU_01, BR_22 |
| UR_07 | As a bedside critical-care nurse I want physiological alarms with prioritised visual and audible annunciation conforming to the medical alarm-system standard, with priorities distinguishable by sound alone, so that I recognise and react to the most urgent patient condition first — even when the monitor is out of my line of sight — without alarm fatigue. | High | BR_11, IU_01 |
| UR_08 | As an intensivist I want to adjust clinical alarm limits to the individual patient within safe, bounded ranges, with the currently active limits and any deviation from defaults visible at a glance, so that alarming reflects the patient's actual clinical state instead of generating false alarms — and the next shift can see how alarming has been tailored. | High | BR_11 |
| UR_09 | As a bedside critical-care nurse I want distinct technical alarms for sensor misplacement, sensor disconnection, and stale or frozen data that identify the affected sensor or parameter so that I never confuse a measurement problem with a change in the patient's condition and can correct the right sensor immediately. | High | BR_22, IU_01 |
| UR_10 | As a bedside critical-care nurse I want the system to promptly annunciate any internal failure of monitoring or diagnostic functions and to indicate which functions remain reliable so that it never fails silently while I believe the patient is being monitored, and I know what I can still trust. | High | BR_22 |
| UR_11 | As a pre-hospital professional I want monitoring and diagnostic support to start automatically with safe default settings as soon as the sensors are connected to the patient, requiring no menu navigation or configuration, so that my hands and attention stay on the patient rather than on the device. | High | BR_21 |
| UR_12 | As an emergency-room nurse I want the system to look, alarm, and operate identically in the ICU, ER, and mobile medical unit, with any setting-specific limitations stated on the device itself, so that patient handovers between care areas require no relearning and no guesswork about capability. | Medium | BR_20 |
| UR_13 | As a pre-hospital professional I want the display to remain readable in direct sunlight, darkness, and vehicle vibration, and the alarms clearly audible above engine, siren, and traffic noise, so that I do not miss a deterioration while the vehicle is moving. | High | IU_01 |
| UR_14 | As an emergency physician I want to transmit the current and recent monitored parameters together with the ranked diagnostic candidates to the hospital information system via the standard healthcare interfaces so that a remote specialist can review the same picture I am seeing and give a second opinion on my working diagnosis. | High | BR_23, IU_01 |
| UR_15 | As a bedside critical-care nurse I want a simulation training mode that replays realistic patient scenarios on the same device and interface used in live care, is unmistakably marked as simulation at all times while active, and cannot affect a real patient so that I can practise interpreting alarms and diagnostic candidates safely before live use. | High | BR_17 |
| UR_16 | As an emergency-room nurse I want my completed simulation training sessions to be recorded per user, scenario, and completion date — retrievable by the clinical educator for the organisation's competency files — so that my qualification to operate the system is demonstrable to my employer and auditors. | High | BR_17 |
| UR_17 | As an intensivist I want the system to log measurements, alarms, diagnostic outputs, and user actions with accurate, consistent timestamps so that the sequence of events around a clinical incident can be fully and unambiguously reconstructed afterwards. | High | BR_25 |
| UR_18 | As an emergency-room nurse I want patient data on the device and in transmission to be protected against unauthorised access without delaying an authorised clinician's access to the patient's data in an emergency so that using the system never exposes my patients' data, breaches data-protection obligations, or slows urgent care. | High | BR_14, BR_13 |
| UR_19 | As a biomedical / clinical engineer I want security and software updates to be announced, versioned, and installable without interrupting active patient monitoring — and never to start automatically while a patient is connected — so that the fleet stays current and secure without clinical disruption. | High | BR_13, BR_18 |
| UR_20 | As a biomedical / clinical engineer I want the software to install on our existing portable patient monitors without hardware changes and without degrading the monitor's existing measurement or alarm performance so that deployment across the fleet is fast and does not compromise established monitoring functions. | High | BR_09 |
| UR_21 | As an emergency-room nurse I want instructions for use and on-device guidance available in my local language so that I can operate the system correctly and resolve routine questions at the bedside without external help. | High | BR_16 |
### User DFMEA (USER_DFMEA_*)

A structured analysis of how users might misuse, misinterpret, or fail to operate the product, the consequences, and the mitigations the design must include.

| ID | Item/Function | Requirement | Failure Mode | End-effect | Rationale | Failure Cause | Severity | Prevention | Classification | Traces |
|----|---------------|-------------|--------------|------------|-----------|---------------|----------|------------|----------------|--------|
| USER_DFMEA_01 | Sensor application | UR_04 (per-sensor live values) | User attaches a sensor to the wrong body site; it still produces plausible-looking values | Physiologically wrong parameters feed the display and the AI, leading to a wrong diagnostic candidate and wrong treatment | A misplaced sensor is a known input risk explicitly flagged for MMSS; plausible values give the user no visual cue of error | Time pressure during emergency hook-up; sensors physically fit multiple sites; identical connectors across sensor types; poor lighting and restricted patient access in transport | Critical | Per-sensor signal-plausibility checking with a technical alarm naming the suspect sensor; on-screen sensor placement confirmation with pictograms at connection | High | UR_04, UR_09 |
| USER_DFMEA_02 | AI diagnostic candidates | UR_03 (AI marked adjunctive) | Clinician treats the top-ranked AI candidate as a confirmed diagnosis and skips independent clinical assessment | Treatment initiated for the wrong condition; actual condition progresses untreated | Over-reliance on automation (automation bias) is a documented input risk and grows with routine use | Persuasive ranked presentation; habituation; high workload favouring cognitive shortcuts; night-shift fatigue; junior or agency staff deferring to the system over their own assessment | Critical | Persistent "adjunctive — clinical judgement required" marking on every AI surface; visual style clearly distinct from measured vitals; ranking shown with uncertainty indication | High | UR_02, UR_03 |
| USER_DFMEA_03 | AI candidate list vs vitals | UR_02 (candidates never obscure vitals) | User focuses attention on the diagnostic panel and misses a deteriorating live parameter | Delayed response to deterioration visible in the vitals the user stopped scanning | Attention tunnelling onto the novel AI feature diverts scanning from primary vitals | Salient, dynamic AI panel competing with static waveforms for attention; single clinician covering multiple patients with intermittent glances at the screen | Critical | Fixed layout in which all vitals remain simultaneously visible; deterioration escalated by alarms independent of where the user is looking | High | UR_01, UR_02, UR_07 |
| USER_DFMEA_04 | Diagnosis convergence status | UR_06 (converging vs cannot converge) | User misreads "still converging" as "no diagnosis available" (or vice versa) and stops waiting or waits indefinitely | Treatment delayed while user waits past the 2-minute window, or user abandons a result that was seconds away | Diagnosis timeout not being communicated is a named input risk causing treatment delay | Ambiguous or absent progress/timeout indication; interruption or handover mid-convergence so the returning or receiving clinician misjudges the state | Major | Explicit distinct states: progress indicator with elapsed/remaining time for converging; unmissable "cannot converge — reason" notice at timeout | High | UR_05, UR_06 |
| USER_DFMEA_05 | Alarm limit configuration | UR_08 (patient-specific limits) | User enters an alarm limit that is too wide (or transposes high/low) for this patient | Genuine deterioration never triggers an alarm; patient harm from unnoticed decline | Manual limit entry under stress is a classic use-error path with silent, latent effect | Numeric entry slips; limits from the previous patient carried over unreviewed; limits deliberately widened to quiet nuisance alarms and never restored at shift change; unit confusion | Critical | Limits constrained to clinically safe bounds with rejection of out-of-bound entries; high/low sanity cross-check; active limits permanently visible at the parameter; limits reset to safe defaults on new-patient admission | High | UR_08 |
| USER_DFMEA_06 | Alarm annunciation | UR_07 (prioritised alarms) | User silences or pauses alarms to reduce noise and forgets to re-enable them | Subsequent critical alarm never annunciates audibly; missed life-threatening event | Alarm fatigue drives routine silencing; a silenced state is easy to forget in transport handovers | Frequent low-priority alarms; no salient silenced-state reminder; night-shift culture of quieting devices near sleeping patients; silenced state not mentioned at shift handover | Critical | Time-limited silence with automatic reactivation; persistent visual silenced indicator; high-priority alarms exempt from or breaking through silence per IEC 60601-1-8 | High | UR_07 |
| USER_DFMEA_07 | Alarm priority discrimination | UR_07 (priorities by sound alone) | User misjudges a high-priority alarm as low priority while not viewing the screen | Delayed response to a critical physiological event during transport or turned-away care | In mobile settings the user often cannot see the display; sound is the only channel | Alarm tones insufficiently distinct; ambient noise masking (siren, engine, rotor); multiple devices alarming simultaneously in a shared bay | Critical | IEC 60601-1-8 compliant priority-distinct melodies and cadences; loudness validated against transport noise levels | High | UR_07, UR_13 |
| USER_DFMEA_08 | Technical alarms | UR_09 (sensor-specific technical alarms) | User dismisses a sensor-disconnection/misplacement alarm as a nuisance without fixing the sensor | Monitoring gap on that parameter; deterioration in the unmonitored channel goes undetected | Connection failure causing missed vitals is a named input risk; nuisance-alarm habituation makes dismissal likely | High technical-alarm frequency; alarm does not clearly identify the affected sensor or required action; motion artefact in transport teaches users that these alarms are usually false | Critical | Technical alarm names the exact sensor and fault type with corrective instruction; alarm persists or re-annunciates until the signal is restored | High | UR_09 |
| USER_DFMEA_09 | Data freshness | UR_09 (stale data detection) | User reads a frozen/stale value as a current measurement | Clinical decisions based on outdated physiology; deterioration since freeze is invisible | A static number is indistinguishable from a stable patient unless staleness is marked | Intermittent wireless sensor dropout without visible change to the displayed value; brief glances during multi-patient rounds leave no chance to notice a value has stopped updating | Critical | Stale values visually invalidated (greyed/crossed) with age indication and a technical alarm; never display an unmarked last-known value | High | UR_09, UR_01 |
| USER_DFMEA_10 | Degraded-mode awareness | UR_10 (internal failure annunciation) | After a partial internal failure, user continues to rely on functions that are no longer trustworthy | Decisions based on unreliable parameters or AI output from a degraded system | Users assume all-or-nothing failure; partial degradation is counter-intuitive without explicit guidance | Failure notice states the fault but not which functions remain reliable; notice acknowledged reflexively under workload and its content never read | Critical | Failure annunciation explicitly lists still-reliable vs unavailable functions; unreliable outputs suppressed rather than shown | High | UR_10 |
| USER_DFMEA_11 | Monitoring start-up | UR_11 (auto-start with safe defaults) | User connects sensors and walks away assuming monitoring and alarming are active when start-up did not complete | Patient effectively unmonitored while staff believe otherwise | Auto-start creates an expectation of zero verification; a silent start-up failure is invisible | Boot fault; sensor handshake failure; user skips confirmation glance under time pressure; simultaneous admissions pulling the clinician to the next patient before start-up completes | Critical | Positive, unambiguous "monitoring active / alarms active" indication per parameter; audible-visual fault annunciation if auto-start fails | High | UR_11 |
| USER_DFMEA_12 | Cross-environment operation | UR_12 (identical operation, stated limitations) | User in mobile transport assumes full ICU capability and relies on a function limited in that environment | Missing or degraded function (e.g. HIS sharing, sensor set) discovered only when needed, delaying care | Identical look-and-feel invites the assumption of identical capability | Environment-specific limitations not salient at the point of use; staff rotating between ICU and transport carry over expectations from the richer environment | Major | Current operating limitations stated on-device in the active context; identical alarm behaviour preserved across environments | High | UR_12 |
| USER_DFMEA_13 | Transport readability/audibility | UR_13 (readable and audible in transport) | User misreads a value or misses an alarm due to sunlight glare, vibration, or engine/siren noise | Wrong value acted on or critical alarm unnoticed during transport | Transport is a named use environment; ambient stressors directly attack the display and audio channels | Insufficient display luminance/contrast; alarm volume below ambient noise; vibration blur; brightness or volume manually turned down earlier and not restored | Critical | Display and alarm output specified and validated against transport ambient conditions; automatic brightness/volume floors that the user cannot set below minimum | High | UR_13 |
| USER_DFMEA_14 | HIS second-opinion sharing | UR_14 (transmit to HIS) | User shares parameters and candidates to the wrong patient record in the HIS | Second opinion rendered on the wrong patient's data, driving a wrong or delayed treatment decision; both patients' records contaminated | Wrong-patient selection under time pressure is one of the most persistent patient-safety error paths, and the remote clinician has no bedside cue to detect the mismatch | Similar patient names; stale patient context from a previous case; unidentified patients admitted under temporary aliases in emergency and transport settings | Critical | Mandatory patient-identity confirmation step showing identifiers before transmission; transmitted dataset labelled with source device and timestamp | High | UR_14 |
| USER_DFMEA_15 | Simulation mode | UR_15 (simulation unmistakably marked) | User mistakes simulated vitals/diagnoses for real patient data, or believes a real patient is monitored while the device is in simulation | Treatment decisions made on fictitious data, or real patient unmonitored during a training session | Simulation replicates the real UI by design; the only defence is unmistakable mode marking and hard separation | Simulation left active after training; marking too subtle; handover between users; training device pressed into clinical service during a surge | Critical | Permanent full-screen simulation banner and distinct colour scheme; simulation blocked or auto-terminated when a real sensor connects; no simulated data ever transmitted to HIS or logs as real | High | UR_15 |
| USER_DFMEA_16 | Training gating | UR_16 (training completion recorded) | Untrained user operates the device and misuses the AI and alarm functions | Use errors from all other rows made more likely; misinterpretation of adjunctive AI output | Trained professionals are the intended user profile; training records are the mechanism to keep that assumption true | Staff turnover; emergency staffing; float and agency staff during surges; no check of training status at use | Major | Training completion recorded per user, scenario, and date and retrievable for rostering; simulation mode provided as the safe practice path | Medium | UR_16 |
| USER_DFMEA_17 | Emergency access | UR_18 (data protection without delaying access) | User is locked out by authentication at the start of an emergency and cannot reach live vitals or start monitoring | Monitoring and diagnosis delayed during the most time-critical phase | Security controls sized for records access can fatally slow bedside use if applied to live monitoring | Forgotten credentials; shared-device session locked by another user; gloved or contaminated hands defeating touch or biometric entry | Critical | Live monitoring, display, and alarms never behind authentication; break-glass access to protected functions with automatic audit logging | High | UR_18, UR_17 |
| USER_DFMEA_18 | Software updates | UR_19 (no auto-update with patient connected) | User starts (or fails to defer) a software update while a patient is being monitored | Monitoring and alarming interrupted mid-care; missed events during restart | An update-induced monitoring gap is silent to the clinical team unless explicitly blocked | Update prompt accepted reflexively; user unaware a patient is still connected; update scheduled by biomedical engineering without bedside coordination | Critical | Update start hard-blocked while any sensor/patient connection is active; explicit confirmation that monitoring is not in use before installation proceeds | High | UR_19, UR_20 |
| USER_DFMEA_19 | On-device guidance | UR_21 (IFU/guidance in local language) | User misunderstands operating or corrective-action guidance presented in a non-local language or ambiguous wording | Incorrect sensor correction, alarm handling, or configuration; downstream use errors | Guidance is the mitigation channel for many other failure modes; if it is unreadable those mitigations fail | Device deployed with wrong language setting; translation ambiguity; guidance too long to read during a time-critical intervention | Major | On-device guidance and IFU provided in the local language, selected at installation and verified; pictogram support for time-critical instructions | Medium | UR_21 |
### Use Scenarios

Concrete narratives of how the product is used in the real world, walking from a triggering situation to a successful outcome. Each scenario contains use tasks (UT_*).

#### Pre-Hospital Emergency Response at the Scene and During Transport

A paramedic arrives at a roadside collision, powers on the portable monitor beside a semi-conscious patient, and continues monitoring uninterrupted in the back of a moving ambulance. There is no time for configuration — the software must be measuring within moments of attaching sensors.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_01 | Power on and begin monitoring immediately | The paramedic switches the monitor on at the scene; the software auto-starts into monitoring with safe default settings, requiring no menu navigation before measurement can begin. | UR_11 |
| UT_02 | Attach sensors and confirm live values | The paramedic applies the six non-invasive sensors in clinical priority order — oxygenation and heart rate first — glancing at the screen to confirm each sensor's live value appears within seconds of attachment, verifying correct placement before the patient is moved onto the stretcher. | UR_04, UR_01 |
| UT_03 | Monitor all vitals during transport | In the moving ambulance, the paramedic keeps all parameters continuously and simultaneously in view while positioned at the patient's side, reading the display and hearing alarms despite vibration, siren and road noise, and changing daylight. | UR_01, UR_13 |
| UT_04 | Respond to a clinical alarm en route | When the patient's SpO2 drops, the paramedic — hands busy with the airway — recognises the alarm's priority from its sound alone without looking away from the patient, then confirms the alarming parameter on screen and intervenes. | UR_07, UR_13 |
| UT_05 | Hand over with a documented timeline | On arrival at the ER, the paramedic uses the timestamped event log to relay when vitals changed and alarms occurred during transport as part of the structured verbal handover to the receiving team. | UR_17 |

#### ER Intake of an Undifferentiated Patient

An emergency physician receives a patient with unclear symptoms — dyspnoea, tachycardia, no history available. She uses the monitor's vitals and the AI-ranked diagnostic candidates as an adjunct to focus her differential, including the case where the AI cannot reach a conclusion in time.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_06 | Establish full-parameter monitoring at intake | The ER nurse connects all sensors during initial triage and verifies that every parameter displays continuously and simultaneously on one screen before the physician's assessment begins. | UR_01, UR_04 |
| UT_07 | Review ranked diagnostic candidates | Within two minutes of valid signals being available, the physician reviews the ranked list of diagnostic candidates displayed alongside the live vitals and weighs it against her own history-taking and examination findings. | UR_02, UR_05 |
| UT_08 | Treat AI output as adjunctive | The physician sees the adjunctive marking on the candidate list, reminds the resident during the bedside teaching moment that it does not replace clinical judgement, and orders confirmatory diagnostics based on her own assessment. | UR_03 |
| UT_09 | Handle the convergence timeout | For a second patient with noisy signals from shivering and movement, the display first shows a "still converging" notice; when no reliable ranking can be formed, it changes to "cannot converge" and the physician proceeds on vitals and examination alone, undistracted by a pending result. | UR_06, UR_05 |

#### ICU Continuous Monitoring Across a Shift

An ICU nurse monitors a post-operative patient over a 12-hour shift, tailors alarm limits to the patient's baseline to reduce nuisance alarms, and hands the patient over to the night shift with a clear picture of what happened.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_10 | Take over a monitored patient at shift start | As part of her start-of-shift safety check, the incoming nurse confirms that all parameters are displayed and that the currently active alarm limits shown on screen match the care plan, before accepting responsibility for the patient. | UR_01, UR_08 |
| UT_11 | Tailor alarm limits to the patient | Because the patient is a chronically bradycardic athlete whose baseline keeps triggering nuisance low-heart-rate alarms, the nurse adjusts the heart-rate alarm limits to patient-specific values within the unit's alarm-management policy; the new limits remain visible on the display so any colleague can see what is set. | UR_08 |
| UT_12 | Triage overlapping alarms | When two alarms sound at once during the night, the nurse distinguishes the high-priority alarm from the lower-priority one by sound, attends to the critical condition first, and then addresses and clears the second. | UR_07 |
| UT_13 | Prepare and deliver shift handover | At handover, the nurse walks the night nurse through the timestamped log of alarms, limit changes, and vital-sign trends from the shift, so the patient's course is conveyed from the record rather than from memory. | UR_17, UR_08 |

#### Sensor Fault and Misplacement Recovery

During routine monitoring, a sensor detaches when the patient turns over in bed. The nurse must be told immediately which sensor failed, which readings are still trustworthy, and be able to restore full monitoring quickly.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_14 | Recognise a sensor-specific technical alarm | A misplacement alarm sounds; from the annunciation alone the nurse identifies exactly which of the six sensors is affected and that it is a technical, not clinical, alarm — so she heads to the bedside to fix a sensor, not to treat a deterioration. | UR_09, UR_07 |
| UT_15 | Determine which readings remain reliable | Before acting, the nurse reads the on-screen indication of which parameters are still measured reliably and which are compromised, and continues to trust the unaffected vitals while she works. | UR_10 |
| UT_16 | Reposition the sensor and confirm recovery | The nurse re-seats the detached sensor and watches its live value reappear within seconds, confirming full monitoring is restored and the technical alarm has cleared before leaving the bedside. | UR_04, UR_09 |
| UT_17 | Catch stale data on an apparently normal display | On a later round, a stale-data alarm alerts the nurse that one parameter has stopped updating even though the last displayed value looked normal; she troubleshoots the sensor rather than being falsely reassured by a frozen reading. | UR_09, UR_10 |

#### Second-Opinion Consultation via the HIS

A physician in a small regional hospital faces an ambiguous case at night, with no specialist on site, and wants a remote specialist to look at the monitoring data. She shares the data to the hospital information system without letting security steps delay emergency care.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_18 | Confirm patient identity before sharing | The physician initiates HIS transmission; the software prompts her to confirm the patient's identity so the data lands in the correct record, and she verifies the displayed identifiers against the patient's wristband. | UR_14, UR_18 |
| UT_19 | Transmit vitals and candidates for second opinion | She transmits the current vitals, trends, and the adjunctive-marked diagnostic candidates to the HIS, then phones the on-call specialist, who opens the data remotely while they talk. | UR_14, UR_03 |
| UT_20 | Maintain protected but immediate access | While data protection controls guard the transmission, the physician at the bedside retains uninterrupted, undelayed access to the live monitoring and alarms throughout the emergency. | UR_18 |
| UT_21 | Reconcile the consultation in the record | After the call, the physician checks the timestamped log to document when data was shared and correlates the specialist's advice with the vitals at that moment. | UR_17, UR_14 |

#### Simulation-Based Training Session

A clinical educator runs a training afternoon for new ambulance staff using simulation mode, in the trainees' local language, and needs evidence afterwards that each trainee completed the exercises — with zero risk of simulated data being mistaken for a real patient.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_22 | Start a clearly marked simulation | The educator activates simulation mode and opens the session by pointing out the full-screen banner that marks it unmistakably as simulation, demonstrating to trainees that no output can be confused with, or affect, a real patient. | UR_15 |
| UT_23 | Practise alarm response in local language | Trainees work through a deteriorating-patient scenario, following on-screen guidance and labels in their own language while practising alarm recognition and sensor handling. | UR_21, UR_15 |
| UT_24 | Practise the sensor-failure drill safely | The educator injects a simulated sensor disconnection; trainees practise identifying the failed sensor and the remaining reliable parameters without any real-world consequence. | UR_15, UR_09 |
| UT_25 | Record and retrieve training completion | At the end of the session, the educator retrieves the recorded completion evidence for each trainee and files it with the hospital's competency records. | UR_16 |

#### Fleet Deployment and Software Update by the Biomedical Engineer

A biomedical engineer rolls out a software update across the hospital's monitor fleet, coordinating with ward staff on which units are free. Updates must never interrupt active monitoring, and each updated unit must perform at least as well as before it returns to clinical use.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_26 | Verify no patient is connected before updating | The engineer selects a monitor for update; on a unit still connected to a patient, the software refuses to start the update and it never auto-starts, so the engineer defers that unit and moves on rather than negotiating a monitoring gap at the bedside. | UR_19 |
| UT_27 | Install the update on a free unit | On a disconnected monitor, the engineer runs the installation and confirms it completes without degrading any monitoring function of the device. | UR_20, UR_19 |
| UT_28 | Verify post-update readiness | After installation, the engineer performs a functional check — sensors show live values, alarms annunciate correctly — and reviews the log entry recording the update before releasing the unit back to the ward. | UR_20, UR_17 |
| UT_29 | Confirm consistent behaviour across care settings | The engineer spot-checks that an updated unit operates identically whether deployed to the ICU, ER, or an ambulance, with any setting-specific limitations stated on the device so rotating staff are not surprised. | UR_12 |

#### Degraded-Mode Operation After Partial Failure

During a long inter-hospital transfer, one sensor channel fails permanently and cannot be recovered en route. The transport nurse must keep monitoring safely with the remaining parameters until arrival.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_30 | Acknowledge the unrecoverable failure | The nurse receives the technical alarm for the failed channel, works through the corrective actions available in the vehicle — re-seating the sensor and checking the cable — and acknowledges the failure when it cannot be restored during transport. | UR_09, UR_10 |
| UT_31 | Continue monitoring on reliable parameters | The display clearly indicates which parameters remain reliable; the nurse continues monitoring those parameters continuously, with alarm behaviour intact for the functioning channels, in the noisy transport environment. | UR_10, UR_07, UR_13 |
| UT_32 | Hand over the degraded state with evidence | On arrival, the nurse hands over the patient together with the timestamped log showing when the channel failed and which data remained valid, so the receiving team can judge the monitoring history correctly. | UR_17, UR_10 |
### Usability FMEA (UFMEA_*)

An FMEA focused on usability: where the user interface, workflow, or interaction model can lead to errors, slow operation, or unsafe outcomes.

| ID | Scenario Title | Use Error | Cause | Effect | HF Cause | Rationale | Usability Impact Level | Mitigation (existing) | Mitigation (new) | Classification | Traces |
|----|----------------|-----------|-------|--------|----------|-----------|------------------------|-----------------------|------------------|----------------|--------|
| UFMEA_01 | Pre-Hospital Emergency Response at the Scene and During Transport | Paramedic reads the start-up/self-test screen as an already-live monitoring display and attaches sensors expecting values that are not yet being measured | Start-up screen visually resembles the monitoring layout; no unambiguous "measuring" state indication | Interval of unmonitored patient time at the scene while the paramedic believes monitoring is active | Expectation bias under time pressure; state ambiguity between booting and monitoring — paramedics do not watch a boot sequence, they glance once while their hands are on the patient | Auto-start with no menus removes navigation errors but shifts risk to state recognition — the user must instantly know when measurement has actually begun from a single glance | High | Software auto-starts directly into monitoring with safe defaults | Distinct start-up screen that cannot be mistaken for live monitoring, plus an explicit per-parameter "measuring" indication that appears only when valid data flows | High | UT_01 |
| UFMEA_02 | Pre-Hospital Emergency Response at the Scene and During Transport | Paramedic attributes a live value to the wrong sensor while confirming placement, accepting a misplaced sensor as correctly applied | Adjacent parameter tiles look alike; direct sunlight glare and roadside distraction while matching six sensors to six on-screen values | A misplaced or swapped sensor goes into transport undetected, yielding wrong or absent readings for that parameter | Perceptual confusion between visually similar display tiles; divided attention at an accident scene, gloved hands and glare degrading both touch precision and reading accuracy | Confirming each of six attachments by glancing at a dense screen invites tile mix-ups precisely when verification matters most | High | Live value appears within seconds of each attachment, in clinical priority order | Unambiguous sensor-to-tile coding (matching colour/icon/label per sensor) and a transient highlight of the tile belonging to the sensor just attached | High | UT_02 |
| UFMEA_03 | Pre-Hospital Emergency Response at the Scene and During Transport | Paramedic mishears a high-priority alarm as low priority under siren and road noise and defers response | Alarm priority tones insufficiently discriminable in the transport noise spectrum | Delayed intervention for a deteriorating patient (e.g. falling SpO2) during transport | Auditory masking; priority encoding carried by sound alone when eyes and hands are on the patient; crews habituated to a continuous background of tones default to "low priority" when uncertain | The scenario explicitly relies on recognising priority from sound alone — the tone set must survive the worst acoustic environment, not the quiet lab | High | Priority-differentiated alarm tones audible in transport environments | Priority tones validated for discriminability against siren/road-noise spectra; redundant high-visibility flash pattern readable in peripheral vision and in direct sunlight | High | UT_04, UT_03 |
| UFMEA_04 | Pre-Hospital Emergency Response at the Scene and During Transport | Paramedic scrolls past or misorders events in the timestamped log during verbal handover, relaying an incomplete or wrong timeline | Log presented as a long undifferentiated list; handover performed standing in a busy ER corridor | Receiving team acts on an inaccurate picture of when vitals changed and alarms occurred | Working-memory overload while translating raw log entries into a spoken narrative, under interruption and time pressure to hand the patient off | Handover is the single point where transport history transfers; a log optimised for storage rather than telling loses information at that point | Medium | Timestamped event log of vitals changes and alarms available on device | A condensed handover view that summarises alarms, interventions, and trend inflections in chronological order on one screen | High | UT_05 |
| UFMEA_05 | ER Intake of an Undifferentiated Patient | Physician anchors on the top-ranked diagnostic candidate and narrows the differential prematurely, under-weighting her own findings | Ranked-list presentation implies confidence ordering; top item visually dominant | Confirmatory diagnostics for the actual condition delayed or omitted; misdiagnosis risk | Anchoring and automation bias toward machine-ranked output, amplified by the cognitive load and time pressure of undifferentiated ER intake | Ranking is the product's core value and its core usability hazard — the display format itself steers clinical reasoning | High | Candidate list explicitly marked as adjunctive to clinical judgement | Present candidates with visible uncertainty/evidence indicators rather than a bare rank order, avoiding visual dominance of the first entry | High | UT_07, UT_08 |
| UFMEA_06 | ER Intake of an Undifferentiated Patient | Physician overlooks the adjunctive marking after repeated exposure and cites the AI output as a diagnostic result to the team | Static, always-identical marking loses salience with habituation | AI output treated as a confirmed diagnosis in team communication and documentation | Banner blindness — persistent labels stop being read after routine exposure; once spoken aloud or documented, the adjunctive status is stripped and the output propagates as fact | A warning everyone has seen a hundred times protects no one; an AI candidate documented as a diagnosis drives treatment decisions downstream, so the adjunctive status must survive habituation and export | High | Persistent adjunctive marking on the candidate list | Adjunctive status embedded in the candidate wording itself (e.g. "consider…") and repeated in any exported/HIS representation, not carried by a separable banner alone | High | UT_08 |
| UFMEA_07 | ER Intake of an Undifferentiated Patient | Physician confuses the "still converging" notice with the "cannot converge" state and either waits for a result that will never come or abandons a result about to arrive | The two states differ only in wording; both occupy the same screen region with similar styling | Attention held by a pending result during time-critical assessment, or available AI support discarded | Poor state discriminability between two semantically opposite messages; clinicians read state from shape and motion, not prose, when a patient is in front of them | The scenario's safe outcome depends on the physician instantly telling "wait" from "stop waiting" — subtle text differences cannot carry that | Medium | Distinct "still converging" and "cannot converge" notices with a two-minute bound | Visually and structurally distinct state presentations (e.g. progress indication vs. terminal icon with recommended action "proceed on clinical assessment") | Medium | UT_09 |
| UFMEA_08 | ICU Continuous Monitoring Across a Shift | Incoming nurse misreads the displayed alarm limits at shift start — pairing a limit with the wrong parameter or misreading units — and accepts a mismatched configuration | Limits shown in a dense table; parameter rows visually similar; check performed during a busy shift change | Patient monitored a full shift with limits that do not match the care plan; missed or nuisance alarms | Visual row-slippage in tabular data; verification performed as a quick glance rather than a read, because shift change is the busiest moment of the shift | The start-of-shift check is a deliberate safety barrier; its display must be designed for verification, not just disclosure | High | Active alarm limits permanently visible on the display | Limits rendered adjacent to each parameter's live value with clear unit labels, and a deviation cue when a limit differs from the unit's default profile | High | UT_10 |
| UFMEA_09 | ICU Continuous Monitoring Across a Shift | Nurse adjusts the wrong limit while tailoring alarms — wrong parameter selected, or upper bound changed when the lower was intended | Similar-looking limit-edit screens for all parameters; upper/lower fields adjacent; interruption mid-task | Alarm fails to trigger at true deterioration, or nuisance alarms persist and erode trust | Slip during selection in a homogeneous menu structure; interrupted task resumed at the wrong step — ICU nurses are interrupted several times per hour and resume from memory | Limit editing is a rare, high-consequence interaction performed under distraction — the classic recipe for a selection slip | High | Adjusted limits remain visible on the main display for any colleague to see | Edit screen shows parameter name, current value, and proposed limit together with a confirmation step summarising exactly what will change; an interrupted, uncommitted edit re-presents the pending change on return instead of committing or discarding it silently | High | UT_11 |
| UFMEA_10 | ICU Continuous Monitoring Across a Shift | Nurse silences or clears both overlapping alarms with one action while intending to address only the lower-priority one | Global silence/acknowledge control acts on all active alarms; small touch targets under night-shift lighting | High-priority alarm annunciation lost while the critical condition is still untreated | Mis-touch on adjacent controls; incorrect mental model of the silence control's scope; alarm fatigue makes reflexive, unscoped silencing the practised default response to any new tone | Overlapping alarms are exactly when per-alarm control matters; a global gesture inverts the triage the sounds were designed to enable | High | Priority-differentiated annunciation lets alarms be distinguished by sound | Per-alarm acknowledgement scoped to the selected alarm; high-priority alarms excluded from any single-gesture global silence | High | UT_12 |
| UFMEA_11 | ICU Continuous Monitoring Across a Shift | Night nurse receiving handover misses the limit-change entry among routine log events and assumes default alarm limits | Limit changes, alarms, and trend events interleaved uniformly in the timestamped log | Night shift misinterprets alarm behaviour (e.g. bradycardia alarms absent by design read as reassurance) | Signal lost in noise — safety-relevant configuration events not distinguished from routine entries; on nights, silence is read as stability, so a deliberately widened limit masquerades as a quiet patient | The log serves both documentation and handover; a wrong mental model of alarm coverage can persist a full night shift while the patient deteriorates silently — that is a direct patient-harm pathway, not a documentation defect | High | Timestamped log of alarms, limit changes, and trends | Log filtering/highlighting by event type, with active non-default limits called out in the handover view | High | UT_13 |
| UFMEA_12 | Sensor Fault and Misplacement Recovery | Nurse misidentifies which of the six sensors triggered the technical alarm and manipulates a working sensor | Annunciation names the sensor ambiguously (channel number vs. body-site terms); similar cabling at the bedside | Faulty sensor stays compromised while a good channel is disturbed, extending degraded monitoring | Mapping error between on-screen sensor designation and physical sensor on the patient — clinicians think in body sites, not channel numbers, and cables converge invisibly under sheets and dressings | Fixing the right sensor first time is the whole task; every mismatch between screen naming and bedside reality doubles the gap duration | High | Technical alarm identifies the affected sensor and is distinguishable from clinical alarms | Sensor identification by body-site name and matching visual coding on connector/cable consistent with the on-screen designation | High | UT_14, UT_16 |
| UFMEA_13 | Sensor Fault and Misplacement Recovery | Nurse misreads the reliability indication and continues to trust a compromised parameter (or distrusts a reliable one) | Reliability state shown by a subtle cue (dimming, small icon) easily missed or inverted in interpretation | Clinical decisions based on invalid readings, or valid readings ignored during the fault | Weak perceptual coding of a safety-critical state; ambiguous iconography; a plausible-looking number is trusted regardless of any small icon beside it | The scenario hinges on the nurse partitioning trust across parameters mid-task — the display must make that partition impossible to misread | High | On-screen indication of which parameters are reliable vs. compromised | Unmistakable compromised-state rendering (value visually suppressed/struck with explicit "unreliable" label) that cannot be read as a normal value | High | UT_15 |
| UFMEA_14 | Sensor Fault and Misplacement Recovery | Nurse leaves the bedside after re-seating the sensor on seeing a value flash, without confirming the technical alarm has actually cleared | Momentary value reappearance read as full recovery; alarm-clear state not checked | Sensor still intermittent; monitoring gap persists after the nurse has departed | Premature task closure — the goal feels achieved when the salient cue appears, and the nurse has other patients pulling her away from the bedside | Recovery confirmation is a two-condition check (value stable and alarm cleared) but the UI rewards the first condition alone | Medium | Live value reappears within seconds; technical alarm clears on recovery | Explicit recovery confirmation cue (e.g. transient "sensor restored" notice) issued only when the signal is stable and the alarm state has cleared | High | UT_16, UT_17 |
| UFMEA_15 | Second-Opinion Consultation via the HIS | Physician clicks through the patient-identity confirmation without verifying against the wristband, sending data to the wrong record | Confirmation dialog identical on every transmission; routine cases train reflexive acceptance | Monitoring data and diagnostic candidates filed in another patient's record; remote specialist advises on wrong data | Habituated click-through of a repeated confirmation prompt — every routine "yes" trains the reflex that fails on the one mismatched case | A confirmation that is always answered "yes" stops being a check; identity errors here propagate to the remote consultation undetected | High | Identity-confirmation prompt with displayed patient identifiers before HIS transmission | Confirmation requiring an active identity act (e.g. wristband scan or entering an identifier fragment) rather than a single acknowledging tap, consistent with positive patient identification practice already routine at the bedside | High | UT_18 |
| UFMEA_16 | Second-Opinion Consultation via the HIS | Physician navigating the HIS-sharing menus loses sight of live vitals, missing a deterioration during the consultation set-up | Transmission workflow presented as a full-screen flow replacing the monitoring view | Deterioration or alarm onset unnoticed at the bedside during the minutes of sharing set-up | Mode confusion — administrative task visually displaces the safety-critical monitoring task; head-down menu work suppresses the peripheral monitoring clinicians normally maintain | The scenario requires monitoring access to remain uninterrupted; a full-screen sharing dialog quietly violates that requirement | High | Live monitoring and alarms remain accessible without delay during data-protection steps | Sharing workflow constrained to a partial overlay that never occludes live vitals and alarm indications | High | UT_20, UT_19 |
| UFMEA_17 | Simulation-Based Training Session | A clinician encountering the device mid-session mistakes simulated vitals for a real patient, or the educator's trainees later treat a real screen as "just simulation" | Simulation banner habituated during long sessions; visual similarity of simulated and real displays | Real deterioration ignored as simulation, or simulated crisis escalated as real | Banner blindness plus context carry-over between training and clinical use | The marking must work for the unbriefed bystander, not only for participants who watched it being switched on | High | Full-screen unmistakable simulation banner; simulated data cannot affect a real patient | Persistent global visual treatment of the entire simulated display (e.g. distinct background/watermark on every screen and log entry), not a banner element alone | High | UT_22, UT_24 |
| UFMEA_18 | Simulation-Based Training Session | Educator ends the session but leaves the device in simulation mode, and it is returned toward clinical readiness still simulating | Mode exit buried in menus; no forcing function at session end; handling delegated to trainees | A device that would display simulated data en route to clinical use — caught late or not at all | Post-completion error — the goal (training done) is achieved before the safety step (mode exit); packing up and returning equipment is nobody's focal task | Mode persistence after task completion is a classic latent error; the design must make lingering simulation impossible to overlook | High | Simulation clearly marked while active | Simulation mode requires explicit exit with confirmation, times out to a blocking "still in simulation" state, and blocks live sensor data from displaying while active | High | UT_22, UT_25 |
| UFMEA_19 | Fleet Deployment and Software Update by the Biomedical Engineer | Engineer misreads the "update refused — patient connected" message as a technical fault and retries, troubleshoots, or seeks an override at a bedside unit | Refusal presented as a generic error dialog without stating the reason and the safe next action | Time lost fault-finding a healthy safeguard; pressure to circumvent the interlock; ward disturbance at an occupied bed | Incorrect mental model — protective refusal indistinguishable from malfunction | An interlock that does not explain itself gets fought instead of respected; the message must convert refusal into the correct deferral action | Medium | Update hard-blocked and never auto-started while a patient connection is active | Refusal dialog states the cause ("active patient connection"), the affected unit, and the recommended action (defer and select another unit) | High | UT_26, UT_27 |
| UFMEA_20 | Degraded-Mode Operation After Partial Failure | Transport nurse, after acknowledging the unrecoverable channel, wrongly generalises the failure — assuming alarms or reliability are degraded across all parameters, or overlooking the failed channel's absence later in transport | Acknowledgement clears the salient alarm; degraded state thereafter shown only subtly; vibration and noise degrade reading precision | Under-trust in valid parameters (ignored alarms) or forgotten monitoring gap at handover | Incorrect generalisation of a partial failure; low-salience persistent state after alarm acknowledgement; over hours of transport, out of sight becomes out of mind | Acknowledgement must silence the sound, not the information — the degraded configuration has to stay self-evident for hours and transfer intact into the handover log | High | Display indicates which parameters remain reliable; alarm behaviour intact on functioning channels; failure timestamped in the log | Persistent degraded-mode summary strip (failed channel named, remaining channels marked "monitoring active") that survives acknowledgement and is auto-included in the handover log view | High | UT_30, UT_31, UT_32 |
### Usability Requirements (USR_*)

Measurable requirements for how the product must perform from a user perspective: task completion times, error rates, learnability, accessibility. Validated through usability testing.

| ID | Requirement | Classification | Traces |
|----|-------------|----------------|--------|
| USR_01 | ≥ 95% of representative users shall correctly read the displayed value of any parameter enumerated in the Acquired Parameters / Signals table within 3 seconds from a viewing distance of 1 m, without touching the device, both under direct sunlight of ≥ 100,000 lux and in darkness, and while the device is subjected to random vibration per the EN 1789 / IEC 60068-2-64 road-ambulance test profile. | High | UR_01, UR_13 |
| USR_02 | While a defined test recording of combined siren and road noise is reproduced at 72–78 dB(A) measured at the operator position, ≥ 95% of participants shall correctly identify the priority (high/medium/low) of an annunciated alarm by sound alone within 5 seconds of alarm onset, with zero high-priority alarms classified as low priority across the test population. | High | UR_07, UR_13, UFMEA_03 |
| USR_03 | ≥ 95% of participants shall detect the onset of a high-priority visual alarm indication within 5 seconds while the display is only in their peripheral vision, in both direct-sunlight and darkened test conditions. | High | UR_07, UFMEA_03 |
| USR_04 | When attaching six sensors in clinical priority order while wearing clinical examination gloves and exposed to a directional glare source of ≥ 100,000 lux at 45° incidence to the display, ≥ 95% of participants shall correctly match each just-attached sensor to its on-screen parameter tile on the first attempt, with a sensor-to-tile misattribution rate ≤ 2% of attachments across the test population. | High | UR_04, UFMEA_02 |
| USR_05 | ≥ 95% of unbriefed participants shall correctly state, within 3 seconds of a single glance, whether the device is still starting up or actively measuring for each connected parameter, with zero participants reporting the start-up screen as live monitoring. | High | UR_11, UFMEA_01 |
| USR_06 | ≥ 95% of participants shall correctly discriminate the "still converging" state from the "cannot converge" state within 3 seconds of presentation, and after a "cannot converge" notice ≥ 95% shall state the correct next action (proceed on clinical assessment) without prompting. | High | UR_06, UFMEA_07 |
| USR_07 | ≥ 95% of participants — including those exposed to the display repeatedly across a 60-minute session — shall correctly describe every displayed, logged, or HIS-transmitted diagnostic candidate as adjunctive (not a confirmed diagnosis or measurement) when questioned at the end of the session, with zero participants citing a candidate as a diagnostic result. | High | UR_03, UFMEA_05, UFMEA_06 |
| USR_08 | At a simulated shift-start check, ≥ 95% of participants shall correctly pair every active alarm limit with its parameter and unit, and 100% shall detect a limit that deviates from the unit default profile, within 30 seconds total. | High | UR_08, UFMEA_08 |
| USR_09 | In an alarm-limit adjustment task including a scripted mid-task interruption, ≥ 95% of participants shall commit the intended change to the intended parameter and bound on the first attempt, with a wrong-parameter or wrong-bound commit rate of 0% after the confirmation step across the test population, and mean task time ≤ 60 seconds. | High | UR_08, UFMEA_09 |
| USR_10 | With two alarms of different priority active simultaneously, ≥ 95% of participants shall silence only the alarm they intend to address on the first attempt, and no single user action in testing shall silence a high-priority alarm together with a lower-priority one. | High | UR_07, UFMEA_10 |
| USR_11 | In HIS-transmission testing seeded with a patient-identity mismatch in 1 of every 10 trials, participants shall detect and abort 100% of mismatched transmissions via the active identity-confirmation step, while completing correct-identity confirmations within 15 seconds on average. | High | UR_14, UR_18, UFMEA_15 |
| USR_12 | During the complete HIS-sharing workflow, live vital-sign values and alarm indications shall remain visible at all times, and ≥ 95% of participants shall detect a simulated deterioration alarm within 10 seconds while performing the sharing task. | High | UR_14, UFMEA_16 |
| USR_13 | 100% of unbriefed clinicians approaching a device in simulation mode mid-session shall identify the displayed data as simulated within 5 seconds, from any screen or log view, without any participant initiating a real-patient response. | High | UR_15, UFMEA_17 |
| USR_14 | In session-end testing, 0% of devices shall be returned toward clinical readiness while still in simulation mode: 100% of participants shall either explicitly exit simulation with confirmation or be stopped by the blocking "still in simulation" state before live use is possible. | High | UR_15, UFMEA_18 |
| USR_15 | Following an unrecoverable channel failure and alarm acknowledgement, ≥ 95% of participants shall correctly identify, at any point during a simulated 2-hour transport, which parameters remain reliably monitored and which channel has failed, within 5 seconds of being asked, with zero participants generalising the failure to functioning channels. | High | UR_10, UFMEA_13, UFMEA_20 |
| USR_16 | After re-seating a faulty sensor, ≥ 95% of participants shall correctly distinguish full recovery (stable signal and cleared alarm) from momentary value reappearance before leaving the bedside, with a premature-departure rate ≤ 5% in fault-recovery testing. | High | UR_09, UFMEA_12, UFMEA_14 |
| USR_17 | Using the condensed handover view, ≥ 95% of receiving clinicians shall correctly recount all alarms, limit changes (including active non-default limits), and trend inflections from the preceding monitoring period within 2 minutes, with zero safety-relevant events omitted across the test population. | High | UR_17, UFMEA_04, UFMEA_11 |
| USR_18 | After completing one simulation training scenario and without further assistance, ≥ 90% of first-time users shall correctly perform the core monitoring tasks (read vitals, identify alarm priority, interpret a diagnostic candidate as adjunctive, respond to a technical alarm) on their first live-equivalent attempt. | High | UR_15 |
| USR_19 | ≥ 95% of representative users per target-market language shall each score ≥ 90% on the defined comprehension test covering routine bedside operating questions, using only the local-language IFU and on-device guidance, without external help. | High | UR_21 |
| USR_20 | (a) Live monitoring, display, and alarm functions shall require zero authentication interaction — verified in 100% of trials with no credential prompt presented; (b) an authorised clinician, including via the break-glass mechanism, shall reach protected functions within 5 seconds of initiating access in 100% of trials. | High | UR_18 |
| USR_21 | ≥ 95% of biomedical engineers encountering the "update refused — patient connected" condition shall correctly state the refusal cause and take the recommended deferral action within 30 seconds, with zero attempts to troubleshoot or override the interlock at an occupied bed. | High | UR_19, UFMEA_19 |
## Concept

### UI/UX Design

Wireframes, interaction flows, navigation structures, and visual design principles that translate the user requirements into a tangible concept.

#### Design Principles

The following principles govern every screen and interaction of the MMSS user interface. Each traces to the usability requirements it realises.

1. **Glanceability first.** Every safety-relevant fact — current values, active alarm limits, alarm state, measuring state, reliability state — is readable in a single glance from 1 m without any interaction (USR_01, USR_08, USR_15). Nothing safety-relevant lives behind a tap.
2. **Alarm-first hierarchy.** Alarm annunciation always outranks every other screen element in position, size, colour, and motion. Alarm control is always per-alarm and scoped; no gesture can silence a high-priority alarm together with anything else (USR_02, USR_03, USR_10, UFMEA_10).
3. **Measured is never interpreted.** Measured vital signs and AI-derived diagnostic candidates occupy structurally separate screen regions with different visual grammar. Adjunctive status is embedded in the candidate wording itself ("Consider …") so it survives habituation, quotation, logging, and HIS export (USR_07, UFMEA_05, UFMEA_06).
4. **State is unmistakable.** Start-up, converging, cannot-converge, measuring, unreliable, degraded, and simulation states are each rendered with distinct shape and structure — never by wording or subtle styling alone (USR_05, USR_06, USR_13, USR_15, UFMEA_01, UFMEA_07, UFMEA_13).
5. **Minimal interaction, forgiving interaction.** Monitoring requires zero configuration: the device auto-starts into monitoring with safe defaults (UFMEA_01). The rare interactions that exist (limit editing, sharing, simulation control) use large glove-compatible targets, explicit confirmation summaries, and interruption-safe resume (USR_09, UFMEA_09).
6. **Environment robustness.** Every visual element passes in direct sunlight (≥ 100,000 lux), darkness, and vehicle vibration; every tone survives siren and road noise (USR_01, USR_02, USR_03, UR_13).
7. **The display tells the handover story.** Configuration deviations, degraded channels, and event history remain self-evident on screen for hours and transfer intact into a condensed handover view (USR_15, USR_17, UFMEA_11, UFMEA_20).

#### Main Monitoring Screen

The monitoring screen is the home state — the device boots into it, and every workflow returns to it. All six parameter tiles (one per source element in the Acquired Parameters / Signals table) are simultaneously visible with live value and active alarm limits (USR_01, USR_08). The diagnostic candidate panel is a fixed side region that can never expand over, or push aside, the vitals (UR_02, UFMEA_16).

```
+------------------------------------------------------------------------------------------------+
| ALARM BAR   [!!] HIGH  SpO2 LOW 84 %           [ ACK THIS ALARM ]      12:41   Batt 82%  HIS↔ |
|             [! ] MED   RR HIGH 28 /min         [ ACK THIS ALARM ]      Bed 7 · DOE, J.        |
+--------------------------------+--------------------------------+------------------------------+
| ECG (green)        ● measuring | SpO2 (blue)        ● measuring | DIAGNOSTIC SUPPORT           |
|                                |                                | -- adjunctive to clinical -- |
|   HR   128        ⌃150  ⌄50   |    84             ⌃100  ⌄90   |                              |
|        bpm                     |    %              *ALARM*      |  Consider: Sepsis            |
|  ~~ECG waveform~~~~~~~~~~~~~~  |  Pulse 126 bpm                 |  evidence [########--]       |
+--------------------------------+--------------------------------+  Consider: Pulm. embolism    |
| NIBP (red)         ● measuring | TEMP (yellow)      ● measuring |  evidence [#####-----]      |
|                                |                                |  Consider: Pneumonia         |
|   92/58 (69)      ⌃180/110    |   38.9            ⌃39.0       |  evidence [###-------]      |
|        mmHg        ⌄90/50 *   |    °C              ⌄35.0       |                              |
|                                |                                |  State: ● converged 12:39   |
+--------------------------------+--------------------------------+  Not a diagnosis. Verify     |
| CO2 (grey)         ● measuring | EEG (purple)     ✖ UNRELIABLE  |  by clinical assessment.     |
|                                |                                |                              |
|  etCO2 46  RR 28  ⌃60 ⌄20    |  -- 4̶2̶ --  index               +------------------------------+
|   mmHg    /min    ⌃30 ⌄6 !   |  CHECK SENSOR: forehead, left  | [Limits] [Log] [Handover]    |
|  ~~capnogram~~~~~~~~~~~~~~~~  |  ~~no valid signal~~           | [Share to HIS]   [Settings]  |
+--------------------------------+--------------------------------+------------------------------+
| STATUS  ECG ● | SpO2 ● | NIBP ● | TEMP ● | CO2 ● | EEG ✖ fault  ||  * = non-default limit      |
| DEGRADED MODE: EEG channel failed 12:12 — all other channels monitoring active   [handover ✓] |
+------------------------------------------------------------------------------------------------+
```

Key elements:

- **Alarm bar (top, full width).** One row per active alarm, ordered by priority, each with its own dedicated acknowledge control — there is no global silence for high-priority alarms (USR_10, UFMEA_10). A silenced alarm stays listed with a crossed-bell icon and a countdown until re-annunciation.
- **Parameter tiles.** Each tile carries: the parameter name with its **sensor colour code** matching the physical connector and cable (USR_04, UFMEA_02, UFMEA_12); a per-parameter **measuring state dot** that appears only when valid data flows (USR_05, UFMEA_01); the live value in glance-size numerals; and the **active alarm limits rendered adjacent to the value with units**, with a `*` deviation cue when a limit differs from the unit default profile (USR_08, UFMEA_08). On sensor attachment the owning tile flashes a transient highlight for 5 s to confirm sensor-to-tile mapping (USR_04).
- **Unreliable-value rendering.** A compromised parameter shows its last value struck through and dimmed, overlaid with a solid `✖ UNRELIABLE` label and the affected sensor named by body site — it cannot be read as a normal value (USR_15, UFMEA_13).
- **Diagnostic candidate panel (right, fixed width).** Candidates are worded "Consider: …" with per-candidate evidence indicators instead of a bare rank order; no entry is visually dominant (USR_07, UFMEA_05). The panel header and footer state adjunctive status; the same wording is embedded in logs and HIS exports (UFMEA_06). The panel's state row distinguishes *converging* (animated progress ring + elapsed time) from *cannot converge* (static terminal icon + the action "Proceed on clinical assessment") by shape and structure, not wording alone (USR_06, UFMEA_07).
- **Status strip (bottom).** Per-parameter measuring/fault state, convergence state, and — when applicable — a persistent **degraded-mode strip** naming the failed channel and confirming the remaining channels are actively monitored. This strip survives alarm acknowledgement and is auto-included in the handover view (USR_15, UFMEA_20).

#### Key Interaction Flows

**Flow 1 — Alarm handling (per-alarm acknowledge)** (USR_10, UFMEA_10)

1. An alarm annunciates: dedicated row in the alarm bar, priority tone, and a high-visibility flash pattern readable in peripheral vision and sunlight (USR_02, USR_03, UFMEA_03).
2. The user taps the acknowledge control **on that alarm's own row**; the tap target belongs to exactly one alarm — there is no shared or global control for high-priority alarms.
3. Only the selected alarm's audio is silenced. The row remains visible with a crossed-bell icon and a re-annunciation countdown; the visual indication and the alarm condition itself persist until the condition clears.
4. Any other active alarm continues annunciating unchanged, at its own priority.
5. When the physiological condition resolves, the row clears and the event is written to the log with timestamps for onset, acknowledgement, and resolution.

**Flow 2 — Alarm-limit editing** (USR_08, USR_09, UFMEA_09)

1. From the monitoring screen the user taps `[Limits]`, then the target parameter **tile itself** (colour-coded, showing its live value) — never a look-alike list row.
2. The edit screen shows, together on one screen: parameter name and colour code, current live value, current limits, and the proposed limit; upper and lower bounds are visually distinct, separated controls. Entry is bounded to the safe range.
3. Committing requires a **confirmation summary**: "ECG heart-rate LOWER limit: 50 → 45 bpm" — parameter, bound, old value, new value — with explicit `[Confirm change]` / `[Discard]`.
4. **Interruption handling:** if the user leaves mid-edit (new alarm, timeout, navigation away), the uncommitted change is neither applied nor silently discarded. On return, the pending change is re-presented as the same confirmation summary for an explicit decision.
5. After commit, the new limit appears immediately next to the value on the tile with the `*` non-default cue, and the change is logged and highlighted in the handover view (USR_17, UFMEA_11).

**Flow 3 — Sensor fault recovery** (USR_16, UFMEA_12, UFMEA_13, UFMEA_14)

1. A technical alarm annunciates with a tone set distinct from clinical alarms; the affected sensor is named **by body site** ("SpO2 sensor — left index finger"), matching the colour coding on the connector and cable.
2. The affected tile switches to unreliable rendering (struck value, `✖ UNRELIABLE`); all other tiles explicitly retain their measuring dots so trust is partitioned per parameter.
3. The user locates the physical sensor via its colour code and body-site name and corrects it.
4. A momentary value reappearance does **not** clear the state. The tile shows "signal returning — confirming…" until the signal is stable and the alarm condition has cleared.
5. Only then does the device issue an explicit **recovery confirmation**: a transient "Sensor restored — SpO2 monitoring active" notice on the tile, the measuring dot returns, and the technical alarm row clears. The fault and recovery are logged with timestamps.
6. If the channel cannot recover, the flow ends in the persistent degraded-mode strip instead (UFMEA_20).

**Flow 4 — Sharing to HIS** (USR_11, USR_12, UFMEA_15, UFMEA_16)

1. The user taps `[Share to HIS]`. The workflow opens as a **partial overlay** confined to the diagnostic-panel column; all six tiles, the alarm bar, and alarm annunciation remain fully visible and active throughout (USR_12).
2. The overlay displays the patient identifiers to be transmitted and the destination record.
3. Confirmation requires an **active identity act** — scanning the patient wristband or entering an identifier fragment — not a single acknowledging tap (USR_11). A mismatch blocks transmission and states the discrepancy.
4. On match, transmission proceeds with a progress indication in the overlay; diagnostic candidates are exported with their adjunctive wording intact (UFMEA_06).
5. Any alarm during the flow annunciates normally over the overlay; the user can act on it and resume sharing where they left off.
6. Completion (or abort) is confirmed in the overlay, logged, and the overlay dismisses back to full-width monitoring.

**Flow 5 — Simulation mode enter/exit** (USR_13, USR_14, UFMEA_17, UFMEA_18)

1. Entering simulation requires a deliberate settings action with confirmation — it is never reachable by accident from monitoring.
2. While active, the **entire display** carries a global simulation treatment: a distinct background tint and a repeating "SIMULATION" watermark on every screen, overlay, and log entry — not a dismissible banner element (USR_13).
3. Simulated data is architecturally isolated: it cannot trigger HIS transmission and simulated alarms are visually stamped as simulated.
4. **Auto-block on real sensor:** if a live sensor delivers real patient data while simulation is active, the device blocks the real data from displaying, annunciates the conflict, and demands a simulation-exit decision before any monitoring value is shown (UFMEA_18).
5. Exiting requires an explicit `[End simulation]` action with confirmation. There is no timeout that silently returns the device to clinical mode.
6. If the session goes idle, the device escalates to a blocking full-screen "STILL IN SIMULATION" state that must be explicitly resolved before the device can be returned toward clinical readiness (USR_14).

#### Navigation Structure

The navigation model is **flat and monitoring-centred** — there is no menu tree.

- **Level 0 — Monitoring screen.** The permanent home state. The device auto-starts into it with safe defaults and no configuration steps (UFMEA_01, USR_05); every flow returns to it automatically. All monitoring, alarm, state, and reliability information lives here — **zero-menu monitoring**: a user who never touches the screen misses nothing safety-relevant (USR_01).
- **Level 1 — five direct-access functions**, each exactly one tap from the monitoring screen, each opening as an overlay or single screen with a one-tap return: `[Limits]` (Flow 2), `[Log]` (filterable event log with event-type highlighting for alarms, limit changes, and technical events — UFMEA_11), `[Handover]` (condensed chronological summary of alarms, interventions, limit changes with active non-default limits called out, trend inflections, and any degraded-mode entry — USR_17, UFMEA_04, UFMEA_20), `[Share to HIS]` (Flow 4), and `[Settings]` (language, display/volume within floors, simulation entry, device information; software update is refused with a stated cause and deferral action while a patient is connected — USR_21, UFMEA_19).
- There is no level 2. No safety-relevant information is ever more than one tap deep, and no overlay may occlude the parameter tiles or the alarm bar.

#### Visual Design Principles

- **Alarm colour semantics per IEC 60601-1-8:** high-priority clinical alarms in red with a fast flash pattern; medium priority in yellow with a slow flash; low priority in cyan, steady. **Technical alarms** use a separate cool-blue treatment with a distinct tone set and a sensor/wrench glyph so a measurement problem can never be read as a change in patient state (UR_09, UFMEA_12). Alarm colours are reserved: red, yellow, and cyan appear nowhere else in the interface.
- **Sensor identity colours:** each of the six source elements owns a fixed identity colour (ECG green, SpO2 blue, NIBP red-brown, Temp yellow-ochre, CO2 grey, EEG purple) applied consistently to tile header, physical connector, and cable marker; identity colours are desaturated relative to alarm colours and all foreground/background pairs meet contrast for sunlight and night readability with redundant text labels for colour-vision deficiency (USR_04).
- **Simulation treatment:** a global background tint plus repeating diagonal "SIMULATION" watermark applied to every screen, overlay, exported view, and log entry while the mode is active — structurally inseparable from the content it marks (USR_13, UFMEA_17).
- **Unreliable-value rendering:** struck-through, dimmed digits at reduced size, overlaid with a solid high-contrast `✖ UNRELIABLE` label and body-site sensor name; the compromised state is carried by structure (strike + overlay + label), never by dimming alone (USR_15, UFMEA_13).
- **Typography and sizing for 1 m glance reading:** primary parameter values in a heavyweight tabular numeral face at ≥ 20 mm digit height (readable at ≥ 1 m in vibration); alarm-limit and unit text ≥ 5 mm; minimum touch-target size 15 × 15 mm with 5 mm spacing for gloved use (USR_01, USR_04). Numerals are tabular so values do not shift position as digits change.
- **Brightness and volume floors:** display luminance auto-ranges with an enforced floor sufficient for ≥ 100,000 lux sunlight readability and a night mode that preserves alarm-colour discriminability; alarm volume cannot be reduced below the level validated to be discriminable over siren and road noise, and high-priority visual alarms retain a flash pattern detectable in peripheral vision in both sunlight and darkness (USR_01, USR_02, USR_03, UR_13).
- **Motion discipline:** animation is reserved for state semantics only — alarm flash patterns, the converging progress ring, and the transient sensor-attachment highlight. Nothing else on the screen moves, so any motion is meaningful (USR_05, USR_06).
### Actors

Individuals, groups, or systems that perform roles or tasks within the system or process.

| Actor | Description |
|-------|-------------|
| Bedside Critical-Care Nurse | Trained ICU nurse supervising several monitored patients over prolonged shifts; applies sensors, performs continuous vital-signs surveillance, and is the first responder to clinical and technical alarms. |
| Intensivist | Licensed ICU physician responsible for diagnostic and therapeutic decisions on critically ill patients; tailors alarm limits to the individual patient and reviews trends and event history for case and incident review. |
| Emergency Physician | Licensed physician making time-critical decisions on undifferentiated, acutely ill patients in the ER; relies on fast vitals availability, early ranked diagnostic candidates, and HIS data sharing for second opinions. |
| Emergency-Room Nurse | Trained ER nurse who connects patients at intake, watches multiple bays, and hands patients over between care areas; needs identical operation across settings and secure, undelayed data handling. |
| Pre-hospital Professional | Trained paramedic operating in a mobile medical unit at the scene and in moving vehicles; applies sensors rapidly and monitors en route under noise, vibration, and variable lighting with near-zero device interaction. |
| Biomedical / Clinical Engineer | Hospital technician who deploys the MMSS onto the existing monitor fleet, installs updates, verifies post-update readiness, and accesses logs for service and incident investigation; works outside the live bedside. |
| Clinical Educator | Trainer who runs mandatory simulation-based training sessions on the device itself and retrieves evidenced training-completion records for the organisation's competency files. |
| Measurement devices | The six non-invasive devices (ECG monitor, pulse oximeter, blood pressure monitor, thermal probe, capnometer, EEG monitor) supplying the acquired parameters and signals; each also annunciates audibly on its own, independent of the MMSS. |
| AI diagnostic engine | Commercially validated off-the-shelf analysis engine that receives live monitoring data from the MMSS and returns ranked diagnostic candidates; independently issues an audible notification when its two-minute convergence budget expires. |
| Hospital information system (HIS) | External hospital system that receives monitored parameters, trends, and adjunctive-marked diagnostic candidates from the MMSS for remote review and second opinion, over a recognised healthcare interoperability standard. |
| Host CPU platform / RTOS | Compact embedded CPU platform with a real-time operating system on which the MMSS executes; provides computing resources, device connectivity, and OS services. |
| Monitor display | Display unit of the portable patient monitor on which the MMSS presents vital signs, waveforms, diagnostic candidates, statuses, and alarm annunciations. |
### Use Cases (UC_*)

_To be added_

| ID | Title | Actor | Goal | Satisfies | Classification | Precondition | Main Success Scenario | Alternative Scenarios | Exception Scenarios | Post Condition | Traces |
|----|-------|-------|------|-----------|----------------|--------------|-----------------------|-----------------------|---------------------|----------------|--------|
| UC_01 | Start monitoring automatically with incremental sensor attachment | Pre-hospital Professional | Have live monitoring running within seconds of power-on, per sensor as each is attached, with no configuration | UR_11, UR_04 | High | Monitor powered off; patient accessible; measurement devices available | 1. Actor powers on the monitor.<br>2. MMSS auto-starts into monitoring with safe default settings, requiring no menu navigation.<br>3. Actor attaches the first sensor to the patient.<br>4. MMSS shows that parameter's live value within seconds and positively indicates "measuring" for it.<br>5. Actor attaches the remaining sensors one by one; each value appears within seconds of its own attachment. | A1. Sensors are attached in any clinical priority order; each channel goes live independently, without waiting for the full set.<br>A2. Sensors were already applied to the patient before power-on (a second responder worked in parallel): each is detected at start-up and its channel goes live without reattachment. | E1. Auto-start does not complete: MMSS annunciates the fault audibly and visually and never shows a false "monitoring active" state.<br>E2. An attached sensor delivers no valid signal: a technical alarm identifies the affected sensor (UC_06). | All connected parameters live with alarming active; monitoring state unambiguous per parameter | UT_01, UT_02, UR_11, UR_04 |
| UC_02 | Display all vital signs continuously | Bedside Critical-Care Nurse (primary); Pre-hospital Professional (transport conditions) | Assess the patient's condition at a glance, at any time, in any intended environment | UR_01, UR_13 | High | Monitoring started (UC_01); sensors delivering valid signals | 1. MMSS acquires all parameters enumerated in the Acquired Parameters / Signals table.<br>2. MMSS displays all current values and waveforms simultaneously and in real time, with no user interaction needed to bring any parameter into view; intermittently measured parameters (e.g. non-invasive blood pressure) are shown with the time of their last measurement, never presented as if continuous.<br>3. The nurse reads the display at a glance, including from the foot of the bed; during transport, the pre-hospital professional reads the same display at the patient's side in a moving vehicle.<br>4. Alarms remain audible above ambient noise and the display remains readable in the prevailing light. | A1. Ambient conditions change (sunlight, darkness, vibration, siren noise): presentation stays readable and audible; brightness and volume never fall below safe minimums. | E1. A parameter stops updating: the value is visually invalidated as stale and a technical alarm is raised (UC_06); an unmarked last-known value is never shown as current. | Patient's current physiological state continuously and completely visible | UT_03, UT_06, UT_10, UR_01, UR_13 |
| UC_03 | Present ranked diagnostic candidates | Emergency Physician (supported by AI diagnostic engine) | Obtain an adjunctive, ranked diagnostic direction within two minutes without losing sight of the live vitals | UR_02, UR_03, UR_05, UR_06 | High | Monitoring active; connected sensors delivering valid signals | 1. MMSS provides the live monitoring data to the AI diagnostic engine.<br>2. MMSS shows a distinct "still converging" status while the ranking forms.<br>3. Within 2 minutes of valid signals, MMSS presents the ranked diagnostic candidates alongside — never obscuring — the live vitals.<br>4. Every candidate is visibly marked as adjunctive AI interpretation, distinct from measured values.<br>5. Actor weighs the candidates against own examination and retains diagnostic accountability. | A1. The ranking updates as signals evolve: the refreshed list replaces the prior one, visibly indicated as changed rather than silently swapped, with adjunctive marking preserved.<br>A2. Only a partial sensor set is attached: the candidates reflect the available signals only, and that limitation is visible alongside the ranking. | E1. Convergence is determined impossible: MMSS replaces "still converging" with an unmissable "cannot converge" notice and the actor proceeds on clinical judgement alone; the AI diagnostic engine additionally self-annunciates its timeout audibly. | Adjunctive candidates visible, or an explicit cannot-converge notice shown; vitals never obscured | UT_07, UT_08, UT_09, UR_02, UR_03, UR_05, UR_06 |
| UC_04 | Raise clinical alarm on abnormal vital sign | Bedside Critical-Care Nurse | Recognise and react to the most urgent patient condition first, even without line of sight to the screen | UR_07 | High | Monitoring active; alarm limits active (defaults or per UC_05) | 1. A vital sign crosses its active alarm limit.<br>2. MMSS annunciates a prioritised visual and audible alarm conforming to the medical alarm-system standard, with priority distinguishable by sound alone.<br>3. Actor recognises the priority without viewing the screen, confirms the alarming parameter on the display, and intervenes.<br>4. The alarm clears when the condition resolves; the event — including any transient alarm that resolved before the actor could attend — is logged with timestamp so it is never lost to the record. | A1. Two alarms sound at once: the higher priority is discriminable first and attended before the lower one.<br>A2. Actor pauses the audible alarm: the silence is time-limited with a persistent visual silenced indicator, and high-priority alarms break through. | E1. The alarm condition persists unaddressed: MMSS re-annunciates until the condition is resolved or the limits are deliberately changed (UC_05). | Actor aware of and responding to the condition; alarm event logged | UT_04, UT_12, UR_07 |
| UC_05 | Adjust clinical alarm limits to the patient | Intensivist (or Bedside Critical-Care Nurse per unit protocol) | Make alarming reflect the individual patient's actual clinical state without unsafe settings or hidden changes | UR_08 | High | Monitoring active; patient's clinical baseline known | 1. Actor opens the alarm-limit setting for a parameter.<br>2. MMSS shows the current limits, the defaults, and the permitted safe bounds.<br>3. Actor enters patient-specific limits.<br>4. MMSS validates the entries against the safe bounds and high/low consistency and applies them.<br>5. The active limits and their deviation from defaults remain visible at the parameter for any colleague. | A1. A new patient is admitted: limits reset to safe defaults rather than carrying over.<br>A2. Actor reverts a parameter to the safe defaults with a single deliberate action, without re-entering values. | E1. An entry is outside safe bounds or high/low transposed: MMSS rejects it and keeps the prior limits active. | Patient-specific limits active, visible at a glance, and logged with timestamp | UT_10, UT_11, UR_08 |
| UC_06 | Raise technical alarm for sensor fault or stale data | Bedside Critical-Care Nurse | Never confuse a measurement problem with a patient change, and correct the right sensor immediately | UR_09 | High | Monitoring active | 1. MMSS detects sensor misplacement, sensor disconnection, or stale/frozen data on a channel.<br>2. MMSS raises a technical alarm, distinct from clinical alarms, naming the affected sensor or parameter and the fault type with corrective guidance.<br>3. Affected values are visually invalidated and never presented as current.<br>4. Actor corrects the sensor at the bedside.<br>5. MMSS shows the live value returning within seconds and clears the alarm. | A1. Stale data behind an apparently normal display: the alarm is raised even though the last shown value looked plausible, prompting troubleshooting instead of false reassurance.<br>A2. A short-lived artifact (patient movement, repositioning, cuff inflation) disturbs a channel: the affected value is invalidated for the duration and recovers on its own, without a persisting alarm for every routine movement. | E1. The fault cannot be corrected: the alarm persists or re-annunciates until acknowledged, and degraded-mode handling applies (UC_07). | Full monitoring restored, or the fault explicitly acknowledged; all events logged | UT_14, UT_16, UT_17, UR_09 |
| UC_07 | Annunciate internal failure and operate in degraded mode | Bedside Critical-Care Nurse | Never rely on a silently failed function, and keep monitoring safely on what remains reliable | UR_10 | High | Monitoring active; an internal monitoring or diagnostic function fails | 1. MMSS detects the internal failure.<br>2. MMSS promptly annunciates the failure audibly and visually.<br>3. MMSS explicitly indicates which functions remain reliable and which are unavailable; unreliable outputs are suppressed rather than displayed.<br>4. Actor acknowledges the failure and continues monitoring the reliable parameters, with alarm behaviour intact for those channels.<br>5. The failure, acknowledgement, and remaining valid data are recorded in the timestamped log. | A1. The failed function recovers: MMSS restores it and indicates that full capability is available again. | E1. The failure affects the alarm capability itself: the measurement devices' own independent audible alarms remain available as the annunciation backstop. | No silent failure; degraded state and remaining trustworthy capability unambiguous; log supports handover | UT_15, UT_30, UT_31, UT_32, UR_10 |
| UC_08 | Share monitoring data with the HIS for second opinion | Emergency Physician (with HIS) | Let a remote specialist review the same live picture, in the correct patient record, without exposing data | UR_14, UR_03, UR_18 | High | Monitoring active; HIS reachable over the standard healthcare interface | 1. Actor initiates transmission to the HIS.<br>2. MMSS displays the patient identifiers and requires explicit identity confirmation before anything is sent.<br>3. Actor verifies the identifiers against the patient's wristband and confirms.<br>4. MMSS transmits the current and recent parameters, trends, and ranked candidates — still marked adjunctive — labelled with source device and timestamp, over the protected standard interface.<br>5. The remote specialist reviews the data while the actor retains full bedside monitoring; the transmission is logged. | A1. Actor cancels at the identity-confirmation step: nothing is transmitted.<br>A2. Unidentified patient admitted under a temporary alias: the actor confirms the alias identifiers exactly as registered in the HIS before sending, so the data lands in the alias record and nowhere else. | E1. HIS unreachable: MMSS notifies the actor; live monitoring and alarms at the bedside are unaffected.<br>E2. Identity mismatch discovered at confirmation: actor aborts and no data leaves the device. | Data delivered to the correct HIS record with adjunctive marking preserved; share event logged | UT_18, UT_19, UT_21, UR_14, UR_03, UR_18 |
| UC_09 | Run a simulation training session | Clinical Educator | Train staff realistically on the clinical interface with zero possibility of simulated data being taken as real | UR_15 | High | No real patient connected; training scenarios available; local language configured | 1. Educator activates simulation mode.<br>2. MMSS displays a permanent full-screen simulation banner and a distinct visual scheme.<br>3. MMSS replays realistic patient scenarios — vitals, alarms, diagnostic candidates, injected sensor faults — on the same interface used in live care, with guidance in the local language.<br>4. Trainees practise alarm recognition, sensor-fault handling, and candidate interpretation.<br>5. Educator ends the session and MMSS returns unambiguously to normal mode. | A1. Educator injects a simulated sensor disconnection: trainees identify the failed sensor and the remaining reliable parameters without real-world consequence. | E1. A real sensor is connected while simulation is active: MMSS blocks or terminates the simulation.<br>E2. Simulated data is never transmitted to the HIS nor logged as real patient data. | Training delivered risk-free; device unmistakably back in clinical mode | UT_22, UT_23, UT_24, UR_15 |
| UC_10 | Record and retrieve training completion | Clinical Educator | Evidence each user's completion of mandatory training for employer and auditors | UR_16 | High | Simulation session (UC_09) conducted with identified trainees | 1. MMSS records completion per user and per scenario with the completion date.<br>2. Educator retrieves the completion evidence at the end of the session.<br>3. Educator files the records with the organisation's competency records. | A1. Records are retrieved later, on demand, for an audit or rostering check. | E1. A trainee did not complete a scenario: no completion is recorded for that scenario, and the gap is visible in the evidence. | Each user's qualification to operate the system is demonstrable | UT_25, UR_16 |
| UC_11 | Review event log and handover view | Bedside Critical-Care Nurse | Convey or reconstruct the patient's monitored course from the record rather than from memory | UR_17 | High | Monitoring has occurred; events logged with accurate, consistent timestamps | 1. Actor opens the event log or the condensed handover view.<br>2. MMSS presents measurements, alarms, limit changes, diagnostic outputs, and user actions in chronological order with consistent timestamps.<br>3. Actor walks the receiving clinician through the timeline at handover, under normal shift-change time pressure, without leaving live monitoring.<br>4. The receiving clinician accepts responsibility with a complete, accurate picture. | A1. Incident review: the intensivist reconstructs the exact sequence of events around a clinical incident from the same log. | E1. A logged failure interrupted recording: the gap is explicitly marked in the timeline, never silently omitted. | Patient's course transferred or reconstructed completely and unambiguously | UT_05, UT_13, UT_32, UR_17 |
| UC_12 | Install a software update on the fleet | Biomedical / Clinical Engineer | Keep the fleet current and secure without ever interrupting active patient monitoring or degrading performance | UR_19, UR_20, UR_12 | High | Update announced and versioned; target monitor selected | 1. Engineer selects a monitor for update.<br>2. MMSS verifies that no patient or sensor connection is active.<br>3. Engineer starts the installation on the free unit.<br>4. MMSS installs the update and records it with its version in the log.<br>5. Engineer performs the functional check — live values appear, alarms annunciate — and confirms no measurement or alarm performance is degraded.<br>6. The unit returns to service behaving identically in ICU, ER, or ambulance, with any setting-specific limitations stated on the device. | A1. Fleet rollout: connected units are refused and deferred; the engineer proceeds unit by unit as they become free. | E1. A patient is connected: MMSS refuses to start the update, and the update never auto-starts.<br>E2. Installation fails or degrades a function: the unit is withheld from clinical use and the failure is logged. | Fleet updated without clinical disruption; post-update readiness evidenced in the log | UT_26, UT_27, UT_28, UT_29, UR_19, UR_20, UR_12 |
| UC_13 | Access patient data under protection in an emergency | Emergency-Room Nurse | Keep patient data protected without ever delaying an authorised clinician's urgent access | UR_18 | High | Device in clinical use; data-protection controls active | 1. Actor approaches the device during an emergency.<br>2. Live monitoring, display, and alarms are available immediately, with no authentication step in the way.<br>3. Actor accesses protected functions (e.g. data transmission, stored records) through authorised access, workable with gloved hands.<br>4. MMSS protects stored and transmitted patient data against unauthorised access throughout. | A1. Break-glass access: in an emergency the actor reaches a protected function without normal credentials, and the access is automatically audit-logged. | E1. An unauthorised access attempt occurs: it is refused and logged, and live monitoring at the bedside is unaffected. | Urgent care never delayed; data protection and audit trail intact | UT_20, UR_18 |
### Design Decisions (DD_*)

Choices made during design, with the considered alternatives and the rationale for the final choice.

| ID | Decision | Alternatives | Rationale | Traces |
|----|----------|--------------|-----------|--------|
| DD_01 | Deliver the MMSS as software only, installed onto the customers' existing, unchanged portable patient monitors and operating entirely within that platform's fixed processing, memory, and interface envelope; feasibility of the real-time budgets on this envelope is confirmed by early prototype evidence before full development commitment. | (a) New dedicated monitoring hardware shipped with the software; (b) hardware upgrade kits for the installed fleet; (c) offloading processing to a companion or cloud device. | Software-only delivery protects the customers' installed-base investment, unlocks that base as the sales channel, and avoids hardware production, logistics, and re-approval of fielded devices. The fixed envelope cannot be resized, so the decision is gated on early platform performance confirmation rather than assumed headroom. | BR_06, BR_09, UC_12 |
| DD_02 | Source the diagnostic capability as a commercially validated, off-the-shelf AI diagnostic engine, integrated without modification of its validated behaviour; no custom-developed or retrained diagnostic model in the first release. | (a) Develop a proprietary diagnostic model in-house; (b) license a model and retrain/tune it on own data; (c) rule-based (non-AI) decision-support logic. | Reusing a clinically validated component shortens time-to-market and the clinical-evidence burden, and de-risks regulatory clearance of the diagnostic claim; any modification would void the supplier's validation and forfeit that benefit. Supplier contracts must secure validation-evidence access, change notification, and continuity for the committed service period. | BR_07, BR_08, BR_10, UC_03 |
| DD_03 | Allocate the two-minute diagnostic convergence budget entirely to the AI diagnostic engine; the measurement-acquisition-and-display chain carries its own independent sub-second presentation and alarm budgets and is never gated on diagnostic processing. | (a) One shared end-to-end timing budget spanning acquisition, diagnosis, and display; (b) convergence deadline owned and enforced by the display chain. | Separate budget ownership keeps each timing claim architecturally clean and independently verifiable: vital-signs display and alarming stay sub-second regardless of diagnostic load, and the two-minute figure becomes a bounded, labelled claim on the diagnostic capability alone rather than an entangled system property. | UC_02, UC_03, BR_21 |
| DD_04 | Ground the IEC 62304 safety-classification reduction (class C to class B) on two risk mitigations demonstrably independent of the MMSS: each measurement device's own audible alarm annunciation, and the AI diagnostic engine's audible self-notification when its two-minute convergence budget expires. | (a) Accept class C development rigour for the whole software; (b) build a redundant alarm/watchdog channel inside the MMSS software; (c) add dedicated external watchdog hardware. | Both mitigation mechanisms already exist outside the MMSS, so independence does not rest on new development; a software-internal redundant channel would not be independent and could not support the reduction, while full class C rigour would escalate development and documentation effort disproportionately. The rationale is documented as a formal, evidence-linked justification agreed early with the authority. | BR_02, BR_03, UC_03, UC_04, UC_07 |
| DD_05 | Integrate exactly six enumerated measurement device types (ECG monitor, pulse oximeter, blood pressure monitor, thermal probe, capnometer, EEG monitor), each over its published standard interface governed by a per-device interface control document; no open device-framework in the first release. | (a) Open plug-and-play framework accepting arbitrary compliant devices; (b) proprietary own-brand sensor line; (c) a reduced modality set. | A fixed, bounded device set over published interfaces makes integration and verification effort predictable, keeps measurement-accuracy liability with the source devices, and caps service and training scope; supplier contracts bind interface stability and change notification so third-party changes cannot silently invalidate the integration. | BR_09, BR_10, UC_01, UC_02, UC_06 |
| DD_06 | Realise the HIS connection as a recognised HL7/FHIR-class interoperability interface; the specific protocol and interface specification are deferred but bounded to that standard class, and are agreed with reference customers and frozen before any dependent design commitment. | (a) Commit to one specific protocol immediately; (b) proprietary point-to-point hospital interfaces; (c) omit HIS integration from the first release. | Standards-based exchange is a tender requirement and avoids per-hospital custom integration projects; committing to a specific protocol before reference-customer alignment risks an early wrong choice, while a proprietary interface would be a supportability and lock-in dead end. The bounded deferral converts an open risk into a scheduled decision. | BR_06, BR_23, UC_08 |
| DD_07 | Adopt an IEC 60601-1-8-conformant alarm scheme for all annunciation: priority-encoded audible and visual clinical alarms distinguishable by sound alone, and technical alarms clearly distinct from clinical alarms in tone and presentation. | (a) Legacy proprietary alarm semantics carried over from earlier products; (b) simplified single-priority alarming; (c) visual-only alarm indication. | Alarm-standard conformity is mandatory for market access and represents the accepted state of the art for alarm safety and alarm-fatigue control; standard semantics are already familiar to clinical staff, reducing training burden and misinterpretation risk across all care settings. | BR_11, UC_04, UC_06 |
| DD_08 | Start monitoring automatically: the software boots directly into monitoring with safe default settings and zero required configuration, each parameter channel going live independently within seconds of its sensor being attached, with a positive per-parameter "measuring" indication. | (a) Guided start-up wizard with patient/profile entry; (b) profile selection before monitoring starts; (c) manual per-channel activation. | In emergency use, every interaction before measurement costs patient time; auto-start with safe defaults removes navigation errors and keeps hands and attention on the patient. The residual state-ambiguity hazard is controlled by the positive per-parameter measuring indication rather than by adding interaction. | BR_21, UC_01 |
| DD_09 | Provide simulation-based training as a mode of the operational software itself — with global unmistakable simulation marking, hard isolation of simulated data from HIS transmission and clinical logs, and automatic blocking when a real sensor delivers patient data — rather than as a separate trainer product. | (a) Standalone trainer device or separate training software; (b) classroom/e-learning materials only; (c) supplier-hosted remote simulator. | Training on the identical software and interface used in live care is inherently realistic and reuses the operational platform, avoiding a second product variant to develop, verify, and maintain; the confusion hazard this creates is controlled by the marking, isolation, and real-sensor interlock rather than by product separation. | BR_17, UC_09, UC_10 |
| DD_10 | Record all safety-relevant runtime behaviour — measurements, alarms, limit changes, diagnostic outputs, user actions, updates, and break-glass accesses — in an on-device timestamped event log operated under a governed retention policy sized to the embedded storage envelope. | (a) Continuous streaming of events to the HIS or a central server as the primary record; (b) minimal fault-only logging; (c) unbounded local retention. | Reconstructability is required for incident investigation, handover, audits, and liability defence, and mobile/pre-hospital use offers no guaranteed connectivity, so the authoritative record must live on the device; retention, extraction, and the personal-data status of log content are governed decisions aligned with data-protection obligations, not improvised at the first incident. | BR_14, BR_25, UC_11, UC_13 |
| DD_11 | Enforce a software-update interlock: installation is hard-blocked and never auto-starts while any patient or sensor connection is active, and a refused update states the cause and the recommended deferral action. | (a) Centrally scheduled forced updates across the fleet; (b) updating with a temporary reduced-monitoring fallback mode; (c) unrestricted manual updates at the engineer's discretion. | An update-induced monitoring gap is silent to the clinical team and clinically unacceptable; the interlock makes the committed security-and-maintenance update service deliverable to fielded units without ever trading it against active patient monitoring, and the explanatory refusal prevents the safeguard being fought as a fault. | BR_13, BR_18, UC_12 |
| DD_12 | Apply a two-tier security model: live monitoring, display, and alarming are never placed behind authentication; protected functions (data transmission, stored records, configuration) require authorised access, with an audit-logged break-glass path for emergency access without normal credentials. | (a) Full authentication in front of all device functions; (b) no access control on the device, relying on physical ward security; (c) break-glass without audit logging. | This reconciles the two non-negotiables — data-protection compliance and never delaying urgent care: bedside vitals and alarms remain instantly available while stored and transmitted data stay protected, and audit-logged break-glass is established healthcare security practice that preserves accountability for exceptional access. | BR_13, BR_14, UC_13 |
| DD_13 | Ship one single software variant, deployed unchanged across ICU, emergency room, and mobile/pre-hospital settings, with any setting-dependent limitations (such as absent HIS connectivity in mobile use) stated on the device in the active context. | (a) Setting-specific software variants or configurations per care environment; (b) feature-licensed editions unlocking capability per setting. | A single variant keeps verification, service, documentation, and training scope to one configuration and guarantees identical operation at every patient handover point; the on-device limitation statement keeps the cross-setting claim honest where connectivity genuinely differs, instead of fragmenting the product to hide it. | BR_09, BR_20, UC_12 |
---

# Development

## SOLUTION: Mobile Monitoring Software Solution (MMSS)

### External Interfaces

The points where the system connects to context elements, sub-systems, or other systems — connection type, data/signals exchanged, and protocols/standards.

At its external boundary the MMSS, treated as a black box, connects to ten context elements over defined digital interfaces, each governed by an Interface Control Document (ICD). Six device interfaces (IF_01–IF_06) are logical data connections over the host platform's device connectivity, through which the MMSS acquires the vital-sign parameters and signals enumerated in the Acquired Parameters / Signals table — ECG (heart rate, ECG waveform), SpO2/pulse rate, non-invasive blood pressure (systolic/diastolic/mean), body temperature, capnometry (etCO2, respiration rate), and EEG (waveform, cerebral indices) — each at an input rate of at least 0.1 Hz per the source device's published protocol. The display presentation interface (IF_07) carries the rendered monitoring picture — vital signs, waveforms, ranked diagnostic candidates, and alarm annunciations — to the monitor display per ICD-DISP-001. The AI diagnostic engine interface (IF_08) is a local API/library interface per ICD-AIE-001 over which the MMSS supplies acquired monitoring data and receives ranked diagnostic candidates as structured data. The HIS communication interface (IF_09) is a network interface for optional transmission of identity-labelled monitoring data to hospital information systems; its protocol is to be defined (ICD-HIS-001, HL7 or FHIR class, TBD). Finally, the host platform/OS services interface (IF_10) is the set of documented real-time operating system and platform services (scheduling, timing, storage, device and network access) per ICD-RTOS-001, within whose fixed resource envelope the MMSS must operate.

| Interface | Context Element | Type | Data Exchanged | Protocol / Standard |
|-----------|-----------------|------|----------------|---------------------|
| IF_01–IF_06 | ECG monitor, pulse oximeter, blood pressure monitor, thermal probe, capnometer, EEG monitor | Digital data input | Vital-sign parameters and waveforms per the Acquired Parameters / Signals table, plus device status | ICD-ECG-001, ICD-SPO2-001, ICD-NIBP-001, ICD-TEMP-001, ICD-CO2-001, ICD-EEG-001 |
| IF_07 | Monitor display | Digital presentation output | Vital signs, waveforms, ranked diagnostic candidates, alarm annunciations | ICD-DISP-001 |
| IF_08 | AI diagnostic engine | Local API/library exchange | Monitoring data out; ranked diagnostic candidates in (structured data) | ICD-AIE-001 |
| IF_09 | Hospital information system | Network data output | Identity-labelled monitoring data and diagnostic candidates for second opinion | ICD-HIS-001 — TBD (HL7 or FHIR class) |
| IF_10 | Host CPU platform | Software service interface | RTOS and platform services: scheduling, timing, storage, device/network access | ICD-RTOS-001 |

_To be added_

### Requirements

The full set of requirements the system must satisfy, derived from the user requirements and constrained by the context, regulatory requirements, and design decisions. Requirements are SMART and form the basis for verification.

#### Interface Requirements (RQ_IF_*)

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_IF_01 | The MMSS shall communicate with each of the six measurement devices in full conformance with that device's Interface Control Document (ICD-ECG-001, ICD-SPO2-001, ICD-NIBP-001, ICD-TEMP-001, ICD-CO2-001, ICD-EEG-001). | ICD conformance is the contractual boundary with the unchanged third-party devices; deviation would produce undefined data behaviour at a safety-relevant input. | High | IF_01, IF_02, IF_03, IF_04, IF_05, IF_06 |
| RQ_IF_02 | The MMSS shall acquire, over the interfaces assigned in the Acquired Parameters / Signals table, every parameter and signal enumerated in that table, and no acquisition of a listed parameter shall be omitted while its source device is connected and delivering. | The enumerated parameter set is the complete physiological input on which display, alarming, and diagnostic support depend; a silently missing parameter invalidates the clinical picture. | High | IF_01, IF_02, IF_03, IF_04, IF_05, IF_06 |
| RQ_IF_03 | The MMSS shall acquire each vital-sign parameter and signal on IF_01 through IF_06 at an input rate of at least 0.1 Hz (at least one new value per 10 seconds) per parameter, whenever the source device delivers at that rate or faster per its ICD. | The 0.1 Hz minimum input rate is the specified freshness floor ensuring displayed values and diagnostic inputs are never staler than 10 seconds; the rate obligation is conditioned on device delivery, which the MMSS cannot control beyond the ICD. | High | IF_01, IF_02, IF_03, IF_04, IF_05, IF_06 |
| RQ_IF_04 | The MMSS shall detect the absence of data on any of the interfaces IF_01 through IF_06 that has a connected measurement device, and shall trigger a connection alarm when no data has been received on that interface for 5 seconds, the trigger occurring no earlier than 5.0 s and no later than 5.5 s after the last received data. | An undetected disconnected or silent measurement source is a hazardous silent failure; the 5-second inactivity threshold with a bounded trigger tolerance makes the connection alarm condition implementable and testable. | High | IF_01, IF_02, IF_03, IF_04, IF_05, IF_06 |
| RQ_IF_05 | The MMSS shall detect data received on IF_01 through IF_06 that violates the format, range, or validity rules of the applicable ICD, shall exclude such data from presentation and from transmission to the AI diagnostic engine, and shall annunciate a technical fault for the affected interface. | Malformed or out-of-range interface data must never be presented as a valid measurement or fed into diagnosis; rejection plus annunciation prevents decisions based on wrong data. | High | IF_01, IF_02, IF_03, IF_04, IF_05, IF_06, IF_08 |
| RQ_IF_06 | The MMSS shall present all vital signs, waveforms, ranked diagnostic candidates, and alarm annunciations to the monitor display exclusively via IF_07, in conformance with ICD-DISP-001. | The display is the sole visual channel to the clinician; conformant presentation over the defined interface guarantees the clinical picture is rendered completely and correctly. | High | IF_07 |
| RQ_IF_07 | The MMSS shall transmit the acquired vital-sign parameters and signals to the AI diagnostic engine via IF_08 in the data format defined in ICD-AIE-001. | The diagnostic capability depends on the engine receiving the complete, correctly formatted physiological input; the ICD defines the validated exchange with the off-the-shelf engine. | High | IF_08 |
| RQ_IF_08 | The MMSS shall receive the ranked diagnostic candidates from the AI diagnostic engine via IF_08 as structured data conforming to ICD-AIE-001, in which each candidate's identity, rank, and likelihood ordering are machine-readable fields. | Structured, machine-readable candidates allow the MMSS to present ranked guidance unambiguously and keep interpreted output distinguishable from measured data. | High | IF_08 |
| RQ_IF_09 | The MMSS shall exchange monitoring data with the hospital information system via IF_09 using a recognised health-informatics interoperability standard of the HL7/FHIR class, in conformance with ICD-HIS-001; the selection between HL7 v2.x and HL7 FHIR is an open decision that shall be closed and released in ICD-HIS-001 before the IF_09 design is frozen. | Standards-based exchange is required for hospital integration without custom interface projects; the unresolved protocol choice is a gating dependency for IF_09 implementation and must be closed in ICD-HIS-001, not discovered during coding. | Medium | IF_09 |
| RQ_IF_10 | The MMSS shall label all data transmitted via IF_09 with the patient identity, the source device identity, and a marking that distinguishes measured values from AI-derived diagnostic candidates. | Identity labelling prevents wrong-patient association at the receiving hospital, and the measured-versus-interpreted marking preserves the adjunctive status of AI output beyond the point of care. | Medium | IF_09 |
| RQ_IF_11 | The MMSS shall use only the operating system and platform services documented in ICD-RTOS-001 when executing on the host CPU platform. | Restricting the MMSS to documented platform services keeps its behaviour defined and verifiable on the fixed, unchanged host platform and prevents dependence on undocumented behaviour. | High | IF_10 |
| RQ_IF_12 | The MMSS shall perform all of its interface communication on IF_01 through IF_09 using the connectivity, processing, memory, and storage resources available within the fixed resource envelope of the host CPU platform as declared in ICD-RTOS-001, without requiring any modification of the platform. | The software-only proposition rests on the unchanged installed base; interface operation must fit the fixed platform envelope or the deployment claim fails. | High | IF_10, IF_01, IF_02, IF_03, IF_04, IF_05, IF_06, IF_07, IF_08, IF_09 |

#### Functional Requirements (RQ_FN_*)

What the system must do — its functions, features, and behaviors. Each traces back to a use case or user requirement.

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_FN_01 | The MMSS shall, on power-on, start directly into monitoring operation with the released default configuration (default alarm limits and default display layout), requiring no user interaction or configuration, and shall be ready to acquire and display measurements within 10 seconds of power-on. If start-up does not complete, the MMSS shall annunciate the failure audibly and visually and shall never indicate an active monitoring state that has not been reached. | In emergency response every interaction before measurement costs patient time; a silent start-up failure would leave the patient believed-monitored but unmonitored. Naming the released default configuration makes "safe defaults" a verifiable artefact rather than a judgement call. | High | UC_01, UR_11 |
| RQ_FN_02 | The MMSS shall acquire each parameter independently as soon as its measurement device delivers a signal, without waiting for any other sensor, and shall display that parameter's value within 1 second of acquisition, together with a positive per-parameter "measuring" indication that is shown only while valid data is being acquired. | Sensors are applied one by one under time pressure; per-channel go-live with a positive measuring indication confirms correct placement immediately and prevents a false belief that a channel is live. | High | UC_01, UR_04 |
| RQ_FN_03 | The MMSS shall continuously and simultaneously display the current values, and waveforms for the signals designated as waveforms in the Acquired Parameters / Signals table, of all parameters enumerated in that table, refreshing the displayed values at an update interval of at most 1 second, with no user interaction required to bring any parameter into view. Intermittently measured parameters shall be displayed with the time of their last measurement and never presented as continuous. | The clinician must assess the complete physiological picture at a glance at any moment; hidden or seemingly-continuous intermittent values would misrepresent the patient's current state. Designating waveforms in the enumerated table removes guesswork about which signals require waveform rendering. | High | UC_02, UR_01 |
| RQ_FN_04 | The MMSS shall forward the acquired monitoring data of all live parameters enumerated in the Acquired Parameters / Signals table to the AI diagnostic engine continuously while monitoring is active, and shall display the ranked diagnostic candidates within 1 second of their receipt from the AI diagnostic engine, positioned alongside and never obscuring the live vital signs. The MMSS's contribution to end-to-end diagnostic latency shall be limited to this uninterrupted forwarding and the 1-second presentation budget; the 2-minute convergence budget from valid signals to ranking is owned by the AI diagnostic engine per RQ_CS_06. | Diagnostic direction must arrive while it can still influence time-critical decisions inside the golden hour, without displacing the primary vital-signs view; the MMSS can only be verified against its own forwarding and presentation obligations, not against the engine's convergence performance. | High | UC_03, UR_02, UR_05 |
| RQ_FN_05 | The MMSS shall present two visually and structurally distinct diagnostic states — "still converging" and "cannot converge" — and shall replace the converging state with an explicit cannot-converge notice, including the indication to proceed on clinical assessment, within 1 second of receiving the AI diagnostic engine's convergence-timeout annunciation via IF_08. If neither diagnostic candidates nor a convergence-timeout annunciation have been received via IF_08 by 130 seconds (the 2-minute convergence budget plus a 10-second tolerance) after the connected sensors began delivering valid signals, the MMSS shall itself present the cannot-converge notice no later than that bound. | The clinician must instantly know whether to wait for a result or fall back on clinical judgment alone; the bounded self-detection guarantees the notice appears even when the engine fails silently and never annunciates its own timeout. | High | UC_03, UR_06 |
| RQ_FN_06 | The MMSS shall mark every AI-derived diagnostic candidate as adjunctive interpretation, visibly distinct from measured values, in every representation in which a candidate appears: on the display, in every event-log entry containing a candidate, and in every data set transmitted to the HIS. No diagnostic candidate shall ever be presented, logged, or exported without this marking. | Interpreted output mistaken for a measurement or confirmed diagnosis is a critical misuse hazard and an AI-legislation transparency obligation; the marking must survive logging and export, not only display. | High | UC_03, UC_08, UR_03 |
| RQ_FN_07 | The MMSS shall generate a clinical alarm whenever a monitored vital sign violates its active alarm limit, with prioritised visual and audible annunciation conforming to IEC 60601-1-8, the alarm priority distinguishable by sound alone, and the alarm displayed within 1 second of detection of the limit violation. | Immediate, priority-encoded alarming lets the clinician react to the most urgent condition first, even without line of sight to the screen; naming the standard makes the annunciation characteristics implementable without interpretation. | High | UC_04, UR_07 |
| RQ_FN_08 | The MMSS shall allow adjustment of clinical alarm limits per parameter only within predefined clinically safe bounds, shall reject any entry outside those bounds or with high/low limits transposed while retaining the prior limits, shall keep the active limits and their deviation from defaults visible at the parameter at all times, and shall reset all alarm limits to safe defaults on admission of a new patient. | Patient-specific alarming reduces nuisance alarms, but unsafe, hidden, or carried-over limits are a direct patient-harm path that the system itself must exclude. | High | UC_05, UR_08 |
| RQ_FN_09 | The MMSS shall provide alarm acknowledgement scoped to exactly one alarm per user action: acknowledgement shall silence only the audible annunciation of the selected alarm for a fixed period of at most 120 seconds with automatic reactivation while the alarm condition persists, shall maintain a persistent visual indication of the silenced state, and shall leave every other active alarm annunciating unchanged. | Unscoped or permanent silencing during overlapping alarms is a known critical use error; a bounded, per-alarm silence period consistent with IEC 60601-1-8 audio-pause conventions preserves triage while controlling alarm fatigue and is directly testable. | High | UC_04, UR_07 |
| RQ_FN_10 | The MMSS shall detect, per channel, sensor misplacement, sensor disconnection, and stale or frozen data (no new valid value within the parameter's expected delivery interval per its ICD), and shall raise a technical alarm — distinct in tone and presentation from clinical alarms — that names the affected sensor or parameter and the fault type. A connection fault shall be triggered after 5 seconds without data from a connected measurement device (per the trigger tolerance of RQ_IF_04), and every technical alarm shall be displayed within 1 second of its trigger. | The clinician must never confuse a measurement problem with a change in the patient's condition, and must be able to correct the right sensor immediately; anchoring staleness detection to the per-parameter ICD delivery interval makes the detection criterion implementable per channel. | High | UC_06, UR_09 |
| RQ_FN_11 | The MMSS shall visually invalidate, within 1 second of detection, any displayed value that is stale, frozen, or originating from a faulted channel, such that it cannot be read as a current measurement, and shall never display an unmarked last-known value as current. A value shall be restored as current only when a valid signal is delivered again. | A frozen number is indistinguishable from a stable patient; unmarked stale data leads to clinical decisions on outdated physiology. | High | UC_06, UR_09 |
| RQ_FN_12 | The MMSS shall detect internal failures of its monitoring or diagnostic functions by cyclic self-checks with a period of at most 5 seconds, annunciate each detected failure audibly and visually within 1 second of detection — bounding the maximum time from failure occurrence to annunciation at 6 seconds — explicitly indicate which functions remain reliable and which are unavailable, and suppress the outputs of unreliable functions rather than displaying them. | The system must never fail silently: the clinician needs to know both that a failure occurred and exactly what can still be trusted; the fixed self-check period makes the failure-to-annunciation time bounded and objectively verifiable by fault injection. | High | UC_07, UR_10 |
| RQ_FN_13 | The MMSS shall transmit the current monitored parameters (as enumerated in the Acquired Parameters / Signals table), stored trend data, and ranked diagnostic candidates to the hospital information system over the standard healthcare interface, forwarding diagnostic candidates within 1 second of their receipt from the AI diagnostic engine, and shall require explicit confirmation of the displayed patient identifiers before any transmission; on cancellation or identity mismatch, zero data shall leave the device, and every transmission shall be labelled with source device and timestamp. | Remote second opinion requires the complete live picture in the correct patient record; wrong-record transmission is a persistent patient-safety error the system must actively block. "Stored trend data" bounds the transmitted history to what is retained on-device per RQ_NF_11, removing the ambiguity of "recent". | High | UC_08, UR_14, UR_18 |
| RQ_FN_14 | The MMSS shall provide a simulation training mode that replays realistic patient scenarios on the clinical interface, in which every screen, overlay, and log entry carries an unmistakable global simulation marking for its entire duration; simulated data shall never be transmitted to the HIS nor recorded as real patient data, and if a real sensor delivers patient data while simulation is active, the MMSS shall block the real data from being displayed as monitoring, annunciate the conflict, and require an explicit simulation-exit decision. | Realistic training is only safe if simulated data can never be mistaken for, mixed with, or displace real patient data — for participants and unbriefed bystanders alike. | High | UC_09, UR_15 |
| RQ_FN_15 | The MMSS shall record completion of each simulation training scenario per identified user, per scenario, with the completion date, shall record no completion for a scenario the user did not complete, and shall make the completion records retrievable on demand as evidence. | Training completion is a risk-control measure whose effectiveness must be demonstrable to employers and auditors; incomplete training must be visible, not silently absent. | High | UC_10, UR_16 |
| RQ_FN_16 | The MMSS shall record measurements, clinical and technical alarms (including onset, acknowledgement, and resolution), alarm-limit changes, diagnostic outputs, and user actions in an event log with timestamps derived from a single system clock at a resolution of 1 second or finer, presented in chronological order; any interruption of logging shall be explicitly marked as a gap in the timeline and never silently omitted. | A complete, unambiguous timestamped record is the basis for shift handover, incident reconstruction, and the manufacturer's post-market and liability obligations; a single clock source is what makes the timestamps mutually consistent by construction. | High | UC_11, UR_17 |
| RQ_FN_17 | The MMSS shall refuse to start a software update, and shall never start one automatically, while any patient or sensor connection is active; a refused update shall state the cause and the recommended deferral action, and every installed update shall be recorded in the event log with its version. | An update-induced monitoring gap is silent to the clinical team and clinically unacceptable; an unexplained refusal would be fought as a fault instead of respected as a safeguard. | High | UC_12, UR_19 |
| RQ_FN_18 | The MMSS shall provide live monitoring, display, and alarm functions without any authentication step, shall protect stored and transmitted patient data and protected functions behind authorised access, shall refuse and log every unauthorised access attempt without affecting live monitoring, and shall provide a break-glass emergency access path to protected functions without normal credentials that is automatically recorded in the audit log. | Data-protection compliance must never delay urgent care; audit-logged break-glass access reconciles emergency availability with accountability for exceptional access. | High | UC_13, UR_18 |
| RQ_FN_19 | The MMSS shall provide identical appearance, alarm behaviour, and operation as one software variant across ICU, ER, and mobile (ambulance) deployment settings, and shall state any active setting-dependent limitation on-device, in the context where it applies, within 5 seconds of the limitation condition becoming active. | One variant with identical behaviour eliminates retraining and setting-specific use errors when staff and patients move between contexts; on-device statement of active limitations keeps users aware of exactly what the system cannot do here and now. | High | UC_12, UR_12 |
| RQ_FN_20 | The MMSS shall present all on-device operating guidance, labels, and corrective-action instructions during clinical operation in the configured target-market language, which shall be selected and verified at installation; no clinical-operation text shall be presented in any other language. | Clinical staff act fastest and most safely on instructions in their own language; installation-time selection and verification guarantees the correct language is locked in before first clinical use. | High | UR_21 |

#### Performance Requirements (RQ_PR_*)

Quantitative requirements on how well the system performs its functions: response times, throughput, accuracy, capacity, availability.

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_PR_01 | The MMSS shall be ready to acquire and display measurements within 10 seconds of power application to the host platform, measured until the MMSS positively indicates monitoring readiness; the host platform's boot time as characterised in ICD-RTOS-001 forms a fixed part of this budget, and the MMSS's own initialisation shall fit within the remainder. | In emergency response the golden hour starts at patient contact; a bounded, verifiable activation time guarantees monitoring capability is available within seconds of arrival. Making the platform-boot share explicit exposes the MMSS's actual initialisation budget instead of hiding it inside a figure the software only partly controls. | High | RQ_FN_01 |
| RQ_PR_02 | The MMSS shall display each acquired vital-sign value within 1 second, end-to-end, from its acquisition at the measurement-device interface until it is visible on the monitor display, for every parameter enumerated in the Acquired Parameters / Signals table, including under the full-load condition defined in RQ_PR_09. | The clinician acts on the displayed value as the patient's current state; a bounded end-to-end latency at the system boundary keeps the display clinically real-time regardless of internal processing stages, and referencing the defined full-load condition replaces the unverifiable "all monitoring conditions". | High | RQ_FN_02, RQ_FN_03 |
| RQ_PR_03 | The MMSS shall display every clinical alarm annunciation within 1 second of detection of the alarm condition. | Alarm reaction time directly determines intervention time on a deteriorating patient; the 1-second display budget makes the alarm path verifiably immediate. | High | RQ_FN_07 |
| RQ_PR_04 | The MMSS shall trigger a connection alarm after 5 seconds without data from a connected measurement device — the trigger occurring no earlier than 5.0 s and no later than 5.5 s after the last received data — and shall display that alarm within 1 second of the trigger, yielding a worst-case 6.5 seconds from last received data to visible annunciation. | A silent measurement source is a hazardous hidden failure; "exactly 5 seconds" is not implementable on a real scheduler, so a bounded trigger tolerance makes the maximum unnoticed-loss interval both achievable and testable at the system boundary. | High | RQ_FN_10 |
| RQ_PR_05 | The MMSS shall display received ranked diagnostic candidates within 1 second of their receipt from the AI diagnostic engine. | Diagnostic guidance loses value with every second inside the golden hour; the presentation budget ensures the MMSS adds no perceptible delay to the engine's result. | High | RQ_FN_04 |
| RQ_PR_06 | The MMSS shall forward ranked diagnostic candidates to the hospital information system within 1 second of their receipt from the AI diagnostic engine, whenever HIS transmission is active and confirmed. | A remote second opinion is only useful if it sees the same picture at the same time as the bedside; the forwarding budget keeps the remote view synchronous with the local one. | Medium | RQ_FN_13 |
| RQ_PR_07 | The MMSS shall support the AI diagnostic engine's 2-minute convergence budget — owned entirely by the engine per RQ_CS_06 — by delivering the acquired monitoring data to the engine continuously and without interruption, and shall make the ranked diagnostic candidates visible to the clinician no later than the engine's convergence budget plus the MMSS's 1-second presentation budget: a worst case of 2 minutes + 1 second from the connected sensors delivering valid signals. Any labelled time-to-diagnosis claim shall cite this combined 2-minute-plus-1-second figure. | The budget arithmetic must close at the clinician's eye: the engine owns the full 2 minutes (RQ_CS_06) and the MMSS adds up to 1 second of presentation, so the clinician-visible worst case is 2 minutes + 1 second; making the combined figure explicit — and requiring labelling to cite it — keeps the claim honest, verifiable at the system boundary, and bounded to the MMSS's own obligations. | High | RQ_FN_04, RQ_FN_05 |
| RQ_PR_08 | The MMSS shall sustain acquisition and processing of every vital-sign parameter enumerated in the Acquired Parameters / Signals table at an input rate of at least 0.1 Hz per parameter, with all six measurement devices connected and delivering simultaneously, without loss of any parameter's input and without any accepted value becoming staler than 10 seconds before processing. | The 0.1 Hz floor per parameter under full simultaneous load guarantees no displayed value or diagnostic input is ever staler than 10 seconds, even in the worst-case device configuration; stating the staleness bound makes "deferral" measurable. | High | RQ_FN_02, RQ_FN_03 |
| RQ_PR_09 | The MMSS shall sustain a display refresh interval of at most 1 second for all displayed vital-sign values under full load, defined as all parameters enumerated in the Acquired Parameters / Signals table live simultaneously from all six connected devices with active diagnostic candidates and active alarm annunciations. | The refresh guarantee must hold precisely when the clinical situation is most demanding; specifying it under full load makes the worst case, not the average case, the verified case. | High | RQ_FN_03 |
| RQ_PR_10 | The MMSS shall meet every timing budget specified in RQ_PR_01 through RQ_PR_09 without degradation while HIS transmission, event logging, or simulation-mode rendering is concurrently active. | Secondary functions must never steal time from the safety-relevant monitoring and alarm paths; requiring the budgets to hold under concurrent load makes the isolation verifiable at the system boundary. | High | RQ_FN_13, RQ_FN_14, RQ_FN_16 |

#### Non-Functional Requirements (RQ_NF_*)

How the system should behave rather than what it does: reliability, maintainability, security, privacy, scalability. Compliance, labeling, and training requirements live here too.

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_NF_01 | The MMSS shall be developed and maintained under a software lifecycle process compliant with IEC 62304 at software safety class B, with the technical file containing the initial class C assessment and the documented rationale for the reduction to class B based on demonstrably independent risk-control measures. | The notified body will not accept a reduced classification without an evidence-linked mitigation rationale; an unjustified reduction is a conformity-assessment rejection risk that surfaces late and expensively. | High | BR_02, RE_02 |
| RQ_NF_02 | The MMSS shall be supported by a risk management file compliant with ISO 14971 covering the entire product lifecycle, in which all identified hazards — including wrong or delayed diagnosis, undetected sensor misplacement, missed alarms, and undetected connection loss — are evaluated, controlled, and the residual risk documented as acceptable against the state of the art. | A complete, lifecycle-maintained risk management file is a legal precondition for market access and the foundation of the safety argument and the class B justification. | High | BR_03, RE_03 |
| RQ_NF_03 | The MMSS shall be supported by a usability engineering file compliant with IEC 62366-1, including a summative usability evaluation performed with representative trained medical professionals in each intended use environment (ICU, emergency room, and mobile/pre-hospital use), covering misinterpretation of AI diagnostic output as a use-related hazard. | Use error under time pressure is a dominant harm source in acute care; the authority requires validated evidence that safety-related interactions are safe in every claimed environment, not only in the laboratory. | High | BR_04, RE_04 |
| RQ_NF_04 | The MMSS shall conform to the applicable requirements of IEC 60601-1-8 for its physiological and technical alarm functions — including alarm prioritisation, alarm-signal characteristics, and indication of alarm and fault conditions — with conformity demonstrated by verification evidence in the technical file. | Alarm-standard conformity is mandatory for market access and the accepted state of the art for alarm safety and alarm-fatigue control in acute care. | High | BR_11, RE_07 |
| RQ_NF_05 | The MMSS shall be developed and maintained under a secure product lifecycle process compliant with IEC 81001-5-1, including a documented cybersecurity risk assessment, a vulnerability monitoring and management process, and security updates deliverable to fielded installations for the entire declared support period. | Networked medical software connected to clinical systems is a mandated attack-surface concern; regulators require lifecycle security that demonstrably reaches deployed units, not design-phase security alone. Naming the standard removes ambiguity about which lifecycle process is audited. | High | BR_13, RE_08 |
| RQ_NF_06 | The MMSS shall process patient health data in compliance with applicable data-protection law (GDPR/HIPAA class), including encryption of stored patient data using a published, non-deprecated algorithm of at least AES-128 strength, encryption of all patient data transmitted outside the device (TLS 1.2 or stronger equivalent), role-based access control to patient data, and audit logging of accesses to patient data. | Data-protection compliance is a legal obligation with severe penalties; naming minimum algorithm strength for storage as well as transport makes the encryption obligation implementable and verifiable, not aspirational. | High | BR_14, RE_09 |
| RQ_NF_07 | The MMSS shall achieve an availability of at least 99.9% of powered-on operating time for its monitoring and alarm functions, and shall detect any unresponsive software state by a watchdog mechanism independent of the monitored software path (using the host platform's watchdog facility per ICD-RTOS-001) and restore monitoring and alarm operation automatically within 30 seconds of detection. | The clinical claim rests on continuous availability during critical care; a quantified availability target with detected, bounded recovery makes reliability verifiable, and anchoring watchdog independence to the platform facility prevents a self-monitoring design that fails with the software it watches. | High | BR_22, RE_03 |
| RQ_NF_08 | The MMSS shall be updatable in the field by installation of a released software version within a planned service window of at most 60 minutes per device, without modification, recertification, or replacement of the host hardware platform. | The software-only proposition and the committed update service only hold if updates fit the fixed installed base and a rosterable clinical downtime window. | High | BR_09, BR_18 |
| RQ_NF_09 | The MMSS shall be delivered with compliant labelling, unique device identification, and instructions for use in the official languages of each target market, with the instructions for use stating the intended use, residual risks, the performance characteristics and limitations of the AI diagnostic function, and the training required before clinical use. | Labelling/UDI/IFU compliance is a legal placing-on-market condition, and truthful disclosure of AI limitations and training prerequisites is what makes the conditions for safe use enforceable. | High | BR_16, RE_12 |
| RQ_NF_10 | The MMSS shall record evidenced completion of the mandatory training per individual user, and these training-completion records shall be retained and retrievable for at least the committed support period and made available to the customer organisation. | Training is a risk-control measure; without retrievable completion records neither the manufacturer nor the customer can demonstrate to an authority that the control is effective in the field. | High | BR_17, RE_13 |
| RQ_NF_11 | The MMSS shall log measured data, diagnostic outputs, alarms, detected fault conditions, and user actions such that any clinical event sequence can be reconstructed after the fact, with logs retained per a governed log-retention policy of at least 30 days on-device and extractable for incident investigation and audit. | Reconstructability is required for vigilance, incident investigation, and liability defence; partial logs that omit the clinical event chain offer no evidential value. The 30-day on-device window must be sized against the fixed storage envelope declared in ICD-RTOS-001 — a hard feasibility dependency to be confirmed early. | High | BR_25, RE_11 |
| RQ_NF_12 | The MMSS shall comply with applicable AI legislation for high-risk AI systems, presenting AI-generated diagnostic candidates at all times visibly distinguished from measured values, subordinate to clinician judgement, and accompanied by accessible documentation of the AI function's performance characteristics and limitations. | AI transparency and human oversight are market-access conditions in key jurisdictions and the primary defence that diagnostic accountability remains with the treating professional. | High | BR_12, RE_06 |

#### Constraint Requirements (RQ_CS_*)

External constraints the system must respect: regulatory rules, applicable standards, imposed technology choices, environmental conditions.

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_CS_01 | The MMSS shall be qualified as a medical device and shall hold the applicable market clearance or approval (e.g. CE marking under EU MDR 2017/745, US FDA clearance) in each target market before being placed on that market. | Placing unqualified diagnostic-support software on the market is illegal; qualification and the correct conformity-assessment route are non-negotiable preconditions for sale. | High | RE_01 |
| RQ_CS_02 | The MMSS shall be developed under ANSI AAMI IEC 62304 as software safety class C mitigated to class B, and the mitigation rationale shall be maintained as a controlled record in the technical file for the life of the product. | The authority holds the manufacturer to the classification actually justified by the hazard analysis; the C-to-B reduction is only valid while its documented rationale and independent mitigations remain in force. | High | RE_02 |
| RQ_CS_03 | The MMSS shall, in its first release, obtain all diagnostic interpretation exclusively from a commercially available, clinically validated AI diagnostic engine integrated without modification of its validated behaviour; no custom-developed diagnostic model shall be used. | Modifying a validated component voids its validation evidence; the clinical-evidence strategy accepted for market access rests on the unmodified, pre-validated model. | High | RE_05 |
| RQ_CS_04 | The MMSS shall acquire physiological data exclusively from the six specified non-invasive measurement device types — ECG monitor, pulse oximeter, blood pressure monitor, thermal probe, capnometer, and EEG monitor — via their published standard interfaces. | The documented intended use and conformity claim are bounded to this enumerated device set; acquisition from unspecified sources would invalidate the approved operating principle. | High | RE_01 |
| RQ_CS_05 | The MMSS shall exchange data with hospital information systems exclusively over recognised health-informatics interoperability standards of the HL7/FHIR class, with the selected standard and interface specification documented in the technical file. | The authority requires documented, standards-based interfaces so clinical data shared for second opinions is complete, correctly interpreted, and traceable across the care chain. | High | RE_10 |
| RQ_CS_06 | The MMSS shall allocate the two-minute diagnostic convergence budget entirely to the AI diagnostic engine, which independently annunciates expiry of that budget; the MMSS shall not claim or consume any part of that budget in its own processing chain. | The convergence claim enters the labelling as a verifiable performance characteristic, and the independent timeout annunciation is a risk-control measure underpinning the class B justification. | High | RE_02, RE_05 |
| RQ_CS_07 | The MMSS shall execute on the existing compact embedded CPU platform with its real-time operating system, within the processing, memory, and interface capacity that platform provides, without any modification of the host hardware. | The conformity claim, intended use, and verification evidence are established against this fixed platform envelope; hardware modification would trigger re-assessment of the installed base. | High | RE_01, RE_11 |
| RQ_CS_08 | The MMSS shall subject every post-market modification — including any update to or replacement of the incorporated AI diagnostic engine — to a documented change-control process that assesses the significance of the change and completes any required re-validation or new conformity assessment before deployment to fielded units. | The device on the market must at all times correspond to the device that was approved; undocumented or unassessed changes, especially to the AI model, invalidate the certificate. | High | RE_14, RE_15 |

### Verification (SV_*)

The **BDD feature files** that verify the functional requirements, defined jointly by the 3-Amigos (Product Owner, Development Lead, Verification Lead). Write **one feature file per functional requirement** as a `gherkin` fenced block, tagged `@ID:RQ_FN_xx` to trace it to the requirement it verifies. Each feature has a user story (`As a … I want … So that …`), a `Rule:` that captures the requirement's "shall" statement, and one or more concrete `Scenario`s with `Given / When / Then` steps and data tables for the expected values. Use measurable outcomes (e.g. "within 5 seconds"). Every RQ_FN_* must have a feature file and every RQ_* must be covered by at least one scenario. The converter records each feature file as one row (`SV_*`) in the workbook's Verification table.

```gherkin
@ID:RQ_FN_01
Feature: Automatic Start into Monitoring
    As a pre-hospital professional I want the monitor to start directly into monitoring with safe defaults within 10 seconds
    So that no interaction stands between patient contact and live measurement

Rule: The MMSS shall, on power-on, start directly into monitoring with the released default configuration, requiring no user interaction, and be ready to acquire and display within 10 seconds; a failed start-up shall be annunciated and never shown as an active monitoring state.

Scenario: Power-on reaches monitoring readiness without interaction
    Given the patient simulator runs the default adult profile with no sensors connected
    When the harness applies power to the host platform and records the power-on timestamp
    Then the display test interface reports the monitoring screen with the released default configuration without any user input
    And the readiness indication appears no later than 10 seconds after the harness power-on timestamp (RQ_PR_01)

Scenario: Start-up failure is annunciated and never masked
    Given the platform stub is configured to abort MMSS start-up with error code STARTUP_FAIL
    When the harness applies power to the host platform
    Then the audio capture records the start-up failure tone and the display test interface reports the failure notice within 10 seconds of the harness power-on timestamp
    And the display test interface reports no "monitoring active" indication
```

```gherkin
@ID:RQ_FN_02
Feature: Independent Per-Parameter Go-Live
    As a pre-hospital professional I want each parameter to go live within 1 second of its own sensor delivering
    So that I can attach sensors in any order and trust each channel immediately

Rule: The MMSS shall acquire each parameter independently as soon as its device delivers a signal, display its value within 1 second of acquisition, and show a positive per-parameter "measuring" indication only while valid data is acquired.

Scenario: One sensor goes live without waiting for the others
    Given the MMSS is in monitoring with no sensors connected in the patient simulator
    When the SpO2 sensor is connected and the simulator delivers a valid 97 % signal, timestamped by the harness at the device interface
    Then the display test interface reports, within 1 second of that timestamp (RQ_PR_02)
    | parameter | value shown | measuring indication |
    | SpO2      | 97          | on                   |
    | ECG       | none        | off                  |
```

```gherkin
@ID:RQ_FN_03
Feature: Continuous Simultaneous Display of All Parameters
    As a bedside critical-care nurse I want all enumerated parameters and waveforms visible simultaneously, refreshed at least every second
    So that I can assess the complete physiological picture at a glance

Rule: The MMSS shall continuously and simultaneously display current values and designated waveforms of all enumerated parameters, refreshing at an interval of at most 1 second with no user interaction, and shall show intermittent parameters with the time of their last measurement.

Scenario: All parameters visible with bounded refresh and intermittent labelling
    Given all six measurement devices are connected and delivering per their device ICDs (RQ_IF_01, RQ_IF_02) in the patient simulator
    And one NIBP measurement has completed at a simulator-recorded time
    When the simulator ramps every continuous parameter for 60 seconds with harness-timestamped value changes at each channel's ICD rate of at least 0.1 Hz (RQ_IF_03)
    Then every enumerated parameter and designated waveform is reported visible via the Display Interface IF_07 (RQ_IF_06) by the display test interface without any user interaction
    And each displayed value change follows its harness-timestamped simulator change by at most 1 second
    And the NIBP value is shown with a last-measurement time equal to the simulator-recorded completion time

Scenario: Refresh and latency budgets hold under full concurrent load
    Given all six devices deliver at their maximum ICD rates of at least 0.1 Hz per channel (RQ_PR_08)
    And the AI-engine data stream and an identity-confirmed HIS transmission are active concurrently
    When the simulator ramps every continuous parameter for 300 seconds with harness-timestamped value changes
    Then each displayed value change follows its harness-timestamped simulator change by at most 1 second (RQ_PR_10)
    And the display test interface reports a refresh interval of at most 1 second for every parameter throughout the 300 seconds (RQ_PR_09)
```

```gherkin
@ID:RQ_FN_04
Feature: Diagnostic Candidate Forwarding and Presentation
    As an emergency physician I want ranked diagnostic candidates displayed within 1 second of the engine's result, alongside the vitals
    So that diagnostic direction arrives without displacing the primary monitoring view

Rule: The MMSS shall forward acquired monitoring data of all live parameters to the AI diagnostic engine continuously while monitoring is active, and shall display received ranked candidates within 1 second of receipt, alongside and never obscuring the live vital signs.

Scenario: Candidates from the stubbed engine are shown within 1 second beside the vitals
    Given all six devices are delivering in the patient simulator
    And the stubbed AI diagnostic engine confirms receipt of an ICD-conformant continuous data stream (RQ_IF_07) with no gap exceeding the ICD-defined interval across a 2-minute convergence window (RQ_PR_07)
    When the stub returns the structured ranked list "1. sepsis 0.71, 2. pneumonia 0.45" (RQ_IF_08), timestamped by the harness at IF_08
    Then the display test interface reports both candidates in rank order within 1 second of the IF_08 timestamp (RQ_PR_05)
    And the display test interface reports no overlap between the candidate area and any of the six parameter value areas
```

```gherkin
@ID:RQ_FN_05
Feature: Converging and Cannot-Converge Diagnostic States
    As an emergency physician I want an unmissable cannot-converge notice within 1 second of the engine's timeout
    So that I know instantly whether to wait or proceed on clinical judgement alone

Rule: The MMSS shall present visually and structurally distinct "still converging" and "cannot converge" states, replacing the converging state with an explicit cannot-converge notice, including the indication to proceed on clinical assessment, within 1 second of the engine's timeout annunciation via IF_08; when neither candidates nor a timeout annunciation are received via IF_08, the MMSS shall itself present the notice no later than 130 seconds after the connected sensors began delivering valid signals.

Scenario: Engine timeout annunciation replaces the converging state
    Given the stubbed AI engine has placed the MMSS in the "still converging" display state
    When the stub sends the convergence-timeout annunciation on IF_08, timestamped by the harness
    Then the display test interface reports the cannot-converge notice with the proceed-on-clinical-assessment indication, replacing the converging state, within 1 second of the IF_08 timestamp

Scenario: Unresponsive engine yields the self-detected cannot-converge notice within the bound
    Given the connected sensors began delivering valid signals at a harness-timestamped start
    And the MMSS shows the "still converging" state
    When the stubbed AI engine stops responding on IF_08 and sends neither candidates nor a timeout annunciation
    Then the display test interface reports the cannot-converge notice no later than 130 seconds after the harness-timestamped start of valid signals
    And the event log records the engine non-response detection event
```

```gherkin
@ID:RQ_FN_06
Feature: Adjunctive Marking of Diagnostic Candidates
    As an emergency physician I want every AI candidate marked as adjunctive in every representation
    So that interpreted output is never mistaken for a measured value or confirmed diagnosis

Rule: The MMSS shall mark every AI-derived diagnostic candidate as adjunctive interpretation, visibly distinct from measured values, on the display, in every event-log entry containing a candidate, and in every data set transmitted to the HIS; no candidate shall appear anywhere without this marking.

Scenario: Adjunctive marking present in display, log, and HIS export
    Given the stubbed AI engine has delivered the ranked candidates "sepsis 0.71" and "pneumonia 0.45" to the monitoring MMSS
    And an identity-confirmed transmission to the stubbed HIS endpoint is active
    When the candidate list is displayed, logged, and transmitted
    Then the defined adjunctive-interpretation marking is verified present for every candidate in each representation
    | representation        | verified via           |
    | Display Interface     | display test interface |
    | event-log entry       | log retrieval          |
    | HIS transmission data | HIS stub capture       |
```

```gherkin
@ID:RQ_FN_07
Feature: Clinical Alarm on Limit Violation
    As a bedside critical-care nurse I want a prioritised alarm within 1 second of a limit violation, distinguishable by sound alone
    So that I react to the most urgent condition first even without line of sight to the screen

Rule: The MMSS shall generate a clinical alarm whenever a monitored vital sign violates its active alarm limit, with prioritised visual and audible annunciation conforming to IEC 60601-1-8, priority distinguishable by sound alone, displayed within 1 second of detection.

Scenario: Heart-rate limit violation raises a high-priority alarm within 1 second
    Given the MMSS is monitoring with the active heart-rate upper alarm limit at 120 bpm
    When the patient simulator steps the heart rate from 100 to 140 bpm, timestamped by the harness at the device interface
    Then the display test interface reports the heart-rate clinical alarm within 1 second of the harness step timestamp (RQ_PR_03)
    And the audio capture matches the IEC 60601-1-8 high-priority burst pattern
```

```gherkin
@ID:RQ_FN_08
Feature: Safe Adjustment of Alarm Limits
    As an intensivist I want limit changes bounded to safe values, always visible, and reset for a new patient
    So that alarming fits the patient without unsafe, hidden, or carried-over settings

Rule: The MMSS shall allow alarm-limit adjustment per parameter only within predefined clinically safe bounds, reject out-of-bounds or transposed entries while retaining the prior limits, keep active limits and their deviation from defaults visible at the parameter, and reset all limits to safe defaults on admission of a new patient.

Scenario: Valid limit change is applied and shown at the parameter
    Given the MMSS is monitoring with default heart-rate limits of 50 and 120 bpm
    When the user commits a lower heart-rate limit of 45 bpm within the safe bounds
    Then the active limits shown at the heart-rate parameter are 45 and 120 bpm with a non-default deviation cue

Scenario: Out-of-bounds entry is rejected and prior limits retained
    Given the MMSS is monitoring with active heart-rate limits of 50 and 120 bpm and a predefined safe lower bound of 30 bpm
    When the user enters a lower heart-rate limit of 20 bpm
    Then the entry is rejected with the safe bounds stated in the rejection message
    And the active limits remain 50 and 120 bpm

Scenario: Transposed limit entry is rejected and prior limits retained
    Given the MMSS is monitoring with active heart-rate limits of 50 and 120 bpm
    When the user enters a lower heart-rate limit of 130 bpm and an upper heart-rate limit of 50 bpm
    Then the entry is rejected with the transposition stated in the rejection message
    And the active limits remain 50 and 120 bpm

Scenario: New patient admission resets all limits to the released safe defaults
    Given the MMSS is monitoring with the lower heart-rate limit changed to 45 bpm
    When the user admits a new patient
    Then the active limits shown at every parameter equal the released safe defaults
    And the active heart-rate limits shown are 50 and 120 bpm with no deviation cue
```

```gherkin
@ID:RQ_FN_09
Feature: Per-Alarm Scoped Acknowledgement
    As a bedside critical-care nurse I want acknowledgement to silence only the selected alarm for a bounded period
    So that overlapping alarms are never silenced wholesale and nothing stays muted while its condition persists

Rule: The MMSS shall scope acknowledgement to exactly one alarm per user action, silencing only that alarm's audible annunciation for at most 120 seconds with automatic reactivation while the condition persists, maintaining a persistent visual silenced indication, and leaving every other active alarm annunciating unchanged.

Scenario: Acknowledging one of two alarms leaves the other annunciating and reactivates in time
    Given two clinical alarms are active from the patient simulator
    | alarm             | priority |
    | heart rate high   | high     |
    | SpO2 low          | medium   |
    When the user acknowledges the SpO2 low alarm and its condition persists
    Then only the SpO2 audible annunciation stops and a persistent silenced indication is shown
    And the heart-rate alarm continues annunciating unchanged
    And the SpO2 audible annunciation reactivates within 120 seconds
```

```gherkin
@ID:RQ_FN_10
Feature: Technical Alarm for Sensor Fault and Stale Data
    As a bedside critical-care nurse I want measurement problems alarmed distinctly, naming the sensor and fault
    So that I never confuse a sensor fault with a patient change and can correct the right sensor immediately

Rule: The MMSS shall detect, per channel, sensor misplacement, disconnection, and stale or frozen data, and raise a technical alarm — distinct in tone and presentation from clinical alarms — naming the affected sensor or parameter and fault type; a connection fault triggers after 5 seconds without data (trigger 5.0–5.5 s) and every technical alarm is displayed within 1 second of trigger.

Scenario: Disconnected SpO2 sensor raises a named technical alarm within bounds
    Given all six devices are connected and delivering in the patient simulator
    When the SpO2 sensor is disconnected in the simulator, with the last SpO2 sample timestamped by the harness at the device interface
    Then the event log records the SpO2 connection-fault trigger 5.0 to 5.5 s after that timestamp (RQ_IF_04)
    And the display test interface reports a technical alarm naming SpO2 and "sensor disconnected" within 1 second of the logged trigger (RQ_PR_04)
    And the audio capture matches the technical-alarm tone pattern and no clinical-priority pattern

Scenario: Misplaced temperature sensor raises a named technical alarm
    Given all six devices are connected and delivering in the patient simulator
    When the simulator delivers the misplacement signature on the temperature channel, timestamped by the harness at the device interface
    Then the event log records the temperature misplacement-fault trigger
    And the display test interface reports a technical alarm naming the temperature sensor and "sensor misplaced" within 1 second of the logged trigger (RQ_PR_04)
    And the audio capture matches the technical-alarm tone pattern and no clinical-priority pattern

Scenario: Stale ECG channel raises a named technical alarm
    Given all six devices are connected and delivering in the patient simulator
    When the simulator stops delivering ECG samples beyond the channel's ICD delivery interval (RQ_IF_04), with the last ECG sample timestamped by the harness
    Then the event log records the ECG stale-data trigger
    And the display test interface reports a technical alarm naming ECG and "stale data" within 1 second of the logged trigger (RQ_PR_04)
    And the audio capture matches the technical-alarm tone pattern and no clinical-priority pattern
```

```gherkin
@ID:RQ_FN_11
Feature: Visual Invalidation of Untrustworthy Values
    As a bedside critical-care nurse I want stale or faulted values made unreadable as current measurements
    So that I never base a clinical decision on outdated physiology

Rule: The MMSS shall visually invalidate, within 1 second of detection, any displayed value that is stale, frozen, or from a faulted channel so it cannot be read as current, shall never display an unmarked last-known value as current, and shall restore a value as current only when a valid signal is delivered again.

Scenario: Frozen channel is invalidated and restored only on valid signal
    Given all six devices are delivering and the display test interface reports current values
    When the patient simulator stops delivering temperature samples for longer than the channel's expected ICD delivery interval
    Then the display test interface reports the temperature value in the defined invalidated rendering state within 1 second of the logged staleness detection
    When the simulator resumes delivering a changing valid temperature signal
    Then the display test interface reports the temperature value in the current rendering state only after the first valid sample's harness timestamp

Scenario: Malformed interface data is rejected and never displayed
    Given all six devices are delivering valid signals in the patient simulator
    When the simulator injects an SpO2 data frame that violates the device ICD format (RQ_IF_05)
    Then the display test interface reports no value derived from the malformed frame
    And the event log records an invalid-data rejection event naming the SpO2 channel
```

```gherkin
@ID:RQ_FN_12
Feature: Internal Failure Annunciation and Degraded Operation
    As a bedside critical-care nurse I want internal failures annunciated with an explicit map of what remains reliable
    So that I never rely on a silently failed function

Rule: The MMSS shall detect internal failures of its monitoring or diagnostic functions by cyclic self-checks with a period of at most 5 seconds, annunciate each detected failure audibly and visually within 1 second of detection — bounding failure occurrence to annunciation at 6 seconds — explicitly indicate which functions remain reliable and which are unavailable, and suppress the outputs of unreliable functions rather than displaying them.

Scenario: Injected diagnostic-function failure is annunciated and its output suppressed
    Given the MMSS is monitoring with all six simulator channels live
    When the fault-injection test interface fails the diagnostic presentation function, timestamped by the harness
    Then the audio capture records the failure annunciation and the display test interface reports the failure notice within 1 second of the logged failure detection
    And the failure annunciation occurs within 6 seconds of the harness-timestamped fault injection
    And the display test interface lists the diagnostic function as unavailable and all six parameter channels as reliable
    And the display test interface reports no diagnostic candidate output while the failure persists

Scenario: Watchdog restores monitoring within 30 seconds of an application hang
    Given the MMSS is monitoring with all six simulator channels live
    When the fault-injection test interface hangs the MMSS application, timestamped by the harness
    Then the display test interface reports restored monitoring readiness within 30 seconds of the hang timestamp (RQ_NF_07)
    And the event log contains the watchdog recovery entry with the restart timestamp
```

```gherkin
@ID:RQ_FN_13
Feature: Identity-Confirmed Transmission to the HIS
    As an emergency physician I want HIS transmission gated on explicit identity confirmation
    So that the remote second opinion lands in the correct patient record and nothing leaves on a mismatch

Rule: The MMSS shall transmit current parameters, stored trend data, and ranked candidates to the HIS, forwarding candidates within 1 second of receipt, and shall require explicit confirmation of the displayed patient identifiers before any transmission; on cancellation or identity mismatch zero data shall leave the device, and every transmission shall be labelled with source device and timestamp.

Scenario: Confirmed identity releases labelled transmission
    Given the MMSS with device identifier "MMSS-0042" is monitoring patient identifiers "PAT-4711, Doe, 1961-03-05" and the stubbed HIS endpoint is reachable
    When the user initiates sharing and explicitly confirms the displayed identifiers
    Then the stubbed HIS endpoint captures HL7/FHIR-class messages conforming to ICD-HIS-001 (RQ_IF_09, RQ_CS_05) containing parameters, stored trends, and candidates, each labelled with source "MMSS-0042" and a transmission timestamp (RQ_IF_10)
    And each candidate is captured at the HIS endpoint within 1 second of its receipt on IF_08 (RQ_PR_06)
    And the capture shows every message was carried over the defined encrypted transport (RQ_NF_06)

Scenario: Identity mismatch blocks all transmission
    Given the MMSS is monitoring patient "PAT-4711" and the stubbed HIS endpoint is reachable
    When the user initiates sharing and the confirmation entry "PAT-4712" does not match the displayed identifier
    Then the transmission is blocked with the discrepancy stated on the Display Interface
    And the stubbed HIS endpoint capture records zero bytes received from the MMSS

Scenario: Cancellation at identity confirmation sends nothing
    Given the MMSS is monitoring patient "PAT-4711" and the stubbed HIS endpoint is reachable
    When the user initiates sharing and cancels at the identity-confirmation step
    Then the stubbed HIS endpoint capture records zero bytes received from the MMSS
```

```gherkin
@ID:RQ_FN_14
Feature: Isolated and Unmistakably Marked Simulation Mode
    As a clinical educator I want simulation globally marked and hard-isolated from real data paths
    So that simulated data can never be mistaken for, mixed with, or displace real patient data

Rule: The MMSS shall provide a simulation mode in which every screen, overlay, and log entry carries an unmistakable global simulation marking for its entire duration; simulated data shall never be transmitted to the HIS nor recorded as real patient data, and real sensor data arriving during simulation shall be blocked from display, the conflict annunciated, and an explicit simulation-exit decision required.

Scenario: Simulation is globally marked and isolated from the HIS
    Given simulation mode is active replaying training scenario "cardiac-arrest-01"
    When the scenario replays for 60 seconds
    Then the display test interface reports the global simulation marking on every screen and overlay, and every log entry written carries the simulation flag
    And the stubbed HIS endpoint capture records zero bytes received while simulation is active

Scenario: Real sensor during simulation forces an exit decision
    Given simulation mode is active replaying training scenario "cardiac-arrest-01"
    When the SpO2 sensor delivers real patient data in the patient simulator
    Then the display test interface reports no real SpO2 value in the monitoring area
    And the conflict annunciation is issued and the display test interface reports the simulation-exit decision prompt before any monitoring value is shown
```

```gherkin
@ID:RQ_FN_15
Feature: Training Completion Records
    As a clinical educator I want per-user, per-scenario completion records retrievable on demand
    So that each user's qualification is demonstrable to employers and auditors

Rule: The MMSS shall record completion of each simulation training scenario per identified user, per scenario, with the completion date, shall record no completion for a scenario the user did not complete, and shall make the records retrievable on demand.

Scenario: Completed and uncompleted scenarios are recorded distinguishably
    Given a simulation session runs with the identified user "trainee-01"
    When the user completes scenario "sensor-fault-handling" on 2026-07-04 and aborts scenario "alarm-triage" before completion
    Then retrieving the retained completion records on demand (RQ_NF_10) returns
    | user       | scenario              | completion date |
    | trainee-01 | sensor-fault-handling | 2026-07-04      |
    And no completion record exists for "trainee-01" and scenario "alarm-triage"
```

```gherkin
@ID:RQ_FN_16
Feature: Timestamped Event Log with Explicit Gaps
    As an intensivist I want a chronological, single-clock event log that marks any recording gap
    So that handover and incident reconstruction rest on a complete, unambiguous record

Rule: The MMSS shall record measurements, clinical and technical alarms (onset, acknowledgement, resolution), alarm-limit changes, diagnostic outputs, and user actions in an event log with timestamps from a single system clock at 1-second resolution or finer, in chronological order, with any logging interruption explicitly marked as a gap and never silently omitted.

Scenario: Events are logged chronologically and an interruption is marked
    Given the MMSS is monitoring while the simulator raises an SpO2-low alarm that is acknowledged and resolved, a heart-rate limit change is made, and the stubbed engine delivers a diagnostic output
    When the fault-injection test interface suspends logging for 30 seconds and the log is then retrieved
    Then all recorded events appear in chronological order with timestamps from one system clock at 1-second resolution or finer
    And the SpO2 alarm entry carries onset, acknowledgement, and resolution timestamps
    And the 30-second interruption is explicitly marked as a gap entry in the timeline
    And a harness-seeded log entry dated 30 days earlier remains retrievable from the same log (RQ_NF_11)
```

```gherkin
@ID:RQ_FN_17
Feature: Update Interlock During Active Monitoring
    As a biomedical engineer I want updates refused with a stated cause while a patient is connected, and installed updates logged
    So that an update can never open a silent monitoring gap

Rule: The MMSS shall refuse to start a software update, and never start one automatically, while any patient or sensor connection is active; a refused update shall state the cause and the recommended deferral action, and every installed update shall be recorded in the event log with its version.

Scenario: Update refused while a sensor connection is active
    Given the MMSS is monitoring with at least one sensor connected in the patient simulator
    When the engineer starts a software update installation
    Then the update is refused with the cause and the recommended deferral action stated
    And no update process starts during 10 minutes of continued monitoring

Scenario: Update on a free unit is installed and logged with its version
    Given no patient or sensor connection is active
    When the engineer installs update version 2.1.0
    Then the installation completes within 60 minutes (RQ_NF_08) and the event log contains the update entry with version 2.1.0
```

```gherkin
@ID:RQ_FN_18
Feature: Two-Tier Access with Audit-Logged Break-Glass
    As an emergency-room nurse I want monitoring instantly available and protected functions guarded with an audited emergency path
    So that data protection never delays urgent care and every exceptional access stays accountable

Rule: The MMSS shall provide live monitoring, display, and alarm functions without any authentication step, protect stored and transmitted patient data and protected functions behind authorised access, refuse and log every unauthorised access attempt without affecting live monitoring, and provide a break-glass access path without normal credentials that is automatically recorded in the audit log.

Scenario: Monitoring needs no authentication while protected access is guarded
    Given the MMSS is monitoring with role-based data-protection controls active (RQ_NF_06)
    When a user views live values and alarms and then attempts to open stored records without authorisation
    Then the live values and alarms are shown with zero authentication steps
    And the unauthorised attempt is refused and logged while live monitoring continues uninterrupted

Scenario: Break-glass access is granted and audit-logged
    Given the MMSS is monitoring with data-protection controls active
    When the user invokes the break-glass path to a protected function without normal credentials
    Then access to the protected function is granted
    And the audit log contains the break-glass access entry with user context and timestamp
```

```gherkin
@ID:RQ_FN_19
Feature: Identical Behaviour Across Deployment Settings
    As an emergency-room nurse I want one software variant behaving identically in ICU, ER, and ambulance, with active limitations stated on-device
    So that patient handovers between care areas require no relearning and no guesswork about capability

Rule: The MMSS shall provide identical appearance, alarm behaviour, and operation as one software variant across ICU, ER, and mobile deployment settings, and shall state any active setting-dependent limitation on-device, in the context where it applies, within 5 seconds of the limitation condition becoming active.

Scenario: Same build shows identical operation and states the active limitation in transit
    Given one MMSS software build with a single version identifier is deployed in an ICU, an ER, and an ambulance test context
    When the same monitoring and alarm workflow is executed in each of the three contexts
    Then the display test interface reports identical screens, alarm behaviour, and operating steps across all three contexts
    And in the ambulance context, where the stubbed HIS endpoint is unreachable, the display test interface reports the limitation statement "HIS unreachable" within 5 seconds of the condition becoming active
```

```gherkin
@ID:RQ_FN_20
Feature: Local-Language On-Device Guidance in Clinical Operation
    As an emergency-room nurse I want all on-device guidance and corrective instructions in my local language
    So that I can operate the system correctly and resolve routine questions at the bedside without external help

Rule: The MMSS shall present all on-device operating guidance, labels, and corrective-action instructions during clinical operation in the configured target-market language, selected and verified at installation; no clinical-operation text shall be presented in any other language.

Scenario: Device configured for de-DE presents all clinical-operation text in German
    Given the target-market language "de-DE" was selected and verified at installation
    When the MMSS is used in clinical operation and a sensor-fault corrective-action instruction is triggered in the patient simulator
    Then all operating guidance, labels, and the corrective-action instruction captured via the display test interface are rendered in "de-DE"
    And the display test interface reports zero clinical-operation text elements rendered in any other language
```

```gherkin
@verification:by-review
Feature: Verification by Review
    Process, documentation, and constraint requirements that no executable scenario can prove are closed by review of objective evidence.

Rule: Each requirement listed below is verified by review of the named evidence item; the requirement passes only when the evidence item exists, is approved, and explicitly addresses every clause of the requirement.

Scenario Outline: Requirement closed by evidence review
    Given the evidence item "<evidence>" is presented for review
    When the reviewer checks it clause by clause against <requirement>
    Then every clause of <requirement> is explicitly satisfied and the review record is signed with a pass verdict

    Examples:
    | requirement | evidence                                                                           |
    | RQ_IF_11    | static analysis report of platform service calls                                   |
    | RQ_IF_12    | resource-utilisation report against the platform envelope                          |
    | RQ_NF_01    | IEC 62304 class B lifecycle file with classification rationale                     |
    | RQ_NF_02    | ISO 14971 risk management file                                                     |
    | RQ_NF_03    | IEC 62366-1 usability file with summative evaluation report                        |
    | RQ_NF_04    | IEC 60601-1-8 alarm-system conformity evidence                                     |
    | RQ_NF_05    | IEC 81001-5-1 secure development lifecycle records                                 |
    | RQ_NF_06    | security verification report of at-rest encryption (AES-128 or stronger)          |
    | RQ_NF_07    | availability analysis demonstrating 99.9 % availability                            |
    | RQ_NF_09    | released labelling, UDI, and IFU package                                           |
    | RQ_NF_10    | records-retention policy and customer-availability procedure for training records  |
    | RQ_NF_12    | AI-regulation transparency documentation                                           |
    | RQ_CS_01    | regulatory clearance certificate issued before marketing                           |
    | RQ_CS_02    | controlled 62304 class C-to-B reduction record                                     |
    | RQ_CS_03    | configuration audit of the unmodified AI model                                     |
    | RQ_CS_04    | design review limiting interfaces to the six device types                          |
    | RQ_CS_06    | ICD review of the engine-owned 2-minute budget                                     |
    | RQ_CS_07    | configuration audit of the unchanged embedded platform                             |
    | RQ_CS_08    | post-market change-control procedure records                                       |
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
