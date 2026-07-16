---
id: canvas-fixed-builder-style-css-only
type: idea
tags: [canvas]
---

# Canvas builds converge on one fixed script: the workspace path is the only required input, switching styles swaps CSS only

How the [unified canvas](archive/single-canvas-subsumes-gallery.md) gets built is now fixed as **one
script** (`build_canvas.py`): the agent feeds it the workspace path and it renders the complete
canvas HTML -- card collection, edge derivation, layout, and data embedding are all built in; no
second build path exists. Template (structure + interaction JS) and style (CSS) are separated --
the template keeps one CSS injection slot, filled with the current style by default; switching
styles **swaps only the CSS file** (passed via `--css`); opening another template or writing
another script for the sake of looks is forbidden.

**Live switching (re-iterated 2026-07-10)**: style choice belongs to the human and is exercised
right on the canvas -- a switcher sits permanently in the toolbar, the full set of precompiled
CSS is embedded, and reskinning needs zero rebuilds; the choice is a projection-layer preference
stored in the browser, not in the source of truth. `--css` remains for locked-down builds (pin a
single style, no switcher).

Motivation: the unified UI once lived only in temp directories and artifacts; republishing meant
hand-stitching the data, and a schema mismatch blanked the whole page (hit on 2026-07-10); the
fixed script reduces "md changed, rebuild and publish in the same turn" to a single command,
while style packs stay swappable wholesale through the CSS slot
([style-canvas orthogonality](style-canvas-orthogonality.md)).

**Precompilation (added the same day, 2026-07-10)**: rather than compiling on demand at selection
time, compile every style's CSS ahead of time into the repo -- each style directory carries one
`canvas.css` (the compiled product of the design.md spec; the spec remains the source of truth,
and changing the spec forces a recompile), so whichever `--css` the user picks points straight at
it, zero wait. **Format unification (iterated again the same day)**: canvas/ holds no CSS at all
-- the default style also returns to a style pack, and the default build =
`styles/pin-and-paper/canvas.css` (the canvas's native look), identical in format and validation
to every other style, never rewritten by a style switch.
