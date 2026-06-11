---
Executed by: orchestration (CLAUDE.md)
Flow: flows/expectationeering-flow/flow.md
Templates: flows/expectationeering-flow/expectationeering-workbook.md
Inputs: inputs/
Date: 2026-06-11
---

# Expectationeering Workbook

**Product**: Mobile Monitoring Software Solution (MMSS)
**Date**: 2026-06-11
**Workshop Team**: User Stakeholder, Customer Stakeholder, Business Stakeholder, Regulatory Stakeholder, Product Owner, System Architect, Usability Validation, Development Lead, Verification Lead, Quality Assurance

---

# Introduction

This workbook captures the expectations and requirements for the product, from informal stakeholder expectations through to verifiable system requirements. Every requirement item has a unique identifier, starting with the stakeholder expectations, and each item traces to the upstream item it is derived from.

## Intended users of the document

The development, quality, regulatory, and verification teams of the legal manufacturer; product management and clinical/usability specialists contributing to the requirements; and auditors or notified-body reviewers assessing the design history file.

## Scope of the document

The Mobile Monitoring Software Solution (MMSS): medical device software that transforms an existing portable patient monitor into an active clinical decision-support tool — from informal stakeholder expectations through to verifiable system requirements (Verification, SV_*). Architecture, detailed design, system DFMEA, and item decomposition are downstream and out of scope.

---

# Application

## Stakeholders (INFORMAL)

The stakeholder level is the start of the requirement approach. It captures the problem to be solved and the expectations of each stakeholder in a product-agnostic ("product-free") way.

### Problem

#### Domain Description

The domain is **patient monitoring and clinical decision support for critically ill patients**, spanning pre-hospital and mobile care (ambulances, mobile medical units), emergency rooms, and intensive care units. In this domain, trained medical professionals must continuously track key vital signs — acquired non-invasively from the patient — detect life-threatening changes the moment they occur, and reach a working diagnosis fast enough to start the right treatment within the narrow window that determines patient outcome. Solutions in this domain — from any vendor — combine vital-sign acquisition from measurement sensors, real-time presentation and alarming, and increasingly some form of diagnostic assistance, while operating under strict medical-device legislation (e.g. EU MDR 2017/745, US FD&C Act), lifecycle and risk standards (IEC 62304, ISO 14971, IEC 62366-1, IEC 60601-1-8), and health-data protection law (GDPR, HIPAA). Buyers are hospital and emergency-medical-service organisations procuring against clinical value, regulatory acceptability, fleet and IT compatibility, and total cost of ownership.

#### Actual State

Today, critical care relies on conventional portable patient monitors that passively display vital signs, supported by the clinician's unaided diagnostic judgement.

**Pros:**
- Continuous non-invasive vital-sign monitoring is mature, trusted, and clinically accepted as the safety baseline of critical care.
- Conventional alarming for abnormal physiological values is established and familiar to clinical staff.
- Large installed fleets of monitors and measurement sensors exist, with trained users and proven procurement, service, and regulatory pathways.
- The clinician remains unambiguously in charge of diagnosis and treatment, keeping clinical responsibility clear.

**Cons:**
- Monitors are passive displays: interpreting the data and converging on a diagnosis depends entirely on the individual clinician's experience, under extreme time pressure and cognitive load.
- Time-to-diagnosis in pre-hospital and mobile settings is highly variable; diagnostic delay or error directly worsens outcomes for critically ill patients.
- Sensor disconnection or misplacement can go unnoticed, leading to treatment decisions based on false or missing data.
- Diagnostic guidance, when available at all, is not present at the patient's side in mobile settings; advanced support is confined to the hospital.
- Patient data and preliminary findings are handed over verbally under stress, causing information loss at transitions of care.
- Clinicians have no safe environment to build competence and justified trust in newer assistive capabilities before facing them in a live emergency.

#### Desired State

In the desired situation, the proven monitoring baseline is preserved while the monitoring capability becomes an active partner in diagnosis.

**Pros (retained from the actual state):**
- Continuous, trusted non-invasive vital-sign monitoring and established clinical alarming remain the foundation.
- Existing sensor fleets, user competence, and procurement and regulatory pathways continue to be leveraged.
- The trained clinician remains the final clinical decision-maker, with responsibility boundaries intact.

**Pros (new):**
- Clinicians receive ranked, clinically validated diagnostic candidates in real time at the patient's side — converging within minutes of patient connection — shortening time-to-diagnosis wherever the patient is.
- Monitoring is operational within seconds and continues seamlessly through transport and handover, including in environments with intermittent connectivity.
- Sensor faults, disconnections, and misplacements are detected automatically and announced unmistakably, so decisions are never silently based on bad data.
- Diagnostic suggestions are always clearly distinguishable from measured facts, and their absence or delay is explicitly signalled, protecting clinical judgement.
- Patient data and diagnostic findings flow to the receiving hospital through standard healthcare interoperability interfaces, enabling second opinions and prepared handovers.
- Clinicians can train on the diagnostic-support capability in a safe simulation setting before live use.
- The capability is delivered, certified, supported, and updated as regulated medical device software over a multi-year service life, within a commercially sustainable cost of ownership.

**Cons:**
- Diagnostic assistance introduces new hazards (misleading suggestions, automation bias, silent algorithm change) that demand rigorous validation, risk control, and human-in-the-loop safeguards.
- The regulatory, cybersecurity, and post-market surveillance burden grows substantially compared to passive monitoring.
- Clinical acceptance requires evidence, training, and trust-building; the benefit case must be demonstrable to justify procurement.

#### Identified Gaps (DC_*)

The design changes needed to move from the actual state to the desired state.

| ID | Description |
|----|-------------|
| DC_01 | Provide ranked, real-time diagnostic candidates derived from the patient's live vital signs at the point of care, converging to a usable diagnostic picture within minutes of patient connection, to demonstrably shorten time-to-diagnosis. |
| DC_02 | Make monitoring operational within seconds of reaching the patient, so no treatment time is lost at the start of an emergency. |
| DC_03 | Sustain continuous, low-latency real-time presentation of key vital signs throughout the care episode — including transport, handover between care settings, and environments with intermittent connectivity. |
| DC_04 | Alert clinicians immediately and unmistakably to abnormal physiological conditions, with alarm behaviour conforming to the applicable alarm and patient-monitoring standards and at least on par with conventional monitoring. |
| DC_05 | Automatically detect and unmistakably announce sensor disconnection, misplacement, and unreliable readings, so clinical decisions are never silently based on false or missing data. |
| DC_06 | Keep diagnostic suggestions clearly and permanently distinguishable from measured clinical facts, positioned as advisory input to a trained professional who retains final clinical judgement. |
| DC_07 | Explicitly signal when diagnostic guidance is unavailable or has not arrived within the expected time, so clinicians fall back on their own assessment instead of waiting on absent support. |
| DC_08 | Make the capability usable under high-stress mobile and critical-care conditions: readable at a glance in moving vehicles, poor lighting, and noise; operable in minimal steps with standard clinical training; with foreseeable use errors identified and controlled through usability engineering. |
| DC_09 | Share patient data and diagnostic findings with hospital information systems through established healthcare interoperability standards, enabling second opinions and prepared handovers without custom interface projects. |
| DC_10 | Deliver the new capability as software on existing, unmodified monitoring hardware and the installed fleet of non-invasive measurement sensors, through standardised, contractually documented interfaces that permit supplier substitution and protect prior investments. |
| DC_11 | Base any diagnostic intelligence on clinically validated, change-controlled algorithms — sourced as commercially validated off-the-shelf components where appropriate and qualified for use in a medical device — with documented evidence of claimed performance in the intended population and use environments. |
| DC_12 | Establish full regulatory conformity capability for diagnostic-support software: medical-device qualification and classification per applicable legislation, certified quality-management-system development with design control, an IEC 62304-compliant software lifecycle, ISO 14971 risk management, qualification of third-party software, and complete, submission-ready technical documentation. |
| DC_13 | Build layered, independent risk-control measures around every safety-critical function — alarming, diagnosis, fault detection — so that no single failure can cause unmitigated patient harm, residual liability stays absorbable, and the resulting software safety classification remains commercially manageable with documented justification. |
| DC_14 | Provide a structured training offering with a safe simulation/practice capability, so clinical users build competence and justified trust in diagnostic guidance before using it on real patients. |
| DC_15 | Make the capability maintainable and updatable in the field over a multi-year service life — security patches, regulatory maintenance, post-market surveillance and vigilance — within the capacity of an established support organisation. |
| DC_16 | Demonstrate cybersecurity risk management and protection of personal health data compliant with applicable data-protection law for all data processed, displayed, or transmitted. |
| DC_17 | Achieve a commercially sustainable offering: predictable total cost of ownership, pricing and terms competitive in tender processes, and a scoped, validated release baseline that keeps regulatory submission and launch dates predictable. |

### Expectations

Stakeholder expectations are written "product-free": they apply to any product in the problem domain, including competitors. Format: *The \<stakeholder\> wants \<expectation\> to \<benefit driver\>.*

#### User Expectations (UE_*)

**Stakeholder**: Critical Care Clinician

Trained medical professionals — paramedics, emergency physicians, and ICU/emergency nurses — who monitor and treat critically ill patients in time-pressured, often mobile or chaotic environments (ambulances, emergency rooms, ICUs), frequently while their hands and attention are divided between the patient and the equipment.

| ID | Expectation | Traces |
|----|-------------|--------|
| UE_01 | The Clinician wants continuous, real-time visibility of a critically ill patient's key vital signs to detect deterioration the moment it begins and intervene without delay. | DC_03 |
| UE_02 | The Clinician wants monitoring to be up and running within seconds of reaching the patient to avoid losing treatment time in emergencies where every minute affects outcome. | DC_02 |
| UE_03 | The Clinician wants early diagnostic guidance, ranked by likelihood, while still at the patient's side to narrow down the cause faster than unaided assessment allows under time pressure. | DC_01 |
| UE_04 | The Clinician wants to be alerted immediately and unmistakably when a vital sign becomes abnormal to act on a life-threatening change even when attention is focused elsewhere on the patient. | DC_04 |
| UE_05 | The Clinician wants to be warned when a sensor is disconnected, misplaced, or delivering unreliable readings to avoid treating — or failing to treat — a patient based on false or missing data. | DC_05 |
| UE_06 | The Clinician wants to always be able to distinguish suggested diagnoses from confirmed clinical facts to retain final clinical judgement and avoid being misled into premature treatment decisions. | DC_06 |
| UE_07 | The Clinician wants vital signs and alerts to be readable and interpretable at a glance, in moving vehicles, poor lighting, and noisy surroundings, to keep eyes and hands on the patient rather than on the equipment. | DC_08 |
| UE_08 | The Clinician wants patient monitoring to continue uninterrupted during transport and handover between care settings to prevent gaps in observation at the most vulnerable moments of the care chain. | DC_03 |
| UE_09 | The Clinician wants patient data and diagnostic findings shared with the receiving hospital to enable a second opinion and a prepared, seamless handover without verbally repeating everything under stress. | DC_09 |
| UE_10 | The Clinician wants to practise interpreting diagnostic guidance in a safe training setting before using it on real patients to build justified trust and avoid misreading suggestions in a live emergency. | DC_14 |
| UE_11 | The Clinician wants to know explicitly when diagnostic guidance is not available or has not arrived in the expected time to fall back on their own clinical assessment instead of waiting on absent support. | DC_07 |
| UE_12 | The Clinician wants operating the monitoring equipment to require minimal steps and no specialist technical knowledge beyond standard clinical training to stay focused on the patient rather than on the device. | DC_08 |

#### Market Expectations (ME_*)

**Stakeholder**: Hospital & EMS Procurement

The procurement organisation of hospitals and emergency medical services that selects, purchases, and contracts patient monitoring and clinical decision-support solutions for critical care and pre-hospital use, balancing clinical value, total cost of ownership, regulatory acceptability, and fit with the existing equipment fleet and IT landscape.

| ID | Expectation | Traces |
|----|-------------|--------|
| ME_01 | The Hospital & EMS Procurement wants demonstrable evidence of faster time-to-diagnosis in critical care and pre-hospital settings to justify the investment through improved patient outcomes and shorter intervention times. | DC_01 |
| ME_02 | The Hospital & EMS Procurement wants the solution to hold valid regulatory clearance for medical device software in the target markets at time of purchase to avoid deployment delays, contract penalties, and liability exposure. | DC_12 |
| ME_03 | The Hospital & EMS Procurement wants any diagnostic-support capability to use clinically validated, certified algorithms to satisfy clinical governance boards and reduce the risk of misdiagnosis claims. | DC_11 |
| ME_04 | The Hospital & EMS Procurement wants the solution to work with the non-invasive measurement devices already in the installed fleet through standardised interfaces to avoid replacing existing sensor and monitor investments. | DC_10 |
| ME_05 | The Hospital & EMS Procurement wants integration with hospital information systems via established healthcare interoperability standards (e.g. HL7/FHIR) to fit the existing IT landscape without costly custom interface projects. | DC_09 |
| ME_06 | The Hospital & EMS Procurement wants a predictable total cost of ownership — covering licences, updates, training, and support — over the equipment's service life to plan multi-year budgets reliably. | DC_17 |
| ME_07 | The Hospital & EMS Procurement wants vendor-provided clinician training, including a safe practice/simulation capability, to bring staff to competence quickly and limit the cost and risk of misuse during rollout. | DC_14 |
| ME_08 | The Hospital & EMS Procurement wants reliable alarming for abnormal patient conditions and sensor or connection faults at least on par with conventional monitoring equipment to meet the clinical safety baseline expected of any monitoring purchase. | DC_04, DC_05 |
| ME_09 | The Hospital & EMS Procurement wants long-term vendor support commitments, including security patches and regulatory maintenance of the software, to protect the investment over a typical 7–10 year equipment lifecycle. | DC_15 |
| ME_10 | The Hospital & EMS Procurement wants the solution to perform dependably in mobile and ambulance environments with intermittent connectivity to ensure clinical usability across the full range of deployment settings being paid for. | DC_03 |
| ME_11 | The Hospital & EMS Procurement wants documented cybersecurity and patient data protection compliant with applicable health data regulations to pass IT security review and avoid data-breach liability. | DC_16 |
| ME_12 | The Hospital & EMS Procurement wants pricing and contract terms competitive with comparable monitoring and decision-support offerings on the market to defend the selection in a public or competitive tender process. | DC_17 |

#### Business Expectations (BE_*)

**Stakeholder**: Legal Manufacturer

The organisation that designs, produces, and places the product on the market and therefore carries full legal responsibility for its safety, performance, and post-market support. It speaks for executive strategy, R&D, quality management, regulatory affairs, manufacturing/release, finance, legal, and customer service.

| ID | Expectation | Traces |
|----|-------------|--------|
| BE_01 | The Legal Manufacturer wants the product to strengthen its existing patient-monitoring portfolio rather than create an unrelated product line to protect its strategic market position and concentrate investment where the organisation already holds competence and brand credibility. | DC_10 |
| BE_02 | The Legal Manufacturer wants development effort confined to software on top of existing, unmodified hardware platforms to limit capital investment, avoid hardware re-qualification cost, and keep time-to-market within the business case window. | DC_10 |
| BE_03 | The Legal Manufacturer wants any diagnostic intelligence sourced as a commercially validated off-the-shelf component rather than developed in-house for the first release to cap R&D cost and schedule risk and to avoid carrying the validation burden of a novel clinical algorithm. | DC_11 |
| BE_04 | The Legal Manufacturer wants every safety-critical function backed by an independent mitigation path so that the residual software safety classification, and with it the development and documentation burden under IEC 62304, remains commercially manageable. | DC_13 |
| BE_05 | The Legal Manufacturer wants the development executed under its established quality management system with full design control and traceable documentation to remain audit-ready and to defend itself credibly in any liability or regulatory proceeding. | DC_12 |
| BE_06 | The Legal Manufacturer wants residual product liability exposure — in particular from misdiagnosis, missed alarms, or undetected sensor faults — reduced to a level its legal and insurance position can absorb to protect the organisation from claims that could exceed the product's lifetime earnings. | DC_13 |
| BE_07 | The Legal Manufacturer wants the clinical decision-support function positioned as advisory to a trained professional, never as an autonomous diagnosis, to keep the responsibility boundary between manufacturer and clinical user legally defensible. | DC_06 |
| BE_08 | The Legal Manufacturer wants external interfaces to measurement devices and hospital systems built on standardised, contractually documented interface definitions to limit integration liability, enable supplier substitution, and avoid lock-in to any single component vendor. | DC_09, DC_10 |
| BE_09 | The Legal Manufacturer wants the product to be maintainable and updatable in the field throughout a multi-year service life to meet support commitments, deliver security and regulatory updates economically, and protect recurring service revenue. | DC_15 |
| BE_10 | The Legal Manufacturer wants the service and complaint-handling burden of the product to fit the capacity and competence of its existing support organisation to keep cost-of-quality within margin targets and satisfy post-market surveillance obligations without major new hiring. | DC_15 |
| BE_11 | The Legal Manufacturer wants a structured training offering, including safe practice facilities for clinical users, deliverable alongside the product to mitigate foreseeable-misuse liability and reduce use-error-driven complaints and field actions. | DC_14 |
| BE_12 | The Legal Manufacturer wants the release scope frozen against a validated baseline with deferral of unproven capabilities to later releases to make regulatory submission, verification, and manufacturing release predictable and to protect the launch date committed to the market. | DC_17 |

#### Regulatory Expectations (RE_*)

**Stakeholder**: Competent Authority / Notified Body

The national competent authorities (e.g. FDA, EU member-state authorities) and accredited notified bodies that decide whether medical device software may be placed on a market, audit its technical documentation, and monitor it after release. They enforce mandatory market-access legislation and can approve, refuse, or withdraw the product.

| ID | Expectation | Traces |
|----|-------------|--------|
| RE_01 | The Competent Authority wants any software that provides diagnostic or clinical decision support to be qualified and classified as a medical device under the applicable legislation of each target market (e.g. EU MDR 2017/745, US FD&C Act) to ensure it enters the market only through the legally mandated conformity assessment or premarket pathway. | DC_12 |
| RE_02 | The Notified Body wants a complete technical documentation file — intended use, clinical evaluation, risk management file, software lifecycle records, usability file, and labelling — maintained and submission-ready to be able to grant and sustain the certificate required for market access. | DC_12 |
| RE_03 | The Competent Authority wants clinical evidence demonstrating that the diagnostic-support output achieves its claimed performance and clinical benefit in the intended patient population and use environments to confirm a favourable benefit-risk determination before approval. | DC_11 |
| RE_04 | The Competent Authority wants the software developed and maintained under a certified quality management system (e.g. ISO 13485 or equivalent QMS regulation) to provide assurance that design controls, change control, and release discipline are enforced throughout the product lifecycle. | DC_12 |
| RE_05 | The Competent Authority wants the software lifecycle executed in compliance with IEC 62304 at the safety class resulting from its hazard analysis, with documented justification for any classification reduction through external risk-control measures, to ensure development rigour matches the harm the software can cause. | DC_12, DC_13 |
| RE_06 | The Competent Authority wants risk management performed and documented per ISO 14971 across the entire lifecycle — including hazards from sensor faults, data loss, missed or misleading alarms, and incorrect diagnostic output — to demonstrate that all residual risks are acceptable against the clinical benefit. | DC_12, DC_13 |
| RE_07 | The Competent Authority wants a usability engineering process per IEC 62366-1 with summative evaluation of safety-related use scenarios to demonstrate that foreseeable use errors by clinical users in high-stress mobile and critical-care environments are identified and controlled. | DC_08 |
| RE_08 | The Competent Authority wants alarm system behaviour to conform to the applicable alarm and patient-monitoring standards (e.g. IEC 60601-1-8) to ensure clinicians are reliably and consistently alerted to physiological and technical alarm conditions. | DC_04 |
| RE_09 | The Competent Authority wants any AI or machine-learning component governed by a defined oversight framework — validated performance claims, locked or change-controlled algorithms, transparency of intended use and limitations, and human-in-the-loop positioning — to prevent unverified or silently changing algorithms from influencing clinical decisions. | DC_06, DC_11 |
| RE_10 | The Competent Authority wants third-party and off-the-shelf software components qualified as SOUP with documented verification of their suitability, known anomalies, and failure behaviour to ensure that externally sourced functionality does not undermine the safety case of the overall device. | DC_11, DC_12 |
| RE_11 | The Competent Authority wants demonstrated cybersecurity risk management and protection of personal health data in compliance with applicable data-protection law (e.g. GDPR, HIPAA) for all data processed, displayed, or transmitted to external health-information systems to safeguard patient safety, privacy, and data integrity. | DC_16 |
| RE_12 | The Surveillance Authority wants an operational post-market surveillance and vigilance system — incident reporting, trend analysis, periodic safety update reporting, and field safety corrective action capability — to ensure emerging risks are detected and acted upon for as long as the product remains on the market. | DC_15 |

### Ideal Product Model (KA_*)

The Ideal Product Model is the blueprint that aligns stakeholder expectations with product capabilities — the key proposition attributes, their priority, feasibility, and risk.

| ID | Benefit Driver | Expectation | Proposition Attributes | Superior to | Priority | Feasible | Risk | Rationale |
|----|----------------|-------------|------------------------|-------------|----------|----------|------|-----------|
| KA_01 | Immediate, uninterrupted patient visibility | UE_01, UE_02, UE_08, ME_10 | Continuous real-time multi-parameter vital signs monitoring that is operational within seconds of patient connection and runs uninterrupted across transport and handover, dependable even with intermittent network connectivity. | Conventional monitoring set-ups with slow start-up and observation gaps during transfer between care settings. | High | Yes — mature capability class, but real-time acquisition across six measurement-device classes on a fixed embedded platform within sub-second presentation budgets demands early integration prototyping. | Medium — real-time device connectivity and integration is a recognised high-probability project risk, and an undetected connection failure has critical clinical impact. | Continuous visibility from first patient contact is the baseline clinical value on which every other capability builds. |
| KA_02 | Faster time-to-diagnosis at the point of care | UE_03, ME_01 | Ranked, likelihood-ordered diagnostic candidates generated in real time at the patient's side, converging to a predictive shortlist within minutes of patient connection, with demonstrable evidence of faster time-to-diagnosis. | Unaided clinical assessment and passive vital-signs-only displays that leave the differential diagnosis entirely to the clinician under time pressure. | High | Challenging — diagnostic convergence time is owned by the validated algorithm component, not by the integrating software, whose own contribution must stay within sub-second hand-off and presentation budgets on fixed hardware. | High — clinical performance claims must be evidenced in the intended population and environments; algorithm validation complexity and regulatory clearance timing of the diagnostic claim are both recognised high-impact risks, and as legal manufacturer the organisation carries misdiagnosis liability on every published performance claim — each figure must be evidenced and insurable. | This is the differentiating value proposition and the measurable outcome procurement pays for. |
| KA_03 | Trustworthy, certifiable diagnostic intelligence | ME_03, BE_03, RE_03, RE_09, RE_10 | Diagnostic intelligence sourced as a commercially validated, change-controlled off-the-shelf algorithm, qualified as third-party software (SOUP) with documented performance claims, known limitations, anomalies, and failure behaviour, under a defined AI oversight framework. | Novel in-house clinical algorithms carrying unproven evidence and the full validation burden for the first release. | High | Yes — clinically validated components of this class are commercially available. | Medium-High — dependency on the external algorithm supplier's clinical evidence, change control, and roadmap, plus clearance-timing exposure for the diagnostic claim; legal responsibility for the third-party component's performance stays with the legal manufacturer, so supplier agreements must secure change notification, anomaly disclosure, and component availability across the full service life. | Caps R&D cost and schedule risk while satisfying clinical governance and regulatory AI-oversight expectations. |
| KA_04 | Reliable physiological alarming | UE_04, ME_08, RE_08 | Immediate, unmistakable alarms for abnormal vital signs, conforming to applicable alarm and patient-monitoring standards (e.g. IEC 60601-1-8) and perceivable even when the clinician's attention is elsewhere on the patient. | Monitoring set-ups whose alarm behaviour varies by device and configuration, risking missed or ambiguous alerts. | High | Yes — standardised alarm behaviour is a well-understood engineering discipline, achievable within sub-second annunciation budgets. | Medium — alarm failures are among the highest-severity clinical hazards; residual risk remains acceptable only with an independent annunciation path outside the software. | Alarm reliability at least on par with conventional monitoring is the entry ticket for any monitoring purchase. |
| KA_05 | Trustworthy data through fault transparency | UE_05, ME_08 | Automatic detection and unambiguous annunciation of sensor disconnection, misplacement, and unreliable readings, so clinicians never act — or fail to act — on silently false or missing data. | Equipment that keeps displaying stale or implausible values without flagging sensor or connection faults. | High | Partly — connectivity supervision (inactivity timeout) and annunciation are established software practice, but misplacement detection itself resides in the fixed measurement devices; the software can only supervise and annunciate what the devices report. | Medium-High — undetected sensor misplacement feeding a wrong diagnosis is a critical-impact risk, and its mitigation depends on auto-detection capability in devices outside the design's control; the responsibility split between the software and the fixed measurement devices must be contractually documented in the interface definitions to keep the liability boundary defensible. | False data is more dangerous than no data; fault transparency protects the integrity of both monitoring and diagnostic support. |
| KA_06 | Clinician-in-command advisory positioning | UE_06, BE_07, RE_09 | Diagnostic suggestions always presented as advisory candidates, visually and semantically distinct from measured clinical facts, with the trained professional explicitly positioned as the final decision-maker (human-in-the-loop). | Decision-support presentations that blur the line between suggestion and finding, inviting automation bias and premature treatment. | High | Yes — a matter of disciplined presentation, labelling, and claims wording. | Medium — clinician misinterpretation of advisory candidates is a critical-impact risk; presentation discipline must be reinforced by mandatory practice training and summative usability evidence. | Keeps the responsibility boundary between manufacturer and clinical user legally defensible and clinically safe. |
| KA_07 | Explicit absence of guidance | UE_11 | Active notification when diagnostic guidance is unavailable or has not converged within its expected time window, prompting an immediate fallback to unaided clinical assessment. | Decision-support tools that fail silently, leaving clinicians waiting on support that will not arrive. | High | Yes — timeout supervision and status signalling are straightforward. | Low-Medium — low probability but critical impact if a guidance timeout goes unannounced; controlled by annunciating the timeout through two independent paths. | A clinician who knows support is absent loses no time; one who does not delays treatment. |
| KA_08 | Glanceable, low-burden operation in harsh environments | UE_07, UE_12, RE_07 | At-a-glance readability of vital signs, alarms, and guidance in moving vehicles, poor lighting, and noise; operation in minimal steps with standard clinical training only; developed under a usability engineering process (IEC 62366-1) with summative evaluation of safety-related use scenarios. | Equipment-centric interfaces that pull eyes and hands away from the patient and demand specialist device knowledge. | High | Yes — established usability engineering practice, though the fixed display hardware bounds the presentation design space and summative evaluation in mobile scenarios takes real effort. | Medium — use errors in high-stress mobile contexts are safety-relevant. | In mobile critical care the interface competes with the patient for attention; it must lose that competition by design. |
| KA_09 | Seamless hospital handover | UE_09, ME_05, BE_08 | Sharing of patient data and diagnostic findings with receiving hospital information systems over established healthcare interoperability standards (e.g. HL7/FHIR), built on contractually documented interface definitions. | Verbal-only handover under stress and bespoke per-site integration projects. | Medium | Conditional — interoperability standards are mature, but the hospital-side protocol choice and interface control definitions are still undecided and must be fixed early. | Medium — protocol and interface agreements are still open and a known integration risk. | Enables second opinion and a prepared handover while avoiding costly custom IT projects and integration liability. |
| KA_10 | Fleet-compatible, software-only proposition | ME_04, BE_01, BE_02, BE_08 | Capability delivered as software on existing, unmodified monitoring hardware and the installed base of non-invasive measurement devices, through standardised, documented device interfaces that enable supplier substitution. | Rip-and-replace offerings that force new hardware purchases and lock the customer to a single vendor. | High | Yes — contingent on stable, published device interfaces for all six measurement device classes. | Medium-High — real-time integration across six fixed device classes is a high-probability, high-impact project risk, to be retired by early prototyping and prioritised interface definition. | Protects both customer and manufacturer investment and keeps time-to-market and capital cost inside the business case. |
| KA_11 | Confidence through safe practice | UE_10, ME_07, BE_11 | A safe training and simulation capability, delivered alongside a structured vendor training offering, letting clinicians practise interpreting diagnostic guidance before using it on real patients. | Live-patient learning curves and document-only training programmes. | High | Yes — simulation and scenario replay are established training practice. | Medium — training is a designated risk control for a critical-severity misinterpretation hazard; under-resourcing it converts directly into use-error complaints, field actions, and foreseeable-misuse liability. | Builds justified clinician trust and brings staff to competence quickly; as a formal risk control against clinician misinterpretation it is a release condition for the manufacturer, not an optional add-on. |
| KA_12 | Market access by design | ME_02, BE_05, RE_01, RE_02, RE_04, RE_05, RE_06 | Development as regulated medical device software under a certified quality management system with full design control: lifecycle per IEC 62304 at the hazard-derived safety class, risk management per ISO 14971 across the lifecycle, and a complete, submission-ready technical documentation file at launch. | Retrofit compliance efforts that delay clearance, erode launch dates, and expose the buyer to deployment penalties. | High | Yes — established processes; the documentation and evidence effort is substantial but well-charted. | Medium — clearance timing remains a schedule risk on the critical path. | Valid regulatory clearance at time of purchase is a hard procurement criterion; without it there is no market. |
| KA_13 | Independently mitigated safety architecture | BE_04, BE_06, RE_05, RE_06 | Every safety-critical function — alarming and diagnostic support — backed by an independent external risk-control path, with documented justification for the resulting software safety-classification reduction. | Single-channel designs whose software carries the full highest-class development burden and undiluted liability exposure. | High | Yes — independent risk-control measures are available in the use environment. | Medium — the classification-reduction justification must survive notified-body scrutiny. | Keeps the IEC 62304 documentation burden and residual liability commercially absorbable without weakening patient safety. |
| KA_14 | Secure and private by design | ME_11, RE_11 | Documented cybersecurity risk management and protection of personal health data compliant with applicable data-protection law (e.g. GDPR, HIPAA) for all data processed, displayed, or transmitted to external health-information systems. | Connected monitoring equipment with an unverified security posture that fails hospital IT security review. | High | Yes — established security engineering and privacy practice. | Medium — an evolving threat landscape demands sustained maintenance. | Failing IT security review blocks procurement regardless of clinical merit; breaches create patient-safety and liability harm. |
| KA_15 | Supportable across the service life | ME_09, BE_09, BE_10, RE_12 | Field-maintainable and updatable software across a 7–10 year service life, with committed security patches, regulatory maintenance, and an operational post-market surveillance and vigilance capability, all within the existing support organisation's capacity. | Products whose support cost, patch cadence, and obsolescence shift the lifecycle burden onto the customer. | Medium | Yes — requires update and surveillance mechanisms designed in from the start. | Medium — long-horizon commitments and cost-of-quality exposure; surveillance and vigilance are statutory obligations for as long as the product remains on the market, and the support burden must fit the existing service organisation's capacity and competence without major new hiring. | Protects the customer's multi-year investment and the manufacturer's service revenue while satisfying vigilance obligations. |
| KA_16 | Predictable, competitive lifecycle cost | ME_06, ME_12, BE_12 | A frozen, validated first-release scope with deferral of unproven capabilities to later releases, supporting a predictable total cost of ownership and pricing competitive with comparable monitoring and decision-support offerings. | Scope-creeping programmes with slipping launch dates and opaque lifetime costs. | Medium | Yes — primarily a scope-governance decision rather than a technical one. | Low-Medium — deferred scope may disappoint individual stakeholders, but uncontrolled scope growth threatens the committed launch date, the submission baseline, and the business-case margin. | A defendable tender position and a protected launch date are prerequisites for commercial success; the frozen, validated baseline is what makes regulatory submission, verification, and manufacturing release dates credible. |

### Business 'Requirements' (BR_*)

Conceptual project inputs from all business stakeholders that apply across the whole product lifecycle (development, launch, manufacturing, deployment, operation & use, end of life).

| ID | Description | Rationale | Stakeholder | Importance | Traces |
|----|-------------|-----------|-------------|------------|--------|
| BR_01 | The product must be developed as regulated medical device software under a certified quality management system with full design control, following a software lifecycle per IEC 62304 at the hazard-derived safety class, and a complete, submission-ready technical documentation file must be available at launch. | Without demonstrable design control and a complete technical file there is no regulatory clearance and therefore no market; retrofit compliance destroys the launch date. | Regulatory Affairs (Legal Manufacturer) | Critical | KA_12 |
| BR_02 | Risk management per ISO 14971 must be applied across the entire product lifecycle, from concept through post-market, with all risk-control measures verified and residual risks documented and accepted before release. | Risk management is the statutory backbone of market access and the legal manufacturer's primary defence in any liability claim. | Quality Management | Critical | KA_12 |
| BR_03 | Every safety-critical function (alarming, diagnostic support) must be backed by an independent external risk-control path, with a documented safety-classification-reduction justification capable of withstanding notified-body scrutiny. | Independent mitigation keeps the development documentation burden and residual liability commercially absorbable without weakening patient safety. | Quality Management / Regulatory Affairs | Critical | KA_13 |
| BR_04 | Diagnostic intelligence for the first release must be sourced as a commercially validated, change-controlled off-the-shelf algorithm qualified as third-party software (SOUP), with supplier agreements securing documented performance claims, change notification, anomaly disclosure, and component availability across the full service life. | Caps R&D cost, validation effort, and clearance-timing risk while keeping the legal manufacturer's third-party-component obligations contractually covered. | R&D Management (Legal Manufacturer) | Critical | KA_03 |
| BR_05 | Every published clinical performance claim — including any time-to-diagnosis claim — must be backed by documented clinical evidence in the intended population and use environments, and must be insurable. | As legal manufacturer the organisation carries misdiagnosis liability on every claim it publishes; unevidenced claims are uninsurable exposure. | Legal Manufacturer | Critical | KA_02 |
| BR_06 | All labelling, marketing claims, and on-product presentation must position diagnostic output as advisory candidates only, visually and semantically distinct from measured clinical facts, with the trained professional explicitly the final decision-maker (human-in-the-loop). | Keeps the responsibility boundary between manufacturer and clinical user legally defensible and counters automation bias, a recognised critical-severity hazard. | Legal & Compliance | Critical | KA_06 |
| BR_07 | Unavailability or non-convergence of diagnostic guidance within its expected time window must be actively annunciated to the clinician through at least two mutually independent notification paths, so that fallback to unaided clinical assessment is immediate. | A silent decision-support failure delays treatment and converts directly into critical-severity liability; independence of the notification paths is what removes residual risk from the supporting software and underpins the safety-classification reduction. | Legal Manufacturer / Clinician | High | KA_07 |
| BR_08 | Physiological alarm behaviour must conform to the applicable alarm and patient-monitoring standards (e.g. IEC 60601-1-8), with annunciation perceivable even when the clinician's attention is elsewhere. | Standards-conformant alarm reliability is the entry ticket for any monitoring purchase and among the highest-severity hazard areas. | Regulatory Affairs / Clinician | Critical | KA_04 |
| BR_09 | Sensor disconnection, misplacement, and unreliable readings must be automatically detected (within the limits of what the fixed measurement devices report) and unambiguously annunciated, so clinicians never act on silently false or missing data. | False data is more dangerous than no data; fault transparency protects clinical trust in both monitoring and diagnostic support. | Clinician / Quality Management | High | KA_05 |
| BR_10 | The responsibility split between the software product and the fixed measurement devices (including fault-detection duties) must be contractually documented in the interface definitions. | An undocumented liability boundary leaves the legal manufacturer exposed for failures originating in equipment outside its design control. | Legal & Compliance | High | KA_05, KA_10 |
| BR_11 | The capability must be delivered as software only, running on existing, unmodified monitoring hardware and the installed base of non-invasive measurement devices, through standardised, published device interfaces that permit supplier substitution. | Protects customer and manufacturer investment, avoids vendor lock-in objections in tenders, and keeps capital cost and time-to-market inside the business case. | Hospital Procurement / Finance | Critical | KA_10 |
| BR_12 | Real-time integration with all six measurement-device classes and the external information-system interfaces must be retired as a risk through early prototyping and prioritised interface-control definition, ahead of committed development milestones. | Device and hospital connectivity is the highest-probability project risk; late integration failures threaten the launch date and the submission baseline. | R&D Management | High | KA_01, KA_09, KA_10 |
| BR_13 | Continuous multi-parameter monitoring must be operational within seconds of patient connection and remain uninterrupted across transport and handover; monitoring and alarming must remain fully functional without external network connectivity, with intermittent connectivity affecting only optional hospital data sharing. | Continuous visibility from first patient contact is the baseline clinical value the buyer pays for; in mobile pre-hospital use no external network can be assumed, so the safety-relevant capability must be locally autonomous and only the hospital-sharing capability may degrade. | Clinician / Hospital Procurement | High | KA_01 |
| BR_14 | Patient data and diagnostic findings must be shareable with receiving hospital information systems over established healthcare interoperability standards (e.g. HL7/FHIR), with the protocol choice and interface agreements fixed early and no bespoke per-site integration projects. | Enables second opinion and prepared handover while avoiding custom IT project cost and open-ended integration liability. | Hospital Procurement | High | KA_09 |
| BR_15 | The product must be developed under a usability engineering process per IEC 62366-1, with summative evaluation of safety-related use scenarios covering mobile, poorly lit, and high-noise use contexts, operable with standard clinical training only. | Use errors in high-stress mobile contexts are safety-relevant, and summative usability evidence is a market-access prerequisite. | Regulatory Affairs / Clinician | High | KA_08 |
| BR_16 | A safe training and simulation capability, delivered with a structured vendor training offering, must be in place as a formal risk control before release — it is a release condition, not an optional add-on. | Training is the designated risk control for the critical-severity misinterpretation hazard; under-resourcing it converts into use-error complaints, field actions, and foreseeable-misuse liability. | Training Organisation / Legal Manufacturer | High | KA_11 |
| BR_17 | Documented cybersecurity risk management and protection of personal health data compliant with applicable data-protection law (e.g. GDPR, HIPAA) must cover all data processed, displayed, or transmitted to external health-information systems, sufficient to pass hospital IT security review. | Failing IT security review blocks procurement regardless of clinical merit; breaches create patient-safety, regulatory, and liability harm. | IT Security Officer / Data Protection Officer | Critical | KA_14 |
| BR_18 | Valid regulatory clearance for the diagnostic-support claim must be in place in each target market at the time of sale, with regulatory engagement started early enough to keep clearance off the critical path. | Clearance at time of purchase is a hard procurement criterion and clearance timing is a recognised high-impact schedule risk. | Hospital Procurement / Competent Authority | Critical | KA_12, KA_02 |
| BR_19 | The product must be field-maintainable and updatable across a 7–10 year service life through software updates alone — requiring no modification of the existing hardware platform or measurement devices — with committed security patches and regulatory maintenance deliverable within the existing support organisation's capacity and competence without major new hiring. | Protects the customer's multi-year investment and the manufacturer's service margin; an unsupportable product shifts lifecycle cost onto the customer and breaches expectations baked into the tender. | Service Organisation | High | KA_15 |
| BR_20 | An operational post-market surveillance and vigilance capability must be in place from launch and sustained until the product is withdrawn from the market, including an orderly end-of-life process for data, installed base, and obligations. | Surveillance and vigilance are statutory obligations for as long as the product remains on the market; an unmanaged end of life leaves residual regulatory and data-protection exposure. | Quality Management (Legal Manufacturer) | Critical | KA_15 |
| BR_21 | The first release must ship a frozen, validated scope, with unproven capabilities explicitly deferred to later releases under documented scope governance. | A frozen baseline is what makes the regulatory submission, verification, and launch dates credible; uncontrolled scope growth threatens all three. | Programme Management | High | KA_16 |
| BR_22 | Total cost of ownership must be predictable over the full service life and transparently itemisable for tender evaluation — covering licences, deployment, training, support, and updates — with pricing competitive with comparable monitoring and decision-support offerings. | Buying organisations evaluate tenders on disclosed lifetime cost, not list price; an opaque or uncompetitive cost position loses the tender on commercial grounds regardless of clinical merit. | Sales & Marketing / Finance / Hospital Procurement | High | KA_16 |
| BR_23 | The purchasing organisation must retain ownership of all patient data and clinical records produced during use, with the ability to export that data in established healthcare interoperability formats throughout the service life and at end of contract or end of life, without dependency on the supplier. | Data ownership and exit-without-lock-in are standard contractual conditions in healthcare procurement; a buyer who cannot retrieve its own clinical data will not sign, and stranded data at end of life creates regulatory and continuity exposure for the buyer. | Hospital Procurement / Data Protection Officer | High | KA_14, KA_15 |
| BR_24 | Support and maintenance commitments — response times for clinically relevant defects, security-patch delivery timelines, and update cadence — must be contractually specifiable as service levels the buying organisation can hold the supplier to across the service life. | Buyers of safety-relevant clinical equipment require enforceable service-level commitments in the purchase contract, not best-effort support; absence of committable service levels is a tender disqualifier for hospital and EMS fleet operators. | Hospital Procurement / Service Organisation | High | KA_15 |

## Context (FORMAL)

The context level is the start of the solution domain (DHF), based on the problem domain and the stakeholder expectations.

### Intended Use (IU_01)

Write the intended use as a single, flowing prose statement that naturally covers the five aspects — what the product is, what it does (medical indication), who uses it (user profile), where it is used (use environment), and how it works (operating principle). Do **not** add bold labels or headers for the aspects; weave them into the sentences.

| ID | Description |
|----|-------------|
| IU_01 | The Mobile Monitoring Software Solution (MMSS) is medical device software running on an existing portable patient monitor that provides continuous, real-time monitoring of key vital signs of critically ill patients and offers clinical decision support by presenting ranked, real-time diagnostic candidates alongside the vital signs; the diagnostic output is advisory only — it does not provide an autonomous diagnosis, and the final diagnostic and treatment decisions remain at all times with the attending clinician. It is intended to be used exclusively by trained medical professionals in critical care environments, including intensive care units, emergency rooms, and mobile or pre-hospital medical units. The software operates by acquiring physiological data non-invasively from six connected measurement device types (ECG monitor, pulse oximeter, blood pressure monitor, thermal probe, capnometer, and EEG monitor) through standardised interfaces, processing this data through a commercially validated AI analysis engine, presenting the vital signs and ranked diagnostic candidates on the connected monitor display, generating clinical alarms for abnormal patient conditions and for sensor or connection faults, and optionally sharing diagnostic candidates with hospital information systems to obtain a second opinion. |

### Medical Device Classification (MD_01)

| ID | Description | Traces |
|----|-------------|--------|
| MD_01 | Per IEC 62304 (ANSI/AAMI), the MMSS software is initially assessed as software safety Class C, because a failure of the monitoring, alarming, or diagnostic-support software could contribute to death of a critically ill patient as described in the intended use (IU_01). The classification is mitigated to Class B through risk-control measures external to the MMSS software, in accordance with the IEC 62304 classification rules: the measurement devices independently detect sensor misplacement and connection failure and generate their own audible alarms, and the external ALGOS diagnostic engine independently issues an audible notification on diagnosis timeout. Because these independent external systems control the death-of-patient hazards, a failure of the MMSS software alone cannot result in death or irreversible injury, and the residual software safety classification is Class B. | IU_01 |

### Context Diagram

The context diagram identifies the system of interest in relation to its context. The system of interest contains all elements that are part of the design.

_To be added_

#### Product Information

The Mobile Monitoring Software Solution (MMSS) is medical device software (IEC 62304, Class C mitigated to Class B) that runs on an existing portable patient monitor and transforms it from a passive vital signs display into an active clinical decision-support tool. It delivers continuous, real-time vital signs presentation, clinical alarms for abnormal patient conditions and sensor/connection faults, and ranked, real-time diagnostic candidates produced by a commercially validated external AI diagnostic engine. MMSS operates by acquiring physiological data from six fixed, non-invasive measurement device types through their published interfaces, processing and presenting this data on the connected monitor display within a 1-second display latency budget, forwarding the acquired data to the AI engine and rendering the returned diagnostic candidates, and optionally sharing diagnostic candidates with a hospital information system for a second opinion. All hardware — host CPU platform, measurement devices, display, and enclosure — is existing and fixed; MMSS is the software product only.

#### System of Interest

The part of the broader system this document is about — the product, subsystem, or component you are responsible for designing.

| System Element | Description |
|----------------|-------------|
| MMSS software | The complete Mobile Monitoring Software Solution: the application software stack running on the existing portable patient monitor, covering measurement-device data acquisition, data processing, interfacing with the external AI diagnostic engine, vital signs and diagnostic candidate presentation, clinical alarm generation, and optional hospital information system integration. The SOI is the software product as a whole; no hardware is part of the design. |

#### Context Elements

Essential elements for your product that are not part of the design.

| Context Element | Description |
|-----------------|-------------|
| Host CPU platform | Existing compact embedded CPU with real-time OS capabilities on which the MMSS software executes; fixed hardware, outside the design. |
| ECG monitor | Existing non-invasive measurement device providing electrocardiogram data; fixed behaviour, accessed through its published interface; generates its own independent audible alarms and auto-detects sensor misplacement. |
| Pulse oximeter | Existing non-invasive measurement device providing oxygen saturation and pulse rate; fixed behaviour, accessed through its published interface; independent audible alarms and misplacement detection. |
| Blood pressure monitor | Existing non-invasive measurement device providing blood pressure values; fixed behaviour, accessed through its published interface; independent audible alarms and misplacement detection. |
| Thermal probe | Existing non-invasive measurement device providing body temperature; fixed behaviour, accessed through its published interface; independent audible alarms and misplacement detection. |
| Capnometer | Existing non-invasive measurement device providing end-tidal CO2 and respiratory data; fixed behaviour, accessed through its published interface; independent audible alarms and misplacement detection. |
| EEG monitor | Existing non-invasive measurement device providing electroencephalogram data; fixed behaviour, accessed through its published interface; independent audible alarms and misplacement detection. |
| Monitor display | Existing display of the portable patient monitor on which MMSS presents vital signs, alarms, and diagnostic candidates; fixed hardware. |
| AI diagnostic engine (ALGOS / Open Evidence) | External, commercially validated off-the-shelf AI diagnostic engine. MMSS supplies it with acquired patient data and receives structured, ranked diagnostic candidates; convergence within 2 minutes is an ALGOS budget, and ALGOS independently issues an audible notification on diagnosis timeout. |
| Hospital information system (HIS) | External hospital system with which MMSS optionally shares diagnostic candidates to obtain a second opinion; interface protocol TBD (HL7/FHIR). |
| Clinician user | Trained medical professional who operates the monitor, observes vital signs, alarms, and diagnostic candidates, and retains final diagnostic and treatment responsibility. |
| Patient | Critically ill patient being monitored; the measurement subject. The patient is connected to the measurement devices, not directly to the MMSS software. |

#### External Interfaces (IF_*)

Connections between the system of interest and the context elements (mechanical, chemical, electronic, digital, logical, etc.).

| ID | Name | Port 1 | Port 2 | ICD |
|----|------|--------|--------|-----|
| IF_01 | ECG acquisition interface | MMSS software | ECG monitor | Published device ICD (existing) |
| IF_02 | Pulse oximeter acquisition interface | MMSS software | Pulse oximeter | Published device ICD (existing) |
| IF_03 | Blood pressure acquisition interface | MMSS software | Blood pressure monitor | Published device ICD (existing) |
| IF_04 | Temperature acquisition interface | MMSS software | Thermal probe | Published device ICD (existing) |
| IF_05 | Capnometry acquisition interface | MMSS software | Capnometer | Published device ICD (existing) |
| IF_06 | EEG acquisition interface | MMSS software | EEG monitor | Published device ICD (existing) |
| IF_07 | Display presentation interface | MMSS software | Monitor display | Display interface of the existing monitor platform (existing) |
| IF_08 | AI diagnostic engine interface | MMSS software | AI diagnostic engine (ALGOS / Open Evidence) | Open Evidence library interface specification (existing, off-the-shelf); structured diagnostic candidate format |
| IF_09 | Hospital information system interface | MMSS software | Hospital information system (HIS) | TBD — protocol HL7 or FHIR; ICD to be defined |
| IF_10 | Clinician interaction interface | MMSS software | Clinician user | MMSS user interface specification (to be produced in this project) |
| IF_11 | Host platform execution interface | MMSS software | Host CPU platform | Real-time OS / platform API of the existing embedded CPU (existing) |

#### Acquired Parameters / Signals

Whenever the product acquires, exchanges, or presents a **set** of parameters, signals, or data items from a set of source elements (measurement devices, sensors, sub-systems, services), enumerate that set here instead of leaving it as a collective phrase elsewhere. One row per source-element/parameter combination, taken from the input. If no such parameter set applies to this product, write `_Not applicable_`.

| Source Element | Parameter / Signal | Unit / Typical Range | Interface |
|----------------|--------------------|----------------------|-----------|
| ECG monitor | Heart rate | bpm; typical adult range 30–250 | IF_01 |
| ECG monitor | ECG waveform | mV; surface-ECG amplitude approx. 0.1–5 mV | IF_01 |
| Pulse oximeter | Oxygen saturation (SpO2) | %; clinical display range 70–100 | IF_02 |
| Pulse oximeter | Pulse rate | bpm; typical adult range 30–250 | IF_02 |
| Blood pressure monitor | Systolic blood pressure | mmHg; typical adult range 60–250 | IF_03 |
| Blood pressure monitor | Diastolic blood pressure | mmHg; typical adult range 30–150 | IF_03 |
| Blood pressure monitor | Mean arterial pressure (MAP) | mmHg; typical adult range 40–180 | IF_03 |
| Thermal probe | Body temperature | °C; clinical range 30–43 | IF_04 |
| Capnometer | End-tidal CO2 (EtCO2) | mmHg; display range 0–100, normal 35–45 | IF_05 |
| Capnometer | Respiratory rate | breaths/min; typical adult range 4–60 | IF_05 |
| EEG monitor | EEG waveform | µV; scalp-EEG amplitude approx. 10–200 µV | IF_06 |

## Users

### User Groups

Collections of users who share common characteristics (a synonym is User Role).

| User | User Group | User Profile |
|------|------------|--------------|
| Paramedic / EMS Clinician | Pre-hospital Care Provider | Certified paramedic or emergency medical technician trained in advanced life support; operates the MMSS in mobile medical units and ambulances under time pressure, vibration, noise, and variable lighting; connects the measurement devices to the patient, monitors vital signs, and responds to alarms and AI diagnostic candidates en route to hospital. |
| Emergency Physician | Emergency Department Clinician | Licensed physician specialised in emergency medicine; uses the MMSS in the emergency room during patient reception, triage, and stabilisation; interprets vital signs trends and ranked AI diagnostic candidates as advisory input while retaining full diagnostic and treatment authority. |
| Emergency / ICU Nurse | Critical Care Nurse | Registered nurse with critical care or emergency training; performs continuous bedside monitoring in ICU and emergency settings; attaches and repositions sensors, acknowledges and escalates alarms, and is typically the first responder to sensor-fault and connection alarms. |
| Intensivist / ICU Physician | Intensive Care Clinician | Board-certified intensive care physician; uses the MMSS in the ICU for continuous surveillance of critically ill patients; correlates vital signs and AI diagnostic candidates with the broader clinical picture and directs the treatment plan. |
| Hospital Clinician (Second Opinion) | Remote Consulting Clinician | Physician within the hospital who receives MMSS diagnostic candidates and vital signs via the hospital information system; reviews shared data away from the patient to provide a second opinion to the on-scene or bedside clinician. |
| Clinical Trainer / Trainee | Simulation Training User | Trained medical professional acting as instructor, or clinician in training, using the MMSS mandatory simulation training mode; rehearses device connection, alarm handling, and correct interpretation of AI diagnostic candidates in a non-clinical setting before live use. |

### User Requirements / Needs (UR_*)

The user expectations translated over the product context into requirements specific to YOUR product. They are SMARTER than the expectations and form the base for product validation. Format: *As a \<user group\> I want \<feature\> so that \<benefit\>.*

| ID | Description | Classification | Traces |
|----|-------------|----------------|--------|
| UR_01 | As a Pre-hospital Care Provider I want the MMSS to be fully operational, with live vital signs visible, within 10 seconds of system activation so that monitoring starts at first patient contact without delaying care. | Safety-critical | IU_01, BR_13 |
| UR_02 | As a Pre-hospital Care Provider I want continuous, real-time display of all parameters enumerated in the Acquired Parameters / Signals table (Context section), each presented within 1 second of acquisition, so that I always act on the patient's current physiological state. | Safety-critical | IU_01, BR_13 |
| UR_03 | As a Pre-hospital Care Provider I want monitoring, alarming, and diagnostic support to remain fully functional without any external network connection so that patient safety in the ambulance never depends on connectivity that cannot be assumed. | Safety-critical | IU_01, BR_13 |
| UR_04 | As an Intensive Care Clinician I want monitoring to continue uninterrupted across patient transport and handover between care settings so that no observation gap occurs at the moments of highest clinical risk. | Safety-critical | IU_01, BR_13 |
| UR_05 | As an Emergency Department Clinician I want ranked, likelihood-ordered diagnostic candidates presented alongside the vital signs, updated in real time as new data arrives, so that my differential diagnosis is supported at the point of care without leaving the patient. | High | IU_01, BR_05 |
| UR_06 | As an Emergency Department Clinician I want every diagnostic candidate to be visually and semantically distinct from measured clinical facts and explicitly labelled as advisory so that I remain the final decision-maker and am not misled into treating a suggestion as a finding. | Safety-critical | IU_01, BR_06 |
| UR_07 | As a Critical Care Nurse I want an immediate, unmistakable alarm within 1 second of detection of any abnormal vital sign, clearly identifying which vital sign is abnormal, so that I can intervene before the patient's condition deteriorates further without first having to search the display for the cause. | Safety-critical | IU_01, BR_08 |
| UR_08 | As a Critical Care Nurse I want physiological alarms to be perceivable — audibly and visually — even when my attention is elsewhere on the patient or I am away from the display, so that no abnormal condition goes unnoticed at the bedside. | Safety-critical | IU_01, BR_08 |
| UR_09 | As a Critical Care Nurse I want a sensor disconnection alarm presented within 1 second after 5 seconds of signal inactivity from any of the connected measurement devices listed in the Acquired Parameters / Signals table (Context section), so that I never mistake a silent, stale reading for a stable patient. | Safety-critical | IU_01, BR_09 |
| UR_10 | As a Critical Care Nurse I want sensor misplacement and unreliable readings, as reported by the measurement devices, to be unambiguously annunciated and clearly attributed to the affected sensor so that I can correct the sensor instead of acting on false data. | Safety-critical | IU_01, BR_09 |
| UR_11 | As an Emergency Department Clinician I want an active, clearly perceivable notification whenever diagnostic guidance has not converged within its expected 2-minute window or is otherwise unavailable so that I fall back to unaided clinical assessment immediately instead of waiting on support that will not arrive. | Safety-critical | IU_01, BR_07 |
| UR_12 | As a Pre-hospital Care Provider I want vital signs, alarms, and diagnostic candidates to be readable at a glance from working distance in a moving vehicle, in poor lighting, and in bright sunlight so that I can monitor the patient without stopping hands-on care. | High | IU_01, BR_15 |
| UR_13 | As a Pre-hospital Care Provider I want alarm annunciation that remains perceivable in the high-noise environment of a mobile medical unit so that sirens, road noise, and the engine never mask a clinically relevant alarm. | Safety-critical | IU_01, BR_08, BR_15 |
| UR_14 | As a Critical Care Nurse I want every routine task — activation, alarm acknowledgement, and reviewing diagnostic candidates — to be operable in a minimal number of steps with standard clinical training only, so that the interface never competes with the patient for my attention. | High | IU_01, BR_15 |
| UR_15 | As an Emergency Department Clinician I want to share the current vital signs and diagnostic candidates with the hospital information system in a single action, with transfer completing within 1 second, so that a second opinion can be obtained without interrupting patient care. | High | IU_01, BR_14 |
| UR_16 | As a Remote Consulting Clinician I want to receive the shared vital signs and diagnostic candidates through the hospital information system in an established interoperability format (e.g. HL7/FHIR) so that I can review the case away from the patient and return a timely second opinion. | High | IU_01, BR_14 |
| UR_17 | As a Pre-hospital Care Provider I want temporary loss of hospital connectivity to affect only the optional data sharing — never monitoring, alarming, or diagnostic display — and to be clearly indicated as a sharing-only limitation, so that I know exactly which capability is degraded. | High | IU_01, BR_13, BR_14 |
| UR_18 | As a Simulation Training User I want a simulation training mode in which I can rehearse device connection, alarm handling, and interpretation of AI diagnostic candidates with realistic scenarios so that I reach competence and justified trust before using the system on real patients. | High | IU_01, BR_16 |
| UR_19 | As a Simulation Training User I want the simulation mode to be unmistakably distinguished from live clinical operation at all times, and impossible to confuse with it, so that simulated data can never be mistaken for a real patient or vice versa. | Safety-critical | IU_01, BR_16 |
| UR_20 | As an Intensive Care Clinician I want the source and validation status of the diagnostic intelligence (the commercially validated AI engine) to be transparently identified in the product information so that I can judge the weight to give its advisory candidates within the broader clinical picture. | Medium | IU_01, BR_04, BR_06 |
| UR_21 | As a Critical Care Nurse I want physiological alarms (abnormal vital signs) to be clearly distinguishable — by distinct audible and visual signatures — from technical alarms (sensor disconnection, misplacement, or fault) so that I can triage my response by sound alone in a busy unit and never treat a patient-critical alarm with the urgency of a cable problem, or vice versa. | Safety-critical | IU_01, BR_08, BR_09 |
| UR_22 | As an Emergency Department Clinician I want to review the recent trend of each monitored vital sign over the course of the episode, alongside the current values, so that I can recognise gradual deterioration and receive a patient at handover with the physiological course en route visible, not just a snapshot. | High | IU_01, BR_13 |

### User DFMEA (USER_DFMEA_*)

A structured analysis of how users might misuse, misinterpret, or fail to operate the product, the consequences, and the mitigations the design must include.

| ID | Item/Function | Requirement | Failure Mode | End-effect | Rationale | Failure Cause | Severity | Prevention | Classification | Traces |
|----|---------------|-------------|--------------|------------|-----------|---------------|----------|------------|----------------|--------|
| USER_DFMEA_01 | AI diagnostic candidate presentation | UR_06: diagnostic candidates visually and semantically distinct from measured facts and labelled advisory | Clinician treats an AI diagnostic candidate as a confirmed clinical finding and initiates treatment on it without independent assessment | Wrong or premature treatment of the patient; potential serious patient harm | Risk register R_05 identifies clinician misinterpretation of AI candidates as a Critical risk; automation bias is a well-documented human factor with decision-support tools | Candidate rendering resembles measured data; advisory labelling absent, subtle, or habitually ignored under time pressure | Critical | Persistent, non-dismissible advisory labelling; visual segregation of candidates from vitals (separate zone, distinct styling); mandatory simulation training on candidate interpretation before live use | Safety-critical | UR_06 |
| USER_DFMEA_02 | AI diagnostic candidate ranking | UR_05: ranked, likelihood-ordered candidates updated in real time | Clinician fixates on the top-ranked candidate and discards lower-ranked alternatives that match the patient (anchoring) | Correct diagnosis overlooked; delayed or wrong treatment | Likelihood ordering invites anchoring on rank 1; ranking is probabilistic support, not exclusion of alternatives | Rank presentation overstates certainty; likelihood differences between candidates not perceivable | Critical | Display relative likelihood indication per candidate, not bare ordinal rank; show multiple candidates with comparable prominence when likelihoods are close; training-mode scenarios where the correct diagnosis is not rank 1 | High | UR_05, UR_06 |
| USER_DFMEA_03 | Physiological alarm annunciation | UR_07, UR_08: unmistakable alarm within 1 s, perceivable when attention is elsewhere | Caregiver does not perceive an abnormal-vital-sign alarm while performing hands-on care away from the display | Intervention delayed; patient deterioration progresses unobserved | Bedside and pre-hospital caregivers routinely work eyes-off-display; a visual-only or quiet alarm fails exactly when needed most | Alarm volume/salience insufficient; caregiver positioned away from display; concurrent task load | Critical | Redundant audible + visual annunciation; alarm sound levels and tone signatures per alarm standard (IEC 60601-1-8 alignment); alarm light visible from wide angle | Safety-critical | UR_07, UR_08 |
| USER_DFMEA_04 | Alarm annunciation in mobile unit | UR_13: alarms perceivable in high-noise mobile environment | Alarm masked by siren, engine, and road noise in a moving ambulance and goes unnoticed | Abnormal condition or sensor fault unnoticed during transport; missed intervention window | Ambulance ambient noise can exceed typical alarm sound pressure; R_07 rates an undetected failure during monitoring as Critical | Alarm acoustic design not validated against mobile-unit noise spectrum; speaker output fixed too low | Critical | Validate alarm audibility against representative ambulance noise profiles; high-contrast full-screen visual alarm component as redundant channel; usability testing in simulated transport conditions | Safety-critical | UR_13, UR_08 |
| USER_DFMEA_05 | Sensor disconnection detection | UR_09: disconnection alarm within 1 s after 5 s signal inactivity | Caregiver interprets a frozen, stale vital-sign value as a current, stable reading | Silent monitoring gap; deterioration missed while display shows reassuring numbers | R_07: connection failure not detected → missed vital signs, rated Critical; a stale value is more dangerous than a blank one | Disconnection not annunciated prominently; stale value remains on screen visually identical to live data | Critical | Visually invalidate stale values immediately (blank/strike/grey with timestamp); distinct technical alarm for disconnection; never display a non-live value in the live-data style | Safety-critical | UR_09 |
| USER_DFMEA_06 | Sensor placement and signal quality | UR_10: misplacement and unreliable readings unambiguously annunciated and attributed | Caregiver does not recognise that a sensor is misplaced and acts on physiologically false data | Wrong diagnosis or wrong treatment based on corrupted input; AI candidates also corrupted downstream | R_04: sensor misplacement not detected → wrong diagnosis, rated Critical; misplaced sensors often still produce plausible-looking values | Misplacement annunciation generic (not attributed to the affected sensor); caregiver assumes device-side detection covers all cases | Critical | Attribute every misplacement/quality alarm to the specific sensor with corrective guidance; flag affected parameters as unreliable on the display; suppress AI candidate updates flagged as derived from unreliable input | Safety-critical | UR_10 |
| USER_DFMEA_07 | Alarm acknowledgement / silencing | UR_07, UR_14: alarm identifies the abnormal vital sign; routine tasks operable in minimal steps | Caregiver silences or acknowledges an alarm reflexively without identifying and addressing its cause (alarm fatigue) | Underlying abnormal condition persists unaddressed; subsequent identical alarm also dismissed | Alarm fatigue is a leading documented cause of monitoring-related patient harm; acknowledgement must not equal resolution | High alarm frequency; acknowledgement gesture too easy relative to cause review; cause not shown at acknowledgement point | Critical | Show the triggering vital sign and value in the acknowledgement interaction itself; time-limited silencing with automatic re-annunciation while the condition persists; no global permanent alarm-off in live mode | Safety-critical | UR_07, UR_14 |
| USER_DFMEA_08 | Physiological vs technical alarm differentiation | UR_21: distinct audible and visual signatures for physiological vs technical alarms | Caregiver mistakes a patient-critical physiological alarm for a routine technical (cable/sensor) alarm and deprioritises it | Delayed response to a life-threatening condition | UR_21 exists precisely because triage-by-sound is how nurses operate in busy units; signature confusion inverts clinical priority | Audible signatures insufficiently distinct; visual coding inconsistent between alarm classes | Critical | Distinct, standard-aligned tone families and colour coding per alarm class; consistency verified in usability testing by sound-only identification tasks | Safety-critical | UR_21 |
| USER_DFMEA_09 | Diagnostic convergence timeout | UR_11: active notification when diagnosis has not converged within 2 minutes or is unavailable | Clinician keeps waiting for diagnostic support that will not arrive instead of falling back to unaided assessment | Treatment delayed in a time-critical situation | R_06: diagnosis timeout not communicated → delay of treatment, rated Critical; absence of output is inherently easy to miss | Timeout indication passive or absent on the MMSS display; clinician's attention on the patient, not on the elapsed time | Critical | Active audible + visual timeout notification on MMSS (in addition to the independent ALGOS notification); diagnostic area explicitly states "no converged diagnosis — continue clinical assessment" | Safety-critical | UR_11 |
| USER_DFMEA_10 | System activation under time pressure | UR_01, UR_14: operational within 10 s; routine tasks in minimal steps with standard training | Provider mis-sequences or stalls activation/setup steps at first patient contact under acute time pressure | Monitoring start delayed; first minutes of a critical episode unrecorded and unsupported | Pre-hospital first contact is the highest-stress moment of use; every extra decision point is an error opportunity | Activation requires configuration choices; unclear progress feedback; steps differ from trained sequence | High | Single-action activation to a safe live-monitoring default; clear progress indication during the ≤10 s start-up; no configuration decisions required before monitoring begins | Safety-critical | UR_01, UR_14 |
| USER_DFMEA_11 | Simulation training mode | UR_19: simulation mode unmistakably distinguished from live operation | User runs a live patient session while the system is in simulation mode (or vice versa) without noticing | Live patient unmonitored while display shows simulated data — or simulated data acted on as real; severe patient harm potential | Mode error is a classic catastrophic use error; UR_19 is Safety-critical for exactly this reason | Mode indication subtle or only shown at entry; simulation visuals identical to live visuals; device handed over between users mid-session | Critical | Persistent full-perimeter simulation watermark/banner on every screen; distinct colour scheme in simulation; deliberate confirmation to enter, automatic prominent exit prompt; live sensor connection blocked or flagged while in simulation | Safety-critical | UR_19 |
| USER_DFMEA_12 | Training transfer to live use | UR_18: rehearse connection, alarms, and AI candidate interpretation with realistic scenarios | User skips or only partially completes simulation training and operates the live system without justified competence | Untrained interpretation errors in live use — compounding every other failure mode in this table | R_05 mitigation mandates simulation training; an optional or skippable training mode does not mitigate | Training not enforced organisationally; scenarios unrealistic so competence is illusory | High | Scenario coverage spanning alarm handling, sensor faults, timeout, and misleading AI rankings; completion tracking available to the operating organisation; product information states training prerequisite | High | UR_18 |
| USER_DFMEA_13 | Hospital data sharing (sender side) | UR_15, UR_17: single-action sharing; connectivity loss indicated as sharing-only limitation | Provider believes data was shared with the hospital when transfer silently failed (or vice versa, repeats sends) | Second opinion never arrives or is based on absent data; receiving team prepares on wrong information | Handover decisions build on the assumption that the hospital has seen the data; a silent failure breaks that assumption invisibly | Transfer result not confirmed on screen; connectivity loss not surfaced at the moment of sending | High | Explicit per-transfer success/failure confirmation with timestamp; persistent sharing-degraded indicator while offline; queued-transfer status visible | High | UR_15, UR_17 |
| USER_DFMEA_14 | Hospital data review (receiver side) | UR_16: shared vitals and candidates received in established interoperability format | Remote clinician treats a shared snapshot as the patient's live current state, or misreads candidates stripped of their advisory context | Second opinion based on outdated or misframed data; conflicting guidance returned to the bedside | Data crossing the HIS boundary loses the MMSS display context (timestamps, advisory labelling, signal-quality flags) unless explicitly carried | Shared payload omits acquisition timestamps, advisory labelling, or sensor-reliability flags; HIS rendering not controlled by MMSS | High | Embed acquisition timestamp, advisory disclaimer, and signal-quality status in every shared payload as inseparable data fields; sharing format (HL7/FHIR) profile mandates these fields | High | UR_16 |
| USER_DFMEA_15 | Display readability in field conditions | UR_12: readable at working distance in a moving vehicle, poor lighting, and bright sunlight | Provider misreads a vital-sign value or alarm cue due to glare, vibration, or low light | Wrong value acted on, or abnormal value not recognised; clinically equivalent to an alarm not perceived | Pre-hospital lighting and motion are uncontrollable; a value misread is as harmful as a value not shown — a misread SpO2 or blood pressure in transit drives treatment directly | Font size/contrast inadequate for working distance; no high-brightness/high-contrast mode; colour-only coding fails in glare | Critical | Minimum character heights and contrast ratios for working distance; redundant coding (colour + shape/position) for all safety information; readability validated in simulated sunlight, night, and motion conditions | High | UR_12 |
| USER_DFMEA_16 | Trend review at handover | UR_22: recent trend of each vital sign visible alongside current values | Receiving clinician judges the patient on a current-value snapshot, missing gradual deterioration en route | Deterioration trajectory missed at handover; treatment priority set wrongly | Handover is a known information-loss point; a stable instantaneous value can mask a steep negative trend | Trend view hidden behind navigation; trend timescale or axis scaling misleading | High | Trend access in one action from the main screen; consistent, labelled timescales and scaling; episode trend automatically presented in the handover/sharing view | High | UR_22 |
| USER_DFMEA_17 | AI source and validation transparency | UR_20: source and validation status of the diagnostic engine transparently identified | Clinician assigns the wrong evidentiary weight to AI candidates because the engine's nature and validation scope are unknown to them | Systematic over-trust (or dismissal) of diagnostic support across all uses | Calibrated trust requires knowing what the advice is based on; UR_20 makes this product information, not tribal knowledge | Validation status buried in documentation; not accessible from the diagnostic display | Medium | Engine identity and validation status accessible directly from the diagnostic candidate area; covered explicitly in simulation training content | Medium | UR_20 |
| USER_DFMEA_18 | Continuity across transport and handover | UR_04: monitoring uninterrupted across transport and handover | User inadvertently interrupts monitoring (power, mode, or sensor handling) during patient movement, assuming the system tolerates it | Observation gap at the moment of highest clinical risk; episode trend broken | Transport/handover involves physical manipulation of patient, sensors, and device simultaneously — peak opportunity for inadvertent interruption | Accidental power/standby actuation; intentional sensor swap interpreted by the user as "system handles it" while alarms are silenced | High | Guarded/confirmed shutdown and standby actions in live mode; explicit "monitoring interrupted" state with prominent resume path; episode data preserved across interruptions | Safety-critical | UR_04 |
| USER_DFMEA_19 | Patient changeover / episode start | UR_01, UR_22: operational within 10 s of activation; trend reflects the current patient's episode | Provider connects a new patient without starting a new episode, so trends and AI diagnostic input silently mix the previous patient's data with the new patient's | Trend view and AI candidates computed on cross-patient data; wrong diagnosis or wrong triage of the new patient | Back-to-back use on consecutive patients is routine in pre-hospital and ED practice; carried-over data is invisible contamination because every displayed value still looks plausible | No enforced new-patient/episode step on reconnection; under time pressure the provider attaches sensors and resumes; device handed between crews mid-shift | Critical | Detect an all-sensors-disconnected interval and require an explicit new-patient/same-patient confirmation before resuming trends and AI analysis; mark episode start time visibly on the trend view; never feed cross-episode data to the AI engine | Safety-critical | UR_01, UR_22 |

### Use Scenarios

Concrete narratives of how the product is used in the real world, walking from a triggering situation to a successful outcome. Each scenario contains use tasks (UT_*).

#### Scenario 1 — Emergency Deployment and Patient Connection in a Mobile Medical Unit

A paramedic crew reaches a critically ill patient at the roadside. The MMSS-equipped portable monitor must go from cold start to live multi-parameter monitoring at first patient contact, with no reliance on any external network.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_01 | Activate the system | The Pre-hospital Care Provider powers on the monitor at first patient contact and observes the MMSS reach full operational readiness, with the live vital signs view presented, within 10 seconds. | UR_01 |
| UT_02 | Connect measurement devices | The provider attaches the clinically indicated non-invasive sensors from the device set enumerated in the Acquired Parameters / Signals table (Context section) to the patient and confirms each device is recognised by the MMSS. | UR_02 |
| UT_03 | Verify live vital signs | The provider checks that every connected parameter appears on the display within 1 second of acquisition and is readable at a glance from working distance in the vehicle's lighting conditions. | UR_02, UR_12 |
| UT_04 | Operate standalone at the scene | With no hospital or network connection available at the roadside, the provider simply continues working — monitoring, alarming, and diagnostic support all remain fully functional without connectivity and without any action or configuration on the provider's part. | UR_03 |

#### Scenario 2 — Continuous Monitoring with AI Diagnostic Support En Route

During transport, the clinician monitors the patient hands-on while the AI engine converges on ranked diagnostic candidates, which must support — never replace — the clinician's own differential diagnosis.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_05 | Monitor vital signs at a glance | The Pre-hospital Care Provider repeatedly glances at the display from working distance in the moving vehicle — in poor lighting and bright sunlight — and reads the current values of all acquired parameters without interrupting hands-on care. | UR_02, UR_12 |
| UT_06 | Review ranked diagnostic candidates | The clinician reviews the likelihood-ordered diagnostic candidates presented alongside the vital signs and observes them update in real time as new measurement data arrives. | UR_05 |
| UT_07 | Distinguish advisory output from measured facts | The clinician verifies that every diagnostic candidate is visually and semantically distinct from measured vital signs and explicitly labelled as advisory, and forms their own clinical judgement accordingly. | UR_06 |
| UT_08 | Review vital sign trends | The clinician opens the recent trend of each monitored vital sign over the episode, alongside the current values, to recognise gradual deterioration en route. | UR_22 |
| UT_09 | Check the diagnostic source identification | At a calm moment outside hands-on care — during familiarisation or between deployments, not while treating in the moving vehicle — the clinician consults the product information to confirm the source and validation status of the AI diagnostic engine, informing the weight given to its advisory candidates in later episodes. | UR_20 |

#### Scenario 3 — Abnormal Vital Sign Alarm Response

While the clinician's attention is on an intervention, a vital sign crosses an alarm limit. The alarm must cut through the high-noise environment, identify its cause instantly, and be handled in minimal steps.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_10 | Perceive the physiological alarm | The Critical Care Nurse, attending to the patient away from the display amid siren and road noise, perceives the audible and visual alarm annunciated within 1 second of detection of the abnormal vital sign. | UR_07, UR_08, UR_13 |
| UT_12 | Triage the alarm by its signature | While still hands-on with the patient and before reaching the display, the nurse recognises by sound alone that the alarm is physiological rather than technical and assigns it patient-critical urgency. | UR_21 |
| UT_11 | Identify the abnormal vital sign | The nurse then turns to the display and immediately identifies which vital sign is abnormal, without searching the screen for the cause. | UR_07 |
| UT_13 | Acknowledge the alarm | After initiating clinical intervention, the nurse acknowledges the alarm in a minimal number of steps using standard clinical training only. | UR_14 |
| UT_14 | Confirm continued monitoring | The nurse verifies that real-time display of all acquired parameters continues uninterrupted while the patient is stabilised. | UR_02 |

#### Scenario 4 — Sensor Disconnection and Misplacement Recovery

A sensor works loose during patient movement. The system must expose the stale or unreliable signal as a technical fault — never letting it masquerade as a stable patient — and guide the nurse to the affected sensor.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_15 | Perceive the disconnection alarm | After 5 seconds of signal inactivity from a connected measurement device, the Critical Care Nurse perceives the connection alarm presented within 1 second of the trigger. | UR_09 |
| UT_16 | Identify the affected sensor | The nurse recognises the alarm's technical (not physiological) signature and reads which device from the Acquired Parameters / Signals table (Context section) is affected. | UR_09, UR_21 |
| UT_17 | Recognise a misplacement annunciation | When a device reports sensor misplacement or an unreliable reading, the nurse sees it unambiguously annunciated and clearly attributed to the affected sensor, and refrains from acting on the suspect value. | UR_10 |
| UT_18 | Correct the sensor and confirm recovery | The nurse re-seats or replaces the affected sensor and confirms that the technical alarm clears and valid, real-time readings resume on the display. | UR_10, UR_02 |

#### Scenario 5 — Diagnostic Timeout Fallback

The AI engine fails to converge within its 2-minute window. The clinician must learn this actively — not by noticing an absence — and continue care unaided while monitoring and alarming remain fully available.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_19 | Perceive the non-convergence notification | The Emergency Department Clinician perceives an active, clearly presented notification that diagnostic guidance has not converged within the expected 2-minute window. | UR_11 |
| UT_20 | Fall back to unaided assessment | The clinician immediately proceeds with unaided clinical assessment, confirming that vital signs monitoring and alarming remain fully functional and unaffected by the diagnostic unavailability. | UR_11, UR_03 |
| UT_21 | Recognise resumption of diagnostic support | When diagnostic candidates later become available, the clinician recognises their return on the display and re-incorporates the advisory guidance into the assessment. | UR_05, UR_11 |

#### Scenario 6 — Hospital Handover with Data Sharing and Second Opinion

Approaching the hospital, the crew shares the case with the receiving team for a second opinion, then hands the patient over with the physiological course en route intact — monitoring never pausing across the transition.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_22 | Share the case with the HIS | Approaching the hospital, the Pre-hospital Care Provider — the crew member actually with the patient en route — shares the current vital signs and diagnostic candidates with the hospital information system in a single action and confirms the transfer completes within 1 second. | UR_15 |
| UT_23 | Receive and review remotely | The Remote Consulting Clinician receives the shared vital signs and diagnostic candidates through the HIS in an established interoperability format (e.g. HL7/FHIR), reviews the case away from the patient, and returns a second opinion. | UR_16 |
| UT_24 | Handle a sharing connectivity loss | When hospital connectivity drops mid-transport, the Pre-hospital Care Provider sees a clear indication that only data sharing is degraded, and confirms monitoring, alarming, and diagnostic display continue unaffected. | UR_17 |
| UT_25 | Hand over with continuous monitoring | At handover, the Intensive Care Clinician receives the patient with monitoring uninterrupted across the transition and reviews the en-route vital sign trends alongside current values. | UR_04, UR_22 |

#### Scenario 7 — Simulation Training Session

Before first clinical use, a clinician rehearses the complete workflow in simulation mode, building competence and justified trust — with no possibility of confusing simulated data with a live patient.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_26 | Enter simulation mode | The Simulation Training User starts the simulation training mode and confirms it is unmistakably distinguished from live clinical operation at all times. | UR_18, UR_19 |
| UT_27 | Rehearse connection and alarm handling | The user works through realistic scenarios rehearsing device connection, physiological alarm response, and sensor fault recovery within the simulation. | UR_18 |
| UT_28 | Practise interpreting AI candidates | The user practises reading ranked diagnostic candidates, treating them as advisory input distinct from measured facts, until reaching competence and justified trust. | UR_18, UR_06 |
| UT_29 | Exit simulation and return to live mode | The user ends the session and confirms the unambiguous return to live clinical operation, with no simulated data carried over or mistakable for a real patient. | UR_19 |

### Usability FMEA (UFMEA_*)

An FMEA focused on usability: where the user interface, workflow, or interaction model can lead to errors, slow operation, or unsafe outcomes.

| ID | Scenario Title | Use Error | Cause | Effect | HF Cause | Rationale | Usability Impact Level | Mitigation (existing) | Mitigation (new) | Classification | Traces |
|----|----------------|-----------|-------|--------|----------|-----------|------------------------|-----------------------|------------------|----------------|--------|
| UFMEA_01 | Scenario 1 — Emergency Deployment and Patient Connection in a Mobile Medical Unit | Provider begins relying on the display before the system has reached full operational readiness | Power-on performed while moving to the patient; provider glances away during the boot sequence and assumes a partially rendered screen is live monitoring | Early clinical decisions based on absent or initialising data | Time pressure at first patient contact drives anticipatory behaviour; incomplete states resemble the live view | At the roadside the provider acts within seconds; any boot state that visually resembles live monitoring invites premature trust | Critical | < 10 s activation target limits the exposure window | Distinct, full-screen start-up state that cannot be mistaken for the live vital signs view; explicit "ready" transition cue | Basic | UT_01 |
| UFMEA_02 | Scenario 1 — Emergency Deployment and Patient Connection in a Mobile Medical Unit | Provider attaches a sensor but fails to notice it was not recognised by the MMSS | Recognition feedback is subtle or per-device confirmation is skipped while multiple sensors are applied in rapid succession | A clinically indicated parameter is silently absent from monitoring and from AI input | Divided attention across several near-simultaneous manual tasks; confirmation step competes with patient care | Multi-sensor application under time pressure makes per-device visual confirmation the step most likely to be dropped | Critical | Connection alarm after 5 s of inactivity covers devices that were once active | Persistent per-device connection status strip showing every expected parameter slot as connected / absent | Basic | UT_02 |
| UFMEA_03 | Scenario 1 — Emergency Deployment and Patient Connection in a Mobile Medical Unit | Provider misreads a vital sign value from working distance in glare or poor lighting | Bright sunlight or dim vehicle interior degrades display legibility; similar-looking digits and adjacent parameters confused | Wrong value carried into clinical assessment | Visual perception degraded by ambient lighting; glance-reading substitutes pattern recognition for careful reading | Roadside and in-vehicle lighting is uncontrolled; glance legibility is the dominant reading mode in this scenario | Critical | — | High-contrast display mode with large parameter-coded digits and colour/position coding verified at working distance under glare and low-light conditions | Basic | UT_03, UT_05 |
| UFMEA_04 | Scenario 2 — Continuous Monitoring with AI Diagnostic Support En Route | Clinician interprets the top-ranked AI candidate as a confirmed diagnosis rather than advisory output | Ranked presentation reads as a conclusion; advisory labelling overlooked under cognitive load | Premature closure of the differential diagnosis; wrong or delayed treatment | Automation bias and authority gradient toward computer-generated output; anchoring on the first-listed item | Risk register R_05 identifies clinician misinterpretation of AI candidates as a critical project risk | Catastrophic | Mandatory simulation training mode (R_05 mitigation); advisory labelling and visual separation of candidates from measured vitals | Likelihood presented as explicit ranked probability bands, never as a single asserted result; persistent "advisory — not a diagnosis" framing on the candidate panel | Performance | UT_06, UT_07 |
| UFMEA_05 | Scenario 2 — Continuous Monitoring with AI Diagnostic Support En Route | Clinician anchors on an earlier candidate ranking and misses a real-time re-ranking | Candidates update continuously as data arrives; changes occur while attention is on hands-on care | Clinician acts on a superseded ranking that no longer reflects the patient state | Change blindness — unattended incremental updates on a peripheral display are not perceived | En-route attention is intermittent by design; silent list re-ordering is exactly the change humans fail to detect | Critical | Real-time candidate updating | Salient change indication (e.g. highlight and brief marker) when candidate order or membership changes since the last glance | Performance | UT_06 |
| UFMEA_06 | Scenario 2 — Continuous Monitoring with AI Diagnostic Support En Route | Clinician reads the trend of the wrong parameter or misreads the time axis in the moving vehicle | Trend views accessed via small touch targets under vibration; compressed time axes look alike | Gradual deterioration attributed to the wrong vital sign or missed entirely | Motor precision degraded by vehicle vibration; perceptual confusion between similar trend plots | Trend review happens mid-transport on a vibrating platform — selection and reading errors are both plausible | Moderate | Trends shown alongside current values for context | Large touch targets sized for vibration; trend plots labelled with parameter name, units and colour matching the live tile | Performance | UT_08 |
| UFMEA_07 | Scenario 3 — Abnormal Vital Sign Alarm Response | Nurse fails to perceive a physiological alarm amid siren and road noise | Alarm tone masked by ambient noise; visual signal outside the nurse's field of view while hands-on | Abnormal vital sign unaddressed; patient deterioration progresses untreated | Auditory masking in a high-noise environment; attention captured by the intervention in progress | The scenario explicitly places the nurse away from the display in siren noise — single-channel annunciation is insufficient | Catastrophic | Audible and visual alarm within 1 s of detection; DEVICES generate independent audible alarms (R_07) | Alarm audio characteristics (frequency bands, level) specified against the documented ambulance noise spectrum; wide-angle visual beacon visible from any working position | Basic | UT_10 |
| UFMEA_08 | Scenario 3 — Abnormal Vital Sign Alarm Response | Nurse mis-triages a physiological alarm as a technical one by sound and delays response | Physiological and technical alarm signatures insufficiently distinct, or signature mapping not retained from training | Patient-critical alarm treated with the lower urgency of a sensor fault | Confusable auditory coding; retrieval failure under stress for rarely exercised sound–meaning mappings | Triage-by-sound-alone is the designed behaviour (UT_12); it fails exactly when the signatures are not discriminable under noise | Critical | Distinct physiological vs technical alarm signatures; simulation training rehearses alarm response | Alarm signature discriminability validated by listening tests in representative noise; signatures aligned with IEC 60601-1-8 conventions clinicians already know | Basic | UT_12, UT_11 |
| UFMEA_09 | Scenario 3 — Abnormal Vital Sign Alarm Response | Nurse silences or acknowledges the wrong alarm when multiple alarms are active | Several alarms annunciate together; acknowledge control acts on a different alarm than the one the nurse intends | An unhandled critical alarm is silenced and forgotten while a lesser one is addressed | Alarm fatigue and habituated acknowledge gestures; ambiguous mapping between the control and the alarm instance | Multi-alarm episodes are routine in critical care; per-alarm attribution of the acknowledge action is essential | Critical | Acknowledgement designed for minimal steps with standard clinical training | Acknowledge action always bound to an explicitly identified single alarm; silenced alarms remain visually latched until resolved; re-annunciation on persistence | Basic | UT_13 |
| UFMEA_10 | Scenario 3 — Abnormal Vital Sign Alarm Response | Nurse mis-taps an adjacent control under vehicle vibration while acknowledging | Touch targets too small or too close for use in a moving vehicle with gloved hands | Unintended action triggered (e.g. wrong screen, wrong function) during a critical episode | Degraded fine motor control from vibration and gloves; haste during intervention | The acknowledge interaction occurs at the worst moment for motor precision — design must absorb the tremor | Moderate | — | Glove-compatible touch targets meeting in-motion size/spacing minima; destructive or mode-changing actions require confirmation; accidental-touch rejection | Basic | UT_13, UT_14 |
| UFMEA_11 | Scenario 4 — Sensor Disconnection and Misplacement Recovery | Nurse reads a stale, frozen value as a stable patient before the disconnection is annunciated | Last-known value remains displayed without distinction during the inactivity window or after a fault | Treatment decisions based on data that no longer reflects the patient; wrong diagnosis fed to the AI (R_04) | Frozen numbers are perceptually identical to genuinely stable ones; no cue prompts suspicion | Risk register R_04 rates undetected misplacement as Critical — the display must never let stale data masquerade as live | Catastrophic | 5 s inactivity alarm; DEVICES auto-detect misplacement (R_04) | Stale or unreliable values immediately rendered visually invalid (greyed/struck/blanked with fault annotation), never shown as normal live data | Basic | UT_15, UT_17 |
| UFMEA_12 | Scenario 4 — Sensor Disconnection and Misplacement Recovery | Nurse re-seats the wrong sensor after a connection or misplacement alarm | Alarm attribution to the affected device unclear; several similar sensor cables on the patient | Fault persists while the nurse believes it is being corrected; monitoring gap extends | Weak mapping between on-screen device identification and the physical sensor on the body | With six device types attached, attribution ambiguity converts a quick fix into a prolonged blind spot | Moderate | Alarm identifies the affected device from the Acquired Parameters / Signals table | Affected-device indication uses the same name, icon and colour as the live parameter tile; physical-location hint in the alarm detail | Basic | UT_16, UT_18 |
| UFMEA_13 | Scenario 4 — Sensor Disconnection and Misplacement Recovery | Nurse assumes recovery after re-seating without confirming the alarm cleared and valid readings resumed | Attention returns to the patient immediately after the manual fix; recovery confirmation step skipped | Sensor still faulty; parameter silently absent or unreliable for the rest of transport | Premature exit — completing the motor action is felt as completing the task | Confirmation is a separate cognitive step the workflow must enforce, not assume | Moderate | Technical alarm persists until signal genuinely resumes | Positive recovery cue (alarm clears with distinct confirmation tone/visual) so absence of sound is never the only evidence of success | Basic | UT_18 |
| UFMEA_14 | Scenario 5 — Diagnostic Timeout Fallback | Clinician misses the non-convergence notification and continues waiting for AI guidance | Timeout banner too subtle, transient, or displaced by other screen activity; clinician attention on the patient | Treatment delayed while the clinician expects diagnostic support that will not arrive (R_06) | Absence of an expected event is intrinsically hard to notice; passive cues are filtered under load | Risk register R_06 rates uncommunicated timeout as Critical; the notification must be active, persistent and multi-channel | Critical | ALGOS sends an independent audible notification on the 2-minute timeout; MMSS also notifies | Timeout presented as a persistent, attention-demanding banner with audible cue, latched until the clinician acknowledges it | Basic | UT_19, UT_20 |
| UFMEA_15 | Scenario 5 — Diagnostic Timeout Fallback | Clinician treats previously displayed candidates as current after a timeout, or misses their later resumption | Candidate panel retains pre-timeout content, or resumption appears without salience | Decisions based on superseded advisory output; returned guidance unused | Display inertia read as continuity; change blindness on resumption | The transition into and out of diagnostic unavailability must be explicit in both directions | Moderate | Resumption renders new candidates on the display | During timeout the candidate panel shows an explicit "no current diagnostic guidance" state (stale candidates cleared or marked superseded); resumption announced with a salient cue | Performance | UT_19, UT_21 |
| UFMEA_16 | Scenario 6 — Hospital Handover with Data Sharing and Second Opinion | Provider shares the case to the wrong patient context or destination in the HIS | Single-action share performed under handover pressure with patient/destination selection defaulted or stale from a prior episode | Wrong-patient record contamination; second opinion rendered on the wrong case | Slip on a routine one-tap action; carry-over of prior-episode context | A one-action share is required for speed (UT_22) but concentrates all error potential in the preceding context selection | Critical | Transfer confirmation within 1 s | Share action preceded by a compact patient/destination verification summary; new episode always clears prior sharing context | Performance | UT_22, UT_23 |
| UFMEA_17 | Scenario 6 — Hospital Handover with Data Sharing and Second Opinion | Provider misreads the sharing-degraded indication as a monitoring failure — or fails to notice sharing was never delivered | Degradation cue ambiguous about scope; provider assumes the hospital received data that never arrived | Either unwarranted distrust and distraction from patient care, or a handover planned around a second opinion that never came | Incorrect mental model of which functions share a failure domain | UT_24 requires the provider to see that only sharing is degraded — the indication must state scope and delivery status explicitly | Critical | Clear indication that only data sharing is degraded; monitoring/alarming/diagnostics unaffected | Per-transfer delivery status (sent / failed / pending retry) visible to the provider; degraded-sharing cue textually scoped to connectivity only | Performance | UT_24, UT_22 |
| UFMEA_18 | Scenario 7 — Simulation Training Session | User confuses simulation with live operation — acting on simulated data as real, or leaving the device in simulation mode for a live patient | Simulation visuals closely mirror live mode by design; mode indicator overlooked; session not cleanly exited before clinical use (UT_29) | Clinical action taken on fictitious data, or a live patient connected to a monitor still in simulation | Mode error — the classic failure when two modes share one interface; realistic training maximises the resemblance | Training realism and mode distinguishability are in direct tension; the design must resolve it structurally, not by labelling alone | Catastrophic | Simulation mode required to be unmistakably distinguished from live operation at all times | Persistent full-perimeter simulation watermark/banner impossible to crop or overlook; live sensor data detection while in simulation forces an exit prompt; simulation auto-terminates with explicit confirmation and no data carry-over | Basic | UT_26, UT_29 |
| UFMEA_19 | Scenario 7 — Simulation Training Session | User rehearses in simulation behaviours that differ from live-mode behaviour, building negative transfer | Simulated alarm timing, candidate behaviour, or interaction sequences deviate from the live implementation | Trained responses misfire in real episodes — exactly where training was meant to protect (undermines R_05 mitigation) | Habit formation transfers whatever was practised, correct or not | Simulation is the mandated mitigation for misinterpretation risk; fidelity gaps silently convert the mitigation into a hazard | Moderate | Simulation rehearses realistic connection, alarm and AI-interpretation scenarios | Simulation reuses the identical live UI, alarm signatures and interaction sequences, differing only in the mode indication and data source | Basic | UT_27, UT_28 |
| UFMEA_20 | Scenario 3 — Abnormal Vital Sign Alarm Response | Nurse responds late to — or reflexively silences without patient assessment — a genuine physiological alarm after repeated nuisance alarms | Motion artefact and patient handling in the moving vehicle trigger frequent false threshold alarms, each demanding the same acknowledge response as a real event | Real deterioration is answered late or silenced unexamined; the alarm system's protective value is eroded for the rest of transport | Alarm fatigue — desensitisation is a conditioned response to a high false-positive rate, not a vigilance failure of the individual nurse | Nuisance alarms from movement artefact are endemic in transport monitoring; safety is determined by the response to the hundredth alarm, not the first | Critical | Distinct physiological vs technical alarm signatures; minimal-step acknowledgement | Artefact-robust alarm handling (brief signal-quality validation before annunciation) to keep the in-motion false-alarm rate low; escalating re-annunciation so an unanswered genuine alarm becomes progressively more insistent | Basic | UT_10, UT_13 |

### Usability Requirements (USR_*)

Measurable requirements for how the product must perform from a user perspective: task completion times, error rates, learnability, accessibility. Validated through usability testing.

| ID | Requirement | Classification | Traces |
|----|-------------|----------------|--------|
| USR_01 | From power-on, the system shall reach a fully operational state with live vital signs displayed within 10 seconds, and in usability validation 100% of participants shall correctly distinguish the start-up state from the live monitoring view and identify the moment of operational readiness without prompting. | Safety-critical | UR_01, UFMEA_01 |
| USR_02 | A trained user connecting a patient for the first time after training shall complete connection of all clinically indicated measurement devices, with live vital signs confirmed on screen, within 3 minutes; during validation, 100% of unrecognised or absent sensors shall be detected by the user from the per-device connection status indication within 10 seconds of attachment. | Safety-critical | UR_02, UFMEA_02 |
| USR_03 | In simulated bright-sunlight glare and low-light vehicle-interior conditions, participants at a working distance of 1 m and viewing angles up to ±30° shall read displayed vital sign values with ≥ 99% accuracy in single-glance reading trials (≤ 2 seconds exposure per reading). | High | UR_12, UFMEA_03 |
| USR_04 | In usability validation, ≥ 95% of participants shall correctly characterise the AI diagnostic candidates as advisory ranked suggestions — not confirmed diagnoses — when questioned immediately after a simulated clinical scenario, and 100% shall correctly distinguish candidate entries from measured vital sign values on the display. | Safety-critical | UR_06, UFMEA_04 |
| USR_05 | When the AI candidate ranking changes while the participant performs a concurrent hands-on patient-care task, ≥ 90% of ranking changes shall be detected and correctly described by the participant at their next interaction with the display, within 30 seconds of the change. | High | UR_05, UFMEA_05 |
| USR_06 | Under simulated in-vehicle vibration and wearing clinical examination gloves, participants shall select the intended vital sign trend view at first attempt in ≥ 95% of trials and correctly identify the displayed parameter, its units, and the direction of its trend in ≥ 98% of readings. | High | UR_22, UFMEA_06 |
| USR_07 | In a representative mobile-medical-unit noise environment (siren, engine, and road noise per the documented ambulance noise spectrum), 100% of physiological alarms shall be perceived by participants within 3 seconds of annunciation from any working position around the patient, including positions where the display is outside the field of view. | Safety-critical | UR_08, UR_13, UFMEA_07 |
| USR_08 | Upon perceiving a physiological alarm, participants shall identify the affected vital sign within 5 seconds without searching or paging the display, with ≥ 95% first-attempt accuracy; the alarm presentation itself shall appear within 1 second of detection. | Safety-critical | UR_07, UFMEA_07 |
| USR_09 | In listening tests conducted in representative transport noise, participants shall classify alarms as physiological versus technical by sound alone with ≥ 95% accuracy, without sight of the display. | Safety-critical | UR_21, UFMEA_08 |
| USR_10 | In multi-alarm scenarios during usability validation, participants shall acknowledge the alarm they intend in ≥ 98% of trials, zero critical physiological alarms shall be unintentionally silenced and left unaddressed, and acknowledgement of a single identified alarm shall require no more than 2 interaction steps. | Safety-critical | UR_07, UR_14, UFMEA_09 |
| USR_11 | Under simulated vehicle vibration with gloved hands, all touch interactions shall succeed at first attempt in ≥ 95% of trials, and zero unintended mode-changing or destructive actions shall result from mis-taps across the full validation test set. | High | UR_14, UFMEA_10 |
| USR_12 | In usability validation, 100% of participants shall recognise a stale, disconnected, or device-reported-unreliable value as invalid (not a live reading) within 5 seconds of viewing it, and zero participants shall report a frozen value as a current, stable patient state. | Safety-critical | UR_09, UR_10, UFMEA_11 |
| USR_13 | Following a sensor disconnection or misplacement alarm with six device types attached, participants shall identify the correct physical sensor at first attempt in ≥ 95% of trials and shall correctly state, after corrective action, whether valid readings have resumed in 100% of trials. | Safety-critical | UR_10, UFMEA_12, UFMEA_13 |
| USR_14 | While engaged in a concurrent patient-care distractor task, 100% of participants shall notice and correctly interpret the diagnostic non-convergence (2-minute timeout) notification within 10 seconds of its presentation, and shall state that fallback to unaided clinical assessment is required. | Safety-critical | UR_11, UFMEA_14 |
| USR_15 | At any moment during and after a diagnostic timeout episode, ≥ 95% of participants shall correctly state whether current diagnostic guidance is available, and 100% shall detect the resumption of diagnostic candidates within 30 seconds of resumption. | Safety-critical | UR_11, UFMEA_15 |
| USR_16 | The share-to-HIS task shall be completed by trained users in a single share action taking ≤ 10 seconds of user interaction time including the patient/destination verification step, with zero wrong-patient or wrong-destination shares across the full validation test set. | High | UR_15, UFMEA_16 |
| USR_17 | When hospital connectivity is lost, ≥ 95% of participants shall correctly state that only data sharing is degraded — monitoring, alarming, and diagnostic display unaffected — and shall correctly report the delivery status (sent / failed / pending) of their most recent transfer. | High | UR_17, UFMEA_17 |
| USR_18 | In usability validation covering entry, use, and exit of simulation mode, 100% of participants shall correctly identify at every probe whether the system is in simulation or live clinical operation, and zero mode-confusion incidents (acting on simulated data as real, or leaving simulation active for a live patient) shall occur. | Safety-critical | UR_19, UFMEA_18 |
| USR_19 | After completing the standard training programme including the simulation mode (total duration ≤ 4 hours), users shall perform all routine tasks — activation, patient connection, alarm acknowledgement, and diagnostic candidate review — unaided with ≥ 95% task success at first live-equivalent assessment, and simulated alarm signatures, candidate behaviour, and interaction sequences shall be identical to live operation in behavioural fidelity testing, differing only in mode indication and data source. | High | UR_18, UR_14, UFMEA_19 |
| USR_20 | In an extended in-motion scenario including repeated artefact-induced nuisance alarms, ≥ 95% of genuine physiological alarms shall still receive a patient assessment before silencing, and 100% of participants shall perceive the escalating re-annunciation of an unanswered genuine alarm within 30 seconds. | Safety-critical | UR_07, UR_08, UFMEA_20 |

## Concept

### UI/UX Design

Wireframes, interaction flows, navigation structures, and visual design principles that translate the user requirements into a tangible concept.

#### Design Principles

1. **Glance readability in motion and glare** (UR_12, USR_03, USR_06): all vital sign values rendered in high-contrast, large-format numerals (minimum digit height sized for ≥ 99% single-glance accuracy at 1 m and ±30° viewing angle); dark background with high-luminance foreground, automatic brightness adaptation for sunlight/low-light vehicle interiors; touch targets sized and spaced for gloved operation under vibration (USR_11).
2. **Alarm hierarchy with distinct signatures** (UR_07, UR_08, UR_21, USR_07–USR_09): physiological alarms (red, fast pulse pattern, high-urgency tone per IEC 60601-1-8 style) are visually and audibly distinct from technical alarms (yellow/cyan, slower pattern, distinct lower-urgency tone), classifiable by sound alone in transport noise; the affected parameter tile flashes and is named in the alarm banner so the cause is identified without searching (USR_08); unanswered genuine alarms escalate in re-annunciation (USR_20).
3. **Advisory framing of AI candidates** (UR_05, UR_06, UR_20, USR_04): diagnostic candidates live in a dedicated, visually segregated panel, ranked with explicit likelihood indicators, each entry prefixed with an "ADVISORY" treatment (distinct typography, suggestion-style cards, never numeric-vital styling); the panel header permanently identifies the validated AI source ("Open Evidence — advisory only").
4. **Unmistakable mode indication** (UR_19, USR_18): live clinical operation has no mode banner; simulation mode shows a permanent, full-width, high-contrast orange "SIMULATION — NOT A REAL PATIENT" banner plus watermarked background and a distinct screen border — present on every screen, never dismissible.
5. **Minimal-step operation** (UR_01, UR_14, USR_01, USR_10): monitoring auto-starts on activation and device connection — no setup wizard before live vitals; alarm acknowledgement of an identified alarm takes ≤ 2 interaction steps; routine tasks need no menu deeper than one level.
6. **Validity is always explicit** (UR_09, UR_10, USR_12): a value is shown as a number only while live and reliable; stale, disconnected, or device-flagged-unreliable values are replaced by an unmissable invalid state ("--?--" with greyed tile and sensor-fault marker), never a frozen number.
7. **Graceful, legible degradation** (UR_03, UR_11, UR_17, USR_14, USR_15, USR_17): loss of connectivity or AI convergence degrades only the affected function and says so explicitly; monitoring and alarming are never visually entangled with optional functions.

#### Screen Inventory and Navigation Structure

| # | Screen / Surface | Purpose | Reached from | Realises |
|---|------------------|---------|--------------|----------|
| S1 | Main Monitoring Screen | Live vital signs tiles (all parameters in the Acquired Parameters / Signals table), AI candidate panel, status bar | Auto on activation (default home) | UR_01, UR_02, UR_05 |
| S2 | Alarm Overlay / Banner | Annunciate physiological and technical alarms over any screen | Automatic on alarm condition | UR_07, UR_08, UR_21 |
| S3 | Diagnostic Candidates Panel (expanded) | Full ranked candidate list with likelihoods, source label, timeout state | Tap candidate panel on S1 | UR_05, UR_06, UR_11, UR_20 |
| S4 | Sensor Status View | Per-device connection, placement, and signal-quality state for all six device types | Tap status bar device icons or any technical alarm | UR_09, UR_10 |
| S5 | Trends View | Episode-course trend graphs per vital sign, alongside current values | Tap any vital tile on S1 | UR_22 |
| S6 | Share-to-HIS Dialog | Single-action share with patient/destination verification and delivery status | Share button on S1/S3 | UR_15, UR_16, UR_17 |
| S7 | Simulation Mode Entry / Exit | Deliberate two-step confirmed entry into training mode; explicit exit | Menu → Training (blocked while live patient episode active) | UR_18, UR_19 |
| S8 | Patient Episode Start / Reset | New-episode confirmation clearing prior trends and candidates | Menu → New Patient (confirmed action) | UR_04, UR_22 |

Navigation: flat, one level deep. S1 is the permanent home; every other surface is one tap from S1 and one tap (Back/Close) returns. Alarm overlays (S2) pre-empt all screens and deep-link to the affected tile (physiological) or affected sensor on S4 (technical).

#### Wireframe W1 — Main Monitoring Screen (S1, live mode)

```
+------------------------------------------------------------------------------+
| 10:42:17  | EPISODE 00:14:32 | ECG SpO2 NIBP TEMP CO2 EEG | HIS:OK | [Menu]  |  <- status bar (S4 entry)
+------------------------------------------------------------------------------+
|  +---------------+  +---------------+  +---------------+   | AI DIAGNOSTIC   |
|  | HR    (ECG)   |  | SpO2          |  | NIBP          |   | CANDIDATES      |
|  |    112        |  |    94 %       |  |  138/92       |   | Open Evidence   |
|  |    bpm   /\/\ |  |   pleth ~~~~  |  |  MAP 107 mmHg |   | -- ADVISORY --  |
|  +---------------+  +---------------+  +---------------+   |-----------------|
|  +---------------+  +---------------+  +---------------+   | 1. Sepsis  72%  |
|  | TEMP          |  | etCO2 (CAP)   |  | EEG           |   | 2. PE      14%  |
|  |   38.9 C      |  |    32 mmHg    |  |  cont. trace  |   | 3. ACS      8%  |
|  |               |  |  RR 24 /min   |  |  ~~~~~~~~~~~  |   |-----------------|
|  +---------------+  +---------------+  +---------------+   | updated 0:05 ago|
|   (tap any tile -> S5 Trends)                              | [Expand]  (S3)  |
+------------------------------------------------------------+-----------------+
|                       ALARM ZONE (idle: thin neutral strip)                  |
+------------------------------------------------------------------------------+
|        [ Share to HIS ]                [ Trends ]              [ Sensors ]   |
+------------------------------------------------------------------------------+
```

Notes: six tiles map one-to-one to the Acquired Parameters / Signals set (UR_02); candidate panel is colour- and typography-segregated from tiles (UR_06, USR_04); in simulation mode an orange full-width banner "SIMULATION — NOT A REAL PATIENT" is inserted above the status bar and the screen border is orange (UR_19).

#### Wireframe W2 — Physiological Alarm Overlay (S2)

```
+------------------------------------------------------------------------------+
| ████ RED FLASHING BANNER ████████████████████████████████████████████████████|
| !!  SpO2 LOW : 84 %   (limit 90 %)                 HIGH-URGENCY TONE (cont.) |
|     [ ACKNOWLEDGE / SILENCE 60 s ]                                  [ View ] |
+------------------------------------------------------------------------------+
|  ... main screen remains visible; SpO2 tile flashes red in sync ...          |
|  Technical alarm variant (yellow, distinct slower tone):                     |
| ~~  ECG SENSOR DISCONNECTED — check lead placement      [ Sensors ] [ Ack ]  |
+------------------------------------------------------------------------------+
```

Notes: banner names the affected parameter and value — no searching (UR_07, USR_08); one tap = acknowledge for a single alarm (USR_10); with multiple simultaneous alarms each gets its own row and its own Ack — no global silence of unseen alarms (USR_10); acknowledged-but-unresolved genuine alarms re-annunciate with escalating urgency (USR_20); red/fast vs yellow/slow signatures separate physiological from technical (UR_21, USR_09).

#### Wireframe W3 — Diagnostic Candidates Panel, expanded with timeout state (S3)

```
+------------------------------------------------------------------------------+
| AI DIAGNOSTIC CANDIDATES — Open Evidence (validated) — ADVISORY ONLY  [Close]|
+------------------------------------------------------------------------------+
| NORMAL STATE:                                                                |
|  #1  Sepsis                       likelihood ████████░░  72%   ^ rising      |
|  #2  Pulmonary embolism           likelihood ██░░░░░░░░  14%                 |
|  #3  Acute coronary syndrome      likelihood █░░░░░░░░░   8%   v falling     |
|  Last updated: 5 s ago            These are suggestions, not diagnoses.      |
+------------------------------------------------------------------------------+
| TIMEOUT STATE (replaces list after 2-min non-convergence):                   |
|  /!\  NO DIAGNOSTIC GUIDANCE AVAILABLE                                       |
|  AI has not converged within 2 minutes.                                      |
|  CONTINUE WITH UNAIDED CLINICAL ASSESSMENT.        [ Acknowledge ]           |
|  (Monitoring and alarms are NOT affected.)         + attention tone          |
+------------------------------------------------------------------------------+
```

Notes: ranked, likelihood-ordered, live-updating with change markers (UR_05, USR_05); permanent source/validation label (UR_20); timeout state is active and attention-demanding, states the fallback explicitly, and shows resumption visibly when candidates return (UR_11, USR_14, USR_15).

#### Interaction Flows

**F1 — Physiological alarm response** (UR_07, UR_08, USR_08, USR_10)
1. Abnormal vital detected → red banner + high-urgency tone within 1 s; affected tile flashes; perceivable audibly away from display.
2. Clinician reads parameter + value directly from banner (no navigation).
3. One tap **Acknowledge** silences audio for 60 s; banner persists while condition persists.
4. If condition persists unacknowledged or returns, alarm re-annunciates with escalating urgency until resolved.

**F2 — Sensor-fault recovery** (UR_09, UR_10, USR_12, USR_13)
1. 5 s signal inactivity or device-reported misplacement → yellow technical banner within 1 s, naming the device; affected tile shows invalid state ("--?--"), never a frozen value.
2. Tap **Sensors** (or banner) → S4 highlights the faulted device with placement guidance.
3. Clinician corrects the physical sensor.
4. On valid signal resumption the tile returns to live numerals with a brief "readings resumed" confirmation; the banner clears.

**F3 — Share to hospital for second opinion** (UR_15, UR_16, UR_17, USR_16, USR_17)
1. Tap **Share to HIS** → S6 shows patient identifier + destination for verification (single confirmation step).
2. Tap **Confirm Share** → current vitals + candidates transmitted (≤ 1 s); status shows Sent / Pending / Failed.
3. On connectivity loss, status bar shows "HIS: offline — sharing only"; pending shares queue and auto-send on reconnection; monitoring/alarming visibly unaffected.

**F4 — Entering and leaving simulation mode** (UR_18, UR_19, USR_18)
1. Menu → **Training** (disabled while a live patient episode is active).
2. Explicit confirmation "Enter SIMULATION — no real patient data will be shown" → orange banner, watermark, and border appear on every screen.
3. Trainee rehearses connection, alarms, and candidate interpretation with behaviour identical to live operation except mode indication and data source (USR_19).
4. Exit requires deliberate Menu → **End Simulation** + confirmation; system returns to a clearly bannerless live-idle state; simulation cannot persist into a live episode start (S8 forces mode check).

### Actors

Individuals, groups, or systems that perform roles or tasks within the system or process.

| Actor | Description |
|-------|-------------|
| Paramedic / EMS Clinician | Pre-hospital care provider operating the MMSS in mobile medical units; connects measurement devices to the patient, monitors vital signs, and responds to alarms and AI diagnostic candidates en route to hospital. |
| Emergency Physician | Emergency department clinician using the MMSS during reception, triage, and stabilisation; interprets vital signs trends and ranked AI diagnostic candidates as advisory input while retaining diagnostic authority. |
| Emergency / ICU Nurse | Critical care nurse performing continuous bedside monitoring; attaches and repositions sensors, acknowledges and escalates alarms, and is typically the first responder to sensor-fault and connection alarms. |
| Intensivist / ICU Physician | Intensive care clinician using the MMSS for continuous ICU surveillance; correlates vital signs and AI diagnostic candidates with the broader clinical picture and directs the treatment plan. |
| Hospital Clinician (Second Opinion) | Remote consulting clinician who receives MMSS diagnostic candidates and vital signs via the hospital information system and provides a second opinion to the on-scene or bedside clinician. |
| Clinical Trainer / Trainee | Instructor or clinician in training using the MMSS mandatory simulation training mode to rehearse device connection, alarm handling, and interpretation of AI diagnostic candidates before live use. |
| ECG Monitor | Data-providing system actor; supplies electrocardiogram data to the MMSS over its published interface and reports sensor misplacement and connection status. |
| Pulse Oximeter | Data-providing system actor; supplies oxygen saturation and pulse rate data to the MMSS over its published interface and reports sensor misplacement and connection status. |
| Blood Pressure Monitor | Data-providing system actor; supplies blood pressure values to the MMSS over its published interface and reports sensor misplacement and connection status. |
| Thermal Probe | Data-providing system actor; supplies body temperature data to the MMSS over its published interface and reports sensor misplacement and connection status. |
| Capnometer | Data-providing system actor; supplies end-tidal CO2 and respiratory data to the MMSS over its published interface and reports sensor misplacement and connection status. |
| EEG Monitor | Data-providing system actor; supplies electroencephalogram data to the MMSS over its published interface and reports sensor misplacement and connection status. |
| AI Diagnostic Engine (ALGOS / Open Evidence) | External validated AI system actor; receives acquired patient data from the MMSS and returns structured, ranked diagnostic candidates, converging within its 2-minute budget and independently notifying on diagnosis timeout. |
| Hospital Information System (HIS) | External hospital system actor; receives diagnostic candidates and vital signs shared by the MMSS to support a second opinion (protocol TBD, HL7/FHIR). |
| Monitor Display | Presentation peer system actor; renders the vital signs, alarms, and diagnostic candidates output by the MMSS to the clinician on the portable patient monitor. |
| Host Platform Clock / Timer | Host CPU platform real-time OS timing service acting on the MMSS; drives the 1-second timer-based UI update cycle and the 5-second connection-inactivity alarm trigger. |

### Use Cases (UC_*)

_To be added_

| ID | Title | Actor | Goal | Satisfies | Classification | Precondition | Main Success Scenario | Alternative Scenarios | Exception Scenarios | Post Condition | Traces |
|----|-------|-------|------|-----------|----------------|--------------|-----------------------|-----------------------|---------------------|----------------|--------|
| UC_01 | Activate System and Connect Patient | Paramedic / EMS Clinician | Bring the MMSS from cold start to live multi-parameter monitoring at first patient contact. | UR_01, UR_02 | Safety-critical | Monitor powered off; measurement devices physically available; patient reached. | 1) Clinician powers on the monitor; 2) MMSS reaches full operational readiness with the live vital signs view within 10 s; 3) clinician attaches the clinically indicated sensors from the Acquired Parameters / Signals set; 4) MMSS recognises each connected device; 5) each connected parameter appears on the display within 1 s of acquisition. | A1: Only a subset of the six device types is clinically indicated — MMSS monitors the connected subset and presents only those parameters. A2: Monitor is already running from a previous patient (patient changeover) — clinician starts a fresh episode for the new patient and no vital signs, trends, or diagnostic candidates from the previous patient are carried into the new episode's display. | E1: A device is not recognised — MMSS annunciates the affected device as a technical fault (see UC_07); E2: Readiness not reached within 10 s — clinician proceeds with unaided assessment without waiting, connects sensors once readiness is reached, and treats persistent failure to start as a device fault. | MMSS is operational and displaying live vital signs for all connected devices. | UT_01, UT_02, UT_03, UR_01, UR_02 |
| UC_02 | Monitor Live Vital Signs at the Point of Care | Paramedic / EMS Clinician | Read the current value of every acquired parameter at a glance without interrupting hands-on care. | UR_02, UR_12 | Safety-critical | UC_01 completed; episode in progress. | 1) MMSS continuously acquires all connected parameters; 2) each value is presented within 1 s of acquisition on the 1 s UI update cycle; 3) clinician glances at the display from working distance — in a moving vehicle, poor lighting, or bright sunlight — and reads all current values without searching. | A1: Clinician is hands-on with the patient — perceivable presentation lets monitoring continue without dedicated attention to the screen. | E1: A parameter stops updating — the stale signal is exposed as a connection alarm (UC_07), never shown as a current value. | Clinician acts on the patient's current physiological state at all times. | UT_03, UT_05, UT_14, UR_02, UR_12 |
| UC_03 | Operate Standalone Without External Network | Paramedic / EMS Clinician | Keep monitoring, alarming, and diagnostic support fully functional with no external network connection. | UR_03 | Safety-critical | MMSS operational at a scene with no hospital or network connectivity. | 1) Clinician continues normal monitoring with no connectivity-related action or configuration; 2) MMSS provides monitoring, alarming, and diagnostic candidate display fully locally; 3) clinician completes on-scene care unaffected by the absence of a network. | A1: Connectivity becomes available later — optional HIS sharing (UC_09) becomes possible without interrupting monitoring. | E1: None — absence of connectivity is the nominal standalone condition and degrades nothing but optional sharing (see UC_09 E1). | Patient safety functions were delivered without any dependency on connectivity. | UT_04, UT_20, UR_03 |
| UC_04 | Review AI Diagnostic Candidates | Emergency Physician | Use ranked, advisory diagnostic candidates to support — never replace — the clinician's own differential diagnosis. | UR_05, UR_06 | Safety-critical | UC_01 completed; AI diagnostic engine receiving acquired patient data. | 1) MMSS presents likelihood-ordered diagnostic candidates alongside the vital signs; 2) candidates update in real time as new measurement data arrives; 3) clinician verifies each candidate is visually and semantically distinct from measured facts and explicitly labelled as advisory; 4) clinician forms an independent clinical judgement informed by the candidates. | A1: Candidate ranking changes as data accrues — clinician observes the re-ranking and reassesses. | E1: Diagnostic guidance has not converged within 2 minutes or is unavailable — UC_08 (Diagnostic Timeout) applies. | Clinician's differential diagnosis is supported while clinical authority remains with the clinician. | UT_06, UT_07, UR_05, UR_06 |
| UC_05 | Respond to Abnormal Vital Sign Alarm | Emergency / ICU Nurse | Perceive, triage, and identify a physiological alarm immediately, even with attention away from the display in a high-noise environment. | UR_07, UR_08, UR_13, UR_21 | Safety-critical | Monitoring active; nurse attending the patient away from the display. | 1) A vital sign crosses an alarm limit; 2) MMSS annunciates an audible and visual alarm within 1 s of detection, perceivable over the high ambient noise of the care environment — siren, road, and engine noise in a mobile medical unit, or concurrent alarms and activity in a busy unit; 3) by sound alone the nurse recognises the physiological (not technical) signature and assigns patient-critical urgency; 4) at the display the nurse immediately identifies which vital sign is abnormal without searching; 5) nurse initiates clinical intervention. | A1: Nurse is at the display when the alarm triggers — visual identification is immediate and triage by sound is unnecessary. | E1: A technical alarm sounds concurrently — distinct signatures let the nurse prioritise the physiological alarm first. | Abnormal condition is perceived and intervention is started without delay. | UT_10, UT_11, UT_12, UR_07, UR_08, UR_13, UR_21 |
| UC_06 | Acknowledge and Manage Alarms | Emergency / ICU Nurse | Acknowledge an annunciated alarm in minimal steps while monitoring continues uninterrupted. | UR_14, UR_02 | Safety-critical | An alarm is annunciated; clinical response initiated. | 1) Nurse acknowledges the alarm in a minimal number of steps using standard clinical training only; 2) the annunciation is silenced or de-escalated per acknowledgement; 3) nurse confirms real-time display of all acquired parameters continues uninterrupted. | A1: The alarm condition has already cleared (e.g. sensor corrected) — the alarm resolves and acknowledgement records the handled event. | E1: The alarm condition persists after acknowledgement — the abnormal state remains visibly indicated until resolved. | Alarm handled; monitoring never interrupted by alarm management. | UT_13, UT_14, UR_14, UR_02 |
| UC_07 | Recover from Sensor Disconnection or Misplacement | Emergency / ICU Nurse | Expose a stale or unreliable signal as a technical fault, locate the affected sensor, and restore valid readings. | UR_09, UR_10, UR_21 | Safety-critical | Monitoring active; a sensor works loose, disconnects, or is misplaced. | 1) After 5 s of signal inactivity from a connected device, MMSS presents the connection alarm within 1 s of the trigger; 2) nurse recognises the technical (not physiological) alarm signature; 3) nurse reads which device is affected, unambiguously attributed; 4) nurse re-seats or replaces the sensor; 5) the technical alarm clears and valid real-time readings resume. | A1: The device reports misplacement or an unreliable reading rather than disconnecting — MMSS annunciates it attributed to the affected sensor and the nurse refrains from acting on the suspect value. | E1: The fault persists after correction — the technical alarm remains active and the nurse escalates (replaces the device or continues without that parameter, knowingly). | No stale or unreliable reading masquerades as a stable patient; valid monitoring restored. | UT_15, UT_16, UT_17, UT_18, UR_09, UR_10, UR_21 |
| UC_08 | Handle Diagnostic Timeout | Emergency Physician | Learn actively that diagnostic guidance is unavailable and continue care unaided with monitoring intact. | UR_11 | Safety-critical | UC_04 in progress; AI engine fails to converge within its 2-minute window. | 1) MMSS presents an active, clearly perceivable notification that diagnostic guidance has not converged within the expected window; 2) clinician immediately proceeds with unaided clinical assessment; 3) clinician confirms vital signs monitoring and alarming remain fully functional and unaffected. | A1: Diagnostic candidates later become available — the clinician recognises their return on the display and re-incorporates the advisory guidance (UC_04 resumes). | E1: Diagnostic support never resumes during the episode — care is completed on monitoring and unaided assessment alone. | No treatment delay caused by silently absent diagnostic support. | UT_19, UT_20, UT_21, UR_11 |
| UC_09 | Share Case with HIS for Second Opinion | Paramedic / EMS Clinician | Send the current vital signs and diagnostic candidates to the hospital information system in a single action. | UR_15, UR_17 | High | Episode in progress; hospital connectivity available. | 1) Approaching the hospital, the clinician triggers sharing in a single action; 2) MMSS transfers the current vital signs and diagnostic candidates to the HIS; 3) clinician confirms the transfer completed within 1 s. | A1: Clinician repeats the share later in transport — the then-current data set is transferred. | E1: Hospital connectivity drops — MMSS clearly indicates a sharing-only limitation while monitoring, alarming, and diagnostic display continue unaffected; the clinician retries when connectivity returns. | Receiving team has the current case data; on-board patient care was never interrupted. | UT_22, UT_24, UR_15, UR_17 |
| UC_10 | Receive and Review Shared Case Remotely | Hospital Clinician (Second Opinion) | Review the shared case away from the patient and return a timely second opinion. | UR_16 | High | UC_09 completed; HIS access available to the remote clinician. | 1) The remote clinician receives the shared vital signs and diagnostic candidates through the HIS in an established interoperability format (e.g. HL7/FHIR); 2) clinician reviews the case away from the patient; 3) clinician returns a second opinion to the on-scene or bedside clinician. | A1: Updated shares arrive during review — the clinician bases the opinion on the most recent data set. | E1: The received data set is incomplete or malformed — the clinician requests a re-share rather than opining on partial data. | A timely second opinion reaches the treating clinician. | UT_23, UR_16 |
| UC_11 | Review Vital Sign Trends | Emergency Physician | Recognise gradual deterioration from the episode's physiological course, not just a snapshot. | UR_22 | High | Monitoring active; episode history accumulated. | 1) Clinician opens the recent trend view of the monitored vital signs; 2) MMSS presents each parameter's trend over the episode alongside the current values; 3) clinician assesses the course for gradual deterioration. | A1: At handover, the receiving clinician reviews the en-route trends to take over with the full physiological course visible. | E1: A parameter has gaps from earlier sensor faults — the gaps are evident in the trend rather than interpolated as valid data. | Deterioration patterns are recognisable; episode course informs treatment. | UT_08, UT_25, UR_22 |
| UC_12 | Hand Over Patient with Continuous Monitoring | Intensivist / ICU Physician | Receive the patient across a care-setting transition with no observation gap. | UR_04, UR_22 | Safety-critical | Patient arriving from transport with MMSS monitoring active. | 1) Crew and receiving team perform handover while MMSS monitoring continues uninterrupted; 2) the receiving clinician reads the current vital signs and reviews the en-route trends alongside them; 3) clinical responsibility transfers with the physiological course visible. | A1: A second opinion from UC_10 is already available — it is incorporated into the handover briefing. | E1: A sensor must be repositioned during the physical transfer — the technical alarm path (UC_07) covers the transition and monitoring of the remaining parameters continues. | Patient handed over with zero observation gap at the moment of highest clinical risk. | UT_25, UR_04, UR_22 |
| UC_13 | Conduct Simulation Training Session | Clinical Trainer / Trainee | Reach competence and justified trust on the full workflow before live use, with no possibility of confusing simulation and live operation. | UR_18, UR_19 | Safety-critical | MMSS available outside live clinical use; trainee assigned. | 1) User starts simulation training mode and confirms it is unmistakably distinguished from live operation at all times; 2) user rehearses device connection, physiological alarm response, and sensor fault recovery in realistic scenarios; 3) user practises interpreting ranked AI candidates as advisory input distinct from measured facts; 4) user ends the session and confirms the unambiguous return to live mode with no simulated data carried over. | A1: The trainer replays a scenario to repeat a weak skill until competence is reached. | E1: An attempt is made to use the system clinically while in simulation mode — the persistent, unmistakable simulation indication prevents simulated data being taken for a real patient. | User is competent and calibrated; system is back in live mode with no residual simulated data. | UT_26, UT_27, UT_28, UT_29, UR_18, UR_19 |
| UC_14 | Consult Diagnostic Source Information | Intensivist / ICU Physician | Judge the weight to give the AI's advisory candidates from its identified source and validation status. | UR_20 | Medium | Calm moment outside hands-on care (familiarisation or between deployments). | 1) Clinician opens the product information; 2) MMSS presents the source and validation status of the commercially validated AI diagnostic engine transparently; 3) clinician notes this to calibrate the weight given to advisory candidates in later episodes. | A1: Consulted during initial familiarisation training rather than between deployments. | E1: None — informational consultation outside time-critical care. | Clinician is informed about the diagnostic intelligence behind the advisory output. | UT_09, UR_20 |

### Design Decisions (DD_*)

Choices made during design, with the considered alternatives and the rationale for the final choice.

| ID | Decision | Alternatives | Rationale | Traces |
|----|----------|--------------|-----------|--------|
| DD_01 | Source the diagnostic intelligence for the first release as a commercially validated, off-the-shelf AI model (Open Evidence), integrated as a third-party (SOUP) component behind a defined library interface. | (a) Develop a custom in-house AI diagnostic model; (b) co-develop a model with a research partner; (c) defer diagnostic support to a later release. | A custom model carries the project's two highest-rated risks — regulatory clearance delay (R_01) and validation complexity (R_02). A commercially validated model caps validation effort and clearance-timing risk while still delivering the diagnostic-support value in v1.0; deferral would remove the product's core differentiator. Mandated as a first-release constraint in the project description. | BR_04, UC_04, UC_14 |
| DD_02 | Present AI diagnostic output exclusively as ranked, likelihood-ordered advisory candidates, visually and semantically distinct from measured clinical facts, with the trained clinician explicitly the final decision-maker. | (a) Present a single "most likely diagnosis"; (b) present candidates with recommended treatment actions; (c) suppress low-confidence candidates entirely. | A single or action-coupled diagnosis invites automation bias and shifts the responsibility boundary toward the manufacturer — the critical-severity misinterpretation hazard (R_05). Advisory-only ranked presentation keeps the human-in-the-loop boundary legally defensible while preserving the clinical value of differential support. | BR_06, BR_05, UC_04 |
| DD_03 | Adopt independent external risk-control paths for the safety-critical functions — measurement devices generate their own audible alarms (R_07) and ALGOS notifies audibly and independently on diagnosis timeout (R_06) — as the basis for the IEC 62304 Class C → Class B mitigation. | (a) Develop the entire MMSS software stack at Class C; (b) build a redundant internal software alarm channel inside MMSS; (c) accept a single annunciation path. | Internal redundancy within one software system cannot support a safety-classification reduction; full Class C development inflates the documentation and verification burden beyond the business case. Mutually independent external paths remove residual MMSS risk for silent alarm/timeout failure and give the classification-reduction justification notified-body-grade independence. | BR_03, BR_07, UC_05, UC_08 |
| DD_04 | Integrate all six measurement device types (ECG, pulse oximeter, BP monitor, thermal probe, capnometer, EEG) through standardised, published device interfaces defined in interface control documents, with device-internal behaviour treated as fixed and out of scope. | (a) Proprietary per-vendor driver integrations; (b) negotiate device firmware modifications for tighter coupling; (c) restrict v1.0 to a subset of device types. | Published ICDs keep the fixed hardware unmodified (software-only scope), permit supplier substitution demanded in tenders, and contractually document the MMSS/device responsibility split. Early prioritised ICD definition is the designated mitigation for the highest-probability project risk, real-time integration failure (R_03). | BR_10, BR_11, BR_12, UC_01, UC_07 |
| DD_05 | Allocate sensor-fault detection (misplacement, unreliable reading) to the measurement devices per their published interfaces, with MMSS responsible for unambiguous, device-attributed annunciation plus its own 5-second-inactivity connection alarm. | (a) MMSS performs its own signal-quality and artefact analysis on raw waveforms; (b) rely solely on device-reported status with no MMSS-side inactivity detection. | Devices are fixed components with the sensor-physics knowledge to self-detect misplacement (mitigation for R_04); duplicating that analysis in MMSS adds Class C-relevant complexity without better detection. The MMSS-side inactivity alarm covers the residual gap — a device that silently stops reporting (R_07) — so no stale value ever masquerades as a current reading. | BR_09, BR_10, UC_07, UC_02 |
| DD_06 | Integrate with hospital information systems through an established healthcare interoperability standard (HL7/FHIR, exact protocol and ICD to be fixed early), with no bespoke per-site integration. | (a) Bespoke per-hospital integration projects; (b) proprietary export format with hospital-side adapters; (c) no HIS integration in v1.0. | Standard interoperability protocols enable second opinion and prepared handover while avoiding open-ended per-site integration cost and liability; early protocol fixation is part of retiring the connectivity risk (R_03). Dropping HIS sharing would forfeit a stated product capability and procurement expectation. | BR_14, BR_12, UC_09, UC_10 |
| DD_07 | Keep all safety-relevant functions — monitoring, alarming, and diagnostic candidate display — fully locally autonomous on the host platform, with external network connectivity required only for optional HIS sharing. | (a) Cloud-hosted AI processing with on-device display; (b) hybrid local monitoring with cloud diagnostics; (c) require a guaranteed network link. | In pre-hospital and transport use no external network can be assumed; any cloud dependency in the safety path would make alarming or diagnostic support silently unavailable exactly when the patient is most exposed. Local autonomy confines connectivity loss to the optional sharing capability, which degrades visibly and recoverably. | BR_13, UC_03, UC_09 |
| DD_08 | Drive the user interface from a timer-based 1-second update cycle on the host real-time OS, within the 1-second MMSS display latency budget (DPREC ≤ 800 ms, DPROC ≤ 200 ms). | (a) Event-driven rendering on every data arrival; (b) faster (sub-second) refresh cycle; (c) per-parameter independent refresh rates. | A fixed 1 s timer gives deterministic, verifiable display latency on the embedded RTOS and bounds rendering load regardless of input rate (≥ 0.1 Hz per parameter), which event-driven rendering cannot guarantee under multi-device burst conditions. 1 s matches the specified vital-signs and alarm display budgets; faster refresh adds load without clinical benefit. | UC_02, UC_05, BR_13 |
| DD_09 | Start monitoring automatically upon device connection: MMSS recognises each connected device and presents its parameter without per-device configuration, reaching operational readiness within 10 seconds of power-on. | (a) Manual per-device setup and parameter enablement; (b) preconfigured static device profiles selected by the clinician; (c) deferred parameter display until clinician confirmation. | At first patient contact every configuration step is a treatment delay and a use-error opportunity in a high-stress mobile context. Auto-recognition over the published ICDs delivers continuous visibility within seconds of patient connection and supports operation with standard clinical training only. | BR_13, BR_15, UC_01 |
| DD_10 | Provide a dedicated simulation training mode strictly separated from live operation, with a persistent, unmistakable mode indication and no simulated data carried into live mode. | (a) Training on a separate non-clinical installation only; (b) classroom/document-based training without simulation; (c) a demo overlay within live mode. | Simulation training in the actual product is the designated risk control for the critical-severity misinterpretation hazard (R_05) and a formal release condition. Strict mode separation with persistent indication eliminates the new hazard the capability would otherwise introduce — simulated data being mistaken for a real patient. | BR_16, BR_06, UC_13 |
| DD_11 | Segregate patient data by episode: each patient connection opens a fresh episode, and no vital signs, trends, or diagnostic candidates from a previous episode are carried into the current display or shared data set. | (a) Continuous rolling data buffer across patients; (b) manual "clear patient data" action by the clinician; (c) no on-device history at all. | Episode segregation prevents the safety hazard of prior-patient data being read or shared as current-patient data at changeover, gives trends and HIS sharing a well-defined per-patient scope, and provides the data boundary on which data-protection and data-export obligations operate. Manual clearing is a foreseeable-omission use error; no history would forfeit trend review at handover. | UC_01, UC_11, UC_12, BR_17, BR_23 |
| DD_12 | Annunciate physiological and technical alarms with distinct, standards-conformant audible and visual signatures (per IEC 60601-1-8), so urgency and alarm class are recognisable by sound alone with attention away from the display. | (a) A single common alarm tone for all conditions; (b) visual-only differentiation of alarm classes; (c) proprietary non-standard alarm sound scheme. | In high-noise mobile environments the clinician triages by sound before reaching the display; a common tone forces a display check for every event and delays response to patient-critical conditions. Standards-conformant distinct signatures are a market-access prerequisite and match clinicians' trained expectations from existing monitoring equipment. | BR_08, BR_09, UC_05, UC_07 |
| DD_13 | Deliver the capability as application software only, running on the existing unmodified host CPU platform, monitor display, and installed measurement devices, maintained across the service life through software updates alone. | (a) Bundle a new purpose-built hardware platform; (b) modify the existing monitor hardware for the AI workload; (c) companion mobile device for the diagnostic display. | Software-only delivery protects the installed-base investment, keeps capital cost and time-to-market inside the business case, removes the portability/weight budget risk (R_08) from this project's scope, and makes 7–10-year field maintainability achievable through the existing update channel. | BR_11, BR_19, UC_01 |

---

# Development

## SOLUTION: Mobile Monitoring Software Solution (MMSS)

### External Interfaces

The points where the system connects to context elements, sub-systems, or other systems — connection type, data/signals exchanged, and protocols/standards.

_To be added_

The MMSS is treated as a black box; its external boundary consists of the eleven connections identified in the Context (IF_01–IF_11). The table below describes each connection at the system boundary — connection type, the data or signals exchanged across it, and the governing protocol or standard. The measurement parameters and signals carried by the six device acquisition interfaces are enumerated per source element in the Acquired Parameters / Signals table (Context section); that table is the single source of truth for the acquired parameter set and is referenced here rather than repeated.

| Interface | Connection type | Data / signals exchanged | Protocol / standard |
|-----------|-----------------|--------------------------|---------------------|
| IF_01 — ECG acquisition | Digital data acquisition from existing measurement device | ECG monitor parameters per the Acquired Parameters / Signals table (heart rate, ECG waveform) | Published ECG device ICD (existing) |
| IF_02 — Pulse oximeter acquisition | Digital data acquisition from existing measurement device | Pulse oximeter parameters per the Acquired Parameters / Signals table (SpO2, pulse rate) | Published pulse oximeter ICD (existing) |
| IF_03 — Blood pressure acquisition | Digital data acquisition from existing measurement device | Blood pressure parameters per the Acquired Parameters / Signals table | Published blood pressure monitor ICD (existing) |
| IF_04 — Temperature acquisition | Digital data acquisition from existing measurement device | Body temperature per the Acquired Parameters / Signals table | Published thermal probe ICD (existing) |
| IF_05 — Capnometry acquisition | Digital data acquisition from existing measurement device | Capnometry parameters per the Acquired Parameters / Signals table (end-tidal CO2, respiratory data) | Published capnometer ICD (existing) |
| IF_06 — EEG acquisition | Digital data acquisition from existing measurement device | EEG parameters per the Acquired Parameters / Signals table | Published EEG monitor ICD (existing) |
| IF_07 — Display presentation | Digital output to the existing monitor display | Vital signs values and waveforms, clinical and connection alarm presentations, ranked diagnostic candidates | Display interface of the existing monitor platform (existing) |
| IF_08 — AI diagnostic engine | Logical request/response exchange with external off-the-shelf AI engine | Outbound: acquired patient measurement data. Inbound: structured, ranked diagnostic candidates | Open Evidence library interface specification (existing); structured diagnostic candidate format |
| IF_09 — Hospital information system | Digital network connection to external hospital system | Diagnostic candidates shared for second opinion | HL7 or FHIR (protocol TBD); ICD to be defined in this project |
| IF_10 — Clinician interaction | Logical user-interaction boundary with the clinician | Operator commands and settings inbound; visual presentation and feedback outbound (via IF_07) | MMSS user interface specification (to be produced in this project) |
| IF_11 — Host platform execution | Logical execution/service interface to the existing host CPU platform | Platform and real-time OS services consumed by the MMSS | Real-time OS / platform API of the existing embedded CPU (existing) |

### Requirements

The full set of requirements the system must satisfy, derived from the user requirements and constrained by the context, regulatory requirements, and design decisions. Requirements are SMART and form the basis for verification.

#### Interface Requirements (RQ_IF_*)

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_IF_01 | The MMSS shall acquire the ECG monitor parameters listed in the Acquired Parameters / Signals table via the published ECG device ICD at an input rate of at least 0.1 Hz per parameter. | ECG data must arrive at the boundary at the specified minimum input rate for continuous monitoring and diagnostic support. | Class C (mitigated to Class B) | IF_01 |
| RQ_IF_02 | The MMSS shall acquire the pulse oximeter parameters listed in the Acquired Parameters / Signals table via the published pulse oximeter ICD at an input rate of at least 0.1 Hz per parameter. | SpO2 and pulse rate must arrive at the boundary at the specified minimum input rate for continuous monitoring. | Class C (mitigated to Class B) | IF_02 |
| RQ_IF_03 | The MMSS shall acquire the blood pressure parameters listed in the Acquired Parameters / Signals table via the published blood pressure monitor ICD at an input rate of at least 0.1 Hz per parameter. | Blood pressure values must arrive at the boundary at the specified minimum input rate for continuous monitoring. | Class C (mitigated to Class B) | IF_03 |
| RQ_IF_04 | The MMSS shall acquire the body temperature parameter listed in the Acquired Parameters / Signals table via the published thermal probe ICD at an input rate of at least 0.1 Hz. | Temperature must arrive at the boundary at the specified minimum input rate for continuous monitoring. | Class C (mitigated to Class B) | IF_04 |
| RQ_IF_05 | The MMSS shall acquire the capnometry parameters listed in the Acquired Parameters / Signals table via the published capnometer ICD at an input rate of at least 0.1 Hz per parameter. | Capnometry data must arrive at the boundary at the specified minimum input rate for continuous monitoring. | Class C (mitigated to Class B) | IF_05 |
| RQ_IF_06 | The MMSS shall acquire the EEG parameters listed in the Acquired Parameters / Signals table via the published EEG monitor ICD at an input rate of at least 0.1 Hz per parameter. | EEG data must arrive at the boundary at the specified minimum input rate for continuous monitoring and diagnostic support. | Class C (mitigated to Class B) | IF_06 |
| RQ_IF_07 | The MMSS shall detect a connection fault on each measurement device acquisition interface (IF_01–IF_06) within 5 seconds of data inactivity on that interface. | An undetected connection failure leads to missed vital signs; the input mandates a connection alarm trigger at 5 seconds of inactivity, observable at the system boundary as a detected fault per interface. | Class C (mitigated to Class B) | IF_01, IF_02, IF_03, IF_04, IF_05, IF_06 |
| RQ_IF_08 | The MMSS shall submit acquired patient measurement data to the external AI diagnostic engine and shall accept the resulting structured, ranked diagnostic candidates, both in conformance with the Open Evidence library interface specification. | The request/response exchange with the off-the-shelf AI engine is the sole channel for diagnostic support; conformance to the existing library interface specification makes the exchange verifiable at the boundary. | Class C (mitigated to Class B) | IF_08 |
| RQ_IF_09 | The MMSS shall present vital signs, alarm presentations, and ranked diagnostic candidates on the monitor display in conformance with the display interface of the existing monitor platform. | The monitor display is the sole visual output channel of the system; conformance to the fixed platform display interface is required because the display hardware is outside the design. | Class C (mitigated to Class B) | IF_07 |
| RQ_IF_10 | The MMSS shall transmit diagnostic candidates to the hospital information system in conformance with the baselined HIS interface control document, which shall specify either the HL7 or the FHIR protocol. | HIS sharing for second opinion requires a standardised hospital protocol; the input fixes the protocol family (HL7/FHIR), and conformance to the single baselined ICD — produced in this project and fixed before design freeze (see RQ_CS_05) — makes the exchange verifiable at the boundary. | Class C (mitigated to Class B) | IF_09 |
| RQ_IF_11 | The MMSS shall accept clinician inputs and provide operating feedback in conformance with the MMSS user interface specification produced in this project. | Trained clinicians operate the system through a defined interaction boundary; a baselined UI specification makes the interaction verifiable. | Class C (mitigated to Class B) | IF_10 |
| RQ_IF_12 | The MMSS shall obtain all platform and operating-system services exclusively through the real-time OS / platform API of the existing host CPU platform. | The host platform is fixed hardware outside the design; constraining the system to its published API keeps the execution boundary controlled and verifiable. | Class C (mitigated to Class B) | IF_11 |

#### Functional Requirements (RQ_FN_*)

What the system must do — its functions, features, and behaviors. Each traces back to a use case or user requirement.

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_FN_01 | The MMSS shall, upon system activation, reach full operational readiness with the live vital signs view available within 10 seconds. | Monitoring must start at first patient contact without delaying care; the 10-second readiness window is an externally specified activation target. | Safety-critical | UC_01, UR_01 |
| RQ_FN_02 | The MMSS shall recognise any subset of the six supported measurement device types connected at its external device interfaces — whether connected at activation or during an active episode — and continuously acquire from each connected device all parameters and signals enumerated in the Acquired Parameters / Signals table (Context section), without operator configuration. | The clinician attaches only the clinically indicated sensors, and may add or swap sensors mid-episode; the system must acquire every available parameter from whatever devices are connected, including hot-connected devices, without further configuration. | Safety-critical | UC_01, UC_02, UR_02 |
| RQ_FN_03 | The MMSS shall present the current value of every acquired parameter on the monitor display within 1 second of its acquisition. | Clinicians act on the patient's current physiological state; presentation within the externally specified 1-second window keeps the display real-time. | Safety-critical | UC_02, UR_02 |
| RQ_FN_04 | The MMSS shall cease presenting a parameter as a current value once signal inactivity from its source device reaches the 5-second connection-fault threshold (RQ_FN_09), marking the value as invalid or removing it, so that a stale reading is never displayed as live data. | A silent, stale reading mistaken for a stable patient is a direct path to missed deterioration; staleness must be exposed, never masked, and the staleness threshold must coincide with the externally specified 5-second inactivity window so display and alarm behaviour are consistent and testable. | Safety-critical | UC_02, UC_07, UR_09 |
| RQ_FN_05 | The MMSS shall provide vital signs monitoring, alarm annunciation, and diagnostic candidate display fully functional without any external network connection. | Pre-hospital and transport use cannot assume connectivity; all patient-safety functions must be delivered locally. | Safety-critical | UC_03, UR_03 |
| RQ_FN_06 | The MMSS shall detect when any acquired vital sign crosses its alarm limit and generate a physiological alarm identifying the affected vital sign. | Abnormal vital signs must be detected by the system, not discovered by the clinician scanning the display. | Safety-critical | UC_05, UR_07 |
| RQ_FN_07 | The MMSS shall annunciate each physiological alarm audibly and visually within 1 second of detection, with the abnormal vital sign identified on the display. | Intervention before deterioration requires immediate, multi-modal annunciation perceivable when the clinician's attention is away from the display. | Safety-critical | UC_05, UR_07, UR_08 |
| RQ_FN_08 | The MMSS shall annunciate physiological alarms and technical alarms with distinct audible and visual signatures such that the alarm class is distinguishable by sound alone. | Nurses triage by sound in noisy units; a patient-critical alarm must never be confused with a cable problem, or vice versa. | Safety-critical | UC_05, UC_07, UR_21 |
| RQ_FN_09 | The MMSS shall generate a connection alarm after 5 seconds of signal inactivity from any connected measurement device and present it within 1 second of the trigger, attributed to the affected device. | A disconnected sensor must be exposed within the externally specified reaction window so the stale signal is recognised and corrected. | Safety-critical | UC_07, UR_09 |
| RQ_FN_10 | The MMSS shall annunciate sensor misplacement and unreliable-reading conditions reported by a measurement device as a technical alarm unambiguously attributed to the affected sensor. | Undetected misplacement can drive a wrong diagnosis; the clinician must correct the sensor instead of acting on false data. | Safety-critical | UC_07, UR_10 |
| RQ_FN_11 | The MMSS shall allow the operator to acknowledge an annunciated alarm in no more than two interaction steps, silencing or de-escalating the annunciation while acquisition, display, and alarming of all parameters continue uninterrupted. | Alarm management must never compete with the patient for attention or interrupt monitoring. | Safety-critical | UC_06, UR_14 |
| RQ_FN_12 | The MMSS shall keep an acknowledged alarm condition visibly indicated until the underlying condition has cleared. | Acknowledgement silences the annunciation, not the clinical fact; an unresolved abnormal or fault state must remain evident. | Safety-critical | UC_06, UR_07 |
| RQ_FN_13 | The MMSS shall provide each acquired patient data value to the external AI diagnostic engine over its published interface within 1 second of its acquisition at the device interface. | The diagnostic engine can only converge on candidates if it continuously receives the live measurement data; bounding the forwarding delay to 1 second keeps the externally specified 2-minute convergence budget attributable to the engine, not to buffering inside the system. | Safety-critical | UC_04, UR_05 |
| RQ_FN_14 | The MMSS shall present the diagnostic candidates received from the external AI diagnostic engine on the monitor display within 1 second of receipt, ordered by likelihood with each candidate's likelihood indication shown, and shall update the presentation whenever a new candidate set is received. | Ranked, real-time advisory candidates alongside the vital signs support the differential diagnosis at the point of care; the 1-second display window is externally specified. | Safety-critical | UC_04, UC_08, UR_05 |
| RQ_FN_15 | The MMSS shall present every diagnostic candidate visually and semantically distinct from measured vital signs and explicitly labelled as advisory. | The clinician remains the final decision-maker; a suggestion must never be mistakable for a measured clinical fact. | Safety-critical | UC_04, UR_06 |
| RQ_FN_16 | The MMSS shall present an active, clearly perceivable notification when diagnostic candidates have not been received within the expected 2-minute convergence window or when diagnostic support is otherwise unavailable. | Silently absent diagnostic support delays treatment; the clinician must be actively told to fall back to unaided assessment. | Safety-critical | UC_08, UR_11 |
| RQ_FN_17 | The MMSS shall, upon a single operator action, transfer the current vital signs and diagnostic candidates to the hospital information system, completing the transfer within 1 second. | A second opinion must be obtainable without interrupting patient care; single-action sharing with the externally specified 1-second transfer keeps the workflow hands-free. | High | UC_09, UR_15 |
| RQ_FN_18 | The MMSS shall transfer shared vital signs and diagnostic candidates to the hospital information system in the healthcare interoperability format — HL7 or FHIR — defined in the baselined HIS interface control document. | The remote consulting clinician can only review the case if the shared data arrives in a format the hospital systems consume; naming the permitted protocol family and the governing ICD makes conformance verifiable. | High | UC_10, UR_16 |
| RQ_FN_19 | The MMSS shall, on loss of hospital connectivity, clearly indicate a sharing-only limitation while vital signs monitoring, alarming, and diagnostic candidate display continue unaffected. | The clinician must know exactly which capability is degraded; connectivity loss may never silently impair safety functions. | High | UC_09, UR_17 |
| RQ_FN_20 | The MMSS shall record the time history of every acquired parameter for the full duration of the patient episode, with recording capacity for at least 24 hours of continuous acquisition from all six supported device types simultaneously. | Trend review and handover with the physiological course visible require the episode history to be retained; an explicit minimum capacity bound makes the requirement implementable and testable on the fixed embedded platform's storage. | High | UC_11, UR_22 |
| RQ_FN_21 | The MMSS shall present, on operator request, the trend of each monitored vital sign over the patient episode alongside the current values, with acquisition gaps shown as gaps and never interpolated as valid data. | Gradual deterioration is recognised from the course, not a snapshot, and fabricated data in gaps would mislead the clinician. | High | UC_11, UC_12, UR_22 |
| RQ_FN_22 | The MMSS shall allow the operator to start a new patient episode, after which no vital signs, trends, or diagnostic candidates from any previous episode are presented within the new episode. | At patient changeover, residual data from the previous patient must never be attributed to the new patient. | Safety-critical | UC_01, UR_22 |
| RQ_FN_23 | The MMSS shall maintain uninterrupted acquisition, display, and alarming of all connected parameters throughout an active patient episode, including during patient transport and handover. | No observation gap may occur at the care-setting transitions where clinical risk is highest. | Safety-critical | UC_12, UR_04 |
| RQ_FN_24 | The MMSS shall provide a simulation training mode that the operator can enter and exit, offering realistic scenarios for device connection, alarm handling, and interpretation of AI diagnostic candidates. | Clinicians must reach competence and justified trust on the full workflow before using the system on real patients. | Safety-critical | UC_13, UR_18 |
| RQ_FN_25 | The MMSS shall, while in simulation training mode, continuously present an unmistakable simulation indication and shall keep simulated data fully separated from live patient data, with no simulated data carried over after exiting the mode. | Simulated data mistaken for a real patient — or vice versa — is a critical use error; the mode boundary must be impossible to confuse. | Safety-critical | UC_13, UR_19 |
| RQ_FN_26 | The MMSS shall present, on operator request, product information identifying the source and validation status of the external AI diagnostic engine. | Clinicians calibrate the weight given to advisory candidates from the transparent identity and validation status of the diagnostic intelligence. | Medium | UC_14, UR_20 |

#### Performance Requirements (RQ_PR_*)

Quantitative requirements on how well the system performs its functions: response times, throughput, accuracy, capacity, availability.

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_PR_01 | The MMSS shall reach full operational readiness, with the live vital signs view available on the monitor display, within 10 seconds of system activation, measured from the activation command to the first presented live view. | Quantifies the activation function with the externally specified 10-second target so monitoring can begin at first patient contact without delaying care. | Safety-critical | RQ_FN_01 |
| RQ_PR_02 | The MMSS shall present each acquired parameter value on the monitor display within 1 second of its acquisition at the external device interface, measured end-to-end at the system boundary from data arrival to visible presentation. | The 1-second end-to-end display budget is the externally specified bound that keeps the presented values clinically real-time. | Safety-critical | RQ_FN_03 |
| RQ_PR_03 | The MMSS shall annunciate each physiological alarm audibly and visually within 1 second of detection of the alarm condition, measured from arrival at the external device interface of the first acquired value that violates the alarm limit to perceivable annunciation. | Quantifies alarm annunciation with the externally specified 1-second window so intervention can begin before deterioration progresses; anchoring the measurement to data arrival at the system boundary makes the window measurable black-box. | Safety-critical | RQ_FN_06, RQ_FN_07 |
| RQ_PR_04 | The MMSS shall generate a connection alarm when signal inactivity from any connected measurement device persists for 5 seconds, measured from the last received signal at the device interface to alarm generation. | The externally specified 5-second inactivity window bounds how long a stale signal can go unexposed before the system reacts. | Safety-critical | RQ_FN_09 |
| RQ_PR_05 | The MMSS shall present each connection alarm and each sensor misplacement or unreliable-reading technical alarm on the monitor display within 1 second of the alarm trigger. | Quantifies technical alarm presentation with the externally specified 1-second window so a faulty signal source is corrected before it misleads. | Safety-critical | RQ_FN_09, RQ_FN_10 |
| RQ_PR_06 | The MMSS shall present received diagnostic candidates on the monitor display within 1 second of their receipt at the external AI diagnostic engine interface. | The externally specified 1-second display window keeps advisory candidates aligned with the live vital signs they accompany. | Safety-critical | RQ_FN_14 |
| RQ_PR_07 | The MMSS shall complete transmission of the current vital signs and diagnostic candidates within 1 second of the initiating operator action, measured from the operator action to the completed handover of the data at the MMSS hospital-information-system network interface. | Quantifies the second-opinion transfer with the externally specified 1-second target so sharing never interrupts hands-on care; the measurement endpoint is the system's own network boundary because hospital-side network and HIS processing delays are outside the system's control. | High | RQ_FN_17 |
| RQ_PR_08 | The MMSS shall sustain simultaneous acquisition from all six supported measurement device types at an input rate of at least 0.1 Hz per acquired parameter (consistent with RQ_IF_01–RQ_IF_06) while meeting all display and alarm timing requirements of this section. | The externally specified minimum input rate, sustained at full device capacity across every acquired parameter, bounds the system's worst-case acquisition load on the fixed embedded platform. | Safety-critical | RQ_FN_02 |
| RQ_PR_09 | The MMSS shall refresh all presented parameter values on the monitor display on a timer-based update cycle of 1 second, each refresh presenting every value acquired up to the start of that cycle, such that the 1-second end-to-end presentation bound of RQ_PR_02 is met for every acquired value. | The externally specified 1-second timer-based update interval gives the clinician a deterministic, predictable display refresh; binding each cycle to the values acquired before it makes the refresh mechanism provably consistent with the end-to-end display latency budget instead of silently conflicting with it. | Safety-critical | RQ_FN_03 |
| RQ_PR_10 | The MMSS shall present the diagnostic-support timeout notification when ranked diagnostic candidates have not been received from the external AI diagnostic engine within 2 minutes of the start of patient data provision to that engine. | Quantifies the absent-diagnosis notification against the engine's external 2-minute convergence budget so the clinician is actively told to fall back to unaided assessment. | Safety-critical | RQ_FN_16 |

#### Non-Functional Requirements (RQ_NF_*)

How the system should behave rather than what it does: reliability, maintainability, security, privacy, scalability. Compliance, labeling, and training requirements live here too.

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_NF_01 | The MMSS shall continue full vital-signs monitoring, alarm detection, and alarm annunciation during complete loss of external network connectivity, with only the hospital-information-system data-sharing function degrading; verified by a network-disconnection test demonstrating zero interruption of monitoring and alarming functions while offline. | In mobile pre-hospital use no external network can be assumed; the safety-relevant monitoring and alarming capability must be locally autonomous, with only optional hospital sharing permitted to degrade. | High | BR_13 |
| RQ_NF_02 | The MMSS shall restrict access to its clinical functions, configuration, and stored patient data to authenticated and authorised users, denying all unauthenticated access attempts, using an authentication mechanism that does not prevent meeting the 10-second activation-to-readiness requirement (RQ_PR_01); verified by security verification testing including negative access-attempt test cases and a timed authenticated activation. | Unprotected access to a clinical decision-support system creates patient-safety, data-protection, and hospital IT-security-review failures that block procurement and market access; in emergency pre-hospital use, access control must not delay the start of monitoring beyond the specified activation window. | Safety-critical | BR_17, RE_11 |
| RQ_NF_03 | The MMSS shall protect the integrity and authenticity of all patient data and diagnostic findings transmitted to hospital information systems such that any corruption or tampering in transit is detected and the affected data is rejected and flagged rather than presented as valid; verified by interface fault-injection and integrity testing. | Corrupted clinical data accepted as valid at the receiving hospital can drive wrong treatment decisions; demonstrated cybersecurity risk management for transmitted health data is a mandatory approval criterion. | Safety-critical | BR_17, RE_11 |
| RQ_NF_04 | The MMSS shall process, store, and transmit personal health data in conformance with applicable data-protection law (e.g. GDPR, HIPAA), including protection of patient data at rest and in transit and no disclosure to recipients other than the configured hospital information system; verified by a documented data-protection assessment against a complete data-flow inventory. | Compliance with data-protection law is a statutory market-access and procurement precondition; breaches create regulatory, liability, and patient-trust harm. | Safety-critical | BR_17, BR_23, RE_11 |
| RQ_NF_05 | The MMSS shall accept field installation of software updates — including security patches and regulatory maintenance releases — throughout a service life of up to 10 years without any modification of the host hardware platform or measurement devices, with the installed software version unambiguously identifiable after each update; verified by update installation and version-identification tests on the unmodified target platform. | The product is software-only on fixed hardware; field maintainability through software updates alone protects the customer investment and keeps lifecycle obligations deliverable, with the 10-year upper bound of the declared 7–10 year service life taken as the design bound so the obligation is unambiguous. | High | BR_19 |
| RQ_NF_06 | The MMSS shall record in a persistent, retrievable audit log every alarm condition (type, onset, annunciation, and resolution times), every set of diagnostic candidates presented (content and timestamp), and every operator action on alarms and diagnostic output, retaining the log across power cycles for the duration of the configured retention period; verified by audit-log inspection tests covering each event class. | Post-market vigilance, incident investigation, and liability defence all depend on reconstructing what the system showed and what the operator did at the time of a clinical event. | Safety-critical | BR_20, RE_12 |
| RQ_NF_07 | The MMSS shall demonstrate, through summative usability evaluation per IEC 62366-1 covering safety-related use scenarios in mobile, poorly lit, and high-noise contexts, that trained medical professionals complete the safety-related tasks without critical use errors; evidenced by a completed usability engineering file including the summative evaluation report. | Summative usability evidence for foreseeable use errors in high-stress mobile environments is a mandatory market-access prerequisite and the control for use-error hazards. | High | BR_15, RE_07 |
| RQ_NF_08 | The MMSS shall be delivered with labelling and instructions for use that state the intended use, user profile, residual risks, and limitations, and that present the diagnostic output as advisory candidates only with the trained professional as final decision-maker, conformant with the labelling requirements of each target market; verified by labelling review against the applicable regulatory labelling requirements. | Labelling is part of the device under medical device law; advisory-only positioning of AI output in the labelling keeps the manufacturer–clinician responsibility boundary legally defensible. | Safety-critical | BR_06, RE_02 |
| RQ_NF_09 | The MMSS shall provide a simulation-training mode, unambiguously distinguished from clinical operation on the display at all times, in which clinicians can exercise monitoring, alarming, and diagnostic-candidate interpretation on simulated patient data without creating, modifying, or transmitting live clinical data; verified by training-mode functional tests including verification of the mode indication and data isolation. | Simulation training is the designated risk control for the critical-severity hazard of clinician misinterpretation of AI candidates and is a release condition, not an option. | High | BR_16 |
| RQ_NF_10 | The MMSS shall segregate all acquired and derived patient data by monitoring episode such that data from one patient episode cannot be displayed within, associated with, or exported as part of another episode, and each episode's data can be individually exported and purged; verified by episode-segregation and export/purge test cases. | Cross-episode data mixing is a misdiagnosis hazard and a data-protection violation; episode-level export and purge underpin the buyer's data-ownership and retention obligations. | High | BR_23, RE_11 |
| RQ_NF_11 | The MMSS shall capture and make exportable the operational data required for post-market surveillance — software and AI-component version identification, fault and error logs, and alarm occurrence statistics — without including personal health data beyond what surveillance analysis requires; verified by inspection of the exported surveillance data set. | An operational post-market surveillance system is a statutory obligation from launch until market withdrawal; the system itself must supply the field data that surveillance and trend analysis consume. | Safety-critical | BR_20, RE_12 |

#### Constraint Requirements (RQ_CS_*)

External constraints the system must respect: regulatory rules, applicable standards, imposed technology choices, environmental conditions.

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_CS_01 | The MMSS shall be developed and maintained under a software lifecycle compliant with IEC 62304 at safety Class C, applying Class B rigour only where a documented safety-classification-reduction rationale based on independent external risk-control measures is recorded and accepted in the risk management file; evidenced by the IEC 62304 lifecycle documentation and the classification rationale. | Failing software may result in patient death; authorities require development rigour matched to the hazard class, and any classification reduction must withstand notified-body scrutiny. | Safety-critical | RE_05 |
| RQ_CS_02 | The MMSS shall be developed and maintained under a risk management process compliant with ISO 14971 covering the entire lifecycle — including hazards from sensor faults, data loss, missed or misleading alarms, and incorrect diagnostic output — with all residual risks documented and accepted before release; evidenced by a complete risk management file. | ISO 14971 risk management is the statutory backbone of market access and the basis for every benefit-risk determination by the authority. | Safety-critical | RE_06 |
| RQ_CS_03 | The MMSS shall use, in its first release, only a commercially available, validated, off-the-shelf diagnostic AI model qualified as SOUP per IEC 62304 — with documented performance claims, known anomalies, and failure behaviour — and shall include no custom-developed diagnostic model; evidenced by the SOUP qualification records in the technical file. | An off-the-shelf validated model with documented SOUP qualification caps validation effort and clearance risk, and is the imposed sourcing decision for release one. | Safety-critical | RE_09, RE_10 |
| RQ_CS_04 | The MMSS shall interface with exactly six fixed measurement device types — ECG monitor, pulse oximeter, blood pressure monitor, thermal probe, capnometer, and EEG monitor — exclusively through their published interface control documents, relying on no device behaviour not specified in those documents; verified by interface conformance testing against each published ICD. | The devices are fixed, externally owned equipment; restricting reliance to published interface definitions keeps the device-boundary hazards analysable and the responsibility split documented. | Safety-critical | RE_06 |
| RQ_CS_05 | The MMSS shall exchange patient data and diagnostic findings with hospital information systems exclusively over an established healthcare interoperability standard (HL7 or FHIR, with the protocol and interface control document fixed before design freeze), with no bespoke per-site protocol; verified by conformance testing against the selected standard's profile. | Standardised interoperability protects the integrity and traceability of transmitted health data and avoids unassessable custom integrations at each site. | High | RE_11 |
| RQ_CS_06 | The MMSS shall execute entirely on the existing fixed hardware platform — the compact embedded CPU with real-time OS capabilities and its connected monitor display — requiring no hardware design, modification, or procurement; verified by installation and full functional operation on the unmodified target platform. | The cleared system configuration, including the independent hardware risk-control paths that justify the safety-classification reduction, is defined on this fixed platform; altering it would invalidate the approval basis. | High | RE_05 |
| RQ_CS_07 | The MMSS shall present all AI diagnostic output exclusively as ranked advisory candidates for evaluation by a trained medical professional, and shall make no autonomous-diagnosis claim in any display, output, or accompanying information; verified by inspection of all diagnostic-output presentations and claims against this rule. | Authorities require human-in-the-loop positioning and transparent limitations for AI components; an autonomous-diagnosis claim would change the device qualification, classification, and required clinical evidence. | Safety-critical | RE_09 |
| RQ_CS_08 | The MMSS shall satisfy the market-access requirements of each target market — including qualification and conformity assessment as medical device software under EU MDR 2017/745 and the applicable FDA software premarket pathway — with conformity demonstrated and clearance in place before placement on that market; evidenced by the granted certificates and clearances per market. | Market access is granted per jurisdiction only through the legally mandated pathway; without demonstrated conformity in each target market the product may not be sold there. | Safety-critical | RE_01, RE_02 |

### Verification (SV_*)

The **BDD feature files** that verify the functional requirements, defined jointly by the 3-Amigos (Product Owner, Development Lead, Verification Lead). Write **one feature file per functional requirement** as a `gherkin` fenced block, tagged `@ID:RQ_FN_xx` to trace it to the requirement it verifies. Each feature has a user story (`As a … I want … So that …`), a `Rule:` that captures the requirement's "shall" statement, and one or more concrete `Scenario`s with `Given / When / Then` steps and data tables for the expected values. Use measurable outcomes (e.g. "within 5 seconds"). Every RQ_FN_* must have a feature file and every RQ_* must be covered by at least one scenario. The converter records each feature file as one row (`SV_*`) in the workbook's Verification table.

```gherkin
@ID:RQ_FN_01
Feature: Reach Operational Readiness After Activation
    As a clinician I want the live vital signs view available within 10 seconds of activating the system
    So that monitoring can begin at first patient contact without delaying care

Rule: The MMSS shall, upon system activation, reach full operational readiness with the live vital signs view available within 10 seconds.

Scenario: Live vital signs view is available within 10 seconds of authenticated activation
    Given the MMSS is installed on the unmodified target hardware platform (RQ_CS_06)
    And the simulator is running
    And the MMSS is powered off
    And the ECG Electrodes are connected in the simulator and delivering a Heart Rate of 72 /min
    When the MMSS is activated and the operator authenticates with valid credentials (RQ_NF_02)
    Then the live vital signs view is visible on the monitor display within 10 seconds of the activation command (RQ_PR_01)
    And the MMSS indicates full operational readiness within 10 seconds of the activation command (RQ_PR_01)

Scenario: Unauthenticated access to clinical functions and stored patient data is denied
    Given the MMSS is running on the unmodified target hardware platform
    When access to clinical functions, configuration, and stored patient data is attempted without valid credentials
    Then every unauthenticated access attempt is denied (RQ_NF_02)
```

```gherkin
@ID:RQ_FN_02
Feature: Recognise Connected Devices And Acquire All Parameters
    As a clinician I want the system to acquire every available parameter from whatever supported devices are connected, without any configuration
    So that I can attach only the clinically indicated sensors — also mid-episode — and still capture all available data

Rule: The MMSS shall recognise any subset of the six supported measurement device types connected at its external device interfaces — whether connected at activation or during an active episode — and continuously acquire from each connected device all enumerated parameters and signals without operator configuration.

Scenario: Acquire all parameters from a subset of devices connected at activation
    Given the simulator is running
    And the following devices are connected in the simulator
    | device         |
    | ECG Electrodes |
    | SpO₂ Probe     |
    And the simulator is configured to output the following values
    | parameter  | value   |
    | Heart Rate | 72 /min |
    | SpO2       | 97 %    |
    | Pulse Rate | 71 /min |
    When the MMSS is activated
    Then the following parameters are continuously acquired with the simulator values without any operator configuration
    | parameter  | value   |
    | Heart Rate | 72 /min |
    | SpO2       | 97 %    |
    | Pulse Rate | 71 /min |

Scenario: Acquire parameters from a device hot-connected during an active episode
    Given the simulator is running
    And the MMSS is running with an active patient episode
    And only the ECG Electrodes are connected in the simulator
    When the NIBP Cuff is connected in the simulator
    Then the following parameters are continuously acquired without any operator configuration
    | parameter    |
    | Systolic BP  |
    | Diastolic BP |
    | MAP          |
    And acquisition of Heart Rate continues uninterrupted

Scenario: Sustain acquisition from all six device types at the minimum input rate
    Given the simulator is running
    And the following devices are connected in the simulator exclusively via their published interface control documents (RQ_CS_04)
    | device              |
    | ECG Electrodes      |
    | SpO₂ Probe          |
    | NIBP Cuff           |
    | Temperature Probe   |
    | EtCO₂ Sampling Line |
    | EEG Electrodes      |
    And the simulator delivers every parameter of the Acquired Parameters / Signals table at an input rate of 0.1 Hz per parameter
    And the MMSS is running
    When acquisition is sustained for 10 minutes
    Then every parameter of the Acquired Parameters / Signals table is acquired at an input rate of at least 0.1 Hz per parameter (RQ_IF_01, RQ_IF_02, RQ_IF_03, RQ_IF_04, RQ_IF_05, RQ_IF_06, RQ_PR_08)
    And every acquired value is presented on the monitor display within 1 second of its acquisition (RQ_PR_08)
    And the recorded time history shows no acquisition gap for any parameter over the 10 minutes
```

```gherkin
@ID:RQ_FN_03
Feature: Present Current Parameter Values In Real Time
    As a clinician I want every acquired parameter value shown on the monitor display within 1 second of its acquisition
    So that I act on the patient's current physiological state, not on outdated values

Rule: The MMSS shall present the current value of every acquired parameter on the monitor display within 1 second of its acquisition.

Scenario: A newly acquired vital sign value is presented within 1 second
    Given the simulator is running
    And the MMSS is running
    And the SpO₂ Probe is connected in the simulator
    When the simulator delivers the following new values at the device interface
    | parameter  | value   |
    | SpO2       | 94 %    |
    | Pulse Rate | 88 /min |
    Then the following values are visible on the existing monitor platform display within 1 second of their acquisition at the device interface (RQ_PR_02, RQ_IF_09)
    | parameter  | value   |
    | SpO2       | 94 %    |
    | Pulse Rate | 88 /min |

Scenario: Display refreshes on a 1-second timer cycle presenting all previously acquired values
    Given the simulator is running
    And the MMSS is running
    And the ECG Electrodes are connected in the simulator and delivering Heart Rate values at 0.5-second intervals
    When the display output is recorded for 60 seconds
    Then the presented parameter values refresh on a timer-based update cycle of 1 second (RQ_PR_09)
    And each refresh presents every value acquired up to the start of that refresh cycle (RQ_PR_09)
    And every acquired value is visible on the monitor display within 1 second of its acquisition (RQ_PR_02)
```

```gherkin
@ID:RQ_FN_04
Feature: Never Display A Stale Value As Live Data
    As a clinician I want a parameter to stop being shown as a current value when its source device falls silent
    So that I never mistake a stale reading for a stable patient

Rule: The MMSS shall cease presenting a parameter as a current value once signal inactivity from its source device reaches the 5-second connection-fault threshold, marking the value as invalid or removing it.

Scenario: A parameter is marked invalid when its source device falls silent for 5 seconds
    Given the simulator is running
    And the MMSS is running
    And the ECG Electrodes are connected in the simulator and delivering a Heart Rate of 72 /min at 1-second intervals
    When the simulator stops all signal output from the ECG Electrodes
    Then after 5 seconds of signal inactivity the Heart Rate is no longer presented as a current value
    And the last Heart Rate value is marked as invalid or removed from the live view

Scenario: Live presentation resumes when the device signal returns
    Given the simulator is running
    And the MMSS is running
    And the ECG Electrodes have been silent for more than 5 seconds and the Heart Rate is marked invalid
    When the simulator resumes delivering a Heart Rate of 75 /min at 1-second intervals
    Then the Heart Rate of 75 /min is presented as a current value within 1 second
```

```gherkin
@ID:RQ_FN_05
Feature: Full Patient-Safety Function Without Network
    As a clinician in pre-hospital and transport settings I want monitoring, alarms, and diagnostic candidates fully functional without any network
    So that patient safety never depends on connectivity

Rule: The MMSS shall provide vital signs monitoring, alarm annunciation, and diagnostic candidate display fully functional without any external network connection.

Scenario: Monitoring, alarming, and diagnostic display operate with all external network connections removed
    Given the simulator is running
    And all external network connections are disconnected in the simulator
    And the simulated AI diagnostic engine is connected at its local published interface
    And the simulated AI diagnostic engine is configured to send the following candidate set
    | candidate               | likelihood |
    | Symptomatic bradycardia | 58 %       |
    And the MMSS is running
    And the ECG Electrodes are connected in the simulator
    When the simulator delivers a Heart Rate of 35 /min, below the configured lower alarm limit of 40 /min
    Then the Heart Rate value is visible on the monitor display within 1 second
    And a physiological alarm for Heart Rate is annunciated audibly and visually within 1 second
    And the configured candidate set is presented on the monitor display
    And vital signs monitoring, alarm detection, and alarm annunciation continue without interruption for 10 minutes while offline (RQ_NF_01)
```

```gherkin
@ID:RQ_FN_06
Feature: Detect Alarm Limit Violations
    As a clinician I want the system to detect when any vital sign crosses its alarm limit
    So that abnormal vital signs are detected by the system, not by me scanning the display

Rule: The MMSS shall detect when any acquired vital sign crosses its alarm limit and generate a physiological alarm identifying the affected vital sign.

Scenario: A physiological alarm is generated for each vital sign crossing its limit
    Given the simulator is running
    And the MMSS is running
    And all six supported devices are connected in the simulator
    And the following alarm limits are configured
    | vital sign  | limit type | limit value |
    | Heart Rate  | lower      | 40 /min     |
    | SpO2        | lower      | 90 %        |
    | Systolic BP | upper      | 180 mmHg    |
    When the simulator delivers the following limit-violating values
    | vital sign  | delivered value |
    | Heart Rate  | 32 /min         |
    | SpO2        | 84 %            |
    | Systolic BP | 195 mmHg        |
    Then a physiological alarm is generated for each violating vital sign
    And each alarm identifies the affected vital sign

Scenario: No physiological alarm is generated while all vital signs stay within their limits
    Given the simulator is running
    And the MMSS is running
    And all six supported devices are connected in the simulator
    And the following alarm limits are configured
    | vital sign | limit type | limit value |
    | Heart Rate | lower      | 40 /min     |
    | SpO2       | lower      | 90 %        |
    When the simulator delivers the following in-range values for 60 seconds
    | vital sign | delivered value |
    | Heart Rate | 72 /min         |
    | SpO2       | 97 %            |
    Then no physiological alarm is generated
```

```gherkin
@ID:RQ_FN_07
Feature: Annunciate Physiological Alarms Immediately
    As a clinician I want every physiological alarm annunciated audibly and visually within 1 second
    So that I can intervene before deterioration even when my attention is away from the display

Rule: The MMSS shall annunciate each physiological alarm audibly and visually within 1 second of detection, with the abnormal vital sign identified on the display.

Scenario: Audible and visual annunciation within 1 second of detection
    Given the simulator is running
    And the MMSS is running
    And the SpO₂ Probe is connected in the simulator
    And the SpO2 lower alarm limit is configured to 90 %
    When the simulator delivers an SpO2 value of 82 %, below the configured lower alarm limit, timestamped by the test harness at the device interface
    Then an audible alarm signal is emitted within 1 second of arrival of the violating value at the device interface (RQ_PR_03)
    And a visual alarm indication is shown within 1 second of arrival of the violating value at the device interface (RQ_PR_03)
    And the display identifies SpO2 as the abnormal vital sign
```

```gherkin
@ID:RQ_FN_08
Feature: Distinguish Physiological From Technical Alarms
    As a nurse triaging by sound in a noisy unit I want physiological and technical alarms to sound and look different
    So that a patient-critical alarm is never confused with a cable problem

Rule: The MMSS shall annunciate physiological alarms and technical alarms with distinct audible and visual signatures such that the alarm class is distinguishable by sound alone.

Scenario: Physiological and technical alarms have distinct signatures
    Given the simulator is running
    And the MMSS is running
    And the ECG Electrodes and the NIBP Cuff are connected in the simulator
    When the simulator delivers a Heart Rate of 30 /min, below the configured lower alarm limit of 40 /min
    And the simulator disconnects the NIBP Cuff for more than 5 seconds
    Then the following alarms are annunciated with distinct audible signatures
    | alarm class   | trigger                   |
    | physiological | Heart Rate below limit    |
    | technical     | NIBP Cuff connection lost |
    And the audio captured at the speaker output contains a distinct tone pattern per alarm class, distinguishable by sound alone
    And the visual signatures of the two alarm classes are distinct
```

```gherkin
@ID:RQ_FN_09
Feature: Alarm On Device Signal Inactivity
    As a clinician I want a connection alarm when a device falls silent for 5 seconds
    So that a disconnected sensor is exposed before its stale signal misleads me

Rule: The MMSS shall generate a connection alarm after 5 seconds of signal inactivity from any connected measurement device and present it within 1 second of the trigger, attributed to the affected device.

Scenario Outline: Connection alarm after 5 seconds of inactivity on each device interface, presented within 1 second
    Given the simulator is running
    And the MMSS is running
    And the <device> is connected in the simulator and delivering values at 1-second intervals
    When the simulator stops all signal output from the <device>
    Then a connection alarm is generated after 5 seconds of signal inactivity on the <device> interface (RQ_IF_07, RQ_PR_04)
    And the connection alarm is presented within 1 second of the trigger (RQ_PR_05)
    And the alarm is attributed to the <device>

    Examples:
    | device              |
    | ECG Electrodes      |
    | SpO₂ Probe          |
    | NIBP Cuff           |
    | Temperature Probe   |
    | EtCO₂ Sampling Line |
    | EEG Electrodes      |
```

```gherkin
@ID:RQ_FN_10
Feature: Alarm On Sensor Misplacement And Unreliable Readings
    As a clinician I want sensor misplacement and unreliable readings annunciated as a technical alarm naming the sensor
    So that I correct the sensor instead of acting on false data

Rule: The MMSS shall annunciate sensor misplacement and unreliable-reading conditions reported by a measurement device as a technical alarm unambiguously attributed to the affected sensor.

Scenario: A misplacement condition reported by a device raises an attributed technical alarm
    Given the simulator is running
    And the MMSS is running
    And the SpO₂ Probe is connected in the simulator
    When the simulator reports the following condition from the SpO₂ Probe
    | condition           |
    | sensor misplacement |
    Then a technical alarm is annunciated and presented on the monitor display within 1 second of the reported condition (RQ_PR_05)
    And the alarm is unambiguously attributed to the SpO₂ Probe

Scenario: An unreliable-reading condition raises an attributed technical alarm
    Given the simulator is running
    And the MMSS is running
    And the ECG Electrodes are connected in the simulator
    When the simulator reports an unreliable-reading condition from the ECG Electrodes
    Then a technical alarm is annunciated and presented on the monitor display within 1 second of the reported condition (RQ_PR_05)
    And the alarm is unambiguously attributed to the ECG Electrodes
```

```gherkin
@ID:RQ_FN_11
Feature: Acknowledge Alarms In Two Steps Without Interrupting Monitoring
    As a clinician I want to acknowledge an alarm in at most two interaction steps while monitoring continues
    So that alarm management never competes with the patient for attention

Rule: The MMSS shall allow the operator to acknowledge an annunciated alarm in no more than two interaction steps, silencing or de-escalating the annunciation while acquisition, display, and alarming of all parameters continue uninterrupted.

Scenario: An alarm is acknowledged in two interaction steps and monitoring continues
    Given the simulator is running
    And the MMSS is running with all six supported devices connected in the simulator
    And the simulator is delivering a Heart Rate of 32 /min, below the configured lower alarm limit of 40 /min
    And the resulting physiological alarm for Heart Rate is being annunciated
    When the operator acknowledges the alarm using no more than 2 interaction steps via the clinician interaction boundary defined in the MMSS user interface specification (RQ_IF_11)
    Then the audible annunciation is silenced or de-escalated
    And acquisition and display of all connected parameters continue uninterrupted
    And a subsequently delivered SpO2 value of 84 %, below the configured lower alarm limit of 90 %, still raises a physiological alarm within 1 second

Scenario: Alarm events, presented candidates, and operator actions are recorded in a persistent audit log
    Given the simulator is running
    And the MMSS is running with an active patient episode
    And a physiological alarm for Heart Rate has been annunciated, acknowledged by the operator, and resolved
    And the simulated AI diagnostic engine has sent a candidate set which is presented
    When the MMSS is power-cycled and the audit log is retrieved
    Then the audit log contains the alarm condition with its type, onset, annunciation, and resolution times (RQ_NF_06)
    And the audit log contains the presented candidate set with its content and timestamp (RQ_NF_06)
    And the audit log contains the operator acknowledgement action with its timestamp (RQ_NF_06)
```

```gherkin
@ID:RQ_FN_12
Feature: Keep Acknowledged Alarm Conditions Visible
    As a clinician I want an acknowledged alarm condition to stay visibly indicated until it has cleared
    So that an unresolved abnormal or fault state remains evident

Rule: The MMSS shall keep an acknowledged alarm condition visibly indicated until the underlying condition has cleared.

Scenario: Acknowledged alarm remains visible while the condition persists and disappears when it clears
    Given the simulator is running
    And the MMSS is running
    And the simulator is delivering an SpO2 value of 82 %, below the configured lower alarm limit of 90 %
    And the resulting physiological alarm for SpO2 is being annunciated
    When the operator acknowledges the alarm
    Then the SpO2 alarm condition remains visibly indicated on the monitor display
    When the simulator raises the SpO2 value to 97 %, above the lower alarm limit
    Then the visible alarm condition indication for SpO2 is cleared
```

```gherkin
@ID:RQ_FN_13
Feature: Forward Acquired Data To The AI Diagnostic Engine
    As a clinician I want every acquired patient data value forwarded to the AI diagnostic engine within 1 second
    So that the engine can converge on diagnostic candidates within its 2-minute budget

Rule: The MMSS shall provide each acquired patient data value to the external AI diagnostic engine over its published interface within 1 second of its acquisition at the device interface.

Scenario: Each acquired value arrives at the AI engine interface within 1 second
    Given the simulator is running
    And the simulated AI diagnostic engine is connected at the published interface
    And the MMSS is running
    And the ECG Electrodes are connected in the simulator
    When the simulator delivers the following values at the device interface, timestamped by the test harness
    | parameter  | value    |
    | Heart Rate | 118 /min |
    Then the simulated AI diagnostic engine receives the following values, conformant with the Open Evidence library interface specification, within 1 second of their acquisition timestamps (RQ_IF_08)
    | parameter  | value    |
    | Heart Rate | 118 /min |
```

```gherkin
@ID:RQ_FN_14
Feature: Present Ranked Diagnostic Candidates
    As a clinician I want received diagnostic candidates shown within 1 second, ranked by likelihood, and refreshed on every update
    So that ranked advisory candidates support my differential diagnosis at the point of care

Rule: The MMSS shall present the diagnostic candidates received from the external AI diagnostic engine on the monitor display within 1 second of receipt, ordered by likelihood with each candidate's likelihood indication shown, and shall update the presentation whenever a new candidate set is received.

Scenario: A received candidate set is presented within 1 second, ordered by likelihood
    Given the simulator is running
    And the MMSS is running
    When the simulated AI diagnostic engine sends the following candidate set in conformance with the Open Evidence library interface specification (RQ_IF_08)
    | candidate            | likelihood |
    | Pulmonary embolism   | 62 %       |
    | Pneumothorax         | 23 %       |
    | Anxiety reaction     | 9 %        |
    Then the candidates are visible on the monitor display within 1 second of receipt (RQ_PR_06)
    And the candidates are ordered by descending likelihood
    And each candidate's likelihood indication is shown

Scenario: The presentation updates when a new candidate set is received
    Given the simulator is running
    And the MMSS is running
    And the simulated AI diagnostic engine has sent a candidate set with top candidate "Pulmonary embolism" at 62 % which is presented
    When the simulated AI diagnostic engine sends the following new candidate set
    | candidate          | likelihood |
    | Pneumothorax       | 71 %       |
    | Pulmonary embolism | 18 %       |
    Then the presented candidate list is replaced by the new set within 1 second of receipt
```

```gherkin
@ID:RQ_FN_15
Feature: Mark Diagnostic Candidates As Advisory
    As a clinician I want every diagnostic candidate clearly distinct from measured vital signs and labelled as advisory
    So that a suggestion is never mistaken for a measured clinical fact

Rule: The MMSS shall present every diagnostic candidate visually and semantically distinct from measured vital signs and explicitly labelled as advisory.

Scenario: Candidates are visually distinct from vital signs and labelled advisory
    Given the simulator is running
    And the MMSS is running
    And the ECG Electrodes are connected in the simulator and Heart Rate is displayed
    When the simulated AI diagnostic engine sends the following candidate set
    | candidate    | likelihood |
    | Sepsis       | 48 %       |
    | Dehydration  | 31 %       |
    Then every presented candidate is visually distinct from the measured vital signs
    And every presented candidate carries an explicit advisory label
    And no diagnostic-output presentation contains an autonomous-diagnosis claim (RQ_CS_07)
```

```gherkin
@ID:RQ_FN_16
Feature: Notify When Diagnostic Support Is Absent
    As a clinician I want an active notification when diagnostic candidates fail to arrive or diagnostic support is unavailable
    So that I fall back to unaided assessment instead of waiting on silently absent support

Rule: The MMSS shall present an active, clearly perceivable notification when diagnostic candidates have not been received within the expected 2-minute convergence window or when diagnostic support is otherwise unavailable.

Scenario: Notification when no candidates arrive within the 2-minute convergence window
    Given the simulator is running
    And the MMSS is running with an active patient episode
    And the ECG Electrodes are connected in the simulator and delivering values at 1-second intervals
    And the simulated AI diagnostic engine is connected and configured to stay silent
    When 2 minutes elapse after the start of patient data provision to the engine without any candidate set received
    Then an active, clearly perceivable notification of absent diagnostic support is presented on the monitor display at the 2-minute mark (RQ_PR_10)

Scenario: Notification when diagnostic support becomes unavailable
    Given the simulator is running
    And the MMSS is running with diagnostic candidates being presented
    When the simulator disconnects the AI diagnostic engine interface
    Then an active, clearly perceivable notification that diagnostic support is unavailable is presented
```

```gherkin
@ID:RQ_FN_17
Feature: Share Patient Data With One Action
    As a clinician I want to send the current vital signs and diagnostic candidates to the hospital information system with a single action
    So that I can obtain a second opinion without interrupting patient care

Rule: The MMSS shall, upon a single operator action, transfer the current vital signs and diagnostic candidates to the hospital information system, completing the transfer within 1 second.

Scenario: A single operator action transfers vital signs and candidates within 1 second
    Given the simulator is running
    And the simulated hospital information system is connected
    And the MMSS is running with the following current data
    | data type            | content                 |
    | vital sign           | Heart Rate 122 /min     |
    | vital sign           | SpO2 89 %               |
    | diagnostic candidate | Pulmonary embolism 62 % |
    When the operator performs the single share action
    Then the simulated hospital information system receives the current vital signs and diagnostic candidates
    And the transfer completes within 1 second of the operator action, measured at the MMSS hospital-information-system network interface and timestamped by the test harness (RQ_PR_07)

Scenario: The operator is informed when the transfer cannot complete
    Given the simulator is running
    And the simulated hospital information system is unreachable
    And the MMSS is running with current vital signs and diagnostic candidates presented
    When the operator performs the single share action
    Then the operator is clearly informed that the transfer did not complete
    And vital signs monitoring, alarming, and diagnostic candidate display continue unaffected
```

```gherkin
@ID:RQ_FN_18
Feature: Share Data In The Healthcare Interoperability Format
    As a remote consulting clinician I want shared data delivered in the agreed HL7 or FHIR format
    So that the hospital systems can consume the case for review

Rule: The MMSS shall transfer shared vital signs and diagnostic candidates to the hospital information system in the healthcare interoperability format — HL7 or FHIR — defined in the baselined HIS interface control document.

Scenario: Transferred data conforms to the format defined in the HIS interface control document
    Given the simulator is running
    And the simulated hospital information system is connected
    And the MMSS is running with the following current data
    | data type            | content                 |
    | vital sign           | Heart Rate 122 /min     |
    | diagnostic candidate | Pulmonary embolism 62 % |
    When the operator performs the single share action
    Then the message captured at the simulated hospital information system validates against the message definition in the baselined HIS interface control document (RQ_IF_10, RQ_CS_05)
    And the captured message contains the shared vital signs and diagnostic candidates
    And the captured message carries integrity and authenticity protection for the patient data (RQ_NF_03)
    And the format is one of
    | format |
    | HL7    |
    | FHIR   |

Scenario: Data corrupted in transit is detected, rejected, and flagged — never presented as valid
    Given the simulator is running
    And the simulated hospital information system is connected
    And the MMSS is running with current vital signs and diagnostic candidates presented
    When the operator performs the single share action
    And the test harness corrupts the transferred message in transit
    Then the integrity verification of the corrupted message fails at the simulated hospital information system (RQ_NF_03)
    And the corrupted data is rejected and flagged as invalid rather than presented as valid (RQ_NF_03)
```

```gherkin
@ID:RQ_FN_19
Feature: Indicate Sharing Limitation On Connectivity Loss
    As a clinician I want a clear indication when only sharing is degraded by connectivity loss
    So that I know exactly which capability is limited while monitoring stays safe

Rule: The MMSS shall, on loss of hospital connectivity, clearly indicate a sharing-only limitation while vital signs monitoring, alarming, and diagnostic candidate display continue unaffected.

Scenario: Connectivity loss is indicated as a sharing-only limitation
    Given the simulator is running
    And the MMSS is running with the simulated hospital information system connected
    And the ECG Electrodes are connected in the simulator and delivering a Heart Rate of 75 /min
    And the simulated AI diagnostic engine is connected and sending candidate sets
    When the simulator disconnects the hospital connectivity
    Then a sharing-only limitation is clearly indicated on the monitor display
    And the Heart Rate remains visible and updating on the monitor display
    And a delivered Heart Rate value of 31 /min, below the configured lower alarm limit of 40 /min, still raises a physiological alarm within 1 second
    And diagnostic candidates continue to be presented
```

```gherkin
@ID:RQ_FN_20
Feature: Record The Full Episode History
    As a clinician I want the time history of every acquired parameter recorded for the whole episode
    So that trend review and handover can rely on the complete physiological course

Rule: The MMSS shall record the time history of every acquired parameter for the full duration of the patient episode, with recording capacity for at least 24 hours of continuous acquisition from all six supported device types simultaneously.

Scenario: Every acquired parameter is recorded over the episode
    Given the simulator is running
    And the MMSS is running with all six supported devices connected in the simulator
    When the simulator delivers continuous values for 30 minutes
    Then the recorded time history contains values of every acquired parameter covering the full 30 minutes

Scenario: Recording capacity covers at least 24 hours from all six device types
    # Long-duration soak test: run unattended in the overnight automated rig against the device simulator
    Given the simulator is running
    And the MMSS is running with all six supported devices connected in the simulator
    When the simulator delivers continuous values for 24 hours
    Then the recorded time history covers the full 24 hours for all acquired parameters without loss of recorded data
```

```gherkin
@ID:RQ_FN_21
Feature: Present Trends With Honest Gaps
    As a clinician I want vital sign trends over the episode shown next to the current values, with gaps shown as gaps
    So that I recognise gradual deterioration without being misled by fabricated data

Rule: The MMSS shall present, on operator request, the trend of each monitored vital sign over the patient episode alongside the current values, with acquisition gaps shown as gaps and never interpolated as valid data.

Scenario: Trend is shown on request with an acquisition gap rendered as a gap
    Given the simulator is running
    And the MMSS is running with the ECG Electrodes connected in the simulator
    And the simulator has delivered Heart Rate values for 10 minutes, with no signal between minute 4 and minute 6
    When the operator requests the Heart Rate trend
    Then the Heart Rate trend over the episode is presented alongside the current value
    And the interval between minute 4 and minute 6 is shown as a gap
    And no interpolated values are presented as valid data within the gap
```

```gherkin
@ID:RQ_FN_22
Feature: Start A Clean New Patient Episode
    As a clinician I want a new patient episode to start without any data from the previous patient
    So that residual data is never attributed to the new patient

Rule: The MMSS shall allow the operator to start a new patient episode, after which no vital signs, trends, or diagnostic candidates from any previous episode are presented within the new episode.

Scenario: No previous-episode data is presented after starting a new episode
    Given the simulator is running
    And the MMSS is running with an active patient episode containing the following data
    | data type            | content                    |
    | vital sign trend     | Heart Rate over 10 minutes |
    | diagnostic candidate | Sepsis 48 %                |
    When the operator starts a new patient episode
    Then no vital signs from the previous episode are presented
    And no trends from the previous episode are presented
    And no diagnostic candidates from the previous episode are presented

Scenario: Episode data is segregated and individually exportable and purgeable
    Given the simulator is running
    And the MMSS holds a completed patient episode A with recorded vital signs and diagnostic candidates
    And the MMSS is running with an active patient episode B containing recorded vital signs
    When the operator exports episode A
    Then the exported data set contains only data of episode A and no data of episode B (RQ_NF_10)
    When the operator purges episode A
    Then no data of episode A is retrievable on the MMSS (RQ_NF_10)
    And the data of episode B remains presented and retrievable (RQ_NF_10)
```

```gherkin
@ID:RQ_FN_23
Feature: Monitor Without Interruption Through Transport And Handover
    As a clinician I want acquisition, display, and alarming to continue uninterrupted throughout the episode
    So that no observation gap occurs at the care-setting transitions where risk is highest

Rule: The MMSS shall maintain uninterrupted acquisition, display, and alarming of all connected parameters throughout an active patient episode, including during patient transport and handover.

Scenario: Acquisition, display, and alarming continue through a simulated transport and handover
    Given the simulator is running
    And the MMSS is running with all six supported devices connected in the simulator
    And an active patient episode is in progress
    When the simulator plays a 20-minute transport and handover sequence with continuous device data
    Then the recorded time history shows no acquisition gap for any connected parameter
    And the monitor display presents current values throughout the sequence
    And an SpO2 value of 84 %, below the configured lower alarm limit of 90 %, injected at minute 12 of the sequence raises a physiological alarm within 1 second
```

```gherkin
@ID:RQ_FN_24
Feature: Train In Simulation Mode
    As a clinician I want a simulation training mode with realistic scenarios for connection, alarms, and AI candidates
    So that I reach competence and justified trust before using the system on real patients

Rule: The MMSS shall provide a simulation training mode that the operator can enter and exit, offering realistic scenarios for device connection, alarm handling, and interpretation of AI diagnostic candidates.

Scenario: Operator enters simulation mode, runs training scenarios, and exits
    Given the MMSS is running
    When the operator enters the simulation training mode
    Then the following training scenario types are available
    | scenario type                              |
    | device connection                          |
    | alarm handling                             |
    | interpretation of AI diagnostic candidates |
    When the operator runs an alarm handling scenario
    Then simulated vital signs, alarms, and diagnostic candidates are presented as in live operation
    When the operator exits the simulation training mode
    Then the MMSS returns to live operation
```

```gherkin
@ID:RQ_FN_25
Feature: Keep Simulation Unmistakably Separate From Live Data
    As a clinician I want simulation mode continuously marked and its data fully separated from live patient data
    So that simulated data is never mistaken for a real patient, or vice versa

Rule: The MMSS shall, while in simulation training mode, continuously present an unmistakable simulation indication and shall keep simulated data fully separated from live patient data, with no simulated data carried over after exiting the mode.

Scenario: Simulation indication is continuously presented during the mode
    Given the MMSS is running
    When the operator enters the simulation training mode and runs a scenario for 10 minutes
    Then an unmistakable simulation indication is continuously visible on the monitor display for the full 10 minutes (RQ_NF_09)

Scenario: No simulated data is carried over after exiting simulation mode
    Given the MMSS is running with an active live patient episode containing recorded Heart Rate history
    And the operator has entered the simulation training mode
    And the simulation has produced simulated vital signs, alarms, and diagnostic candidates
    When the operator exits the simulation training mode
    Then no simulated vital signs, trends, alarms, or diagnostic candidates are presented in live operation (RQ_NF_09)
    And the recorded live patient episode history contains no simulated data (RQ_NF_09)
    And no live clinical data was created, modified, or transmitted during the simulation (RQ_NF_09)
```

```gherkin
@ID:RQ_FN_26
Feature: Disclose AI Diagnostic Engine Provenance
    As a clinician I want product information identifying the source and validation status of the AI diagnostic engine on request
    So that I can calibrate the weight I give to its advisory candidates

Rule: The MMSS shall present, on operator request, product information identifying the source and validation status of the external AI diagnostic engine.

Scenario: Product information about the AI diagnostic engine is presented on request
    Given the MMSS is running
    When the operator requests the product information for the AI diagnostic engine
    Then the following information is presented on the monitor display
    | information item  |
    | source            |
    | validation status |
    And each information item presents a non-empty value identifying the external AI diagnostic engine

Scenario: Installed software version is unambiguously identifiable after a field software update
    Given the MMSS is running on the unmodified target hardware platform with software version 1.0.0 installed
    When the operator installs the field software update package with version 1.1.0
    Then the update installation completes without any modification of the host hardware platform or measurement devices (RQ_NF_05)
    And the presented product information identifies the installed software version as 1.1.0 (RQ_NF_05)

Scenario: Exported post-market surveillance data set contains the required operational data
    Given the MMSS is running and has annunciated alarms and recorded fault and error log entries
    When the operator exports the post-market surveillance data set
    Then the exported data set contains the following items (RQ_NF_11)
    | item                                |
    | software version identification     |
    | AI-component version identification |
    | fault and error logs                |
    | alarm occurrence statistics         |
    And the exported data set contains no patient-identifying personal health data (RQ_NF_11)
```

```gherkin
@verification:by-review
Feature: Review-Verified Requirements
    As a verification lead I want every requirement that is verifiable only by inspection or process evidence confirmed by a documented review
    So that the complete requirement set has objective verification evidence before release

Rule: The MMSS shall obtain all platform and operating-system services exclusively through the real-time OS / platform API of the existing host CPU platform (RQ_IF_12).

Scenario: Platform service usage is confirmed by code-level interface review
    Given the source code and the platform API usage inventory of the release candidate
    When the code-level interface review is performed
    Then the review confirms that all platform and operating-system services are obtained exclusively through the real-time OS / platform API (RQ_IF_12)

Rule: The MMSS shall process, store, and transmit personal health data in conformance with applicable data-protection law (RQ_NF_04).

Scenario: Data-protection conformance is confirmed by a documented assessment
    Given the documented data-protection assessment and the complete data-flow inventory
    When the data-protection review is performed
    Then the review confirms conformance with applicable data-protection law for every data flow in the inventory, including protection at rest and in transit and no disclosure beyond the configured hospital information system (RQ_NF_04)

Rule: The MMSS shall demonstrate summative usability per IEC 62366-1 for the safety-related use scenarios (RQ_NF_07).

Scenario: Summative usability evidence is confirmed by review of the usability engineering file
    Given the completed usability engineering file including the summative evaluation report
    When the usability evidence review is performed
    Then the review confirms that trained medical professionals completed all safety-related tasks in mobile, poorly lit, and high-noise contexts without critical use errors (RQ_NF_07)

Rule: The MMSS shall be delivered with labelling and instructions for use conformant with each target market's labelling requirements (RQ_NF_08).

Scenario: Labelling and instructions for use are confirmed by labelling review
    Given the labelling and instructions for use of the release candidate
    When the labelling review against the applicable regulatory labelling requirements is performed
    Then the review confirms that intended use, user profile, residual risks, and limitations are stated and that the diagnostic output is presented as advisory candidates only with the trained professional as final decision-maker (RQ_NF_08)

Rule: The MMSS shall be developed and maintained under an IEC 62304-compliant software lifecycle at safety Class C, with any Class B reduction justified in the risk management file (RQ_CS_01).

Scenario: Lifecycle compliance is confirmed by review of the IEC 62304 documentation
    Given the IEC 62304 lifecycle documentation and the safety-classification-reduction rationale
    When the lifecycle compliance review is performed
    Then the review confirms Class C lifecycle compliance and that every Class B reduction is covered by an accepted classification rationale in the risk management file (RQ_CS_01)

Rule: The MMSS shall be developed and maintained under an ISO 14971-compliant risk management process covering the entire lifecycle (RQ_CS_02).

Scenario: Risk management compliance is confirmed by review of the risk management file
    Given the complete risk management file
    When the risk management review is performed
    Then the review confirms ISO 14971 coverage of sensor faults, data loss, missed or misleading alarms, and incorrect diagnostic output, with all residual risks documented and accepted before release (RQ_CS_02)

Rule: The MMSS shall use only a commercially available, validated, off-the-shelf diagnostic AI model qualified as SOUP per IEC 62304, and no custom-developed diagnostic model (RQ_CS_03).

Scenario: SOUP qualification of the diagnostic AI model is confirmed by review of the technical file
    Given the SOUP qualification records in the technical file
    When the SOUP qualification review is performed
    Then the review confirms documented performance claims, known anomalies, and failure behaviour for the off-the-shelf model and the absence of any custom-developed diagnostic model (RQ_CS_03)

Rule: The MMSS shall satisfy the market-access requirements of each target market with conformity demonstrated and clearance in place before placement on that market (RQ_CS_08).

Scenario: Market clearances are confirmed by review of the granted certificates
    Given the granted certificates and clearances per target market
    When the market-access readiness review is performed
    Then the review confirms a granted EU MDR 2017/745 conformity assessment and a completed FDA software premarket pathway clearance before placement on each respective market (RQ_CS_08)
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
