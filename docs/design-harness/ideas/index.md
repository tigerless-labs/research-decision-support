# ideas -- human-created, two states (exist / archive), every card leaves a trail

Only humans can create cards; archived cards move to [archive/](archive/); changes are recorded in
[logs.md](../logs.md). Subheadings are tags (single level, at most one per card, optional); the
heading-less section at the end is unclassified.

## positioning: what the product is, who it serves, how humans and agents divide the work

- [Judgment-provenance wedge](judgment-provenance-wedge.md) -- the provenance chain is the selling
  point.
- [Agent thinks, does not adjudicate](agent-synthesizes-human-adjudicates.md) -- synthesis belongs
  to the agent, adjudication to the human.
- [Five persona scenarios](four-persona-scenarios.md) -- video creator / developer / vibe coder /
  researcher / life decision-maker.

## evidence: how material comes in, how it gets graded, how claims are anchored

- [Buffer captures anything](buffer-captures-anything.md) -- zero-threshold entry; structure is the
  agent's job afterwards.
- [Claims anchor evidence](claims-anchor-evidence.md) -- claims put on the board in output must
  anchor back to sources.
- [Evidence grading](evidence-grading.md) -- sources are not equal-weighted; grading is
  configurable per scenario.

## classification: where tags come from and where they show up

- [Source tags self-classify](source-tags-self-classify.md) -- tags are assigned by the agent;
  cards self-organize.
- [Tags in layer index](tags-in-layer-index.md) -- retrieval goes through derived indexes; no
  classification layer.

## schema: the minimal structural conventions for entities and relations

- [Idea layer single entity, iterated in place](idea-layer-single-entity.md) -- ADR: single
  entity + log; its state-machine subdivision has been simplified to two states (logs 2026-07-09).
- [References + tags, minimal facts](single-edge-single-tag.md) -- references forward-only and
  acyclic, tags single and optional; distances and coordinates are all derived (its "exactly
  two" exclusivity superseded 2026-07-14).
- [Conflicts get a schema](conflict-schema-red-edges.md) -- optional `conflicts: [<id>]` on the
  newer card, red edges on the canvas; the field lives exactly as long as the conflict.
- [One engine, many schemas](one-engine-many-schemas.md) -- switching scenarios swaps the schema,
  not the engine.
- [Board free surface](board-freeform-layer.md) -- a fourth directory, one file, one board;
  freedom belongs to the human; furthest downstream, may not be referenced.

## sync: the consistency discipline between ideas and output

- [Layers decoupled, drift reminder only](layers-decoupled-drift-reminder.md) -- no sync either
  way; layers reconnect only at human-ordered assembly; one far-behind reminder, never nagging.
- [Output is human-initiated, ideas become the decision record](output-primary-after-generation.md)
  -- first assembly on the human's word; direct output edits calibrate backward into ideas; the
  idea layer keeps provenance and rejected paths.

## canvas: shape and behavior of the visualization layer

- [Creation canvas](creation-canvas.md) -- the canvas replaces the decision model as the form.
- [Unified canvas](single-canvas-subsumes-gallery.md) -- the two templates merge into the single
  canvas, taking the best of each.
- [Fixed script, styles swap CSS only](canvas-fixed-builder-style-css-only.md) -- one script, one
  required input renders the canvas; the template keeps a CSS slot.
- [Edges appear on demand](canvas-edges-on-demand.md) -- none drawn by default; a single click
  lights up neighbor edges.
- [Style-canvas orthogonality](style-canvas-orthogonality.md) -- style is pure UI, canvas sets the
  IA, the binding is lifted into the skill.

## protocol: conventions and teaching surface of the portable core

- [Projections hold no facts](drafts-not-state.md) -- markdown is the sole source of truth.
- [Protocol decoupled from runtime](runtime-agnostic-protocol.md) -- the contract binds files, not
  a CLI.
- [Protocol teaches in situ](protocol-discoverability-in-situ.md) -- empty states + timely hints +
  action receipts, no manual.
- [Diagrams as the native format](diagrams-in-markdown-native-format.md) -- system design diagrams
  in markdown are mermaid visual format, not prose with attached images.
- [Principles as bullets, not paragraphs](principles-as-bullets.md) -- one bullet, one principle;
  each can be referenced / modified / ledgered on its own.

## skill: how the operating skill discovers and binds workspaces

- [Many workspaces, freely named](workspaces-many-and-freely-named.md) -- multiple workspaces per
  host, any directory name; the config pointer is the registry, discovery never trusts the name.
- [SKILL.md and protocol fuse into one file](skill-and-protocol-single-file.md) -- structure →
  workflow → disciplines → quickstart; definitions before procedures, "never" rules close the
  body; templates inline, big option sets stay as references.

---

*unclassified*

- [Read-tag-judge loop](read-tag-judge-loop.md) -- the minimal loop of human-agent interaction.
