# [博客] Agentic Code Review — "missing intent" 与 review 崩塌的量化

Addy Osmani（2026）+ *AI Slop and the Software Commons* 论文（1154 帖分析）+
Faros AI 实测（22k 开发者 / 4k 团队，2026-03）。

核心逻辑：审 agent PR 的人是"**第一个看到这段代码的人类**"——正常 review 里作者已理解
过改动，reviewer 只是复核；agent PR 里没人重建过 why，"review wasn't built to recover
missing intent"。关键：**agent 的推理存在过但被丢弃**——论文明说解法是把"想做什么、
排除了什么"作为 decision log 附在 PR 上，"this is a tooling problem, and tooling
problems get solved"。Faros 数据：review 时长中位数 +441.5%、churn +861%、零 review
合并 +31.3%、人均缺陷率 9%→54%——决策密度爆炸，记录与复核能力没变。

**与 loom 的关系**：decision-log skill 的最强时代论据——agent 时代"why 蒸发"从慢性病
变急性病，且解法方向（决策日志）已被独立指出但无人做成 agent-native 工具。来源：
[Agentic Code Review](https://addyosmani.com/blog/agentic-code-review/)、
[Pragmatic Engineer 2026](https://newsletter.pragmaticengineer.com/p/ai-impact-on-software-engineers-part-2)、
[Stack Overflow: decision fatigue](https://stackoverflow.blog/2026/05/21/coding-agents-are-giving-everyone-decision-fatigue/)。
