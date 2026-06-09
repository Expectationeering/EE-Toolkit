# Mobile Monitor for Critical Care

AI Driven Diagnostic Support

Project Description

![A paramedic examining a patient Description automatically generated](media/image1.jpeg){width="4.229166666666667in" height="3.375in"}

Mobile Monitoring Software Solution (MMSS)

Date: 2026-03-02

# 1. Project Overview

## 1.1 Purpose

The purpose of the MMSS project is to develop medical device software that transforms an existing portable patient monitor from a passive vital signs display into an active clinical decision-support tool. By integrating an AI-driven diagnostic engine into the monitoring software, MMSS enables clinicians --- particularly in pre-hospital and mobile care settings --- to receive ranked, real-time diagnostic candidates alongside raw vital signs data, converging to a predictive diagnosis within two minutes of patient connection.

The software acquires data from a defined set of non-invasive measurement devices through standardised interfaces, processes it through an AI analysis engine, presents vital signs and diagnostic output on a connected monitor display, generates clinical alarms for abnormal conditions and sensor faults, and optionally shares data with hospital information systems. The project delivers the complete MMSS software stack --- from device acquisition through AI processing to user presentation and hospital integration --- as a regulated medical device software product compliant with IEC 62304.

# 2. Scope

This project covers software development only. No hardware development, hardware modification, or hardware procurement is in scope. All physical components --- the host CPU platform, measurement devices (ECG monitor, pulse oximeter, blood pressure monitor, thermal probe, capnometer, EEG monitor), monitor display, and physical enclosure --- are treated as existing, fixed elements. MMSS interfaces with these components through defined interface control documents; their internal design and physical characteristics are outside the scope of this project.

**[In scope:]{.underline}**

- Application software only --- all five software items: AC, DAC, DEC, DPREC, DPROC

- Interfacing with the external Open Evidence AI library

- The AI model is used as a commercially validated off-the-shelf component

- Drivers and polling logic for the six measurement device types

- Vital signs display, alarm presentation, and diagnostic candidate rendering

- Hospital information system integration for second opinion

**[Out of scope:]{.underline}**

- Hardware design, selection, or modification of any physical component

- Device behavior is fixed and accessed through published interfaces

- Physical enclosure, portability, weight, or battery design

# 3. Intended Use and Classification

## 3.1 Intended Use

The Mobile Monitor for critical care is intended to provide a comprehensive, real-time monitoring solution for critically ill patients. Its primary purpose is to ensure continuous tracking of key vital signs and offer diagnostic support through advanced technologies such as Artificial Intelligence (AI). The Mobile Monitor is portable, user-friendly, and non-invasive to provide maximum efficiency and comfort in various critical care environments, including intensive care units (ICU), emergency rooms, and mobile medical units. The Smart Mobile Monitor is intended to be used by trained medical professionals.

## 3.2 Medical Device Classification

  -----------------------------------------------------------------------------------------------------
  Field                 Value
  --------------------- -------------------------------------------------------------------------------
  Standard              IEC 62304

  Initial Class         Class C --- Failing software may result in death of the patient

  After Mitigation      Class B --- Alarming and diagnosis functions mitigated to independent systems
  -----------------------------------------------------------------------------------------------------

# 4. Product Context

![](media/image2.png){width="6.2in" height="4.522579833770779in"}

# 5. System Requirements

  -----------------------------------------------------------------------------
  Requirement                               Target
  ----------------------------------------- -----------------------------------
  System Activation                         \< 10 seconds

  Vital Signs Display                       \< 1 second after acquisition

  Vital Sign Alarm Display                  \< 1 second after detection

  Connection Alarm Trigger                  5 seconds of inactivity

  Connection / Misplacement Alarm Display   \< 1 second after trigger

  Diagnose Candidates Display               \< 1 second after receipt from AI

  Diagnose Candidates → HIS                 \< 1 second

  DPROC latency budget                      ≤ 200 ms

  DPREC latency budget                      ≤ 800 ms

  DEC latency budget                        ≤ 800 ms

  Diagnosis Convergence (ALGOS)             2 minutes maximum

  Vital Signs Input Rate                    ≥ 0.1 Hz

  UI Update Interval                        1 second (timer-based)
  -----------------------------------------------------------------------------

# 6. Constraints and Assumptions

  ---------------------------------------------------------------------------------------------------------------------
  Type           Statement
  -------------- ------------------------------------------------------------------------------------------------------
  Constraint     First release must use commercially available validated AI model (Open Evidence) --- no custom model

  Constraint     Software must comply with ANSI AAMI IEC 62304 as Class C (mitigated to B)

  Constraint     Must support 6 device types: ECG, Pulse Oximeter, BP Monitor, Thermal Probe, Capnometer, EEG

  Constraint     2-minute diagnosis convergence is an ALGOS budget --- not an MMSS budget

  Constraint     MMSS display latency budget is 1 second (DPREC ≤ 800 ms, DPROC ≤ 200 ms)

  Assumption     Clinician users are trained medical professionals

  Assumption     Host system is a compact embedded CPU with real-time OS capabilities

  Assumption     Open Evidence provides structured diagnose candidates to MMSS

  Assumption     HIS interface protocol TBD (HL7/FHIR) --- ICDs to be defined

  Assumption     ALGOS sends audible notification independently on 2-minute timeout --- no residual MMSS risk
  ---------------------------------------------------------------------------------------------------------------------

# 7. Risk Register

  ---------------------------------------------------------------------------------------------------------------------------------------------------------------
  ID     Risk                                                      Prob.    Impact     Mitigation
  ------ --------------------------------------------------------- -------- ---------- --------------------------------------------------------------------------
  R_01   AI algorithm regulatory clearance delays                  Medium   High       Use commercially validated Open Evidence model; engage regulatory early

  R_02   AI model validation complexity                            High     High       Off-the-shelf validated model mandated for v1.0

  R_03   Connectivity / real-time integration challenges           High     High       Prototype early; prioritise ICD definition for external interfaces

  R_04   Sensor misplacement not detected → wrong diagnosis        Medium   Critical   DEVICES must auto-detect misplacement

  R_05   Clinician misinterpretation of AI candidates              Medium   Critical   Mandatory simulation training mode in MMSS; hands-on training

  R_06   Diagnosis timeout not communicated → delay of treatment   Low      Critical   ALGOS and MMSS both notify on 2-minute timeout

  R_07   Connection failure not detected → missed vital signs      Low      Critical   DEVICES generate independent audible alarms; MMSS shows connection alarm

  R_08   Portability targets exceed budget                         Medium   Medium     Confirm hardware platform weight/size targets early
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------
