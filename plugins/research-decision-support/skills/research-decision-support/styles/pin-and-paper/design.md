---
slug: pin-and-paper
name: Pin & Paper
version: 1
scheme: light
colors-light:
  surface: "#f8f1d6"
  page: "#efe56a"
  ink: "#1f3a8a"
  ink-2: "#2d4fb8"
  muted: "#7d86ad"
  grid: "#e0d494"
  wash: "#f5eca0"
  ring: "rgba(31,58,138,0.28)"
  accent-a: "#2d4fb8"
  accent-b: "#a3552e"
  accent-c: "#8a6a2e"
  accent-d: "#c2452e"
  positive: "#3e7d4e"
colors-dark:
  surface: "#262214"
  page: "#171509"
  ink: "#e8e0bf"
  ink-2: "#c2b98f"
  muted: "#857d5c"
  grid: "#3a3520"
  wash: "#2e2a18"
  ring: "rgba(232,224,191,0.16)"
  accent-a: "#8fa3e8"
  accent-b: "#d08a5a"
  accent-c: "#c9a66b"
  accent-d: "#e07a63"
  positive: "#6da97c"
color-aliases:
  accent: accent-a
  positive: positive
  link: accent-a
typography:
  body-family: Segoe Print, Bradley Hand, Chalkboard SE, Comic Sans MS, cursive, system-ui
  heading-family: Segoe Print, Bradley Hand, Chalkboard SE, Comic Sans MS, cursive, system-ui
  mono-family: ui-monospace, SFMono-Regular, Menlo, monospace
  base-size: "14px"
  line-height: "1.6"
  heading-weight: "700"
components:
  card-radius: "3px"
  pill-radius: "999px"
  card-border: 2px solid ink
  focus-ring: 0 0 0 2px ring
  max-width: "1160px"
  section-gap: "28px"
---

# Pin & Paper

A handmade pinboard: bright yellow paper ground, everything written in ink blue by hand,
notes pinned, slips taped, kraft blocks stacked — all sitting slightly askew.

## Atmosphere

Loud, warm, and unmistakably hand-set. The whole page is one sheet of bright yellow paper;
text is ink blue, never black. Every element may carry a small rotation (±1–2°) so nothing
looks machine-aligned. Shadows are soft and paper-like under pinned notes, or hard ink
offsets under kraft blocks. The dark fallback is the same board photographed at night:
warm blacks, yellowed paper dimmed to ochre, the ink turning to light periwinkle.

## Accent roles

Accents read as different pens and papers on the board:

- accent-a — the ink-blue pen itself: the style's lead accent, factual and ever-present.
- accent-b — terracotta marker: the ideating, sketchy register.
- accent-c — kraft umber: the heaviest paper stock, for what's finished and bound.
- accent-d — red pencil: the hand's own corrections and marks.
- positive — reserved stamp green for confirmed/valid marks only.

## Signature moves

- One bright yellow paper ground; no neutral gray anywhere.
- Three card grammars, mixed freely: a pinned cream note (brass pin dot at top, soft
  drop shadow), a dashed-border yellow slip, and a kraft block with solid ink border and
  a hard offset shadow.
- Headings get a hand-drawn underline: a short thick rule rotated about -1deg.
- Slight per-card rotation; connectors and rules are drawn in the ink blue.
- Type is a handwriting stack throughout — headings are just bigger handwriting.

## Do / Don't

Do keep all text in ink blue on light; do vary card grammars within one view; do rotate
gently and sparingly. Don't use pure black or gray text, don't flatten everything into one
card shape, don't exceed ~2° of rotation, don't add photographic texture.

## Canvas renderings

### tabbed-gallery

The switcher is a row of paper strips pinned along the top edge, each strip slightly
rotated a different way; the active strip sits straight (0°), gets the brass pin dot, and
its label is underlined by the hand-drawn rule. Gallery cards mix the three card grammars
in a loose masonry flow — pinned notes for source-flavored cards, dashed slips for idea
cards, kraft blocks for finished pieces — with edges and counts inked in blue.

### single-canvas

Layers map to the three card grammars: sources render as pinned cream notes (brass pin,
soft paper shadow), ideas as dashed-border yellow slips, and output docs as kraft blocks
with solid ink borders and hard offset shadows — the visibly heaviest stock on the board.
Cluster labels are handwritten headings with the rotated underline; edges between cards
are ink-blue strokes. The selected card gains a full ink outline instead of extra shadow.
