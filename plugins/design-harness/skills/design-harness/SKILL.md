---
name: design-harness
description: A decision board for evidence-based calls — the human adjudicates, the agent runs the errands. Three layers (sources → ideas → output) in plain markdown, kept in permanent two-way sync, projected onto a visual canvas. Use for vendor/tool selection, literature reviews, due diligence, competitive analysis, or any contested call that must stand on traceable evidence — triggers like "file these papers", "put this on the board", "assemble the design", "how do we decide this".
license: MIT
allowed-tools: Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/*)
metadata:
  author: tigerless.ai
  repository: https://github.com/tigerless-labs/design-harness
---

# design-harness — the human adjudicates, the agent runs errands

When triggered, operate the workspace at `docs/design-harness/` (or wherever an
existing workspace lives). Markdown is the **only source of truth**; every other surface —
indexes, backlinks, layout, the canvas HTML — is a projection that can be regenerated at any
time and is **never committed**.

Full contract (card schema, facts, sync invariants, ledger format):
[references/protocol.md](references/protocol.md). Read it once per session before writing.

## The three layers

1. **sources/** — evidence. One source, one card, filed under `sources/<type>/`. The agent
   files and grades these freely, and picks the type dir itself — no preset list; name it
   for what the source is (papers, github, podcasts, …) and create new dirs as needed. The
   dir name is projected verbatim as the card's canvas badge.
2. **ideas/** — judgment. **Only the human creates ideas.** Two states: live (the file
   exists) and archived (moved to `ideas/archive/`, never deleted). When a new idea repeats
   an old one's judgment, merge them automatically; if they conflict, put both on the board
   and let the human pick.
3. **output/** — assembly. The **human initiates** the first assembly; its form comes from
   [references/output-forms/](references/output-forms/system-design.md) and the human's
   `target.md`. Before output exists, ideas are primary and human input lands in ideas only.

Plus one free surface: **board/** — the human's own boards, one markdown file per board
(a comparison matrix, a theme grid, any scratch reasoning). **No schema, no required
fields** — the freedom belongs to the human; you edit a board only when asked ("lay these
three sources out as a comparison"). Boards may reference the three layers; **nothing may
reference a board** — it is terminal, and a board's conclusions must be distilled into an
idea card (human-created) to enter the flow.

## The sync invariant (never break this)

Once output exists, the two layers stay in permanent two-way sync, same turn:

- Human adds or changes an idea → re-derive the affected output elements (re-derive, don't
  rewrite the whole document).
- Human edits output → back-calibrate the change into ideas (you transcribe; the judgment
  is still theirs).
- Conflict between the layers → **output wins**.
- Every sync writes the ledger: one line per layer touched (see protocol).

## The errand list (yours)

Intake and grade sources · derive references and tag classification (one pass — both are
relationship reads) · anchor every output claim to its evidence · auto-merge same-judgment
ideas · refresh existing output · back-calibrate human output edits into ideas · regenerate
the touched layer's index · append the ledger · assemble drafts when asked. Disagreements
between sources go on the board as-is; you never pick a side, and you never create or
archive an idea or start the first assembly on your own.

## Teach in place, never lecture

- Workspace young, no output: leave the assembly seat visibly empty — say once that output
  starts on the human's word.
- Ideas look mature: suggest assembly in one line; don't push twice.
- Human asks for output too early: comply, deliver it honestly thin, and say which ideas are
  missing — never refuse.
- First assembly: state the sync invariant in one line ("from now on, edits on either side
  sync to the other; conflicts resolve toward output").
- Every sync: give a one-line receipt of what was re-derived or back-calibrated.

## Getting started

`<skill-dir>` below is this skill's own directory, wherever the host agent installed it.

```bash
python3 <skill-dir>/scripts/init_workspace.py <workspace>   # idempotent bootstrap
```

After **every** write, run both validators:

```bash
python3 <skill-dir>/scripts/check_workspace.py <workspace>
python3 <skill-dir>/scripts/check_doc_links.py <workspace>
```

## Target and output forms

`target.md` registers the human's acceptance criteria; output fulfils that list, and target
changes are a refresh trigger just like idea changes. When the human sets a target,
recommend a form from [references/output-forms/](references/output-forms/system-design.md)
— first in the library: **system-design** (mermaid diagrams as the markdown itself, plus a
`modules/` layer, one module one file).

## The canvas

The canvas is the human's main thinking surface and is **only a projection** — it holds no
facts and accepts no writes that bypass markdown. There is exactly one canvas — the unified
canvas ([template](canvas/template.html); its interaction contract lives in the workspace's
canvas module doc) — and one fixed builder:
rules (truth-driven, edges = in-card references, layout derived from references + tags) live
in the builder; the workspace path is the only required input.

```bash
python3 <skill-dir>/scripts/build_canvas.py <workspace> -o <temp-dir> [--css style.css] [--title '...']
```

Visual style is CSS-only and lives entirely in the style pack at `canvas/styles/`: the
template carries a `/*__CSS__*/` slot and no CSS of its own. Every style ships a precompiled
`canvas/styles/<slug>/canvas.css`. The default build embeds the whole pack and a toolbar
style switcher — the human changes skins live for the session, and every open starts on
pin-and-paper (the canvas's native look). Passing
`--css canvas/styles/<slug>/canvas.css` builds a pinned single-style canvas with no
switcher. Never fork the template or the builder for looks.

Build into a temp directory, an artifact, or a fixed `canvas.html` at the workspace root
(gitignore it) — the projection never enters version control. Whenever the markdown truth
changes, rebuild and republish the canvas in the same turn; never edit the HTML directly.

A build is not delivered until the human holds a clickable link. The output is one fully
self-contained HTML file (all dependencies inlined, zero network requests), so any host
works. **Default delivery is a published HTML link**: publish the file as an artifact (or
the host's equivalent hosted page) and give that URL. The one exception is Claude Code (a
local CLI session), where a local link works: give the absolute `file://…/canvas.html`
URL, or serve the temp dir with a local static server and give that URL. Either way,
**every rebuild reuses the existing link**: republish to the same artifact URL, or
overwrite the same local file path — mint a new link only when the human asks for one.

To pick a style, read [canvas/styles/selection-index.json](canvas/styles/selection-index.json) — never
bulk-read the pack. Open a style's `design.md` only when (re)compiling its canvas.css —
the spec is the truth, so whenever a design.md changes, recompile its canvas.css in the
same change (the pack validator checks token coverage in both palettes and bans external
reach).
