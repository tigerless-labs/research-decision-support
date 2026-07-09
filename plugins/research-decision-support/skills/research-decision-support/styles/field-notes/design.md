---
slug: field-notes
name: Field Notes
version: 1
scheme: light
colors-light:
  surface: "#fffdf5"
  page: "#faf6ec"
  ink: "#1f2430"
  ink-2: "#565d6b"
  muted: "#98937f"
  grid: "#e8e1cd"
  ring: "rgba(31,36,48,0.12)"
  c-sources: "#3b82d9"
  c-synthesis: "#2aa876"
  c-ideas: "#f0a01f"
  c-decisions: "#7048c8"
  c-ok: "#2e9e44"
colors-dark:
  surface: "#201f1a"
  page: "#161512"
  ink: "#f2eee2"
  ink-2: "#c4bfae"
  muted: "#8d8875"
  grid: "#35332a"
  ring: "rgba(242,238,226,0.12)"
  c-sources: "#5c9ee8"
  c-synthesis: "#3cbf8b"
  c-ideas: "#f2b13f"
  c-decisions: "#9d7ff0"
  c-ok: "#46b45e"
color-aliases:
  accent: c-ideas
  positive: c-ok
  link: c-sources
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

A warm notebook for exploratory sessions: cream paper, navy-leaning ink, bright layer inks
used like colored pens, and enough air that half-formed ideas don't feel crowded.

## Atmosphere

Light-native. Warm cream page with slightly brighter card stock; ink is a soft navy-black
rather than pure black. Corners round generously, spacing is loose, headings are heavy and
friendly. The dark fallback keeps the notebook warmth — aged-paper darks, never cold gray.

## Layer semantics

Layer hues behave like a four-pen set, saturated and cheerful but semantically strict:

- sources — bright pen blue: material collected in the field.
- synthesis — fresh green: groupings sketched around the material.
- ideas — marker amber: the style's accent — this is a thinking-out-loud style.
- decisions — vivid violet: the few things already settled.
- ok — reserved green for confirmed/valid marks only.

## Signature moves

- Big rounded cards on cream, one idea per card, generous 36px section gaps.
- Heavy (800) headings at modest sizes — friendly weight, not shouting scale.
- Layer hue appears as a fat left border plus a matching pill; body stays ink.
- Status pills are rounded and lowercase, like margin scribbles formalized.
- Empty states and unassigned buckets are first-class, cheerfully labeled.

## Do / Don't

Do leave whitespace even when content is short; do let the ideas layer set the visual
temperature; do use the muted token for meta-text so notes read as notes. Don't compress
into tables when cards will do; don't use pure white or pure black anywhere; don't render
this style for formal sign-off documents.

## Invariants

Every projection in this style is a single self-contained HTML file making zero external
requests (system font stacks only). Card titles, bodies, and frontmatter values are
untrusted: escape on interpolation, sanitize rendered markdown, guard script-tag breakout in
embedded JSON. Both light and dark are fully styled via prefers-color-scheme plus a
data-theme override toggle.
