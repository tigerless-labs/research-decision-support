---
name: design-harness
description: A decision board for evidence-based calls — the human adjudicates, the agent runs the errands. Three layers (sources → ideas → output) in plain markdown, synced on the human's command, projected onto a visual canvas. Use for vendor/tool selection, literature reviews, due diligence, competitive analysis, or any contested call that must stand on traceable evidence — triggers like "file these papers", "put this on the board", "assemble the design", "how do we decide this".
license: MIT
allowed-tools: Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/*)
metadata:
  author: tigerless-labs
  repository: https://github.com/tigerless-labs/design-harness
---

# design-harness — the human adjudicates, the agent runs errands

Markdown is the **single source of truth**; the canvas HTML, every layer index, and the
location registry are projections, rebuildable at any time. Judgment comes only from the
human; you lay out options and evidence and run the errands — never adjudicate in the
human's place.

## Structure

### Workspace layout

```
<workspace>/
├── target.md             the human's acceptance criteria; source of the output form
├── logs.md               append-only change ledger (see "Disciplines · Ledger")
├── index.md              workspace entry point
├── sources/<type>/*.md   ① evidence: one source, one card
├── ideas/*.md            ② judgments (archive/ holds archived cards)
├── output/…              ③ assembly; internal structure set by the chosen output form
└── board/*.md            free surface: one file, one board
```

A host may hold many workspaces under any directory names; the sole registry is
`.design-harness/config.json` at the host root — discovery trusts the registry, never
the directory name.

Every layer also carries an `index.md`, grouped under tag headings (`## TAG: one line on
why they belong together`), unclassified cards flat at the end after a `---` divider and
an *unclassified* marker. Search goes through the indexes; there is no classification
layer.

### Three layers + the free surface

1. **sources/ — evidence.** One source, one card, filed under `sources/<type>/`. The
   agent ingests and grades freely, and invents the type directories itself — no preset
   list; name them after what the source is (papers, github, podcasts, …), adding
   directories as needed. The directory name projects verbatim as the card's badge on
   the canvas.
2. **ideas/ — judgments.** **Judgment comes only from the human**: decision judgments the
   human voices in conversation are transcribed into idea cards automatically, and the
   human can simply ask for a card to be added; the agent transcribes, never invents.
   Two states: live (the file exists) and archived (moved into `ideas/archive/`, never
   deleted). A new idea repeating an old card's judgment merges automatically; a
   conflicting one puts both on the board for the human to pick.
3. **output/ — assembly, the convergent layer.** **First assembly is human-initiated**;
   its form comes from [references/output-forms/](references/output-forms/system-design.md)
   and the human's `target.md`. Ideas diverge, output converges: output changes only on
   the human's word (see "Workflow · Sync").

One free surface besides: **board/** — the human's own boards, one markdown file per
board (comparison matrices, theme grids, any scratch reasoning). **No schema, no
required fields** — this freedom belongs to the human; edit only when asked ("lay these
three sources out as a comparison").

### Card schema and templates

- A card = **frontmatter + title + summary**. No fixed sections; references are inline
  links in the summary.
- `ideas/` cards (including `archive/`): frontmatter **requires `id` and `type`**;
  `tags` and `conflicts` optional (see "Exactly three structured facts"). No status
  field — the file's existence is the live state, sitting under `archive/` is the
  archived state.
- `sources/` cards: frontmatter optional; when present only `tags` is read.
- `board/` documents: **no schema**. The board is **terminal**: it may reference any
  layer, but sources/ideas/output must never reference the board — distill a board's
  conclusions into idea cards.

idea card template:

```markdown
---
id: <kebab-slug, matching the filename>
type: idea
tags: [<at most one; omit the whole line>]
conflicts: [<ids of prior cards this judgment contends with; omit when none>]
---

# <the judgment in one sentence>

<Summary: what the judgment says and why; the evidence and prior cards it stands on as
inline links.>
```

source card template:

```markdown
---
tags: [<at most one; the whole frontmatter may be omitted>]
---

# <source name + one-line characterization>

<Core content + relevance to this project; the original provenance (arXiv/URL/date/
authors) as inline links.>
```

target template:

```markdown
# target — acceptance criteria for the output

## Purpose
(One paragraph: what this workspace decides, for whom, and where the boundaries are.)

## Current requirements
- (One checkable requirement per line.)

## Fulfilment map
- (Requirement → output file mapping, updated with each assembly.)
```

### Exactly three structured facts

1. **References** — inline markdown links in the card body. Forward only: a link points
   at the evidence or prior cards this card stands on, never at supporters. "Who cites
   me" is a projection-derived backlink, never written down. **Acyclic**: mutual
   references mean the two cards should merge, or one edge is a mistakenly written
   backlink — delete it.
2. **Tags** — single level, **at most one per card**, optional. A card that truly
   belongs to two tags is two cards: split it. No tag just means unclassified. Tags may
   be proposed by the human or assigned by the agent.
3. **Conflict** — the optional `conflicts: [<other card's id>]` in the **newer** card's
   frontmatter, declaring a judgment conflict with prior cards (written on the new card
   only, acyclic, same direction as references). The field lives exactly as long as the
   conflict: the human's adjudication removes it — archive the loser and the edge
   vanishes with the card; rewrite in place and the entry is deleted. The indexes'
   pending-conflict annotations derive from this field.

Everything else — backlinks, distances, coordinates, clusters, index groupings — is
derived and never enters the truth.

### Rendering contract — the engine's minimum

Everything projection needs. **This section is the engine; everything else in this file
is methodology**, freely reconfigurable per schema — one engine serves many thin
schemas, a new scenario is a new schema configuration rather than a new engine; the
contract binds files, and the CLI is only the first host.

- Four layer names: `sources/` and `ideas/` become canvas nodes, `output/` and `board/`
  become document panels. Paths containing an `archive/` segment are excluded;
  `index.md` is excluded.
- Files are UTF-8 markdown.
- Frontmatter is optional; when present it must close (`---` … `---`).

Everything else degrades without breaking: no H1 → show the filename stem; no tag → the
*unclassified* group; any source type directory → the name projects verbatim;
unresolvable link → no edge. Silent data loss is a validator error, never waved through:
markdown under an unknown top-level directory, or frontmatter opened but never closed,
is INVALID.

### Canvas — the only projection surface

The canvas is the human's main thinking surface and **only a projection** — it holds no
facts and accepts no writes that bypass markdown. There is exactly one canvas — the
unified canvas ([template](canvas/template.html); its interaction contract lives in the
workspace's canvas module doc) — and exactly one builder: the rules (truth-driven,
edges = in-card references, layout derived from references + tags) are built in, and
the workspace path is the only required input. Conflict edges render **red** — a
template-base default every style pack inherits and may override.

Visual style is pure CSS, living entirely in the `canvas/styles/` style pack; the
template carries a single `/*__CSS__*/` slot and no CSS of its own. The default build
embeds the whole pack plus the top-right toolbar switcher — the human reskins live there
(every open starts from the pin-and-paper native look); you only hint at the switcher
once. `--css canvas/styles/<slug>/canvas.css` pins one style with no switcher — to name
a slug, read [canvas/styles/selection-index.json](canvas/styles/selection-index.json),
never bulk-read the whole pack. Never fork the template or the builder for looks; when a
style's `design.md` changes, recompile its `canvas.css` in the same change — the spec is
the truth (the pack validator checks the dual palettes and bans external reach).

## Workflow

0. **Discover the workspace** (the first step on every trigger). Order: a path the human
   gives > the `.design-harness/config.json` registry > the default
   `docs/design-harness/`. More than one candidate, or zero: ask — **never initialize a
   new workspace silently** (init in the wrong place forks the truth). Only the
   bootstrap writes the registry; on finding a workspace the registry missed, re-run the
   bootstrap to record it. A fresh bootstrap ends by asking the human for the target
   (purpose and acceptance criteria, in the human's words) — transcribe the answer into
   `target.md`, never invent one; the human may defer. Scripts run at the host project root (`<skill-dir>` is
   wherever this skill is installed):

   ```bash
   python3 <skill-dir>/scripts/discover_workspace.py          # prints which workspace resolves
   python3 <skill-dir>/scripts/init_workspace.py <workspace>  # bootstrap: skeleton + registry + both validators
   ```
1. **Ingest evidence**: file source cards, grade, anchor to provenance; source
   disagreements go on the board as-is.
2. **Transcribe judgments**: judgments the human voices in conversation transcribe into
   idea cards automatically; same-judgment cards merge automatically, conflicts go on
   the board for the human to pick; derive references and tag classification (one
   pass — both are relationship reads).
3. **Sync (on the human's command, never automatic)**: idea → output re-derivation runs
   only when the human orders it — apply directly with a one-line receipt, a diff first
   for large changes; re-derive the affected elements, never rewrite the whole document.
   A human edit to output is itself an adjudication: back-transcribe it into idea cards
   automatically (transcription only). Target changes follow the same discipline as idea
   changes. When output lags you may hint once ("output is N ideas behind"), never
   twice.
4. **Assemble**: first assembly is human-initiated; the form comes from `target.md` +
   the output-forms library — when the human sets a target, recommend a form from the
   library; if `target.md` is still blank when assembly is called for, ask for the
   target once more before recommending; the first is **system-design** (mermaid diagrams are the markdown body
   itself, plus a `modules/` layer, one module per file). Anchor every output claim to
   evidence; write principles as bullet lists, one principle per bullet — so each can be
   referenced, edited, and ledgered on its own; in the system-design form the diagram
   IS the markdown body: mermaid blocks carry `click` declarations into module files.
5. **Project and deliver**: whenever the truth changes, regenerate the touched layers'
   indexes, rebuild the canvas, and republish in the same turn; append the ledger.

   ```bash
   python3 <skill-dir>/scripts/build_canvas.py <workspace> -o <temp-dir> [--css …] [--title '…']
   ```

   Without `<workspace>` the tool discovers on its own (registry → default location) and
   refuses to act on ambiguity. `-o` takes a directory (the file lands inside as
   `canvas.html`) or a `.html` path written as-is. Build targets are a temp dir, an
   artifact, or the fixed `canvas.html` beside the workspace (gitignore it; the builder
   refuses to write inside the workspace). A build is not delivered until the human holds a clickable link. The
   product is one fully self-contained HTML file (all dependencies inlined, zero network
   requests). **The default delivery is a published HTML link**: publish as an artifact
   (or the host's hosted pages) and hand over that URL; in Claude Code (a local CLI
   session) a local link suffices — an absolute `file://…/canvas.html` URL or a local
   static server. **Every rebuild reuses the existing link** — mint a new one only when
   the human asks. So the link survives the session: record the delivery target — the
   HTML output path or the published link — under a `"canvas"` key in the
   `.design-harness/config.json` registry, and read it back before building; later
   sessions then rebuild the same file and republish the same link.

### Teach in place, never lecture

- First contact (the workspace just bootstrapped, whether the skill fired passively or
  on demand): the first move is always to build the workspace, construct the initial
  canvas in the same turn, hand over the link, then orient in one sentence — "From now
  on every resource we look into files itself, and the decision judgments we talk
  through land on the board; you can also just ask me to change things, and tell me
  whenever you want the design assembled." Never repeat it.
- The workspace is young, no output yet: leave the assembly seat visibly empty — say
  once "output starts on the human's word".
- Ideas look mature: suggest assembly in one sentence; never push twice.
- The human asks for output too early: comply, deliver the honestly thin result, and say
  which ideas are missing — never refuse.
- First assembly: state the sync rule in one sentence ("from here output updates only
  when you order a sync; edit output directly and I back-transcribe it into ideas").
- Every sync: give a one-line receipt of what was re-derived or back-transcribed.

## Disciplines

- **The never list**: never pick sides, never invent judgments, never archive an idea on
  your own, never initiate first assembly on your own, never touch output outside the
  human's command.
- **Markdown first**: change the truth first, then rebuild every affected projection
  (indexes, canvas HTML) in the same turn; never edit a projection directly; projections
  are disposable — build to a temp dir or an artifact, never commit them.
- **The ledger**: `logs.md` is append-only and covers both ideas **and** output. Every
  change, one line per touched layer:

  ```
  - YYYY-MM-DD · card or doc · action · delta (old → new) · reason
  ```

  Record **the delta itself** — the minimal old → new — not just the action and reason.
  When the workspace sits outside git, the ledger is the only way back.
- **Validation**: two validators — `scripts/check_workspace.py` and
  `scripts/check_doc_links.py` — run automatically at bootstrap and on every canvas
  build: failure exits nonzero, prints the full problem list, and produces no HTML; fix
  the truth, then rebuild. When this file's contract changes, the validators change in
  the same commit.

## Toolbox

All live in `<skill-dir>/scripts/` and run standalone; command syntax sits at the usage
sites (workflow steps 0 and 5).

- `init_workspace.py` — bootstrap: skeleton (idempotent, never clobbers) + registry
  write + runs both validators itself.
- `discover_workspace.py` — read-only discovery, prints which workspace resolves;
  ambiguity is reported, never resolved silently.
- `build_canvas.py` — the only canvas build entry; runs both validators as a gate, then
  emits the self-contained HTML.
- `check_workspace.py` — schema validation: required frontmatter, single tag, conflicts
  targets, forward-only acyclic references, no inbound board references.
- `check_doc_links.py` — link integrity: no dangling links inside the workspace.
- `check_style_pack.py` — style pack validation: dual palettes, no external reach,
  tokens aligned to the template.
