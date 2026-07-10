# canvas template: single-canvas (三团) — design spec, not yet built

One infinite canvas, Figma-style zoom and drag. Three clusters map to the three layers;
inside a cluster, cards group into sub-clusters by tag, laid out horizontally. Zoom level is
the semantic level: bird's-eye (clusters) → classification (tag groups) → close reading
(card text).

Edges (= in-card references) are not drawn by default: single-click a card to light up its
adjacent edges, double-click to open the card detail. This on-demand behavior is specific to
this template, not a canvas-wide rule.

Shares every template-independent rule with the rest of the pack (truth-driven, no facts
held, layout derived from references + tags) — those live in the builder, not here.
