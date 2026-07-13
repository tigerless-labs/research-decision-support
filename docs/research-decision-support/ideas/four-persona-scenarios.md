---
id: four-persona-scenarios
type: idea
tags: [positioning]
---

# Persona scenarios: the same decision protocol, different evidence sources and adjudication artifacts

"Research-based decisions" are not researcher-only -- every persona runs the same protocol
(gather evidence, lay out options, the human adjudicates, leave a trail); the differences are
only in evidence sources and adjudication artifacts. These are exactly the two axes the thin
schema should parameterize:

| Persona | Typical decisions | Evidence sources | Adjudication artifact (what the decision card looks like) |
|---|---|---|---|
| **Researcher** | choosing a direction, picking methods, taking sides on disputes | papers, datasets, benchmarks, peer review | direction comparison matrix -> ADR, citation-level provenance |
| **Software developer** | technology selection, architecture trade-offs, adding dependencies | repos, docs, benchmarks, issue threads | drivers x options -> ADR, affects anchored to modules |
| **Vibe coder** | product direction, design intent, feature trade-offs | competitor experience, user feedback, demo runs | design canvas elements <- endorsed by decision cards (see creation-canvas's downstream extension) |
| **Video creator** | topic selection, title/thumbnail, narrative structure | platform data, comment sections, competing channels, trend tools | topic adjudication card: hypothesis (HDD-style) -> publish as experiment -> data backfill review |
| **Life decision-maker** | changing jobs, choosing schools, buying a home, picking a city | real offer/school/listing data, first-person experience posts, policy documents, advice from family and friends | PrOACT-style decision card: objectives (drivers) x options x consequences + accepted trade-offs; mostly one-shot, high-stakes, irreversible -> full protocol |

The commonality validates the protocol's generality; the differences carve out each scenario
skill: evidence grading tables differ (researcher: reviews > papers; video creator: first-hand
platform data > second-hand trend articles; life decision-maker: first-hand hard data and
first-person experience posts > marketing content -- agent/admissions/employer talk is an
inherent conflict-of-interest source and must be graded down), adjudication cadence differs (the
video creator runs a high-frequency OODA loop, the researcher a low-frequency deliberation
table; the life decision-maker decides least often with the highest stakes per decision, mostly
one-way doors -- irreversible, exactly the persona for whom the full protocol pays off most),
but "vetoes leave a trail, decisions are traceable" wins across the board -- "why we didn't buy
that apartment" is worth as much as "why we didn't use that framework", and the life
decision-maker gains one extra benefit of their own: the decision log defends against
after-the-fact self-blame and family second-guessing.

All four competitor clusters serve only the researcher persona (see the competitors group in the
[sources index](../sources/index.md)); the decision-traceability market for the other personas
is empty. The life-decision scenario has independent corroboration -- the PrOACT original,
Smart Choices (see [PrOACT](../sources/methods/proact.md)), uses job-change and home-purchase
level choices as its examples; the [sources index](../sources/index.md) shows the underlying
methods (GTD/ACH/ADR/Shape Up...) were themselves born in different industries -- crossing
personas is native to the methods.

Builds on [one-engine-many-schemas](one-engine-many-schemas.md) (persona = a parameterized
dimension of the schema); the vibe coder persona's adjudication artifact is the creation
canvas's downstream extension; the selection basis for the scenario skills repo. To be weighed
in [decisions/](index.md): which persona ships first.
