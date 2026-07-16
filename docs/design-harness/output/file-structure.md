# File structure — the design→disk mapping

The skill v2 file layout: two trees — the **skill package** (portable kernel, distributed
with the plugin, read-only) and the **workspace** (writable, many per host).
Splitting the trees decouples protocol from runtime: the kernel can be moved wholesale and
reused, while every fact stays in the workspace.

## Skill package (the kernel)

```
plugins/design-harness/skills/design-harness/
├── SKILL.md              the single operating-and-contract doc, four sections in order:
│                         structure (layout, layers, card schemas with inline skeletons, the
│                         three facts, rendering contract, canvas anatomy) → workflow
│                         (discover → ingest → transcribe → sync on command → assemble →
│                         project, teach-in-place attached) → disciplines (the "never" list,
│                         ledger format, validator gate) → quickstart (command runbook)
├── references/
│   ├── output-forms/     the output form library (recommended set), one form one spec
│   │   └── system-design.md   first entry: mermaid diagrams (with click-through) + a modules layer
│   └── publish-canvas-github-pages.md   serving the committed canvas over GitHub Pages
├── scripts/
│   ├── init_workspace.py     workspace bootstrap (idempotent, never overwrites); records the
│   │                         workspace location in the host's pointer file, then runs both
│   │                         validators itself — one command, fails nonzero on any problem
│   ├── discover_workspace.py workspace discovery: pointer file → default location → find by
│   │                         directory name; ambiguity (many or zero hits) is reported, never
│   │                         resolved silently — pure read, only the bootstrap writes the pointer
│   ├── check_workspace.py    schema validation: required frontmatter, single tag, forward-only
│   │                         acyclic references, conflicts targets resolve
│   ├── check_doc_links.py    link integrity validation
│   ├── build_canvas.py       the canvas builder (fixed script): the workspace path is the only
│   │                         required input; runs both validators as a gate (problems abort
│   │                         the build, no HTML) → collects cards / derives edges /
│   │                         lays out / embeds data into a single-file HTML in one step;
│   │                         --css swaps the style; writes only to temp dirs or artifacts
│   ├── check_style_pack.py   style pack validation (schema, dual palettes, no external reach,
│   │                         tokens pinned to the default template)
│   ├── workspace.py          shared card reader (frontmatter/tag/link parsing, shared by the
│   │                         three tools and the builder)
│   └── vendor/               offline rendering dependencies (markdown/sanitize/mermaid; mermaid embedded on demand)
└── canvas/               the canvas layer: exactly one canvas (the unified canvas), structure
    ├── template.html         and style side by side in the same layer; the unified canvas
    │                         implementation: structure + interaction JS, with a CSS injection
    │                         slot and no CSS of its own; the interaction contract's truth
    │                         lives in modules/canvas
    └── styles/               the style pack: agent-readable pure UI specs (palette / type /
        └── <slug>/               geometry / mood — three-tier progressive, dual palettes,
                                  content-agnostic, bound only to the token interface); every
                                  style ships a precompiled canvas.css — the default build is
                                  pin-and-paper (the canvas's native look), --css swaps in any other
```

- **Rules and templates are separate**: template-independent invariants (truth-driven,
  edges = references, derived layout) live in build_canvas and the protocol contract;
  canvas/ holds only form.
- **Styles hang under the canvas, bounded by the token interface**: with the canvas
  converged to one, style × canvas orthogonality degenerates into an interface
  convention — a style writes only tokens and presentation, never touches canvas
  structure, and the whole pack stays swappable; tokens are abstract accent roles, and
  the layer→accent semantic binding is written once, in SKILL.md's rendering section.
  The canvas_renderings multi-canvas selector retired along with the template set;
  a style's custom presentation section now targets the unified canvas directly.
- **One contract, two readings**: SKILL.md's structure and disciplines sections are read by
  humans and agents, and check_workspace.py is their machine-executable form — same origin,
  so changing the contract means changing the validator.
- **The form library is open**: adding an output form = adding one spec to
  output-forms/, engine untouched (one engine, many schemas).

## Workspace (the truth)

```
docs/design-harness/
├── target.md             the human's acceptance criteria for output; source of the output form
├── logs.md               append-only change ledger — for a workspace outside git it is
│                         the only way back
├── index.md              workspace entry point (derived)
├── sources/              ① evidence layer: one source, one card; type dirs are thin shells, path = type
│   ├── index.md              derived: grouped under tag headings, unclassified flat at the end
│   └── <type>/*.md
├── ideas/                ② judgment layer: only the human creates
│   ├── index.md              derived
│   ├── archive/              the archived state (second of two), moved never deleted
│   └── *.md
├── output/               ③ integration layer: the human initiates assembly
│   ├── index.md              derived
│   └── …                     internal structure set by the form spec target selects; currently
│                             (system design) = the system.md spine + modules/, one module one doc
└── board/                free surface: the human's own boards, one file one board (comparisons
    ├── index.md              or any scratch reasoning), no schema; the most downstream — may
    └── *.md                  reference the three layers, never referenced (derived index as usual)
```

Every layer index and the canvas HTML are projections: regenerated with the cards, holding
no facts; the canvas HTML sits beside the workspace and may be committed for sharing.

A host may hold **many workspaces under any directory names**. The host project root
carries the registry (`.design-harness/config.json`) recording every workspace path;
discovery trusts the registry, never the directory name. The registry may also record
the canvas delivery target (output path or published link) so rebuilds across sessions
land on the same file and link. The registry is not truth — it can be lost or stale and
discovery rebuilds it from the tree.

## Module → file mapping

- source / idea / output → the workspace's three layer dirs (behavior boundaries in [modules/](modules/source.md)).
- canvas → build_canvas.py + canvas/ (including styles/).
- agent → SKILL.md.
- protocol → SKILL.md's structure and disciplines sections + the two validators + the workspace's logs.md.

**Provenance**: [SKILL.md and protocol fuse into one file](../ideas/skill-and-protocol-single-file.md) ·
[many workspaces, freely named](../ideas/workspaces-many-and-freely-named.md) ·
[protocol decoupled from runtime](../ideas/runtime-agnostic-protocol.md) ·
[one engine, many schemas](../ideas/one-engine-many-schemas.md) ·
[projections hold no facts](../ideas/drafts-not-state.md) ·
[tabbed gallery template](../ideas/archive/tabbed-gallery-template.md) ·
[single canvas, three clusters](../ideas/archive/single-canvas-clustered-graph.md) ·
[protocol taught in place](../ideas/protocol-discoverability-in-situ.md) ·
[style–canvas orthogonality](../ideas/style-canvas-orthogonality.md).
