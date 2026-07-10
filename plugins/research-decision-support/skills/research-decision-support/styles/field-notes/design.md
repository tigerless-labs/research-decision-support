---
slug: field-notes
name: Field Notes
version: 2
scheme: light
colors-light:
  surface: "#fffdf5"
  page: "#faf6ec"
  ink: "#1f2430"
  ink-2: "#565d6b"
  muted: "#98937f"
  grid: "#e8e1cd"
  wash: "#f3ecdc"
  accent-d: "#c24d0c"
  ring: "rgba(31,36,48,0.12)"
  accent-a: "#3b82d9"
  accent-b: "#f0a01f"
  accent-c: "#7048c8"
  positive: "#2e9e44"
colors-dark:
  surface: "#201f1a"
  page: "#161512"
  ink: "#f2eee2"
  ink-2: "#c4bfae"
  muted: "#8d8875"
  grid: "#35332a"
  wash: "#2a2820"
  accent-d: "#e78a52"
  ring: "rgba(242,238,226,0.12)"
  accent-a: "#5c9ee8"
  accent-b: "#f2b13f"
  accent-c: "#9d7ff0"
  positive: "#46b45e"
color-aliases:
  accent: accent-b
  positive: positive
  link: accent-a
typography:
  body-family: system-ui, -apple-system, Segoe UI, sans-serif
  heading-family: system-ui, -apple-system, Segoe UI, sans-serif
  mono-family: ui-monospace, SFMono-Regular, Menlo, monospace
  base-size: "15px"
  line-height: "1.65"
  heading-weight: "800"
components:
  card-radius: "14px"
  pill-radius: "999px"
  card-border: 1px solid grid
  focus-ring: 0 0 0 3px ring
  max-width: "1080px"
  section-gap: "36px"
---

# Field Notes

A warm notebook for exploratory sessions: cream paper, navy-leaning ink, bright accent
inks used like colored pens, and enough air that half-formed thoughts don't feel crowded.

## Atmosphere

Light-native. Warm cream page with slightly brighter card stock; ink is a soft navy-black
rather than pure black. Corners round generously, spacing is loose, headings are heavy and
friendly. The dark fallback keeps the notebook warmth — aged-paper darks, never cold gray.

## Accent roles

Accents behave like a four-pen set, saturated and cheerful but semantically strict:

- accent-a — bright pen blue: matter-of-fact notes.
- accent-b — marker amber: the style's lead accent — thinking out loud.
- accent-c — vivid violet: the piece taking shape.
- accent-d — warm terracotta: the hand holding the pen.
- positive — reserved green for confirmed/valid marks only.

## Signature moves

- Big rounded cards on cream, one idea per card, generous 36px section gaps.
- Heavy (800) headings at modest sizes — friendly weight, not shouting scale.
- Accent hue appears as a fat left border plus a matching pill; body stays ink.
- Status pills are rounded and lowercase, like margin scribbles formalized.
- Empty states and unassigned buckets are first-class, cheerfully labeled.

## Do / Don't

Do leave whitespace even when content is short; do let accent-b set the visual
temperature; do use the muted token for meta-text so notes read as notes. Don't compress
into tables when cards will do; don't use pure white or pure black anywhere; don't render
this style for formal sign-off documents.
