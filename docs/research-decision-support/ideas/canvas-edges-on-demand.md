---
id: canvas-edges-on-demand
type: idea
tags: [canvas]
---

# Canvas edges appear on demand: single-click to see relations, double-click for detail

Relations between nodes are derived by the agent in real time and stored persistently, but **no
edges are drawn by default** -- a screen full of lines is cognitive load, not information; the
graph's default state is a clean scatter field, and edges are query results, not background.
Interaction has two levels: **single-click** a node to light up only its direct neighbor edges
(what this idea relates to); **double-click** to open the node's detail -- body, logs, evidence
anchors. Whether the three blocks (source / idea / design) share one screen or split is deferred.

This project's map page has already validated the load-reducing effect of "hover lights only
direct neighbors" (full-chain highlighting was rejected); the counterexample is
[InfraNodus](../sources/products/infranodus.md)-style full-graph edges -- a hairball on first
paint, with influence ranking drowned in visual noise.

Refines [creation-canvas](creation-canvas.md) -- "real-time automatic linking" is made precise as
**derive in real time, render on demand**. To be weighed in [decisions/](../index.md): the three
blocks on one screen vs split screens; whether single-click neighbors are tiered by hop count.
