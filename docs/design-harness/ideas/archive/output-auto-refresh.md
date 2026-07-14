---
id: output-auto-refresh
type: idea
tags: [sync]
---

# Output auto-refreshes with ideas: the assembled product never lags behind judgments

The third module is renamed from design to **output** -- the assembly product of exist-state
ideas, unrestricted in form (the current output is the system design). It comes with one
automation discipline: **on every idea-layer change (create / update / archive / merge /
supersede), the agent re-derives the affected output elements in the same turn** -- when a
judgment changes, the product assembled from it changes immediately, leaving no window where
"the doc says A while the judgment is already B". A refresh is re-derivation, not a full
rewrite: only elements linked to the changed idea are touched, the rest stay put. This is the
structural cure for "document rot" -- rot's root cause is update labor nobody owns; assign it
explicitly to the agent and pin it to the idea-change trigger, and the product cannot go stale.

The precedent for rolling updates is the living review of
[EBM/GRADE](../../sources/methods/ebm-grade.md) (re-assess conclusions as new evidence appears);
"any inventory needing manual upkeep will rot" is the
[IBIS cautionary tale](../../sources/methods/ibis-qoc.md) (Grudin's paradox -- update labor must
belong to the agent); the premise that projections must be regenerable is
[drafts-not-state](../drafts-not-state.md).

Same pipeline as the [creation canvas](../creation-canvas.md)'s "carrying decisions downward into
design". This rule refreshes only **existing** output; first generation is initiated by the
human. To be weighed: refresh granularity (element-level vs full re-derivation) and the
degradation behavior on failure.
