---
id: idea-layer-single-entity
type: idea
tags: [schema]
---

# ADR：idea 层单实体原地迭代，否决 GTD 式双层

**裁决**（2026-07-08；状态机细分已被 2026-07-09 生命周期简化 supersede，现为
存在/归档二态）：idea 层不分"缓存 + 清理后"两层——单实体，原地迭代；append-only
log 承担全部留痕。**原地迭代含自动合并**（2026-07-09）：人提出的新 idea 若与
既有卡是同一判断（重复或增量），agent 自动并入旧卡、log 记合并，不开二卡；
**冲突不算可合并**——新旧主张相抵时必须如实上板呈现分歧，由人裁决。

**理由**：存活方法的共性是单实体多状态（ADR / Issue / Kanban / Shape Up /
Zettelkasten，GTD 的 inbox 也是状态不是实体），多实体模型死于捕获成本（IBIS，
Grudin 悖论，见 [IBIS 反面教材](../sources/methods/ibis-qoc.md)）；双层给每条 idea
加一次搬运动作，违背"结构尽可能简单、约束尽可能少"的产品理念。

**保留义务**（层砍掉、行为不砍）：出生零门槛——
[buffer-captures-anything](buffer-captures-anything.md) 的捕获行为收敛为
存在态；允许蒸发——归档留 log 不删除；
[claims-anchor-evidence](claims-anchor-evidence.md) 的锚定义务落在 output
上板的主张，不再有晋级门禁。
