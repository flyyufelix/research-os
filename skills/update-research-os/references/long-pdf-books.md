# Long PDF Books and Other Long Documents

Use this procedure during bootstrap or later updates when a PDF is too long for a reliable linear reading, especially books, theses, manuals, and reports of roughly 100 pages or more. Apply judgment rather than a strict page threshold.

## Preserve and map

1. Preserve the supplied PDF unchanged as `library/sources/<source-id>/source.pdf`.
2. Record bibliographic metadata and whether the PDF has searchable text. If it is scanned, use OCR when available and disclose its quality.
3. Build a structural map from the table of contents, preface, introduction, chapter openings or summaries, conclusion, index, and bibliography. Do not claim to have read chapters that were only mapped.
4. Extract or search text locally when practical. Search first with terminology from `notes/research-origin.md` and personal notes, then add vocabulary introduced by the book itself. Inspect context around matches instead of loading the complete extracted text into the model context.
5. Distinguish PDF page numbers from printed page numbers whenever they differ.

## Select reading iteratively

During bootstrap, read enough structural material before manifesto v0 to let the book introduce its own questions, vocabulary, and organization; after manifesto v0, use it as one selection lens. During an update, map the whole book first, then use the existing manifesto and any newly discovered book vocabulary to rank chapters or page ranges by whether they:

- directly support or challenge a central hypothesis;
- define a core concept or method;
- fill an important evidence gap;
- conflict with another core source;
- could change project scope, confidence, or the next decision.

Deep-read the highest-value sections within the run's practical limits. Also inspect one plausible section chosen from the book's framing rather than the manifesto's vocabulary. Do not read the entire book merely because it was supplied.

## Source note requirements

Use these reading levels accurately:

- `mapped`: structure and likely relevance identified, but no substantive chapter was closely read;
- `partial`: named chapters or page ranges were closely read;
- `full`: the entire substantive book was examined closely enough to evaluate its overall argument and evidence.

In `note.md`, include:

- reading level and selection rationale;
- exact sections and pages examined;
- sections only skimmed or mapped;
- a relevance map such as `section | pages | likely relevance | status`;
- claims and evidence from examined sections only;
- limitations, tensions, and bibliographic or OCR uncertainty;
- promising unread sections and what future question would justify revisiting them.

Use page-level citations for book claims when possible. A mapped or partially read book may shape search vocabulary and research questions, but only examined passages may support evidence claims in `manifesto.md`.

## Token and attention discipline

- Prefer structural extraction, local text search, and targeted page ranges over placing the whole PDF in context.
- Allocate deeper reading by decision value, not by chapter order or source prestige.
- Stop when additional reading is unlikely to change the provisional or existing manifesto, an indexed source assessment, or the immediate next decision.
- Preserve the relevance map so `update-research-os` can deepen the same book later without starting over.
