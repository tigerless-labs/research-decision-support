---
id: tags-in-layer-index
type: idea
tags: [classification]
---

# All tags surface in each layer's index: retrieval goes through derived indexes, no classification layer

A tag's source of truth lives in exactly one place -- the `tags:` field of the card's
frontmatter. Retrieval friction is not solved by adding a structural layer (a classification
layer duplicates facts and inevitably rots) but by a **derived index**: each layer's index.md
groups by tag as **subheadings**, formatted `TAG: one line on why this is a class`, with member
rows listed under each group; unclassified cards sit flat in the heading-less section at the
end. The agent regenerates the index in the same turn as any card change, so it never lags. To
change a tag, change only the card -- the index follows automatically.

Precedent: Luhmann's Zettelkasten kept a register (keyword index) beside the card boxes as the
retrieval entry point -- the index is a derivative, not a structural layer.

The register convention of [Zettelkasten](../sources/methods/zettelkasten.md); the reasons a
classification layer was rejected are the same as
[source-tags-self-classify](source-tags-self-classify.md) (fixed classification always
misfits).

Tag uniqueness comes from [single-edge-single-tag](single-edge-single-tag.md); tagging timing
and optionality, see [source-tags-self-classify](source-tags-self-classify.md); the never-lags
discipline matches [output-auto-refresh](output-auto-refresh.md).
