---
slug: terminal-green
name: Terminal Green
version: 1
scheme: dark
colors-light:
  surface: "#ffffff"
  page: "#f6f8fa"
  ink: "#1f2328"
  ink-2: "#59636e"
  muted: "#6e7781"
  grid: "#d1d9e0"
  wash: "#eff2f5"
  ring: "rgba(26,127,55,0.35)"
  accent-a: "#0969da"
  accent-b: "#9a6700"
  accent-c: "#8250df"
  accent-d: "#bf3989"
  positive: "#1a7f37"
colors-dark:
  surface: "#161b22"
  page: "#0d1117"
  ink: "#e6edf3"
  ink-2: "#a5b1bd"
  muted: "#8b949e"
  grid: "#30363d"
  wash: "#1c2129"
  ring: "rgba(63,185,80,0.4)"
  accent-a: "#58a6ff"
  accent-b: "#d29922"
  accent-c: "#bc8cff"
  accent-d: "#f778ba"
  positive: "#3fb950"
color-aliases:
  accent: positive
  positive: positive
  link: accent-a
typography:
  body-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace
  heading-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace
  mono-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace
  base-size: "13px"
  line-height: "1.5"
  heading-weight: "700"
components:
  card-radius: "6px"
  pill-radius: "999px"
  card-border: 1px solid grid
  focus-ring: 0 0 0 2px ring
  max-width: "1280px"
  section-gap: "20px"
---

# Terminal Green

A developer terminal session in the GitHub-dark idiom, from the frontend-slides preset:
blue-black panels, ANSI accents, monospace as the only voice, and a live prompt as the
page's pulse.

## Atmosphere

Dark-native. Blue-cast near-black page, panels one step lighter with soft-rounded corners,
thin cool borders. Everything — headings included — is monospace; hierarchy comes from
weight, hue, and prompt punctuation rather than typeface changes. The light fallback is the
matching light-terminal theme: airy blue-grays, same ANSI logic.

## Accent roles

Accents are the ANSI palette, applied like shell output coloring:

- accent-a — ANSI blue: paths, links, references.
- accent-b — ANSI yellow: pending, in-flight, under evaluation.
- accent-c — ANSI magenta-violet: finished artifacts.
- accent-d — ANSI pink: the operator's own input.
- positive — terminal green, the style's signature: success and valid states only.

## Signature moves

- A prompt line with a blinking block cursor heads every view; the prompt names the view.
- Window chrome dots and a title bar frame the whole projection as one terminal window.
- Content compresses into aligned listing rows — name, meta, description columns.
- Bracketed argument chips for navigation and filters.
- A status footer line reports counts and state in lowercase.

## Do / Don't

Do keep all type monospace; do color only tokens and markers, leaving prose in ink; do
align columns character-tight. Don't add scanlines or glow, don't exceed one green element
per row, don't use accent hues as backgrounds outside the active chip.

## Canvas renderings

### tabbed-gallery

The switcher is a row of bracketed command chips — one per gallery page, numbered like
positional arguments; the active chip fills with its accent and inverts its text. Cards
compress into a listing table: one row per card with name in the page accent, meta dimmed,
description in ink; the prompt line above echoes the active page and a status footer
closes the view.
