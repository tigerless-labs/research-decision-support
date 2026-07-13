# idea — decision module

**Responsibilities**: the sole home of judgment — the primary work surface before output
exists; once output is generated, it becomes the decision record (the provenance chain,
the rejected paths, the judgment corpus reused across outputs).

**Behavior boundaries**:

- **Only the human creates ideas** (the agent may consolidate scattered observations into
  a draft suggestion, but landing the card is the human's act).
- Exactly two states: **live / archived** — live means present and participating in
  assembly; there is no anchoring/adjudication/adoption workflow and no status label.
- Archival can be triggered by human or agent; the card moves into the `ideas/archive/`
  subdirectory, logged, never deleted.
- When a new idea repeats an existing card's judgment (duplicate/increment), the agent
  **auto-merges** it into the old card and ledgers it; a conflict is not mergeable — the
  disagreement goes on the board as-is for the human to adjudicate.
- **Permanent two-way sync** with output: a human idea lands in both layers the same turn;
  a human output edit is back-calibrated into this layer by the agent (transcription; the
  judgment stays the human's).
- Each node carries an append-only log (birth/update/merge/supersede; pending); the layer
  ledger [logs.md](../../logs.md) records every card change (including body updates) — until
  node-level logs land, it is the only trace of idea changes.

**Provenance**: [output primary](../../ideas/output-primary-after-generation.md) ·
[single-entity ADR](../../ideas/idea-layer-single-entity.md) (its state-machine breakdown
was simplified to two states; see logs 2026-07-09) ·
[the agent thinks but never adjudicates](../../ideas/agent-synthesizes-human-adjudicates.md) ·
[the buffer captures anything](../../ideas/buffer-captures-anything.md).
