---
id: creation-canvas
type: idea
tags: [canvas]
---

# Creation canvas: scattered ideas go on the board in real time and auto-link; the human refines them on the board into the final decision

The form that fits this project better than a "decision model" is a **creation canvas**:
scattered ideas -- read out of reference material or freshly surfaced -- go on the board one by
one, each new entry appearing instantly as a node and auto-linking to existing nodes; relations
are derived by the agent from content, the human never drags edges by hand. Facing a graph that
grows with input, the human combines, merges, and prunes on the board, refining scattered points
into the final decision. The main battlefield is **helping people clarify their thinking**; the
deciding factor is UI+AI that is intuitive, good-looking, and clear. The canvas is a real-time
projection of the markdown source of truth, not a new place where facts live.

Every node carries its own **logs**: where the idea was born, the content and reason of every
update, the process of being merged or pruned -- append-only, readable by clicking on the board.
The graph answers "what does it look like now"; the logs answer "how did it get this way".

The former vibe-code design board (where design intent lands, downstream of decision cards) is
folded in as this card's downstream extension: the same board synthesizes ideas upward into
decisions and carries decisions downward into design.

Obsidian ecosystem survey (2026-07): automatic linking is already commoditized --
[InfraNodus](../sources/products/infranodus.md) auto-builds graphs and spots gaps, and Smart
Connections / Auto Linker and peers do semantic and title-level auto-linking -- but all of them
stop at "relation discovery"; none produces a decision. The open slot is exactly the second half
after linking. The original evidence for the vibe-code extension (spec-kit / BMAD validating the
category, [tribal knowledge](../sources/blogs/tribal-knowledge-why.md) proving the why evaporates
first) still holds.

Builds on [judgment-provenance-wedge](judgment-provenance-wedge.md) (the canvas is where
judgment-to-decision becomes visible; node logs are provenance turned into UI),
[read-tag-judge-loop](archive/read-tag-judge-loop.md) (judgments dropped while reading are the material
that goes on the board), [drafts-not-state](drafts-not-state.md) (the board is a projection,
markdown is the source of truth), and [one-engine-many-schemas](one-engine-many-schemas.md) (the
canvas is the engine's view layer; swapping domains swaps schema and board);
[buffer-captures-anything](archive/buffer-captures-anything.md)'s triage products are the on-ramp to the
board. To be weighed in [decisions/](../index.md): how the canvas hands off to decision cards;
the derivation criteria for automatic linking.
