# Skills Hardening — Design

**Date:** 2026-08-05
**Branch:** SuperPowers
**Status:** Approved by Eric (design dialogue, 2026-08-05)

## Goal

Audit and improve the six EE-Toolkit project skills against the superpowers
`writing-skills` methodology:

- `execute-flow` (orchestration procedure)
- `trace-check` (deterministic validation script)
- `fmea`, `gherkin-sv`, `requirements-quality` (injected reference bodies)
- `install-toolkit` (one-time setup)

Primary focus is **form**: structure, discoverability (description quality),
token efficiency. **Behavioral changes require Eric's approval per finding**
before they are applied.

## Context and roadmap

This is sub-project 1 of 3 agreed for adopting superpowers in this repo:

1. **Skills hardening** (this spec)
2. Working agreements for developing the toolkit with superpowers workflows
3. Superpowers patterns inside the `execute-flow` orchestration

Sub-projects 2 and 3 get their own brainstorm → spec → plan cycles and are
**out of scope** here.

## Audit phase

One audit checklist is derived from `superpowers:writing-skills` and its
`anthropic-best-practices.md`, covering at minimum:

- Frontmatter and description quality: "Use when…", triggering conditions
  only, third person, **no workflow summary** in the description
- Keyword coverage for discovery (symptoms, commands, file types)
- Token efficiency (word counts; move detail to `--help`/reference files)
- Form matches the failure type (recipe vs prohibition vs structural slot)
- Cross-references by skill name without force-loading files
- Flowcharts only for non-obvious decisions
- One excellent example instead of many mediocre ones
- No redundancy between skills (the toolkit's existing single-source principle)

**Execution:** six read-only subagents run in parallel (superpowers
`dispatching-parallel-agents` pattern), one per skill. Each receives the
checklist, the skill's path, and context on how `execute-flow` uses that skill
— injected body, script, or user command — because test criteria differ per
skill type (reference vs technique vs setup).

**Output:** one synthesized findings report at
`docs/superpowers/reviews/2026-08-05-skills-audit.md`. Each finding records:
skill, category (**form** or **behavior**), severity, and a concrete proposal.
Findings are prioritized by impact (expected: `execute-flow` first).

## Fix phase

Sequential, in impact order, one skill at a time.

- **Form findings** are applied directly.
- **Behavior findings** are presented to Eric in a bundle; only approved ones
  are applied.
- **Architectural constraint:** the bodies of `fmea`, `gherkin-sv`, and
  `requirements-quality` are injected inline into agent prompts by
  `execute-flow`. Any text change to those bodies is by definition a behavior
  change and requires approval.

**Testing (Iron Law, pragmatically applied):**

- Every substantive change gets a failing test first: cheap micro-tests or
  retrieval/application scenarios with subagents.
- **No full flow runs** for testing (a full expectationeering run costs
  ~1.7M tokens).
- Purely structural fixes (frontmatter, word reduction without meaning change)
  are verified by checking that all references from `execute-flow` and
  CLAUDE.md remain intact (grep) and, where applicable, running `trace-check`.

**STOP rule:** finish, test, and commit one skill completely before starting
the next. No batch edits across skills.

## Completion and verification

- All work on the existing `SuperPowers` branch, one commit per skill.
- Close out with `superpowers:verification-before-completion` (evidence before
  claims) and `superpowers:requesting-code-review`.
- Integrate via `superpowers:finishing-a-development-branch`.

## Error handling

- A subagent audit that returns unusable output → I audit that skill myself
  inline.
- A micro-test that keeps failing after a fix → revert the change and record
  the finding as "not resolved" in the report instead of iterating endlessly.

## Success criteria

- Findings report exists and covers all six skills.
- All form findings fixed; all behavior findings either approved-and-fixed or
  explicitly deferred with rationale.
- Every applied substantive change has test evidence; references between
  CLAUDE.md, `execute-flow`, and the skills remain intact.
- One commit per hardened skill on `SuperPowers`, reviewed before merge.
