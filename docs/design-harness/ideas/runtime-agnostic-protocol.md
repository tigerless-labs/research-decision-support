---
id: runtime-agnostic-protocol
type: idea
tags: [protocol]
---

# The protocol fits any agent product: the CLI is only the first host, not the form

The system's portable contract is **files and schema** -- the markdown source of truth, the
frontmatter contract, the validator, the canvas projection -- none of which depends on any
particular agent runtime. Any agent product that can read and write files and run
"triage / linking / anchoring / the final move" (CLI tools, IDE agents, chat products, homegrown
agents) can host this decision protocol; runtime differences collapse into one **thin adapter
layer** (skill / prompt / MCP / API wrapper), with the protocol body unchanged. Hosting on a
Claude Code skill today is a distribution starting point, not a product boundary -- bind to a
single runtime and the protocol's lifespan is capped by the host's.

This repository as it stands is the proof: the workspace contract (typed cards + validator +
site generation) is pure file operations, and the skill is only the carrier of the operating
procedure; agent-ecosystem carriers churn fast (skills / MCP / competing agent frameworks
coexist), and betting on a single carrier directly conflicts with the repo's
distribution-first positioning.

Builds on [one-engine-many-schemas](one-engine-many-schemas.md) -- that card swaps domains
horizontally (schema replaceable), this card swaps hosts vertically (runtime replaceable);
together they are two degrees of freedom of the same engine;
[drafts-not-state](drafts-not-state.md) (markdown as source of truth, no server) is the
technical precondition of portability; the division-of-labor constraint of
[agent-synthesizes-human-adjudicates](agent-synthesizes-human-adjudicates.md) is the invariant
every adapter must preserve -- switching hosts must not switch away "the human adjudicates". To
be weighed in [decisions/](../index.md): the adapter's minimal interface surface (which
operations the protocol requires).
