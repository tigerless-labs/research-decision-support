---
slug: terminal-ledger
name: Terminal Ledger
version: 1
scheme: dark
colors-light:
  surface: "#fbfcfb"
  page: "#f4f6f4"
  ink: "#101510"
  ink-2: "#465046"
  muted: "#6b756b"
  grid: "#dde3dd"
  ring: "rgba(16,21,16,0.12)"
  c-sources: "#1d6fb8"
  c-synthesis: "#178a5e"
  c-ideas: "#a86e00"
  c-decisions: "#5b46c2"
  c-ok: "#1d7a3e"
colors-dark:
  surface: "#111411"
  page: "#0a0c0a"
  ink: "#e6ede6"
  ink-2: "#a8b3a8"
  muted: "#6b756b"
  grid: "#232823"
  ring: "rgba(230,237,230,0.12)"
  c-sources: "#4ea8de"
  c-synthesis: "#3fb47f"
  c-ideas: "#d99a2b"
  c-decisions: "#a68bfa"
  c-ok: "#37a862"
color-aliases:
  accent: c-synthesis
  positive: c-ok
  link: c-sources
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

## Layer semantics

Layer hues read like syntax highlighting — informational, never decorative:

- sources — clear signal blue: inputs on the wire.
- synthesis — terminal green: the organizing pass, also the style's accent.
- ideas — amber warning-light: claims under evaluation.
- decisions — violet phosphor: committed state.
- ok — green reserved for pass/valid markers only.

## Signature moves

- Monospace body text; proportional type only in headings and navigation.
- Square corners and thin rules; density comes from tight spacing, not smaller ink.
- Tabular layouts everywhere data allows: aligned columns, right-aligned counts.
- Status rendered as bracketed uppercase tags in layer hues on the panel surface.
- Wide reading measure to hold tables; prose lines still capped for readability.

## Do / Don't

Do keep every accent at identity strength on dark neutral ground; do align numerics in
columns; do prefer one dense table over three sparse cards. Don't add glow, scanline, or
CRT effects; don't use layer hues as backgrounds; don't let monospace leak into long prose
paragraphs beyond summaries.

## Invariants

Every projection in this style is a single self-contained HTML file making zero external
requests (system font stacks only). Card titles, bodies, and frontmatter values are
untrusted: escape on interpolation, sanitize rendered markdown, guard script-tag breakout in
embedded JSON. Both light and dark are fully styled via prefers-color-scheme plus a
data-theme override toggle.
