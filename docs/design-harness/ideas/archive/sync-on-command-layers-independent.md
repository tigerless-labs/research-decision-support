---
id: sync-on-command-layers-independent
type: idea
tags: [sync]
---

# Ideas and output are independent — sync is a human command, not an invariant

Adjudicated 2026-07-14, superseding the automatic two-way sync invariant:

- **ideas diverge, output converges.** Ideas accumulate freely and may contradict; output is the
  converged artifact and changes only on the human's word. Divergence between the layers is
  information (what has not yet been adjudicated into the design), not an error to eliminate.
- **idea → output re-derivation runs only when the human commands a sync.** The agent applies
  directly and gives a receipt; for large changes it presents a diff first.
- **back-transcription stays automatic**: a human edit to output is already an adjudication —
  transcribing it into ideas is pure legwork and keeps the judgment-provenance chain unbroken.
- **drift hints at the agent's discretion** ("output lags N ideas"), never nagging.
- With no automatic sync, conflicts surface only at sync moments with the human present — the
  automatic "output wins" rule retires.

Supersedes [output auto-refreshes with ideas](output-auto-refresh.md) (archived on the
human's call) and the permanent two-way half of
[output is primary](../output-primary-after-generation.md) (slimmed in place).
