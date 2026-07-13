---
id: idea-layer-single-entity
type: idea
tags: [schema]
---

# ADR: the idea layer is a single entity iterated in place, rejecting a GTD-style two-layer split

**Adjudication** (2026-07-08; the state-machine subdivision was superseded by the 2026-07-09
lifecycle simplification -- now two states, exist/archive): the idea layer is not split into
"buffer + processed" layers -- one entity, iterated in place; the append-only log carries all
traceability. **In-place iteration includes auto-merge** (2026-07-09): if a new idea the human
raises is the same judgment as an existing card (duplicate or incremental), the agent merges it
into the old card and logs the merge instead of opening a second card; **conflicts do not count
as mergeable** -- when old and new claims contradict, the disagreement must be presented on the
board as-is for the human to adjudicate.

**Rationale**: the surviving methods share single-entity-many-states (ADR / Issue / Kanban /
Shape Up / Zettelkasten; GTD's inbox is also a state, not an entity), while multi-entity models
die of capture cost (IBIS, Grudin's paradox, see the
[IBIS cautionary tale](../sources/methods/ibis-qoc.md)); a two-layer split adds one move-over
action per idea, violating the product tenet of "structure as simple as possible, constraints as
few as possible".

**Preserved obligations** (the layer is cut, the behavior is not): zero-threshold birth --
[buffer-captures-anything](buffer-captures-anything.md)'s capture behavior converges into the
exist state; evaporation stays allowed -- archiving keeps the log instead of deleting;
[claims-anchor-evidence](claims-anchor-evidence.md)'s anchoring obligation falls on claims put
on the board in output, with no promotion gate remaining.
