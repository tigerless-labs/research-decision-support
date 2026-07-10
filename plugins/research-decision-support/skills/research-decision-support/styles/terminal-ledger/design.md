---
slug: terminal-ledger
name: Terminal Ledger
version: 2
scheme: dark
colors-light:
  surface: "#fbfcfb"
  page: "#f4f6f4"
  ink: "#101510"
  ink-2: "#465046"
  muted: "#6b756b"
  grid: "#dde3dd"
  wash: "#eef2ee"
  accent-d: "#b5541d"
  ring: "rgba(16,21,16,0.12)"
  accent-a: "#1d6fb8"
  accent-b: "#a86e00"
  accent-c: "#5b46c2"
  positive: "#1d7a3e"
colors-dark:
  surface: "#111411"
  page: "#0a0c0a"
  ink: "#e6ede6"
  ink-2: "#a8b3a8"
  muted: "#6b756b"
  grid: "#232823"
  wash: "#161a16"
  accent-d: "#e08a4d"
  ring: "rgba(230,237,230,0.12)"
  accent-a: "#4ea8de"
  accent-b: "#d99a2b"
  accent-c: "#a68bfa"
  positive: "#37a862"
color-aliases:
  accent: positive
  positive: positive
  link: accent-a
typography:
  body-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace
  heading-family: system-ui, -apple-system, Segoe UI, sans-serif
  mono-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace
  base-size: "13px"
  line-height: "1.45"
  heading-weight: "600"
components:
  card-radius: "4px"
  pill-radius: "3px"
  card-border: 1px solid grid
  focus-ring: 0 0 0 2px ring
  max-width: "1320px"
  section-gap: "16px"
---

# Terminal Ledger

A disciplined terminal aesthetic for evidence-dense engineering sessions: charcoal with a
faint green undertone, phosphor-adjacent accents kept on a short leash, monospace as the
working voice.

## Atmosphere

Dark-native. The page is near-black with a barely-there green cast; panels are one shade
lighter, separated by thin grid lines like a ledger ruled in ink. Everything aligns to a
tight rhythm — this style trades warmth for scan speed. In its light fallback the same
discipline holds on paper-green tinted white.

## Accent roles

Accent hues read like syntax highlighting — informational, never decorative:

- accent-a — clear signal blue: inputs on the wire.
- accent-b — amber warning-light: things under evaluation.
- accent-c — violet phosphor: committed state.
- accent-d — rust amber: operator input, distinct from machine output.
- positive — green reserved for pass/valid markers only.

## Signature moves

- Monospace body text; proportional type only in headings and navigation.
- Square corners and thin rules; density comes from tight spacing, not smaller ink.
- Tabular layouts everywhere data allows: aligned columns, right-aligned counts.
- Status rendered as bracketed uppercase tags in accent hues on the panel surface.
- Wide reading measure to hold tables; prose lines still capped for readability.

## Do / Don't

Do keep every accent at identity strength on dark neutral ground; do align numerics in
columns; do prefer one dense table over three sparse cards. Don't add glow, scanline, or
CRT effects; don't use accent hues as backgrounds; don't let monospace leak into long prose
paragraphs beyond summaries.
