---
id: protocol-discoverability-in-situ
type: idea
tags: [protocol]
---

# The protocol teaches in situ: empty states + timely hints + action receipts, no manual

Discoverability of the protocol rules (output must be human-initiated, accumulate ideas first,
two-way sync) relies not on onboarding docs but on the system's own surfaces teaching **at the
right moments**:

- **The empty state teaches who initiates**: the canvas's output cluster keeps a permanent
  dashed placeholder ("output not yet generated - just say 'generate output'"); when the ideas
  show signals of mature clustering, the agent proactively offers "ready to assemble -- want me
  to generate?" -- the timing of the hint belongs to the agent, the button stays in the human's
  hand.
- **Honest presentation teaches accumulation, with no gate**: when the human asks for output too
  early, do not refuse; the agent reports the state ("only N idea cards, M of them unanchored --
  the assembly will be thin. Generate anyway?"), the consequence of thinness is put on the
  table, and the human adjudicates; the canvas's left-to-right layout of source -> idea ->
  output is itself the process order.
- **Receipts teach sync**: on first output generation, explain once that "from now on, whichever
  side you edit, I sync the other"; after that, every sync gets a one-line receipt (which layer,
  which spots, how many log lines), and the nodes on the passively updated side flash on the
  canvas.

The three are isomorphic: a rule becomes visible **at the moment it takes effect, on the surface
where it takes effect**, in keeping with the fool-proof constraint; hinting belongs to the
agent, deciding belongs to the human.

Empty states and just-in-time hints are mature interaction conventions (no separate source card;
noted as common knowledge for now); for the division of labor see
[agent thinks, does not adjudicate](agent-synthesizes-human-adjudicates.md).

The three rules being taught come from
[output-primary-after-generation](output-primary-after-generation.md); the carriers of the
empty state and the flashing depend on the [creation canvas](creation-canvas.md) /
[single canvas, three clusters](archive/single-canvas-clustered-graph.md); receipts correspond
to the one-line-per-layer entries of the ledger, [logs.md](../logs.md).
