# Completed example: music and studying

This example shows how Research OS turns a brain dump, personal notes, and papers into a connected research program. The question is deliberately approachable, but the evidence is mixed enough to demonstrate real research judgment.

This folder contains completed example outputs, not a separate scaffold. It uses the repository's canonical [`AGENTS.md`](../../AGENTS.md) and [skills](../../skills/README.md). Open the repository root as the ChatGPT Work project so those shared workflows remain available; do not copy or maintain another set of skills inside this example.

## Follow the workflow

### 1. Start with the raw inputs

The [`staging-material/`](staging-material/) folder contains exactly what a researcher might provide before the first build:

- an [`ideas.md`](staging-material/ideas.md) brain dump;
- two editable [personal notes](staging-material/personal-notes/);
- two short, open-access [PDF papers](staging-material/papers/).

### 2. Inspect the organized system

The bootstrap workflow maps all inputs, drafts a provisional manifesto, deepens the most relevant evidence, and then refines the system:

- [`notes/research-origin.md`](notes/research-origin.md) is an unchanged copy of the initial brain dump;
- [`notes/`](notes/) contains the researcher's first-party thinking;
- [`library/_index.md`](library/_index.md) links to structured notes for external sources;
- [`manifesto.md`](manifesto.md) synthesizes the current questions, preferences, evidence, tensions, and next decisions.

The two PDFs are copied unchanged into their source folders beside the agent-generated notes. Both were read fully because they bear directly on the central question; a less decisive or much longer source could instead be mapped or selectively read, with its actual coverage recorded.

### 3. See what happens next

The [sample Literature Scout report](scout/reports/2026-08-30.md) uses gaps in the manifesto to identify one candidate. The candidate remains separate from accepted evidence until a person decides to index, watch, or dismiss it.

## Trace one idea through the system

The original brain dump asks whether lyrics interfere with reading. A [personal observation](notes/study-observations.md) separates feeling focused from understanding a text. The [Sun paper note](library/sources/sun-2024-background-music-reading-comprehension/note.md) adds narrow experimental evidence, while the [Küssner review note](library/sources/kussner-2017-background-music-personality/note.md) shows why personality-based explanations remain unsettled. The [manifesto](manifesto.md) combines these strands into conditional hypotheses and explicit evidence gaps.

## Included papers

- Mats B. Küssner (2017), [publisher page](https://doi.org/10.3389/fpsyg.2017.01991), CC BY.
- Yanping Sun et al. (2024), [publisher page](https://doi.org/10.3389/fpsyg.2024.1363562), CC BY.

The PDFs are included for teaching and attribution remains with their authors and publishers.
