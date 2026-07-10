---
slug: 8-bit-orbit
name: 8-Bit Orbit
version: 1
scheme: dark
colors-light:
  surface: "#ffffff"
  page: "#edf1fb"
  ink: "#131a3d"
  ink-2: "#414c7c"
  muted: "#7480ac"
  grid: "#c6cfe9"
  wash: "#e0e6f5"
  ring: "rgba(0,148,126,0.4)"
  accent-a: "#00947e"
  accent-b: "#a08600"
  accent-c: "#d4008f"
  accent-d: "#2f6fd0"
  positive: "#3f9f2c"
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
titles only. The light fallback is a daylight arcade: pale blue-white ground, ink-navy
text, the same neon logic at print-safe depth.

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
