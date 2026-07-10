# protocol 协议与账本

**职责**：系统的可移植内核——文件布局、卡片 schema、校验规则、变更账本。

**行为边界**：

- markdown 是唯一真身，一切界面皆投影且永不入库。
- 投影同步纪律：真身改动同回合重建投影，顺序恒为先 markdown 后 HTML，禁止只改
  HTML。
- frontmatter 承载 schema（校验器强制执行）；卡的结构＝frontmatter + **标题 +
  摘要**，无固定段落，引用内联在摘要中。
- 结构化事实只有两种：**引用**（唯一关联，卡内正文的链接，**只准向前**——指向
  本卡赖以成立的证据与先行卡，"谁引用了我"由投影派生 backlink 不落笔）与
  **tag**（唯一分类：单层、一卡至多一个、可选，无目录树）。
- 距离/坐标是投影派生量，不入真身。
- 各层 index 也是派生投影：以 tag 为小标题分组（`TAG：一句为何一类`），未分类
  卡平铺末尾，agent 随卡变更同回合重生成，检索走 index 不设分类层。
- [logs.md](../../logs.md) 为覆盖 ideas 与 output 两层的 append-only 变更账本，
  每行记录**改动本身**（旧→新的最小 delta）而不只动作与原因——docs 不入 git，
  账本是回溯的唯一依据。
- 协议不绑运行时：绑定契约而非宿主，CLI 是第一宿主而非形态本身；同一引擎可配
  多份薄 schema 服务不同人格场景。

**溯源**：账本纪律锚 [ADR](../../sources/methods/adr-method.md)（append-only+supersede，
"不可变、只变状态"）与[决策日志](../../sources/methods/decision-journal.md)
（记当时预期防事后美化，①级实证） ·
[引用+tag 两种事实](../../ideas/single-edge-single-tag.md) ·
[tag 上 index](../../ideas/tags-in-layer-index.md) ·
[协议不绑运行时](../../ideas/runtime-agnostic-protocol.md) ·
[一引擎多 schema](../../ideas/one-engine-many-schemas.md) ·
[人格场景](../../ideas/four-persona-scenarios.md)。
