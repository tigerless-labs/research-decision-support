<h1 align="center">research-decision-support</h1>

<p align="center"><strong>Step one of vibe coding: turn scattered reading and half-formed ideas into a design you can defend.</strong></p>

<p align="center">
  <a href="#the-missing-first-step">Why</a> ·
  <a href="#what-it-does">What it does</a> ·
  <a href="#how-it-works">How it works</a> ·
  <a href="#see-it-live">Live example</a> ·
  <a href="#status">Status</a>
</p>

---

## The missing first step

Vibe coding is magic when you know what to build. But the hardest projects don't start
with a design — they start with **thirty open tabs and a head full of fragments**: a
half-idea from a paper, a counter-idea from a blog post, three approaches fighting each
other, and no way to tell which one deserves to win.

Prompting an agent to code from that state just launders the confusion into confident
syntax. What's missing is the step *before* the first prompt: reading the material,
letting your fragments collide, and settling them into a design — **without losing the
trail of why**.

**research-decision-support** is an [Agent Skill](https://agentskills.io) (Claude Code
plugin, works with any SKILL.md-compatible agent) that runs that step with you. It's
built for two moments:

- you want to build something new, but you have **fragments of ideas, not a mature design**;
- you have **too many ideas fighting** and need them laid out, linked, and settled.

## What it does

Three moves, one loop:

**1. Read faster, on a beautiful workbench.** Drop anything — papers, repos, blog posts,
a deep-research report. The agent files each source as a card, grades it (survey > paper >
docs > forum post), tags it, and anchors the claims to where they came from. A generated
HTML workbench turns the pile into something you can actually speed-read: one digest card
per source, filter, search, and tag *while you read*.

**2. Your fragments become idea cards — automatically recorded, visibly connected.** Say a
half-formed thought in conversation and it lands as a card. The agent links it to the
evidence that supports it, clusters neighbors, and surfaces conflicts (*these two ideas
can't both be true*) instead of quietly picking a side. Every card carries an append-only
log — where it was born, what changed it, what merged into it. Your thinking stops
evaporating between sessions.

**3. When you say go, the ideas assemble into a design.** One command turns the surviving
ideas into the output — a system design, an architecture doc, whatever your target
declares. From then on ideas and output stay in two-way sync: add an idea and the design
refreshes; edit the design and the agent calibrates the ideas underneath. Every element of
the design links back through the ideas to the sources that earned it. *Then* you vibe
code — from a design that can answer "why?" at every line.

### Who decides

You do. The founding rule is **人拍板、agent 跑腿** — the human adjudicates, the agent
does the legwork. The agent collects, grades, links, drafts, and keeps the ledger; it
never picks a winner. When sources disagree, it presents the contradiction. When ideas
fight, it lays them side by side. The design that comes out is *your* judgment, with
receipts — not an AI's confident guess.

## How it works

Three layers of plain Markdown in your repo, one canvas over them:

```
source ──▶ idea ◀──▶ output
(evidence:        (your judgment:      (the design:
 agent-filed,      only you create,     assembled on your go,
 graded,           auto-linked,         two-way synced,
 claim-anchored)   append-only logs)    every element traceable)
```

- **`sources/`** — agent territory. Everything you touch gets filed and graded
  automatically; you only verify at decision time.
- **`ideas/`** — yours. Only a human creates an idea card; the agent may draft and
  connect, never adjudicate. Two states only: it exists, or you archived it (archives
  keep their reasons — killed ideas defend you against relitigating them later).
- **`output/`** — the deliverable. Human-initiated, then it becomes the primary work
  surface; the agent keeps the ideas synchronized underneath.
- **The canvas** — a self-contained HTML projection of all of it: no server, no
  database, no dependencies, dark/light. It's a *projection*, never a store — the
  Markdown stays the single source of truth; the HTML is rebuilt on demand and thrown
  away.

Everything is versionable, greppable, and renders on GitHub. No lock-in: the protocol is
files + schema; the agent is just the runtime.

## See it live

[`examples/autoharness/`](examples/autoharness/index.md) is the unedited workspace from a
real project (agent-harness self-evolution research): **93 cards, 170 live links** — every
decision traceable back to the papers that justify it. Render it into the workbench in ten
seconds:

```bash
python3 archive/skill-v1/skill/scripts/build_site.py \
  examples/autoharness -o /tmp/workbench-demo --title autoharness
open /tmp/workbench-demo/index.html
```

It's not just for code projects — anything shaped "read materials → make a defensible
call" fits: vendor selection, due diligence, competitive analysis, literature review.

## Status

Being rebuilt in the open, and **dogfooded on itself** — this repo's own design was
produced by running the method on ~80 sources about decision-making methods
(Zettelkasten, ADR, GRADE evidence grading, set-based design, Shape Up…).

- **v1** (four-layer workspace + HTML workbench) shipped, then taught us the schema was
  wrong. It lives in [`archive/skill-v1/`](archive/skill-v1/) and still runs — the demo
  above uses it.
- **v2** (source → idea → output + canvas, this README) is the redesign now being built.
  The plugin will land here:

```
/plugin marketplace add tigerless-labs/research-decision-support
/plugin install research-decision-support@research-decision-support
```

Star/watch to catch the v2 release.

## FAQ

**Is this a note-taking app?** No — it's a method your coding agent executes, stored as
plain Markdown in your repo. No database, no server, no account.

**Why not just ask the agent to "design it for me"?** Because agents are great at
execution and bad at judgment, and a wrong design costs you the entire branch of code
built on it. Ten seconds of human adjudication at the fork beats ten thousand tokens down
the wrong path. This skill makes those ten seconds fast — and permanent.

**What happens to my rejected ideas?** They're archived with their reasons, not deleted.
Six months later, when someone asks "why didn't we do X?", you have the card.

## License

MIT — vendored renderers ([marked](https://github.com/markedjs/marked),
[DOMPurify](https://github.com/cure53/DOMPurify)) keep their original headers.
