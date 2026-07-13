---
id: evidence-grading
type: idea
tags: [evidence]
---

# Evidence grading: sources are not equal-weighted; grades are auto-annotated by the agent and visible throughout

Evidence in the system is not treated as equal-weighted -- every piece of evidence receives a
grade on intake (default order: systematic review > paper > official docs > high-quality blog >
social post), the grade is visible on every panel cell, and at adjudication time "three posts"
versus "one review" is clear at a glance. Two companion disciplines: **the grading table is
configurable per persona/scenario** (for the researcher, reviews rank highest; for the video
creator, first-hand platform data > second-hand trend articles -- the grade order is a parameter
of the scenario skill, not a global constant); **grading is annotation, not filtering** --
low-grade evidence still enters the base (new directions often surface in posts first), its
weight is simply honest. Annotation labor belongs entirely to the agent; the human may overrule
individual items (the overrule itself leaves a trail).

The grading mechanism comes from [EBM/GRADE](../sources/methods/ebm-grade.md) (evidence pyramid
plus four certainty levels, medicine's standard for thirty years); "grade and conclusion appear
as a pair" comes from its SoF table convention; the same discipline is already applied to the
methods we ourselves collect (the tier-1 to tier-4 endorsement grading in the
[sources index](../sources/index.md)); for grading tables varying by scenario see the
evidence-source comparison column of [four persona scenarios](four-persona-scenarios.md).

Builds on [claims-anchor-evidence](claims-anchor-evidence.md) -- anchoring governs "which piece
of evidence this points to", grading governs "how much to trust it"; together they are the
evidence base's complete constitution (see [EBM/GRADE](../sources/methods/ebm-grade.md)). To be
weighed in [decisions/](index.md): the default grading table's exact order; the permission
boundary for manual overrules.
