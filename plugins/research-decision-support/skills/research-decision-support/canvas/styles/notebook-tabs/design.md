---
slug: notebook-tabs
name: Notebook Tabs
version: 1
scheme: light
colors-light:
  surface: "#fdfbf5"
  page: "#efe9dd"
  ink: "#22201c"
  ink-2: "#55504a"
  muted: "#97907f"
  grid: "#e0d8c4"
  wash: "#f6f2e7"
  ring: "rgba(34,32,28,0.14)"
  accent-a: "#4f9dc9"
  accent-b: "#d9982b"
  accent-c: "#8a76c0"
  accent-d: "#c25a4a"
  positive: "#3e7d4e"
colors-dark:
  surface: "#27241f"
  page: "#1a1815"
  ink: "#f0ebdf"
  ink-2: "#c8c1b1"
  muted: "#8f887a"
  grid: "#3b372e"
  wash: "#2e2a24"
  ring: "rgba(240,235,223,0.14)"
  accent-a: "#7ab8d4"
  accent-b: "#e0b054"
  accent-c: "#ab94d9"
  accent-d: "#d97f6d"
  positive: "#6da97c"
color-aliases:
  accent: accent-b
  positive: positive
  link: accent-a
typography:
  body-family: system-ui, -apple-system, Segoe UI, sans-serif
  heading-family: Bodoni MT, Didot, Georgia, serif
  mono-family: ui-monospace, SFMono-Regular, Menlo, monospace
  base-size: "14px"
  line-height: "1.55"
  heading-weight: "700"
components:
  card-radius: "10px"
  pill-radius: "999px"
  card-border: 1px solid grid
  focus-ring: 0 0 0 2px ring
  max-width: "1160px"
  section-gap: "28px"
---

# Notebook Tabs

An editorial paper notebook lifted from the frontend-slides preset of the same name: a cream
sheet resting on a dark desk, classic serif display over quiet sans, and pastel index tabs
doing the wayfinding.

## Atmosphere

Light-native and tactile. The page reads as physical stock — warm cream surface on a deeper
parchment ground, soft single shadow allowed only under the sheet itself. Serif headings at
generous sizes give it a magazine masthead voice. The dark fallback is the same notebook
photographed at night: aged warm darks, never cold gray.

## Accent roles

Accents are the pastel tab set, inked at readable strength:

- accent-a — sky ink: cool and factual.
- accent-b — honey amber: the style's lead accent, the tab you reach for first.
- accent-c — lavender ink: the composed, finished register.
- accent-d — red pencil: the hand's own markings.
- positive — reserved leaf green for confirmed/valid marks only.

## Signature moves

- One elevated paper sheet holds everything; the ground behind it stays dark and empty.
- Serif display headings over sans body; a thin ruled line under every section title.
- Cards separate with dotted rules like notebook entries, not boxed borders.
- Binder-hole ornaments on the sheet's left edge; decoration budget ends there.
- Index-tab motif for navigation: rounded tabs protruding from the sheet edge.

## Do / Don't

Do keep the sheet as the single elevated plane; do let accent hues appear as tab fills and
entry markers at pastel strength. Don't box every card, don't stack shadows, don't let the
desk ground compete with the sheet.

## Canvas renderings

### tabbed-gallery

The switcher is the style's namesake: vertical index tabs attached to the sheet's right
edge, one per gallery page, vertical text, the active tab at full accent strength and
protruding further than its siblings. Cards render as dotted-rule notebook entries in a
two-to-three column flow; each entry carries a small accent dot as its page mark.

### single-canvas

Layers take three stationery forms. Sources are index cards: cream stock with a colored
tab tongue protruding from the top edge in the source accent. Ideas are sticky notes:
accent-tinted paper with no border, held by a translucent tape strip at the top center.
Output docs are stamped files: double-line frames (border plus offset outline) with the
meta line inked in the output accent like a stamp. Cards keep the gentle per-card
rotation; serif titles throughout. World titles and group labels are italic serif
mastheads over thin ink rules on the parchment ground; edges are soft warm-ink curves.
