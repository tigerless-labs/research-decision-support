---
tags: [methodology-repository]
---

# [GitHub] github/spec-kit -- the ceiling for methodology repositories (~111k stars)

github.com/github/spec-kit · released 2025-09, reached 111k stars by 2026-06 (one of the year's
fastest-growing dev tools) · MIT.

Core logic: Spec-Driven Development -- **each stage produces one markdown file that feeds the
next**: Spec -> Plan -> Tasks -> Implement, plus `constitution.md` (the project's immutable
principles). The form = the Specify CLI (`specify init` one-command bootstrap) + templates + slash
commands (/speckit.specify ...). **Supports 30+ agents** (Copilot/Claude Code/Cursor/Gemini...),
later adding extensions/presets/bundles (a role configured in one step). Criticism (Martin
Fowler's site): the markdown is verbose and repetitive, and agents don't always follow the
templates.

How it caught fire: official GitHub backing + **inventing and naming a category** (SDD, spawning
ecosystem articles like "15 SDD frameworks compared") + single-command install + agent-agnostic.

**Relevance to this project**: structurally isomorphic (a layered chain of markdown artifacts) but
covering a different segment -- spec-kit assumes you already know what to build; this project
handles the upstream "read material -> form judgments -> set direction". Composable: the decisions
layer's ADRs feed constitution.md. Sources: [repo](https://github.com/github/spec-kit),
[GitHub blog](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/),
[commentary on Fowler's site](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html).
