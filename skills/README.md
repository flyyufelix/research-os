# Research OS skills

Skills are reusable Markdown workflows for an AI agent. This visible folder contains the canonical instructions so they can be read and edited directly in Obsidian, GitHub, or any text editor.

| Skill | Purpose | Edit this file |
|---|---|---|
| Bootstrap Research OS | Map initial material, iteratively develop `manifesto.md`, and build `library/` and `notes/` | [`bootstrap-research-os/SKILL.md`](bootstrap-research-os/SKILL.md) |
| Update Research OS | Index new or changed resources—including long books—reconcile scout decisions, and assess manifesto impact | [`update-research-os/SKILL.md`](update-research-os/SKILL.md) |
| Scout Literature | Find and rank new literature candidates without indexing them | [`scout-literature/SKILL.md`](scout-literature/SKILL.md) |

## How discovery works

ChatGPT discovers repository skills from `.agents/skills/`. Each matching hidden `SKILL.md` in this repository is deliberately tiny: it contains the skill's discovery metadata and directs the agent to read the corresponding canonical workflow in this folder. No symlinks are used.

This separation provides:

- visible and editable workflows for Obsidian users;
- automatic ChatGPT Work discovery;
- normal behavior in ZIP downloads and on Windows;
- one detailed source of truth for each workflow.

For ordinary workflow changes, edit only the visible file linked above. If you change a skill's `name` or `description` in its YAML front matter, ask ChatGPT Work to synchronize those two fields in the matching `.agents/skills/<name>/SKILL.md` discovery loader. The workflow body belongs only in the visible file.

You normally do not need to invoke a skill explicitly: describe the task plainly and ChatGPT Work should select the matching workflow. Explicit skill mentions remain useful for teaching and reproducibility.
