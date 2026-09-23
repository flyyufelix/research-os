# Research OS

Research OS is a simple, Markdown-based workspace for developing a research project with an AI agent. It brings together your questions, personal notes, and research sources, then maintains a living overview that can guide future searching, thinking, writing, and presentations.

All important content is stored in ordinary text files. You can read and edit them with Obsidian—a note-taking app that organizes Markdown files—or any text editor.

Research OS captures the working memory, current state, research taste, and preferences of your project in `manifesto.md`. This is the most important file in the system: every current and future Research OS workflow uses it as the primary guide for searching, evaluating sources, brainstorming, writing, and creating presentations.

> **New to Research OS?** Follow the [beginner website](https://flyyufelix.github.io/research-os/) to download the project, build your first `manifesto.md`, connect an AI agent, and run Literature Scout.

## Quick navigation

- [What Research OS does](#what-research-os-does)
- [The core loop](#the-core-loop)
- [Components](#components)
- [Build your first Research OS](#build-your-first-research-os)
- [Maintain and update the system](#maintain-and-update-the-system)
- [Manifesto version history](#manifesto-version-history)
- [Literature Scout](#literature-scout)
- [FAQ](#faq)

---

## What Research OS does

Research OS helps you:

- preserve your original questions, hypotheses, doubts, and research preferences;
- organize papers, books, reports, webpages, videos, and personal notes;
- maintain the current state of your research program in `manifesto.md`;
- discover relevant literature for human review;
- give future AI tasks reliable context for brainstorming, writing, presentations, and research decisions.

---

## The core loop

```text
1. Add your ideas, notes, and sources
                    ↓
2. Ask the agent to build or update the Research OS
                    ↓
3. Review the manifesto, source library, and notes
                    ↓
4. Use them for research, writing, and literature discovery
                    ↓
              Add new material
                    ↺
```

---

## Components

```text
research-os/
├── AGENTS.md                   Project guide for the AI agent
├── manifesto.md                Working memory of the research program
├── CHANGELOG.md                Approved manifesto release history
├── versions/
│   └── manifesto/              Immutable approved manifesto snapshots
├── library/                    Indexed external sources
│   ├── _index.md
│   └── sources/
├── notes/                      Your editable personal notes
├── staging-material/           Temporary materials for the first build
│   ├── ideas.md
│   ├── papers/
│   └── personal-notes/
├── skills/                     Visible, editable agent workflows
├── .agents/skills/             Files for automatic skill discovery
├── scout/                      Literature Scout settings and reports
└── examples/                   A completed example
```

### `AGENTS.md`

The project guide for the AI agent: its purpose, components, and operating rules.

### `manifesto.md`

The **working memory of your research program** and **the most important file** in the system. It records your questions, hypotheses, scope, uncertainties, research preferences, evidence gaps, and next decisions. It links external evidence to `library/` and your own thinking to `notes/`, giving future searches, writing, and presentations a reliable starting point.

### `CHANGELOG.md` and `versions/manifesto/`

`CHANGELOG.md` explains what changed in each approved manifesto version, why it changed, which AI agent prepared it, and who approved it. `versions/manifesto/` preserves a complete, read-only snapshot of every approved version. These files provide a transparent history without requiring students to use Git.

### `library/`

Indexed external sources such as papers, books, and webpages. `library/_index.md` lists them; each source has a note under `library/sources/`.

### `notes/`

Your editable personal notes. The first build copies `ideas.md` unchanged to `notes/research-origin.md` and imports any other personal notes here.

### `staging-material/`

A temporary drop zone for your initial ideas, papers, and personal notes. Clear it only after checking that everything has a permanent copy in `notes/` or `library/`.

### `skills/` and `.agents/skills/`

Reusable instructions for the AI agent:

- [`bootstrap-research-os`](skills/bootstrap-research-os/SKILL.md) builds the initial system;
- [`update-research-os`](skills/update-research-os/SKILL.md) processes new or changed material;
- [`scout-literature`](skills/scout-literature/SKILL.md) discovers literature candidates.

The editable instructions are in `skills/`. The hidden `.agents/skills/` files let ChatGPT Work discover them automatically. See the [skills guide](skills/README.md).

### `scout/`

Literature Scout settings, its record of previous candidates, and dated reports.

### `examples/`

A [worked Research OS example](examples/music-and-studying/README.md) with raw inputs, two PDF papers, personal notes, indexed source notes, a manifesto, and a scout report.

---

## Build your first Research OS

1. Clone the repository with Git and open the `research-os` folder in ChatGPT Work. If you do not use Git, choose **Code → Download ZIP** on GitHub and unzip the downloaded folder instead.
2. Replace the content of `staging-material/ideas.md` with your interests, questions, tentative hypotheses, doubts, preferred evidence, and scope. Rough or incomplete writing is fine.
3. Optionally add reference files—including PDF papers, books, theses, and reports—to `staging-material/papers/`, and personal notes to `staging-material/personal-notes/`.
4. Ask the agent to build the system:

```text
Build my Research OS using everything in staging-material.
```

ChatGPT Work should recognize this as a first-time build and use the included `bootstrap-research-os` skill in the background. You do not need to name the skill in your prompt.

One prompt starts a multi-pass build: ChatGPT Work maps the complete collection, drafts a provisional manifesto, reads the most decision-relevant material more deeply, checks at least one promising direction outside the initial framing, and then refines the manifesto. Long books are mapped and selectively read rather than processed from first page to last; their source notes record exactly which chapters and pages were examined.

When it finishes, review `manifesto.md`, `library/_index.md`, the source notes, and `notes/research-origin.md`. Clear `staging-material/` only after confirming that the important material was preserved.

The first manifesto is proposed as `v0.1.0` with status `Awaiting review`. After you approve it, the agent marks it approved, saves an immutable snapshot, and creates its changelog entry.

---

## Maintain and update the system

Under the hood, the agent uses the [`update-research-os`](skills/update-research-os/SKILL.md) skill to process new material and assess whether `manifesto.md` should change.

### Add a paper, webpage, report, or video

```text
Index [attached PDF / webpage URL / video URL] and update my Research OS.
```

For example: `Index the attached paper.pdf and update my Research OS.`

The agent reads more deeply when a source could affect a central research claim.

### Add or revise a personal note

Create or edit a Markdown file under `notes/`, then ask:

```text
Review my new or changed notes and update my Research OS.
```

---

## Manifesto version history

Research OS uses simple version numbers for `manifesto.md`:

- `v0.1.0 → v0.2.0` means an approved substantive change to the research question, thesis, definitions, scope, hypotheses, confidence, or direction.
- `v0.2.0 → v0.2.1` means an approved supporting update such as new evidence, links, vocabulary, uncertainties, or clarification.
- `v1.0.0` is used only when you explicitly designate the manifesto as the first formal, submitted, or stable research baseline.

The agent first presents a proposed version and explains what would change and why. Your existing approved `manifesto.md` remains unchanged until you explicitly approve the complete proposal. The published version records its timestamp, the AI agent that prepared it, the researcher who approved it, and a short change summary.

Versioning is intentionally lighter elsewhere. Library source notes remain one current file with AI attribution and a short revision history for substantive interpretive changes. Original source files are not overwritten, personal notes preserve the researcher's writing, and scout ledgers remain append-only.

---

## Literature Scout

Literature Scout periodically searches for papers, reports, research posts, blogs, and news related to `manifesto.md`. It saves a ranked report for human review without automatically indexing candidates or changing the manifesto.

See the [Literature Scout guide](scout/README.md) for configuration, manual runs, scheduling, candidate review, and optional email delivery through a Gmail connection.

---

## FAQ

### What should I write in `ideas.md`? Can it be vague?

Yes. Write the questions, patterns, hypotheses, preferences, doubts, boundaries, and disagreements already in your head. Fragments are fine. The purpose is to preserve your starting point, not to produce polished writing.

### What if my notes are in Notion, OneDrive, Google Drive, or another Obsidian folder?

ChatGPT Work can use [plugins and connectors](https://learn.chatgpt.com/docs/plugins) to access supported services such as Notion and Google Drive after you install and authorize them. Availability varies by service and workspace; for OneDrive or another location without an available connector, export or sync selected notes to Markdown, copy them into `staging-material/personal-notes/`, or use an authorized read-only MCP connection. Decide which location is your main copy so future updates can be matched correctly.

### Can I edit files in `notes/` myself?

Yes. They are your personal, editable notes. After a meaningful change, ask ChatGPT Work to review them and update your Research OS.

### When should `manifesto.md` change?

When new evidence or thinking creates a lasting improvement: stronger evidence, a serious challenge, a useful definition, a new uncertainty, a scope decision, or a changed research direction. Major changes should be proposed for your approval.

### What happens if I add a long PDF book?

ChatGPT Work first maps its contents, introduction, conclusion, index, and relevant terminology. It then uses the developing or existing manifesto to select high-value chapters and one discovery-oriented section. The source note distinguishes material that was only mapped from pages that were closely read, so the book can be revisited later without starting over.

### Will a local scheduled task run while my Mac is asleep?

No, not when it needs the local project. The Mac must be awake and the ChatGPT app running. On a Mac that remains connected to power, you can enable **System Settings → Energy Saver → Prevent automatic sleeping on power adapter when the display is off**. The exact setting name and location may vary by Mac model and macOS version. Otherwise, use a cloud scheduled task.

### Should I use a local or cloud project?

Use a **local project** for the simplest setup and direct access to files on your computer. Local scheduled tasks require the computer to be awake and ChatGPT running.

Use a **cloud project** if tasks must run while your computer is off or the project is shared. Store the project and skills in GitHub, keep large files or external notes in an authorized online service, and connect those sources to ChatGPT Work. See [ChatGPT Work cloud setup](https://learn.chatgpt.com/docs/cloud).

### Can I delete `staging-material/` after the first build?

Yes, after confirming that your original ideas, personal notes, and source records were copied into `notes/` and `library/`, and that no permanent file links back to staging.

### Where are the skill files, and must I invoke them explicitly?

The editable skills are in the visible [`skills/`](skills/) folder. The matching files under `.agents/skills/` help ChatGPT Work discover them automatically. You normally do not need to name a skill: describe the task plainly, and ChatGPT Work should select the matching workflow.

For ordinary changes, edit `skills/<name>/SKILL.md`. If you rename a skill or change its description, ask ChatGPT Work to synchronize the matching discovery file under `.agents/skills/`.
