# Skills Hardening Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking. **Exception:** Tasks 1–3 dispatch subagents and talk to Eric — they MUST run inline in the main session, not inside a worker subagent.

**Goal:** Audit all six EE-Toolkit skills against the superpowers writing-skills criteria and fix the findings, one skill at a time, with test evidence for every substantive change.

**Architecture:** Phase A (Tasks 1–3): six parallel read-only audit subagents → one synthesized findings report → approval gate with Eric for behavior findings. Phase B (Tasks 4–9): fix one skill per task in the impact order set by the report, each substantive change preceded by a failing micro-test (Iron Law). Phase C (Task 10): verification and code review.

**Tech Stack:** Claude Code Agent tool (parallel dispatch), Grep/Glob for reference checks, PowerShell for word counts, `scripts/check_traces.py` untouched (only its skill doc may change).

**Spec:** `docs/superpowers/specs/2026-08-05-skills-hardening-design.md` (approved 2026-08-05).

## Global Constraints

- Behavior findings are applied ONLY after Eric approved them in Task 3; unapproved ones are recorded as deferred, never silently applied.
- Any text change to the bodies of `fmea`, `gherkin-sv`, or `requirements-quality` is a **behavior** change (they are injected verbatim into agent prompts by `execute-flow`).
- Iron Law: every substantive change needs a failing micro-test BEFORE the edit. If the baseline does not fail, drop the finding (mark "not reproduced").
- NO full flow runs for testing (a full expectationeering run costs ~1.7M tokens). Micro-tests only: 3 reps per variant, single-shot subagents.
- One skill per commit; finish, test, and commit one skill before touching the next (STOP rule). Tasks 4–9 must not be batched.
- Single-source principle: never duplicate content between skills, agent files, or CLAUDE.md.
- All work on the existing `SuperPowers` branch. Commit messages end with `Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>`.
- Windows: use PowerShell syntax; project venv Python is `.venv\Scripts\python.exe`.
- Baseline facts (2026-08-05): word counts — execute-flow 2016, fmea 689, requirements-quality 530, trace-check 500, gherkin-sv 434, install-toolkit 213. Known reference sites to skills: `CLAUDE.md:20-24` (routing table + supporting-skills line), `.claude/skills/execute-flow/SKILL.md:49-51` (injection of gherkin-sv, requirements-quality, fmea), `execute-flow/SKILL.md:69,97,103` (trace-check), `.claude/agents/quality-assurance.md:17` (trace-check), `flows/expectationeering-flow/flow.md` (check per skill).

---

### Task 1: Dispatch the six parallel audit subagents

**Files:**
- Create: `<scratchpad>/audit-execute-flow.md`, `<scratchpad>/audit-fmea.md`, `<scratchpad>/audit-gherkin-sv.md`, `<scratchpad>/audit-requirements-quality.md`, `<scratchpad>/audit-trace-check.md`, `<scratchpad>/audit-install-toolkit.md` (`<scratchpad>` = the session scratchpad directory)
- Modify: none (audits are read-only)

**Interfaces:**
- Produces: six raw audit reports (markdown tables per the prompt below) consumed by Task 2.

- [ ] **Step 1: Dispatch six agents in ONE message (parallel), one per skill**

Use the Agent tool, `subagent_type: "Explore"` (read-only). For each skill, instantiate this prompt, replacing `<NAME>`, `<TYPE>`, `<USAGE>` from the table below:

```
You are auditing one Claude Code skill file against a quality checklist. You are read-only: do not modify any files.

Skill under audit: .claude/skills/<NAME>/SKILL.md
Skill type: <TYPE>
How it is used: <USAGE>

Read for context (do not audit these): CLAUDE.md; .claude/skills/execute-flow/SKILL.md (how the toolkit consumes supporting skills — skip this context item if it is itself the skill under audit); flows/expectationeering-flow/flow.md sections that mention the skill.

Evaluate each checklist point:
1. Frontmatter: name is letters/numbers/hyphens only; description is third person, starts with "Use when..." or equivalent trigger phrasing, describes ONLY triggering conditions (symptoms, situations, contexts), and does NOT summarize the skill's process or workflow (a workflow-summarizing description causes agents to follow the description instead of reading the body).
2. Keyword coverage: would an agent searching for the symptoms/tasks this skill solves find it? Check for error messages, commands, file types, synonyms.
3. Token efficiency: body word count versus value delivered; details that could move to a script's --help, a reference file, or be cut; redundant examples; repeated content.
4. Structure: overview states the core principle in 1-2 sentences; quick-reference table where scanning helps; flowcharts ONLY for non-obvious decisions; one excellent example rather than several mediocre ones.
5. Form matches failure type: rules an agent might skip under pressure need explicit counters (rationalization table / red flags); output-shape guidance should be a positive recipe or contract (what the output IS), not a prohibition list; required elements should be structural slots in a template, not prose reminders.
6. Cross-references: other skills referenced by name; no @-force-loading links; no content duplicated from another skill, agent file, or CLAUDE.md.
7. Correctness: every path, command, step number, and ID the skill cites exists in the repo and is current.

Category rules: "behavior" = any change to the meaning of an injected body, any change to what a procedure does, any description/trigger change that alters when the skill activates. "form" = wording, structure, ordering, frontmatter polish that preserves meaning and triggering.

Return ONLY raw markdown (no preamble), in exactly this shape:

## Audit: <NAME>
Body word count: <n>. Description length: <n> chars.
Overall verdict: <one paragraph>

| # | Category | Severity | Location | Finding | Concrete proposal |
|---|----------|----------|----------|---------|-------------------|
| 1 | form/behavior | high/medium/low | line ref | what is wrong | exact replacement or change |
```

Per-skill values:

| `<NAME>` | `<TYPE>` | `<USAGE>` |
|---|---|---|
| execute-flow | orchestration procedure (user command) | Invoked when the user asks to run a flow; orchestrates specialist agents end to end per flows/<name>/flow.md and injects the bodies of fmea, gherkin-sv, and requirements-quality into agent prompts at specific steps |
| fmea | injected reference body | Body injected verbatim by execute-flow into FMEA authoring/co-author steps 6d, 6e, 6h, 6i and the usability-chain QA sub-audit; never invoked by the user |
| gherkin-sv | injected reference body | Body injected verbatim by execute-flow into 3-Amigos steps 9f–9h and the SV QA sub-audit; never invoked by the user |
| requirements-quality | injected reference body | Body injected verbatim by execute-flow into every requirement-authoring/co-author step (BR_*, UR_*, USR_*, RQ_*) and QA sub-audits; never invoked by the user |
| trace-check | script reference | Points agents to scripts/check_traces.py; run during QA audit step 10a and after authoring steps that add traced rows |
| install-toolkit | setup procedure (user command) | One-time environment setup triggered by "install toolkit" / "setup" |

- [ ] **Step 2: Save each agent's report verbatim to its scratchpad file**

Write each result unmodified to `<scratchpad>/audit-<NAME>.md`. If an agent returns unusable output (no findings table, ignored the format), audit that skill yourself inline against the same checklist and write the result in the same format (spec's error-handling rule).

- [ ] **Step 3: Sanity-check coverage**

Confirm all six files exist and each contains a findings table (possibly empty). No commit — nothing in the repo changed.

---

### Task 2: Synthesize the findings report

**Files:**
- Create: `docs/superpowers/reviews/2026-08-05-skills-audit.md`

**Interfaces:**
- Consumes: the six `<scratchpad>/audit-*.md` reports from Task 1.
- Produces: the findings report with stable finding IDs (`EF-1`, `FM-1`, `GS-1`, `RQ-1`, `TC-1`, `IT-1`, numbered per skill) consumed by Tasks 3–10.

- [ ] **Step 1: Merge and normalize**

Read all six reports. Deduplicate overlapping findings (e.g. two agents flagging the same cross-reference from both ends — keep one, note both locations). Re-check each finding's category against the Global Constraints rule (injected-body text change = behavior) — subagents may miscategorize; your classification wins and MUST be applied before Task 3's approval gate (a miscategorized behavior finding would skip approval).

- [ ] **Step 2: Write the report**

Structure:

```markdown
# Skills Audit — 2026-08-05

Method: six parallel read-only subagent audits against the writing-skills
checklist (see docs/superpowers/plans/2026-08-05-skills-hardening.md, Task 1).

## Impact order for the fix phase
1. <skill> — <one-line reason>   (order = severity-weighted finding count,
   weighted by how central the skill is to a flow run)
...

## Findings

### execute-flow
| ID | Category | Severity | Location | Finding | Proposal | Status |
|----|----------|----------|----------|---------|----------|--------|
| EF-1 | ... | ... | ... | ... | ... | open |

### fmea
| FM-1 | ... (same columns)
... (one section per skill, all six present even if empty)

## Deferred / dropped findings
(filled in Tasks 3–9: rejected by Eric, or baseline not reproduced)
```

Every finding row keeps the subagent's concrete proposal. Status starts as `open`.

- [ ] **Step 3: Commit**

```powershell
git add docs/superpowers/reviews/2026-08-05-skills-audit.md
git commit -m @'
Add skills audit findings report (superpowers skills hardening)

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
'@
```

---

### Task 3: Approval gate for behavior findings

**Files:**
- Modify: `docs/superpowers/reviews/2026-08-05-skills-audit.md`

**Interfaces:**
- Consumes: findings report from Task 2.
- Produces: each behavior finding's Status set to `approved` or `deferred`; the definitive fix order. Tasks 4–9 may only apply `approved` behavior findings and `open` form findings.

- [ ] **Step 1: Present the bundle to Eric**

List every behavior finding (ID, skill, finding, proposal, severity) in the chat, grouped by skill, with a recommendation per finding. Use AskUserQuestion (multiSelect, one question per skill with behavior findings; batch up to 4 options per question, split across questions if more) so Eric can approve/reject per finding. Form findings are listed for transparency but need no approval.

- [ ] **Step 2: Record decisions**

Update Status per behavior finding: `approved` or `deferred (rejected by Eric, <date>)`. Move rejected ones to the Deferred section with rationale. Confirm the impact order with Eric in the same exchange (default: the report's order).

- [ ] **Step 3: Commit**

```powershell
git add docs/superpowers/reviews/2026-08-05-skills-audit.md
git commit -m @'
Record approval decisions on behavior findings

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
'@
```

---

## Phase B — fix tasks

Tasks 4–9 each follow the same seven-step procedure, written out in full per task so every task is self-contained. **Execute them in the impact order from the report**, not necessarily in task-number order. If a skill has zero applicable findings, its task collapses to: update report statuses (n/a) and skip the commit.

**Micro-test recipe (used by every fix task; "3 reps" = 3 independent single-shot subagents, fresh context each):**

- *Description/trigger change* → **discovery test**: give a fresh subagent the full list of this repo's six skill descriptions (old variant vs new variant) plus a realistic user request that should (or should not) trigger the skill, and ask which skill applies. 3 reps per variant. Baseline (old) must show the failure (wrong/missed pick) in ≥1 rep; fixed (new) must pick correctly in 3/3.
- *Body guidance change* → **application test**: give a fresh subagent the (old vs new) skill body plus the task-scenario seed listed in the task, and score the output ONLY against the specific defect the finding targets. Baseline must exhibit the defect in ≥1 of 3 reps; fixed must be defect-free in 3/3.
- *Structural-only change* (frontmatter polish, reordering, word reduction with meaning preserved) → no micro-test; verification is the reference check + word count in the closing steps.
- Read every rep's output yourself; do not score by pattern-match alone. If the baseline shows no failure in 3 reps, mark the finding `deferred (not reproduced)` and make no edit for it.

### Task 4: Fix skill — execute-flow

**Files:**
- Modify: `.claude/skills/execute-flow/SKILL.md`
- Modify: `docs/superpowers/reviews/2026-08-05-skills-audit.md` (statuses)

**Interfaces:**
- Consumes: `approved`/`open` EF-* findings from the report.
- Produces: hardened skill file; report statuses `fixed` / `deferred (not reproduced)` / `not resolved`.

- [ ] **Step 1: Collect applicable findings**

From the report: all EF-* rows with Status `open` (form) or `approved` (behavior). If none, set statuses to `n/a`, skip to Task per impact order.

- [ ] **Step 2: Per substantive finding — write and run the failing micro-test (baseline)**

Apply the micro-test recipe above. Task-scenario seed for execute-flow application tests: "A user says: 'run expectationeering'. Given the skill body, state exactly which file you open first, which agent you spawn for step <n named in the finding>, and what you inject into its prompt." Discovery-test request seed: "start the expectationeering flow" and near-miss "explain what the expectationeering flow does" (must NOT trigger execution). Document each baseline failure verbatim in the scratchpad (`<scratchpad>/microtest-EF-<id>.md`).

- [ ] **Step 3: Apply the fixes**

Edit `.claude/skills/execute-flow/SKILL.md` per the approved proposals. Structural-only findings may be applied together with tested ones in this single edit pass.

- [ ] **Step 4: Re-run each micro-test (GREEN)**

Same scenarios, new body: 3/3 reps must be free of the targeted defect. A test that keeps failing after one fix iteration → re-edit that specific change back to the original text (do not `git checkout` the whole file — other fixes in it must survive), set Status `not resolved`, continue.

- [ ] **Step 5: Reference and structure verification**

Run Grep for `execute-flow` across `CLAUDE.md`, `.claude`, `flows` — confirm CLAUDE.md:20-24 routing still matches the skill's name/triggers, and that `execute-flow/SKILL.md` still cites `gherkin-sv`, `requirements-quality`, `fmea`, `trace-check` at their injection points (former lines 49–51, 69, 97, 103 — line numbers may shift; the four names must each still appear in an injection/run instruction). Word count:

```powershell
(Get-Content .claude\skills\execute-flow\SKILL.md -Raw -Encoding utf8 | Measure-Object -Word).Words   # expect ≤ 2016
```

- [ ] **Step 6: Update report statuses**

Set each EF-* row to `fixed`, `deferred (not reproduced)`, or `not resolved` with a one-line note.

- [ ] **Step 7: Commit**

```powershell
git add .claude/skills/execute-flow/SKILL.md docs/superpowers/reviews/2026-08-05-skills-audit.md
git commit -m @'
Harden execute-flow skill per audit findings

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
'@
```

### Task 5: Fix skill — requirements-quality

**Files:**
- Modify: `.claude/skills/requirements-quality/SKILL.md`
- Modify: `docs/superpowers/reviews/2026-08-05-skills-audit.md` (statuses)

**Interfaces:**
- Consumes: `approved`/`open` RQ-* findings from the report. NOTE: this is an injected body — ALL body-text changes are behavior and need `approved` status; only frontmatter/heading polish can be a form finding.
- Produces: hardened skill file; report statuses `fixed` / `deferred (not reproduced)` / `not resolved`.

- [ ] **Step 1: Collect applicable findings** — all RQ-* rows with Status `open` (form) or `approved` (behavior). If none, set statuses to `n/a` and skip the commit.
- [ ] **Step 2: Per substantive finding — failing micro-test (baseline)** per the micro-test recipe. Application-test seed: "Using the criteria below, author 3 user requirements for a kitchen kettle, then list which of the 10 checks each one could still fail." Score only the defect the finding targets. Document baselines in `<scratchpad>/microtest-RQ-<id>.md`.
- [ ] **Step 3: Apply the fixes** — Edit `.claude/skills/requirements-quality/SKILL.md` per the approved proposals; structural-only findings may ride along in the same pass.
- [ ] **Step 4: Re-run each micro-test (GREEN)** — 3/3 defect-free. Still failing after one fix iteration → re-edit that specific change back to the original text, mark `not resolved`, continue.
- [ ] **Step 5: Reference and structure verification** — Grep `requirements-quality` across `CLAUDE.md`, `.claude`, `flows`: the execute-flow injection instruction (former line 50) and the CLAUDE.md supporting-skills line must still name it. Word count: `(Get-Content .claude\skills\requirements-quality\SKILL.md -Raw -Encoding utf8 | Measure-Object -Word).Words` — expect ≤ 530 unless a finding explicitly added content.
- [ ] **Step 6: Update report statuses** — each RQ-* row → `fixed` / `deferred (not reproduced)` / `not resolved` with a one-line note.
- [ ] **Step 7: Commit**

```powershell
git add .claude/skills/requirements-quality/SKILL.md docs/superpowers/reviews/2026-08-05-skills-audit.md
git commit -m @'
Harden requirements-quality skill per audit findings

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
'@
```

### Task 6: Fix skill — fmea

**Files:**
- Modify: `.claude/skills/fmea/SKILL.md`
- Modify: `docs/superpowers/reviews/2026-08-05-skills-audit.md` (statuses)

**Interfaces:**
- Consumes: `approved`/`open` FM-* findings. NOTE: injected body — ALL body-text changes are behavior and need `approved` status.
- Produces: hardened skill file; report statuses updated.

- [ ] **Step 1: Collect applicable findings** — all FM-* rows with Status `open` (form) or `approved` (behavior). If none, set statuses to `n/a` and skip the commit.
- [ ] **Step 2: Per substantive finding — failing micro-test (baseline)** per the micro-test recipe. Application-test seed: "Using the rules below, author 2 USER_DFMEA rows for a kitchen kettle (failure mode: dry boil) with severity and impact values, and state why each value is on-scale." Document baselines in `<scratchpad>/microtest-FM-<id>.md`.
- [ ] **Step 3: Apply the fixes** — Edit `.claude/skills/fmea/SKILL.md` per the approved proposals; structural-only findings may ride along.
- [ ] **Step 4: Re-run each micro-test (GREEN)** — 3/3 defect-free; persistent failure → re-edit that change back, mark `not resolved`, continue.
- [ ] **Step 5: Reference and structure verification** — Grep `fmea` across `CLAUDE.md`, `.claude`, `flows`: the execute-flow injection instruction (former line 51) and the CLAUDE.md supporting-skills line must still name it. Word count: `(Get-Content .claude\skills\fmea\SKILL.md -Raw -Encoding utf8 | Measure-Object -Word).Words` — expect ≤ 689 unless a finding explicitly added content.
- [ ] **Step 6: Update report statuses** — each FM-* row updated with a one-line note.
- [ ] **Step 7: Commit**

```powershell
git add .claude/skills/fmea/SKILL.md docs/superpowers/reviews/2026-08-05-skills-audit.md
git commit -m @'
Harden fmea skill per audit findings

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
'@
```

### Task 7: Fix skill — gherkin-sv

**Files:**
- Modify: `.claude/skills/gherkin-sv/SKILL.md`
- Modify: `docs/superpowers/reviews/2026-08-05-skills-audit.md` (statuses)

**Interfaces:**
- Consumes: `approved`/`open` GS-* findings. NOTE: injected body — ALL body-text changes are behavior and need `approved` status.
- Produces: hardened skill file; report statuses updated.

- [ ] **Step 1: Collect applicable findings** — all GS-* rows with Status `open` (form) or `approved` (behavior). If none, set statuses to `n/a` and skip the commit.
- [ ] **Step 2: Per substantive finding — failing micro-test (baseline)** per the micro-test recipe. Application-test seed: "Using the format rules below, write one SV feature file for RQ_FN_01 'kettle switches off at boil', including tags and one data table, exactly per the required indentation." Document baselines in `<scratchpad>/microtest-GS-<id>.md`.
- [ ] **Step 3: Apply the fixes** — Edit `.claude/skills/gherkin-sv/SKILL.md` per the approved proposals; structural-only findings may ride along.
- [ ] **Step 4: Re-run each micro-test (GREEN)** — 3/3 defect-free; persistent failure → re-edit that change back, mark `not resolved`, continue.
- [ ] **Step 5: Reference and structure verification** — Grep `gherkin-sv` across `CLAUDE.md`, `.claude`, `flows`: the execute-flow injection instruction (former line 49) and the CLAUDE.md supporting-skills line must still name it. Word count: `(Get-Content .claude\skills\gherkin-sv\SKILL.md -Raw -Encoding utf8 | Measure-Object -Word).Words` — expect ≤ 434 unless a finding explicitly added content.
- [ ] **Step 6: Update report statuses** — each GS-* row updated with a one-line note.
- [ ] **Step 7: Commit**

```powershell
git add .claude/skills/gherkin-sv/SKILL.md docs/superpowers/reviews/2026-08-05-skills-audit.md
git commit -m @'
Harden gherkin-sv skill per audit findings

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
'@
```

### Task 8: Fix skill — trace-check

**Files:**
- Modify: `.claude/skills/trace-check/SKILL.md`
- Modify: `docs/superpowers/reviews/2026-08-05-skills-audit.md` (statuses)

**Interfaces:**
- Consumes: `approved`/`open` TC-* findings. `scripts/check_traces.py` itself is out of scope — only the skill doc changes.
- Produces: hardened skill file; report statuses updated.

- [ ] **Step 1: Collect applicable findings** — all TC-* rows with Status `open` (form) or `approved` (behavior). If none, set statuses to `n/a` and skip the commit.
- [ ] **Step 2: Per substantive finding — failing micro-test (baseline)** per the micro-test recipe. Retrieval-test seed: "Using the skill body below, give the exact command to validate outputs/2026-07-04-170434/Project_Description_Workbook.md on Windows, and state what exit code 1 means." Document baselines in `<scratchpad>/microtest-TC-<id>.md`.
- [ ] **Step 3: Apply the fixes** — Edit `.claude/skills/trace-check/SKILL.md` per the approved proposals; structural-only findings may ride along.
- [ ] **Step 4: Re-run each micro-test (GREEN)** — 3/3 defect-free; persistent failure → re-edit that change back, mark `not resolved`, continue.
- [ ] **Step 5: Reference and structure verification** — Grep `trace-check` across `CLAUDE.md`, `.claude`, `flows`: the execute-flow QA-loop instruction and `.claude/agents/quality-assurance.md:17` must still resolve. Extra correctness check: the documented command must match reality — `.venv\Scripts\python.exe scripts\check_traces.py --help` runs without error. Word count: `(Get-Content .claude\skills\trace-check\SKILL.md -Raw -Encoding utf8 | Measure-Object -Word).Words` — expect ≤ 500 unless a finding explicitly added content.
- [ ] **Step 6: Update report statuses** — each TC-* row updated with a one-line note.
- [ ] **Step 7: Commit**

```powershell
git add .claude/skills/trace-check/SKILL.md docs/superpowers/reviews/2026-08-05-skills-audit.md
git commit -m @'
Harden trace-check skill per audit findings

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
'@
```

### Task 9: Fix skill — install-toolkit

**Files:**
- Modify: `.claude/skills/install-toolkit/SKILL.md`
- Modify: `docs/superpowers/reviews/2026-08-05-skills-audit.md` (statuses)

**Interfaces:**
- Consumes: `approved`/`open` IT-* findings.
- Produces: hardened skill file; report statuses updated.

- [ ] **Step 1: Collect applicable findings** — all IT-* rows with Status `open` (form) or `approved` (behavior). If none, set statuses to `n/a` and skip the commit.
- [ ] **Step 2: Per substantive finding — failing micro-test (baseline)** per the micro-test recipe. Discovery-test seeds: "set up the toolkit" (must trigger) and near-miss "install the python dependencies for this script" (must NOT trigger). Document baselines in `<scratchpad>/microtest-IT-<id>.md`.
- [ ] **Step 3: Apply the fixes** — Edit `.claude/skills/install-toolkit/SKILL.md` per the approved proposals; structural-only findings may ride along.
- [ ] **Step 4: Re-run each micro-test (GREEN)** — 3/3 correct; persistent failure → re-edit that change back, mark `not resolved`, continue.
- [ ] **Step 5: Reference and structure verification** — Grep `install-toolkit` across `CLAUDE.md`, `.claude`: the CLAUDE.md routing-table row must still match the skill's name and triggers. Word count: `(Get-Content .claude\skills\install-toolkit\SKILL.md -Raw -Encoding utf8 | Measure-Object -Word).Words` — expect ≤ 213 unless a finding explicitly added content.
- [ ] **Step 6: Update report statuses** — each IT-* row updated with a one-line note.
- [ ] **Step 7: Commit**

```powershell
git add .claude/skills/install-toolkit/SKILL.md docs/superpowers/reviews/2026-08-05-skills-audit.md
git commit -m @'
Harden install-toolkit skill per audit findings

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
'@
```

---

### Task 10: Final verification and code review

**Files:**
- Modify: `docs/superpowers/reviews/2026-08-05-skills-audit.md` (closing summary)

**Interfaces:**
- Consumes: all fix-task commits and final report statuses.

- [ ] **Step 1: Invoke superpowers:verification-before-completion**

Follow it. Evidence to produce, minimum: (a) `git log --oneline main..SuperPowers` shows the spec commit, report commits, and one commit per changed skill; (b) the report contains zero rows with Status `open` or `approved` (everything is `fixed`, `n/a`, `deferred (...)`, or `not resolved`); (c) re-run the Task 4–9 reference Greps once more — all six skill names still resolve everywhere they are consumed; (d) word counts ≤ baselines unless a finding explicitly added content.

- [ ] **Step 2: Close out the report**

Append a `## Outcome` section: counts of fixed / deferred / not resolved per skill, and test evidence pointers (scratchpad microtest files). Commit:

```powershell
git add docs/superpowers/reviews/2026-08-05-skills-audit.md
git commit -m @'
Close skills audit: outcome summary and verification evidence

Co-Authored-By: Claude Fable 5 <noreply@anthropic.com>
'@
```

- [ ] **Step 3: Invoke superpowers:requesting-code-review**

Review scope: all commits on `SuperPowers` since `main` that touch `.claude/skills/` or `docs/superpowers/`. Address findings per superpowers:receiving-code-review.

- [ ] **Step 4: Invoke superpowers:finishing-a-development-branch**

Present Eric the integration options for the `SuperPowers` branch. Do not merge without his choice.
