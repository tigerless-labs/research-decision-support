---
tags: [决策留痕]
---

# [方法] ADR — 决策记录的存活标本

Michael Nygard "Documenting Architecture Decisions" (2011) · 软件业普遍实践 ·
工具生态见 [adr-tools / log4brains](../github/adr-tooling.md)。

核心逻辑：一条决策一份记录，结构 context → decision → **consequences**（后果：好坏
都写——提前声明"我们知道代价并接受它"，防翻案式重审）。状态生命周期 proposed →
accepted → superseded；记录不可变，推翻靠新记录 supersede 旧记录。它是 90 年代设计
论证工具（IBIS/QOC 一族）**唯一活到主流的后裔**，活因是极简：一页纸、无专用工具、
无本体论。

边界：为工程决策设计；options 一节只列不管生成；靠人自觉书写，覆盖率是老大难。

**与本项目的关系**：决定卡结构的出身（context/verdict/理由/代价、append-only、
supersede、已决卡顶三行 summary=ADR 的 collapse）；"极简才存活"支撑架构极简约束。
书写劳动移交 agent，治覆盖率痼疾。
