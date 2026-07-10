---
id: output-auto-refresh
type: idea
tags: [同步]
---

# output 随 idea 自动刷新：装配产物永不滞后于判断

第三模块由 design 更名为 **output**——存在态 idea 的装配产物，形态不限（当前的
output 就是系统设计）。配套一条自动化纪律：**每次 idea 层变更（新增/更新/归档/
合并/supersede），agent 在同一回合重推 output 受影响的元素**——判断变了，装配它的
产物立即跟着变，不留"文档说 A、判断已是 B"的窗口。刷新是重derive不是重写全文：
只动链到被变更 idea 的元素，其余不碰。这是"文档腐烂"的结构性解法——腐烂的根因是
更新劳动无人认领，把它显式判给 agent 且钉在 idea 变更这个触发点上，产物就不可能
陈旧。

滚动更新的先例是 [EBM/GRADE](../sources/methods/ebm-grade.md) 的 living review
（新证据出现即重估结论）；"需要人工维护的库存必然腐烂"见
[IBIS 反面教材](../sources/methods/ibis-qoc.md)（Grudin 悖论——更新劳动必须归 agent）；
投影必须可再生的前提见 [drafts-not-state](drafts-not-state.md)。

与[创作画板](creation-canvas.md)的"向下承接决策成设计"同一条流水线。本规则只
刷新**已存在**的 output，首次生成由人启动。待权衡：刷新的粒度（元素级 vs 全文
重推）与失败时的降级行为。
