---
tags: [对抗偏误]
---

# [方法] 假设驱动开发 HDD — 单实体全生命周期与"否决同价"

精益/持续交付社区实践 · 参考 [MinimumCD 实践指南](https://migration.minimumcd.org/docs/migrate-to-cd/optimize/hypothesis-driven-development/)。

核心逻辑：把功能表述为可证伪假设（"我们相信 [改动] 会带来 [结果]，因为 [理由]"——没有
because 就是愿望不是假设），全生命周期一条记录（hypothesis register）：proposed →
validated / invalidated / inconclusive。关键姿态：**invalidated 不是失败**——从不推翻
假设的团队没有在做真实验；越早证伪省得越多。

边界：假设质量依赖 SMART 表述纪律；inconclusive 的处置（延长/放弃/重跑）需要额外规则。

**与本项目的关系**：决定卡状态机的出身（open → decided 三种结局）；"否决与采纳同价、
否决留痕"直接来自 invalidated-is-learning。假设=想法与决定是同一实体的不同状态，
支撑"idea 不配独立名词"。
