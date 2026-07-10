---
slug: block-frame
name: BlockFrame
version: 1
scheme: light
colors-light:
  surface: "#ffffff"
  page: "#fffdf5"
  ink: "#000000"
  ink-2: "#333333"
  muted: "#666666"
  grid: "#000000"
  wash: "#fff3c4"
  ring: "rgba(0,0,0,0.55)"
  accent-a: "#37b6d4"
  accent-b: "#f45fd0"
  accent-c: "#e8a614"
  accent-d: "#000000"
  positive: "#3f9e2d"
colors-dark:
  surface: "#221f28"
  page: "#17151a"
  ink: "#fffdf5"
  ink-2: "#d8d4c8"
  muted: "#9a958a"
  grid: "#fffdf5"
  wash: "#2c2833"
  ring: "rgba(255,253,245,0.55)"
  accent-a: "#6fd9ef"
  accent-b: "#ff8ae0"
  accent-c: "#ffcb52"
  accent-d: "#fffdf5"
  positive: "#7fd45f"
color-aliases:
  accent: accent-b
  positive: positive
  link: accent-a
typography:
  body-family: system-ui, -apple-system, Segoe UI, sans-serif
  heading-family: Inter, system-ui, sans-serif
  mono-family: Space Grotesk, ui-monospace, Menlo, monospace
  base-size: "14px"
  line-height: "1.5"
  heading-weight: "900"
components:
  card-radius: "0px"
  pill-radius: "0px"
  card-border: 3px solid grid
  card-shadow: 6px 6px 0 grid
  focus-ring: 0 0 0 3px ring
  max-width: "1220px"
  section-gap: "24px"
---

# BlockFrame

Neobrutalist pop from the frontend-slides bold pack: candy pastels inside chunky black
borders with hard offset shadows — zine layout, sticker books, toy packaging. Joyful,
slightly crooked, never timid.

## Atmosphere

Light-native. Off-white ground, saturated pastel fills (sky, pink, yellow, green, cream)
cycling across surfaces, and five structural laws: thick black borders on every region,
hard offset shadows with zero blur, square corners everywhere, saturated pastel accents,
and layouts allowed a deliberate tilt. The dark fallback keeps the laws and inverts the
ink: near-black ground, off-white borders and shadows, neons brightened.

## Accent roles

Cartridge pastels, inked darker where they must read as marks:

- accent-a — pool blue: the factual register.
- accent-b — hot pink: the style's lead accent — energy and work-in-progress.
- accent-c — mustard yellow: the settled, headline register.
- accent-d — solid ink: the manual mark, pure black (light) / off-white (dark).
- positive — leafy green for confirmed/valid marks only.

## Signature moves

- 3px solid ink borders on every card; 6px hard offset shadows, zero blur, square corners.
- Pastel fills cycle with deliberate juxtaposition; ink text on every fill.
- Ultra-heavy (900) uppercase display with tight tracking; label voice tracked wide.
- One tilted element per view — a badge, a sticker dot, a rotated card — never more.
- A single circular accent dot is the only rounded shape allowed.

## Do / Don't

Do collide bordered cards against bordered cards; do keep every shadow hard and every
corner square; do put ink text on pastel fills. Don't blur or soften anything, don't tint
text with pastels, don't tilt more than one element per view.

## Canvas renderings

### tabbed-gallery

The switcher is a row of bordered blocks — each tab a 3px-bordered rectangle filled with
its page's pastel, the active tab popped by a hard offset shadow and a slight tilt. Cards
sit in a dense grid, each a bordered pastel block with an ink uppercase title; one card
per view may carry the circular accent-dot badge, and the whole grid keeps square corners
and hard shadows throughout.
