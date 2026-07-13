---
id: drafts-not-state
type: idea
tags: [protocol]
---

# HTML holds no facts: browser annotations are drafts, markdown is the source of truth

The page can be rebuilt wholesale with zero loss; annotations dropped while reading live in
browser-local storage and flow back into the cards via exported patches. This preserves the
agent-native form (the agent reads and writes markdown, the human views the rendering) and avoids
introducing a server. This is exactly the difference from
[Elicit](../sources/products/elicit.md): its tables are the product's database; this project's
"tables" are only projections of markdown.

**Sync discipline** (human adjudication, 2026-07-09): every change to the markdown source of
truth must be followed by **rebuilding and republishing the HTML projection in the same turn**;
the editing order is always **markdown first, then sync HTML**; editing only the HTML is strictly
forbidden -- "independent editing" does not exist as an action on the projection.
