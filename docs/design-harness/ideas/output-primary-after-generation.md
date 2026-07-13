---
id: output-primary-after-generation
type: idea
tags: [sync]
---

# Output is human-initiated; after generation, ideas and output stay in sync forever (two-way)

Assembly of output is **initiated by the human**; idea changes no longer auto-trigger first
generation. The core invariant: **ideas and output never fall out of sync** -- whichever side
the human edits, the agent propagates the change to the other side in the same turn:

- The human raises an idea / decision -> update ideas **and** output together; if output has not
  been generated yet, update ideas only.
- The human edits output -> the agent **calibrates backward** into ideas (updating existing
  cards or ghostwriting new ones; a ghostwritten card is still the human's judgment -- the agent
  merely transcribes, so "only humans create ideas" is not violated).
- Conflicts resolve in output's favor (after generation it is the primary work surface).

The idea layer is not abolished once output exists; it changes roles: from work surface to
**decision record** -- (1) the provenance chain (output element -> idea -> source) is the
product's wedge; (2) archived cards preserve the rejected paths, the negative space that guards
against after-the-fact revision; (3) the same batch of ideas can assemble multiple outputs. The
precedent is ADR (the append-only why) coexisting long-term with living design docs (the
current what).

For the practice of ADR coexisting with living docs see
[ADR](../sources/methods/adr-method.md); provenance as the selling point, the
[judgment-provenance wedge](judgment-provenance-wedge.md); full records against revision
attempts, the irreversible-decision scenarios of
[four-persona-scenarios](four-persona-scenarios.md).

Calibrates the directional semantics of [output-auto-refresh](output-auto-refresh.md):
auto-refresh acts only on **existing** output (idea change -> re-derive affected elements),
first generation belongs to the human; the added reverse flow (output change -> ideas) is
likewise carried by the agent and recorded in the logs.
