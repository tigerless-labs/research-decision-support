---
tags: [auto-research]
---

# [GitHub] assafelovic/gpt-researcher -- the flagship automated deep-research agent

github.com/assafelovic/gpt-researcher · ~28k stars (as of 2025-12) · MIT · a gptr-mcp companion
lets Claude and others call it.

Core logic: a planner splits the question into sub-questions -> concurrent executors crawl and
summarize sources -> a publisher aggregates them into a structured, cited report; optional
LangGraph multi-agent orchestration (chief editor / researcher / reviewer / writer / publisher).
Ranked first on citation quality / report quality / coverage in CMU DeepResearchGym (2025-05,
1000 complex queries), beating Perplexity and OpenAI.

Boundary: **the output is a one-shot prose report**. The research process (who was trusted, and
why) is compressed into the final text; the user's judgment is not an object, and delivering the
report is the endpoint -- not versioned, not re-queryable.

**Relevance to this project**: an upstream intake -- the reports and citations it produces can be
split into sources cards; this project takes over where it stops (judgment -> design). Sources:
[repo](https://github.com/assafelovic/gpt-researcher),
[SkillsLLM snapshot](https://skillsllm.com/skill/gpt-researcher).
