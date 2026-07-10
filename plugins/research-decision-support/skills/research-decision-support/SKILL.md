---
name: research-decision-support
description: A decision board for evidence-based calls — the human adjudicates, the agent runs the errands. Three layers (sources → ideas → output) in plain markdown, kept in permanent two-way sync, projected onto a visual canvas. Use for vendor/tool selection, literature reviews, due diligence, competitive analysis, or any contested call that must stand on traceable evidence — triggers like "file these papers", "put this on the board", "assemble the design", 整理这批材料、把想法上板、装配 output、这个点怎么决策.
license: MIT
allowed-tools: Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/*)
metadata:
  author: tigerless.ai
  repository: https://github.com/tigerless-labs/research-decision-support
---

# research-decision-support — the human adjudicates, the agent runs errands

When triggered, operate the workspace at `docs/research-decision-support/` (or wherever an
existing workspace lives). Markdown is the **only source of truth**; every other surface —
indexes, backlinks, layout, the canvas HTML — is a projection that can be regenerated at any
time and is **never committed**.

Full contract (card schema, facts, sync invariants, ledger format):
[references/protocol.md](references/protocol.md). Read it once per session before writing.

## The three layers

1. **sources/** — evidence. One source, one card. The agent files and grades these freely.
2. **ideas/** — judgment. **Only the human creates ideas.** Two states: live (the file
   exists) and archived (moved to `ideas/archive/`, never deleted). When a new idea repeats
   an old one's judgment, merge them automatically; if they conflict, put both on the board
   and let the human pick.
3. **output/** — assembly. The **human initiates** the first assembly; its form comes from
   [references/output-forms/](references/output-forms/system-design.md) and the human's
   `target.md`. Before output exists, ideas are primary and human input lands in ideas only.

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

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/init_workspace.py <workspace>   # idempotent bootstrap
```

After **every** write, run both validators:

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/check_workspace.py <workspace>
python3 ${CLAUDE_SKILL_DIR}/scripts/check_doc_links.py <workspace>
```

## Target and output forms

`target.md` registers the human's acceptance criteria; output fulfils that list, and target
changes are a refresh trigger just like idea changes. When the human sets a target,
recommend a form from [references/output-forms/](references/output-forms/system-design.md)
— first in the library: **system-design** (mermaid diagrams as the markdown itself, plus a
`modules/` layer, one module one file).

## The canvas

The canvas is the human's main thinking surface and is **only a projection** — it holds no
facts and accepts no writes that bypass markdown. Rules (truth-driven, edges = in-card
references, layout derived from references + tags) live in the builder; each template under
[canvases/](canvases/tabbed-gallery/template.html) carries only its own form. When setting a
target, ask which template the human wants — `tabbed-gallery` (implemented) or
`single-canvas` ([design spec](canvases/single-canvas/spec.md), not yet built).

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/build_canvas.py <workspace> -o <temp-dir> --template tabbed-gallery
```

Build only into a temp directory or an artifact — the projection never enters the repo.
Whenever the markdown truth changes, rebuild and republish the canvas in the same turn;
never edit the HTML directly.

For visual styling beyond the template default, use the style pack: read
[styles/selection-index.json](styles/selection-index.json) first and load **only** the
chosen style's `design.md` — never bulk-read the pack.
