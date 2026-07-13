---
tags: [bias-resistance]
---

# [Method] Hypothesis-Driven Development (HDD) -- single-entity full lifecycle and "rejection is worth as much"

Lean / continuous-delivery community practice. See the
[MinimumCD practice guide](https://migration.minimumcd.org/docs/migrate-to-cd/optimize/hypothesis-driven-development/).

Core logic: state each feature as a falsifiable hypothesis ("we believe [change] will produce
[outcome], because [reason]" -- without the because it is a wish, not a hypothesis), with one
record for the full lifecycle (a hypothesis register): proposed -> validated / invalidated /
inconclusive. The key stance: **invalidated is not failure** -- a team that never overturns a
hypothesis is not running real experiments; the earlier you falsify, the more you save.

Boundaries: hypothesis quality depends on SMART-statement discipline; handling inconclusive
results (extend / abandon / rerun) needs extra rules.

**Relation to this project**: the origin of the decision card's state machine (open -> decided
with three endings); "rejection is worth as much as adoption, and rejection leaves a trace" comes
straight from invalidated-is-learning. Hypothesis = idea and decision are different states of the
same entity, supporting "idea does not deserve its own noun".
