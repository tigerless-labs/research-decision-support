---
slug: blue-professional
name: Blue Professional
version: 1
scheme: light
colors-light:
  surface: "#fffef4"
  page: "#fdfae7"
  ink: "#111111"
  ink-2: "#3d3d3d"
  muted: "#6b6b6b"
  grid: "#e5dfc4"
  wash: "#f6f2dc"
  ring: "rgba(30,43,250,0.30)"
  accent-a: "#1e2bfa"
  accent-b: "#6b6b6b"
  accent-c: "#0f17a8"
  accent-d: "#9a9a9a"
  positive: "#059669"
colors-dark:
  surface: "#181a30"
  page: "#101120"
  ink: "#f2efe2"
  ink-2: "#c9c6b6"
  muted: "#8e8b7d"
  grid: "#2b2e4a"
  wash: "#1e2038"
  ring: "rgba(93,104,255,0.35)"
  accent-a: "#5d68ff"
  accent-b: "#8e8b7d"
  accent-c: "#8b93ff"
  accent-d: "#6f6c60"
  positive: "#10b981"
color-aliases:
  accent: accent-a
  positive: positive
  link: accent-a
typography:
  body-family: Inter, system-ui, -apple-system, Segoe UI, sans-serif
  heading-family: Space Grotesk, system-ui, sans-serif
  mono-family: ui-monospace, SFMono-Regular, Menlo, monospace
  base-size: "14px"
  line-height: "1.55"
  heading-weight: "700"
components:
  card-radius: "12px"
  pill-radius: "999px"
  card-border: 1.5px solid ring
  focus-ring: 0 0 0 2px ring
  max-width: "1180px"
  section-gap: "28px"
---

# Blue Professional

Consulting-grade restraint from the frontend-slides bold pack: a warm cream canvas and a
single saturated cobalt carrying every emphasis moment — investment-research reports,
quarterly briefings, financial dashboards.

## Atmosphere

Light-native. Warm cream ground on every surface — never pure white, never gray — with a
tight ladder of muted grays for text and exactly one saturated cobalt for everything that
matters. Cards are 4% cobalt tints with translucent cobalt hairlines and soft 10–14px
corners; chrome is pill-shaped. Built for executive readability at distance. The dark
fallback is a deep ink-navy boardroom where the cobalt brightens to keep its authority.

## Accent roles

One hue, one hierarchy — the ladder is tonal, not chromatic:

- accent-a — saturated cobalt: the style's single voice; every emphasis, metric, link.
- accent-b — mid gray: the quiet secondary register.
- accent-c — deep cobalt-navy: the settled, weightiest register.
- accent-d — light gray: the faintest, manual register.
- positive — restrained emerald for positive/valid marks only.

## Signature moves

- Cream ground everywhere; surfaces separate by tint and hairline, never by pure white.
- Cobalt-at-4% card fills with 1.5px cobalt-at-20% borders and 10–14px rounded corners.
- Pill-shaped chrome: tags, buttons, and filters at full 100px radius.
- Grotesk-voiced display and numerals; metrics render large in cobalt.
- Single-accent discipline: if two things are cobalt, one of them must yield.

## Do / Don't

Do keep every accent moment cobalt; do let grays do the subordination; do use generous
numerals for anything quantitative. Don't introduce a second hue, don't use pure white or
pure black surfaces, don't box content in solid-color borders.

## Canvas renderings

### tabbed-gallery

The switcher is a row of pill-shaped tabs on the cream ground — inactive pills are
hairline-bordered cream, the active pill fills solid cobalt with cream text. Cards sit in
an even grid as 4% cobalt tints with translucent borders; each card leads with a small
uppercase cobalt eyebrow, and metric-bearing cards render their number at display scale in
cobalt.
