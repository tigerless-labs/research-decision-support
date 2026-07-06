# [GitHub] stanford-oval/storm — 多视角提问的知识策展系统

github.com/stanford-oval/storm · ~27.6k★ · dspy 实现 · `pip install knowledge-storm` · 70k+ 人试用。

核心逻辑：两阶段写百科式长文——pre-writing（多视角提问 + 模拟"编辑×专家"对话做检索，
产 outline+references）→ writing（按 outline 成文带引用）。**Co-STORM** 变体维护一张动态
mind map（层级概念结构），号称与人共建概念空间、降低长对话认知负担。

边界：mind map 是**系统的**概念组织，不是**用户的**判断台账；产物仍是文章草稿（官方自述
"到 pre-writing 为止有用，成文需大改"），不通向设计/决策。

**与 loom 的关系**：所有 auto research agent 里离 loom 最近的形态（有结构化中间层），但
中间层不可版本化、不承载"我的评判"。来源：[repo](https://github.com/stanford-oval/storm)。
