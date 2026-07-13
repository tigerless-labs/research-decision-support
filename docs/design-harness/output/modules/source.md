# source — evidence module

**Responsibilities**: the sole entry point for reference material and one's own
observations; holds every evidence card and provides the anchor for every claim.

**Behavior boundaries**:

- The agent automatically intakes every source that appears in a session, one source one card.
- No topic directory tree; type containers are thin shells, and topical structure emerges from tags.
- Type directory names have no preset list: the agent picks (or creates) one at intake;
  the canvas badge projects the directory name verbatim, and no type dir means no badge.
- Graded at intake (review > paper > doc > post; the grading table is configurable per scenario).
- Tag classification happens in the reference-derivation pass and is **optional** — set by
  the human or suggested by the agent; an untagged card is legal, gets referenced and
  assembled as usual, and lands in the canvas's unclassified area awaiting a tag.
- Stores only "what the material says"; judgment never enters this layer.

**Provenance**: [tag self-classification](../../ideas/source-tags-self-classify.md) ·
[evidence grading](../../ideas/evidence-grading.md) ·
[claims anchor evidence](../../ideas/claims-anchor-evidence.md).
