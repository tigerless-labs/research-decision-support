---
id: creation-canvas
type: idea
tags: [画板]
---

# 创作画板：零散 idea 实时上板自动连线，人在板上提炼成最终决策

比"决策模型"更贴合本项目的形态是一块**创作画板**：从参考资料读出的和自己冒出的零散
idea 逐条上板，每新增一条实时显示为节点并与已有节点自动连线——关联由 agent 从内容
推导，人不手动拉线。人面对一张随输入生长的图，在板上组合、合并、裁剪，把散点提炼成
最终决策。主战场是**帮人理清思路**，胜负手是 UI+AI 的直观、好看、清晰；画板是
markdown 真身的实时投影，不是新的事实存放处。

每个节点自带 **logs**：idea 的诞生来源、每次更新的内容与原因、被合并/裁剪的过程，
append-only 追加，板上点开可读——图回答"现在长什么样"，logs 回答"怎么长成这样的"。

原 vibe-code design 画板（设计意图落点、接决定卡下游）收编为本卡的下游延伸：同一块
板，向上综合 idea 成决策，向下承接决策成设计。

Obsidian 生态勘察（2026-07）：自动连线已商品化——[InfraNodus](../sources/products/infranodus.md)
自动成图+空隙识别，Smart Connections / Auto Linker 等做语义与标题级自动建链——但全部
停在"关联发现"，无一产出决策；空位正是连线之后的下半程。vibe-code 延伸的原有证据
（spec-kit / BMAD 验证品类、[tribal knowledge](../sources/blogs/tribal-knowledge-why.md)
证明 why 先蒸发）继续成立。

Builds on [judgment-provenance-wedge](judgment-provenance-wedge.md)（画板是判断→决策的
可视化现场，节点 logs 即溯源的 UI 化）、[read-tag-judge-loop](read-tag-judge-loop.md)
（读中落下的判断即上板素材）、[drafts-not-state](drafts-not-state.md)（板是投影，
markdown 是真身）、[one-engine-many-schemas](one-engine-many-schemas.md)（画板是引擎的
视图层，schema 换域即换板）；[buffer-captures-anything](buffer-captures-anything.md)
的分诊产物是上板入口。To be weighed in [decisions/](../index.md)：画板与决定卡的产出衔接、
自动连线的推导口径。
