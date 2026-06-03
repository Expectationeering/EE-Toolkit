# EE Toolkit — Agentic AI Kit

**AI agents that help you apply [Expectationeering](https://www.expectationeering.org) — drafting your story and filling the workbook, domain by domain, with you and your stakeholders firmly in the lead.**

> No Story — No Glory!

Expectationeering is an open methodology that turns vague stakeholder expectations into a precise, validated product definition — a narrative that holds from first idea to final delivery. The **Agentic AI Kit** is the part of the EE Toolkit that puts AI agents to work *applying* that methodology.

> ⏳ **Heads-up: a full run takes a while.** Executing the complete flow drives dozens of agent steps — every stakeholder, design, and requirement section, the 3-Amigos verification session, and a quality-assurance audit loop. Expect it to run for **many minutes up to an hour or more**, depending on the size of your input and the AI model you use. Let it work to the end, or [run it step by step](#make-it-your-own) if you'd rather go section by section.

---

## What's inside

- **Agent prompts** — ready-to-use prompts and system instructions, one matching agent per domain
- **Templates** — workbook-aligned output templates and structured formats for traceability
- **Reference data** — worked-example data to ground the agents
- **Guidance** — how to set the agents up and review their output

> ℹ️ _Adjust this list to match the actual folder structure once the code is in the repo._

## How to use it

1. **Set up the agents** — load the prompts and system instructions into your preferred LLM assistant.
2. **Draft domain by domain** — feed in your context and let each agent draft the story, stakeholders, expectations, requirements, and use cases.
3. **Review & decide** — every output is yours to review, correct, and approve. The agents draft; **humans decide.**

## ⚠️ AI drafts — it can't align your stakeholders

The agents accelerate the drafting, but they can't reconcile the egos, opinions, and pet topics your stakeholders bring to the table. That alignment only happens when people sit down together. **Run the workshop first**, then use the kit to go fast. Alignment is the step you can't automate.

## Requirements

- An LLM assistant / chat model of your choice — the kit is **tool-agnostic**.
- The free [Expectationeering Workbook](https://www.expectationeering.org/workbook/) as the structure the agents help you fill in.

## Getting started

You don't need to know anything about Python, terminals, or installing software. This toolkit runs through **[Claude Code](https://claude.com/claude-code)** — an AI assistant that does the technical work for you. You just paste instructions.

### 1. Get the project onto your computer

On the GitHub page, click the green **Code** button → **Download ZIP**, then unzip the folder somewhere you can find it. (If you know git, you can clone it instead.)

### 2. Open the folder in Claude Code

Open Claude Code and point it at the unzipped project folder.

### 3. Copy this prompt to install everything

Paste the text below into Claude Code and send it. You only do this **once**.

```text
install toolkit
```

That's it — Claude Code installs the three tools the kit needs (**uv** to run the scripts, **pandoc** to read your Word input, and **Graphviz** to draw the context diagram), sets up the environment, and tells you when you're ready. It may ask permission to run a few commands — say yes.

Claude Code will install what's needed, set up the environment, and confirm when you're ready. It may ask for permission to run a few commands — that's normal; say yes.

### 4. Copy this prompt to run a flow

Put your project document — a Word `.docx` file — into the **`inputs`** folder. Then paste:

```text
Execute flows/expectationeering-flow
```

Or just type one of these — they all start the same flow:

```text
start expectationeering
```
```text
run expectationeering
```

> 📄 **The files in `inputs` and `outputs` are just examples.** Replace the example document in **`inputs`** with your own, and feel free to delete the example workbook in **`outputs`** — it was only generated to show you what the result looks like.

When it finishes, your completed workbook is in the **`outputs`** folder, in both Word (`.docx`) and markdown — named after your input document with `_Workbook` added (e.g. `Project_Description.docx` → `Project_Description_Workbook`).

### What a run costs

A full run drives every flow step (all stakeholder, design, and requirement sections), a 3-Amigos session that writes the BDD verification scenarios, and a quality-assurance pass that audits traceability and requirement quality — fixing what it finds until nothing remains — then renders the context diagram and the Word document.

Measured on the bundled example input ([`inputs/Project_Description.docx`](inputs/)), one complete run was:

| Metric | Example run |
|--------|-------------|
| AI tokens | **~101,000** |
| Wall-clock time | **~13–14 minutes** |
| Tool actions (file edits, conversions, audits) | ~68 |
| Output | ~530 KB Word workbook, 130+ tables, 40+ requirements, 19 BDD scenarios, embedded context diagram |

Treat this as a baseline for a small-to-medium project. Cost scales with the size and complexity of your input document — a larger brief means more requirements to author and more quality-assurance correction cycles, so expect the token count and time to rise accordingly.

## Make it your own

The kit is meant to be adapted — nothing here is locked down.

- **Adjust the agents and the flow.** Each agent is a plain prompt in [`.claude/agents/`](.claude/agents/) (one file per role), and the flow is a single readable document in [`flows/expectationeering-flow/flow.md`](flows/expectationeering-flow/flow.md). Edit an agent's voice or expertise, or change the flow's steps, sequencing, and templates, to fit your domain and house style.
- **Add your own flow.** Drop a new folder under [`flows/`](flows/) containing a `flow.md` plus its templates, following the same structure as the example flow. Then start it the same way — `Execute flows/<your-flow>`. The kit picks up the metadata (templates, inputs, convert command) and orchestrates it for you.
- **Run it step by step.** You don't have to run the whole flow in one go. The flow's `## Steps` table gives every step its own ID (`1a`, `1b`, … `10a`), role, and artifact, so you can ask Claude Code to run a single step, pause between steps to review, or pick up where you left off — the workbook is filled incrementally and stays consistent. Just say what you want in plain language, for example:

  ```text
  Run step 1 of flows/expectationeering-flow
  ```
  ```text
  Run step 6f of flows/expectationeering-flow
  ```
  ```text
  Run steps 1a–1e of flows/expectationeering-flow, then stop so I can review
  ```
  ```text
  Continue the expectationeering flow from step 9a
  ```

  The first per-step run initialises the workbook (just like a full run); each later step reads the workbook so far, fills only its own section(s), and leaves the rest untouched.

## Works alongside a strict QMS

The product definition the kit helps produce is **conceptual project input** — it lives in the front end, *outside* your Quality Management System — and then becomes the controlled input that feeds the development governed *under* your QMS.

## Learn more

- 🌐 **Method:** https://www.expectationeering.org
- 📘 **Workbook & worked example:** https://www.expectationeering.org/workbook/
- 🧩 **The Agentic AI Kit:** https://www.expectationeering.org/agentic-ai/
- 🤝 **Providers** (workshops, training, Polarion): https://www.expectationeering.org/suppliers/
- ✉️ **Contact:** https://www.expectationeering.org/contact/

## Contributing

Direct commits are restricted to maintainers. To propose a change, **fork** this repository and open a **pull request** — it will be reviewed before merging. Issues and suggestions are very welcome.

## License

Released under the [MIT License](LICENSE). You're free to use and adapt the kit; attribution is appreciated.
