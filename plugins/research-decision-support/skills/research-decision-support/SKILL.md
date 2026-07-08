---
name: research-decision-support
description: Decision support for research — weave what you read (papers, repos, posts, reports) into provenance-linked decisions you can defend. Four structural layers (sources → synthesis → ideas → decisions), maintained in any order, each with a fixed card format; the agent files evidence and coaches the method, the judgment stays yours. Use when doing a literature review, evaluating vendors/tools, due diligence, competitive analysis, or landing a contested call — triggers like "file these papers", "compare these directions", "decide this contested point", 整理这批论文、做个方向对比、这个点怎么决策.
license: MIT
allowed-tools: Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/*)
metadata:
  author: tigerless.ai
  repository: https://github.com/tigerless-labs/research-decision-support
---

# research-decision-support — reading → defensible decisions

When triggered, enter **synthesis mode**. The four layers are **structure, not stages** — move
across them at the pace real work happens (open a decision after the first batch of sources,
read more, revise an idea, reopen a verdict), in any order. The skill never imposes a
sequence; it does exactly one job: **file every block the user produces into the right layer,
keep it atomic, keep the links unbroken.** Layers relate by provenance (decisions weigh
ideas, ideas cite sources), not by time. What gets built from the decisions lives downstream
in the project's own docs and links back to the decision cards that justify it.

Card types and frontmatter contract: [note-types](references/note-types.md). The skeleton
borrows proven practice: Zettelkasten (atomic + linked) · Webster-Watson concept matrices ·
ADR + decision trade-off methods (ATAM, set-based design).

**Hard rules**:

- **Three voices never share a card**: literature note (source says) ≠ permanent note (I say)
  ≠ decision (we decide). See [note-types](references/note-types.md).
- **Relative Markdown links** connect cards; `[[wikilinks]]` are not the link mechanism.
- **Append-only**: ADRs are never edited — a new one `supersedes` the old.
- After every write, run the validators:
  `python3 ${CLAUDE_SKILL_DIR}/scripts/check_doc_links.py <docs-root>` and
  `python3 ${CLAUDE_SKILL_DIR}/scripts/check_workspace.py <workspace>`.

**Card discipline** (every card, every time):

- **Real-time capture**: the moment a decision lands in conversation, it lands in a card.
- **Deferred content quarantined**: mark it "deferred", keep it minimal, in its own section —
  never interleaved with settled content.
- **Settled = distilled**: decided content in its final compressed form, no derivation trail.
- **Readable at a glance**: settled / deferred / open are visually separate in every card.

## Getting started

The workspace lives at `docs/research-decision-support/` by default — if a workspace already
exists elsewhere in the project, use that one instead. On first use, bootstrap the skeleton
(idempotent, never overwrites):

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/init_workspace.py <workspace>
```

Open each round by saying in one line **which layer you're touching and what you're doing**,
then start. Bottom-up (sources → ideas → decisions) and top-down (open the decision first,
backfill evidence) are both fine.

## Start light — layers earn their place

Don't impose all four layers on a young workspace. Start with **sources + ideas** only.
Activate a layer when its signal appears, and say so in one line:

- **synthesis** — when sources start clustering and comparisons repeat (~10+ sources).
- **decisions** — the first time two options genuinely contend.

An empty layer directory is fine; a force-filled one is noise.

## Proactive coaching — the skill's other half

Filing is the passive half; the active half is **recognizing the moment and nudging one step**.
Act on the trigger, don't wait for instructions:

- **New material arrives** (user reads/cites/discusses a paper, repo, post, report) → file a
  source card into the right subtype directory and update the index. Never ask first.
- **Unassigned sources pile up** (new cards clearly exceed existing directions) → propose a
  clustering: "do these belong with direction X, or is this a new direction?" Offer a tentative
  grouping, but only write the synthesis card **after the user rules** — directions are the
  user's judgment, not the agent's.
- **Judgments scattered in chat** ("I think…", "this seems weak", "interesting") → prompt
  promotion: worthwhile judgments become idea cards (status: candidate) with citations attached
  on the spot; explicitly say when something isn't worth keeping.
- **An adopted idea sits unweighed** (no decision references it) → point it out when timely:
  open the decision it belongs to, or downgrade/cut it.
- **Two options tug back and forth** → open a decision worksheet (drivers × options ×
  trade-offs), converge to an ADR.

Restraint: one nudge at a time, one sentence of reasoning; if the user passes, drop it — never
repeat the pitch.

## The four layers (maintain in any order)

What each layer *holds* — not an execution order. Any layer can change at any time.

### sources — `sources/` (`papers/` `repos/` `posts/` …)
- One literature note per source (core claims, method, strengths/weaknesses, relevance to this
  project). Facts only — no judgment mixed in. Follow the existing card format in the directory.
- **Auto-file by type** into subdirectories; the type set is open — create a new one
  (`videos/`, `datasets/`, …) rather than force-fitting.

### synthesis — `synthesis/`
- Cluster sources into directions: one MOC per direction
  ([direction-moc](templates/direction-moc.md)) + a concept matrix (sources × dimensions +
  **a "my verdict" column**). Organize by concept, never by author.
- **Every direction states its boundary**: name the adjacent/confusable directions and where
  the line is — directions must be mutually exclusive.

### ideas — `ideas/`
- Each endorsed thought or new claim becomes one permanent note
  ([idea-note](templates/idea-note.md)): **in your own words, atomic, citing the sources it
  rests on**. `status: candidate / adopted / doubtful` (候选/采纳/存疑 equally valid).
- Key: not a summary of a source — your claim.

### decisions — `decisions/`
Contested points get a worksheet ([decision-worksheet](templates/decision-worksheet.md)),
skeleton **drivers → options → trade-offs → verdict**:
- **Drivers** (weighted quality attributes) are the point: decide against cost /
  maintainability / convergence …, not in a vacuum (ATAM sensitivity/trade-off points).
- **Set-based options**: keep ≥2 variants alive, narrow with evidence — don't bet early.
- **Trade-offs**: options × drivers, evidence linked from source cards.
- **Reversibility gate**: two-way doors just get tried; only one-way doors get the full
  treatment (Bezos).
- **Bayesian reopen**: record what new evidence would overturn this decision.

Settled worksheets **collapse into an ADR** ([adr](templates/adr.md), `supersedes` the old,
append-only). `affects` anchors the verdict to the ideas it settles — or to stable IDs in
the project's downstream design docs, which live outside the workspace and link back.

## Closing each round

Run both validators (no dangling links, frontmatter conforms); state in one line **which
layers changed**.

## Rendering is a projection — never committed

When the user wants to see the whole picture (or share it), render the workspace into the
workbench (overview / read / compare / ideas / decisions / map + card reader):

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/build_site.py <workspace> -o /tmp/workbench --title <name>
```

Output goes to a **temp directory**, or publish it as an artifact — **generated HTML is never
committed**. Markdown is the single source of truth; the projection rebuilds in one command.
The read page supports in-flow tagging (status / direction / one-line take, saved as browser
drafts); when the user hands back an exported patch, write each entry into the corresponding
card's frontmatter and body.
