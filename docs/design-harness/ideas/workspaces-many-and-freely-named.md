---
id: workspaces-many-and-freely-named
type: idea
tags: [skill]
---

# Many workspaces, freely named — the config pointer is the registry

The human's judgment (2026-07-14): a host project may hold **more than one workspace**, and the
workspace directory is **not required to be named `design-harness`** — any name is legal. The one
requirement is that every workspace is recorded in the host-root config pointer
(`.design-harness/config.json`); discovery trusts the registry, not the directory name.
