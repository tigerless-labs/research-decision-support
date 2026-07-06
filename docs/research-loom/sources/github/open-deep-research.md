# [GitHub] langchain-ai/open_deep_research（及 Deep Agents）— 工程化研究流水线

github.com/langchain-ai/open_deep_research · MIT · Deep Research Bench 第 6（RACE 0.4344）；
2026 年主力已转向 **Deep Agents** harness（~23k★），做长任务的规划/上下文管理/多 agent 编排。
同类：HuggingFace smolagents 的 open_deep_research 示例（code-action 极简版）、字节 DeerFlow、
DeepSearcher（~7k★）、Local Deep Research（本地隐私向，3k+★）。

核心逻辑：supervisor-researcher 架构——planner 出分节研究计划，各节并行"搜+写"，最后
合成报告；模型/搜索 API 全可换。

边界：整族的共同形态——**query in, report out**。中间产物（子问题、来源取舍）是运行时
状态，跑完即弃；报告不可追问、不可增量演化。

**与 loom 的关系**：证明"自动读写"已是红海（三家 20k+★），而"读后判断的沉淀"无人做——
loom 不与之竞争检索与成文，吃它们的输出当原料。来源：
[langchain repo](https://github.com/langchain-ai/open_deep_research)、
[smolagents 示例](https://github.com/huggingface/smolagents/tree/main/examples/open_deep_research)、
[Together 对比评测](https://www.together.ai/blog/open-deep-research)。
