# protocol — the portable contract

The checkable parts are enforced by `scripts/check_workspace.py` and
`scripts/check_doc_links.py`; when this contract changes, the validators change in the
same commit.

## Workspace layout

```
<workspace>/
├── target.md             the human's acceptance criteria; source of the output form
├── logs.md               append-only change ledger (see The ledger)
├── index.md              workspace entry point
├── sources/<type>/*.md   ① evidence: one source, one card
├── ideas/*.md            ② judgment (archive/ holds archived cards)
├── output/…              ③ assembly, laid out by the chosen output form
└── board/*.md            free surface: one file, one board
```

Every layer also holds an `index.md` (see Indexes are projections).

## Rendering contract — the engine's minimum

Everything the projections require. All sections below this one are methodology, freely
reconfigurable per schema; this section is the engine.

- The four layer names: `sources/` and `ideas/` become canvas nodes, `output/` and
  `board/` become document panels. An `archive/` path segment excludes; `index.md`
  excludes.
- Files are UTF-8 markdown.
- Frontmatter is optional; when present it must close (`---` … `---`).

Everything else degrades, never breaks: no H1 → filename stem shown; no tag →
*unclassified* group; any source type dir → its name projected verbatim; unresolvable
link → no edge. Silent data loss is a validator error, never a shrug: markdown under
an unknown top-level dir, and frontmatter that opens without closing, are INVALID.

## Card schema

- A card is **frontmatter + title + summary**. No fixed sections; references are inline
  links in the summary.
- `ideas/` cards (including `archive/`): frontmatter **requires `id` and `type`**;
  `tags` optional. No status field — existence is the live state, location under
  `archive/` is the archived state.
- `sources/` cards: frontmatter optional; when present, only `tags` is read.
- `board/` documents: **no schema**. Boards are **terminal**: they may reference any
  layer, but sources/ideas/output must never reference a board — distill a board's
  conclusion into an idea card instead.

## Exactly two structured facts

1. **References** — inline markdown links in a card's body. Forward-only: a link points at
   the evidence or prior card this card stands on, never at supporters. "Who cites me" is a
   derived backlink, computed by projections, never written down. **No cycles**: mutual
   references mean the cards should merge, or one edge is a misclassified backlink — drop
   it.
2. **Tags** — single layer, **at most one per card**, optional. A card that genuinely
   belongs to two tags is two cards: split it. Untagged simply means unclassified. Tags may
   be proposed by the human or assigned by the agent.

Everything else — backlinks, distance, coordinates, clusters, index groupings — is derived
and never enters the truth.

## Output documents

- Principles are bullet lists, one principle per bullet — never paragraphs — so each can
  be cited, edited, and ledgered on its own.
- In the system-design form, diagrams **are** the markdown: mermaid blocks with `click`
  declarations pointing at module files — never prose plus an external image.

## Indexes are projections

Each layer's `index.md` groups cards by tag as `## TAG: one line on why they belong
together`, with untagged cards flat at the end after a `---` rule and an `*unclassified*` marker.
Regenerate the touched index in the same turn as any card change. Search goes through the
index; there is no classification layer.

## The ledger

`logs.md` is append-only and covers ideas **and** output. One line per layer touched per
change:

```
- YYYY-MM-DD · card-or-doc · action · delta (old → new) · reason
```

Record the **delta itself** — the minimal old → new — not just the action and reason. The
workspace stays out of git, so the ledger is the only way back.

## Sync invariants

- Before output exists: human input lands in ideas only; ideas are primary.
- First assembly: human-initiated, form from `target.md` + the output-forms library.
- After output exists: two-way sync every turn — idea change re-derives affected output
  elements; human output edits back-calibrate into ideas; **conflicts resolve toward
  output**; each sync writes one ledger line per layer.
- Target changes are refresh triggers, same discipline as idea changes.

## Projection discipline

- Markdown first, always: change the truth, then rebuild every affected projection
  (indexes, canvas HTML) in the same turn. Editing a projection directly is forbidden.
- Projections are disposable: built into temp directories or artifacts, never committed.

## Runtime

The protocol binds this contract, not a host: the CLI is the first host, not the form
itself. One engine serves many thin schemas — a new persona scenario is a new schema
configuration, not a new engine.
