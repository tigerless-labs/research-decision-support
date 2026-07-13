# [GitHub] adr-tools / log4brains -- the ADR tool family and the "decision disconnect" pain point

github.com/npryce/adr-tools (bash CLI, the de facto standard) · github.com/thomvaill/log4brains
(Node, static-site publishing) · adr.github.io (spec hub).

Core logic: template scaffolding + numbering + a supersede state machine; log4brains holds that an
ADR is immutable (only its status changes) -- "a document never expires -- it was at least true
some day". Convention stores them in `docs/adr/`, same repo and version as the code.

Pain point (2026 framing, the Catio guide): the tools stop at the template/CLI layer, and **nobody
solves the disconnect (drift) between decisions and the living system**; DevOps.com: "decisions,
pitfalls, and the why are the hardest to get into docs". Neither flagship tool has agent
involvement or any notion of an evidence chain (decision <- evidence).

**Relevance to this project**: the mindset of this project's decisions layer (drivers x options x
trade-offs, append-only, affects anchoring), taken on its own, is exactly the open slot for an
agent-native decision-log skill. Sources:
[Catio 2026 guide](https://www.catio.tech/blog/architecture-decision-record),
[log4brains](https://github.com/thomvaill/log4brains),
[DevOps.com](https://devops.com/documentation-is-dead-long-live-documentation/).
