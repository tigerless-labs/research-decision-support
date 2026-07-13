---
slug: 8-bit-orbit
name: 8-Bit Orbit
version: 1
scheme: dark
colors-light:
  surface: "#121a42"
  page: "#0d1334"
  ink: "#e8ecff"
  ink-2: "#b9c2e8"
  muted: "#8f9cc9"
  grid: "#2e3a6e"
  wash: "#131c4a"
  ring: "rgba(0,255,204,0.45)"
  accent-a: "#00ffcc"
  accent-b: "#ffe600"
  accent-c: "#ff00aa"
  accent-d: "#4fa8ff"
  positive: "#7cff00"
colors-dark:
  surface: "#0e1434"
  page: "#0a0f2c"
  ink: "#e8ecff"
  ink-2: "#b9c2e8"
  muted: "#8f9cc9"
  grid: "#2a3563"
  wash: "#101a40"
  ring: "rgba(0,255,204,0.45)"
  accent-a: "#00ffcc"
  accent-b: "#ffe600"
  accent-c: "#ff00aa"
  accent-d: "#4fa8ff"
  positive: "#7cff00"
color-aliases:
  accent: accent-a
  positive: positive
  link: accent-a
typography:
  body-family: ui-monospace, SFMono-Regular, Menlo, monospace
  heading-family: ui-monospace, SFMono-Regular, Menlo, monospace
  mono-family: ui-monospace, SFMono-Regular, Menlo, monospace
  base-size: "13px"
  line-height: "1.5"
  heading-weight: "800"
components:
  card-radius: "0px"
  pill-radius: "0px"
  card-border: 3px solid grid
  focus-ring: 0 0 0 3px ring
  max-width: "1240px"
  section-gap: "20px"
---

# 8-Bit Orbit

Pixel-arcade nostalgia from the frontend-slides bold pack: deep navy void, neon cartridge
colors, chunky borders with hard offset shadows, monospace uppercase everywhere.

## Atmosphere

Dark-native and playful. A deep navy void for the page, panel tiles one shade lighter with
thick square borders and hard-offset block shadows — the CSS equivalent of sprite art.
Type is monospace, headings uppercase with wide tracking and a faint neon glow allowed on
titles only. The style is dark in both schemes — a CRT has no daylight mode; the light
palette only lifts the navy a shade.

## Accent roles

Accents are cartridge neons, one per register:

- accent-a — neon cyan: the style's lead accent and factual register.
- accent-b — neon yellow: the in-play register.
- accent-c — neon magenta: the completed, boss-level register.
- accent-d — arcade blue: the player's own moves.
- positive — lime green, reserved for cleared/valid marks only.

## Signature moves

- Chunky three-pixel borders in the element's accent with hard offset shadows; no blur.
- Uppercase monospace titles with letter-spacing; glow budget spent on headings only.
- Level-numbering motif: stages, worlds, and counters rendered as arcade labels.
- A blinking block cursor as the single permitted animation.
- Footer marquee line in muted ink for flavor text.

## Do / Don't

Do keep borders thick and shadows hard; do give every panel exactly one neon; do respect
reduced-motion by parking the cursor. Don't blur shadows, don't mix two neons in one
element, don't let glow reach body text.

## Canvas renderings

### tabbed-gallery

The switcher is a centered row of world-select buttons — one per gallery page, labelled
like arcade worlds with the page name — where the active world lights its neon border and
text. Cards are cartridge tiles in a grid: stage label in the page accent, uppercase
title, dimmed description, and a bottom status line; the view opens with a marquee title
and closes with an insert-coin footer.

### single-canvas

Layers are three arcade set pieces on a scanlined void, all unrotated, every card the
same panel-navy tile with its meta line parked at the card's foot in muted ink. Sources
are cartridge bricks: thick cyan border, hard dark shadow, cyan title. Ideas are dialog
boxes: a thinner yellow border doubled by an outer yellow ring, ink title, and the
blinking block cursor appended to the foot meta as the single permitted animation.
Output docs are boss stages: thick magenta border, hard shadow, an outer neon glow, and
a star prefixed to the meta.
Edges route at right angles like circuit traces, solid neon; world titles keep the
letterspaced glow and group labels their block-pixel prefix, all over the scanlines.
