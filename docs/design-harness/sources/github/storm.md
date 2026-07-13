---
tags: [auto-research]
---

# [GitHub] stanford-oval/storm -- knowledge curation through multi-perspective questioning

github.com/stanford-oval/storm · ~27.6k stars · implemented on dspy ·
`pip install knowledge-storm` · tried by 70k+ people.

Core logic: two-stage encyclopedia-style long-form writing -- pre-writing (multi-perspective
questioning + simulated "editor x expert" dialogues driving retrieval, producing
outline+references) -> writing (composing cited text from the outline). The **Co-STORM** variant
maintains a dynamic mind map (a hierarchical concept structure), claiming to co-build the concept
space with the human and lower the cognitive load of long conversations.

Boundary: the mind map is **the system's** concept organization, not **the user's** ledger of
judgments; the artifact is still an article draft (the official line: "useful up to pre-writing;
the text needs heavy rework"), and it does not lead to design/decisions.

**Relevance to this project**: of all auto-research agents, the form closest to this project (it
has a structured intermediate layer), but that layer is not versionable and does not carry "my
verdicts". Source: [repo](https://github.com/stanford-oval/storm).
