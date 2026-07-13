---
id: style-canvas-orthogonality
type: idea
tags: [canvas]
---

# Style and canvas are orthogonal: style is pure UI, canvas sets the information architecture, the binding is lifted into the skill

A style pack carries UI only -- palette (abstract accent roles), typography, geometry, mood,
presentation form -- and no content semantics; the canvas template owns the information
architecture and the interaction contract exclusively. The content-layer-to-accent binding is
written in exactly one place, SKILL.md, so a style holds for any content and works with any
canvas. A style may attach a section of custom presentation for a given canvas (the switcher
and the card forms are style signatures); otherwise the canvas's default presentation applies.
Layout variants (vertical tabs / numbered track / command line / focus card / level select)
belong to style as long as the information architecture is unchanged -- no new canvas is opened
for them.

2026-07-10 convergence (human adjudication): with the canvases merged into the single unified
canvas, orthogonality reduces to a token interface convention -- the styles/ directory moves
under canvas/ and the canvas_renderings selector is retired, but the boundary stands: style
writes only tokens and presentation, never touches canvas structure, and stays swappable
wholesale. The new five styles draw on the
[frontend-slides](../sources/github/frontend-slides.md) presets and the Bold pack; the
specification approach follows [one engine, many schemas](one-engine-many-schemas.md), with
presentation attached to the [tabbed gallery template](archive/tabbed-gallery-template.md).
