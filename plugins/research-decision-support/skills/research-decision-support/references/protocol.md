# protocol — the portable contract

Everything here is enforced by `scripts/check_workspace.py` and
`scripts/check_doc_links.py`; when this contract changes, the validators change in the same
commit.

## Workspace layout

```
<workspace>/
├── target.md             the human's acceptance criteria; source of the output form
├── logs.md               append-only change ledger — the only audit trail (docs stay
│                         out of git)
├── index.md              workspace entry point (projection)
├── sources/              ① evidence: one source, one card; type dirs are thin shells,
│   ├── index.md            the path is the type (projection)
│   └── <type>/*.md
├── ideas/                ② judgment: only the human creates these
│   ├── index.md            (projection)
│   ├── archive/            archived state — cards move here, never deleted
│   └── *.md
├── output/               ③ assembly: human-initiated; inner layout set by the chosen
│   ├── index.md            output form (projection)
│   └── …
└── board/                free surface: one file, one board (a comparison, anything);
    ├── index.md            human-owned, no schema (projection index as usual)
    └── *.md
```

## Rendering contract — the engine's minimum

All the projections require. Everything below this section is methodology, freely
reconfigurable per schema; this section is the engine.

- The four layer names: `sources/` and `ideas/` become canvas nodes, `output/` and
  `board/` become document panels. An `archive/` path segment excludes; `index.md`
  excludes.
- Files are UTF-8 markdown.
- Frontmatter is optional; when present it must close (`---` … `---`).

Everything else degrades, never breaks: no H1 → filename stem shown; no tag →
*未分类* group; any source type dir → its name projected verbatim; unresolvable
link → no edge. Silent data loss is a validator error, never a shrug: markdown under
an unknown top-level dir, and frontmatter that opens without closing, are INVALID.

## Card schema

- A card is **frontmatter + title + summary**. No fixed sections; references are inline
  links in the summary.
- `ideas/` cards (including `archive/`): frontmatter **requires `id` and `type`**;
  `tags` optional. No status field — existence is the live state, location under
  `archive/` is the archived state.
- `sources/` cards: frontmatter optional; when present, only `tags` is read.
- `board/` documents: **no schema**; the single-tag rule still applies if tags appear.
  Boards are **terminal**: they may reference any layer, but sources/ideas/output must
  never reference a board — distill a board's conclusion into an idea card instead.
- Principles inside output documents are bullet lists, one principle per bullet — never
  paragraphs — so each can be cited, edited, and ledgered on its own.
- In the system-design output form, diagrams **are** the markdown: mermaid blocks with
  `click` declarations pointing at module files — never prose plus an external image.

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

## Indexes are projections

Each layer's `index.md` groups cards by tag as `## TAG：one line on why they belong
together`, with untagged cards flat at the end after a `---` rule and an `*未分类*` marker.
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
