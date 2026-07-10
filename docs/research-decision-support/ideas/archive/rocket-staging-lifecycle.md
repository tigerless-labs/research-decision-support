---
id: rocket-staging-lifecycle
type: idea
tags: [同步]
---

# 火箭分级生命周期：系统只有一个操作——点火

每次 output 改动＝一次**重新点火**；点火即自动分离：装配完成后当前全部 ideas
归档（`ideas/archive/`），其判断与引用被 output **整理并继承**，此后不再热
重载——[双向同步](../output-primary-after-generation.md)与
[热刷新](../output-auto-refresh.md)被本卡 supersede。点火有 output 则更新（装配
输入＝当前 output + target + 工作面新 ideas，可为零卡——纯格式调整登记进
target 即可），无则创建。**完整性义务**：每张存在态卡要么被继承、要么由人显式
弃档，agent 不得静默丢弃，点火回执报告未继承项与薄弱点（不阻塞）。**留痕**：
logs 记点火行（轮次、归档卡清单、每卡→output 元素的继承映射），output 锚反向
点穿。sources 常驻不归档（撤稿走降级）；复议＝开新 ideas 走新点火，归档卡永不
解冻。使命边界：推动 output 产生，交付即止——与编程流程分离，code agent 不
引用本 workspace 设计。

自动归档的合理性：归档非破坏、纠错便宜（读归档→新卡→再点火），乐观提交模式。
证据面压倒性支撑分离：[ADR](../../sources/methods/adr-method.md) accepted 即不可变、
[决策日志](../../sources/methods/decision-journal.md) 封存防事后美化、
[Shape Up](../../sources/methods/shape-up.md) ship 后 pitch 不复活、
[GTD](../../sources/methods/gtd.md) 工作面必清空、
[Zettelkasten](../../sources/methods/zettelkasten.md) 转瞬笔记用完即弃、
[HDD](../../sources/methods/hdd.md) 假设闭环即 close；
[EBM living review](../../sources/methods/ebm-grade.md) 的更新实质也是重新点火；
[IBIS](../../sources/methods/ibis-qoc.md) 反证活中间层死于维护成本。
