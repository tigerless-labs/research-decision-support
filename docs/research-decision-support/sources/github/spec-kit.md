---
tags: [方法论仓库]
---

# [GitHub] github/spec-kit — 方法论仓库的天花板（~111k★）

github.com/github/spec-kit · 2025-09 发布，2026-06 达 111k★（当年增长最快 dev 工具之一）· MIT。

核心逻辑：Spec-Driven Development——**每个阶段产一份 markdown 喂下一阶段**：
Spec → Plan → Tasks → Implement，配 `constitution.md`（项目不可变原则）。形态 =
Specify CLI（`specify init` 一键 bootstrap）+ 模板 + slash commands（/speckit.specify …）。
**支持 30+ agent**（Copilot/Claude Code/Cursor/Gemini…），后期加 extensions/presets/
bundles（角色一键配齐）。批评（Martin Fowler 站）：markdown 冗长重复、agent 并不总守模板。

做火的手法：GitHub 官方背书 + **发明并命名一个品类**（SDD，衍生出"15 个 SDD 框架对比"
这种生态文章）+ 单命令安装 + agent-agnostic。

**与本项目的关系**：结构同构（分层 markdown 产物链），但覆盖段不同——spec-kit 假设你
已知道要建什么；本项目管它上游的"读材料→形成判断→定方向"。可组合：decisions 层的
ADR 喂给 constitution.md。来源：[repo](https://github.com/github/spec-kit)、
[GitHub blog](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)、
[Fowler 站评述](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html)。
