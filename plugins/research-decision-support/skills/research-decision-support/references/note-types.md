# Three card types + frontmatter contract

## Three voices never share a card (the linchpin)

| Card | Holds | Location | Frontmatter |
|---|---|---|---|
| **Literature note** | what a source **says** — claims, method, strengths/weaknesses | `sources/` (subdirs `papers/` `repos/` `posts/` …) | follows the directory's existing card format (prose; frontmatter optional) |
| **Permanent note** | what **I say** — my claim/new idea, in my own words, citing sources | `ideas/` | `type: idea` |
| **Design** | permanent notes **assembled**: one spine (principles + pipeline + invariants) + per-module files | `design/` | `type: design` |

Plus the **direction MOC** (`synthesis/`, `type: direction`) and the **decision worksheet /
ADR** (`decisions/`, `type: decision` / `adr`).

**Why the split**: a permanent note is not a source summary. Decoupling "the source says" from
"I say" is what lets a thought leave its original context and recombine freely into designs.

## Frontmatter contract (enforced by `scripts/check_workspace.py`)

Only structured cards carry frontmatter; prose source cards are exempt. Missing required
fields or out-of-range status → validator error.

- `type: direction` — requires `id` `type`
- `type: idea` — requires `id` `type` `status`;
  `status ∈ {candidate, adopted, doubtful}` (候选/采纳/存疑 equally valid)
- `type: design` — requires `id` `type`
- `type: decision` — requires `id` `type` `status` `affects`; `status ∈ {open, resolved}`
- `type: adr` — requires `id` `type` `status`; `status ∈ {proposed, accepted, superseded}`

`affects` anchors a decision to stable element IDs in the `design/` spine.

## Link convention

Cards connect via **relative Markdown links** (`[label](../sources/papers/<id>.md)`): they
render on GitHub, backlink in Obsidian, and are checkable by `scripts/check_doc_links.py`.
`[[wikilinks]]` are **not** the link mechanism.

Provenance chain: `design element → ideas/<id>.md → sources/<subdir>/<id>.md` — any design
choice walks back to its sources along relative links.
