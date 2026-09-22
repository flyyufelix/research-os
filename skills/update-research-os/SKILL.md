---
name: update-research-os
description: Ingest new or changed resources into an existing Markdown Research OS and assess their impact on manifesto.md. Use when indexing added PDF papers, long PDF books, theses, webpages, reports, or YouTube videos; importing or reviewing personal notes under notes/; accessing explicitly authorized Notion, OneDrive, Obsidian, Google Drive, or other connected notes; refreshing library/_index.md; revisiting a source at greater reading depth; reconciling indexed, watched, or dismissed literature-scout candidates; or deciding whether new evidence or researcher thinking should update the research manifesto.
---

# Update a Research OS

Maintain an existing Research OS incrementally without rebuilding it or silently changing its research direction.

## Load only the relevant procedure

- For any proposed, approved, or published change to `manifesto.md`, read [manifesto-versioning.md](references/manifesto-versioning.md).
- For PDFs, books, webpages, reports, and YouTube videos, read [external-sources.md](references/external-sources.md). For a long PDF book, thesis, manual, or report, also read [long-pdf-books.md](references/long-pdf-books.md).
- For personal notes already under `notes/`, or local and exported notes to import there, read [personal-notes.md](references/personal-notes.md).
- For Notion, OneDrive, Obsidian, Google Drive, or other connected notes, read [connected-notes.md](references/connected-notes.md) and [personal-notes.md](references/personal-notes.md).

## Workflow

1. Read `AGENTS.md`, `manifesto.md`, `library/_index.md`, and only the existing notes relevant to the request. Also read `scout/_seen.md` when indexing an external source or recording a scout-candidate decision.
2. Resolve the requested scope. Compare titles, DOI, URLs, page or file IDs, paths, existing source IDs, and available change history or modification dates to identify new, changed, duplicate, or inaccessible material.
3. Read the relevant source-type procedure above and ingest each eligible item. For external sources, triage first and choose the reading depth by project decision value, recording the rationale and material examined. Treat personal notes under `notes/` as canonical researcher writing and do not rewrite them unless asked. Import eligible staged or connected personal notes into `notes/` according to the personal-note procedure.
4. Update `library/_index.md` after adding or materially changing an external source note. Do not require an inbox, scratchpad, or separate developed-ideas layer under `notes/`.
5. Reconcile the scout ledger when applicable. Match by DOI, arXiv ID, another stable identifier, canonical URL, or normalized title and year, in that order. After successful indexing, change an unambiguous matching candidate to `indexed`. Change it to `watch` or `dismissed` only when the researcher explicitly makes that decision. Leave failed, incomplete, inaccessible, or ambiguous cases unchanged; never infer dismissal. Preserve the candidate's report link and discovery dates, and report every transition.
6. Compare the new material with the manifesto and relevant existing notes. Record agreement, tension, missing evidence, and changed project relevance.
7. Classify manifesto impact as one or more of:

   - no change
   - supporting evidence
   - new question or uncertainty
   - definition
   - hypothesis
   - scope
   - confidence
   - thesis challenge
   - new direction

8. If there is no manifesto impact, leave its version unchanged. Otherwise read the manifesto versioning procedure, select the proposed version increment, and prepare all directly justified changes as one reviewable proposal. Include retrieval-oriented updates such as core-source links, personal-note links, search vocabulary, evidence gaps, and uncertainties when warranted. Link external evidence claims to `library/` and researcher questions, hypotheses, and preferences to `notes/`.
9. Present the proposed version, exact current and proposed text, change rationale, supporting sources, counterevidence, uncertainty, and downstream consequences. Do not edit `manifesto.md` until the researcher explicitly approves the complete proposal, including patch-level changes.
10. After explicit approval, publish the version according to [manifesto-versioning.md](references/manifesto-versioning.md): update `manifesto.md`, create its immutable approved snapshot, and append the release to `CHANGELOG.md`. If approval is not part of the current request, leave the approved manifesto and version history unchanged.
11. Validate links, provenance, index coverage, reading depth, claim ownership, version consistency, and any scout-ledger transition. Ensure `manifesto.md` contains no links to `staging-material/` or other disposable staging paths. Report the items processed, manifesto impact, approved versions published, proposals awaiting approval, and unresolved issues.

## Bootstrap support

When `bootstrap-research-os` uses this procedure, support both its broad mapping pass and later selective deep-reading pass. Import staged personal notes into `notes/`, create or refine external source records with exact reading coverage, and return structured synthesis inputs. Do not edit `manifesto.md` item by item; the bootstrap workflow owns manifesto v0 and its iterative refinement across the collection.

## Guardrails

- Never add every resource to the manifesto; promote only durable evidence, decisions, uncertainties, and directions that improve future reasoning or retrieval.
- Never publish a manifesto version, snapshot, or changelog entry without explicit researcher approval.
- Never cite disposable staging files from the manifesto.
- Never add demo-only fields, labels, or content to production notes or source records unless explicitly requested.
- Never mark a scout candidate `watch` or `dismissed` without an explicit researcher decision.
- Preserve researcher-authored note content and keep agent inference clearly identified.
- Never overstate reading coverage, causal support, generality, or verification.
- Preserve partial successes and disclose failures or inaccessible material.
