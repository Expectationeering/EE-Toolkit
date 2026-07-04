---
Executed by: orchestration (CLAUDE.md)
Flow: flows/expectationeering-flow/flow.md
Templates: flows/expectationeering-flow/expectationeering-workbook.md
Inputs: inputs/
Date: 2026-06-11
---

# Expectationeering Workbook

**Product**: MMSS (Mobile Monitoring Software Solution)
**Date**: 2026-06-11
**Workshop Team**: User Stakeholder, Customer Stakeholder, Business Stakeholder, Regulatory Stakeholder, Product Owner, System Architect, Usability Validation, Development Lead, Verification Lead, Quality Assurance

---

# Introduction

This workbook captures the expectations and requirements for the product, from informal stakeholder expectations through to verifiable system requirements. Every requirement item has a unique identifier, starting with the stakeholder expectations, and each item traces to the upstream item it is derived from.

## Intended users of the document

This document is intended for the cross-functional expectationeering workshop team (stakeholders, product owner, architect, usability, development and verification leads, and quality assurance) and for downstream development and regulatory readers who implement, verify, and assess the resulting system requirements.

## Scope of the document

The product in scope is the MMSS medical device software (software-only scope per the project), covered from informal stakeholder expectations through to verifiable system requirements.

---

# Application

## Stakeholders (INFORMAL)

The stakeholder level is the start of the requirement approach. It captures the problem to be solved and the expectations of each stakeholder in a product-agnostic ("product-free") way.

### Problem

#### Domain Description

The domain is the real-time monitoring of critically ill patients in mobile and acute-care settings — pre-hospital emergency response (accident scene, ambulance, inter-facility transport) and in-hospital critical care (intensive care units, emergency rooms, mobile medical units). In this domain, trained clinicians attach non-invasive sensors to a patient and rely on continuously displayed vital signs to assess status, detect deterioration, and decide on treatment under severe time pressure. The domain increasingly extends beyond passive measurement to active clinical decision support: deriving ranked, real-time diagnostic candidates from the live patient data to help the clinician reach a working diagnosis quickly. Any product in this domain — and its competitors — must acquire data from heterogeneous measurement devices, present it reliably, alarm on dangerous conditions and faults, support timely diagnostic reasoning, and operate as a regulated medical device under applicable medical-device legislation and harmonised standards.

#### Actual State

**Pros**
- Trained clinicians can already observe key vital signs continuously and in real time on existing portable monitors.
- Established non-invasive measurement devices (ECG, oximetry, blood pressure, temperature, capnography, EEG) are mature, trusted, and widely deployed across the installed base.
- Clinicians apply expert professional judgement to interpret raw vital-signs trends.
- Existing monitors are portable, non-invasive, and usable across varied critical-care environments.

**Cons**
- Monitoring is largely passive: the device displays raw numbers and waveforms but does not help the clinician converge on a diagnosis.
- Reaching a working diagnosis depends entirely on the clinician's recall and reasoning under time pressure, divided attention, and high stress — slowing time-critical treatment decisions.
- Diagnostic support, where it exists at all, is not fast enough, not derived from the live patient data, or not integrated into the monitoring workflow.
- Sensor disconnection or misplacement can go unnoticed, allowing decisions on missing or misleading data.
- Alarm streams are not always prioritised, contributing to alarm fatigue and missed critical events.
- Handover to the receiving hospital and access to a second opinion are often manual, with data not flowing into hospital information systems.
- Onboarding clinicians on new monitoring capability typically requires live exposure, with no safe practice environment.

#### Desired State

**Pros (retained from the actual state)**
- Continuous, real-time, negligible-delay display of key vital signs remains.
- The mature installed base of non-invasive measurement devices continues to be used through standardised interfaces.
- Clinician professional judgement remains central; the clinician stays in control.
- The solution remains portable, non-invasive, and usable across mobile and acute-care environments.

**Pros (newly achieved)**
- Ranked diagnostic candidates are derived from the live patient data and delivered to the clinician quickly after the patient is connected, focusing assessment and accelerating treatment.
- Each candidate is presented with the reasoning and confidence behind it, so the clinician can apply judgement and avoid over-reliance on automated output.
- The clinician is monitoring within seconds of switching on and connecting.
- Vital-sign, sensor-fault, and connection alarms are clear, unmistakable, prioritised, and distinguishable, so genuine emergencies stand out without alarm fatigue.
- The clinician is notified when diagnostic support cannot reach a conclusion in the expected time and can fall back to manual assessment without silent delay.
- A safe simulation mode lets clinicians practise the device and the interpretation of diagnostic output before live use.
- Monitored data and diagnostic findings can be shared with the receiving hospital for smooth handover and a continuing second opinion.
- The capability is delivered as a compliant, regulated, auditable, maintainable medical device backed by enforceable commercial and post-market obligations.

**Cons (residual)**
- Active diagnostic support introduces a new risk of clinician misinterpretation or over-reliance that must be controlled.
- Faster, integrated capability raises regulatory clearance, validation, interoperability, data-protection, and lifecycle-support obligations that must be met before and after market access.

#### Identified Gaps (DC_*)

The design changes needed to move from the actual state to the desired state.

| ID | Description |
|----|-------------|
| DC_01 | Add active clinical decision support that derives ranked diagnostic candidates from the live patient data, converging on candidates quickly after the patient is connected, in place of purely passive vital-signs display. |
| DC_02 | Make the basis of each diagnostic candidate transparent — the supporting reasoning and a confidence indication — so the clinician can apply professional judgement and avoid over-reliance on automated output. |
| DC_03 | Reduce time-to-readiness so a clinician can begin monitoring a patient within seconds of switching on and connecting. |
| DC_04 | Guarantee continuous, real-time display of key vital signs with negligible delay between measurement and presentation. |
| DC_05 | Detect and signal sensor disconnection, misplacement, or otherwise invalid data so the clinician never acts on missing or misleading readings. |
| DC_06 | Provide clear, unmistakable, prioritised, and distinguishable alarms for out-of-limit vital signs and faults, so genuine emergencies stand out and alarm fatigue is controlled. |
| DC_07 | Notify the clinician when diagnostic support cannot reach a conclusion within the expected time, enabling an immediate fall-back to manual assessment without silent delay. |
| DC_08 | Integrate monitored data and diagnostic findings with hospital information systems through standard healthcare interoperability protocols, to support handover and a continuing second opinion. |
| DC_09 | Preserve the existing installed base by interfacing with the established non-invasive measurement devices and host platform through standardised, stable interfaces, avoiding wholesale equipment replacement. |
| DC_10 | Provide a safe simulation/training capability for clinicians to practise device operation and the interpretation of diagnostic output before live use. |
| DC_11 | Ensure operability for trained clinicians in noisy, moving, low-light, high-stress conditions with minimal additional training burden, applying documented usability engineering for safety. |
| DC_12 | Develop, verify, and maintain the solution as a regulated medical device under a documented, risk-managed software lifecycle commensurate with its safety class, with auditable design-history and traceability evidence. |
| DC_13 | Control residual patient-safety risk through independent protective measures and a justified safety classification, rather than relying on any single point of failure. |
| DC_14 | Establish the lifecycle, commercial, and post-market footing — clinical evidence, data protection, labelling and instructions for use, maintainability, predictable cost of ownership, post-market surveillance, and end-of-life commitments — required to place and sustain the solution on the market. |

### Expectations

Stakeholder expectations are written "product-free": they apply to any product in the problem domain, including competitors. Format: *The \<stakeholder\> wants \<expectation\> to \<benefit driver\>.*

#### User Expectations (UE_*)

**Stakeholder**: Clinician (pre-hospital & critical care)

Trained medical professional — paramedic, emergency physician, ICU/ER nurse, or mobile-care clinician — who attaches non-invasive sensors to critically ill patients and acts on the displayed information under time pressure. Works across varied, often mobile environments (ambulance, accident scene, transport, ICU, ER) where attention is divided and conditions are unpredictable.

| ID | Expectation | Traces |
|----|-------------|--------|
| UE_01 | The clinician wants to see the patient's key vital signs continuously and in real time, with negligible delay between measurement and display, to maintain an accurate moment-to-moment picture of patient status. | DC_04 |
| UE_02 | The clinician wants to be ready to monitor a patient within seconds of switching on and connecting, to avoid losing critical time at the start of an emergency. | DC_03 |
| UE_03 | The clinician wants ranked diagnostic candidates derived from the live patient data delivered quickly after the patient is connected, to focus assessment and accelerate appropriate treatment decisions. | DC_01 |
| UE_04 | The clinician wants to understand why each diagnostic candidate is suggested and how confident the suggestion is, to apply professional judgement and avoid over-relying on automated output. | DC_02 |
| UE_05 | The clinician wants a clear, unmistakable alarm when any vital sign moves outside safe limits, to react immediately to patient deterioration even when attention is elsewhere. | DC_06 |
| UE_06 | The clinician wants to be alerted when a sensor is disconnected, misplaced, or otherwise not producing valid data, to avoid acting on missing or misleading readings. | DC_05 |
| UE_07 | The clinician wants to be notified if diagnostic support cannot reach a conclusion within an expected time, to avoid silently waiting and to fall back on manual assessment without delay. | DC_07 |
| UE_08 | The clinician wants alarms and information to be distinguishable and prioritised so genuine emergencies stand out, to act on the most critical event first and avoid alarm fatigue. | DC_06 |
| UE_09 | The clinician wants to operate the device quickly and intuitively in noisy, moving, low-light, and high-stress conditions, to use it effectively without diverting attention from the patient. | DC_11 |
| UE_10 | The clinician wants to practise using the device and interpreting its diagnostic output in a safe simulation mode before live use, to build competence and confidence without risk to real patients. | DC_10 |
| UE_11 | The clinician wants to share the monitored data and diagnostic findings with the receiving hospital, to support a smooth handover and a second opinion that continues the patient's care. | DC_08 |

#### Market Expectations (ME_*)

**Stakeholder**: Hospital / EMS Procurement & Value-Analysis

Represents the buying organisation — health-system value-analysis committees, biomedical/clinical engineering, and ambulance-service (EMS) purchasing — that evaluates, selects, funds, and contracts critical-care monitoring solutions across acute and pre-hospital settings. Their decisions weigh clinical value, total cost of ownership, regulatory clearance, interoperability, supportability, and commercial risk.

| ID | Expectation | Traces |
|----|-------------|--------|
| ME_01 | The hospital procurement organisation wants any candidate critical-care monitoring solution to hold valid medical-device regulatory clearance for its intended use before purchase, to ensure lawful market access and protect the buyer from compliance and liability exposure. | DC_12, DC_14 |
| ME_02 | The value-analysis committee wants a critical-care monitoring solution to demonstrate measurable clinical benefit — faster, better-informed diagnosis in mobile and acute care — to justify the acquisition spend against patient-outcome and reimbursement goals. | DC_01, DC_14 |
| ME_03 | The biomedical engineering department wants a monitoring solution to interoperate with established hospital information systems through standard healthcare interoperability protocols, to avoid costly custom integration and enable continuity of patient data into the electronic record. | DC_08 |
| ME_04 | The procurement organisation wants a monitoring solution to integrate with the non-invasive measurement devices already in its installed base through standardised device interfaces, to protect prior capital investment and avoid wholesale equipment replacement. | DC_09 |
| ME_05 | The health-system finance function wants a critical-care monitoring solution to offer a predictable, competitive total cost of ownership — including licensing, updates, service, and consumables — to keep the acquisition within budget and forecastable over the asset's life. | DC_14 |
| ME_06 | The clinical engineering organisation wants a monitoring solution to be serviceable and maintainable with clear update, patch, and support commitments, to minimise downtime and sustain device availability throughout its operational life. | DC_14 |
| ME_07 | The EMS purchasing organisation wants a monitoring solution to be usable by trained clinicians with minimal additional training burden, to limit adoption cost and protect frontline productivity during rollout. | DC_11 |
| ME_08 | The procurement organisation wants a critical-care monitoring solution to provide a built-in simulation or training capability, to reduce the cost and clinical risk of onboarding staff without exposing patients. | DC_10 |
| ME_09 | The value-analysis committee wants a monitoring solution to provide clinical decision support that demonstrably differentiates it from passive vital-signs monitoring, to justify selecting it over lower-cost incumbent alternatives. | DC_01, DC_02 |
| ME_10 | The procurement and contracting function wants a monitoring solution to be backed by enforceable commercial terms — warranty, liability allocation, data-protection compliance, and supply continuity — to make the purchase contractable and limit institutional risk. | DC_14 |

#### Business Expectations (BE_*)

**Stakeholder**: Legal Manufacturer

The legal manufacturer is the organisation that designs, produces, and places the medical device software on the market, and therefore carries full regulatory, liability, and post-market responsibility for it. It speaks across executive strategy, legal & compliance, finance, operations, R&D, quality management, regulatory affairs, sales, service, and HR.

| ID | Expectation | Traces |
|----|-------------|--------|
| BE_01 | The legal manufacturer wants the diagnostic-support capability built on a commercially validated off-the-shelf analysis engine to reduce its own validation burden and accelerate time-to-market. | DC_01, DC_12 |
| BE_02 | The legal manufacturer wants the safety-critical alarming and diagnostic functions to be mitigated to independent, lower-risk classification to contain liability exposure and constrain development and verification cost. | DC_13 |
| BE_03 | The legal manufacturer wants the device to be developed under a compliant software lifecycle with a complete design history file so that it can demonstrate due diligence and satisfy external audit and certification obligations. | DC_12 |
| BE_04 | The legal manufacturer wants the residual patient-safety risk to rest with independent protective measures rather than with a single point of failure so that it limits its responsibility for clinical harm. | DC_13 |
| BE_05 | The legal manufacturer wants the solution to integrate with existing, fixed measurement and host platforms through published, stable interfaces to avoid hardware investment and protect the business case. | DC_09 |
| BE_06 | The legal manufacturer wants a robust post-market surveillance and complaint-handling capability so that it can meet its ongoing regulatory obligations and respond to field issues without disproportionate cost. | DC_14 |
| BE_07 | The legal manufacturer wants the product to be maintainable and serviceable across its full lifecycle so that defect correction, updates, and support remain affordable and sustainable for the organisation. | DC_14 |
| BE_08 | The legal manufacturer wants the diagnostic-support capability to be differentiated and defensible in the market so that it strengthens competitive positioning and protects intellectual-property value. | DC_01, DC_02 |
| BE_09 | The legal manufacturer wants the product to be manufacturable and deployable at the required scale and quality level so that production and rollout stay within operational capacity and margin targets. | DC_14 |
| BE_10 | The legal manufacturer wants clear end-of-life, support, and decommissioning commitments defined up front so that it can plan workforce competency, contractual obligations, and long-term financial exposure. | DC_14 |

#### Regulatory Expectations (RE_*)

**Stakeholder**: Competent Authority / Notified Body

The government bodies, competent authorities, and accredited notified bodies that determine whether AI-driven diagnostic decision-support software for critical-care monitoring may lawfully be placed on a market. They hold the product to account against applicable medical-device legislation, harmonised standards, and post-market obligations, and can approve, defer, refuse, or withdraw market access.

| ID | Expectation | Traces |
|----|-------------|--------|
| RE_01 | The Competent Authority wants medical-device software in the critical-care monitoring domain to be developed, verified, and maintained under a documented software life-cycle process commensurate with its safety class (per IEC 62304) to ensure systematic control of software risk throughout development and maintenance. | DC_12 |
| RE_02 | The Competent Authority wants the safety classification of diagnostic and alarm-bearing monitoring software to be justified by a documented risk-management process (per ISO 14971) that identifies hazards, estimates and controls risk, and demonstrates acceptable residual risk before market access is granted. | DC_12, DC_13 |
| RE_03 | The Notified Body wants clinical evidence demonstrating the safety, performance, and clinical benefit of AI-assisted diagnostic output to be provided, so that the claimed intended use and diagnostic indications are substantiated rather than asserted. | DC_01, DC_14 |
| RE_04 | The Notified Body wants any off-the-shelf, third-party, or unknown-provenance software component — including a commercially supplied AI diagnostic model — to be qualified, version-controlled, and risk-assessed (SOUP qualification) so that responsibility for the integrated device is fully evidenced regardless of component origin. | DC_12 |
| RE_05 | The Competent Authority wants usability engineering for safety to be applied and documented (per IEC 62366) so that use-related hazards, including misinterpretation of ranked diagnostic candidates by trained clinicians, are identified, mitigated, and validated under representative use conditions. | DC_02, DC_11 |
| RE_06 | The Competent Authority wants the alarm system for abnormal physiological conditions and sensor faults to conform to applicable alarm-safety standards so that clinically actionable conditions are signalled reliably and alarm fatigue or missed alarms are controlled. | DC_05, DC_06 |
| RE_07 | The Surveillance Authority wants patient data processed, displayed, or transmitted to external information systems to be protected in accordance with applicable data-protection and privacy law, so that confidentiality, integrity, and lawful handling of health data are assured. | DC_08, DC_14 |
| RE_08 | The Notified Body wants full design-history and traceability evidence — linking requirements, risk controls, design, and verification — to be maintained and auditable, so that conformity of the technical documentation can be assessed and reproduced. | DC_12 |
| RE_09 | The Competent Authority wants labelling and instructions for use to accurately state the intended use, indications, contraindications, residual risks, limitations of the AI diagnostic support, and required user training, so that the device is used safely and within its validated scope. | DC_02, DC_14 |
| RE_10 | The Surveillance Authority wants a post-market surveillance and vigilance system to be established, including incident reporting, periodic safety review, and field safety corrective actions, so that emerging risks of devices already in clinical use are detected and acted upon. | DC_14 |
| RE_11 | The Competent Authority wants AI-driven decision-support functionality to meet specific transparency, performance-characterisation, and change-control obligations — including disclosure of the model's validated performance, intended population, and known limitations — so that the basis of the diagnostic recommendation is interpretable and its performance is monitorable over its lifecycle. | DC_02, DC_07 |

### Ideal Product Model (KA_*)

The Ideal Product Model is the blueprint that aligns stakeholder expectations with product capabilities — the key proposition attributes, their priority, feasibility, and risk.

| ID | Benefit Driver | Expectation | Proposition Attributes | Superior to | Priority | Feasible | Risk | Rationale |
|----|----------------|-------------|------------------------|-------------|----------|----------|------|-----------|
| KA_01 | Real-time situational awareness | UE_01 | Continuous concurrent acquisition from multiple non-invasive sources with bounded, deterministic measurement-to-display latency | Passive monitors with perceptible refresh lag or periodic sampling | High | High | Low | Bounded-latency continuous display is a mature, well-understood monitoring capability; the only engineering care needed is deterministic scheduling of concurrent multi-source streams, which is routine for this class of device. |
| KA_02 | Time-to-readiness in emergencies | UE_02 | Bounded power-on-to-monitoring readiness for the safety-relevant signal set, with safety self-test and sensor settling completed before valid display | Devices requiring lengthy boot, calibration, or configuration before use | High | Med | Med | Fast start is decisive in emergencies and achievable, but it is in direct tension with mandatory power-on self-test and physiological sensor settling; the residual risk is that aggressive startup time omits integrity checks, so the budget must be characterised, not assumed. |
| KA_03 | Faster, focused diagnosis | UE_03, ME_02, ME_09, BE_08, RE_03 | Automated ranked diagnostic candidate generation from live multi-parameter data, converging to a stable ranking within a bounded time after connection and at a characterised diagnostic-performance level | Passive vital-signs monitoring offering no diagnostic interpretation | High | Med | High | Core differentiator and main clinical-value claim; feasibility is constrained by the need to demonstrate convergence, bounded inference latency, and validated diagnostic performance against clinical evidence, making this the highest-risk capability technically and from a regulatory-evidence standpoint. |
| KA_04 | Trust and appropriate reliance | UE_04, ME_09, RE_05, RE_09, RE_11 | Per-candidate rationale and calibrated confidence indication, derived from and consistent with the diagnostic output | Opaque automated output presented without rationale or confidence | High | Med | Med | Explainability and well-calibrated confidence are essential to safe clinical reliance and regulatory transparency; feasibility depends on the underlying diagnostic capability (KA_03) being able to expose faithful, non-misleading explanations, so it inherits part of that capability's risk. |
| KA_05 | Immediate response to deterioration | UE_05, UE_08, RE_06 | Clear, prioritised, unmistakable alarms on safe-limit breach, distinguishable from lower-priority information, with high detection reliability and controlled false-alarm rate | Undifferentiated or easily-missed alerts prone to alarm fatigue | High | High | High | Standards-driven alarm behaviour (alarm-safety standards) is well established and feasible, but this is a directly safety-critical function: prioritisation that suppresses fatigue must never delay or mask a genuine emergency, so the failure consequence is severe and the risk is high despite mature technology. |
| KA_06 | Protection against misleading data | UE_06, RE_06 | Per-source signal-quality and fault detection that distinguishes disconnection, misplacement, and invalid data, and always explicitly indicates affected readings rather than letting a parameter silently drop out | Systems that display readings without flagging compromised signal integrity | High | High | Med | Signal-quality and fault detection are established per-channel functions, but the business raises risk from Low to Med: silent propagation of invalid data into display or diagnosis is a textbook source of patient-harm complaints and post-market vigilance reporting, and the fault-detection coverage depends on third-party measurement devices the manufacturer does not control (see KA_11). The technology is mature; the liability consequence of an undetected invalid reading is not, so the risk is not negligible. |
| KA_07 | Safe fallback to manual assessment | UE_07, RE_11 | Notification when diagnostic support cannot reach a conclusion within an expected time | Decision-support that fails silently, leaving clinicians waiting | High | High | Low | Technically modest to implement, but the business view raises priority: this fallback is part of the manufacturer's liability and risk-control narrative — it is an explicit safe-state behaviour that limits responsibility for clinical harm when the diagnostic capability is unavailable, and it underpins the residual-risk argument in KA_13. Cheap to build, high in liability value, so it should not be deprioritised as a mere convenience. |
| KA_08 | Effective use under stress | UE_09, ME_07, RE_05 | Intuitive, rapid operation tolerant of noisy, moving, low-light, high-stress environments | Interfaces designed for stable clinical settings that degrade in the field | High | Med | Med | Field-robust usability is achievable through human-factors engineering but must be validated under representative use to satisfy safety and adoption goals. |
| KA_09 | Risk-free competence building | UE_10, ME_08 | Built-in safe simulation/training mode for practising operation and diagnostic interpretation without live patients | Solutions requiring live-patient exposure or external simulators for training | Med | High | Low | A self-contained training mode is technically modest and reduces onboarding cost and clinical risk for buyers and users alike. |
| KA_10 | Continuity of care across handover | UE_11, ME_03, RE_07 | Export of monitored data and diagnostic findings through standard healthcare interoperability protocols, with end-to-end data protection and integrity | Closed devices that cannot export data into the receiving record | High | Med | Med | Standards-based interoperability is mature, but the breadth of receiving-system protocol variants and the privacy-law and data-integrity assurance burden add real integration and verification effort. |
| KA_11 | Investment protection through integration | ME_04, BE_05 | Integration with the heterogeneous installed base of non-invasive measurement devices through standardised device interfaces, tolerating variation across makes, models, and firmware revisions | Solutions mandating wholesale replacement of existing measurement equipment | High | Med | High | Reusing fixed measurement and host platforms protects capital and the business case, but feasibility rests on interfaces the manufacturer does not control: real-world installed bases vary in protocol conformance and firmware, so undocumented or non-conformant behaviour is a significant integration and verification risk. |
| KA_12 | Lawful, contractable market access | ME_01, ME_10, RE_01, RE_02, RE_04, RE_08 | Conformity to applicable medical-device regulation, documented safety classification, lifecycle process, and auditable traceability | Offerings lacking valid clearance or complete conformity evidence | High | Med | High | Non-negotiable for market access; achievable but carries substantial evidence, classification, and audit burden, especially for AI-driven functionality. |
| KA_13 | Contained liability and safe residual risk | BE_02, BE_04, RE_02 | Demonstrably independent protective measures that carry the safety function separately from the diagnostic capability, justifying a lower safety classification with no shared single point of failure | Architectures where one diagnostic/alarm function bears unmitigated safety risk | High | Med | High | Risk mitigation through independent protective layers is a recognised pattern, but proving genuine independence — freedom from shared dependencies that would otherwise force the higher classification — is demanding to design and to evidence; latent coupling is a common failure mode, so the risk is high. |
| KA_14 | Predictable cost and sustained availability | ME_05, ME_06, BE_07, BE_09, BE_10 | Maintainability, serviceability, scalable manufacture/deployment, and predictable total cost of ownership across the full lifecycle | Solutions with opaque ongoing cost or limited support and update commitments | Med | High | Low | Lifecycle supportability and cost predictability are well-understood commercial and operational disciplines that drive buyer and manufacturer confidence. From the business view, priority stays Med (it does not gate market access) but it is the dominant driver of long-run margin: serviceability, update cadence, and decommissioning commitments must be designed in up front, because retrofitting maintainability and committing to end-of-life support later is where total cost of ownership and workforce-competency exposure silently erode the business case. |
| KA_15 | Sustained compliance after market entry | BE_03, BE_06, RE_10 | Compliant software lifecycle with design history file and post-market surveillance, vigilance, and complaint-handling capability | Products without robust ongoing surveillance and corrective-action capability | High | High | Med | Lifecycle documentation and post-market obligations are established practice; sustaining them affordably is the principal challenge. From the business view this is a non-discretionary, ongoing legal-manufacturer responsibility that persists for the device's entire market life: incident reporting, periodic safety review, and field corrective actions are statutory duties whose cost and staffing must be provisioned from launch, and for AI-driven diagnostic functionality the surveillance load (monitoring real-world performance drift) is heavier than for conventional software — hence Med risk despite mature process. |
| KA_16 | Reduced validation burden via proven components | BE_01, RE_04 | Use of qualified, version-controlled, commercially validated off-the-shelf analysis components with full provenance, characterised performance, and documented risk assessment | Bespoke unvalidated analysis components carrying full first-party validation load | High | Med | High | Leveraging validated off-the-shelf capability can accelerate time-to-market, but a third-party analysis component — especially one with opaque internals or training provenance — may not expose the performance characterisation, change-control, and traceability evidence the integrated device must own; if it does not, the expected validation saving inverts into rework. The business raises priority from Med to High because BE_01 makes this the manufacturer's deliberate validation-burden and time-to-market strategy: as legal manufacturer the organisation carries full responsibility for the integrated device regardless of component origin (per SOUP/RE_04), so the qualification, provenance, and supplier change-control terms must be secured up front as a strategic procurement and liability decision, not treated as a mid-tier engineering convenience. |

### Business 'Requirements' (BR_*)

Conceptual project inputs from all business stakeholders that apply across the whole product lifecycle (development, launch, manufacturing, deployment, operation & use, end of life).

| ID | Description | Rationale | Stakeholder | Importance | Traces |
|----|-------------|-----------|-------------|------------|--------|
| BR_01 | The offering shall be developed and placed on the market in conformity with the applicable medical-device regulation for the intended jurisdictions, with a documented and defensible safety classification established early in development. | Conformity and a correct safety classification are non-negotiable preconditions for lawful market access and determine the entire downstream evidence, process, and audit burden; classifying late or wrongly forces costly rework. | Regulatory | High | KA_12 |
| BR_02 | The development, manufacture, and lifecycle activities of the offering shall be conducted under a certified quality-management system providing auditable traceability from need through verification. | A certified QMS with full traceability is required to demonstrate conformity, pass external audit, and sustain the device's regulatory standing across its market life. | Quality | High | KA_12, KA_15 |
| BR_03 | A risk-management process conforming to the recognised medical-device risk-management standard shall run across the full lifecycle, with documented hazard analysis, risk controls, and residual-risk justification. | Safety-critical diagnostic and alarm behaviour demands systematic hazard identification and control; the residual-risk argument underpins both clinical safety and the manufacturer's liability position. | Quality | High | KA_05, KA_06, KA_13 |
| BR_04 | The safety function (safe-limit alarming) shall be realised through protective measures that are demonstrably independent of the diagnostic-support capability, sharing no common computing, power, timing, or data-path dependency that could constitute a single point of failure, so that the device's safety classification can be justified at the lowest defensible level. | Independent protective layers contain liability and reduce the certification burden, but genuine independence must be designed in and evidenced at the dependency level — shared processing, power, clock, or data paths are the latent coupling that silently defeats the independence claim and would force a higher classification. | Legal Manufacturer | High | KA_13, KA_07 |
| BR_05 | The diagnostic-support capability shall be substantiated by clinical evidence demonstrating its diagnostic performance, ranking-convergence behaviour, and bounded end-to-end inference latency (data-availability to ranked-output, treated as a budget the integrated system observes at its boundary) at a characterised level before market entry. | The diagnostic capability is the principal value claim and the highest-risk element; performance and the boundary-observable latency/convergence budget must be characterised on real data, not assumed, because the inference may run in an acquired off-the-shelf or external analysis component whose timing the device must still own at its boundary. | Regulatory | High | KA_03, KA_04 |
| BR_06 | The project shall adopt qualified, version-controlled, commercially validated off-the-shelf analysis capability with documented provenance, characterised performance, change-control, and risk assessment, in preference to bespoke unvalidated analysis components, wherever such capability meets the device's requirements. | Reusing validated off-the-shelf analysis capability is the deliberate strategy to reduce first-party validation load and accelerate time-to-market; the saving only holds if provenance and change-control evidence are secured up front. | Procurement | High | KA_16 |
| BR_07 | Supplier agreements for any incorporated third-party analysis or measurement capability shall secure performance characterisation, provenance, defect notification, and change-control terms commensurate with the legal manufacturer's full responsibility for the integrated device. | The legal manufacturer carries full responsibility for the integrated device regardless of component origin; supplier-of-unknown-provenance obligations must be contracted, not assumed. | Procurement | High | KA_16, KA_11 |
| BR_08 | The offering shall interoperate with the heterogeneous installed base of non-invasive measurement devices through standardised device interfaces governed by controlled interface specifications, tolerating variation across makes, models, and firmware revisions and degrading gracefully on non-conformant or undocumented device behaviour rather than mandating wholesale replacement of existing equipment. | Reusing the existing measurement installed base protects customer capital and the commercial case; because the manufacturer does not control these external interfaces, integration must rest on controlled interface specifications and must tolerate — and explicitly handle — real-world protocol and firmware non-conformance instead of assuming compliant behaviour. From the buyer's view, fit with the installed device base and existing clinical IT is a primary selection criterion: an offering that demands wholesale equipment replacement carries a prohibitive switching cost and is commonly rejected on that basis alone. | Legal Manufacturer | High | KA_11 |
| BR_09 | The offering shall export monitored data and diagnostic findings through standard healthcare interoperability protocols to receiving clinical record and device ecosystems, preserving end-to-end data integrity and the provenance and timestamp of each exported item. | Continuity of care across handover depends on standards-based exchange into the receiving record; closed data is a procurement and clinical-workflow blocker, and exported diagnostic findings must retain integrity, source provenance, and timing so the receiving system can interpret and trust them. | Legal Manufacturer | High | KA_10 |
| BR_10 | Personal and clinical data handled, stored, or transmitted by the offering shall be protected in conformity with applicable data-protection law and healthcare information-security obligations across its lifecycle. | Handling identifiable patient data imposes statutory privacy and security duties; non-conformity blocks deployment and exposes the manufacturer to regulatory and liability action. | Legal Manufacturer | High | KA_10 |
| BR_11 | The offering shall achieve a time-to-market consistent with the clinical and commercial window for emergency point-of-care diagnostic support, balancing speed against the mandatory evidence and conformity burden. | Time-to-market drives competitive positioning and return, but must not be bought by shortcutting safety evidence or conformity; the validated-component strategy exists partly to protect this balance. | Customer | Med | KA_03, KA_16 |
| BR_12 | The offering shall be designed for maintainability and serviceability, with a defined update and support cadence, so that ongoing operational cost and availability remain predictable across the lifecycle. | Serviceability and update cadence must be designed in up front; retrofitting maintainability later is where total cost of ownership and availability commitments silently erode. From the buyer's view this is procurement-decisive, not discretionary: clinical and EMS operations cannot tolerate unplanned downtime, so demonstrable serviceability and a committed update cadence are weighed as heavily as functional capability and frequently gate the purchase. | Legal Manufacturer | High | KA_14 |
| BR_13 | The offering shall be manufacturable and deployable at the scale required by the target markets, with a total cost of ownership that is transparent and predictable to buyers across the full lifecycle. | Scalable manufacture and transparent lifecycle cost are decisive buyer-confidence and margin factors; opaque ongoing cost undermines the commercial case. Institutional buyers (hospital and EMS procurement) require a defensible multi-year TCO — acquisition, consumables, service, training, and updates — to secure budget approval and justify the purchase against competing options; an opaque or unpredictable cost profile is a common reason a buyer walks away, so transparent TCO is a procurement gate rather than a Med-tier preference. | Customer | High | KA_14 |
| BR_14 | A compliant software lifecycle with a maintained design history file, and post-market surveillance, vigilance, and complaint-handling capability, shall be provisioned and staffed from launch and sustained for the device's entire market life. | Post-market surveillance and incident reporting are statutory, ongoing legal-manufacturer duties; for AI-driven diagnostic functionality the real-world performance-monitoring load is heavier and must be resourced from day one. | Legal Manufacturer | High | KA_15 |
| BR_15 | The offering shall provide a self-contained safe simulation and training capability enabling operators to build and maintain competence without exposure to live patients or reliance on external simulators. | Built-in safe training reduces onboarding cost, accelerates adoption, and removes clinical risk during competence building for both buyers and users. | Customer | Med | KA_09 |
| BR_16 | The human interface shall be validated for intuitive, rapid, error-tolerant operation under representative emergency conditions, including noise, motion, low light, and operator stress. | Field-robust usability is essential to safe and effective use under stress and to clinical adoption; it must be demonstrated through human-factors validation, not assumed. | Quality | High | KA_08, KA_05 |
| BR_17 | The diagnostic-support output shall present per-candidate rationale and calibrated confidence, and shall notify the operator when it cannot reach a conclusion within an expected time so that fallback to manual assessment is explicit. | Faithful explanation, calibrated confidence, and an explicit no-conclusion notification are required for safe clinical reliance, regulatory transparency, and the manufacturer's residual-risk and liability narrative. | Regulatory | High | KA_04, KA_07 |
| BR_18 | The project shall establish and protect a defensible competitive position for its automated diagnostic-support and integration capabilities, including the intellectual-property and supplier arrangements that secure that differentiation. | The automated diagnostic capability is the core differentiator; sustaining commercial advantage requires deliberate IP and exclusivity decisions taken alongside the validated-component procurement strategy. | Customer | Med | KA_03, KA_16 |
| BR_19 | The offering shall have a defined end-of-life and decommissioning commitment, covering support duration, secure data disposal, and continuity for deployed units at withdrawal. | End-of-life support and secure decommissioning are part of lifecycle cost and statutory data and safety obligations; committing to them late inflates total cost of ownership and workforce-competency exposure. From the buyer's perspective a committed minimum support horizon and an orderly withdrawal/data-disposal plan are contractually decisive: institutional procurement amortises a clinical-device investment over many years and will not commit capital to an offering that may be stranded, so these commitments are routinely written into purchase contracts and gate the deal. | Legal Manufacturer | High | KA_14, KA_10 |
| BR_20 | Safety-relevant signals shall reach valid display within a bounded, characterised power-on-to-readiness time observed at the user-facing boundary, and the system shall thereafter sustain concurrent acquisition of all configured signal sources at a bounded, deterministic measurement-to-display latency, with mandatory power-on self-test and per-source sensor settling completed before any reading is presented as valid. | Fast readiness is decisive in emergencies but is in tension with mandatory self-test and physiological settling, and steady-state operation must additionally guarantee deterministic concurrent multi-source latency; both the startup budget and the steady-state latency must be characterised as boundary-observable budgets so speed never omits integrity checks nor starves a source. | Quality | High | KA_02, KA_01 |
| BR_21 | Every external interface between the offering and an uncontrolled context element (measurement devices, receiving clinical-record and device ecosystems, and any acquired external analysis capability) shall be governed by a controlled, version-managed interface specification defining data, behaviour, and timing, maintained across the lifecycle. | The offering integrates components and ecosystems the manufacturer does not control; without controlled interface specifications, interoperability (BR_08, BR_09), supplier change-control (BR_07), and the boundary latency budgets (BR_05, BR_20) cannot be verified or sustained as the installed base and external components evolve. | Quality | High | KA_11, KA_10, KA_16 |
| BR_22 | A contractually committed support and service-level arrangement shall be offered to buyers, defining guaranteed availability, fault-response and resolution times, spares/replacement provision, and software-update entitlement for a defined minimum term. | Institutional buyers (hospital and EMS procurement) do not buy a clinical-monitoring capability on functional merit alone — they require binding, contractable support commitments to underwrite continuity of care and to satisfy their own clinical-risk and budget-approval governance. A credible SLA with defined response and resolution times is a baseline competitive expectation in this market and is frequently a mandatory tender criterion; its absence is a common showstopper, so the commercial offering must be able to commit to these terms, distinct from the engineering design-in of serviceability. | Customer | High | KA_14 |

## Context (FORMAL)

The context level is the start of the solution domain (DHF), based on the problem domain and the stakeholder expectations.

### Intended Use (IU_01)

Write the intended use as a single, flowing prose statement that naturally covers the five aspects — what the product is, what it does (medical indication), who uses it (user profile), where it is used (use environment), and how it works (operating principle). Do **not** add bold labels or headers for the aspects; weave them into the sentences.

| ID | Description |
|----|-------------|
| IU_01 | The Mobile Monitoring Software Solution (MMSS) is medical device software that transforms an existing portable patient monitor into a clinical decision-support tool for the real-time monitoring of critically ill patients, providing continuous tracking of key vital signs together with AI-driven diagnostic support that presents ranked, real-time diagnostic candidates to inform clinical judgement, with the ranked output stabilising within two minutes of patient connection. The diagnostic output is intended solely as decision support to assist, and not to replace, the clinical assessment and diagnostic decision of a qualified user. It is intended to be used by trained medical professionals in various critical care environments, including intensive care units, emergency rooms, and pre-hospital mobile medical units. The software operates non-invasively by acquiring data from a defined set of measurement devices through standardised interfaces, processing it through an AI analysis engine, presenting vital signs and diagnostic candidates on a connected monitor display, generating clinical alarms for abnormal physiological conditions and sensor faults, and optionally sharing data with hospital information systems to support a second opinion. |

### Medical Device Classification (MD_01)

| ID | Description | Traces |
|----|-------------|--------|
| MD_01 | IEC 62304 software safety classification. The software receives an initial safety class of Class C, since a failure or latent design flaw could lead to inaccurate vital-sign reporting, a missed alarm, or misleading diagnostic support that could contribute to death or serious injury of the patient. The class is reduced to Class B on the basis that an external hardware risk-control measure independent of the MMSS — independent alarm annunciation and independent vital-sign display/diagnosis on the host monitor — limits the residual harm of a software failure to non-serious injury, in accordance with IEC 62304 §4.3. The adequacy and independence of this risk-control measure must be demonstrated in the risk management file (ISO 14971) before the reduced classification can be relied upon. | IU_01 |

### Context Diagram

The context diagram identifies the system of interest in relation to its context. The system of interest contains all elements that are part of the design.

_To be added_

#### Product Information

The Mobile Monitoring Software Solution (MMSS) is a software-only medical device (IEC 62304) that transforms an existing portable patient monitor from a passive vital-signs display into an active clinical decision-support tool. It runs on the monitor's fixed host CPU platform and delivers, in real time, the patient's vital signs together with ranked AI-driven diagnostic candidates, clinical alarms for abnormal physiological conditions and sensor/connection faults, and optional sharing of monitored data and diagnostic findings with a hospital information system for a second opinion. MMSS operates non-invasively by polling a defined set of six non-invasive measurement device types through standardised interfaces, pre-processing and forwarding the acquired data to an external commercially validated AI analysis library (Open Evidence / ALGOS), and rendering the vital signs, diagnostic candidates, and alarms on the connected monitor display, with the ranked diagnostic output converging within two minutes of patient connection. The product comprises five application software items — AC, DAC, DEC, DPREC, and DPROC — and contains no hardware; all physical components are existing, fixed context elements accessed through controlled interface specifications.

#### System of Interest

The part of the broader system this document is about — the product, subsystem, or component you are responsible for designing.

| System Element | Description |
|----------------|-------------|
| AC — Application Controller | The central application and alarm controller of MMSS. Coordinates system activation and the power-on self-test, orchestrates the other software items, evaluates acquired vital signs against safe limits, and generates and presents clinical alarms for abnormal physiological conditions, sensor misplacement, and connection failure. |
| DAC — Device Acquisition Controller | The device-facing acquisition item. Hosts the drivers and polling logic for the six non-invasive measurement device types, acquires raw vital-sign data through the standardised device interfaces, and detects loss of connection (inactivity) and sensor faults reported by the devices. |
| DEC — Diagnostic Engine Connector | The connector to the external AI analysis library (Open Evidence / ALGOS). Submits pre-processed patient data to the AI engine and receives the structured, ranked diagnostic candidates returned by it, within its ≤ 800 ms latency budget. |
| DPREC — Data Pre-processing Component | Pre-processes and conditions the acquired vital-sign data into the form required for AI analysis and for presentation, within its ≤ 800 ms latency budget, before hand-off to DEC and DPROC. |
| DPROC — Data Processing / Presentation Component | Processes vital signs, diagnostic candidates, and alarm content for the user, and renders them to the connected monitor display on the timer-based UI update interval, within its ≤ 200 ms latency budget; also formats data and diagnostic findings for optional sharing with the hospital information system. |

#### Context Elements

Essential elements for your product that are not part of the design.

| Context Element | Description |
|-----------------|-------------|
| Host CPU Platform / RTOS | The existing compact embedded host CPU of the portable monitor, with real-time OS capabilities, on which MMSS executes. Hardware and OS are fixed and out of scope; accessed through published platform services. |
| ECG Monitor | Non-invasive electrocardiograph measurement device providing cardiac electrical activity and heart rate. Existing fixed device accessed via its published interface. |
| Pulse Oximeter | Non-invasive measurement device providing peripheral oxygen saturation and pulse rate. Existing fixed device accessed via its published interface. |
| Blood Pressure (BP) Monitor | Non-invasive (cuff/NIBP) measurement device providing systolic, diastolic, and mean arterial pressure. Existing fixed device accessed via its published interface. |
| Thermal Probe | Non-invasive temperature measurement device providing body temperature. Existing fixed device accessed via its published interface. |
| Capnometer | Non-invasive measurement device providing end-tidal CO₂ and respiration rate. Existing fixed device accessed via its published interface. |
| EEG Monitor | Non-invasive electroencephalograph measurement device providing brain electrical activity. Existing fixed device accessed via its published interface. |
| Monitor Display | The existing connected display of the portable monitor on which MMSS presents vital signs, diagnostic candidates, and alarms. Fixed hardware, out of scope. |
| External AI Analysis Library (Open Evidence / ALGOS) | The commercially validated off-the-shelf AI diagnostic library that receives pre-processed patient data and returns structured, ranked diagnostic candidates, converging within a 2-minute (ALGOS) budget and notifying independently on timeout. Used as-is, out of scope. |
| Hospital Information System (HIS) | The external clinical information system that optionally receives monitored data and diagnostic findings for a second opinion, over a standard healthcare interoperability protocol (HL7/FHIR, TBD). External system, out of scope. |
| Clinician User | The trained medical professional who operates MMSS, observes vital signs, alarms, and diagnostic candidates, and acts on them. End user, not part of the design. |

#### External Interfaces (IF_*)

Connections between the system of interest and the context elements (mechanical, chemical, electronic, digital, logical, etc.).

| ID | Name | Port 1 | Port 2 | ICD |
|----|------|--------|--------|-----|
| IF_01 | Device Acquisition Interface | MMSS (DAC) | Measurement Devices (ECG, Pulse Oximeter, BP Monitor, Thermal Probe, Capnometer, EEG Monitor) | Standardised device ICD per device type (published; defines polling, vital-sign data, and fault/misplacement reporting) |
| IF_02 | Monitor Display Interface | MMSS (DPROC) | Monitor Display | Display/rendering ICD (vital signs, diagnostic candidates, and alarm presentation; timer-based UI update) |
| IF_03 | AI Analysis Library Interface | MMSS (DEC) | External AI Analysis Library (Open Evidence / ALGOS) | AI library ICD (submission of pre-processed patient data; return of structured ranked diagnostic candidates; timeout notification) |
| IF_04 | HIS Integration Interface | MMSS (DPROC) | Hospital Information System (HIS) | Healthcare interoperability ICD — HL7/FHIR (TBD); export of monitored data and diagnostic findings with provenance and timestamp |
| IF_05 | User Interface | MMSS (AC / DPROC) | Clinician User | Human–machine interface ICD (operator inputs/controls; visual and audible alarm and information presentation) |
| IF_06 | Host Platform Interface | MMSS (all items) | Host CPU Platform / RTOS | Platform services ICD (real-time OS scheduling, timing, compute, and platform resource access) |

#### Acquired Parameters / Signals

Whenever the product acquires, exchanges, or presents a **set** of parameters, signals, or data items from a set of source elements (measurement devices, sensors, sub-systems, services), enumerate that set here instead of leaving it as a collective phrase elsewhere. One row per source-element/parameter combination, taken from the input. If no such parameter set applies to this product, write `_Not applicable_`.

| Source Element | Parameter / Signal | Unit / Typical Range | Interface |
|----------------|--------------------|----------------------|-----------|
| ECG Monitor | Heart Rate | bpm; 30–250 bpm | IF_01 |
| ECG Monitor | ECG Waveform (cardiac electrical activity) | mV; ±5 mV (lead-dependent) | IF_01 |
| Pulse Oximeter | Oxygen Saturation (SpO₂) | %; 0–100% | IF_01 |
| Pulse Oximeter | Pulse Rate | bpm; 30–250 bpm | IF_01 |
| BP Monitor | Systolic Pressure (NIBP) | mmHg; 40–260 mmHg | IF_01 |
| BP Monitor | Diastolic Pressure (NIBP) | mmHg; 20–200 mmHg | IF_01 |
| BP Monitor | Mean Arterial Pressure (NIBP) | mmHg; 30–220 mmHg | IF_01 |
| Thermal Probe | Body Temperature | °C; 25–45 °C | IF_01 |
| Capnometer | End-Tidal CO₂ (EtCO₂) | mmHg; 0–100 mmHg | IF_01 |
| Capnometer | Respiration Rate | breaths/min; 0–60 brpm | IF_01 |
| EEG Monitor | EEG Waveform (brain electrical activity) | µV; ±100 µV (typical) | IF_01 |
| Measurement Devices (all) | Sensor Fault / Misplacement Status | Boolean / status code | IF_01 |
| Measurement Devices (all) | Connection / Activity Status (≥ 0.1 Hz input) | Boolean / status; 5 s inactivity → loss | IF_01 |
| External AI Analysis Library (Open Evidence / ALGOS) | Ranked Diagnostic Candidates | Structured list with confidence/ranking | IF_03 |
| External AI Analysis Library (Open Evidence / ALGOS) | Diagnosis Timeout Notification | Status/event; 2-minute (ALGOS) budget | IF_03 |
| Hospital Information System (HIS) | Monitored Vital Signs & Diagnostic Findings (export) | HL7/FHIR (TBD) structured records with provenance/timestamp | IF_04 |

## Users

### User Groups

Collections of users who share common characteristics (a synonym is User Role).

| User | User Group | User Profile |
|------|------------|--------------|
| ICU Critical-Care Nurse | Bedside Clinical User | Registered nurse with critical-care competency who provides continuous bedside care in the intensive care unit. Highly familiar with patient monitors, vital-sign trends and alarm management; sets up monitoring, responds to alarms and interprets the ranked diagnostic candidates as decision support while managing several deteriorating patients. Works long shifts under high cognitive load and frequent interruptions, often wearing gloves and operating the display at arm's length. |
| Emergency Physician | Diagnosing Clinical User | Licensed physician working in the emergency room who is responsible for rapid assessment and diagnostic decisions on undifferentiated, often unstable patients. Time-pressured and multitasking; uses the real-time vital signs and AI-driven diagnostic candidates to inform, not replace, clinical judgement and to seek a second opinion. Comfortable with clinical IT but expects fast, glanceable information and minimal configuration at the point of care. |
| Paramedic / Pre-Hospital EMS Clinician | Mobile Field User | Emergency medical clinician operating in a pre-hospital mobile medical unit such as an ambulance or rapid-response vehicle. Trained in advanced life support and portable monitoring but works in cramped, moving, poorly lit and noisy environments with limited connectivity. Needs to connect the monitor quickly, read information one-handed during transport, and rely on clear alarms while simultaneously delivering hands-on care. |
| Transport / Retrieval Clinician | Inter-Facility Mobile User | Specialist nurse or physician who monitors critically ill patients during inter- and intra-hospital transfer and retrieval. Skilled in critical-care monitoring across handover boundaries; depends on continuous tracking of vital signs, stable diagnostic output and reliable sensor-fault alarms during movement between care settings, and on optional data sharing with the receiving hospital information system for continuity of care. |
| Biomedical / Clinical Engineer (Super-User) | Setup, Configuration & Training User | Biomedical or clinical engineering professional, or designated clinical super-user, responsible for installing and configuring the software on the portable monitor, validating device interfaces, managing connections to hospital information systems, and training clinical staff. Technically proficient with medical-device integration, networking and standardised interfaces; works in a non-time-critical setting but must ensure safe, correct deployment, calibration of interfaces and ongoing user competency. |

### User Requirements / Needs (UR_*)

The user expectations translated over the product context into requirements specific to YOUR product. They are SMARTER than the expectations and form the base for product validation. Format: *As a \<user group\> I want \<feature\> so that \<benefit\>.*

| ID | Description | Classification | Traces |
|----|-------------|----------------|--------|
| UR_01 | As a Bedside Clinical User I want the patient's vital signs (the parameters enumerated in the Acquired Parameters / Signals table) displayed continuously and in real time with bounded, perceptibly lag-free measurement-to-display latency so that I always have current situational awareness of a deteriorating patient. | High | IU_01, BR_20 |
| UR_02 | As a Mobile Field User I want the system to reach valid monitoring readiness for the safety-relevant signal set within a short, bounded power-on time — with self-test and sensor settling completed before any reading is shown as valid — so that I can start monitoring almost immediately in an emergency without acting on unsettled data. | High | IU_01, BR_20 |
| UR_03 | As a Diagnosing Clinical User I want ranked, real-time diagnostic candidates derived from the live multi-parameter data, with the ranking stabilising within two minutes of patient connection, so that I can focus my assessment quickly on the most likely conditions. | High | IU_01, BR_05 |
| UR_04 | As a Diagnosing Clinical User I want each diagnostic candidate presented with a calibrated confidence indication and a faithful per-candidate rationale so that I can judge how much to rely on the decision support and keep the diagnostic decision my own. | High | IU_01, BR_17 |
| UR_05 | As a Bedside Clinical User I want clear, prioritised, unmistakable alarms whenever a monitored vital sign breaches its safe limits, distinguishable from lower-priority information, so that I respond immediately to patient deterioration. | High | IU_01, BR_03, BR_04, BR_16 |
| UR_06 | As a Mobile Field User I want vital-sign alarms to remain reliably detectable — visually and audibly — in noisy, moving, low-light, high-stress conditions so that a genuine emergency is never missed while I am delivering hands-on care. | High | IU_01, BR_16 |
| UR_07 | As an Inter-Facility Mobile User I want a distinct alarm whenever a sensor is disconnected, misplaced, or reporting a fault, with the affected reading explicitly flagged rather than silently dropping out, so that I never act on missing or invalid data during transport. | High | IU_01, BR_03, BR_04, BR_16 |
| UR_08 | As a Bedside Clinical User I want each affected parameter to indicate its own signal-quality or fault state per source so that I can tell a true physiological change apart from a measurement artefact. | High | IU_01, BR_03, BR_04, BR_16 |
| UR_09 | As a Diagnosing Clinical User I want to be explicitly notified when the diagnostic support cannot reach a conclusion within its expected time so that I fall back to manual clinical assessment without waiting on a silent system. | High | IU_01, BR_17 |
| UR_10 | As a Bedside Clinical User I want alarms prioritised so that higher-acuity alarms are presented above lower-priority information and never masked or delayed by it, so that the most critical event always reaches me first without alarm fatigue suppressing a real emergency. | High | IU_01, BR_03, BR_04, BR_16 |
| UR_11 | As a Mobile Field User I want to operate the system rapidly and one-handed through an intuitive, error-tolerant interface so that I can read and act on information at a glance while my hands are occupied with patient care. | High | IU_01, BR_16 |
| UR_12 | As a Diagnosing Clinical User I want glanceable, minimally-configured presentation of vital signs and diagnostic candidates at the point of care so that I obtain the information I need under time pressure without setup overhead. | High | IU_01, BR_16 |
| UR_13 | As a Setup, Configuration & Training User I want a self-contained safe simulation and training mode that reproduces monitoring, alarms, and diagnostic candidates without a live patient so that I can build and maintain staff competence without any patient exposure. | Med | IU_01, BR_15 |
| UR_14 | As an Inter-Facility Mobile User I want to share monitored vital signs and diagnostic findings with the receiving hospital information system through a standard interoperability protocol, preserving each item's provenance and timestamp, so that care continues seamlessly across handover and a second opinion can be sought. | High | IU_01, BR_09 |
| UR_15 | As an Inter-Facility Mobile User I want continuous tracking of vital signs and stable diagnostic output to be sustained without interruption while the patient is moving between care settings so that monitoring continuity is not lost during transfer. | High | IU_01, BR_20 |
| UR_16 | As a Setup, Configuration & Training User I want the software to acquire data from the existing installed base of non-invasive measurement devices through standardised interfaces, tolerating variation across makes, models, and firmware, so that I can deploy it without replacing existing equipment. | High | IU_01, BR_08 |
| UR_17 | As a Bedside Clinical User I want any personal and clinical data the system handles, displays, or shares to be protected in conformity with applicable privacy and information-security obligations so that patient confidentiality and data integrity are preserved throughout use. | High | IU_01, BR_10 |
| UR_18 | As a Diagnosing Clinical User I want the diagnostic output presented unambiguously as decision support that assists and does not replace my clinical judgement so that responsibility for the diagnostic decision remains clearly with me. | High | IU_01, BR_17 |
| UR_19 | As a Setup, Configuration & Training User I want the deployed software to be maintainable and serviceable with a defined update and support cadence so that monitoring availability and operational cost remain predictable across its lifecycle. | High | IU_01, BR_12 |
| UR_20 | As a Bedside Clinical User I want to acknowledge an alarm and temporarily silence it for a bounded, clearly indicated period that re-arms automatically — without permanently disabling or masking the alarm condition — so that I can manage a known intervention without unsafe workarounds and without leaving the patient unmonitored. | High | IU_01, BR_03, BR_04, BR_16 |

### User DFMEA (USER_DFMEA_*)

A structured analysis of how users might misuse, misinterpret, or fail to operate the product, the consequences, and the mitigations the design must include.

| ID | Item/Function | Requirement | Failure Mode | End-effect | Rationale | Failure Cause | Severity | Prevention | Classification | Traces |
|----|---------------|-------------|--------------|------------|-----------|---------------|----------|------------|----------------|--------|
| USER_DFMEA_01 | Diagnostic candidate display | UR_03 | User accepts top-ranked diagnostic candidate as a confirmed diagnosis without independent assessment | Wrong condition treated; correct condition missed; delayed or harmful intervention | Automation bias drives over-reliance on ranked output, especially under time pressure | Ranked list visually resembles a definitive answer; clinician trusts software over own judgement | Critical | Present output as labelled decision support, never a diagnosis; require explicit clinician confirmation; suppress single dominant "answer" framing | High | UR_03 |
| USER_DFMEA_02 | Confidence and rationale display | UR_04 | User ignores or misreads the per-candidate confidence/rationale and treats a low-confidence candidate as reliable | Over-confident action on weak evidence; misdiagnosis | Confidence indication overlooked or misinterpreted as certainty | Confidence rendered subtly; rationale buried or not read under stress | High | Make confidence prominent and calibrated; show rationale inline; visually de-emphasise low-confidence candidates | High | UR_04 |
| USER_DFMEA_03 | Decision-support framing | UR_18 | User defers final diagnostic responsibility to the system rather than retaining clinical ownership | Erosion of clinical accountability; unchallenged automation error reaches the patient | Ambiguous framing lets the user treat support as authority | Output not unambiguously marked as assistive; no forced acknowledgement of clinician ownership | Critical | Persistent "decision support — not a diagnosis" labelling; clinician sign-off step retains ownership | High | UR_18 |
| USER_DFMEA_04 | Vital-sign alarm | UR_05 | User fails to notice or respond to an active high-priority alarm | Patient deterioration unaddressed; possible irreversible harm or death | Alarm not perceived or not acted on in time | Alarm not distinct enough; competing tasks; alarm fatigue desensitisation | Critical | Unmistakable prioritised multi-modal alarms; escalation on non-response; distinct high-priority signature | High | UR_05 |
| USER_DFMEA_05 | Alarm detectability in field | UR_06 | User misses a genuine alarm in noisy, moving, low-light, high-stress conditions | Real emergency undetected during hands-on care | Environmental masking of visual/audible alarm cues | Ambient noise, motion, glare, divided attention overwhelm alarm salience | Critical | Field-robust alarm design (loudness, vibration, high-contrast visual); environment-adaptive cues | High | UR_06 |
| USER_DFMEA_06 | Sensor connection/placement | UR_07 | User places or connects a sensor incorrectly and does not recognise the resulting fault flag | Acts on invalid/missing data or false reassurance from a non-functioning sensor | Misplacement plus failure to attend to the disconnect/fault alarm | Sensor placement not verified; fault flag overlooked; silent dropout assumed normal | Critical | Explicit per-source disconnect/misplacement alarm; affected reading flagged, never silently dropped; placement guidance | High | UR_07 |
| USER_DFMEA_07 | Signal-quality indication | UR_08 | User mistakes a measurement artefact for a true physiological change (or vice versa) | Unnecessary or omitted intervention based on artefact | Per-parameter signal-quality state ignored or absent from attention | Quality indicator not glanceable; artefact visually identical to real change | High | Couple the quality state to the value itself so a degraded reading cannot look identical to a trusted one (e.g. dim/qualify the value, not just a separate icon); make artefact-suspect values self-evident at a glance without the clinician having to inspect a separate indicator | High | UR_08 |
| USER_DFMEA_08 | Stale/invalid reading handling | UR_01 | User acts on a displayed value that is stale, frozen, or no longer current | Clinical decision made on outdated physiology; deterioration missed | User assumes any displayed number is live and valid | No staleness/freshness cue; frozen value indistinguishable from updating value | Critical | Continuous freshness indication; mark stale/invalid values explicitly; bounded measurement-to-display latency | High | UR_01 |
| USER_DFMEA_09 | Monitoring-readiness on power-on | UR_02 | User begins acting on readings before self-test and sensor settling complete | Decisions made on unsettled, not-yet-valid data | Readings shown or assumed valid before readiness reached | No clear "not ready / settling" state; pressure to start immediately | High | Withhold "valid" status until self-test and settling complete; explicit not-ready indication; bounded readiness time | High | UR_02 |
| USER_DFMEA_10 | Diagnosis-timeout notification | UR_09 | User waits indefinitely for a diagnostic conclusion the system cannot reach | Delayed fallback to manual assessment; lost diagnostic time | Silent non-conclusion misread as "still working" | No explicit timeout/inconclusive notification; user assumes pending result | High | Explicit inconclusive/timeout notification within expected time prompting manual fallback | High | UR_09 |
| USER_DFMEA_11 | Alarm prioritisation | UR_10 | User responds to a lower-priority alert while a higher-acuity alarm is masked or delayed | Most critical event reaches clinician too late | Lower-priority information competes with or hides high-acuity alarm | Inadequate prioritisation; high and low alarms not clearly ranked | Critical | Strict alarm prioritisation; high-acuity alarms never masked or delayed by lower-priority info | High | UR_10 |
| USER_DFMEA_12 | Alarm acknowledge/silence | UR_20 | User silences an alarm and the condition is left effectively unmonitored | Active alarm condition persists unnoticed; patient left unmonitored | Silence misused as a permanent dismissal/workaround | Unbounded or unclear silence period; no automatic re-arm; tempting workaround | Critical | Bounded, clearly indicated silence that auto re-arms; cannot permanently disable the alarm condition | High | UR_20 |
| USER_DFMEA_13 | Alarm silencing workaround | UR_20 | User repeatedly silences a recurring alarm to stop the noise rather than addressing the cause | Genuine deterioration masked by habitual silencing | Alarm fatigue drives nuisance-silencing behaviour | Recurrent alarms; easy repeated silence; no escalation on repeated silencing | Critical | Escalate on repeated silencing; log/flag persistent conditions; design to reduce nuisance alarms | High | UR_20 |
| USER_DFMEA_14 | One-handed mobile operation | UR_11 | User makes an unintended input/selection while operating one-handed in motion | Wrong setting changed; alarm dismissed or view altered unintentionally | Mis-touch under motion and divided attention | Small/closely-spaced controls; no error tolerance; motion-induced mis-taps | High | Large, well-spaced, error-tolerant controls; confirm destructive actions; undo for accidental changes | High | UR_11 |
| USER_DFMEA_15 | Glanceable point-of-care display | UR_12 | User misreads a vital sign or candidate at a glance due to cluttered or ambiguous presentation | Action taken on a misread value or condition | Presentation overload or ambiguity under time pressure | Too much information, poor hierarchy, ambiguous units/labels | High | Glanceable, minimally-configured layout; clear hierarchy, units and labels; minimise clutter | High | UR_12 |
| USER_DFMEA_16 | Training/simulation mode | UR_13 | User mistakes simulation/training mode for live monitoring (or live for simulation) | Acts on simulated data as real, or ignores real patient believing it is simulated | Mode confusion between training and live operation | Insufficient mode distinction; mode persists unexpectedly | Critical | Unmistakable, persistent training-mode indication; safe self-contained simulation; clear mode transitions | Med | UR_13 |
| USER_DFMEA_17 | Competence/training gaps | UR_13 | User operates the system without sufficient training and misuses key functions | Mishandled alarms, misread support, incorrect setup in real use | Inadequate familiarity with workflow, alarms, and decision-support limits | Training not completed or not retained; complex functions | High | Self-contained training mode to build/maintain competence; intuitive design lowering training burden | Med | UR_13 |
| USER_DFMEA_18 | HIS handover/share | UR_14 | User shares vital signs and findings to the wrong patient record or receiving facility | Clinical data attached to wrong patient; handover errors | Mis-selection of patient/destination during share | Handover under pressure; weak patient/destination confirmation | Critical | Force positive patient-identity and destination confirmation displaying patient identifiers for the clinician to match before any share completes; preserve provenance/timestamp; block share on identifier mismatch | High | UR_14 |
| USER_DFMEA_19 | Continuity during transfer | UR_15 | User does not notice a monitoring interruption while the patient moves between settings | Gap in vital-sign tracking and diagnostic output goes unnoticed during transfer | Continuity loss not surfaced to the user | No explicit interruption/continuity-loss indication during movement | Critical | Sustain monitoring across transfer; explicit, salient indication of any interruption or continuity loss | High | UR_15 |
| USER_DFMEA_20 | Multi-device data acquisition | UR_16 | User assumes an installed measurement device is connected and acquiring when it is not | Missing parameter unnoticed; false sense of complete monitoring | Device variation/connection state not clearly surfaced | Heterogeneous makes/models/firmware; silent acquisition failure | High | Per-source acquisition/connection status; flag non-acquiring devices; tolerate device variation explicitly | High | UR_16 |
| USER_DFMEA_21 | Privacy of displayed/shared data | UR_17 | User exposes personal/clinical data to bystanders or shares over an unprotected path | Breach of patient confidentiality and data integrity | Privacy obligations not enforced at the point of display/share | Open environments; no protected-sharing default; bystander-visible display | High | Protected sharing by default; privacy-aware display in shared environments; conformant data handling | High | UR_17 |
| USER_DFMEA_22 | Diagnostic candidate display | UR_04 | User dismisses a correct, high-confidence diagnostic candidate because it conflicts with their initial impression | Correct condition discounted; anchored on wrong working diagnosis; delayed correct treatment | Anchoring/confirmation bias leads the clinician to discard valid support that contradicts their first hypothesis | Faithful rationale not surfaced or not read; high-confidence dissenting candidate easy to scroll past under pressure | High | Surface a calibrated, high-confidence candidate and its supporting rationale prominently enough that a contradicting result is hard to overlook, without overriding the clinician's decision | High | UR_04 |

### Use Scenarios

Concrete narratives of how the product is used in the real world, walking from a triggering situation to a successful outcome. Each scenario contains use tasks (UT_*).

#### Scenario 1 — Pre-hospital deployment and startup

A paramedic arrives on scene to an unresponsive patient. Working one-handed beside the patient, they power on MMSS, let it complete self-test and sensor settling, attach the non-invasive sensors, and reach valid monitoring readiness within seconds so they can begin acting on live vital signs without waiting on unsettled data.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_01 | Power on and await readiness | Mobile Field User powers on MMSS in the field and observes the explicit not-ready/settling state while self-test and sensor settling complete, holding off on acting on any reading until "valid" status is shown. | UR_02 |
| UT_02 | Attach non-invasive sensors | User attaches the installed-base non-invasive measurement devices to the patient and confirms each source is acquiring via its per-source connection status. | UR_16 |
| UT_03 | Confirm monitoring readiness | User confirms the safety-relevant signal set has reached valid readiness within the bounded power-on time before relying on any displayed value. | UR_02 |
| UT_04 | Operate one-handed at the patient | User initiates and adjusts monitoring through the intuitive, error-tolerant interface using one hand while the other hand stays on patient care. | UR_11 |

#### Scenario 2 — Multi-parameter monitoring with a deterioration alarm

During transport the patient's condition worsens. MMSS continuously displays the vital-sign set in real time, and when a parameter breaches its safe limit it raises an unmistakable prioritised alarm that the field user perceives despite ambient noise and motion, acknowledges, and acts upon.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_05 | Monitor live vitals | Bedside Clinical User watches the continuously updated vital signs at a glance, relying on bounded, lag-free measurement-to-display latency for current situational awareness. | UR_01 |
| UT_06 | Read freshness of values | User confirms each displayed value is live and current rather than stale or frozen before acting on it. | UR_01 |
| UT_07 | Detect a deterioration alarm | User perceives the prioritised, unmistakable alarm raised when a vital sign breaches its safe limit, distinguishing it from lower-priority information. | UR_05 |
| UT_08 | Perceive alarm in field conditions | Mobile Field User detects the alarm visually and audibly despite noise, motion, low light, and high stress while delivering hands-on care. | UR_06 |
| UT_09 | Acknowledge and silence under control | Bedside Clinical User acknowledges the alarm and temporarily silences it for a bounded, clearly indicated period while performing a known intervention, confirming the silence is time-limited and re-arms automatically so the patient is never left unmonitored. | UR_20 |
| UT_10 | Confirm prioritisation | User confirms higher-acuity alarms are presented above lower-priority information and are never masked or delayed. | UR_10 |
| UT_30 | Confirm response on live vitals | User watches the continuously displayed vital signs after intervening to confirm the breached parameter has returned within safe limits and the alarm condition has cleared, rather than relying on the silence alone. | UR_01 |

#### Scenario 3 — AI diagnostic-candidate review

With multi-parameter data flowing, the diagnosing clinician reviews the ranked, real-time diagnostic candidates that stabilise within two minutes, weighs each candidate's calibrated confidence and rationale, and retains ownership of the diagnostic decision.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_11 | Review ranked candidates | Diagnosing Clinical User reviews the ranked, real-time diagnostic candidates derived from live multi-parameter data once the ranking stabilises within two minutes of connection. | UR_03 |
| UT_12 | Weigh confidence and rationale | User examines each candidate's calibrated confidence indication and faithful per-candidate rationale to judge how far to rely on the support. | UR_04 |
| UT_13 | Retain diagnostic ownership | User treats the output unambiguously as decision support that assists but does not replace clinical judgement, keeping the diagnostic decision their own. | UR_18 |
| UT_14 | Obtain glanceable point-of-care view | User reads vital signs and candidates through a glanceable, minimally-configured presentation without setup overhead under time pressure. | UR_12 |

#### Scenario 4 — Sensor misplacement or disconnection handling

Mid-transport a sensor is jostled loose and another is misplaced. MMSS raises distinct disconnect/fault alarms, flags the affected readings rather than silently dropping them, and indicates per-parameter signal quality so the user can tell artefact from true change and restore valid monitoring.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_15 | Detect sensor disconnect/fault | Inter-Facility Mobile User perceives the distinct alarm when a sensor is disconnected, misplaced, or faulty, with the affected reading explicitly flagged rather than silently dropping out. | UR_07 |
| UT_16 | Distinguish artefact from change | Bedside Clinical User reads the per-source signal-quality/fault state to tell a true physiological change apart from a measurement artefact. | UR_08 |
| UT_17 | Confirm device acquisition status | User checks the per-source acquisition status to confirm each installed device is connected and acquiring, not silently failed. | UR_16 |
| UT_18 | Restore and revalidate the sensor | User re-seats the affected sensor and confirms the reading returns to a valid, fresh state before resuming reliance on it. | UR_01 |

#### Scenario 5 — Diagnosis-timeout fallback

The diagnostic support cannot reach a conclusion for an atypical presentation. Rather than leaving the clinician waiting on a silent system, MMSS explicitly notifies the inconclusive/timeout state within its expected time, prompting a clean fallback to manual clinical assessment.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_19 | Receive inconclusive notification | Diagnosing Clinical User is explicitly notified when the diagnostic support cannot reach a conclusion within its expected time, rather than waiting on a silent system. | UR_09 |
| UT_20 | Fall back to manual assessment | User proceeds to manual clinical assessment on the timeout notification without losing diagnostic time. | UR_09 |
| UT_21 | Continue vital-sign monitoring | User continues to rely on the uninterrupted real-time vital-sign display while performing the manual assessment. | UR_01 |

#### Scenario 6 — Hospital handover and second opinion

On arrival the patient is handed over to the receiving hospital. The inter-facility user shares the monitored vital signs and diagnostic findings into the hospital information system over a standard interoperability protocol, with provenance, timestamps, patient identity, and privacy preserved so care continues seamlessly.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_22 | Maintain continuity into arrival | Inter-Facility Mobile User keeps vital-sign tracking and stable diagnostic output sustained without interruption as the patient moves into the receiving setting, with any continuity loss surfaced. | UR_15 |
| UT_23 | Confirm patient and destination | User positively confirms patient identity and the receiving destination, matching displayed identifiers, before any share completes. | UR_14 |
| UT_24 | Share vitals and findings to HIS | User shares the monitored vital signs and diagnostic findings to the hospital information system via the standard interoperability protocol, preserving each item's provenance and timestamp for handover and second opinion. | UR_14 |
| UT_25 | Protect data during display and share | Bedside Clinical User ensures personal and clinical data is protected in conformity with privacy and information-security obligations throughout display and sharing. | UR_17 |

#### Scenario 7 — Simulation and training session

Between deployments, a trainer runs a self-contained training session. The Setup, Configuration & Training User exercises monitoring, alarms, and diagnostic candidates in a clearly indicated simulation mode that reproduces realistic behaviour without any live patient, building and maintaining staff competence.

| ID | Use Task | Task Description | Traces |
|----|----------|------------------|--------|
| UT_26 | Enter training/simulation mode | Setup, Configuration & Training User enters the self-contained safe simulation mode, confirming the unmistakable, persistent training-mode indication so it is never mistaken for live monitoring. | UR_13 |
| UT_27 | Practise alarms and diagnostics | User exercises monitoring, alarms, and diagnostic-candidate review against simulated data to build and maintain competence without patient exposure. | UR_13 |
| UT_28 | Acquire from installed-base devices | Setup, Configuration & Training User configures acquisition from the existing installed base of non-invasive devices through standardised interfaces, tolerating make/model/firmware variation, so the system deploys without replacing equipment. | UR_16 |
| UT_29 | Confirm serviceability and updates | User confirms the deployed software is maintainable and serviceable on its defined update/support cadence so monitoring availability stays predictable. | UR_19 |

### Usability FMEA (UFMEA_*)

An FMEA focused on usability: where the user interface, workflow, or interaction model can lead to errors, slow operation, or unsafe outcomes.

| ID | Scenario Title | Use Error | Cause | Effect | HF Cause | Rationale | Usability Impact Level | Mitigation (existing) | Mitigation (new) | Classification | Traces |
|----|----------------|-----------|-------|--------|----------|-----------|------------------------|-----------------------|------------------|----------------|--------|
| UFMEA_01 | Scenario 1 — Pre-hospital deployment and startup | User acts on a displayed reading before the system reaches valid readiness | Settling/not-ready state is too subtle or visually similar to live monitoring, so the transition to "valid" is not noticed | Clinical decision made on unsettled, unreliable data in the critical first seconds | Under emergency time pressure the user expects an instrument to be usable the moment its screen lights up and does not wait for a confirmation cue | A faint or ambiguous readiness state invites premature reliance precisely when the user is most rushed and least able to double-check | Critical | Explicit not-ready/settling state held until self-test and sensor settling complete | Full-screen, colour-coded "NOT READY / SETTLING" lockout overlay that visually suppresses numeric values until valid, with a distinct confirming transition to live | High | UT_01, UT_03 |
| UFMEA_02 | Scenario 1 — Pre-hospital deployment and startup | User mistakes an unconnected or not-yet-acquiring sensor for one that is acquiring | Per-source connection status is small, off to the side, or not glanceable while attaching sensors one-handed | A required parameter is silently absent and the patient is monitored on an incomplete signal set | Attention is on the physical sensor and the patient, not on a status indicator, so connection feedback outside the line of sight is missed | One-handed sensor attachment splits attention; status feedback must be co-located with the value or it will not be perceived | High | Per-source connection/acquisition status shown for each device | Each parameter tile shows an unmistakable "no source / acquiring" placeholder state in place of a number until the source is confirmed acquiring | High | UT_02 |
| UFMEA_03 | Scenario 1 — Pre-hospital deployment and startup | User cannot complete startup actions reliably one-handed and triggers an unintended action | Touch targets too small or controls require two-handed or precise multi-step input | Delayed start of monitoring or an accidental mode/setting change at the patient's side | The non-dominant hand and motion reduce pointing precision; controls designed for desk use fail in the field | Field use is inherently one-handed and in motion, so interaction must tolerate imprecise touch without penalising the user | High | Intuitive, error-tolerant one-handed interface | Large, well-spaced primary touch targets with confirm-on-release and forgiving hit areas validated for gloved, one-handed use | High | UT_04 |
| UFMEA_04 | Scenario 2 — Multi-parameter monitoring with a deterioration alarm | User reads a stale or frozen value as if it were live | Freshness/liveness of each value is not visibly indicated, so a frozen number looks identical to a current one | Action taken on out-of-date physiology; deterioration missed or misjudged | Humans assume a displayed number is current unless told otherwise; there is no instinct to question freshness | A frozen value is indistinguishable from a live one without an explicit liveness cue, and the cost of misreading is a missed deterioration | Critical | Bounded measurement-to-display latency with continuously updated values | Per-value freshness indicator (e.g. live timestamp/heartbeat) that visibly degrades and flags the value if updates stop | High | UT_05, UT_06 |
| UFMEA_05 | Scenario 2 — Multi-parameter monitoring with a deterioration alarm | User fails to perceive a deterioration alarm | Alarm not salient enough, or visually/audibly similar to lower-priority information | Patient deterioration goes unnoticed and unaddressed | Under high cognitive load the user's attention narrows; a non-distinct alarm falls below the perceptual threshold | An alarm that competes with routine information for attention will be missed exactly when load is highest | Critical | Prioritised, unmistakable alarm distinct from lower-priority information | Reserve a unique multi-modal alarm signature (colour, motion, tone pattern) used only for safety-limit breaches, never for informational events | High | UT_07 |
| UFMEA_06 | Scenario 2 — Multi-parameter monitoring with a deterioration alarm | User does not detect the alarm in noisy, moving, low-light field conditions | Single-channel (e.g. audio-only) annunciation masked by ambient noise or screen glare | A genuine emergency is missed while the user delivers hands-on care | Sensory channels are saturated by environment; reliance on one channel guarantees occasional non-perception | Field environments defeat any single annunciation channel, so redundant cross-modal signalling is required to stay detectable | Critical | Visually and audibly detectable alarms specified for field conditions | Redundant visual + audible + (where available) tactile annunciation with high-contrast, glare-resistant alarm presentation | High | UT_08 |
| UFMEA_07 | Scenario 2 — Multi-parameter monitoring with a deterioration alarm | User silences an alarm and the patient is left unmonitored | Silence control is mistaken for a permanent disable, or the silence has no clear time limit or re-arm cue | A re-occurring or new breach is not annunciated; patient monitored in a falsely quiet state | Under stress users seek to stop the disturbance; without a visible countdown they assume the problem is handled | Alarm silencing is a known dangerous workaround pattern; a bounded, self-re-arming, clearly indicated silence is essential | Critical | Time-bounded silence that re-arms automatically without disabling the condition | Persistent visible silence countdown timer and "alarm will re-arm" banner; no UI path to permanently disable a safety alarm | High | UT_09 |
| UFMEA_08 | Scenario 2 — Multi-parameter monitoring with a deterioration alarm | A high-acuity alarm is masked or delayed by lower-priority information | Alarm prioritisation not enforced in the presentation layer; concurrent messages compete for the same channel | The most critical event reaches the user late or not at all; alarm fatigue suppresses a real emergency | When multiple signals coincide, an unprioritised display lets noise hide the signal | Prioritisation must be guaranteed at presentation time, because the user cannot triage what they are never shown | Critical | Prioritised alarm scheme; higher-acuity above lower-priority, never masked | Hard priority queue that pre-empts the alarm channel for the highest-acuity event and suppresses lower-priority annunciation during it | High | UT_10 |
| UFMEA_09 | Scenario 2 — Multi-parameter monitoring with a deterioration alarm | User relies on the silence alone and does not confirm the parameter recovered | After intervening, the user treats the quiet system as proof of recovery without re-reading the live value | An unresolved deterioration is assumed resolved | Cessation of an alarm is psychologically read as "fixed"; confirming the value requires deliberate effort | Silence indicates acknowledgement, not recovery; the design must steer the user back to the live value | High | Continuously displayed live vitals after acknowledgement | Post-acknowledgement prompt that highlights the breached parameter and confirms its return within limits before clearing the alarm state | High | UT_30 |
| UFMEA_10 | Scenario 3 — AI diagnostic-candidate review | User reads candidate ranking before it has stabilised | Pre-stabilisation ordering is shown without indicating it is still settling | Assessment anchored on a transient top candidate that the stabilised ranking later displaces | Users anchor on the first-presented ranked item and are reluctant to revise it once seen | Early, volatile rankings create a strong anchoring bias that persists even after the ranking stabilises | High | Ranking stabilises within two minutes of connection | Explicit "ranking settling" state with a stabilised confirmation cue before candidates are presented as decision-ready | High | UT_11 |
| UFMEA_11 | Scenario 3 — AI diagnostic-candidate review | User misreads a candidate's confidence and over- or under-relies on it | Confidence shown as a bare number or ambiguous label without calibration context or rationale link | Mis-calibrated trust: a low-confidence candidate acted on, or a useful one dismissed | Humans poorly interpret probabilistic confidence and tend to over-trust automation | A confidence figure without calibrated framing and rationale invites systematic mis-reliance | High | Calibrated confidence indication with faithful per-candidate rationale | Confidence shown with a calibrated visual scale tied directly to the candidate's rationale, with explicit low-confidence flagging | High | UT_12 |
| UFMEA_12 | Scenario 3 — AI diagnostic-candidate review | User defers the diagnostic decision to the system rather than retaining ownership | Output framed or styled as a conclusion rather than as decision support | Automation complacency; clinician's independent judgement is bypassed | Authoritative-looking output and time pressure encourage deference to the machine | The decision-support boundary must be enforced in presentation, or responsibility silently shifts to the system | Critical | Output presented unambiguously as decision support, not replacement | Persistent "decision support — clinician decides" framing; candidates presented as assistive list, never as a single declared diagnosis | High | UT_13 |
| UFMEA_13 | Scenario 3 — AI diagnostic-candidate review | User loses time configuring or hunting for information under pressure | View requires setup or the point-of-care layout is cluttered and not glanceable | Delayed assessment at the moment speed matters most | Time pressure collapses tolerance for configuration; any setup overhead is a usability failure | A point-of-care view that demands configuration fails the very situation it exists for | High | Glanceable, minimally-configured point-of-care presentation | Zero-configuration default layout co-locating vitals and top candidates in a fixed, glanceable arrangement | High | UT_14 |
| UFMEA_14 | Scenario 4 — Sensor misplacement or disconnection handling | User does not notice a sensor disconnect/fault and acts on a dropped reading | Disconnect alarm not distinct from limit alarms, or the affected reading is not explicitly flagged | Decision made on missing or invalid data during transport | A dropout looks like a benign value change; without a distinct cue the user cannot tell loss from reading | Silent dropout is more dangerous than an out-of-range value because nothing signals that data is gone | Critical | Distinct disconnect/fault alarm with the affected reading explicitly flagged | Distinct disconnect alarm signature plus an unmistakable "signal lost" overlay replacing the affected value | High | UT_15 |
| UFMEA_15 | Scenario 4 — Sensor misplacement or disconnection handling | User mistakes a measurement artefact for a true physiological change | Per-source signal-quality/fault state not shown alongside the value | Unnecessary or wrong intervention driven by an artefact | Without a quality cue the user has no basis to discount a noisy value and treats it as real | Distinguishing artefact from change is impossible without an explicit per-source quality indication | High | Per-source signal-quality/fault state indication | Inline signal-quality indicator on each parameter tile that visibly degrades and flags low-quality or suspect values | High | UT_16 |
| UFMEA_16 | Scenario 4 — Sensor misplacement or disconnection handling | User believes a silently failed device is still acquiring | Per-source acquisition status not surfaced, so a stopped source looks active | Monitoring continues on a source that is no longer providing data | Absence of a value is not noticed unless absence itself is annunciated | Confirming acquisition requires positive per-source status, since "no update" reads as "no change" | High | Per-source acquisition status display | Always-visible per-source acquisition state with an explicit "not acquiring" indication when a device stops | High | UT_17 |
| UFMEA_17 | Scenario 5 — Diagnosis-timeout fallback | User waits indefinitely on a silently inconclusive diagnostic system | Inconclusive/timeout state not explicitly notified; absence of output read as "still working" | Diagnostic time lost while the user waits for a conclusion that will not come | Humans tolerate silence from a "thinking" system far longer than is safe, assuming progress | A silent system cannot be distinguished from a slow one; the inconclusive state must be actively declared | High | Explicit inconclusive/timeout notification within expected time | Explicit timed "inconclusive — proceed to manual assessment" notification that replaces any pending/working indication | High | UT_19, UT_20 |
| UFMEA_18 | Scenario 6 — Hospital handover and second opinion | User shares vitals and findings against the wrong patient or destination | Identity and destination confirmation step is skippable, weak, or shows ambiguous identifiers | Clinical data attached to the wrong record; handover continuity and privacy compromised | During a rushed handover, confirmation steps are reflexively dismissed without reading | Wrong-patient association is a high-severity error; identity confirmation must be explicit and matched, not assumed | Critical | Positive patient/destination confirmation before any share completes | Mandatory match-and-confirm step displaying patient identity and destination side-by-side, blocking share until explicitly confirmed | High | UT_23, UT_24 |
| UFMEA_19 | Scenario 6 — Hospital handover and second opinion | User does not notice a loss of monitoring/diagnostic continuity during transfer | Continuity loss not surfaced; the display appears unchanged while tracking has actually paused | Gap in vital-sign tracking goes unnoticed across the care-setting transition | A static-looking display is assumed to be a working one; interruptions are invisible without a cue | Continuity loss during a transfer is exactly when attention is divided, so the loss must announce itself | High | Continuity sustained without interruption, with continuity loss surfaced | Persistent continuity status banner that prominently flags any interruption and the affected interval rather than failing silently | High | UT_22 |
| UFMEA_20 | Scenario 7 — Simulation and training session | User mistakes simulation mode for live monitoring (or vice versa) | Training-mode indication too subtle or not persistent across all screens | Simulated data trusted as a real patient, or a real patient treated as a drill | Mode is easily forgotten once set; without a persistent cue the user reverts to the default "this is real" assumption | Mode confusion between simulation and live is a classic, high-consequence use error and demands an unmissable persistent indication | Critical | Self-contained simulation mode with unmistakable persistent training indication | Persistent full-border "TRAINING / SIMULATION" watermark on every screen plus a distinct chrome colour, with a deliberate guarded entry/exit | Med | UT_26, UT_27 |
| UFMEA_21 | Scenario 2 — Multi-parameter monitoring with a deterioration alarm | User acknowledges/silences the wrong alarm when several are active at once and dismisses a high-acuity alarm | A single shared acknowledge/silence control acts on the most recent or selected alarm without making clear which alarm is being silenced | A genuine high-acuity deterioration alarm is silenced in error while the user intends to clear a lower-priority or nuisance alarm; the critical condition is left unannunciated | Under load the user reflexively presses "silence" to stop the noise without reading which of several concurrent alarms is targeted | Concurrent multi-parameter alarms are routine in deteriorating patients; an acknowledge action that does not name its target is a well-known cause of silencing the wrong, more critical alarm | Critical | Time-bounded silence that re-arms automatically without disabling the condition | Acknowledge acts only on an explicitly identified alarm, naming the parameter and priority being silenced and requiring confirmation before silencing the highest-acuity active alarm | High | UT_07, UT_09 |

### Usability Requirements (USR_*)

Measurable requirements for how the product must perform from a user perspective: task completion times, error rates, learnability, accessibility. Validated through usability testing.

| ID | Requirement | Classification | Traces |
|----|-------------|----------------|--------|
| USR_01 | At least 90% of trained users complete power-on to confirmed valid monitoring readiness for the safety-relevant signal set within 30 s in the field, and 0 users act on any reading while the not-ready/settling state is shown (zero premature-reliance use errors observed). | High | UR_02, UFMEA_01 |
| USR_02 | In summative testing, 100% of users correctly distinguish the "not ready / settling" state from live monitoring and withhold action until the "valid" transition is shown; ≤2 s mean time to recognise the transition to valid. | High | UR_02, UFMEA_01 |
| USR_03 | When attaching sensors one-handed, ≥95% of users correctly identify, within 3 s per source, whether each source is acquiring versus not-acquiring, with 0 instances of an unconnected/not-acquiring source being mistaken for an acquiring one. | High | UR_16, UFMEA_02, UFMEA_16 |
| USR_04 | All primary touch targets are ≥12 mm with ≥3 mm spacing and operable one-handed with gloves; trained users complete startup interactions with an unintended-action (mis-tap) rate ≤1% across summative trials, and every destructive action is reversible or confirmed. | High | UR_11, UFMEA_03 |
| USR_05 | Each displayed value carries a continuously visible freshness/liveness cue; ≥95% of users correctly identify a stale or frozen value within 3 s of update cessation, with 0 instances of a frozen value acted on as live. | High | UR_01, UFMEA_04 |
| USR_06 | A high-priority deterioration alarm is detected and correctly identified as high-priority by ≥99% of users within 10 s of onset under representative load, and is reliably distinguished from lower-priority information (≤1% misclassification). | High | UR_05, UFMEA_05 |
| USR_07 | Under field conditions (ambient noise up to the specified field level, motion, low light and glare), ≥99% of users detect a high-priority alarm within 10 s; alarm annunciation is redundant across at least two sensory channels (visual plus audible, tactile where available). | High | UR_06, UFMEA_06 |
| USR_08 | A silenced safety alarm always displays a visible silence countdown and re-arm indication; ≥95% of users correctly report that the alarm is temporarily silenced (not disabled) and will re-arm, and there exists no UI path by which a user can permanently disable a safety-alarm condition (0 such paths). | High | UR_20, UFMEA_07 |
| USR_09 | When two or more alarms are active concurrently, the highest-acuity alarm is presented first and is never masked or delayed; ≥99% of users respond to the highest-acuity alarm before any lower-priority one, and the acknowledge action correctly names the parameter and priority being silenced with ≤1% wrong-alarm silencing. | High | UR_10, UFMEA_08, UFMEA_21 |
| USR_10 | After acknowledging and silencing an alarm and intervening, ≥90% of users re-read and confirm the breached parameter has returned within limits before clearing the alarm state, prompted by the post-acknowledgement confirmation step. | High | UR_01, UFMEA_09 |
| USR_11 | Diagnostic candidates are presented as decision-ready only after the ranking has stabilised; the pre-stabilisation "settling" state is correctly recognised by ≥95% of users, with 0 instances of a user acting on a transient pre-stabilised top candidate. | High | UR_03, UFMEA_10 |
| USR_12 | ≥90% of users correctly interpret each candidate's calibrated confidence level (high vs low) and locate its rationale within 5 s; low-confidence candidates are explicitly flagged and acted on inappropriately in ≤5% of trials. | High | UR_04, UFMEA_11 |
| USR_13 | The diagnostic output is unambiguously framed as decision support; in summative testing ≥95% of users correctly state that the clinician (not the system) owns the diagnostic decision, and the system never presents a single declared diagnosis (0 occurrences). | High | UR_18, UFMEA_12 |
| USR_14 | The point-of-care view requires zero configuration to read vital signs and top diagnostic candidates; ≥90% of users locate a requested vital sign or top candidate within 3 s with no setup steps, and SUS learnability score ≥80. | High | UR_12, UFMEA_13 |
| USR_15 | A sensor disconnect/fault is identified as distinct from a limit alarm by ≥99% of users within 10 s, with the affected reading replaced by an unmistakable "signal lost" indication; 0 instances of a dropped reading acted on as a valid value. | High | UR_07, UFMEA_14 |
| USR_16 | Each parameter carries an inline per-source signal-quality indicator; ≥90% of users correctly distinguish an artefact/low-quality value from a true physiological change within 5 s, with ≤5% artefact-as-real misinterpretation. | High | UR_08, UFMEA_15 |
| USR_17 | The inconclusive/timeout state is actively notified within the diagnostic support's expected time; ≥95% of users recognise it and initiate manual fallback within 10 s of notification, with 0 users left waiting indefinitely on a silent system. | High | UR_09, UFMEA_17 |
| USR_18 | Before any share completes, a mandatory match-and-confirm step displays patient identity and destination side-by-side; the wrong-patient or wrong-destination share rate is 0% in summative testing and the step cannot be skipped. | High | UR_14, UFMEA_18 |
| USR_19 | Any loss of monitoring/diagnostic continuity during transfer is surfaced by a persistent status banner; ≥95% of users notice the continuity-loss indication within 10 s of onset, with 0 interruptions going unnoticed. | High | UR_15, UFMEA_19 |
| USR_20 | A persistent training/simulation indication appears on every screen; 100% of users correctly identify whether the system is in simulation or live mode at any point in a session, with 0 mode-confusion errors, and mode entry/exit requires a deliberate guarded action. | Med | UR_13, UFMEA_20 |

## Concept

### UI/UX Design

Wireframes, interaction flows, navigation structures, and visual design principles that translate the user requirements into a tangible concept.

This section translates the User Requirements (UR_*) and the measurable Usability Requirements (USR_*) into a tangible interface concept for MMSS (Mobile Multi-parameter Safety & Support). It is organised as: (1) screen map and navigation, (2) the main monitoring screen with wireframes, (3) key interaction flows tied to the Use Scenarios, and (4) the visual design principles that govern the whole interface. Design choices reference the USR/UR they satisfy.

#### 1. Navigation structure and screen map

MMSS is a glanceable, point-of-care, mostly single-screen application. The Live Monitoring screen is the persistent "home"; the user almost never has to leave it. All other surfaces are shallow overlays or peers reachable in one action, so that no required information is ever more than one tap deep (supports the zero-configuration, glanceable intent of UR_12 / USR_14).

```
                         ┌──────────────────────────────┐
                         │   STARTUP / READINESS (S0)    │  self-test + sensor settling
                         │   "NOT READY / SETTLING"      │  (UR_02, USR_01/02)
                         └───────────────┬──────────────┘
                                         │ valid transition
                                         ▼
   ┌─────────────────────────────────────────────────────────────────────────┐
   │                      LIVE MONITORING  (S1 — HOME)                         │
   │   vitals tiles · diagnostic-candidate panel · alarm zone · status bar    │
   └───┬───────────┬──────────────┬───────────────┬───────────────┬──────────┘
       │           │              │               │               │
       ▼           ▼              ▼               ▼               ▼
 ┌──────────┐ ┌──────────┐ ┌─────────────┐ ┌─────────────┐ ┌──────────────┐
 │ ALARM    │ │ CANDIDATE│ │ SENSOR /    │ │ HANDOVER /  │ │ SOURCES &    │
 │ DETAIL & │ │ DETAIL   │ │ SOURCE      │ │ SHARE (S5)  │ │ SETTINGS(S6) │
 │ SILENCE  │ │ (S3):    │ │ STATUS (S4) │ │ match-and-  │ │ device list, │
 │ (S2):    │ │ confidence│ │ per-source  │ │ confirm     │ │ service,     │
 │ ack, bounded│ rationale,│ │ acquire/    │ │ identity +  │ │ update       │
 │ silence  │ │ settling │ │ quality/    │ │ destination │ │ cadence      │
 │ (UR_20)  │ │ (UR_03/04)│ │ fault(UR_07)│ │ (UR_14/17)  │ │ (UR_16/19)   │
 └──────────┘ └──────────┘ └─────────────┘ └─────────────┘ └──────────────┘

   SIMULATION / TRAINING MODE (S7) is not a separate screen but a persistent
   mode applied across S0–S6 (full-border watermark + distinct chrome colour).
   Guarded entry/exit only. (UR_13, USR_20)
```

Screen inventory:

| ID | Screen | Purpose | Primary UR/USR |
|----|--------|---------|----------------|
| S0 | Startup / Readiness | Self-test, sensor settling, not-ready lockout until valid | UR_02, USR_01, USR_02 |
| S1 | Live Monitoring (Home) | Continuous vitals, candidates, alarm zone, status bar | UR_01, UR_12, USR_05, USR_14 |
| S2 | Alarm Detail & Silence | Identify, acknowledge, bounded silence, post-ack confirm | UR_05, UR_10, UR_20, USR_06/08/09/10 |
| S3 | Candidate Detail | Confidence, rationale, decision-support framing, timeout | UR_03/04/09/18, USR_11/12/13/17 |
| S4 | Sensor / Source Status | Per-source acquire, signal-quality, fault, disconnect | UR_07/08/16, USR_03/15/16 |
| S5 | Handover / Share | Match-and-confirm identity + destination, protected share | UR_14/17, USR_18 |
| S6 | Sources & Settings | Device acquisition config, serviceability, update cadence | UR_16/19 |
| S7 | Simulation / Training | Persistent mode overlay across all screens | UR_13, USR_20 |

#### 2. Main monitoring screen (S1) — wireframe

The home screen is divided into four fixed, zero-configuration zones. Layout is identical every session so users build muscle memory and locate any vital or top candidate within 3 s with no setup (USR_14). The alarm zone has top visual priority; the candidate panel is deliberately framed as assistive and subordinate to the vitals.

```
┌──────────────────────────────────────────────────────────────────────────────┐
│ ⬤ LIVE    Pt: J. DOE 04F  ●REC  12:04:11   [≡ Sources]   [⇄ Handover]  ░TRAIN░ │ ← Status bar
├──────────────────────────────────────────────────────────────────────────────┤
│ ███████  ALARM ZONE  — HIGH ▸ SpO₂ 84%  LOW LIMIT  ⏱ tap to ACK / SILENCE ███ │ ← Alarm banner
│         (empty / quiet when no active alarm; reserves the space always)        │   (UR_05/10, USR_06/09)
├───────────────────────────────────────────┬────────────────────────────────────┤
│  VITALS TILES  (fixed grid)               │  DIAGNOSTIC CANDIDATES             │
│                                           │  ── Decision support · you decide ─│
│  ┌───────────────┐ ┌───────────────┐      │  (UR_18, USR_13)                   │
│  │ HR        ⟿live│ │ SpO₂     ⚠LOW │      │                                    │
│  │   72          │ │   84  ▼       │      │  1 ▓▓▓▓▓░ HIGH  Hypoxaemia        │
│  │ bpm   ◷ now    │ │ %  ◷ now  ◐QC │      │     why ▸ SpO₂↓ + RR↑  [open]     │
│  └───────────────┘ └───────────────┘      │                                    │
│  ┌───────────────┐ ┌───────────────┐      │  2 ▓▓▓░░░ MED   Sepsis (early)    │
│  │ RR        ⟿live│ │ NIBP     ⟿live│      │     why ▸ HR↑ Temp↑    [open]     │
│  │   24  ▲       │ │ 118/76        │      │                                    │
│  │ /min  ◷ now    │ │ mmHg ◷ 0:30   │      │  3 ░░░░░░ LOW⚑  Anxiety          │
│  └───────────────┘ └───────────────┘      │     low confidence — flagged      │
│  ┌───────────────┐ ┌───────────────┐      │                                    │
│  │ Temp      ⟿live│ │ EtCO₂  ▦NO SRC│      │  ⏳ ranking settling… (0:48)       │
│  │  38.1         │ │  -- signal    │      │  └ shown only until stabilised     │
│  │ °C    ◷ now    │ │     lost ▦    │      │  (UR_03, USR_11)                  │
│  └───────────────┘ └───────────────┘      │                                    │
│                                           │                                    │
├───────────────────────────────────────────┴────────────────────────────────────┤
│ STATUS: 5/6 sources acquiring · EtCO₂ NO SOURCE · continuity OK · ◷ all live    │ ← Source/continuity bar
└──────────────────────────────────────────────────────────────────────────────┘
```

Tile anatomy (each vitals tile carries its own state, so a degraded value can never look identical to a trusted one — supports UR_08, USR_05, USR_16):

```
┌─────────────────────────┐
│ HR              ⟿ live   │  ← liveness/freshness cue (animated). Degrades to "◷ stale 0:14"
│      72                  │     then a flashing "STALE" flag if updates stop (USR_05).
│ bpm     ◷ now   ◐QC      │  ← ◷ age-of-value · ◐QC inline per-source signal-quality
│ ▁▂▃▅▃▂  trend            │     ring that dims/qualifies the value when quality drops (USR_16).
└─────────────────────────┘
Fault/disconnect states REPLACE the number, never blank it silently:
   ⚠ LOW  (limit breach)      ▦ NO SRC / SIGNAL LOST (UR_07, USR_15)
   ◐ ARTEFACT? (low quality)  ▒ SETTLING (not yet valid, UR_02)
```

#### 3. Key interaction flows (tied to Use Scenarios)

**3.1 Startup → monitoring (Scenario 1 · UT_01–04 · USR_01/02/03/04).** Power on → S0 shows a full-screen colour-coded "NOT READY / SETTLING" lockout that visually suppresses all numeric values while self-test and per-sensor settling run. Each source attached one-handed shows an unmistakable per-source "acquiring / no source" placeholder (USR_03). Only when the safety-relevant set is valid does a distinct confirming transition unlock S1 to live; no number can be read as valid before this (USR_01/02). All startup controls are ≥12 mm, ≥3 mm spaced, confirm-on-release for gloved one-handed use (USR_04).

```
[POWER ON] → S0 NOT READY ──(attach sensors, per-source "acquiring…")──▶
   self-test ✔ + settling ✔  ─── distinct "VALID — LIVE" transition ───▶ S1 LIVE
```

**3.2 Alarm acknowledge / silence (Scenario 2 · UT_07–10, UT_30 · USR_06/07/08/09/10).** A safety-limit breach fires the reserved multi-modal alarm signature (unique colour + motion + tone pattern, redundant across visual/audible/tactile for field detectability, USR_06/07). The alarm banner names the parameter and priority. Tapping opens S2. When several alarms are concurrent, the highest-acuity is presented first and the acknowledge action explicitly names the parameter + priority it will silence, requiring confirmation before silencing the highest-acuity alarm (prevents wrong-alarm silencing, USR_09). Silence is bounded with a visible countdown and "will re-arm" banner; there is no UI path to permanently disable a safety alarm (USR_08). After intervention, a post-acknowledgement prompt highlights the breached parameter and asks the user to confirm it has returned within limits before the alarm state clears (USR_10, UT_30).

```
BREACH ▸ multi-modal alarm ─▶ banner "HIGH ▸ SpO₂ LOW"
   tap ▸ S2 ── ACK (names target) ── confirm ── SILENCE 2:00 ⏱ (re-arms)
                                                    │
                          post-ack ▸ "Confirm SpO₂ back in limits?" ── clear
```

**3.3 Candidate review (Scenario 3 · UT_11–14 · USR_11/12/13).** While ranking is unstable, the panel shows an explicit "ranking settling…" state and withholds decision-ready presentation (USR_11). Once stabilised, candidates appear as a ranked *list* — never a single declared diagnosis — under a persistent "Decision support · you decide" header (USR_13). Each candidate carries a calibrated confidence bar; low-confidence candidates are visually de-emphasised and flagged (⚑). "why ▸" expands the faithful per-candidate rationale inline (S3) so confidence and rationale are read together (USR_12). High-confidence dissenting candidates are surfaced prominently enough to resist anchoring/confirmation bias without overriding the clinician.

**3.4 Sensor-fault handling (Scenario 4 · UT_15–18 · USR_03/15/16).** A disconnect/fault fires a *distinct* signature (different from limit alarms) and the affected value is replaced by an unmistakable "▦ SIGNAL LOST" overlay, never silently dropped (USR_15). The inline ◐QC ring degrades and marks artefact-suspect values so artefact vs. true change is glanceable (USR_16). S4 shows always-visible per-source acquisition state with an explicit "not acquiring" indication; on re-seating, the tile returns to live + fresh before reliance resumes (UT_18).

**3.5 Diagnosis-timeout (Scenario 5 · UT_19–21 · USR_17).** If the support cannot conclude within its expected time, any "working…" indication is *replaced* by an explicit, timed "Inconclusive — proceed to manual assessment" notice (never a silent pending state), prompting clean manual fallback while vitals keep streaming (USR_17).

**3.6 Handover / share (Scenario 6 · UT_22–25 · USR_18/19).** A persistent continuity-status banner flags any interruption and the affected interval during transfer (USR_19). Sharing to the HIS opens S5, a mandatory non-skippable match-and-confirm step that displays patient identity and destination side-by-side; the share is blocked until the clinician explicitly matches and confirms (0% wrong-patient/destination target, USR_18). Provenance, timestamps, and protected transport are preserved (UR_14/17).

**3.7 Simulation / training mode (Scenario 7 · UT_26–27 · USR_20).** Training mode applies a persistent full-border "TRAINING / SIMULATION" watermark and a distinct chrome colour to every screen, with deliberate guarded entry/exit, so live and simulated states are never confused (USR_20).

#### 4. Visual design principles

- **Glanceability & fixed layout (UR_12, USR_14):** zero-configuration default; vitals and top candidates occupy fixed positions every session. Large numerals, strong figure/ground contrast, minimal chrome; any required item readable in ≤3 s without navigation.
- **Alarm colour & priority coding (UR_05/10, USR_06/09):** a strict, reserved priority palette — High (red, urgent motion + tone pattern), Medium (amber), Low/info (cyan), Normal (neutral). The high-priority signature is reserved exclusively for safety-limit breaches and never reused for informational events. A hard priority queue guarantees the highest-acuity alarm is presented first and never masked.
- **Legibility, sizing & one-handed/high-stress use (UR_11, USR_04/07):** primary touch targets ≥12 mm with ≥3 mm spacing, confirm-on-release, forgiving hit areas, validated gloved one-handed; destructive actions reversible or confirmed. Redundant cross-modal annunciation (visual + audible + tactile) with high-contrast, glare- and motion-resistant presentation for the field.
- **Freshness & data-validity honesty (UR_01/08, USR_05/16):** every value carries a continuous liveness cue and an inline per-source quality state; stale, settling, artefact, and signal-lost states are visually distinct from a trusted live value and, where degraded, qualify the value itself rather than only a separate icon.
- **Decision-support framing — never autonomous (UR_04/18, USR_11/12/13):** diagnostic output is always a ranked list of candidates with calibrated confidence and faithful rationale, under persistent "decision support · clinician decides" framing. The system never declares a single diagnosis, never auto-acts, and de-emphasises/flags low-confidence candidates; inconclusive states are actively declared, never silent.
- **Mode clarity (UR_13, USR_20):** simulation vs. live is unmistakable and persistent on every screen, with guarded transitions, eliminating mode-confusion use errors.

### Actors

Individuals, groups, or systems that perform roles or tasks within the system or process.

| Actor | Description |
|-------|-------------|
| Bedside Clinical User | ICU critical-care nurse who sets up monitoring, observes continuous vital signs and trends, responds to alarms, and interprets ranked diagnostic candidates as decision support at the bedside. |
| Diagnosing Clinical User | Emergency physician who uses real-time vital signs and ranked diagnostic candidates with their confidence and rationale to inform rapid diagnostic decisions, and who triggers an optional second-opinion export. |
| Mobile Field User | Paramedic / pre-hospital EMS clinician who connects the monitor quickly, starts monitoring in an emergency, and reads information and alarms one-handed in a moving, noisy, low-light field environment. |
| Inter-Facility Mobile User | Transport / retrieval clinician who maintains continuous monitoring and reliable sensor-fault alarms across patient transfer, and manages optional data sharing with the receiving facility. |
| Biomedical / Clinical Engineer (Super-User) | Biomedical/clinical engineer or designated super-user who installs and configures MMSS, validates device interfaces, manages HIS connectivity, and trains clinical staff. |
| Measurement Device | Any of the six non-invasive measurement devices (ECG monitor, pulse oximeter, BP/NIBP monitor, thermal probe, capnometer, EEG monitor) that supplies vital-sign data and fault/misplacement status to MMSS over the Device Acquisition Interface (IF_01). |
| Monitor Display | The portable monitor's display on which MMSS renders vital signs, diagnostic candidates, and alarms over the Monitor Display Interface (IF_02). |
| External AI Analysis Library (Open Evidence / ALGOS) | The off-the-shelf AI diagnostic library that receives pre-processed patient data and returns structured ranked diagnostic candidates, or a timeout notification, over the AI Analysis Library Interface (IF_03). |
| Hospital Information System (HIS) | The external clinical information system that optionally receives exported monitored data and diagnostic findings for a second opinion and continuity of care over the HIS Integration Interface (IF_04). |
| Host CPU Platform / RTOS | The embedded host platform and real-time OS that provides scheduling, timing, compute, and resource services on which MMSS executes, over the Host Platform Interface (IF_06). |

### Use Cases (UC_*)

_To be added_

| ID | Title | Actor | Goal | Satisfies | Classification | Precondition | Main Success Scenario | Alternative Scenarios | Exception Scenarios | Post Condition | Traces |
|----|-------|-------|------|-----------|----------------|--------------|-----------------------|-----------------------|---------------------|----------------|--------|
| UC_01 | Power on and reach valid monitoring readiness | Mobile Field User | Bring MMSS from power-off to confirmed valid monitoring readiness for the safety-relevant signal set within the bounded power-on time, without acting on unsettled data. | UR_02 | High | Device powered off; sensors available to attach; user at the patient in the field. | User powers on MMSS; the explicit "NOT READY / SETTLING" lockout is shown while self-test and per-sensor settling run; numeric values are suppressed; on completion a distinct "VALID — LIVE" transition unlocks live monitoring within the bounded time. | If sensors are still settling, individual parameters remain marked "settling" and become valid as each source settles, rather than blocking the whole set. | Self-test fails — system holds the not-ready lockout, annunciates the fault, and does not present any value as valid; readiness time exceeded — explicit readiness-timeout indication shown rather than a silent wait. | System is in a confirmed valid live-monitoring state, or is explicitly held not-ready; no value was acted on while not valid. | UR_02, UT_01, UT_03 |
| UC_02 | Attach sensors and confirm acquisition | Mobile Field User | Attach the installed-base non-invasive devices and confirm each source is connected and actively acquiring before relying on its readings. | UR_16 | High | MMSS powered on; Measurement Devices available; user operating one-handed at the patient. | User attaches each Measurement Device; MMSS shows a per-source "acquiring" status for every connected device; each parameter tile transitions from "no source / acquiring" placeholder to a live value once its source is confirmed acquiring. | A device of a different make/model/firmware is attached — MMSS tolerates the variation and still reports its per-source acquisition state. | A connected device fails to acquire silently — the tile holds the "not acquiring / no source" indication rather than showing a number; an unsupported device is rejected with an explicit unsupported-source notice. | All intended sources are confirmed acquiring, or any non-acquiring source is explicitly flagged. | UR_16, UT_02, UT_17 |
| UC_03 | Acquire and display vital signs in real time | Bedside Clinical User | Continuously observe the live vital-sign set at a glance with bounded, perceptibly lag-free measurement-to-display latency. | UR_01 | High | Monitoring valid; at least the safety-relevant sources acquiring; Live Monitoring screen active. | MMSS continuously updates each vital-sign tile in real time from the acquiring Measurement Devices; each value carries a continuous freshness/liveness cue; the user reads current values within the bounded latency. | A source temporarily degrades — its value is qualified with an inline signal-quality state while remaining displayed. | Value updates stop — the freshness cue degrades to "stale" and then an explicit stale flag, so the frozen value is never read as live. | The user has current, freshness-cued situational awareness of the patient's vital signs. | UR_01, UT_05, UT_06 |
| UC_04 | Detect and annunciate a vital-sign alarm | Bedside Clinical User | Be reliably alerted, with a prioritised unmistakable alarm, whenever a monitored vital sign breaches its safe limit. | UR_05 | High | Live monitoring active; safe limits configured for the monitored parameters. | A monitored vital sign breaches its safe limit; MMSS fires the reserved high-priority multi-modal alarm signature (colour, motion, tone), naming the parameter and priority in the alarm banner, distinct from lower-priority information; the user perceives and responds. | Multiple alarms active concurrently — the hard priority queue presents the highest-acuity alarm first and never masks or delays it behind lower-priority information. | Alarm not perceived in time — escalation on non-response raises salience until acknowledged. | The breach is annunciated as a prioritised, unmistakable alarm and reaches the user. | UR_05, UT_07, UT_10 |
| UC_05 | Detect alarm in adverse field conditions | Mobile Field User | Perceive a genuine high-priority alarm despite noise, motion, low light, and high-stress hands-on care. | UR_06 | High | Live monitoring active in a field/transport environment; user delivering hands-on care. | A safety-limit breach fires; MMSS annunciates redundantly across at least two sensory channels (visual plus audible, tactile where available) with high-contrast, glare- and motion-resistant presentation; the field user detects the alarm. | Ambient audio masked — the visual and tactile channels remain detectable independently of the audible channel. | A single channel is unavailable (e.g. no tactile hardware) — annunciation falls back to the remaining redundant channels without losing detectability. | The alarm is detected under field conditions and a genuine emergency is not missed. | UR_06, UT_08 |
| UC_06 | Acknowledge and bounded-silence an alarm | Bedside Clinical User | Acknowledge an alarm and temporarily silence it for a bounded, clearly indicated period that re-arms automatically, without disabling or masking the condition. | UR_20 | High | An alarm is active; the user is about to perform a known intervention. | User opens the alarm detail; MMSS names the parameter and priority to be silenced; user confirms; the alarm is silenced for a bounded period with a visible countdown and "will re-arm" banner; it re-arms automatically on expiry. | Several alarms active — the acknowledge action explicitly identifies which alarm it silences and requires confirmation before silencing the highest-acuity alarm, preventing wrong-alarm silencing. | User attempts to permanently disable a safety alarm — no UI path permits it; repeated nuisance-silencing of a recurring condition triggers escalation rather than continued silence. | The alarm is temporarily silenced and guaranteed to re-arm; the condition is never permanently masked. | UR_20, UT_09 |
| UC_07 | Confirm recovery after intervention | Bedside Clinical User | Confirm the breached parameter has returned within safe limits on the live values rather than relying on the silence alone. | UR_01 | High | An alarm has been acknowledged/silenced and an intervention performed. | After acknowledgement, MMSS highlights the breached parameter with a post-acknowledgement prompt; the user re-reads the continuously displayed live value and confirms it has returned within limits before the alarm state is cleared. | Parameter has not yet recovered — the alarm state is not cleared and the prompt persists. | The breach recurs during the silence window — the alarm re-arms and re-annunciates rather than staying silent; the breached parameter's source loses signal during the confirmation window — recovery cannot be confirmed, the prompt persists with a "signal lost — recovery unconfirmed" indication, and the alarm state is not silently cleared. | Recovery is confirmed on live data before the alarm state clears, or the alarm remains active. | UR_01, UT_30 |
| UC_08 | Detect and annunciate a sensor fault, disconnection, or misplacement | Inter-Facility Mobile User | Be distinctly alerted whenever a sensor is disconnected, misplaced, or faulty, with the affected reading explicitly flagged rather than silently dropped. | UR_07 | High | Monitoring active during transport; one or more Measurement Devices attached. | A sensor disconnects, is misplaced, or reports a fault; MMSS fires a distinct disconnect/fault signature (different from a limit alarm) and replaces the affected value with an unmistakable "SIGNAL LOST" overlay; the user is alerted and the reading is never silently dropped. | User re-seats the affected sensor — the tile returns to a valid, fresh value before reliance resumes. | Intermittent dropout — each loss is flagged distinctly rather than averaged into an apparently valid value. | The fault/disconnect is distinctly annunciated and the affected reading is explicitly flagged. | UR_07, UT_15, UT_18 |
| UC_09 | Distinguish artefact from true physiological change | Bedside Clinical User | Tell a measurement artefact apart from a genuine physiological change using a per-source signal-quality state. | UR_08 | High | Live monitoring active; per-source signal-quality indication available on each tile. | Each parameter tile shows an inline per-source signal-quality state that visibly degrades and qualifies the value itself when quality drops; the user uses the cue to discount an artefact and act only on trusted readings. | Quality recovers — the qualification clears and the value returns to a trusted presentation. | Sustained low quality — the value is flagged "artefact?" so it cannot be read as a confirmed change. | The user can reliably distinguish artefact from true change at a glance. | UR_08, UT_16 |
| UC_10 | Request and present AI diagnostic candidates | Diagnosing Clinical User | Obtain ranked, real-time diagnostic candidates with calibrated confidence and faithful rationale, presented as decision support, with the ranking stabilising within two minutes. | UR_03 | High | Valid multi-parameter data flowing; External AI Analysis Library reachable over IF_03. | MMSS sends pre-processed patient data to the External AI Analysis Library and receives structured ranked candidates; while ranking is unstable a "ranking settling" state is shown; once stabilised (within two minutes) candidates appear as a ranked list under persistent "decision support · you decide" framing, each with a calibrated confidence bar and inline rationale. | A high-confidence candidate contradicts the clinician's initial impression — it is surfaced prominently to resist anchoring without overriding the clinician's decision. | Low-confidence candidates are explicitly de-emphasised and flagged; the library returns malformed output — MMSS withholds decision-ready presentation rather than showing unreliable candidates. | Ranked, confidence- and rationale-bearing decision support is presented; the diagnostic decision remains the clinician's. | UR_03, UT_11, UT_12, UT_13 |
| UC_11 | Handle inconclusive diagnosis or timeout | Diagnosing Clinical User | Be explicitly notified when the diagnostic support cannot conclude within its expected time, so as to fall back to manual assessment without waiting on a silent system. | UR_09 | High | A diagnostic request is in progress; AI Analysis Library expected to return within its time bound. | The diagnostic support cannot reach a conclusion within its expected time; MMSS replaces any "working" indication with an explicit, timed "Inconclusive — proceed to manual assessment" notification; the user falls back to manual clinical assessment while vitals keep streaming. | Partial low-confidence output returned past the bound — it is presented as inconclusive rather than as decision-ready candidates. | The AI Analysis Library is unreachable over IF_03 — MMSS declares the inconclusive/unavailable state explicitly instead of a silent pending state. | The inconclusive/timeout state is actively declared and the user fell back to manual assessment without lost time. | UR_09, UT_19, UT_20, UT_21 |
| UC_12 | Maintain continuity and share data to the HIS | Inter-Facility Mobile User | Share monitored vital signs and diagnostic findings to the receiving HIS with provenance, timestamp, identity, and privacy preserved, while sustaining monitoring continuity across transfer. | UR_14 | High | Patient being transferred; monitoring sustained; Hospital Information System reachable over IF_04. | Monitoring continuity is sustained as the patient moves, with any continuity loss surfaced by a persistent banner; the user opens handover, completes a mandatory match-and-confirm step displaying patient identity and destination side-by-side, and shares the data and findings to the HIS over the standard interoperability protocol with provenance, timestamps, and protected transport preserved. | A second opinion is sought — the same shared, provenance-tagged dataset supports it. | Identity/destination mismatch — the share is blocked until explicitly matched and confirmed (no wrong-patient share); HIS unreachable — the share is deferred and the failure surfaced rather than silently dropped; continuity interrupted during transfer — the interruption and affected interval are flagged. | Data and findings are shared to the correct HIS record with provenance and privacy preserved, and continuity loss (if any) is surfaced. | UR_14, UT_22, UT_23, UT_24, UT_25 |
| UC_13 | Run a simulation/training session | Biomedical / Clinical Engineer (Super-User) | Exercise monitoring, alarms, and diagnostic candidates in a self-contained safe simulation mode that is never mistaken for live monitoring. | UR_13 | Med | No live patient connected; user authorised to enter training mode. | User enters the self-contained simulation/training mode through a deliberate guarded action; a persistent full-border "TRAINING / SIMULATION" watermark and distinct chrome colour appear on every screen; the user practises monitoring, alarms, and diagnostic-candidate review against simulated data without patient exposure; exit is via a guarded action back to live. | Trainee practises alarm acknowledge/silence and candidate review using simulated events identical in behaviour to live ones. | User attempts an ambiguous mode transition — entry/exit is guarded and the persistent indication prevents confusing simulation with live; a live patient is connected while in simulation — the mode-confusion guard surfaces the conflict. | A training session is completed safely with no possibility of simulated data being mistaken for live monitoring. | UR_13, UT_26, UT_27 |
| UC_14 | Manage acquisition sources, serviceability, and settings | Biomedical / Clinical Engineer (Super-User) | Configure acquisition from the installed-base devices through standardised interfaces and maintain the software on its defined update/support cadence to keep monitoring availability predictable. | UR_16 | High | MMSS deployed; super-user authorised; Measurement Devices and Host CPU Platform / RTOS available. | The super-user configures acquisition from the existing installed base of non-invasive devices through standardised interfaces, tolerating make/model/firmware variation, and confirms the deployed software is maintainable and serviceable on its defined update and support cadence. | A new device make/model is added — it is configured through the standardised interface without replacing existing equipment. | A device variant is incompatible — it is explicitly rejected with guidance rather than silently failing; a software update is pending — availability impact is made predictable per the update cadence. | Acquisition sources are configured and the software is serviceable, with monitoring availability and cost predictable across the lifecycle. | UR_16, UR_19, UT_28, UT_29 |
| UC_15 | Operate the monitor one-handed at the patient | Mobile Field User | Read and act on monitoring information — including acknowledging an alarm and adjusting the view — rapidly and one-handed through an error-tolerant interface while the other hand stays on patient care. | UR_11 | High | MMSS in valid live monitoring; user delivering hands-on care in motion, one hand occupied. | User operates MMSS with one hand at a glance: large, well-spaced touch targets and confirm-on-release let the user read values, acknowledge an alarm, and switch view without diverting attention from the patient or requiring precise two-handed input. | User wears gloves or operates in motion/vibration — forgiving hit areas and confirm-on-release keep interaction reliable without re-attempts. | A mis-tap targets a destructive action (e.g. silencing an alarm or changing a setting) — the action is confirmed or reversible (undo), so no alarm is dismissed and no setting is changed unintentionally; the screen is occluded or wet — primary actions remain operable or degrade safely rather than triggering an unintended change. | The user reads and acts on monitoring information reliably one-handed, with no unintended or unrecoverable action. | UR_11, UT_04 |

### Design Decisions (DD_*)

Choices made during design, with the considered alternatives and the rationale for the final choice.

| ID | Decision | Alternatives | Rationale | Traces |
|----|----------|--------------|-----------|--------|
| DD_01 | Realise the diagnostic-support capability by integrating a commercially validated off-the-shelf AI analysis library (Open Evidence / ALGOS) for v1, rather than developing a bespoke diagnostic model. | (a) Train and validate a proprietary in-house diagnostic model; (b) integrate a qualified, change-controlled off-the-shelf analysis library; (c) defer automated diagnosis entirely and ship vital-signs monitoring only. | A validated off-the-shelf library brings characterised diagnostic performance, documented provenance, and change-control evidence, sharply reducing first-party validation load and protecting the clinical/commercial window; a bespoke model would multiply the evidence and post-market-monitoring burden for the same v1 value claim, and dropping diagnosis removes the core differentiator. The library is consumed as an external component across a controlled interface so the manufacturer still owns the integrated behaviour and its boundary timing. | UC_10, UC_11, BR_06 |
| DD_02 | Scope the product as software-only, hosted on the existing portable monitor's fixed host CPU platform, with no MMSS-supplied hardware. | (a) Software-only on the incumbent host platform; (b) ship a dedicated MMSS hardware appliance/box alongside the software; (c) require a specified replacement monitor. | Software-only on the installed host preserves the customer's hardware capital, avoids a hardware regulatory and manufacturing burden, and is the fastest defensible route to market; bundling or mandating hardware inflates cost of ownership and switching cost and would be rejected on procurement grounds. All physical components are treated as fixed context elements accessed through controlled interface specifications. | UC_14, BR_08, BR_13 |
| DD_03 | Assume a deterministic real-time-capable execution environment (RTOS / real-time scheduling on the host CPU platform) as a design constraint for the acquisition and display path. | (a) Best-effort general-purpose OS scheduling; (b) deterministic real-time OS / real-time scheduling discipline; (c) dedicated co-processor for time-critical paths. | Bounded power-on-to-readiness and deterministic concurrent measurement-to-display latency cannot be guaranteed on best-effort scheduling under multi-source load; a real-time execution discipline is the lowest-cost way to make the boundary latency budgets verifiable, whereas a co-processor reintroduces hardware scope the product deliberately excludes (DD_02). | UC_01, UC_03, BR_20 |
| DD_04 | Architect the safety function (safe-limit alarming and vital-sign display) on a path independent of the diagnostic-support path, sharing no common computing, power, timing, or data-path dependency. | (a) Single shared path for monitoring, alarming, and diagnosis; (b) logically separated tasks on shared infrastructure; (c) a genuinely independent alarm-and-display path with no shared single point of failure with diagnosis. | The Class C→B reduction depends on a protective measure demonstrably independent of the diagnostic capability; mere logical separation on shared computing, power, or timing leaves latent coupling that defeats the independence claim and would force the higher classification. A dependency-level-independent alarm/display path is the design realisation that lets the residual-harm argument hold. | UC_04, UC_05, UC_08, BR_04 |
| DD_05 | Acquire from the heterogeneous installed base of non-invasive measurement devices exclusively through standardised device-acquisition interfaces governed by controlled interface specifications (ICDs), one per source type. | (a) Per-device bespoke drivers maintained ad hoc; (b) standardised acquisition interfaces governed by versioned ICDs; (c) certify against a single mandated device make/model. | Versioned ICDs let the product tolerate make/model/firmware variation across the installed base and verify interoperability as that base evolves, without replacing existing equipment; ad-hoc drivers erode under firmware drift, and mandating one device make destroys the installed-base value proposition. The ICD is also the contractual anchor for handling non-conformant device behaviour. | UC_02, UC_14, BR_08 |
| DD_06 | Treat the safety-relevant display path and the external diagnostic-convergence path as two separately budgeted timing domains: a bounded deterministic measurement-to-display latency owned internally, and a ranked-output convergence budget (≤ two minutes) observed at the system boundary that includes the external library's contribution. | (a) One combined end-to-end latency budget spanning acquisition through diagnosis; (b) separate display-latency and diagnostic-convergence budgets; (c) no explicit diagnostic-time budget, present whenever ready. | The display path must be deterministic and perceptibly lag-free regardless of the diagnostic path, while the diagnostic convergence runs partly in an external component whose timing the system can only own at its boundary; collapsing both into one budget would make neither verifiable. Separate budgets let the fast display path stay deterministic and let the two-minute convergence be characterised as a boundary-observable budget. | UC_03, UC_10, BR_05, BR_20 |
| DD_07 | Integrate with hospital information systems through a standard healthcare interoperability protocol (HL7 v2 / FHIR — final selection TBD), exporting vitals and diagnostic findings with provenance, timestamp, and patient identity preserved. | (a) Proprietary export format/API; (b) standard healthcare interoperability protocol (HL7/FHIR); (c) manual export (file/print) only. | Standards-based exchange into the receiving record is a clinical-continuity necessity and a procurement gate; a proprietary or manual path is a workflow blocker and undermines trust in exported findings. Preserving provenance, timestamp, and identity per exported item lets the receiving system interpret and trust the data; the HL7-vs-FHIR choice is deferred to the interface-specification stage but the standards-based commitment is fixed now. | UC_12, BR_09, BR_21 |
| DD_08 | Provide a self-contained simulation/training mode entirely within the product, with no reliance on external simulators or live patients, and an unmistakable persistent mode indication. | (a) Train only against live patients/clinical exposure; (b) integrate a third-party external simulator; (c) a built-in self-contained simulation/training mode. | Built-in safe simulation removes clinical risk during competence building and onboarding cost, and avoids a dependency on external simulator availability; the decisive design constraint is that simulated data must never be mistaken for live, so the mode carries a persistent full-screen indication and guarded entry/exit transitions. | UC_13, BR_15 |
| DD_09 | Detect sensor disconnection, misplacement, and fault per source and qualify the affected reading with a distinct signature, never silently dropping or averaging it into an apparently valid value. | (a) Suppress/blank a faulted reading silently; (b) substitute a last-good or interpolated value; (c) flag each affected reading distinctly with a dedicated fault/disconnect signature separate from limit alarms. | A silently dropped or interpolated reading can be misread as valid physiology, which is a safety hazard; a dedicated disconnect/fault signature distinct from a safe-limit alarm tells the user the data — not the patient — is at fault, supporting artefact-versus-true-change discrimination and the hazard-control argument. Per-source detection lets a single faulted source be isolated without degrading the rest. | UC_08, UC_09, BR_03, BR_16 |
| DD_10 | Make the diagnostic output explicitly declare an inconclusive/timeout state when the external analysis cannot conclude within its expected time or is unreachable, rather than holding a silent "working" state. | (a) Wait silently until the library responds; (b) show stale/partial candidates past the time bound; (c) actively declare a timed "inconclusive — proceed to manual assessment" state. | A silent pending state costs the clinician time in an emergency and erodes trust; an explicit, timed no-conclusion notification makes the fallback to manual assessment deliberate and keeps vitals streaming, and is required for the residual-risk and transparency narrative around the external diagnostic component. | UC_11, BR_17, BR_05 |
| DD_11 | Frame diagnostic candidates permanently as decision support, presenting each with calibrated confidence and faithful per-candidate rationale and never as an automated decision or override. | (a) Present a single top diagnosis as an answer; (b) present a ranked list as raw output without confidence/rationale; (c) present a ranked list under persistent "decision support · you decide" framing with calibrated confidence and inline rationale. | Calibrated confidence and faithful rationale are required for safe clinical reliance, regulatory transparency, and the liability narrative; presenting a single answer or unexplained ranking invites automation bias and over-trust. Persistent decision-support framing keeps the diagnostic decision with the qualified clinician, consistent with the intended use. | UC_10, BR_17 |
| DD_12 | Protect personal and clinical data in transit and at rest, and enforce a mandatory patient-identity match-and-confirm step before any HIS share, with protected transport and per-item provenance. | (a) Best-effort handling with transport security only; (b) protected transport plus encryption at rest plus a mandatory identity match-and-confirm gate before share; (c) defer data-protection controls to deployment configuration. | Identifiable patient data carries statutory privacy and security duties whose breach blocks deployment; encryption in transit and at rest is the baseline, and a mandatory match-and-confirm gate before share is the design control against wrong-patient disclosure during handover. Deferring these to configuration leaves the obligation unmet by default. | UC_12, BR_10, BR_21 |
| DD_13 | Design the human interface for reliable one-handed, error-tolerant operation under representative field stress, using large well-spaced targets, confirm-on-release, and reversible/guarded destructive actions. | (a) Standard touch UI tuned for two-handed bench use; (b) field-hardened one-handed UI with forgiving hit areas, confirm-on-release, and undo on destructive actions; (c) hardware-button-only control. | Operators act one-handed under noise, motion, low light, and stress while the other hand stays on patient care; a bench-tuned UI produces mis-taps that could silence an alarm or change a setting, and hardware-only control conflicts with the software-only scope (DD_02). Forgiving targets with confirm-on-release and reversible destructive actions make interaction reliable without unintended or unrecoverable actions. | UC_06, UC_15, BR_16 |
| DD_14 | Design the software for maintainability and serviceability on a defined update/support cadence, with predictable, communicated availability impact for updates. | (a) Ad-hoc patching with no committed cadence; (b) a defined, version-controlled update/support cadence with predictable availability impact; (c) immutable firmware with no field update path. | Serviceability and a committed update cadence must be designed in up front or total cost of ownership and availability commitments silently erode; ad-hoc patching makes availability unpredictable, and an immutable no-update design cannot sustain security and post-market corrective actions across the device's market life. A predictable cadence keeps clinical/EMS availability and lifecycle cost defensible. | UC_14, BR_12, BR_14 |

---

# Development

## SOLUTION: MMSS (Mobile Monitoring Software Solution)

### External Interfaces

The points where the system connects to context elements, sub-systems, or other systems — connection type, data/signals exchanged, and protocols/standards.

Treated as a black box at its external boundary, the MMSS exposes six external connection points. At its **input edge** it acquires vital-sign data and device-health status from a heterogeneous set of measurement devices over a digital acquisition interface; at its **output edges** it renders monitoring and diagnostic information to a display, presents controls and alarms to the clinician, submits pre-processed patient data to an external AI analysis service and receives ranked diagnostic candidates back, and exports monitored data and findings to the hospital record system. It is hosted on, and consumes real-time scheduling and compute services from, an underlying host platform. The MMSS does not reach into any device, library, or system beyond these contracted boundary connections; every exchange crosses one of the interfaces below and is governed by the corresponding ICD.

| Boundary Connection | IF | Direction (w.r.t. MMSS) | Connection Type | Data / Signals Exchanged | Protocol / Standard |
|---------------------|----|--------------------------|-----------------|--------------------------|---------------------|
| Measurement devices (ECG, Pulse Oximeter, BP, Thermal Probe, Capnometer, EEG) | IF_01 | Inbound | Digital device-acquisition link (polled) | Vital-sign parameters and waveforms; sensor fault/misplacement status; connection/activity status | Standardised per-device-type ICD |
| Monitor display | IF_02 | Outbound | Digital display/rendering link (timer-driven) | Vital signs, ranked diagnostic candidates, alarm/visual presentation | Display/rendering ICD |
| External AI analysis library (Open Evidence / ALGOS) | IF_03 | Bidirectional | Digital service request/response | Submitted pre-processed patient data (out); structured ranked diagnostic candidates and timeout notification (in) | AI library ICD |
| Hospital Information System (HIS) | IF_04 | Outbound | Digital interoperability link | Exported monitored vital signs and diagnostic findings with provenance and timestamp | HL7 / FHIR (TBD) |
| Clinician user | IF_05 | Bidirectional | Human–machine interface | Operator inputs/controls (in); visual and audible information and alarms (out) | Human–machine interface ICD |
| Host CPU platform / RTOS | IF_06 | Bidirectional | Platform services binding | Real-time scheduling, timing, compute and resource access requests/grants | Platform services ICD (RTOS) |

_To be added_

### Requirements

The full set of requirements the system must satisfy, derived from the user requirements and constrained by the context, regulatory requirements, and design decisions. Requirements are SMART and form the basis for verification.

#### Interface Requirements (RQ_IF_*)

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_IF_01 | The MMSS shall acquire vital-sign parameters and waveforms from each connected measurement device (ECG, Pulse Oximeter, BP Monitor, Thermal Probe, Capnometer, EEG Monitor) over the device-acquisition interface in conformance with the published per-device-type ICD. | Defines the standardised contract by which the system ingests all monitored physiological data, ensuring interoperability across the supported device set. | Functional / Interface | IF_01 |
| RQ_IF_02 | The MMSS shall acquire each device's sensor fault / misplacement status over the device-acquisition interface as a Boolean or status code per the device ICD. | Acquired device-health status is required at the boundary so the system can detect and surface unreliable or misapplied sensors. | Functional / Interface | IF_01 |
| RQ_IF_03 | The MMSS shall treat a measurement device as disconnected when no valid input (≥ 0.1 Hz) is received from it over the device-acquisition interface for 5 consecutive seconds. | A defined, boundary-observable inactivity criterion ensures consistent loss-of-signal detection across all device types. | Functional / Interface | IF_01 |
| RQ_IF_04 | The MMSS shall present, over the monitor-display interface, the acquired vital signs, the ranked diagnostic candidates, and alarm/visual indications in conformance with the display/rendering ICD. | Establishes the output contract by which monitored and diagnostic information is rendered to the clinician's display. | Functional / Interface | IF_02 |
| RQ_IF_05 | The MMSS shall refresh the monitor-display interface on a timer-driven cycle as defined by the display/rendering ICD. | A deterministic, timer-based update keeps the displayed clinical picture current and predictable. | Functional / Interface | IF_02 |
| RQ_IF_06 | The MMSS shall submit pre-processed patient data to the external AI analysis library over the AI analysis interface in the structure defined by the AI library ICD. | Defines the request side of the diagnostic-support contract with the external AI service. | Functional / Interface | IF_03 |
| RQ_IF_07 | The MMSS shall receive structured ranked diagnostic candidates from the external AI analysis library over the AI analysis interface in the format defined by the AI library ICD. | Defines the response side of the AI contract so returned candidates can be presented and recorded. | Functional / Interface | IF_03 |
| RQ_IF_08 | The MMSS shall, upon receiving a diagnosis timeout notification (or detecting absence of a response past the ICD-defined deadline) from the external AI analysis library over the AI analysis interface, transition the diagnostic-support output to the explicit inconclusive state while leaving vital-sign acquisition unaffected. | A boundary-observable timeout signal — actioned by a defined output-state transition rather than an unspecified "act upon" — lets the system degrade gracefully when the external service does not respond. The MMSS must not rely solely on the library emitting a timeout message; it must also bound the wait itself (deadline-from-request), since an unresponsive off-the-shelf component may never send the notification. | Functional / Interface | IF_03 |
| RQ_IF_09 | The MMSS shall export monitored vital signs and diagnostic findings to the Hospital Information System over the HIS integration interface, each record carrying provenance and a timestamp. | Ensures monitored data and findings reach the patient record with the attribution and timing needed for clinical and audit use. | Functional / Interface | IF_04 |
| RQ_IF_10 | The MMSS shall format all data exported over the HIS integration interface in conformance with the applicable healthcare interoperability standard (HL7 / FHIR, TBD) as defined by the HIS ICD. | Standards-conformant export is required for the receiving hospital system to ingest the data reliably. | Functional / Interface | IF_04 |
| RQ_IF_11 | The MMSS shall accept clinician operator inputs and control actions over the user interface in conformance with the human–machine interface ICD. | Defines the input side of the clinician boundary so the operator can control and configure monitoring. | Functional / Interface | IF_05 |
| RQ_IF_12 | The MMSS shall present visual and audible information and alarm indications to the clinician over the user interface in conformance with the human–machine interface ICD. | Defines the output side of the clinician boundary so monitored status and alarms are perceivable. | Functional / Interface | IF_05 |
| RQ_IF_13 | The MMSS shall distinguish visual from audible alarm indications presented over the user interface such that an alarm condition is conveyed through both modalities per the human–machine interface ICD. | Multi-modal alarm presentation at the boundary reduces the risk of a missed alarm. | Functional / Interface | IF_05 |
| RQ_IF_14 | The MMSS shall obtain real-time scheduling, timing, compute, and resource services from the host platform over the host-platform interface as defined by the platform services (RTOS) ICD. | Defines the dependency contract on the underlying platform that enables the system's real-time behaviour. | Functional / Interface | IF_06 |

#### Functional Requirements (RQ_FN_*)

What the system must do — its functions, features, and behaviors. Each traces back to a use case or user requirement.

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_FN_01 | The MMSS shall, on power-on, execute a startup self-test of its monitoring functions and hold an explicit "NOT READY / SETTLING" state in which no acquired value is presented as valid, until self-test and per-sensor settling for the safety-relevant signal set have completed. | Acting on unsettled or unverified data in an emergency is a safety hazard; an explicit not-ready lockout prevents reliance on any value before validated readiness. | High | UC_01, UR_02 |
| RQ_FN_02 | The MMSS shall transition from the not-ready state to a distinct "VALID — LIVE" monitoring state, unlocking live presentation, only once self-test passes and the safety-relevant signal set has settled. | A clear, distinct readiness transition lets the user know precisely when displayed values may be relied upon. | High | UC_01, UR_02 |
| RQ_FN_03 | The MMSS shall, on self-test failure or when the bounded readiness time is exceeded, remain in the not-ready state, annunciate the fault or readiness-timeout explicitly, and present no value as valid. | A silent failure to reach readiness could be mistaken for a working system; explicit annunciation forces a deliberate response. | High | UC_01, UR_02 |
| RQ_FN_04 | The MMSS shall acquire data by polling each connected measurement device of the six supported types (ECG, Pulse Oximeter, BP Monitor, Thermal Probe, Capnometer, EEG Monitor) and present a per-source connection/acquisition status for every device. | Continuous polling with explicit per-source status ensures the user can confirm each installed device is actually acquiring and not silently failed. | High | UC_02, UR_16 |
| RQ_FN_05 | The MMSS shall tolerate variation in make, model, and firmware across connected measurement devices, reporting each source's acquisition state, and shall explicitly reject and annunciate an unsupported device rather than failing silently. | The product must deploy onto the heterogeneous installed base without replacing equipment, and an unsupported source must be visible rather than appearing absent. | High | UC_02, UR_16 |
| RQ_FN_06 | The MMSS shall continuously display the acquired vital-sign set in real time, updating each parameter tile from its acquiring source within the bounded measurement-to-display latency. | Continuous, lag-free real-time display is the core of situational awareness for a deteriorating patient. | High | UC_03, UR_01 |
| RQ_FN_07 | The MMSS shall present, for each displayed vital-sign value, a continuous freshness/liveness indication and shall mark a value explicitly as "stale" when its source stops updating, so a frozen value is never read as live. | A frozen value indistinguishable from a live one leads to decisions on outdated physiology; explicit freshness indication prevents this. | High | UC_03, UR_01 |
| RQ_FN_08 | The MMSS shall detect when a monitored vital sign breaches its configured safe limit and annunciate a reserved high-priority, multi-modal (visual and audible) alarm that names the breached parameter and its priority and is distinct from lower-priority information. | Unmistakable, prioritised annunciation of a limit breach is the primary mechanism by which the user is alerted to deterioration. | High | UC_04, UR_05 |
| RQ_FN_09 | The MMSS shall annunciate high-priority alarms redundantly across at least two sensory channels (visual plus audible, and tactile where available) with high-contrast, glare- and motion-resistant presentation, such that an alarm remains detectable when any single channel is masked or unavailable. | Field, transport, and high-stress conditions can mask a single channel; redundant multi-channel annunciation keeps a genuine emergency detectable. | High | UC_05, UR_06 |
| RQ_FN_10 | The MMSS shall present concurrently active alarms in strict priority order such that the highest-acuity alarm is presented first and is never masked or delayed by lower-priority information. | Alarm prioritisation ensures the most critical event reaches the clinician first and is not hidden by less urgent alerts. | High | UC_04, UR_10 |
| RQ_FN_11 | The MMSS shall allow the user to acknowledge an active alarm and silence it for a bounded, clearly indicated period with a visible countdown, after which the alarm re-arms automatically, and shall provide no path to permanently disable or mask the underlying alarm condition. | Bounded, auto-re-arming silence lets the user manage a known intervention without ever leaving the patient unmonitored. | High | UC_06, UR_20 |
| RQ_FN_12 | The MMSS shall, when an acknowledge/silence action is requested while multiple alarms are active, explicitly identify the alarm being silenced and require confirmation before silencing the highest-acuity alarm, and shall escalate rather than continue to silence a repeatedly nuisance-silenced recurring condition. | Wrong-alarm silencing and habitual nuisance-silencing both mask real deterioration; explicit targeting and escalation prevent this. | High | UC_06, UR_20 |
| RQ_FN_13 | The MMSS shall, following an alarm acknowledgement, prompt the user to confirm recovery on the live value of the breached parameter and shall not clear the alarm state until the value is confirmed within safe limits or the alarm remains active. | Clearing an alarm on the silence alone risks an uncorrected breach; confirmation on live data ties clearance to actual recovery. | High | UC_07, UR_01 |
| RQ_FN_14 | The MMSS shall detect, per source, a sensor fault, disconnection, or misplacement and annunciate a distinct fault/disconnect signature, different from a safe-limit alarm, while replacing the affected reading with an unmistakable flag rather than silently dropping or substituting it. | A silently dropped or interpolated reading can be misread as valid physiology; a distinct fault signature tells the user the data, not the patient, is at fault. | High | UC_08, UR_07 |
| RQ_FN_15 | The MMSS shall present, for each parameter, an inline per-source signal-quality state that visibly qualifies the value itself when quality degrades, so that an artefact-suspect value cannot be read as a confirmed physiological change. | Coupling signal quality to the value lets the clinician distinguish a measurement artefact from a true change at a glance. | High | UC_09, UR_08 |
| RQ_FN_16 | The MMSS shall treat a measurement device as inactive/disconnected and raise the disconnect indication when no valid input is received from it for the defined inactivity interval. | A defined connection-inactivity criterion ensures consistent, boundary-observable loss-of-signal detection across all device types. | High | UC_08, UR_07 |
| RQ_FN_17 | The MMSS shall request diagnostic analysis from the external AI analysis service using the live multi-parameter data and present the returned diagnostic candidates as a ranked list, reflecting the external service's convergence signal (ranking-stable) at the boundary rather than mandating the convergence time within the MMSS. | Ranked, real-time candidates let the clinician focus quickly on the most likely conditions during the diagnostic window. The 2-minute convergence is an external ALGOS budget (see RQ_CS_06); the MMSS-boundary obligation is to faithfully present whatever the service returns and the settling/stable state it signals — restating the 2-minute figure here would over-commit the device boundary to a time it does not control. | High | UC_10, UR_03 |
| RQ_FN_18 | The MMSS shall present each diagnostic candidate with the calibrated confidence indication and per-candidate rationale supplied by the AI analysis service, faithfully and without embellishment, under persistent "decision support — you decide" framing, de-emphasising and flagging low-confidence candidates and surfacing a high-confidence candidate prominently; where the service supplies no rationale for a candidate, the MMSS shall mark it as rationale-unavailable rather than fabricate one. | Calibrated confidence and faithful rationale under decision-support framing enable safe reliance while keeping the diagnostic decision the clinician's. The confidence and rationale are produced by the off-the-shelf model (RQ_CS_01); the MMSS-boundary obligation is faithful relay (no synthesis or alteration) and an explicit unavailable state, since the device cannot manufacture a rationale the external model does not provide — fabricating one would be a misleading-output hazard and is unimplementable as an internal capability. | High | UC_10, UR_04 |
| RQ_FN_19 | The MMSS shall withhold decision-ready presentation of diagnostic candidates while the ranking is unstable or when the external service returns malformed output, showing an explicit "ranking settling" or unavailable state instead. | Presenting unstable or malformed candidates as decision-ready would mislead the clinician; explicit intermediate states prevent over-trust. | High | UC_10, UR_03 |
| RQ_FN_20 | The MMSS shall, when the diagnostic analysis cannot reach a conclusion within its expected time or the external service is unreachable, replace any "working" indication with an explicit timed "inconclusive — proceed to manual assessment" notification while vital-sign monitoring continues uninterrupted. | An explicit, timed no-conclusion notification makes the fallback to manual assessment deliberate and avoids lost diagnostic time on a silent system. | High | UC_11, UR_09 |
| RQ_FN_21 | The MMSS shall sustain continuous vital-sign tracking and stable diagnostic output without interruption as the patient moves between care settings, and shall surface any monitoring interruption or continuity loss with a persistent, salient indication. | Continuity of monitoring across transfer must be maintained, and any gap must be visible rather than going unnoticed. | High | UC_12, UR_15 |
| RQ_FN_22 | The MMSS shall, before any share to the Hospital Information System, require a mandatory patient-identity and destination match-and-confirm step displaying the identifiers for the clinician to match, and shall block the share on an identifier mismatch. | A forced match-and-confirm gate is the control against attaching clinical data to the wrong patient or facility during handover. | High | UC_12, UR_14 |
| RQ_FN_23 | The MMSS shall share monitored vital signs and diagnostic findings to the Hospital Information System over the standard interoperability protocol, preserving each item's provenance and timestamp, and shall surface a failure rather than silently dropping the share when the HIS is unreachable. | Provenance-preserving, standards-based sharing enables seamless continuity of care and a trustworthy second opinion, with failures made visible. | High | UC_12, UR_14 |
| RQ_FN_24 | The MMSS shall protect personal and clinical data it displays and shares in conformity with applicable privacy and information-security obligations, including protected transport for shared data. | Statutory privacy and security duties bind every handling of identifiable patient data throughout display and sharing. | High | UC_12, UR_17 |
| RQ_FN_25 | The MMSS shall provide a self-contained simulation/training mode that reproduces monitoring, alarms, and diagnostic candidates against simulated data without a live patient, entered and exited only through a guarded action, and shall display a persistent, unmistakable training-mode indication on every screen. | Safe self-contained simulation builds and maintains competence without patient exposure, while persistent indication prevents confusing simulated data with live monitoring. | Med | UC_13, UR_13 |
| RQ_FN_26 | The MMSS shall allow an authorised super-user to configure and manage acquisition sources from the installed-base devices through the standardised interfaces, tolerating make/model/firmware variation and explicitly rejecting an incompatible variant with guidance. | Configurable source/settings management lets the product be deployed and maintained across an evolving installed base without replacing equipment. | High | UC_14, UR_16 |
| RQ_FN_27 | The MMSS shall support a defined update and serviceability cadence and make the availability impact of a pending update predictable and communicated to the user. | A serviceable, predictable update cadence keeps monitoring availability and lifecycle cost defensible across the product's market life. | High | UC_14, UR_19 |
| RQ_FN_28 | The MMSS shall support reliable one-handed, error-tolerant operation — reading values, acknowledging an alarm, and switching view — using large, well-spaced targets and confirm-on-release, and shall make destructive actions confirmed or reversible so a mis-tap neither dismisses an alarm nor changes a setting unintentionally. | Operators act one-handed under field stress; forgiving, error-tolerant interaction prevents unintended or unrecoverable actions during patient care. | High | UC_15, UR_11 |

#### Performance Requirements (RQ_PR_*)

Quantitative requirements on how well the system performs its functions: response times, throughput, accuracy, capacity, availability.

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_PR_01 | The MMSS shall complete power-on self-test and reach a state ready to begin live presentation of each connected source within 10 seconds of power-on under nominal conditions, the 10 s budget covering MMSS self-test and the system's own readiness logic and excluding any sensor's intrinsic physical settling time that is outside MMSS control. | A bounded activation time ensures the device is fit for emergency use without an unacceptable wait, while still permitting the not-ready lockout to complete. The budget is scoped to MMSS-controllable activation: certain sensors (e.g. thermal probe, EEG) have intrinsic physical settling that can exceed 10 s, so a flat "VALID — LIVE for all signals within 10 s" would be unimplementable; per RQ_FN_01/02 each parameter is presented as valid only once its own source has settled. | High | RQ_FN_01 |
| RQ_PR_02 | The MMSS shall present each acquired vital-sign value on the display within 1 second of its acquisition from the source device. | The end-to-end measurement-to-display latency the clinician observes must be sub-second for real-time situational awareness. This 1 s boundary budget is the user-visible roll-up of the internal DPREC (≤ 800 ms) and DPROC (≤ 200 ms) item budgets, which are not themselves MMSS-boundary requirements. | High | RQ_FN_06 |
| RQ_PR_03 | The MMSS shall refresh the displayed vital-sign set on a timer-based update interval of 1 second. | A fixed 1 s UI refresh cadence gives a predictable, readable display and matches the boundary display-latency budget. | High | RQ_FN_06 |
| RQ_PR_04 | The MMSS shall accept and process vital-sign input from each source at a sustained rate of at least 0.1 Hz (one sample per 10 seconds or faster) without loss. | The system must keep pace with the minimum source sampling rate so that no acquired sample is dropped at the boundary. | High | RQ_FN_04 |
| RQ_PR_05 | The MMSS shall update the per-source connection/acquisition status indication within 1 second of a change in that source's acquisition state. | Timely per-source status keeps the user's view of which devices are actively acquiring trustworthy and current. | High | RQ_FN_04 |
| RQ_PR_06 | The MMSS shall annunciate the freshness/liveness state of a displayed vital sign and mark it "stale" within 1 second of its source ceasing to update. | Sub-second staleness marking ensures a frozen value is never read as live for longer than one display cycle. | High | RQ_FN_07 |
| RQ_PR_07 | The MMSS shall present a high-priority safe-limit alarm within 1 second of detecting the limit breach. | Sub-second alarm presentation after detection is the boundary-observable budget that keeps annunciation of deterioration timely. | High | RQ_FN_08 |
| RQ_PR_08 | The MMSS shall trigger the connection (loss-of-signal) alarm when no valid input is received from a measurement device for 5 seconds of continuous inactivity. | A fixed 5 s inactivity criterion gives consistent, boundary-observable loss-of-signal detection across all device types. | High | RQ_FN_16 |
| RQ_PR_09 | The MMSS shall present the connection / sensor-misplacement alarm within 1 second of its trigger condition being met. | Sub-second presentation after trigger ensures a disconnected or misplaced sensor is surfaced to the user without perceptible delay. | High | RQ_FN_14 |
| RQ_PR_10 | The MMSS shall present the ranked diagnostic candidates within 1 second of receiving them from the external AI analysis service. | The MMSS-boundary budget governs only the display latency after receipt; the upstream ranking convergence (2 minutes) is an external ALGOS budget the MMSS only reacts to, not an MMSS performance requirement. | High | RQ_FN_17 |
| RQ_PR_11 | The MMSS shall transmit shared vital signs and diagnostic findings to the Hospital Information System within 1 second of the user confirming the share. | A sub-second share latency keeps clinical handover responsive once the identity-match gate is passed. | High | RQ_FN_23 |
| RQ_PR_12 | The MMSS shall, when the external AI analysis service does not return a converged result within its expected time or is unreachable, present the explicit timed "inconclusive — proceed to manual assessment" notification within 1 second of that expected-time deadline elapsing. | The 2-minute convergence deadline is an external ALGOS budget; the MMSS performance requirement is only the sub-second boundary reaction (the fallback notification) once that external deadline lapses, with monitoring uninterrupted. | High | RQ_FN_20 |
| RQ_PR_13 | The MMSS shall present concurrently active alarms in strict priority order such that the highest-priority active alarm is the foremost annunciation within 1 second of its becoming the highest-acuity active alarm. | Timely re-ordering ensures the most critical event is foremost without being masked or delayed by lower-priority information. | High | RQ_FN_10 |
| RQ_PR_14 | The MMSS shall register a one-handed user action — read, alarm-acknowledge, or view-switch — and present its confirm-on-release feedback within 1 second of the release. | Sub-second, predictable interaction feedback supports reliable one-handed operation under field stress. | High | RQ_FN_28 |
| RQ_PR_15 | The MMSS shall sustain continuous vital-sign tracking and diagnostic output across a care-setting transfer, and shall surface any monitoring interruption with a persistent indication within 1 second of the continuity loss being detected. | Prompt, salient surfacing of any continuity gap prevents an unnoticed interruption during transfer. | High | RQ_FN_21 |

#### Non-Functional Requirements (RQ_NF_*)

How the system should behave rather than what it does: reliability, maintainability, security, privacy, scalability. Compliance, labeling, and training requirements live here too.

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_NF_01 | The MMSS shall be developed, verified, and maintained under a documented software life-cycle process conforming to ANSI/AAMI/IEC 62304 commensurate with its assigned software safety class. | Lawful market access requires the device software to be produced under a class-appropriate, auditable life-cycle process; absence of a conforming process is a direct conformity failure. | Compliance | BR_01, BR_02 |
| RQ_NF_02 | The MMSS shall maintain auditable, version-controlled traceability linking each requirement to its risk controls, design, and verification evidence, reproducible on demand for external audit. | A notified body must be able to assess and reproduce conformity of the technical documentation; unbroken traceability is the evidentiary backbone of the design history file. | Maintainability | BR_02 |
| RQ_NF_03 | The MMSS shall be accompanied by a risk management file conforming to ISO 14971 that documents hazard analysis, implemented risk controls, and a justified acceptable residual risk before market release. | Diagnostic and alarm-bearing software demands systematic hazard control; the residual-risk justification is a precondition of both safety and the reduced safety classification. | Compliance | BR_03 |
| RQ_NF_04 | The MMSS shall achieve and demonstrate that its safe-limit alarm function remains operative and timely independent of the state of its diagnostic-support capability, such that no failure, hang, or resource exhaustion of the diagnostic path (including the external AI library) can delay or suppress a safe-limit alarm beyond its boundary budget, evidenced in the risk management file. | The reduced (Class B) classification can only be relied upon if the independence of the external protective measure is demonstrated; latent coupling silently invalidates the classification basis. Because RQ_CS_04 fixes a single shared host CPU, "independence" here is boundary-observable freedom-from-interference (the alarm path is not blockable by the diagnostic path), not physical hardware separation — the achievable, verifiable property given the imposed platform; the per-CPU mitigation hardware that lifts Class C to B is the external measure, not an internal MMSS allocation. | Reliability | BR_04, BR_03 |
| RQ_NF_05 | The MMSS shall qualify every item of software of unknown provenance (SOUP), including the commercially supplied AI diagnostic model, with documented version identification, performance characterisation, provenance, and risk assessment. | The legal manufacturer owns the integrated device regardless of component origin; SOUP qualification is mandated by IEC 62304 and is the basis for accepting third-party AI capability. | Compliance | BR_06, BR_07 |
| RQ_NF_06 | The MMSS shall be substantiated by clinical evidence characterising its diagnostic-support performance, ranking-convergence behaviour, and bounded boundary-observable inference latency before market entry. | The diagnostic claim is the principal value claim and highest-risk element; intended use and indications must be substantiated by evidence, not asserted, to satisfy the notified body. | Compliance | BR_05 |
| RQ_NF_07 | The MMSS shall undergo and document usability engineering conforming to IEC 62366-1, validating that use-related hazards — including clinician misinterpretation of ranked diagnostic candidates — are mitigated under representative use conditions. | Use-related hazards in safety-critical decision support must be identified, mitigated, and validated through human-factors engineering, not assumed, to satisfy usability-safety obligations. | Usability | BR_16 |
| RQ_NF_08 | The MMSS alarm system for abnormal physiological conditions and sensor/connection faults shall conform to the applicable alarm-safety standard (IEC 60601-1-8) for alarm prioritisation, signalling, and reliability. | Conformity to the recognised alarm-safety standard establishes presumption of conformity for clinically actionable signalling and controls alarm fatigue and missed alarms. | Compliance | BR_03, BR_16 |
| RQ_NF_09 | The MMSS shall protect personal and clinical data it handles, stores, displays, or transmits in conformity with applicable data-protection law (e.g. GDPR/HIPAA) and the applicable health-software security standard (IEC 81001-5-1), preserving confidentiality and integrity across the lifecycle, including authenticated, encrypted transport for all data shared over the HIS integration interface. | Handling identifiable patient data imposes statutory privacy and security duties; non-conformity blocks deployment and exposes the manufacturer to regulatory and liability action. Naming authenticated encrypted transport on the share path gives the security obligation a concrete, verifiable acceptance point rather than an unbounded "protect" — the share over the HIS interface (RQ_IF_09/10) is the principal data-egress surface. | Security | BR_10 |
| RQ_NF_10 | The MMSS shall preserve end-to-end data integrity, source provenance, and timestamp of each monitored value and diagnostic finding it exports to receiving clinical-record and device ecosystems. | The receiving system can only interpret and trust exported diagnostic findings if integrity, provenance, and timing are preserved; corrupted or unattributed export is a clinical-safety and vigilance hazard. | Reliability | BR_09 |
| RQ_NF_11 | The MMSS labelling and instructions for use shall accurately state the intended use, indications, contraindications, residual risks, the limitations of the AI diagnostic support, and the required user training and qualifications. | Accurate labelling confines the device to its validated scope and is a mandatory conformity element; misstated intended use or undisclosed limitations is a labelling non-compliance and a foreseeable-misuse hazard. | Compliance | BR_17, BR_01 |
| RQ_NF_12 | The MMSS shall provide a self-contained safe simulation and training mode, segregated from live patient operation and unambiguously indicated as non-clinical, enabling competence building without exposure to live patients. | Mandatory simulation training is the documented mitigation for clinician misinterpretation of AI candidates; the training mode must be incapable of being mistaken for live clinical use. | Reliability | BR_15 |
| RQ_NF_13 | The MMSS shall be designed for maintainability and serviceability with a defined, documented software-update and patch cadence that preserves the validated safety classification and conformity across each release. | Serviceability and a controlled update cadence must be designed in up front; uncontrolled updates can invalidate the conformity and classification basis and erode availability. | Maintainability | BR_12 |
| RQ_NF_14 | The MMSS shall be supported by a maintained design history file and a post-market surveillance, vigilance, incident-reporting, and complaint-handling capability sustained for the device's entire market life, including monitoring of real-world AI diagnostic performance drift. | Post-market surveillance and vigilance are statutory ongoing legal-manufacturer duties; for AI-driven diagnostic functionality the performance-drift monitoring load is heavier and must be provisioned from launch. | Compliance | BR_14 |
| RQ_NF_15 | The MMSS shall be manufacturable, deployable, and scalable across the target markets without re-validation of unchanged safety- and conformity-relevant software, supporting deployment to the supported device configurations. | Scalable deployment must not silently alter the validated configuration; the conformity and classification basis must hold across every deployed instance and market. | Scalability | BR_13 |
| RQ_NF_16 | The MMSS shall implement a defined end-of-life and decommissioning behaviour covering secure disposal of residual personal data and an orderly, documented withdrawal of deployed units. | Secure data disposal and orderly withdrawal at end-of-life are statutory data-protection and lifecycle-safety obligations; committing to them late inflates total cost of ownership and liability exposure. | Security | BR_19 |

#### Constraint Requirements (RQ_CS_*)

External constraints the system must respect: regulatory rules, applicable standards, imposed technology choices, environmental conditions.

| ID | Description | Rationale | Classification | Traces |
|----|-------------|-----------|----------------|--------|
| RQ_CS_01 | The MMSS shall use a commercially available, externally validated off-the-shelf AI diagnostic model (Open Evidence) for its first release and shall not incorporate a custom or first-party trained diagnostic model. | Imposed v1 constraint: the off-the-shelf validated model is mandated to contain AI validation complexity and regulatory-clearance risk; a custom model is out of scope for the first release. | Imposed technology choice | RE_04, RE_03 |
| RQ_CS_02 | The MMSS shall comply with ANSI/AAMI/IEC 62304 at the software safety class of Class C as mitigated to Class B by an independent external hardware risk-control measure. | The classification and its mitigation are the binding regulatory premise of the entire life-cycle and evidence burden; deviating from it invalidates the conformity basis. | Regulatory rule | RE_01, RE_02 |
| RQ_CS_03 | The MMSS shall support acquisition from the six defined non-invasive measurement device types — ECG monitor, pulse oximeter, blood pressure monitor, thermal probe, capnometer, and EEG monitor — through their standardised interfaces. | Supporting the fixed set of six device types is a scope constraint; the device must integrate the existing installed base through controlled interfaces rather than mandate replacement. | Imposed technology choice | RE_06 |
| RQ_CS_04 | The MMSS shall execute on the fixed embedded host CPU platform providing real-time operating-system capabilities, without requiring hardware modification. | The host platform is an existing, fixed context element; software-only scope and deterministic real-time behaviour constrain the MMSS to the provided RTOS-capable embedded platform. | Environmental condition | RE_06 |
| RQ_CS_05 | The MMSS shall observe a measurement-to-display latency budget of at most 1 second at its user-facing boundary for vital-sign presentation. | The 1-second MMSS display latency budget is an imposed boundary-observable constraint distinct from the ALGOS diagnostic-convergence budget and must be respected for timely situational awareness. | Environmental condition | RE_06 |
| RQ_CS_06 | The MMSS shall treat the 2-minute diagnosis-convergence target as an ALGOS budget external to the MMSS, and shall not be required to meet that convergence time within its own boundary. | The 2-minute convergence is explicitly an ALGOS budget, not an MMSS budget; constraining it correctly prevents mis-allocating an external timing obligation to the device boundary. | Imposed technology choice | RE_11 |
| RQ_CS_07 | The MMSS shall exchange data with hospital information systems through a controlled, version-managed interface specification implementing the agreed healthcare interoperability protocol (HL7 or FHIR, to be confirmed). | The HIS protocol is to be defined (HL7/FHIR); the constraint fixes that exchange must occur through a controlled interface specification using a standard interoperability protocol, however resolved. | Applicable standard | RE_07 |
| RQ_CS_08 | The MMSS shall conform to the applicable medical alarm-system standard (IEC 60601-1-8) for the design, prioritisation, and signalling of physiological and technical alarms. | Conformity to the recognised alarm-safety standard yields presumption of conformity for the alarm function and is an external standards constraint the device must respect. | Applicable standard | RE_06 |
| RQ_CS_09 | The MMSS shall conform to the applicable usability-engineering standard for medical devices (IEC 62366-1) in the design and validation of its user interface. | Usability engineering to the recognised standard is the external constraint establishing conformity for use-safety, including mitigation of diagnostic-candidate misinterpretation. | Applicable standard | RE_05 |
| RQ_CS_10 | The MMSS shall conform to applicable health-data protection law (e.g. GDPR/HIPAA) and the applicable health-software security standard (IEC 81001-5-1) for all personal and clinical data it processes, displays, or transmits. | Data-protection law and the health-software security standard are binding external constraints on lawful handling of identifiable patient data across the device lifecycle. | Regulatory rule | RE_07 |
| RQ_CS_11 | The MMSS shall be deployed and used only by trained medical professionals as the qualified user population, consistent with its intended use and validated training requirements. | The trained-clinician user population is an imposed use constraint and a premise of the usability validation, labelling, and residual-risk argument; use outside it falls outside the validated scope. | Environmental condition | RE_05, RE_09 |

### Verification (SV_*)

The **BDD feature files** that verify the functional requirements, defined jointly by the 3-Amigos (Product Owner, Development Lead, Verification Lead). Write **one feature file per functional requirement** as a `gherkin` fenced block, tagged `@ID:RQ_FN_xx` to trace it to the requirement it verifies. Each feature has a user story (`As a … I want … So that …`), a `Rule:` that captures the requirement's "shall" statement, and one or more concrete `Scenario`s with `Given / When / Then` steps and data tables for the expected values. Use measurable outcomes (e.g. "within 5 seconds"). Every RQ_FN_* must have a feature file and every RQ_* must be covered by at least one scenario. The converter records each feature file as one row (`SV_*`) in the workbook's Verification table.

```gherkin
@ID:RQ_FN_01
Feature: Startup Self-Test and Not-Ready Lockout
    As a clinician I want the MMSS to verify itself and hold a NOT READY state on power-on until monitoring has settled
    So that I never act on an unsettled or unverified value during an emergency

Rule: The MMSS shall, on power-on, run a startup self-test and hold an explicit "NOT READY / SETTLING" state in which no acquired value is presented as valid, until self-test and per-sensor settling for the safety-relevant signal set have completed.

Scenario: MMSS enters NOT READY immediately on power-on
    Given the simulator is running
    And the MMSS is powered off
    When the MMSS is powered on
    Then the displayed readiness state is the following within 2 seconds
    | readiness state      |
    | NOT READY / SETTLING |

Scenario: No acquired value is presented as valid while NOT READY
    Given the simulator is running
    And the simulator injects the following safety-relevant sensors with stable values
    | sensor         | parameter   | injected value |
    | ECG monitor    | Heart Rate  | 82 bpm         |
    | Pulse Oximeter | SpO2        | 97 %           |
    | BP Monitor     | NIBP        | 120/80 mmHg    |
    | Thermal Probe  | Temperature | 36.8 degC      |
    And the MMSS is powered on
    When the MMSS is in the "NOT READY / SETTLING" state
    Then no vital-sign value on the Display Interface is marked valid
    And every parameter tile shows a not-valid indication

Scenario: MMSS holds NOT READY until self-test and settling complete
    Given the simulator is running
    And the simulator injects the safety-relevant sensor set with stable values
    And the simulator holds the self-test routine in an in-progress state
    When the MMSS is powered on
    And the startup self-test has not yet completed
    Then the readiness state remains "NOT READY / SETTLING"

Scenario: MMSS stays NOT READY while one safety-relevant signal is still settling
    Given the simulator is running
    And the simulator injects all safety-relevant sensors as settled except the Thermal Probe
    And the Thermal Probe is injected as still physically settling
    When the MMSS is powered on
    And the startup self-test passes
    Then the readiness state remains "NOT READY / SETTLING"
    And the Temperature tile shows a "settling" not-valid indication

Scenario: MMSS holds NOT READY when a safety-relevant sensor disconnects during settling
    Given the simulator is running
    And the simulator injects the safety-relevant sensor set as settling
    When the Pulse Oximeter is disconnected in the simulator before settling completes
    Then the readiness state remains "NOT READY / SETTLING"
    And no vital-sign value on the Display Interface is marked valid
```

```gherkin
@ID:RQ_FN_02
Feature: Transition to VALID — LIVE Monitoring
    As a clinician I want a distinct VALID — LIVE state to appear only once the device is verified and settled
    So that I know precisely when displayed values may be relied upon

Rule: The MMSS shall transition from the not-ready state to a distinct "VALID — LIVE" monitoring state, unlocking live presentation, only once self-test passes and the safety-relevant signal set has settled.

Scenario: MMSS unlocks live presentation after self-test passes and signals settle
    Given the simulator is running
    And the simulator injects the following safety-relevant sensors as settled
    | sensor         | parameter   | injected value |
    | ECG monitor    | Heart Rate  | 82 bpm         |
    | Pulse Oximeter | SpO2        | 97 %           |
    | BP Monitor     | NIBP        | 120/80 mmHg    |
    | Thermal Probe  | Temperature | 36.8 degC      |
    And the MMSS is in the "NOT READY / SETTLING" state
    When the startup self-test passes
    And the simulator reports the safety-relevant signal set as settled
    Then the displayed readiness state is the following within 1 second
    | readiness state |
    | VALID — LIVE    |
    And live vital-sign presentation is unlocked
    And each parameter tile shows its injected value marked valid

Scenario: Live presentation stays locked until both conditions are met
    Given the simulator is running
    And the simulator injects the safety-relevant sensor set with stable values
    And the MMSS is in the "NOT READY / SETTLING" state
    When the startup self-test passes
    And the simulator reports the safety-relevant signal set as not yet settled
    Then the readiness state is not "VALID — LIVE"
    And live vital-sign presentation remains locked

    # covers: RQ_PR_01
Scenario: MMSS reaches readiness within the 10 second activation budget under nominal conditions
    Given the simulator is running
    And the MMSS is powered off
    And the simulator injects the safety-relevant sensor set with stable values and instantaneous sensor settling
    When the MMSS is powered on under nominal conditions
    Then the MMSS completes self-test and reaches a state ready to begin live presentation within 10 seconds of power-on
    And the measured MMSS activation time excludes any sensor's intrinsic physical settling time
```

```gherkin
@ID:RQ_FN_03
Feature: Self-Test Failure and Readiness-Timeout Annunciation
    As a clinician I want an explicit fault or timeout annunciation when the device cannot reach readiness
    So that a failure to start is never mistaken for a working system

Rule: The MMSS shall, on self-test failure or when the bounded readiness time is exceeded, remain in the not-ready state, annunciate the fault or readiness-timeout explicitly, and present no value as valid.

Scenario: MMSS annunciates a self-test failure and presents no valid value
    Given the simulator is running
    And the MMSS is in the "NOT READY / SETTLING" state
    When the simulator forces the startup self-test to fail
    Then the readiness state remains "NOT READY / SETTLING"
    And an explicit fault annunciation is shown within 1 second
    And the fault annunciation names the failed self-test
    And no vital-sign value on the Display Interface is marked valid

Scenario: MMSS annunciates a readiness-timeout when the bounded time is exceeded
    Given the simulator is running
    And the MMSS is in the "NOT READY / SETTLING" state
    And the bounded MMSS readiness time is 10 seconds
    When the simulator withholds settling so readiness is not reached for 11 seconds
    Then the readiness state remains "NOT READY / SETTLING"
    And an explicit readiness-timeout annunciation is shown within 1 second of the 10 second deadline
    And no vital-sign value on the Display Interface is marked valid

    # covers: RQ_IF_14
Scenario: MMSS obtains real-time scheduling and timing services from the host platform per the platform ICD
    Given the simulator is running
    And the MMSS is executing on the RTOS-capable host platform over the host-platform interface IF_06
    And the MMSS is in the "VALID — LIVE" state
    And the ECG monitor is acquiring with Heart Rate 82 bpm in the simulator
    When the host platform is driven to its specified worst-case compute load for 10 seconds
    Then the MMSS-scheduled 1 second display-refresh timer obtained over IF_06 continues to fire on a 1 second interval
    And each successive timer tick occurs 1 second after the previous one within a tolerance of 100 milliseconds as defined by the platform services (RTOS) ICD
```

```gherkin
@ID:RQ_FN_04
Feature: Poll Devices and Show Per-Source Acquisition Status
    As a clinician I want each connected device polled and its acquisition status shown
    So that I can confirm every installed device is actually acquiring and not silently failed

Rule: The MMSS shall acquire data by polling each connected measurement device of the six supported types and present a per-source connection/acquisition status for every device.

    # covers: RQ_CS_03, RQ_IF_01
Scenario: MMSS shows an acquiring status for each connected supported device
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    When the following measurement devices are connected in the simulator
    | device         |
    | ECG monitor    |
    | Pulse Oximeter |
    | BP Monitor     |
    | Thermal Probe  |
    | Capnometer     |
    | EEG Monitor    |
    Then each device shows an "acquiring" per-source status on the Display Interface within 1 second
    And a per-source status is present for every connected device

Scenario: MMSS shows a not-connected status for a device not present
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    And no Capnometer is connected in the simulator
    When the per-source status is read for the Capnometer
    Then the Capnometer shows a "not connected" per-source status

    # covers: RQ_PR_05
Scenario: MMSS updates a device status from acquiring to failed when polling stops returning
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    And the ECG monitor is acquiring with Heart Rate 82 bpm in the simulator
    When the simulator makes the ECG monitor stop responding to polls
    Then the ECG monitor per-source status changes from "acquiring" to "not acquiring" within 1 second
    And the change is visible without the value being silently frozen as acquiring
```

```gherkin
@ID:RQ_FN_05
Feature: Tolerate Device Variation and Reject Unsupported Devices
    As a super-user I want the MMSS to accept varied make/model/firmware and explicitly reject an unsupported device
    So that the product deploys onto the existing installed base and an unsupported source is never silently absent

Rule: The MMSS shall tolerate variation in make, model, and firmware across connected devices, report each source's acquisition state, and explicitly reject and annunciate an unsupported device rather than failing silently.

Scenario: MMSS acquires from supported devices of differing make and firmware
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    When the following supported devices are connected in the simulator
    | device      | make     | model    | firmware |
    | ECG monitor | Vendor-A | A-100    | 1.2.0    |
    | ECG monitor | Vendor-B | B-900    | 3.0.1    |
    Then each device shows an "acquiring" per-source status within 1 second

Scenario: MMSS explicitly rejects and annunciates an unsupported device
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    When the following unsupported device is connected in the simulator
    | device          | make     | model   | firmware |
    | Infusion Pump   | Vendor-X | X-50    | 0.9.0    |
    Then the device shows a "rejected — unsupported" status within 1 second
    And an explicit rejection annunciation is shown
    And the device is not presented as acquiring

Scenario: MMSS rejects a supported device type running an unsupported firmware variant
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    When the following device is connected in the simulator
    | device      | make     | model   | firmware |
    | ECG monitor | Vendor-C | C-000   | 0.0.1    |
    And the firmware variant is outside the supported compatibility set
    Then the device shows a "rejected — unsupported" status within 1 second
    And the device is not presented as acquiring
```

```gherkin
@ID:RQ_FN_06
Feature: Continuous Real-Time Vital-Sign Display
    As a clinician I want every vital sign updated continuously in real time
    So that I retain situational awareness of a deteriorating patient

Rule: The MMSS shall continuously display the acquired vital-sign set in real time, updating each parameter tile from its acquiring source within the bounded measurement-to-display latency.

    # covers: RQ_PR_02, RQ_CS_05, RQ_IF_04
Scenario: MMSS updates each parameter tile within the boundary latency
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    And the following sensors are acquiring in the simulator
    | sensor         | parameter  | initial value |
    | ECG monitor    | Heart Rate | 82 bpm        |
    | Pulse Oximeter | SpO2       | 97 %          |
    When the simulator changes the acquired values to the following
    | sensor         | parameter  | new value |
    | ECG monitor    | Heart Rate | 88 bpm    |
    | Pulse Oximeter | SpO2       | 95 %      |
    Then each parameter tile shows the new value on the Display Interface within 1 second of acquisition

Scenario: MMSS keeps refreshing the vital-sign set continuously
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    And the ECG monitor is acquiring in the simulator
    When the simulator changes the Heart Rate by 1 bpm every second from 80 bpm to 90 bpm
    Then the Heart Rate tile reflects each new value within 1 second of each change
    And no intermediate value is skipped on the Display Interface

    # covers: RQ_PR_03, RQ_IF_05
Scenario: MMSS refreshes the displayed vital-sign set on a fixed 1 second timer cadence
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    And the ECG monitor is acquiring with Heart Rate 82 bpm in the simulator
    When the Display Interface refresh cadence is observed for 10 seconds
    Then the displayed vital-sign set refreshes on a timer interval of 1 second
    And each successive refresh occurs 1 second after the previous one within a tolerance of 100 milliseconds

    # covers: RQ_PR_04
Scenario: MMSS accepts the minimum sustained source rate without sample loss
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    And the Capnometer is acquiring in the simulator
    When the simulator emits one valid Capnometer sample every 10 seconds for 60 seconds
    Then all 6 emitted samples are accepted and presented in order
    And no sample is dropped at the acquisition boundary
```

```gherkin
@ID:RQ_FN_07
Feature: Value Freshness and Stale Marking
    As a clinician I want a freshness indication on each value and an explicit stale mark when a source stops updating
    So that a frozen value is never read as live physiology

Rule: The MMSS shall present, for each displayed vital-sign value, a continuous freshness/liveness indication and mark a value explicitly as "stale" when its source stops updating.

Scenario: MMSS shows a live freshness indication for an updating value
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    And the ECG monitor is acquiring with Heart Rate 82 bpm in the simulator
    When the simulator updates the Heart Rate every second
    Then the Heart Rate tile shows a "live" freshness indication

    # covers: RQ_PR_06
Scenario: MMSS marks a value stale within 1 second of its source ceasing to update
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    And the ECG monitor is acquiring with Heart Rate 82 bpm in the simulator
    When the ECG monitor stops updating in the simulator
    Then the Heart Rate tile shows a "stale" indication within 1 second
    And the last value 82 bpm is not presented as live

Scenario: MMSS returns a value to live freshness when its source resumes updating
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    And the Heart Rate tile is showing a "stale" indication after the ECG monitor stopped updating
    When the ECG monitor resumes updating with Heart Rate 85 bpm in the simulator
    Then the Heart Rate tile shows a "live" freshness indication within 1 second
    And the tile shows the new value 85 bpm
```

```gherkin
@ID:RQ_FN_08
Feature: Safe-Limit Breach Alarm
    As a clinician I want an unmistakable high-priority multi-modal alarm when a vital sign breaches its safe limit
    So that I am reliably alerted to patient deterioration

Rule: The MMSS shall detect a configured safe-limit breach and annunciate a reserved high-priority, multi-modal (visual and audible) alarm that names the breached parameter and its priority and is distinct from lower-priority information.

    # covers: RQ_PR_07, RQ_IF_12
Scenario: MMSS raises a high-priority multi-modal alarm on a limit breach
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    And the Heart Rate safe limit is configured to 120 bpm
    When the simulator drives the Heart Rate to 150 bpm
    Then a high-priority alarm is presented within 1 second
    And the alarm is annunciated on the following channels
    | channel |
    | visual  |
    | audible |
    And the alarm names the breached parameter "Heart Rate"
    And the alarm shows its priority "high"

Scenario: MMSS raises no safe-limit alarm while the value stays within its limit
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    And the Heart Rate safe limit is configured to 120 bpm
    When the simulator holds the Heart Rate at 118 bpm
    Then no safe-limit alarm is presented for Heart Rate

Scenario: High-priority alarm is visually distinct from lower-priority information
    Given the simulator is running
    And the Heart Rate safe limit is configured to 120 bpm
    And the simulator has driven the Heart Rate to 150 bpm raising a high-priority alarm
    And a low-priority information message is also present
    When the Display Interface is observed
    Then the high-priority alarm is rendered distinctly from the low-priority information

    # covers: RQ_NF_04, RQ_CS_02
Scenario: Safe-limit alarm stays timely when the diagnostic path hangs (RQ_NF_04 independence)
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    And the Heart Rate safe limit is configured to 120 bpm
    And the external AI analysis library is forced into an unresponsive hang in the simulator
    When the simulator drives the Heart Rate to 150 bpm
    Then a high-priority safe-limit alarm is presented within 1 second
    And the alarm presentation latency is not increased by the hung diagnostic path
```

```gherkin
@ID:RQ_FN_09
Feature: Redundant Multi-Channel Alarm Annunciation
    As a clinician working in the field I want high-priority alarms repeated across at least two senses with robust presentation
    So that a genuine emergency stays detectable when one channel is masked

Rule: The MMSS shall annunciate high-priority alarms redundantly across at least two sensory channels with high-contrast, glare- and motion-resistant presentation, such that an alarm remains detectable when any single channel is masked or unavailable.

    # covers: RQ_IF_13, RQ_NF_08, RQ_CS_08
Scenario: MMSS annunciates a high-priority alarm on at least two channels
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    And the SpO2 safe limit is configured to a lower limit of 90 %
    When the simulator drives the SpO2 to 82 % raising a high-priority alarm
    Then the alarm is annunciated on at least 2 of the following channels
    | channel |
    | visual  |
    | audible |
    | tactile |

Scenario: Alarm remains detectable when the audible channel is masked
    Given the simulator is running
    And the simulator has driven the SpO2 to 82 % raising a high-priority alarm on visual and audible channels
    When the audible channel is masked in the simulator
    Then the alarm remains detectable on the visual channel
    And the visual annunciation is high-contrast and glare-resistant
```

```gherkin
@ID:RQ_FN_10
Feature: Strict Alarm Priority Ordering
    As a clinician I want the highest-acuity alarm presented first and never masked by lower-priority ones
    So that the most critical event reaches me before less urgent alerts

Rule: The MMSS shall present concurrently active alarms in strict priority order such that the highest-acuity alarm is presented first and is never masked or delayed by lower-priority information.

    # covers: RQ_PR_13, RQ_NF_08, RQ_CS_08
Scenario: MMSS presents the highest-acuity alarm foremost among concurrent alarms
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    When the following alarms become active concurrently
    | alarm                 | priority |
    | SpO2 critical low     | high     |
    | Temperature high      | medium   |
    | Sensor signal-quality | low      |
    Then the foremost presented alarm is "SpO2 critical low" within 1 second
    And no lower-priority alarm masks or delays the highest-acuity alarm

Scenario: A newly arriving higher-priority alarm becomes foremost
    Given the simulator is running
    And the simulator has raised a medium-priority "Temperature high" alarm as the foremost active alarm
    When the simulator drives the SpO2 to 82 % raising a high-priority "SpO2 critical low" alarm
    Then the "SpO2 critical low" alarm becomes foremost within 1 second
    And the "Temperature high" alarm is presented below it
```

```gherkin
@ID:RQ_FN_11
Feature: Bounded Auto-Re-Arming Alarm Silence
    As a clinician I want to silence an active alarm for a bounded, visible period that auto-re-arms
    So that I can manage a known intervention without ever leaving the patient unmonitored

Rule: The MMSS shall allow the user to acknowledge an active alarm and silence it for a bounded, clearly indicated period with a visible countdown, after which the alarm re-arms automatically, and shall provide no path to permanently disable or mask the underlying alarm condition.

Scenario: MMSS silences an acknowledged alarm for a bounded period with a visible countdown
    Given the simulator is running
    And the configured alarm silence period is 120 seconds
    And the simulator has driven the SpO2 to 82 % raising a high-priority alarm
    When the user acknowledges and silences the alarm
    Then the alarm audible annunciation is silenced for 120 seconds
    And a visible countdown of the remaining silence time is shown counting down from 120 seconds

Scenario: Silenced alarm re-arms automatically when the period elapses
    Given the simulator is running
    And the configured alarm silence period is 120 seconds
    And a high-priority alarm has been silenced
    And the simulator holds the SpO2 at 82 % so the underlying condition still holds
    When the 120 second silence period elapses
    Then the alarm re-annunciates within 1 second

Scenario: No control permanently disables the underlying alarm condition
    Given the simulator is running
    And the simulator has driven the SpO2 to 82 % raising a high-priority alarm
    When the user attempts every available control to permanently disable the alarm
    Then no control permanently disables or masks the underlying alarm condition
    And the alarm re-arms after at most the configured silence period
```

```gherkin
@ID:RQ_FN_12
Feature: Targeted Silence Confirmation and Nuisance Escalation
    As a clinician I want explicit identification and confirmation when silencing among multiple alarms, and escalation of repeated nuisance silencing
    So that I never silence the wrong alarm or habitually mask real deterioration

Rule: The MMSS shall, when an acknowledge/silence action is requested while multiple alarms are active, explicitly identify the alarm being silenced and require confirmation before silencing the highest-acuity alarm, and shall escalate rather than continue to silence a repeatedly nuisance-silenced recurring condition.

Scenario: MMSS identifies and requires confirmation before silencing the highest-acuity alarm
    Given the simulator is running
    And the following alarms are active concurrently
    | alarm             | priority |
    | SpO2 critical low | high     |
    | Temperature high  | medium   |
    When the user requests to silence an alarm
    Then the MMSS explicitly identifies "SpO2 critical low" as the alarm to be silenced
    And the MMSS requires confirmation before silencing it

Scenario: MMSS escalates a repeatedly nuisance-silenced recurring condition
    Given the simulator is running
    And the nuisance-silence escalation threshold is 3 silences
    And the simulator has recurred the same "SpO2 critical low" condition and the user has silenced it 3 times
    When the simulator recurs the same "SpO2 critical low" condition and the user requests silence again
    Then the MMSS escalates the alarm rather than silencing it
```

```gherkin
@ID:RQ_FN_13
Feature: Confirm Recovery on Live Value Before Clearing Alarm
    As a clinician I want to confirm recovery on the live value before an alarm clears
    So that an alarm is never cleared on the silence alone while a breach persists

Rule: The MMSS shall, following an alarm acknowledgement, prompt the user to confirm recovery on the live value of the breached parameter and shall not clear the alarm state until the value is confirmed within safe limits or the alarm remains active.

Scenario: MMSS clears the alarm only after recovery is confirmed on the live value
    Given the simulator is running
    And the Heart Rate safe limit is configured to 120 bpm
    And a Heart Rate safe-limit alarm raised at 150 bpm has been acknowledged
    And the simulator has returned the live Heart Rate to 96 bpm within the safe limit
    When the user confirms recovery on the live value
    Then the alarm state is cleared

Scenario: MMSS keeps the alarm active when the live value is still breached
    Given the simulator is running
    And the Heart Rate safe limit is configured to 120 bpm
    And a Heart Rate safe-limit alarm raised at 150 bpm has been acknowledged
    And the simulator holds the live Heart Rate at 148 bpm above the safe limit
    When the user attempts to clear the alarm
    Then the alarm state remains active
    And the MMSS prompts to confirm recovery on the live value
```

```gherkin
@ID:RQ_FN_14
Feature: Sensor Fault and Disconnect Signature
    As a clinician I want a distinct fault/disconnect signature with an unmistakable flag replacing the reading
    So that a data fault is never misread as valid physiology

Rule: The MMSS shall detect, per source, a sensor fault, disconnection, or misplacement and annunciate a distinct fault/disconnect signature, different from a safe-limit alarm, while replacing the affected reading with an unmistakable flag rather than silently dropping or substituting it.

    # covers: RQ_PR_09, RQ_IF_02
Scenario: MMSS annunciates a distinct fault signature and flags the reading on disconnect
    Given the simulator is running
    And the Pulse Oximeter is acquiring with SpO2 97 % in the simulator
    When the Pulse Oximeter is disconnected in the simulator
    Then a fault/disconnect signature is annunciated within 1 second
    And the signature is distinct from a safe-limit alarm
    And the SpO2 tile is replaced with an unmistakable fault flag
    And no numeric SpO2 value is presented in place of the fault flag

Scenario: MMSS distinguishes a sensor misplacement from a limit breach
    Given the simulator is running
    And the ECG monitor is acquiring with Heart Rate 82 bpm in the simulator
    When the ECG electrodes are injected as misplaced in the simulator
    Then a fault/disconnect signature is annunciated within 1 second
    And the signature is different from a safe-limit alarm
    And the Heart Rate tile is flagged rather than showing a value as confirmed physiology
```

```gherkin
@ID:RQ_FN_15
Feature: Inline Per-Source Signal-Quality State
    As a clinician I want each value qualified by its signal quality when quality degrades
    So that an artefact-suspect value is not read as a confirmed physiological change

Rule: The MMSS shall present, for each parameter, an inline per-source signal-quality state that visibly qualifies the value itself when quality degrades, so that an artefact-suspect value cannot be read as a confirmed physiological change.

Scenario: MMSS qualifies a value inline when its signal quality degrades
    Given the simulator is running
    And the Pulse Oximeter is acquiring with SpO2 88 % at "good" signal quality in the simulator
    When the simulator injects a "poor" SpO2 signal-quality state
    Then the SpO2 value tile shows an inline "poor" signal-quality state within 1 second
    And the SpO2 value 88 % is visibly marked as artefact-suspect

Scenario: MMSS shows a good signal-quality state when quality is nominal
    Given the simulator is running
    And the Pulse Oximeter is acquiring with SpO2 97 % at "good" signal quality in the simulator
    When the SpO2 value tile is observed
    Then the SpO2 value tile shows a "good" inline signal-quality state
    And the SpO2 value 97 % is not marked artefact-suspect
```

```gherkin
@ID:RQ_FN_16
Feature: Connection-Inactivity Disconnect Detection
    As a clinician I want a device treated as disconnected after a defined inactivity interval
    So that loss-of-signal is detected consistently across all device types

Rule: The MMSS shall treat a measurement device as inactive/disconnected and raise the disconnect indication when no valid input is received from it for the defined inactivity interval.

    # covers: RQ_PR_08, RQ_IF_03
Scenario: MMSS raises the disconnect indication after the inactivity interval
    Given the simulator is running
    And the connection-inactivity interval is 5 seconds
    And the ECG monitor is acquiring with Heart Rate 82 bpm in the simulator
    When the simulator withholds all valid input from the ECG monitor for 5 seconds
    Then the ECG monitor shows a disconnect indication within 1 second of the 5 second interval elapsing
    And the ECG monitor is treated as inactive

Scenario: MMSS does not raise disconnect before the inactivity interval elapses
    Given the simulator is running
    And the connection-inactivity interval is 5 seconds
    And the ECG monitor is acquiring with Heart Rate 82 bpm in the simulator
    When the simulator withholds valid input from the ECG monitor for 3 seconds then resumes
    Then the ECG monitor is not treated as disconnected at any point
```

```gherkin
@ID:RQ_FN_17
Feature: Request and Present Ranked Diagnostic Candidates
    As a clinician I want ranked diagnostic candidates returned from the analysis service
    So that I can focus quickly on the most likely conditions

Rule: The MMSS shall request diagnostic analysis from the external AI analysis service using the live multi-parameter data and present the returned diagnostic candidates as a ranked list, reflecting the external service's convergence signal at the boundary.

    # covers: RQ_PR_10, RQ_IF_06, RQ_IF_07, RQ_CS_01, RQ_CS_06
Scenario: MMSS presents returned candidates as a ranked list
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    And the external AI analysis service returns the following candidates
    | candidate     | rank |
    | Sepsis        | 1    |
    | Dehydration   | 2    |
    | Anaemia       | 3    |
    When the diagnostic analysis is requested with the live multi-parameter data
    Then the candidates are presented in ranked order within 1 second of receipt
    | candidate   |
    | Sepsis      |
    | Dehydration |
    | Anaemia     |

Scenario: MMSS reflects the service ranking-stable convergence signal at the boundary
    Given the simulator is running
    And the external AI analysis service returns candidates with signal "ranking-stable"
    When the candidates are presented
    Then the presentation reflects the "ranking-stable" state from the service

Scenario: MMSS re-orders the presented candidates when the service returns a new ranking
    Given the simulator is running
    And the MMSS is presenting the following ranked candidates
    | candidate   | rank |
    | Dehydration | 1    |
    | Sepsis      | 2    |
    When the external AI analysis service returns the following updated ranking
    | candidate   | rank |
    | Sepsis      | 1    |
    | Dehydration | 2    |
    Then the presented order updates to "Sepsis" then "Dehydration" within 1 second of receipt
```

```gherkin
@ID:RQ_FN_18
Feature: Faithful Confidence and Rationale Under Decision-Support Framing
    As a clinician I want each candidate's confidence and rationale relayed faithfully under "you decide" framing
    So that I can rely on decision support safely while keeping the decision mine

Rule: The MMSS shall present each diagnostic candidate with the calibrated confidence and per-candidate rationale supplied by the AI analysis service, faithfully and without embellishment, under persistent "decision support — you decide" framing, de-emphasising low-confidence candidates and surfacing a high-confidence candidate prominently; where the service supplies no rationale, the MMSS shall mark it rationale-unavailable rather than fabricate one.

Scenario: MMSS relays supplied confidence and rationale faithfully under decision-support framing
    Given the simulator is running
    And the external AI analysis service returns the following candidates
    | candidate | confidence | rationale            |
    | Sepsis    | 0.91       | elevated HR and temp |
    | Anaemia   | 0.20       | low SpO2 trend       |
    When the candidates are presented
    Then each candidate shows the supplied confidence and rationale unchanged
    | candidate | confidence | rationale            |
    | Sepsis    | 0.91       | elevated HR and temp |
    | Anaemia   | 0.20       | low SpO2 trend       |
    And the high-confidence candidate "Sepsis" is surfaced prominently
    And the low-confidence candidate "Anaemia" is de-emphasised
    And a persistent "decision support — you decide" framing is shown

Scenario: MMSS marks a candidate rationale-unavailable when the service supplies none
    Given the simulator is running
    And the external AI analysis service returns the following candidate
    | candidate   | confidence | rationale |
    | Dehydration | 0.55       |           |
    When the candidate is presented
    Then the candidate is marked "rationale unavailable"
    And no rationale text is fabricated for the candidate
```

```gherkin
@ID:RQ_FN_19
Feature: Withhold Unstable or Malformed Diagnostic Output
    As a clinician I want unstable or malformed diagnostic output withheld behind an explicit settling/unavailable state
    So that I do not over-trust candidates that are not decision-ready

Rule: The MMSS shall withhold decision-ready presentation of diagnostic candidates while the ranking is unstable or when the external service returns malformed output, showing an explicit "ranking settling" or unavailable state instead.

Scenario: MMSS shows ranking-settling while the external ranking is unstable
    Given the simulator is running
    And the external AI analysis service signals "ranking-unstable"
    When the diagnostic candidates would be presented
    Then the MMSS shows an explicit "ranking settling" state
    And no candidates are presented as decision-ready

Scenario: MMSS shows an unavailable state on malformed service output
    Given the simulator is running
    And the external AI analysis service returns the following malformed payloads
    | malformation                  |
    | non-JSON body                 |
    | missing candidate rank field  |
    | confidence value out of 0..1  |
    When the diagnostic candidates would be presented for each payload
    Then the MMSS shows an explicit "diagnostic unavailable" state for each
    And no candidates are presented as decision-ready
```

```gherkin
@ID:RQ_FN_20
Feature: Timed Inconclusive Fallback to Manual Assessment
    As a clinician I want an explicit timed "inconclusive — proceed to manual assessment" notification when diagnosis cannot conclude
    So that the fallback to manual assessment is deliberate and no time is lost on a silent system

Rule: The MMSS shall, when the diagnostic analysis cannot reach a conclusion within its expected time or the external service is unreachable, replace any "working" indication with an explicit timed "inconclusive — proceed to manual assessment" notification while vital-sign monitoring continues uninterrupted.

    # covers: RQ_PR_12, RQ_IF_08, RQ_CS_06
Scenario: MMSS shows the inconclusive notification when the expected time lapses
    Given the simulator is running
    And the expected diagnostic-convergence time is 120 seconds
    And the diagnostic analysis is in a "working" state
    And the ECG monitor is acquiring with Heart Rate 82 bpm in the simulator
    When the external service returns no converged result for 120 seconds
    Then the "working" indication is replaced with "inconclusive — proceed to manual assessment" within 1 second of the 120 second deadline
    And the Heart Rate tile keeps updating without interruption

Scenario: MMSS shows the inconclusive notification when the service is unreachable
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    And the ECG monitor is acquiring with Heart Rate 82 bpm in the simulator
    When the simulator makes the external AI analysis service unreachable
    Then the "inconclusive — proceed to manual assessment" notification is shown within 1 second
    And the Heart Rate tile keeps updating without interruption
```

```gherkin
@ID:RQ_FN_21
Feature: Continuity Across Care-Setting Transfer
    As a clinician I want monitoring and diagnostic output sustained across a transfer with any interruption surfaced
    So that no monitoring gap goes unnoticed during patient movement

Rule: The MMSS shall sustain continuous vital-sign tracking and stable diagnostic output without interruption as the patient moves between care settings, and shall surface any monitoring interruption or continuity loss with a persistent, salient indication.

Scenario: MMSS sustains monitoring across a care-setting transfer
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    And the ECG monitor is acquiring with Heart Rate 82 bpm in the simulator
    And diagnostic candidates are presented with signal "ranking-stable"
    When the simulator transfers the patient context from "ward" to "ambulance" without dropping any source
    Then the Heart Rate tile keeps updating without interruption
    And the presented diagnostic ranking remains unchanged

    # covers: RQ_PR_15
Scenario: MMSS surfaces a continuity loss with a persistent indication
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    And the ECG monitor is acquiring with Heart Rate 82 bpm in the simulator
    When the simulator injects a 2 second monitoring interruption during the transfer
    Then a persistent, salient continuity-loss indication is shown within 1 second of the interruption
    And the indication persists until the user acknowledges it
```

```gherkin
@ID:RQ_FN_22
Feature: Identity Match-and-Confirm Gate Before Share
    As a clinician I want a mandatory identity and destination match-and-confirm before any share
    So that clinical data is never attached to the wrong patient or facility

Rule: The MMSS shall, before any share to the Hospital Information System, require a mandatory patient-identity and destination match-and-confirm step displaying the identifiers for the clinician to match, and shall block the share on an identifier mismatch.

Scenario: MMSS requires identity match-and-confirm before sharing
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    And the active patient identity is the following
    | patient id  | name        | destination facility |
    | PT-100294   | J. Doe      | HIS-WardA            |
    When the user initiates a share to the Hospital Information System
    Then the MMSS displays the patient and destination identifiers for matching
    | patient id  | destination facility |
    | PT-100294   | HIS-WardA            |
    And the share does not proceed until the user confirms the match

Scenario: MMSS blocks the share on an identifier mismatch
    Given the simulator is running
    And a share to the Hospital Information System has been initiated for patient "PT-100294"
    When the destination record resolves to a different patient "PT-559001"
    Then the MMSS blocks the share
    And a mismatch indication is shown
    And no data is transmitted to the Hospital Information System
```

```gherkin
@ID:RQ_FN_23
Feature: Provenance-Preserving Share to HIS
    As a clinician I want vital signs and findings shared to the HIS with provenance and timestamp, and failures made visible
    So that continuity of care is trustworthy and no share is silently dropped

Rule: The MMSS shall share monitored vital signs and diagnostic findings to the Hospital Information System over the standard interoperability protocol, preserving each item's provenance and timestamp, and shall surface a failure rather than silently dropping the share when the HIS is unreachable.

    # covers: RQ_NF_10, RQ_IF_09, RQ_IF_10, RQ_CS_07, RQ_PR_11
Scenario: MMSS shares data preserving provenance and timestamp
    Given the simulator is running
    And the identity match-and-confirm gate has been passed
    And the Hospital Information System is reachable
    When the user confirms the share
    Then the following items are transmitted over the standard interoperability protocol within 1 second
    | item                  | provenance     | timestamp           |
    | Heart Rate 82 bpm     | ECG monitor    | 2026-06-11T10:15:03Z |
    | SpO2 97 %             | Pulse Oximeter | 2026-06-11T10:15:03Z |
    | diagnostic finding    | AI service     | 2026-06-11T10:15:01Z |
    And each transmitted item preserves its source provenance
    And each transmitted item preserves its timestamp

Scenario: MMSS surfaces a share failure when the HIS is unreachable
    Given the simulator is running
    And the identity match-and-confirm gate has been passed
    And the Hospital Information System is unreachable
    When the user confirms the share
    Then an explicit share-failure indication is shown within 1 second
    And the share is not silently dropped
```

```gherkin
@ID:RQ_FN_24
Feature: Privacy and Security of Displayed and Shared Data
    As a patient I want my personal and clinical data protected in display and sharing, with protected transport
    So that my data is handled lawfully and securely

Rule: The MMSS shall protect personal and clinical data it displays and shares in conformity with applicable privacy and information-security obligations, including protected transport for shared data.

    # covers: RQ_NF_09, RQ_CS_10
Scenario: MMSS uses protected transport for shared data
    Given the simulator is running
    And the identity match-and-confirm gate has been passed for patient "PT-100294"
    When the user confirms a share to the Hospital Information System
    Then the transport channel is authenticated and TLS-encrypted
    And a network capture of the share contains no patient identifiers in clear text

Scenario: MMSS refuses to share when an encrypted channel cannot be established
    Given the simulator is running
    And the identity match-and-confirm gate has been passed for patient "PT-100294"
    When the simulator forces the transport to downgrade to an unencrypted channel
    Then the share is blocked
    And no patient data is transmitted in clear text
```

```gherkin
@ID:RQ_FN_25
Feature: Guarded, Clearly Indicated Simulation/Training Mode
    As a clinician I want a self-contained training mode with a guarded entry/exit and a persistent indication on every screen
    So that I can build competence without patient exposure and never confuse simulated data with live monitoring

Rule: The MMSS shall provide a self-contained simulation/training mode that reproduces monitoring, alarms, and diagnostic candidates against simulated data without a live patient, entered and exited only through a guarded action, and shall display a persistent, unmistakable training-mode indication on every screen.

Scenario: MMSS enters training mode only through a guarded action
    Given the simulator is running
    And the MMSS is in live monitoring
    When the user requests entry to training mode
    Then the MMSS requires a guarded action to confirm entry
    And training mode is entered only after the guarded action is completed

    # covers: RQ_NF_12, RQ_CS_11
Scenario: MMSS shows a persistent training-mode indication on every screen
    Given the simulator is running
    And the MMSS is in training mode
    When the user navigates across the following screens
    | screen      |
    | monitoring  |
    | alarms      |
    | diagnostics |
    Then a persistent, unmistakable training-mode indication is shown on every screen

Scenario: Training mode reproduces monitoring, alarms, and diagnostics on simulated data
    Given the simulator is running
    And the MMSS is in training mode with no live patient
    And the Heart Rate safe limit is configured to 120 bpm
    When the simulated data drives the Heart Rate to 150 bpm
    Then a simulated Heart Rate alarm is reproduced against the simulated data
    And simulated diagnostic candidates are presented
    And the training-mode indication remains shown throughout

Scenario: MMSS exits training mode only through a guarded action
    Given the simulator is running
    And the MMSS is in training mode
    When the user requests exit from training mode
    Then the MMSS requires a guarded action to confirm exit
    And live monitoring resumes only after the guarded action is completed
```

```gherkin
@ID:RQ_FN_26
Feature: Authorised Acquisition-Source Configuration
    As a super-user I want to configure and manage acquisition sources across the installed base, with incompatible variants rejected with guidance
    So that the product is deployable and maintainable without replacing equipment

Rule: The MMSS shall allow an authorised super-user to configure and manage acquisition sources from the installed-base devices through the standardised interfaces, tolerating make/model/firmware variation and explicitly rejecting an incompatible variant with guidance.

Scenario: Authorised super-user configures a supported acquisition source
    Given the simulator is running
    And the user is an authorised super-user
    When the super-user configures the following supported device variant through the standardised interface
    | device         | make     | model   | firmware |
    | Pulse Oximeter | Vendor-A | A-200   | 2.1.0    |
    Then the source is added and shown as configured
    And the source begins acquiring within 1 second

Scenario: MMSS rejects an incompatible variant with guidance
    Given the simulator is running
    And the user is an authorised super-user
    When the super-user attempts to configure the following incompatible device variant
    | device         | make     | model   | firmware |
    | Pulse Oximeter | Vendor-A | A-200   | 0.4.0    |
    Then the MMSS explicitly rejects the variant
    And guidance naming the incompatible firmware is shown

Scenario: MMSS blocks source configuration by an unauthorised user
    Given the simulator is running
    And the user is not an authorised super-user
    When the user attempts to configure an acquisition source
    Then the configuration action is blocked
```

```gherkin
@ID:RQ_FN_27
Feature: Predictable Update and Serviceability Cadence
    As a service owner I want a defined update cadence with predictable, communicated availability impact
    So that monitoring availability and lifecycle cost stay defensible

Rule: The MMSS shall support a defined update and serviceability cadence and make the availability impact of a pending update predictable and communicated to the user.

Scenario: MMSS communicates the availability impact of a pending update
    Given the simulator is running
    And a software update is pending with the following metadata
    | version  | expected downtime | monitoring affected |
    | 2.3.0    | 90 seconds        | yes                 |
    When the user views the pending update
    Then the MMSS shows the expected downtime "90 seconds"
    And the MMSS states that monitoring is affected during the update

    # covers: RQ_NF_13
Scenario: MMSS makes the update follow the defined serviceability cadence
    Given the simulator is running
    And a software update version "2.3.0" is pending with a communicated 90 second downtime
    When the update is scheduled and applied in the simulator
    Then the actual downtime does not exceed the communicated 90 seconds
    And the update completes within the defined serviceability cadence
```

```gherkin
@ID:RQ_FN_28
Feature: Error-Tolerant One-Handed Operation
    As an operator I want reliable one-handed, error-tolerant operation with confirm-on-release and reversible destructive actions
    So that a mis-tap never dismisses an alarm or changes a setting unintentionally

Rule: The MMSS shall support reliable one-handed, error-tolerant operation — reading values, acknowledging an alarm, and switching view — using large, well-spaced targets and confirm-on-release, and shall make destructive actions confirmed or reversible so a mis-tap neither dismisses an alarm nor changes a setting unintentionally.

    # covers: RQ_PR_14, RQ_IF_11
Scenario: MMSS supports one-handed core actions with confirm-on-release
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    When the operator performs the following one-handed actions
    | action            |
    | read a value      |
    | acknowledge alarm |
    | switch view       |
    Then each action completes with confirm-on-release feedback within 1 second

Scenario: A mis-tap does not dismiss an alarm
    Given the simulator is running
    And the simulator has driven the SpO2 to 82 % raising a high-priority alarm
    When the operator presses the alarm-acknowledge control but releases 20 px off-target
    Then the alarm is not dismissed
    And the alarm remains annunciated

Scenario: A destructive action is confirmed or reversible
    Given the simulator is running
    And the MMSS is in the "VALID — LIVE" state
    And the Heart Rate safe limit is configured to 120 bpm
    When the operator initiates a destructive action that would change the Heart Rate safe limit to 200 bpm
    Then the MMSS requires confirmation or makes the action reversible
    And the Heart Rate safe limit remains 120 bpm until the action is confirmed
```

```gherkin
@verification:by-review
Feature: Process and Compliance Verification by Technical-File Review
    As the verification lead I want the process, compliance, and lifecycle requirements verified by document and technical-file review
    So that requirements not observable at the runtime device boundary are still demonstrably covered

Rule: Requirements verified by inspection/analysis/audit of the design history file rather than by executable scenarios at the runtime device boundary.

    # covers: RQ_CS_04
Scenario: Host platform and no-hardware-modification constraint verified by configuration review
    Given the design and build configuration records for the MMSS
    When the technical file is reviewed against the host-platform constraint
    Then the records show the MMSS executes on the specified fixed RTOS-capable embedded host platform with no hardware modification

    # covers: RQ_CS_09
Scenario: IEC 62366-1 usability-engineering conformity verified by standards-conformance review
    Given the usability-engineering file and user-interface design records for the MMSS
    When the technical file is reviewed against IEC 62366-1
    Then the records show the user-interface design and validation conform to IEC 62366-1

    # covers: RQ_NF_01
Scenario: IEC 62304 software life-cycle conformity verified by process audit
    Given the software life-cycle process records and the assigned software safety class for the MMSS
    When the design history file is audited against ANSI/AAMI/IEC 62304
    Then the records show the software was developed, verified, and maintained under a class-appropriate conforming life-cycle process

    # covers: RQ_NF_02
Scenario: Auditable requirement-to-evidence traceability verified by design-history-file review
    Given the version-controlled traceability records for the MMSS
    When the design history file is reviewed for traceability completeness
    Then each requirement traces to its risk controls, design, and verification evidence and the trace is reproducible on demand for external audit

    # covers: RQ_NF_03
Scenario: ISO 14971 risk management file verified by review before release
    Given the risk management file for the MMSS
    When the file is reviewed against ISO 14971 before market release
    Then the file documents the hazard analysis, implemented risk controls, and a justified acceptable residual risk

    # covers: RQ_NF_05
Scenario: SOUP qualification verified by technical-file review
    Given the software-of-unknown-provenance qualification records including the commercially supplied AI diagnostic model
    When the technical file is reviewed against the IEC 62304 SOUP requirements
    Then each SOUP item has documented version identification, performance characterisation, provenance, and risk assessment

    # covers: RQ_NF_06
Scenario: Clinical evidence for diagnostic support verified by review before market entry
    Given the clinical evidence records substantiating the MMSS diagnostic-support performance
    When the evidence is reviewed before market entry
    Then the records characterise the diagnostic-support performance, ranking-convergence behaviour, and bounded boundary-observable inference latency

    # covers: RQ_NF_07
Scenario: IEC 62366-1 usability engineering of use-related hazards verified by review
    Given the usability-engineering records for the MMSS
    When the records are reviewed against IEC 62366-1
    Then the records validate that use-related hazards including clinician misinterpretation of ranked diagnostic candidates are mitigated under representative use conditions

    # covers: RQ_NF_11
Scenario: Labelling and instructions-for-use accuracy verified by review
    Given the labelling and instructions-for-use for the MMSS
    When the labelling is reviewed against the validated scope of the device
    Then the labelling accurately states the intended use, indications, contraindications, residual risks, the limitations of the AI diagnostic support, and the required user training and qualifications

    # covers: RQ_NF_14
Scenario: Post-market surveillance arrangements verified by process review
    Given the post-market surveillance process records for the MMSS
    When the process is reviewed against the post-market surveillance obligation
    Then the records establish a defined post-market surveillance process for the deployed device

    # covers: RQ_NF_15
Scenario: Scalable deployment without re-validation verified by configuration review
    Given the deployment and configuration-management records for the MMSS
    When the records are reviewed against the scalable-deployment constraint
    Then the records show deployment across the target markets and supported device configurations occurs without re-validation of unchanged safety- and conformity-relevant software

    # covers: RQ_NF_16
Scenario: End-of-life and secure-disposal behaviour verified by review
    Given the end-of-life and decommissioning records for the MMSS
    When the records are reviewed against the end-of-life obligation
    Then the records define secure disposal of residual personal data and an orderly, documented withdrawal of deployed units
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
