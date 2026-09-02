# Research OS

## Purpose

This workspace exists to improve the continuity, quality, and traceability of research reasoning. It is not merely a document-summary archive.

`manifesto.md` is the project's curated working memory. It records the current research direction, definitions, hypotheses, preferences, uncertainties, evidence links, and next decisions without trying to contain every source detail.

## Components

- `manifesto.md`: the evolving synthesis and research compass.
- `library/`: external evidence, source notes, preserved originals when appropriate, and the source index.
- `notes/`: the researcher's canonical, editable personal notes.
- `scout/`: literature-search scope, seen-item ledger, and dated scouting reports.
- `staging-material/`: disposable material used during bootstrap or import. Durable outputs must not depend on it.
- `skills/`: canonical, student-editable workflows for bootstrapping, updating, and scouting the Research OS.
- `.agents/skills/`: small discovery loaders and UI metadata that make the visible workflows available to ChatGPT Work.
- `examples/`: a completed miniature Research OS for orientation only.

## Working rules

- Read `manifesto.md` and the relevant indexes before updating an existing system.
- Distinguish source claims, researcher statements, agent interpretations, and uncertainty.
- Preserve source provenance. Never invent evidence, metadata, quotations, timestamps, or reading coverage.
- During bootstrap, map all available inputs, draft a provisional manifesto, selectively deepen decision-relevant and discovery-oriented material, and refine the manifesto in one coordinated run.
- Preserve `staging-material/ideas.md` unchanged as `notes/research-origin.md` before synthesizing it.
- When new resources arrive, index them first and then assess whether they warrant a manifesto change.
- External evidence in the manifesto should link to `library/`; personal questions, hypotheses, preferences, and decisions should link to canonical files in `notes/`.
- Do not link durable outputs to `staging-material/`.
- Preserve productive disagreement and unresolved questions instead of forcing consensus.
- Keep Markdown concise, navigable, and useful for the next research decision.
- Literature Scout produces candidates for human review. It must not index candidates or modify `manifesto.md`, `library/`, or `notes/`.
- Treat `skills/<name>/SKILL.md` as the canonical workflow. The matching `.agents/skills/<name>/SKILL.md` must remain a minimal loader with synchronized `name` and `description` metadata.
