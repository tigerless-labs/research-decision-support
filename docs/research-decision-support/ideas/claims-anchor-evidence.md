---
id: claims-anchor-evidence
type: idea
tags: [证据]
---

# 主张必须锚定证据：无出处的断言不得入库，锚定由 agent 自动完成

系统里任何一条主张（面板格子、方向卡结论、决定卡理由）都必须结构性地指向具体证据
——出处卡 + 原文位置，点开可核验。做不到锚定的内容只有两条路：降级为随想池里的
待查项，或不入库。这不是写作规范而是**入库门禁**：validator 可检查、UI 可点穿。
配套分工是关键——锚定劳动（找出处、建链接、标把握度）全部归 agent，人只负责
说出主张和核验存疑的格子；把锚定成本压到零，门禁才不会重蹈"人工填表"的死路。

结构义务来自 [Toulmin](../sources/methods/toulmin.md)（claim 无 grounds 不成立）；
逐格带把握度来自 [EBM/GRADE](../sources/methods/ebm-grade.md) 的 SoF 表（效应量与
可信度永远成对出现）；反面证据是 SciSpace 式引文编造被 r/PhD 集体避雷——能溯源
即护城河（见 [EBM/GRADE](../sources/methods/ebm-grade.md) 与 [Toulmin](../sources/methods/toulmin.md)）；锚定劳动必须归
agent 的理由见 [IBIS 反面教材](../sources/methods/ibis-qoc.md)（Grudin 悖论）。

Builds on [judgment-provenance-wedge](judgment-provenance-wedge.md)——本卡是那个楔子
的执行机制：判断可溯源之所以成立，是因为每条主张在写入时就被锚死。门禁位置已收敛——锚定义务落在 output 上板的主张，入口零门槛。To be weighed in
[decisions/](index.md)：门禁的严格度（拒绝晋级 vs 标记警告）待裁决。
