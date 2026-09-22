# Manifesto versioning

Use this procedure whenever creating, proposing, approving, or publishing a version of `manifesto.md`. It provides a readable history without requiring Git.

## Core model

- `manifesto.md` is the latest approved research position.
- An agent may prepare a change, but a researcher must explicitly approve it before it replaces the current manifesto.
- Bootstrap is the only exception: when no approved manifesto exists, `manifesto.md` may contain proposed `v0.1.0` with status `Awaiting review`.
- `CHANGELOG.md` is the append-only decision history.
- `versions/manifesto/` contains immutable snapshots of approved versions.
- Do not create a new version for spelling, formatting, or link-only repairs that do not change meaning.

## Version numbers

Use `vMAJOR.MINOR.PATCH`.

- Before the first formal research baseline, remain in `v0.x.x`.
- Increment `MINOR` and reset `PATCH` to zero for a substantive intellectual change: the central question, thesis, definitions, scope, competing hypotheses, confidence, or research orientation.
- Increment `PATCH` for an approved evidence, source-link, search-vocabulary, uncertainty, clarification, or other retrieval-oriented update that does not change the central position.
- Use `v1.0.0` when the researcher explicitly designates the manifesto as the first formal, submitted, or otherwise stable baseline.
- After `v1.0.0`, increment `MAJOR` only for an explicitly approved fundamental reset; otherwise use `MINOR` and `PATCH` by the same rules.

If one approved release contains both minor and patch-level changes, use the higher increment once. Never infer that a manifesto is formal or submitted.

## Version record

Place this human-readable block near the top of `manifesto.md`, after its title:

```markdown
## Version record

- Version: v0.2.1
- Status: Approved
- Updated: 2026-09-22T14:30:00+08:00
- Based on: v0.2.0
- Prepared by: Codex — Research OS Update Agent
- Approved by: Researcher name
- Change summary: Added evidence and clarified the principal uncertainty.
```

For the first version, use `Based on: none`. Use an ISO 8601 timestamp with a numeric UTC offset derived from the actual environment. Record the most specific truthful agent identity available, but do not invent a model name, role, task ID, person, or timestamp. If approval is explicit but the researcher's name is unavailable, use `Approved by: Researcher (name not supplied)`.

During the initial bootstrap, use `Status: Awaiting review`, `Approved by: Pending`, and `Version: v0.1.0`. After approval, update the status, approval field, timestamp, and any final change summary before publishing the snapshot.

## Proposal and approval

For an existing approved manifesto:

1. Determine the proposed version from the highest approved version, not from an abandoned proposal.
2. Present the proposed version, exact changes, change rationale, evidence and counterevidence, uncertainty, and expected downstream consequences.
3. Do not edit `manifesto.md`, create its snapshot, or append a release entry until the researcher explicitly approves the proposal.
4. Treat requested revisions to the proposal as part of the same proposed version until approval.

Approval applies only to the proposal shown. If the accepted content changes materially afterward, obtain approval again.

## Publishing an approved version

After explicit approval:

1. Confirm that the current approved version has an immutable snapshot. For a legacy manifesto without version metadata, ask the researcher to approve it as the versioning baseline before assigning `v0.1.0`; do not guess its approval state.
2. Apply only the approved changes to `manifesto.md` and update its version record.
3. Save an identical snapshot as `versions/manifesto/manifesto_vMAJOR.MINOR.PATCH_YYYY-MM-DD.md`, using the local date from the version timestamp. Never overwrite an existing snapshot; report a filename or content conflict.
4. Append one row to `CHANGELOG.md` containing the version, timestamp, change summary, rationale, preparing agent, and approving researcher. Keep entries oldest-first so the file remains append-only. Do not rewrite older rows to label them superseded; a later approved version already establishes that history.
5. Verify that the live manifesto and new snapshot match exactly, the version number is unique and sequential, the timestamp and attribution agree across records, and all links remain valid.

A successful release must leave the manifesto, snapshot, and changelog consistent. If only part of the publication succeeds, report the partial failure and do not claim that the version was published successfully.

## Changelog format

Create `CHANGELOG.md` when the first version is approved:

```markdown
# Manifesto changelog

This append-only log records approved Research OS manifesto releases. Earlier versions are preserved under `versions/manifesto/`.

| Version | Timestamp | Change | Why | Prepared by | Approved by |
|---|---|---|---|---|---|
| v0.1.0 | 2026-09-22T14:30:00+08:00 | Created the initial manifesto | Established the first research baseline | Codex — Research OS Bootstrap Agent | Researcher name |
```

Keep summaries compact but specific. The `Change` column records what changed; `Why` records the research reason for accepting it.
