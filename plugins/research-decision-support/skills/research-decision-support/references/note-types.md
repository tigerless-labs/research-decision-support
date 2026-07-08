# Three card types + frontmatter contract

## Three voices never share a card (the linchpin)

| Card | Holds | Location | Frontmatter |
|---|---|---|---|
| **Literature note** | what a source **says** — claims, method, strengths/weaknesses | `sources/` (subdirs `papers/` `repos/` `posts/` …) | follows the directory's existing card format (prose; frontmatter optional) |
| **Permanent note** | what **I say** — my claim/new idea, in my own words, citing sources | `ideas/` | `type: idea` |
| **Decision** | what **we decide** — options weighed on evidence, verdict + consequences | `decisions/` | `type: decision` / `adr` |

Plus the **direction MOC** (`synthesis/`, `type: direction`).

**Why the split**: a permanent note is not a source summary. Decoupling "the source says" from
"I say" is what lets a thought leave its original context and be weighed on its own evidence.

## Frontmatter contract (enforced by `scripts/check_workspace.py`)

Only structured cards carry frontmatter; prose source cards are exempt. Missing required
fields or out-of-range status → validator error.

- `type: direction` — requires `id` `type`
- `type: idea` — requires `id` `type` `status`;
  `status ∈ {candidate, adopted, doubtful}` (候选/采纳/存疑 equally valid)
- `type: decision` — requires `id` `type` `status` `affects`; `status ∈ {open, resolved}`
- `type: adr` — requires `id` `type` `status`; `status ∈ {proposed, accepted, superseded}`

`affects` anchors a decision to what it settles: idea card IDs, or stable IDs in your
project's downstream design docs (which live outside the workspace and link back).

## Link convention

Cards connect via **relative Markdown links** (`[label](../sources/papers/<id>.md)`): they
render on GitHub, backlink in Obsidian, and are checkable by `scripts/check_doc_links.py`.
`[[wikilinks]]` are **not** the link mechanism.

Provenance chain: `decision → ideas/<id>.md → sources/<subdir>/<id>.md` — any verdict
walks back to its sources along relative links. What you build from the decisions lives
downstream in your own repo and links back to the decision cards that justify it.
