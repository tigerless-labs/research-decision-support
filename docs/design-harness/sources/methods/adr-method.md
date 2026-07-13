---
tags: [decision-traceability]
---

# [Method] ADR -- the surviving specimen of decision records

Michael Nygard, "Documenting Architecture Decisions" (2011). Common practice across the software
industry. For the tool ecosystem see [adr-tools / log4brains](../github/adr-tooling.md).

Core logic: one decision, one record, structured as context -> decision -> **consequences** (write
down both good and bad -- declaring up front "we know the cost and accept it" defends against
relitigation-style review). State lifecycle: proposed -> accepted -> superseded; records are
immutable, and reversal happens by a new record superseding the old one. It is the **only
descendant of the 1990s design-rationale tools (the IBIS/QOC family) that survived into the
mainstream**, and it survived by being minimal: one page, no dedicated tooling, no ontology.

Boundaries: designed for engineering decisions; the options section only lists, it does not
generate; it relies on humans writing voluntarily, so coverage is a chronic problem.

**Relation to this project**: the origin of the decision card's structure (context/verdict/
reasons/costs, append-only, supersede, decided cards showing a three-line summary at the top =
ADR's collapse); "only the minimal survives" backs the minimal-architecture constraint. The
writing labor moves to the agent, curing the chronic coverage problem.
