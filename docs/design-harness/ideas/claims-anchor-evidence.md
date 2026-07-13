---
id: claims-anchor-evidence
type: idea
tags: [evidence]
---

# Claims must anchor evidence: unsourced assertions stay out of the base, and anchoring is done automatically by the agent

Every claim in the system (a panel cell, a direction card's conclusion, a decision card's
rationale) must structurally point at concrete evidence -- a source card plus the original
passage, verifiable on click. Content that cannot be anchored has only two paths: demote to a
to-verify item in the scratch pool, or stay out of the base. This is not a writing convention but
an **intake gate**: validators can check it, the UI can click through it. The paired division of
labor is the key -- anchoring labor (finding sources, building links, marking confidence) belongs
entirely to the agent; the human only states claims and verifies doubtful cells. Only by driving
the cost of anchoring to zero does the gate avoid repeating the dead end of "humans filling out
forms".

The structural obligation comes from [Toulmin](../sources/methods/toulmin.md) (a claim without
grounds does not stand); per-cell confidence comes from the SoF tables of
[EBM/GRADE](../sources/methods/ebm-grade.md) (effect size and certainty always appear as a pair);
the negative evidence is SciSpace-style citation fabrication being collectively blacklisted on
r/PhD -- traceability is the moat (see [EBM/GRADE](../sources/methods/ebm-grade.md) and
[Toulmin](../sources/methods/toulmin.md)); for why anchoring labor must belong to the agent see
the [IBIS cautionary tale](../sources/methods/ibis-qoc.md) (Grudin's paradox).

Builds on [judgment-provenance-wedge](judgment-provenance-wedge.md) -- this card is that wedge's
enforcement mechanism: judgments are traceable precisely because every claim is anchored at write
time. The gate's position has converged -- the anchoring obligation falls on claims put on the
board in output, and the entry stays zero-threshold. To be weighed in [decisions/](index.md):
the gate's strictness (refuse promotion vs flag a warning).
