# Flow Orchestration Upgrade — Design

**Date:** 2026-08-05
**Branch:** SuperPowers
**Status:** Approved by Eric (design dialogue, 2026-08-05)
**Roadmap:** sub-project 3 of the superpowers adoption (after skills
hardening); the "working agreements" sub-project remains open.

## Goal

Integrate superpowers orchestration patterns into `execute-flow` and close
the parked follow-ups, serving four goals Eric selected: more robust runs,
a better end product, token efficiency, and cleanup. One integrated spec,
validated by a single full ee-flow run.

## 1. Robustness contracts (verification-before-completion in the run)

`execute-flow` gains three explicit contracts:

- **Paste verification.** After every paste the orchestrator deterministically
  checks that (a) the surrounding headings/sections are intact and (b) the
  pasted section contains no template placeholders the step was supposed to
  fill. Only then may the step's todo item be marked completed.
- **Agent failure protocol.** An agent that returns empty, malformed, or
  out-of-scope content gets exactly one re-dispatch with a clarified prompt.
  If that also fails, the run stops and surfaces the failure. The
  orchestrator never authors artefact content itself as a fallback.
- **Evidence before claim.** The existing per-phase trace-check and QA loop
  remain; the rule "a step is complete only when its evidence exists" becomes
  the explicit form of the procedure, not an implicit habit.

## 2. Challenger on the safety-critical chain

New orchestration pattern: after the co-author round of artefact groups with
Classification **Critical/Major** and the FMEA chain (steps 6d–6i, plus
resulting USR/RQ rows classified Critical), the orchestrator spawns one
**challenger agent per artefact group** — with scoped context and the
relevant skill bodies — whose mandate is to refute the artefact: missing
failure modes, unverifiable mitigations, unsupported severity ratings.
Findings go back to the owning author as a correction request **before** the
QA audit runs; the challenger writes nothing itself. This is the superpowers
adversarial-verify pattern, applied where defects are most expensive.

## 3. Token efficiency: model differentiation + context dedup

- **Per-step model override.** `flow.md` gains an optional model designation
  per step (metadata/steps column). `execute-flow` reads it generically and
  passes it as the agent's model override; the default remains the session
  model, so future flows (rte-flow) inherit the mechanism unchanged. The
  initial assignment for ee-flow (which steps run on a cheaper model) is
  decided in the plan phase from the per-step token figures in the existing
  run-stats.
- **GS-4 lands here.** The Verification blurb in
  `templates/expectationeering-workbook.md` is collapsed to a pointer to the
  `gherkin-sv` skill, so 3-Amigos steps stop receiving that text twice.

## 4. Follow-ups

- Retag `templates/Example.feature` from `@ID:PR_02.1` to the
  `@ID:RQ_FN_xx` convention (kills the GS-2 trap at the root); drop any
  now-unneeded caveat wording in `gherkin-sv`.
- Remove the sentence in `.claude/agents/quality-assurance.md` that
  duplicates the injected requirements-quality body ("Tag each finding with
  the violated criterion by name").
- Soften install-toolkit's completion line to "run the flow, e.g.
  `Execute flows/ee-flow`".

## Validation

- Every orchestration change gets cheap micro-tests first (RED/GREEN with
  single-shot subagents, as in the skills-hardening sub-project).
- The sub-project closes with **one full ee-flow validation run**.
  Acceptance: QA audit reaches PASS, trace-check clean at close, and
  run-stats compared against the 2026-07-04 baseline (total tokens,
  wall-clock, QA passes). Expectation: efficiency gains visible; challenger
  cost visible and justified by findings caught before QA.

## Error handling

If the validation run fails on a new mechanism: revert or fix that
mechanism and re-validate only the affected part — no second full run
without Eric's approval. All work on the `SuperPowers` branch.

## Out of scope

The "working agreements" sub-project (superpowers workflows for developing
the toolkit itself, in CLAUDE.md); authoring the rte-flow itself;
description changes deferred at the hardening gate (RQ-3, GS-8).

## Success criteria

- The three robustness contracts and the challenger pattern are in
  `execute-flow` and micro-tested.
- Model-override mechanism works generically; ee-flow carries an initial
  assignment justified by baseline run-stats.
- All four follow-ups closed.
- Validation run passes acceptance; run-stats comparison documented in the
  run's output folder and referenced from the audit trail.
