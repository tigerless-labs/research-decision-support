---
tags: [structured-comparison]
---

# [Method] Decision tree / expected value -- probability x payoff, rolled back to the best path

Decision analysis classic (Raiffa et al., 1960s). A cornerstone of the decision analysis
discipline. Backing: (2) discipline-level long-term testing (mathematically sound; effectiveness
depends on the quality of probability estimates).

Core logic: draw a tree alternating decision nodes (squares) and chance nodes (circles), label
chance branches with probabilities and leaves with outcome values, then roll expectations back
from leaves to root (weight at chance nodes, take the best at decision nodes). Finish with a
sensitivity check: how much must a key probability wobble before the conclusion flips.

Boundaries: only works when probabilities can be reasonably estimated -- under deep uncertainty
(no distribution to speak of) it yields false precision; the applicability of expected value to
one-shot major decisions is contested (no repetition means no "expectation").

**Relation to this project**: a candidate view for multi-stage decisions; expectation rollback and
sensitivity checks go entirely to the agent, probability and value judgments go to the human.
