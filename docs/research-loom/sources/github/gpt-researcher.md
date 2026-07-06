# [GitHub] assafelovic/gpt-researcher — 自动深度研究 agent 的头牌

github.com/assafelovic/gpt-researcher · ~28k★（2025-12 口径）· MIT · 另有 gptr-mcp 供 Claude 等调用。

核心逻辑：planner 把问题拆成子问题 → 并发 executor 爬取并摘要来源 → publisher 聚合成带
引用的结构化报告；可选 LangGraph 多 agent 编排（chief editor / researcher / reviewer /
writer / publisher）。CMU DeepResearchGym（2025-05，1000 复杂查询）上引用质量/报告质量/
覆盖率均第一，压过 Perplexity 与 OpenAI。

边界：**输出是一次性 prose 报告**。研究过程（谁被采信、为什么）压缩进最终文本；用户判断
不是对象，报告交付即终点，不versioned、不可回问。

**与 loom 的关系**：上游入料口——它产的报告与引用可拆成 sources 卡；loom 接管它停下的
地方（判断→设计）。来源：[repo](https://github.com/assafelovic/gpt-researcher)、
[SkillsLLM 快照](https://skillsllm.com/skill/gpt-researcher)。
