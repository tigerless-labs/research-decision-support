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
  newer card declares it in its `conflicts` frontmatter (red edge on the canvas) and the
  disagreement waits as-is for the human to adjudicate; the field lives exactly as long
  as the conflict.
- **Independent of output; sync runs on the human's command**: ideas diverge freely (may
  contradict, may pile up); idea → output re-derivation happens only when the human orders
  a sync. A human output edit is back-calibrated into this layer automatically (transcription;
  the judgment stays the human's).
- Each node carries an append-only log (birth/update/merge/supersede; pending); the layer
  ledger [logs.md](../../logs.md) records every card change (including body updates) — until
  node-level logs land, it is the only trace of idea changes.

**Provenance**: [sync on command](../../ideas/sync-on-command-layers-independent.md) ·
[conflicts get a schema](../../ideas/conflict-schema-red-edges.md) ·
[output primary](../../ideas/output-primary-after-generation.md) ·
[single-entity ADR](../../ideas/idea-layer-single-entity.md) (its state-machine breakdown
was simplified to two states; see logs 2026-07-09) ·
[the agent thinks but never adjudicates](../../ideas/agent-synthesizes-human-adjudicates.md) ·
[the buffer captures anything](../../ideas/archive/buffer-captures-anything.md).
