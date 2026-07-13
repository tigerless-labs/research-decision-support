---
id: diagrams-in-markdown-native-format
type: idea
tags: [protocol]
---

# System design diagrams must be a visual diagram format in the markdown source itself

System design diagrams in output are **fixed to markdown-native declarative diagram formats**
(currently: mermaid code blocks) -- the source of truth is itself a diagram, not a prose
description with an attached image, nor a hand-drawn object that exists only in HTML. Reasons:
the source renders directly in any host that supports it (GitHub / Obsidian / IDE); diagram
changes go through text diffs, so the ledger can record minimal deltas; the node-to-module
click-through mapping can be declared in the diagram source (`click` lines), and the projection
merely redraws without adding facts
([markdown is the sole source of truth](drafts-not-state.md)). Every node in the diagram carries
two lines, main label + sublabel, with the information set matching the projected version block
by block. Versus ASCII box diagrams: those give full layout control and high information
density, but changing one box means hand-reflowing the whole diagram, diffs are alignment noise
that cannot record minimal deltas, there is no click semantics, and box lines skew under CJK
character widths -- suitable only for one-shot static snapshots; for frequently evolving system
diagrams that need click-through, use the declarative format.
