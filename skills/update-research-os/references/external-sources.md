# External Sources

Use this procedure for papers, books, reports, webpages, and videos. Store external evidence under `library/`.

## Every source

- Preserve the supplied original unchanged or record a stable URL.
- Create a stable lowercase ID, preferably `author-year-short-title`.
- Create `library/sources/<source-id>/note.md` and add or update one row in `library/_index.md`.
- Record title, authors or creator, publication date, URL or DOI, access date, source type, and bibliographic uncertainty.
- Mark reading level accurately as `metadata-only`, `abstract`, `mapped`, `partial`, or `full`; state exactly what was examined. Use `mapped` for a long-form source whose structure and likely relevance were mapped without close reading of a substantive section.
- Separate source claims from agent interpretation.
- Record method or evidence, findings, limitations, project relevance, tensions with existing material, and questions raised.
- Never infer causation, universality, or full verification beyond what was examined.

## Choose reading depth

Use two passes. First inspect enough metadata, abstract, and relevant content to judge the source's role. Then choose the least depth that supports a reliable project assessment:

- Use `metadata-only` or `abstract` for discovery records that cannot yet support substantive claims.
- Use `mapped` for a long-form source whose structure, vocabulary, and likely relevant sections were identified without closely reading a substantive section.
- Use `partial` for contextual, supporting, low-priority, or tangential sources when selected sections are enough to index their relevance and limits.
- Promote to `full` when the source directly supports or challenges a central hypothesis, may change the manifesto's thesis, scope, definitions, or confidence, conflicts with a core source, requires methodological or appendix detail to evaluate an important claim, or the researcher requests a full reading.

Base the decision on research value, not prestige, file length, or a blanket default. A `full` reading must examine all relevant main text, methods, results, figures, tables, limitations, and supporting appendices; it need not read references or unrelated supplementary material line by line. Record both the chosen level and its rationale under `Material examined and reading-depth rationale`. Revisit and promote a partial source later if its decision value increases.

## PDF papers and reports

- Copy a supplied PDF unchanged as `source.pdf`.
- Extract text when useful, but inspect tables, figures, equations, or layout visually when they affect interpretation.
- Do not label the source `full` unless its complete relevant content was examined.

## Long PDF books and documents

Follow [long-pdf-books.md](long-pdf-books.md). Preserve the source, build a relevance map, and selectively read by project decision value rather than processing the PDF linearly.

## YouTube videos

- Preserve the URL and available metadata in `source.md`; do not download the video unless explicitly requested and permitted.
- Save an available transcript as `transcript.md`, retaining timestamps when possible.
- Record whether the transcript is official, automatic, researcher-supplied, partial, or complete.
- Link claims in `note.md` to timestamps when available.
- Distinguish `video watched` from `transcript reviewed`; never claim both without doing both.

## Webpages

- Record the stable URL, access date, author or organization, and publication or revision date when available.
- Save source text only when useful and permitted. Keep quotations short and traceable.
