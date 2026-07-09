---
slug: loom-paper
name: Loom Paper
version: 1
scheme: dual
colors-light:
  surface: "#fcfcfb"
  page: "#f9f9f7"
  ink: "#0b0b0b"
  ink-2: "#52514e"
  muted: "#898781"
  grid: "#e1e0d9"
  ring: "rgba(11,11,11,0.10)"
  c-sources: "#2a78d6"
  c-synthesis: "#1baf7a"
  c-ideas: "#eda100"
  c-decisions: "#4a3aa7"
  c-ok: "#008300"
colors-dark:
  surface: "#1a1a19"
  page: "#0d0d0d"
  ink: "#ffffff"
  ink-2: "#c3c2b7"
  muted: "#898781"
  grid: "#2c2c2a"
  ring: "rgba(255,255,255,0.10)"
  c-sources: "#3987e5"
  c-synthesis: "#199e70"
  c-ideas: "#c98500"
  c-decisions: "#9085e9"
  c-ok: "#008300"
color-aliases:
  accent: c-decisions
  positive: c-ok
  link: c-sources
typography:
  body-family: system-ui, -apple-system, Segoe UI, sans-serif
  heading-family: inherit
  mono-family: ui-monospace, SFMono-Regular, Menlo, monospace
  base-size: "14px"
  line-height: "1.5"
  heading-weight: "700"
components:
  card-radius: "8px"
  pill-radius: "999px"
  card-border: 1px solid grid
  focus-ring: 0 0 0 3px ring
  max-width: "1160px"
  section-gap: "24px"
---

# Loom Paper

The workbench's native visual system, extracted into a spec. It is the safe default: every
other style in this pack is a departure from this baseline.

## Atmosphere

Warm near-white paper in light mode, soft charcoal in dark. Ink-first hierarchy: content is
almost-black text on quiet surfaces; chrome (navigation, labels, borders) recedes into muted
grays and hairlines. Nothing glows, nothing gradients — the page should read like a well-set
working document, not a product landing page.

## Layer semantics

Each research layer owns one hue, used only as an identity accent (chips, badges, count
pills, left borders) — never as a background wash:

- sources — cool informational blue: raw material, not yet judged.
- synthesis — organizing green: directions that group the material.
- ideas — warm amber: claims still warming into conviction.
- decisions — deep violet: settled, deliberate, weighty.
- ok — reserved green for positive/valid states only.

## Signature moves

- Hairline borders in the grid token separate everything; no drop shadows for structure.
- Layer-tinted chips and count pills carry the layer hue at full strength on neutral ground.
- Tinted translucency comes from mixing a layer color with transparency, never a new hex.
- One reading measure: content column capped at the max-width token, generous side padding.
- The theme toggle is a quiet bordered pill in the navigation, not an icon spectacle.

## Do / Don't

Do let text dominate; do use the layer hue of whatever layer the element belongs to; do keep
interactive affordances flat with border emphasis on hover. Don't introduce colors outside
the palette, don't use pure white/black surfaces in either scheme, don't decorate with
gradients or shadows, don't color body text with layer hues.

## Invariants

Every projection in this style is a single self-contained HTML file making zero external
requests (system font stacks only). Card titles, bodies, and frontmatter values are
untrusted: escape on interpolation, sanitize rendered markdown, guard script-tag breakout in
embedded JSON. Both light and dark are fully styled via prefers-color-scheme plus a
data-theme override toggle.
