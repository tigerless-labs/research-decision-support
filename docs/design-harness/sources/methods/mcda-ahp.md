---
tags: [structured-comparison]
---

# [Method] MCDA / AHP -- turning "which matters more" into mathematics

Multi-criteria decision analysis; AHP = Saaty (1970s). Backing: (3) a vast academic literature,
but AHP has a known flaw (the rank reversal controversy).

Core logic: decompose the goal into a criteria tree, derive weights from **pairwise comparisons**
between criteria (1-9 scale, eigenvector method with a consistency check), then score options per
criterion x weight and aggregate. Always finish with **sensitivity analysis**: does a small weight
adjustment flip the ranking -- if so, the conclusion is fragile.

Boundaries: heavy process, not for small game; the number of pairwise comparisons grows with the
square of the criteria count; rank reversal (adding an irrelevant option changes the existing
ranking) is a theory-level defect.

**Relation to this project**: not adopted wholesale -- take only the sensitivity analysis: "which
assumption flips the conclusion the moment it moves" is worth building into the panel; weight
computation and sensitivity checks go entirely to the agent.
