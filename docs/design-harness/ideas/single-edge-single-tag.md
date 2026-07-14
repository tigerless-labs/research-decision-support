---
id: single-edge-single-tag
type: idea
tags: [schema]
---

# Structured facts stay minimal: the reference (association) + the tag (only classification)

(Slimmed 2026-07-14: the "exactly two" exclusivity was superseded by the human's
conflict-schema adjudication — a third fact, the `conflicts` frontmatter field, joined the set.
The minimalism principle itself stands: no open-ended relation-type enum.)

The reference is the association between cards: a markdown link in card A's body pointing to
card B is one edge; the surrounding text may carry a one-line semantic note, but the system
defines no relation-type enum (no dependency / support typed edges — conflict alone earned a
dedicated fact). References go
**forward only**: a card may point only at what it stands on (evidence, predecessor cards it
depends on or revises); "whom I support / who cites me" are downstream relations and are never
written down -- backlinks are derived by projection scans, never double-written. A reference may
point at another idea card, but **cycles are forbidden** -- two cards referencing each other
means either the same judgment that should merge, or one side is actually a downstream relation
(delete that reference and leave it to backlinks).

There is **only one classification: the tag** -- single level (the tag is the top-level
category, no nesting), **at most one per card** (no cross-tagging on a single card -- a card
related to two tags is mixing two judgments and splits into two cards), optional (classify only
when a card truly belongs to a class; no tag means unclassified); no directory tree, and small
clusters emerge from tags ([source-tags-self-classify](source-tags-self-classify.md)
generalized to all three layers).

**Distances and coordinates are not facts and never enter the source of truth**: the canvas
derives its layout by force-direction from the two discrete facts, references (attraction) and
tags (same cluster); when the source changes, the layout is recomputed. Coordinates are never
written back to markdown -- this is the dual of "the canvas holds no facts": markdown holds no
layout either. Schemes that store coordinates (e.g. .canvas JSON) turn every drag into a "fact
change" and pollute the ledger.

Precedents: Zettelkasten/Obsidian -- the wiki-link is the graph, the graph emerges from links,
and graph-view layout is computed on the fly, never persisted; typed-edge taxonomies (IBIS's
three entities) died of capture cost.

[Zettelkasten](../sources/methods/zettelkasten.md): links as structure; the
[IBIS cautionary tale](../sources/methods/ibis-qoc.md): the capture cost of multi-type models;
tag emergence, see [source-tags-self-classify](source-tags-self-classify.md).

Refines [source-tags-self-classify](source-tags-self-classify.md)'s tag mechanism to all three
layers; both kinds of facts are produced by the agent's single derivation step (tagging and
edge-drawing are both readings of relations -- see the "derive links" node in the flow
diagram); a reference edge is stored as the reference line in the card body itself (a card =
title + summary, no fixed sections), so the agent deriving a new relation means adding one
reference in the summary.
