---
name: gherkin-sv
description: Canonical format rules for the SV_* Gherkin BDD feature files in the Expectationeering workbook (structure, tagging, exact indentation, data-table alignment, converter rendering). The orchestrator injects this body inline into the prompts of the 3-Amigos steps (9f–9h) and the SV quality-assurance sub-audit — the only steps that need it.
---

# Gherkin SV_* feature-file format

Every `SV_*` verification entry in the workbook is **one Gherkin BDD feature file per functional requirement**, written as a `gherkin` fenced block. **Follow the reference file `flows/expectationeering-flow/Example.feature` (path relative to the project root) for the structure, style, and layout of every feature file** — the leading `@ID:` tag, the `Feature:` line, the `As a … I want … So that …` user story, a `Rule:` capturing the "shall" statement, and concrete `Scenario`s with `Given / When / Then` steps and aligned `| … |` data tables — including its indentation.

## Structure & tracing

- Tag each feature `@ID:RQ_FN_xx` — this traces it to the functional requirement it verifies (**SV → RQ_FN**). If one requirement needs more than one feature file, suffix the tag with a sub-index — `@ID:RQ_FN_01.1`, `@ID:RQ_FN_01.2` — never two files with the same bare tag; the converter strips the suffix when tracing.
- Each feature opens with a user story (`As a … I want … So that …`), states a `Rule:` that captures the requirement's "shall" statement, and contains one or more concrete `Scenario`s with `Given / When / Then` steps and data tables for the expected values.
- Use **measurable** outcomes (e.g. "within 5 seconds") — binary pass/fail, never subjective assertions.
- Every `RQ_FN_*` must have a feature file and every `RQ_*` must be covered by at least one scenario.
- Do **not** add housekeeping comment lines such as `# verifies RQ_PR_01, RQ_IF_01`. Keep cross-coverage traceability in the `@ID:` tag and, where helpful, as a brief inline `(RQ_xx)` reference within the step text — never as a separate `#` comment line.

## Exact indentation (must match `flows/expectationeering-flow/Example.feature`)

- Put `@ID:…`, `Feature:`, `Rule:`, and `Scenario:` / `Scenario Outline:` flush at **column 0**.
- Indent **everything else by exactly 4 spaces** — the `As a … / So that …` user story, every `Given / When / Then / And / But` step, any `# comment` line, `Examples:`, and every `| … |` data-table row.
- Put one blank line before each `Rule:` and before each `Scenario:`.
- Do **not** nest `Rule:`/`Scenario:` under `Feature:` (no 2-space "tree" indentation).

## Rendering

The converter records each feature file as one `SV_*` row in the Verification table and renders it in fixed-width monospace with Gherkin syntax colouring, so misaligned data-table pipes are visible in the final .docx — keep them aligned in the markdown.
