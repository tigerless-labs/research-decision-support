<h1 align="center">research-loom</h1>

<p align="center"><strong>Weave 80 papers into a design you can defend — every claim traceable back to its source.</strong></p>

<p align="center">
  <a href="#quickstart">Quickstart</a> ·
  <a href="#the-mental-model">Mental model</a> ·
  <a href="#see-it-on-a-real-project">Live example</a> ·
  <a href="#the-provenance-map">Provenance map</a>
</p>

---

Most "literature review" folders die the same death: a pile of paper summaries nobody rereads,
a design doc that cites nothing, and — six months later — no way to answer *"why did we build
it this way?"*

**research-loom** is an [Agent Skill](https://agentskills.io) (works in Claude Code and any
SKILL.md-compatible agent) that turns reading into a **provenance-linked design workspace**.
You read; the agent files every output into one of five layers and keeps the links between
them honest. The result is a design where every element traces back through the ideas it was
distilled from to the papers that earned it.

```
sources ──▶ synthesis ──▶ ideas ──▶ design ◀── decisions
(papers      (directions,   (my claims,  (spine +     (trade-offs
 say)         my verdict)    my words)    modules)     → ADRs)
```

## The mental model

The core move is **separating three voices that everyone mixes together**:

| Voice | Card | Layer |
|---|---|---|
| *What the paper says* | literature note — claims, method, strengths/weaknesses, facts only | `sources/` |
| *What I say* | permanent note — an atomic claim in my own words, citing its sources | `ideas/` |
| *What we build* | design doc — ideas assembled into a spine + modules | `design/` |

Why it matters: when "the paper says" and "I say" live in the same note, your ideas stay
chained to their original context and can never recombine. Split them, and an idea becomes a
free-moving part — quotable, reusable, and attackable on its own evidence.

Two more layers keep the middle and the end honest:

- **`synthesis/`** — sources clustered into *directions*, each with a concept matrix
  (sources × dimensions + **a "my verdict" column**). Organized by concept, never by author.
  Each direction must state its boundary against neighboring directions — no mushy overlap.
- **`decisions/`** — contested design points get a worksheet: **drivers → options →
  trade-offs → verdict**. Keep ≥2 options alive until evidence collapses them
  (set-based design); reversible decisions just get tried (two-way doors); the verdict
  collapses into an append-only ADR that records *what evidence would reopen it*.

### Layers, not stages

The five layers are **structural, not sequential**. Real research doesn't march
sources → design; you sketch a design after the first batch of papers, read more, revise an
idea, reopen a decision. The skill never enforces an order — it does exactly one job: **file
every block you produce into the right layer, keep it atomic, keep the links unbroken.**
What *is* enforced is the provenance direction: design elements cite ideas, ideas cite
sources, decisions act on design. That's a dependency graph, not a timeline.

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
10 ideas → 8 design docs**, every link live. Start at its
[index](examples/autoharness/index.md) and follow any design doc backwards to the papers
that justify it.

## The workbench

One command renders any workspace into a **self-contained four-page HTML workbench** —
no dependencies, no server, dark/light theme:

```bash
python3 tools/build_loom_site.py docs/research-loom -o loom-site --title my-project
```

- **Read** — the working loop: digest card per source, filter and search, and tag
  *while you read* — status, direction, a one-line take. Tags are browser drafts;
  one click exports a patch your agent writes back into the cards.
- **Compare** — sources clustered by direction, membership derived from your synthesis
  cards (plus drafts, marked); the unassigned pile is your reading to-do.
- **Map** — the provenance graph: hover a card to light up its direct links.
- **Overview** — where you are: counts, directions, progress.

The [demo](docs/index.html) is generated from the autoharness example. It's not
academia-specific — anything that is "read materials → make a defensible call"
(vendor evaluations, due diligence, competitive analysis) fits the same five layers.

## Quickstart

**1. Install the skill** (Claude Code):

```bash
git clone https://github.com/tigerless-ai/research-loom
mkdir -p ~/.claude/skills
cp -r research-loom/{SKILL.md,templates,references} ~/.claude/skills/research-loom/
```

Any other SKILL.md-compatible agent: point it at `SKILL.md`.

**2. Use it.** In your project, just talk to your agent:

> *"整理这批论文"* / "file these papers" → literature notes into `sources/`
> *"做个方向对比"* / "compare these directions" → concept matrix into `synthesis/`
> *"把这些想法组装成设计"* / "assemble these into a design" → spine + modules into `design/`
> *"这个设计点怎么决策"* / "decide this contested point" → worksheet → ADR into `decisions/`

Everything lands in `docs/research-loom/` as plain Markdown with relative links — renders on
GitHub, backlinks in Obsidian, greppable forever.

**3. Keep it honest:**

```bash
python3 tools/check_doc_links.py docs        # zero dangling links
python3 tools/build_loom_site.py docs/research-loom -o loom-site
```

## Hard rules the skill enforces

1. **Three voices never share a card.** Paper-says / I-say / we-build are separate files in
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
SKILL.md                 the skill (drop into ~/.claude/skills/research-loom/)
templates/               card templates: idea, direction MOC, design, decision worksheet, ADR
references/note-types.md the three-card contract + frontmatter spec
tools/build_loom_site.py workspace → 4-page workbench: overview / read / compare / map
tools/build_loom_map.py  workspace → the provenance map page alone
tools/check_doc_links.py dangling-link validator
examples/autoharness/    real 97-card workspace from a live project
docs/index.html …        the demo workbench, generated from the example
```

## FAQ

**Is this a note-taking app?** No — it's a method your coding agent executes, stored as plain
Markdown in your repo. No database, no server, no lock-in.

**Why not just let the agent "do research"?** Unstructured agent research produces confident
prose with invisible provenance. The loom makes the middle layer — *your* judgment — an
explicit, versioned artifact. When a source is retracted or a benchmark shifts, you can trace
exactly which ideas, designs, and decisions are exposed.

**Does it work for non-ML domains?** Yes. The layers are domain-free; the example happens to
be agent-harness research because that's what we built it for.

---

MIT. Built by [Tigerless AI](https://github.com/tigerless-ai). The skill's operating
instructions are written primarily in Chinese (the templates and validator messages are
bilingual-friendly); the method itself is language-neutral.
