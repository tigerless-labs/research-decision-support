---
slug: bold-signal
name: Bold Signal
version: 1
scheme: dark
colors-light:
  surface: "#ffffff"
  page: "#f4f4f2"
  ink: "#141414"
  ink-2: "#454545"
  muted: "#8a8a8a"
  grid: "#dddddb"
  wash: "#ebebe8"
  ring: "rgba(230,74,25,0.35)"
  accent-a: "#00838f"
  accent-b: "#b07800"
  accent-c: "#e64a19"
  accent-d: "#c2185b"
  positive: "#2e7d32"
colors-dark:
  surface: "#242424"
  page: "#1a1a1a"
  ink: "#ffffff"
  ink-2: "#d0d0d0"
  muted: "#9a9a9a"
  grid: "#3a3a3a"
  wash: "#2d2d2d"
  ring: "rgba(255,87,34,0.45)"
  accent-a: "#26c6da"
  accent-b: "#ffb300"
  accent-c: "#ff5722"
  accent-d: "#ec407a"
  positive: "#66bb6a"
color-aliases:
  accent: accent-c
  positive: positive
  link: accent-a
typography:
  body-family: Space Grotesk, system-ui, sans-serif
  heading-family: Archivo Black, Arial Black, system-ui, sans-serif
  mono-family: ui-monospace, SFMono-Regular, Menlo, monospace
  base-size: "15px"
  line-height: "1.5"
  heading-weight: "900"
components:
  card-radius: "6px"
  pill-radius: "4px"
  card-border: 1px solid grid
  focus-ring: 0 0 0 2px ring
  max-width: "1200px"
  section-gap: "24px"
---

# Bold Signal

High-impact poster energy from the frontend-slides preset: charcoal gradient dark, one
saturated color block as the focal point, ultra-heavy display type, oversized numerals.

## Atmosphere

Dark-native and loud. The page is layered charcoal; one card per view gets promoted to a
full-saturation accent block with dark ink on it, and everything else stays quiet around
it. Display headings are ultra-black weight, tight and often uppercase. The light fallback
keeps the poster logic on warm off-white with the same single-block focus.

## Accent roles

Vivid, confident, one at a time:

- accent-a — electric cyan: the factual register.
- accent-b — amber: the in-progress register.
- accent-c — signal orange: the style's core — whatever matters most wears it.
- accent-d — magenta: the manual, human-energy register.
- positive — a calm green kept small against the loud accents.

## Signature moves

- One promoted block per view: full accent background, dark text, display-scale title.
- Oversized index numerals anchor the top-left of every view.
- Breadcrumb navigation in small caps with opacity states, top-right.
- Subordinate content in thin-bordered translucent panels that never compete.
- Uppercase labels with wide tracking as the only ornament.

## Do / Don't

Do keep exactly one full-saturation surface per view; do push the promoted title to
display scale; do use opacity for navigation hierarchy. Don't promote two blocks at once,
don't put accent hues on body text, don't decorate the charcoal ground.

## Canvas renderings

### tabbed-gallery

The switcher is a breadcrumb row of uppercase page names at the top right — inactive pages
at low opacity, the active one at full strength with an accent underline — paired with an
oversized two-digit numeral at the top left. The first card of the active page is promoted
onto the accent block at poster scale; remaining cards stack as slim translucent panels
beside it, each with its accent-tinted meta line.

### single-canvas

Layers climb a saturation ladder, all unrotated on the charcoal ground. Sources are thin
outline strips: faint translucent fill, hairline ink-mix border, the meta line in the
source accent. Ideas are translucent accent panels: accent-mixed fill with no border and a
heavier title. Output docs are the full-saturation poster blocks: solid accent ground,
dark ink text, display-face uppercase titles — the only full-saturation surfaces in view.
World titles are solid display-black uppercase at poster scale; group labels keep the
short accent underline bar. Edges draw as straight accent strokes, thick and solid.
