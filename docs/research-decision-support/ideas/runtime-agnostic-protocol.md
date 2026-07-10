---
id: runtime-agnostic-protocol
type: idea
tags: [协议]
---

# 协议适配任何 agent 产品：CLI 只是第一个宿主，不是形态

系统的可移植契约是**文件与 schema**——markdown 真身、frontmatter 契约、校验器、
画板投影，全部不依赖任何特定 agent 运行时。凡是能读写文件、跑得动"分诊/连线/锚定/
临门动作"的 agent 产品（CLI 工具、IDE agent、聊天产品、自建 agent）都能承载这套
决策协议；各运行时的差异收敛为一层**薄适配器**（skill / prompt / MCP / API 封装），
协议本体零改动。当前以 Claude Code skill 为宿主只是分发起点，不是产品边界——
绑死单一运行时，协议的生命周期就被宿主的生命周期封顶。

本仓库现状即证明：工作区契约（typed cards + 校验器 + 站点生成）是纯文件操作，
skill 只是操作规程的搬运层；agent 生态载体快速更替（skill / MCP / 各家 agent 框架
并存竞争），押注单一载体与仓库"分发为先"的定位直接冲突。

Builds on [one-engine-many-schemas](one-engine-many-schemas.md)——那张卡横向换域
（schema 可替换），本卡纵向换宿主（运行时可替换），合起来是同一个引擎的两个自由度；
[drafts-not-state](drafts-not-state.md)（markdown 真身、无服务端）是可移植性的
技术前提；[agent-synthesizes-human-adjudicates](agent-synthesizes-human-adjudicates.md)
的分工约束是适配器必须保全的不变量——换宿主不能换掉"人拍板"。To be weighed in
[decisions/](../index.md)：适配器的最小接口面（哪些操作是协议必需）。
