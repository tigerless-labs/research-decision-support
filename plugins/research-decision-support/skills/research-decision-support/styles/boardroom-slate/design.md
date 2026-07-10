---
slug: boardroom-slate
name: Boardroom Slate
version: 2
scheme: light
colors-light:
  surface: "#ffffff"
  page: "#f5f6f8"
  ink: "#16202b"
  ink-2: "#47535f"
  muted: "#7d8894"
  grid: "#dbe0e6"
  wash: "#eceff2"
  accent-d: "#a03d20"
  ring: "rgba(22,32,43,0.12)"
  accent-a: "#2563a8"
  accent-b: "#b07a10"
  accent-c: "#3b3f8f"
  positive: "#1e7a34"
colors-dark:
  surface: "#1a212a"
  page: "#10151b"
  ink: "#f0f3f6"
  ink-2: "#b7c0c9"
  muted: "#7d8894"
  grid: "#2c353f"
  wash: "#222b35"
  accent-d: "#d97a5a"
  ring: "rgba(240,243,246,0.12)"
  accent-a: "#5a95d6"
  accent-b: "#cf9a34"
  accent-c: "#8489e0"
  positive: "#3d9e55"
color-aliases:
  accent: accent-c
  positive: positive
  link: accent-a
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

## Accent roles

Accent hues are desaturated toward institutional weight — legible, never loud:

- accent-a — steady report blue: the factual register.
- accent-b — bronze: matters awaiting ratification.
- accent-c — indigo: the style's accent — always the deepest hue on the page.
- accent-d — oxblood: the manual mark, used sparingly.
- positive — reserved green for approved/valid marks only.

## Signature moves

- Serif display headings over sans body; the pairing is the style's identity.
- White cards edged by hairlines on the cool gray page; shadows never used.
- Lead entries open with an indigo accent-c rule and a small-caps status label.
- Numbered sections and stable anchors, built to be cited in follow-up documents.
- Print-adjacent discipline: nothing depends on hover; state is visible statically.

## Do / Don't

Do keep hierarchy typographic (size, weight, small-caps) rather than chromatic; do give
accent-c the most visual weight on the page; do keep accent use to rules, labels, and
links. Don't introduce rounded-pill playfulness; don't use accent hues in body text; don't
let any element depend on interaction to convey status.
