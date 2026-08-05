# EEToolkit — Claude Project Instructions

## Collaboration Rules
- Terminal commands may run without asking for confirmation (the environment is configured for unattended runs). Still avoid destructive commands (e.g. deleting or overwriting files you did not create) unless the user asked for them.
- Do not install dependencies unless the user explicitly requests it.
- Do exactly what the user asked, and nothing more.
- Offer extra improvements only as optional questions, never as automatic work.
- If a request is ambiguous, ask one concise blocking question before editing.
- Before edits, state exactly what will be changed and which files will be touched.
- After edits, report only what changed and confirm no extra files were modified.
- When running a flow, show progress as a live Update Todos list (one item per phase, kept up to date as work proceeds). Do not open the run by printing the full flow overview / step table.

---

## Commands

All toolkit behaviour lives in skills under `.claude/skills/`; CLAUDE.md only routes to them.

| Trigger | Skill |
|---|---|
| `install toolkit`, "set up the toolkit", "setup" | `install-toolkit` — one-time environment setup (uv, pandoc, `uv sync`, verification) |
| `Execute flows/<name>`, "start/run <flow>", or just the flow name (loose match: ignore case, the `-flow` suffix, and filler words) | `execute-flow` — orchestrate the flow end to end and produce the workbook |

**Supporting skills** (injected into agent prompts or run as scripts by `execute-flow` — not user commands): `requirements-quality` (INCOSE criteria), `gherkin-sv` (SV feature-file format), `fmea` (FMEA table rules), `trace-check` (deterministic traceability script).

---

## Agent Registry

Each agent is defined as a standalone character in `.claude/agents/`. Agents have no dependencies on each other or on any workflow document. They are invoked by the `execute-flow` skill's orchestration procedure based on the task at hand. There is no separate orchestrator agent — the main assistant orchestrates flows directly per that procedure.

**Specialists**

| Agent | File | Role |
|---|---|---|
| User Stakeholder | [.claude/agents/user-stakeholder.md](.claude/agents/user-stakeholder.md) | End-user voice, user goals, pain mapping, usage context |
| Customer Stakeholder | [.claude/agents/customer-stakeholder.md](.claude/agents/customer-stakeholder.md) | Buyer voice, procurement criteria, business value, market expectations |
| Business Stakeholder | [.claude/agents/business-stakeholder.md](.claude/agents/business-stakeholder.md) | Legal manufacturer voice, internal departments, organisational constraints, liability |
| Regulatory Stakeholder | [.claude/agents/regulatory-stakeholder.md](.claude/agents/regulatory-stakeholder.md) | Government & authority voice, market access criteria, compliance obligations, approval readiness |
| System Architect | [.claude/agents/system-architect.md](.claude/agents/system-architect.md) | System decomposition, interface definition, design derivation |
| Usability Validation | [.claude/agents/usability-validation.md](.claude/agents/usability-validation.md) | Use scenarios, UFMEA, safety interaction review, UX/UI design |
| Product Owner | [.claude/agents/product-owner.md](.claude/agents/product-owner.md) | Need consolidation, value translation, traceability authoring, BDD feature files, acceptance criteria, backlog shaping, release gates |
| Development Lead | [.claude/agents/development-lead.md](.claude/agents/development-lead.md) | Implementability review, technical specs, feasibility, architecture compliance |
| Verification Lead | [.claude/agents/verification-lead.md](.claude/agents/verification-lead.md) | Verification strategy, coverage matrix, evidence review, readiness call |
| Quality Assurance | [.claude/agents/quality-assurance.md](.claude/agents/quality-assurance.md) | INCOSE requirements quality evaluation, defect identification, comparative verdict |

---

## Project Structure

```
EEToolkit/
├── CLAUDE.md                              # collaboration rules + routing to skills
├── .claude/
│   ├── agents/                            # specialist agent definitions (see Agent Registry)
│   └── skills/                            # all toolkit behaviour: execute-flow, install-toolkit, + supporting skills
├── inputs/                                # input documents — shared by all flows, never duplicated
├── flows/                                 # one folder per flow: flow.md + flow-specific templates
└── outputs/                               # reports and workbooks written after each run (one dated folder per run)
```
