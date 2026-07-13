# canvas — board projection

**Responsibilities**: the visual face of all cards — the main arena where a human clears
their thinking; the deciding factors are intuitiveness, beauty, clarity.

**Rules (template-independent invariants)**:

- The canvas is **only a visualization layer**: it changes as the markdown truth changes
  (truth moves, board moves), holds no facts of its own, and accepts no writes that bypass
  the truth.
- Edges = in-card references (the agent's derivation step adds reference lines to the summary).
- Layout is derived from two discrete facts — references (gravity) and tags (same cluster);
  distances/coordinates never enter the truth.
- At most one tag per card, so clustering is unambiguous; untagged cards land in the
  unclassified scatter area.
- Doubles as the protocol's in-place manual: before output exists its seat holds a
  standing empty-state placeholder (teaching that the launch right is the human's), layout
  order mirrors process order, and the passively updated side flashes during sync.

**Template (exactly one: the unified canvas — the template-set mechanism retired; there is
only this canvas, one canvas/ layer inside the skill suffices, and the style pack hangs
under it)** — the template fixes only the information architecture and the interaction
contract; visuals belong entirely to the style pack (bounded by the token interface, see
[file-structure](../file-structure.md)):

- **Unified canvas** = single-canvas base + the gallery's strengths merged: one infinite
  canvas, Figma-style zoom/pan, three clusters for the three blocks with tag sub-clusters
  inside; three zoom detents are the gallery's three pages (bird's-eye · clusters /
  classify · tag groups / close-read · cards = grid skim); empty-state in-place teaching
  and red-team injection kept at parity.

**Unified canvas interaction contract (the human's UI adjudication, 2026-07-10)**:

- Layout: three worlds in a row (evidence / ideas / assembly), with the **board block
  centered directly below the three worlds**.
- Tag chips **arranged in rows per cluster** (cluster name labels the row); search lives
  in the toolbar, Enter flies to the hit card.
- Click semantics by zoom detent: **at bird's-eye, clicking a card = fly into close-read
  and select it** (small cards have no content, so outlining is meaningless); at
  classify/close-read detents, click = light neighbors; double-click = detail dialog;
  edges are not drawn by default.
- **Assembly documents participate in reference edges**: at build time the output/board
  document bodies are parsed for links, producing document→card edges; selecting a
  document lights the cards it was assembled from, and a card's detail rail includes an
  "Assembly (cites this card)" derived-backlink section.
- **Mermaid diagrams enlarge on click inside a card**: full-screen top-layer dialog,
  auto-fit to viewport, scroll to zoom, drag to pan, click blank or Esc to close;
  in-diagram click-through is preserved.
- **A standing style switcher in the toolbar, live reskin** (the human's UI adjudication,
  2026-07-10): options come from the style pack index; switching swaps the whole CSS pack
  with zero rebuild; the last choice is remembered in the browser (a projection-layer
  preference, never entering the truth), defaulting to pin-and-paper. A `--css` pinned
  build = one fixed style, no switcher.
- **Three layers, three card grammars** (the human's UI adjudication, 2026-07-10): every
  style must give the three layers three distinct card forms (structure, border, symbols,
  …), never distinguished by accent color alone; each style defines its grammar in its
  design.md `### single-canvas` section, guarded by a test invariant.
- **Style hooks** (option C, 2026-07-13): the template stays singular, but the corners CSS
  cannot reach are opened as standing hooks — one empty chrome shell per card, one ordinal
  slot per world title (hidden by default; the style's CSS decides visibility and form);
  the reference edge's shape is declared by a style CSS variable (curve/straight, read at
  draw time, taking effect instantly on reskin), while color/weight/dash were always
  CSS-overridable. The reskin slot's style element is named; hook default styles live
  outside it and are not overwritten by reskins. Layout-level differences (coordinates,
  sizes) remain shared across styles, out of hook range.
- Mermaid rendering look is driven by the selected style behind two fixed switches, truth
  and diagram kinds unchanged: `look: handDrawn` (mermaid v11's built-in hand-drawn look),
  and `themeVariables` pulled dynamically from the current style's tokens at render time,
  taking effect instantly with the switcher. The token map must cover **every text and
  container surface mermaid renders** — node/edge/cluster labels and cluster fills included —
  because mermaid's built-in themes hardcode label colors that a dark palette cannot survive;
  no theme default may reach the screen. Guarded by a test invariant.

**Build (fixed script, settled 2026-07-10)**:

- There is exactly one build entry, `build_canvas.py`: **the workspace path is the only
  required input**, and one command renders the complete canvas HTML (card collection,
  edge derivation, layout, data embedding, dependency inlining all built in); no second
  build path exists; the artifact goes only to a temp dir or an artifact, never into the truth.
- The build validates before it projects: both validators run as a gate, and any problem
  aborts the build with the full problem list and **no HTML output** — broken truth is
  never projected, and the failure surfaces where the agent must act on it. A freshly
  bootstrapped workspace (zero cards) is valid and renders its empty-state canvas.
- Template and style fully separated: structure is only `canvas/template.html` (with a CSS
  injection slot; the old design-draft spec is deleted — the interaction contract's sole
  truth is this document), and all CSS belongs to the style pack `canvas/styles/`;
  **changing style changes only CSS** (`--css` takes the style file); copying the template
  or writing another script for looks is forbidden. The template is the structural
  contract: the agent never edits the HTML projection; the writable surfaces are the
  markdown truth and style CSS only.
- Style CSS is **precompiled into the repo, one format**: each style dir holds one
  `canvas.css` (the compiled artifact of the design.md spec — the spec is the truth, so
  changing the spec means recompiling), `--css` points straight at it with zero wait; the
  validator checks the canonical tokens exist in both light and dark palettes and bans
  external reach. The default build embeds the whole pack's CSS with the switcher
  (initially showing pin-and-paper — the canvas's native look); `--css` embeds a single
  style only.
- Residuals to clear: small-screen experience, large-card-count performance (the default
  dark palette resolved itself when the default style returned to the style pack —
  pin-and-paper ships both palettes). The two forerunner templates (tabbed gallery /
  single-canvas three-cluster) were archived when the merge completed.

**Provenance**: [the single canvas subsumes the gallery](../../ideas/single-canvas-subsumes-gallery.md) ·
[tabbed gallery template](../../ideas/archive/tabbed-gallery-template.md) ·
[exactly two facts: references + tags](../../ideas/single-edge-single-tag.md) ·
[protocol taught in place](../../ideas/protocol-discoverability-in-situ.md) ·
[creation canvas](../../ideas/creation-canvas.md) ·
[single canvas, three clusters](../../ideas/archive/single-canvas-clustered-graph.md) ·
[edges on demand](../../ideas/canvas-edges-on-demand.md) ·
[projections hold no facts](../../ideas/drafts-not-state.md) ·
[style–canvas orthogonality](../../ideas/style-canvas-orthogonality.md) ·
[fixed builder, style is CSS-only](../../ideas/canvas-fixed-builder-style-css-only.md).
