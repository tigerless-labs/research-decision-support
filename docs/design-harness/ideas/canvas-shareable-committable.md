---
id: canvas-shareable-committable
type: idea
tags: [canvas]
---

# The canvas is also a sharing medium: commit the built HTML so others can walk the why

Beyond aiding the design work itself, the canvas is how you **explain the design to someone
else** — every card links back through ideas to sources, so handing over the board hands over
the reasoning. That makes the built `canvas.html` worth committing: a collaborator who clones
the repo opens one self-contained file and gets the whole board, no server, no toolchain; wire
it to hosted pages and anyone with the link gets it too. This reverses the earlier
never-commit rule (human adjudication, 2026-07-16): the prohibition protected nothing the
truth/projection split doesn't already protect, and it blocked the cheapest sharing path.

The boundary stays where [drafts-not-state](drafts-not-state.md) drew it: the HTML holds no
facts, is rebuilt wholesale from markdown, and is never edited directly — committing a
projection does not promote it to truth. The builder still refuses to write inside the
workspace; the committed file lives beside it. The same-turn sync discipline now extends to
the committed copy: when the truth changes, the rebuilt `canvas.html` rides in the same
change. Builds on [creation-canvas](creation-canvas.md) (the board is where reasoning becomes
visible — sharing it is sharing the reasoning) and
[judgment-provenance-wedge](judgment-provenance-wedge.md) (the provenance chain is the selling
point; a shareable board is that chain made portable).
