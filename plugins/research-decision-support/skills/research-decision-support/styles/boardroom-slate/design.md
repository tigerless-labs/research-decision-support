---
slug: boardroom-slate
name: Boardroom Slate
version: 1
scheme: light
colors-light:
  surface: "#ffffff"
  page: "#f5f6f8"
  ink: "#16202b"
  ink-2: "#47535f"
  muted: "#7d8894"
  grid: "#dbe0e6"
  ring: "rgba(22,32,43,0.12)"
  c-sources: "#2563a8"
  c-synthesis: "#1e7f66"
  c-ideas: "#b07a10"
  c-decisions: "#3b3f8f"
  c-ok: "#1e7a34"
colors-dark:
  surface: "#1a212a"
  page: "#10151b"
  ink: "#f0f3f6"
  ink-2: "#b7c0c9"
  muted: "#7d8894"
  grid: "#2c353f"
  ring: "rgba(240,243,246,0.12)"
  c-sources: "#5a95d6"
  c-synthesis: "#35a184"
  c-ideas: "#cf9a34"
  c-decisions: "#8489e0"
  c-ok: "#3d9e55"
color-aliases:
  accent: c-decisions
  positive: c-ok
  link: c-sources
typography:
  body-family: system-ui, -apple-system, Segoe UI, sans-serif
  heading-family: Georgia, Times New Roman, serif
  mono-family: ui-monospace, SFMono-Regular, Menlo, monospace
  base-size: "14px"
  line-height: "1.55"
  heading-weight: "700"
components:
  card-radius: "6px"
  pill-radius: "4px"
  card-border: 1px solid grid
  focus-ring: 0 0 0 2px ring
  max-width: "1120px"
  section-gap: "28px"
---

# Boardroom Slate

A composed readout style for decisions that leave the room: slate blue-grays on paper white,
serif headlines, restrained accents. Built to survive projection, PDF export, and a
skeptical audience.

## Atmosphere

Light-native. Cool gray page, pure white cards, near-slate ink. Serif headings give
documents authority; everything else is quiet sans. Contrast is high, decoration is near
zero — the style asserts credibility by restraint. The dark fallback is a dimmed boardroom,
same composure on deep slate.

## Layer semantics

Layer hues are desaturated toward institutional weight — legible, never loud:

- sources — steady report blue: the evidence base.
- synthesis — muted teal-green: how the evidence is organized.
- ideas — bronze: judgments awaiting ratification.
- decisions — indigo: the style's accent — ratified positions carry the deepest hue.
- ok — reserved green for approved/valid marks only.

## Signature moves

- Serif display headings over sans body; the pairing is the style's identity.
- White cards edged by hairlines on the cool gray page; shadows never used.
- Decision entries lead with an indigo rule and a small-caps status label.
- Numbered sections and stable anchors, built to be cited in follow-up documents.
- Print-adjacent discipline: nothing depends on hover; state is visible statically.

## Do / Don't

Do keep hierarchy typographic (size, weight, small-caps) rather than chromatic; do give
decisions the most visual weight of any layer; do keep accent use to rules, labels, and
links. Don't introduce rounded-pill playfulness; don't use layer hues in body text; don't
let any element depend on interaction to convey status.

## Invariants

Every projection in this style is a single self-contained HTML file making zero external
requests (system font stacks only). Card titles, bodies, and frontmatter values are
untrusted: escape on interpolation, sanitize rendered markdown, guard script-tag breakout in
embedded JSON. Both light and dark are fully styled via prefers-color-scheme plus a
data-theme override toggle.
