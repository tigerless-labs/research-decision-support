<h1 align="center">research-decision-support</h1>

<p align="center"><strong>Turn what you read into decisions you can defend — every verdict traceable back to its source.</strong></p>

<p align="center">
  <a href="#quickstart">Quickstart</a> ·
  <a href="#the-mental-model">Mental model</a> ·
  <a href="#see-it-on-a-real-project">Live example</a> ·
  <a href="#the-provenance-map">Provenance map</a>
</p>

---

Most "literature review" folders die the same death: a pile of paper summaries nobody rereads,
decisions that cite nothing, and — six months later — no way to answer *"why did we choose
this?"*

**research-decision-support** is an [Agent Skill](https://agentskills.io) (works in Claude Code and any
SKILL.md-compatible agent) that turns reading into a **provenance-linked decision workspace**.
You read; the agent files every output into one of four layers and keeps the links between
them honest. The result is a set of decisions where every verdict traces back through the
ideas it rests on to the papers that earned it.

```
sources ──▶ synthesis ──▶ ideas ──▶ decisions ──▶ (your design docs, downstream)
(papers      (directions,   (my claims,  (trade-offs      (link back to the
 say)         my verdict)    my words)    → ADRs)          decisions they build on)
```

## The mental model

The core move is **separating three voices that everyone mixes together**:

| Voice | Card | Layer |
|---|---|---|
| *What the paper says* | literature note — claims, method, strengths/weaknesses, facts only | `sources/` |
| *What I say* | permanent note — an atomic claim in my own words, citing its sources | `ideas/` |
| *What we decide* | decision record — options weighed on evidence, verdict + consequences | `decisions/` |

Why it matters: when "the paper says" and "I say" live in the same note, your ideas stay
chained to their original context and can never recombine. Split them, and an idea becomes a
free-moving part — quotable, reusable, and attackable on its own evidence.

Two layers keep the middle and the end honest:

- **`synthesis/`** — sources clustered into *directions*, each with a concept matrix
  (sources × dimensions + **a "my verdict" column**). Organized by concept, never by author.
  Each direction must state its boundary against neighboring directions — no mushy overlap.
- **`decisions/`** — contested points get a worksheet: **drivers → options →
  trade-offs → verdict**. Keep ≥2 options alive until evidence collapses them
  (set-based design); reversible decisions just get tried (two-way doors); the verdict
  collapses into an append-only ADR that records *what evidence would reopen it*.

What you *build* from the decisions — architecture docs, specs, code — lives downstream in
your own project, linking back to the decision cards that justify it. Assembly is
domain-specific; the judgment trail is not. That's why design is not a layer here.

### Layers, not stages

The four layers are **structural, not sequential**. Real research doesn't march
sources → decisions; you open a decision after the first batch of papers, read more, revise an
idea, reopen a verdict. The skill never enforces an order — it does exactly one job: **file
every block you produce into the right layer, keep it atomic, keep the links unbroken.**
What *is* enforced is the provenance direction: decisions weigh ideas, ideas cite
sources. That's a dependency graph, not a timeline.

### The intellectual lineage

Nothing here is invented from scratch — it's four proven practices fused into one loop:

- **Zettelkasten** (Luhmann) — atomic notes + explicit links; literature notes ≠ permanent notes
- **Webster & Watson** — concept matrices: organize a review by concept, not by author
- **ADR** (Nygard) — append-only decision records with context and consequences
- **Set-based concurrent engineering** (Toyota) + **ATAM** — keep options alive, decide
  against weighted quality attributes, respect one-way vs two-way doors

## See it on a real project

[`examples/autoharness/`](examples/autoharness/index.md) is the unedited workspace from a
real project (an agent-harness self-evolution research effort): **76 sources → 3 directions →
10 ideas → 4 decisions (1 still open)**, plus the project's downstream design docs linking
back in — every link live. Start at its [index](examples/autoharness/index.md) and follow
any decision backwards to the papers that justify it.

## The workbench

One command renders any workspace into a **self-contained HTML workbench** — one page per
layer, no dependencies, no server, dark/light theme:

```bash
python3 plugins/research-decision-support/skills/research-decision-support/scripts/build_site.py docs/research-decision-support -o /tmp/workbench --title my-project
```

- **Read** — the working loop: digest card per source, filter and search, and tag
  *while you read* — status, direction, a one-line take. Tags are browser drafts;
  one click exports a patch your agent writes back into the cards.
- **Compare** — sources clustered by direction, membership derived from your synthesis
  cards (plus drafts, marked); the unassigned pile is your reading to-do.
- **Ideas** — your claims with their receipts: what each cites and which decisions
  weigh it.
- **Decisions** — the ADR ledger: open vs settled, each linked to the ideas it weighs
  and the evidence behind it.
- **Map** — the provenance graph: hover a card to light up its direct links.
- **Overview** — where you are: counts, directions, progress.

Every card title opens in a built-in reader that renders the markdown properly
([marked](https://github.com/markedjs/marked) + [DOMPurify](https://github.com/cure53/DOMPurify),
MIT, embedded at build time — still zero network requests), with cross-card links staying
inside the reader and a "linked from / links to" trail under each card.

Generated HTML is a throwaway projection — build it into a temp dir (or publish it as an
artifact), never commit it; the markdown stays the single source of truth. Try it on the
bundled example in ten seconds:

```bash
python3 plugins/research-decision-support/skills/research-decision-support/scripts/build_site.py \
  examples/autoharness -o /tmp/workbench-demo --title autoharness
open /tmp/workbench-demo/index.html
```

It's not academia-specific — anything that is "read materials → make a defensible call"
(vendor evaluations, due diligence, competitive analysis) fits the same four layers.

## Quickstart

**1. Install** (Claude Code — this repo is a plugin marketplace):

```
/plugin marketplace add tigerless-labs/research-decision-support
/plugin install research-decision-support@research-decision-support
```

The skill and its scripts travel together — no manual copying, `/plugin marketplace update`
pulls new versions. Any other SKILL.md-compatible agent: point it at
`plugins/research-decision-support/skills/research-decision-support/SKILL.md`.

**2. Use it.** In your project, just talk to your agent:

> *"整理这批论文"* / "file these papers" → literature notes into `sources/`
> *"做个方向对比"* / "compare these directions" → concept matrix into `synthesis/`
> *"这个点怎么决策"* / "decide this contested point" → worksheet → ADR into `decisions/`

Everything lands in `docs/research-decision-support/` as plain Markdown with relative links — renders on
GitHub, backlinks in Obsidian, greppable forever.

**3. Keep it honest:**

The skill bootstraps the workspace on first use, then runs its bundled validators after every
write (zero dangling links, frontmatter conforms) and renders the workbench to a temp dir on
demand — all via `${CLAUDE_SKILL_DIR}`, no setup on your side.

**Start light.** A young workspace needs only `sources/` + `ideas/`; synthesis and
decisions switch on when their signal appears (clusters form, two options contend). The
skill coaches these moments — it never force-fills four layers.

## Hard rules the skill enforces

1. **Three voices never share a card.** Paper-says / I-say / we-decide are separate files in
   separate layers.
2. **Atomic cards, relative Markdown links.** One claim per file; `[[wikilinks]]` are not the
   link mechanism — plain `](../path.md)` links are checkable and render everywhere.
3. **ADRs are append-only.** A new decision `supersedes` the old one; history is never edited.
4. **Real-time capture.** The moment a decision lands in conversation, it lands in a card.
   Nothing lives only in chat.
5. **Settled = distilled.** Decided content is written in its final compressed form; deferred
   content is quarantined in its own minimal section, never interleaved.

## Repo layout

```
.claude-plugin/marketplace.json          this repo IS the marketplace
plugins/research-decision-support/
  .claude-plugin/plugin.json             plugin manifest
  skills/research-decision-support/
    SKILL.md                             the skill
    templates/                           card templates: idea, direction MOC,
                                         decision worksheet, ADR
    references/note-types.md             the three-card contract + frontmatter spec
    scripts/build_site.py           workspace → workbench: overview / read / compare /
                                         ideas / decisions / map + card reader
    scripts/build_map.py            the provenance map page alone
    scripts/check_doc_links.py           dangling-link validator
    scripts/check_workspace.py           frontmatter/status validator (EN + ZH enums)
    scripts/init_workspace.py            one-command idempotent workspace bootstrap
examples/autoharness/                    real 97-card workspace from a live project (not
                                         installed with the plugin — demo only)
tests/                                   pytest suite (incl. injection red-team cases)
LICENSE                                  MIT (vendored marked/DOMPurify keep their headers)
```

## FAQ

**Is this a note-taking app?** No — it's a method your coding agent executes, stored as plain
Markdown in your repo. No database, no server, no lock-in.

**Why not just let the agent "do research"?** Unstructured agent research produces confident
prose with invisible provenance. The skill makes the middle layer — *your* judgment — an
explicit, versioned artifact. When a source is retracted or a benchmark shifts, you can trace
exactly which ideas and decisions are exposed.

**Does it work for non-ML domains?** Yes. The layers are domain-free; the example happens to
be agent-harness research because that's what we built it for.

---

MIT. Built by [Tigerless AI](https://github.com/tigerless-labs). The skill's operating
instructions are written primarily in Chinese (the templates and validator messages are
bilingual-friendly); the method itself is language-neutral.
