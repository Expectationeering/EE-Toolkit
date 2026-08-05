# Flow Orchestration Upgrade Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. **Exception:** every task dispatches micro-test subagents and Task 5 runs a full flow — run all tasks inline in the main session.

**Goal:** Integrate superpowers orchestration patterns (robustness contracts, adversarial challenger, per-step model overrides) into `execute-flow`, close the four parked follow-ups, and prove everything with one full ee-flow validation run.

**Architecture:** All orchestration changes land in `.claude/skills/execute-flow/SKILL.md`; the model-override mechanism is generic (read from `flow.md`), with ee-flow's assignment in `flows/ee-flow/flow.md`; GS-4 and the Example.feature retag touch `templates/`; two one-line follow-ups touch `quality-assurance.md` and `install-toolkit`. Task 5 is the expensive acceptance gate.

**Tech Stack:** Claude Code Agent tool, Grep/Edit, `scripts/check_traces.py`, single-shot haiku subagents for micro-tests.

**Spec:** `docs/superpowers/specs/2026-08-05-flow-orchestration-design.md` (approved 2026-08-05).

## Global Constraints

- Iron Law: every substantive orchestration change gets a failing micro-test BEFORE the edit (RED), and a passing rerun after (GREEN). Micro-tests: single-shot `claude` subagents on haiku, no tools, fresh context; 2–3 reps; read every rep yourself. Baseline not reproduced → no edit, record "not reproduced".
- The full ee-flow run happens ONCE, in Task 5, after all micro-tests are green. No trial runs.
- Model overrides never change the default: a step without a `Model` value runs on the session model.
- The challenger writes nothing — findings go to the owning author (return-content; orchestrator pastes).
- One commit per task; commit messages end with `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>`. All work on `SuperPowers`.
- Windows/PowerShell; venv Python is `.venv\Scripts\python.exe`.
- Baseline for comparison: `outputs/2026-07-04-170434/run-stats.md` — ≈1,890,000 subagent tokens, 44 invocations, wall-clock ≈63 min, 2 QA passes (34 findings round 1).

---

### Task 1: Robustness contracts in execute-flow

**Files:**
- Modify: `.claude/skills/execute-flow/SKILL.md` (return-content block; step 4 opening)

**Interfaces:**
- Produces: the paste-verification contract and the agent-failure protocol that Task 5's run must observe; Task 2's challenger reuses the same re-dispatch mechanics ("one clarified re-dispatch, then stop").

- [ ] **Step 1: RED — micro-test the two failure modes (2 reps each, haiku, no tools)**

Scenario R1 (failure protocol): "You are the flow orchestrator. The step-6d agent returned an empty message after 90 s. The run is mid-flow and you are under time pressure. Current skill text: *'Each agent returns its filled (or improved) section(s) as markdown in its final message. You — the orchestrator — paste each returned section into the live workbook.'* What exactly do you do next? Max 3 numbered steps." **Failure = any rep authors the FMEA rows itself, skips the step, or retries more than once without stopping.**

Scenario R2 (paste verification): "You are the flow orchestrator. You just pasted the step-5a section into the workbook. The pasted text still contains the template placeholder row `| IF_01 | | | |` that step 5a was supposed to fill, but the surrounding headings look fine. Your todo list has step 5a as in_progress. Current skill text: *'Paste the returned section(s) in-place, preserving all surrounding headings, tables, and sections.'* What do you do with the todo item and the placeholder? Answer in 2 sentences." **Failure = any rep marks 5a completed with the placeholder still present.**

Save verbatim outputs to `<scratchpad>/microtest-ORCH-R.md`. If neither scenario fails in any rep, mark both contracts "not reproduced" in the commit message and skip Steps 2–3 for the non-reproduced one.

- [ ] **Step 2: Apply the contracts**

In the return-content blockquote, append after "After each paste, confirm the surrounding headings and sections are untouched.":

```
> **Paste verification — before marking the step's todo completed:** (a) the surrounding headings and neighbouring sections are byte-identical; (b) the pasted section contains no unfilled template placeholder the step was assigned to fill (empty stub rows, `<!-- -->` fill-in comments). Placeholder still present → the step is not done: re-dispatch per the failure protocol below, do not mark completed.
>
> **Agent failure protocol.** An agent that returns empty, malformed, or out-of-scope content (wrong section, prose instead of the table) gets exactly **one** re-dispatch with a clarified prompt naming the defect. If the re-dispatch also fails, stop the run and surface the step, the prompt, and both returns in your final message. Never author artefact content yourself as a fallback, and never skip the step.
```

- [ ] **Step 3: GREEN — rerun R1 and R2 with the new text in the quoted skill excerpt**

Expected: R1 reps re-dispatch once then stop-and-report (no self-authoring); R2 reps refuse to mark completed and re-dispatch. 2/2 each.

- [ ] **Step 4: Reference check + commit**

Grep `execute-flow` body still cites `trace-check`, `gherkin-sv`, `requirements-quality`, `fmea` (injection table intact).

```powershell
git add .claude/skills/execute-flow/SKILL.md
git commit -m @'
Add robustness contracts to execute-flow (paste verification, agent failure protocol)

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
'@
```

---

### Task 2: Challenger on the safety-critical chain

**Files:**
- Modify: `.claude/skills/execute-flow/SKILL.md` (new subsection under "Co-author, gates, and audit modes")

**Interfaces:**
- Consumes: Task 1's failure protocol (re-dispatch mechanics).
- Produces: the `Challenger` mode Task 5's run executes after steps 6e, 6j, and 9e.

- [ ] **Step 1: RED — micro-test challenger drift (2 reps, haiku, no tools)**

Scenario C1: give the rep the role "adversarial challenger of a USER_DFMEA table", one filled USER_DFMEA row (use the worked row from the fmea skill), and the instruction *"Challenge this analysis."* — nothing more. **Failure = the rep rewrites/improves the row or returns a corrected table instead of findings-only.** (This establishes that without an output contract the challenger drifts into authoring — the defect the mode's contract must prevent.)

Save to `<scratchpad>/microtest-ORCH-C.md`. Not reproduced → record it, still perform Step 2 in full (the mode is new spec-mandated functionality, not a defect fix; the RED test only calibrates the anti-drift clause), and skip Step 3.

- [ ] **Step 2: Add the Challenger mode**

Insert into `.claude/skills/execute-flow/SKILL.md` under `## Co-author, gates, and audit modes`, after the **Gates** bullet:

```
- **Challenger (safety-critical chain).** After the listed step completes (co-author round included), spawn one adversarial challenger for the group, with scoped context (the group's section + its direct upstream sections) and the skill bodies per the injection table:
  | After step | Challenger examines | Agent |
  |---|---|---|
  | 6e | USER_DFMEA table | quality-assurance |
  | 6j | UFMEA table + USR_* rows | quality-assurance |
  | 9e | all RQ_* rows with Classification Critical or Major | quality-assurance |
  The challenger's mandate is to **refute**: missing failure modes for covered URs/UTs, causes restating the mode, unverifiable or training-only mitigations, severity ratings unsupported by the stated end-effect, Critical/Major RQ rows failing the ten criteria. It returns a findings list tagged with the owning Role, or PASS — **it returns no corrected content and no rewritten rows**. Route findings to the owning author as one correction request (return-content; you paste), re-run trace-check if traces changed, and continue — challenger findings get **one** remediation round; anything still disputed flows into the step-10 QA audit rather than looping. Cap: one challenger invocation per group per run.
```

- [ ] **Step 3: GREEN — rerun C1 with the mode's mandate text in context**

Give the rep the same row plus the mandate sentence ("It returns a findings list … no corrected content and no rewritten rows"). Expected: findings-only output, 2/2.

- [ ] **Step 4: Commit**

```powershell
git add .claude/skills/execute-flow/SKILL.md
git commit -m @'
Add challenger mode for the safety-critical chain to execute-flow

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
'@
```

---

### Task 3: Per-step model overrides + GS-4 context dedup

**Files:**
- Modify: `.claude/skills/execute-flow/SKILL.md` (step 3 spawn rule)
- Modify: `flows/ee-flow/flow.md` (Steps table: new `Model` column on selected rows)
- Modify: `templates/expectationeering-workbook.md` (Verification blurb)

**Interfaces:**
- Consumes: baseline per-step tokens from `outputs/2026-07-04-170434/run-stats.md`.
- Produces: the `Model` column contract Task 5's run applies.

- [ ] **Step 1: RED — micro-test the default (2 reps, haiku, no tools)**

Scenario M1: "You are the flow orchestrator. The flow.md Steps table has a `Model` column; the row for step 6d has an empty Model cell, the row for step 1a says `sonnet`. Skill text: *'spawn the assigned specialist agent (`subagent_type` matching the role)'* — nothing about models. Which model do you pass for step 6d and which for step 1a?" **Failure = any rep invents a model for 6d (anything other than 'the session default / none') or ignores 1a's value.** Save to `<scratchpad>/microtest-ORCH-M.md`.

- [ ] **Step 2: Add the override rule to execute-flow step 3**

Extend the spawn sentence: after "spawn the assigned specialist agent (`subagent_type` matching the role)" insert:

```
 — if the step's row in flow.md has a `Model` value, pass it as the agent's model override; no value (or no `Model` column) = the session model —
```

- [ ] **Step 3: Add the `Model` column to ee-flow's Steps table**

Add a `Model` column header to the table in `flows/ee-flow/flow.md` (empty cell = session model). Set `sonnet` on exactly these rows, chosen from the baseline stats (persona-voiced list authoring and checklist-driven review passes, all downstream-guarded by 1e consolidation, co-authors, challenger, and the QA loop):

| Step | Baseline tokens | Rationale |
|---|---|---|
| 1a, 1b, 1c, 1d | 26.9k / 27.1k / 28.3k / 28.0k | persona-voiced expectation lists; 1e (session model) consolidates |
| 6c | 29.6k | UR validation review with the full-model author output in hand |
| 6g | 38.0k | Use-scenario review, checklist-driven |
| 8c | 29.3k | UC review, checklist-driven |

All FMEA, RQ, 3-Amigos, QA, and consolidation steps keep the session model. Expected saving ≈207k baseline tokens moved to the cheaper tier.

- [ ] **Step 4: GS-4 — collapse the template's Verification blurb**

In `templates/expectationeering-workbook.md`, replace the paragraph at ~line 311 ("The **BDD feature files** that verify the functional requirements, defined jointly by the 3-Amigos … one row (`SV_*`) in the workbook's Verification table.") with:

```
The **BDD feature files** that verify the functional requirements, defined jointly by the 3-Amigos (Product Owner, Development Lead, Verification Lead). Format, tagging, indentation, and coverage rules: the `gherkin-sv` skill (injected into the authoring steps) is the single source. The converter records each feature file as one `SV_*` row in the workbook's Verification table.
```

Keep the `@ID:RQ_FN_01` example block below it unchanged.

- [ ] **Step 5: GREEN — rerun M1 with the new spawn sentence quoted**

Expected: 6d → session model, 1a → sonnet, 2/2.

- [ ] **Step 6: Verify + commit**

Run `.venv\Scripts\python.exe scripts\check_traces.py "templates/expectationeering-workbook.md" --json` — confirm the template edit introduced no new *structural* damage relative to the pristine-template baseline (the stub-row errors are expected per the trace-check skill; compare finding count before/after the edit — must be identical).

```powershell
git add .claude/skills/execute-flow/SKILL.md flows/ee-flow/flow.md templates/expectationeering-workbook.md
git commit -m @'
Add per-step model overrides (generic mechanism + ee-flow assignment) and GS-4 dedup

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
'@
```

---

### Task 4: Follow-ups (Example.feature retag, QA-agent dedup, install-toolkit wording)

**Files:**
- Modify: `templates/Example.feature:1`
- Modify: `.claude/skills/gherkin-sv/SKILL.md` (only if a caveat about the old tag exists — currently none expected)
- Modify: `.claude/agents/quality-assurance.md:21`
- Modify: `.claude/skills/install-toolkit/SKILL.md` (completion line d)

**Interfaces:**
- Produces: a convention-consistent reference file that Task 5's 3-Amigos steps may follow verbatim.

- [ ] **Step 1: Retag Example.feature**

Change line 1 of `templates/Example.feature` from `@ID:PR_02.1` to `@ID:RQ_FN_02.1` (keeps the sub-index demonstration, adopts the mandated `RQ_FN` prefix). Deterministic verification: `Select-String -Path templates\Example.feature -Pattern '@ID:'` shows exactly one tag, `@ID:RQ_FN_02.1`. Grep the repo's live files (`CLAUDE.md`, `.claude/**`, `flows/**`, `templates/**`, `scripts/**`) for `PR_02` — zero remaining hits.

- [ ] **Step 2: Check gherkin-sv for stale caveats**

Grep `.claude/skills/gherkin-sv/SKILL.md` for `PR_02` and `predates` — expected zero hits (GS-2's caveat was never applied). If a hit appears, delete that clause.

- [ ] **Step 3: Remove the duplicated sentence from quality-assurance.md**

In `.claude/agents/quality-assurance.md:21`, delete the final sentence "Tag each finding with the violated criterion by name." (it survives in the injected requirements-quality body's Audit usage section). The line keeps its pointer to the skill as single source.

- [ ] **Step 4: Soften install-toolkit's completion line**

In `.claude/skills/install-toolkit/SKILL.md`, change "(d) next step: no terminal restart needed — run `Execute flows/ee-flow` now." to "(d) next step: no terminal restart needed — run a flow now, e.g. `Execute flows/ee-flow`."

- [ ] **Step 5: Commit**

All three are deterministic content corrections (tag convention, verbatim-duplicate removal, example wording) — no micro-tests per the structural-only rule.

```powershell
git add templates/Example.feature .claude/agents/quality-assurance.md .claude/skills/install-toolkit/SKILL.md
git commit -m @'
Close parked follow-ups: retag Example.feature, dedup QA agent line, generalize install-toolkit next step

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
'@
```

(Include `.claude/skills/gherkin-sv/SKILL.md` in the add only if Step 2 changed it.)

---

### Task 5: Full ee-flow validation run

**Files:**
- Create: `outputs/<date>-<time>/` (workbook, .docx, run-stats.md, comparison note)

**Interfaces:**
- Consumes: everything from Tasks 1–4.
- Produces: the acceptance evidence for the whole sub-project.

- [ ] **Step 1: Pre-flight**

`git status --short` clean except `.claude/settings.local.json`; `inputs/` contains the primary `.docx`; `.venv\Scripts\python.exe scripts\check_traces.py --help`-style sanity: run it against `outputs/2026-07-04-170434/Project_Description_Workbook.md`, expect exit 0.

- [ ] **Step 2: Execute the flow**

Run `Execute flows/ee-flow` per the updated `execute-flow` skill — with the three new mechanisms live: paste verification + failure protocol (Task 1), challengers after 6e/6j/9e (Task 2), model overrides for 1a–1d/6c/6g/8c (Task 3). Observe the skill exactly; deviations are findings, not improvisations.

- [ ] **Step 3: Acceptance checks**

(a) QA audit final verdict PASS, zero findings; (b) trace-check exit 0 on the finished workbook; (c) .docx produced by the convert command; (d) run-stats.md written per the skeleton, including wall-clock and the challenger invocations as Per-step rows.

- [ ] **Step 4: Baseline comparison**

Append to the new run's `run-stats.md` a `## Comparison vs 2026-07-04 baseline` section: total tokens (baseline ≈1,890,000), invocations (44), wall-clock (≈63 min), QA passes (2) and findings (34), challenger cost and findings caught before QA, tokens on the sonnet tier vs the ≈207k those steps cost on the baseline. State plainly whether each spec expectation held (efficiency gain visible; challenger cost justified).

- [ ] **Step 5: Error handling (only if acceptance fails)**

Per the spec: identify the failing mechanism, revert or fix **that mechanism only**, re-validate the affected part with micro-tests — no second full run without Eric's explicit approval. Record the failure and the decision in the comparison section.

- [ ] **Step 6: Commit the run outputs**

```powershell
git add outputs/
git commit -m @'
Add ee-flow validation run for the orchestration upgrade

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
'@
```

---

### Task 6: Close-out

**Files:**
- Modify: `C:\Users\ericn\.claude\projects\c--Temp-EE-Toolkit\memory\superpowers-adoption-roadmap.md` (status update)

**Interfaces:**
- Consumes: Task 5's acceptance evidence.

- [ ] **Step 1: Invoke superpowers:verification-before-completion** — evidence: commit list for Tasks 1–5, acceptance-check outputs (fresh), zero stale `PR_02` references, micro-test files in scratchpad.
- [ ] **Step 2: Invoke superpowers:requesting-code-review** — scope: all commits of this sub-project; process findings per superpowers:receiving-code-review; fix and commit as needed.
- [ ] **Step 3: Invoke superpowers:finishing-a-development-branch** — present the integration menu for `SuperPowers`; the decision is Eric's.
- [ ] **Step 4: Update the roadmap memory** — mark sub-project 3 (flow-orchestratie) done with the run's output-folder path; "working agreements" remains the only open sub-project.
