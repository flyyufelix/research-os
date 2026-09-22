# Literature Scout scope

See the [Literature Scout guide](README.md) for setup, scheduling, candidate review, and optional email delivery.

Edit this file after `manifesto.md` has been created. Replace the prompts below with settings suitable for your project.

## Research focus

- Domains: derive from `manifesto.md`
- Search vocabulary: use the manifesto vocabulary and add discipline-specific synonyms here
- Nearby topics to include: none specified
- Topics to exclude: none specified

## Retrieval methods

Use every enabled retrieval method that is available in the current environment. “Required” means that the method must be attempted and its outcome reported; an unavailable method should degrade coverage rather than abort the run.

- Web search: required
  - Use for broad discovery, recent developments, official sources, research organizations, grey literature, research blogs, news leads, terminology discovery, and verification.
- OpenAlex: required when accessible
  - Prefer the official OpenAlex MCP when available.
  - Use for structured metadata, stable identifiers, citation and reference traversal, related works, topics, authors, and institutions.
- Multi-source scholarly MCP: required when available
  - Preferred connector: `paper-search-mcp`
  - If it is unavailable, use another available scholarly MCP or connector covering relevant sources such as Semantic Scholar, Crossref, arXiv, PubMed, CORE, OpenAIRE, or Unpaywall.
- Publisher or repository verification: required for shortlisted findings when an authoritative record is accessible
- Citation expansion: one hop from relevant core sources and strong new candidates

Do not install software, configure an MCP, request credentials, or expose secrets during a scout run. If a method is unavailable or fails, continue with the remaining methods, name the missing method, and explain the resulting coverage limitation. Do not call the search comprehensive or exhaustive when a required method was unavailable or failed materially.

## Enabled source categories

Search only sources that are enabled here and accessible in the current environment.

- Scholarly discovery: enabled
  - OpenAlex
  - Crossref
  - Semantic Scholar
  - discipline-appropriate scholarly web search
- Primary repositories, publishers, and proceedings: enabled
  - use sources appropriate to the research domain
- Official university, laboratory, government, and research-organization posts: enabled
- Research blogs and scholarly commentary: enabled as leads
- General news and broader web search: enabled as leads when they point to relevant research or policy developments
- Social posts: disabled by default; enable only as discovery leads and verify claims against stronger sources

Blog posts, news, and social posts are leads, not substitutes for primary evidence.

## Run limits

- Lookback period: 30 days
- Maximum findings: 5
- Languages: English; add others when the researcher can evaluate them
- Timezone: replace with the researcher's local IANA timezone, for example `Asia/Hong_Kong`
- Resurface previously seen items: only for a meaningful new version, correction, retraction, publication, or follow-up

## Inclusion priorities

- Direct relevance to a manifesto question, hypothesis, uncertainty, evidence gap, or decision
- Evidence that challenges the working thesis or supports a competing hypothesis
- Follow-ups, corrections, or related work around core sources
- Primary or official sources with enough accessible material for a defensible relevance assessment

## Exclusions

- Items with no explicit manifesto connection
- Promotional pages with no identifiable evidence
- Duplicate coverage that adds no new source or information
- Material outside the researcher's stated ethical, geographic, population, or disciplinary boundaries

## Email delivery

- Enabled: no
- Authorized recipient: none
- Format: full-detail HTML rendered with `skills/scout-literature/assets/email-report-template.html`

Do not infer a recipient or send email unless this section explicitly enables delivery and supplies an authorized address. Never commit a personal address or credential to a public repository.
