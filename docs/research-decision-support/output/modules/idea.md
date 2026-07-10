# idea 决定模块

**职责**：判断的唯一居所——无 output 时是主工作面；output 生成后转为决策记录
（溯源链、被否掉的路、多 output 复用的判断本体）。

**行为边界**：

- **只有人能创建 idea**（agent 可整合碎片观点成草案建议，落卡须人）。
- 状态只有两个：**存在 / 归档**——存在即在场并参与装配，没有锚定/拍板/采纳
  流程，也无任何状态标签。
- 归档人与 agent 均可触发，卡移入 `ideas/archive/` 子目录，log 留痕不删除。
- 新 idea 与既有卡同判断（重复/增量）时 agent **自动合并**进旧卡、log 记账；
  冲突不算可合并，分歧如实上板由人裁决。
- 与 output **永远双向同步**：人提 idea 同回合双写两层，人改 output 由 agent
  反向校准回本层（代笔誊写，判断仍属人）。
- 每节点带 append-only log（诞生/更新/合并/supersede，待建）；层级账本
  [logs.md](../../logs.md) 记录所有卡的变更（含正文更新）——节点级 log 落地前，
  它是 idea 改动的唯一留痕。

**溯源**：[output 为主](../../ideas/output-primary-after-generation.md) ·
[单实体 ADR](../../ideas/idea-layer-single-entity.md)（其状态机细分已简化为二态，
见 logs 2026-07-09） ·
[agent 思考不拍板](../../ideas/agent-synthesizes-human-adjudicates.md) ·
[缓冲捕获](../../ideas/buffer-captures-anything.md)。
