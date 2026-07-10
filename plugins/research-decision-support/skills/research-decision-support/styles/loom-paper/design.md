---
slug: loom-paper
name: Loom Paper
version: 2
scheme: dual
colors-light:
  surface: "#fcfcfb"
  page: "#f9f9f7"
  ink: "#0b0b0b"
  ink-2: "#52514e"
  muted: "#898781"
  grid: "#e1e0d9"
  wash: "#f1f1ed"
  accent-d: "#c2410c"
  ring: "rgba(11,11,11,0.10)"
  accent-a: "#2a78d6"
  accent-b: "#eda100"
  accent-c: "#4a3aa7"
  positive: "#008300"
colors-dark:
  surface: "#1a1a19"
  page: "#0d0d0d"
  ink: "#ffffff"
  ink-2: "#c3c2b7"
  muted: "#898781"
  grid: "#2c2c2a"
  wash: "#232322"
  accent-d: "#e2673a"
  ring: "rgba(255,255,255,0.10)"
  accent-a: "#3987e5"
  accent-b: "#c98500"
  accent-c: "#9085e9"
  positive: "#008300"
color-aliases:
  accent: accent-c
  positive: positive
  link: accent-a
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

## Accent roles

Each accent owns one hue, used only as an identity mark (chips, badges, count pills, left
borders) — never as a background wash:

- accent-a — cool informational blue: calm, matter-of-fact.
- accent-b — warm amber: attention without alarm.
- accent-c — deep violet: deliberate and weighty — the style's default accent.
- accent-d — burnt sienna: the hand-made, manual mark.
- positive — reserved green for positive/valid states only.

## Signature moves

- Hairline borders in the grid token separate everything; no drop shadows for structure.
- Accent-tinted chips and count pills carry their hue at full strength on neutral ground.
- Tinted translucency comes from mixing an accent with transparency, never a new hex.
- One reading measure: content column capped at the max-width token, generous side padding.
- The theme toggle is a quiet bordered pill in the navigation, not an icon spectacle.

## Do / Don't

Do let text dominate; do use the accent role the element belongs to; do keep
interactive affordances flat with border emphasis on hover. Don't introduce colors outside
the palette, don't use pure white/black surfaces in either scheme, don't decorate with
gradients or shadows, don't color body text with accent hues.
