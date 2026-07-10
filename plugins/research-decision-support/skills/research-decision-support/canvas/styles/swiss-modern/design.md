---
slug: swiss-modern
name: Swiss Modern
version: 1
scheme: light
colors-light:
  surface: "#ffffff"
  page: "#ffffff"
  ink: "#0a0a0a"
  ink-2: "#3d3d3d"
  muted: "#757575"
  grid: "#111111"
  wash: "#f2f2f2"
  ring: "rgba(255,51,0,0.35)"
  accent-a: "#1a1a1a"
  accent-b: "#6e6e6e"
  accent-c: "#ff3300"
  accent-d: "#b0b0b0"
  positive: "#0a7d34"
colors-dark:
  surface: "#0f0f0f"
  page: "#0f0f0f"
  ink: "#fafafa"
  ink-2: "#cccccc"
  muted: "#909090"
  grid: "#f0f0f0"
  wash: "#1c1c1c"
  ring: "rgba(255,68,17,0.4)"
  accent-a: "#ececec"
  accent-b: "#a0a0a0"
  accent-c: "#ff4411"
  accent-d: "#6e6e6e"
  positive: "#43b45f"
color-aliases:
  accent: accent-c
  positive: positive
  link: accent-c
typography:
  body-family: Helvetica Neue, Arial, system-ui, sans-serif
  heading-family: Helvetica Neue, Arial, system-ui, sans-serif
  mono-family: ui-monospace, SFMono-Regular, Menlo, monospace
  base-size: "14px"
  line-height: "1.5"
  heading-weight: "800"
components:
  card-radius: "0px"
  pill-radius: "0px"
  card-border: 2px solid grid
  focus-ring: 0 0 0 2px ring
  max-width: "1240px"
  section-gap: "32px"
---

# Swiss Modern

International-typographic-style discipline from the frontend-slides preset: pure white,
near-black, one fire red, a visible grid, and type doing all the work.

## Atmosphere

Light-native and severe. The page is pure white with a faint construction grid allowed to
show; every border is black and square; hierarchy comes from scale and weight jumps, not
color. Uppercase display headings at heavy weights, tight negative letter-spacing. The dark
fallback inverts to true black with white rules — same austerity, no mood shift.

## Accent roles

A tonal ladder plus one shout — the style deliberately starves color:

- accent-a — full ink black: the primary factual register.
- accent-b — mid gray: the secondary register.
- accent-c — fire red: the single loud voice, always the most important thing in view.
- accent-d — light gray: the quietest, manual register.
- positive — a disciplined green, small marks only.

## Signature moves

- Visible layout grid; every element lands on it, nothing floats.
- Two-pixel black borders, square corners, no shadows, no radii anywhere.
- Oversized numerals as structural anchors; tabular figures throughout.
- Asymmetric composition: one dominant cell, subordinate cells around it.
- Red appears once per view as a rule, a numeral, or an active state — never twice.

## Do / Don't

Do jump type sizes in large deliberate steps; do use uppercase with widened tracking for
labels. Don't round anything, don't tint backgrounds with accents, don't let red appear in
more than one element per view.

## Canvas renderings

### tabbed-gallery

The switcher is a left rail of oversized two-digit numerals with small uppercase labels;
the active numeral turns accent-c red, inactive ones stay in accent-d gray. The gallery is
an asymmetric grid: the first card spans a double cell at display scale, the rest fill
single cells; every card is a two-pixel-bordered box with an uppercase title and a red
index mark.
