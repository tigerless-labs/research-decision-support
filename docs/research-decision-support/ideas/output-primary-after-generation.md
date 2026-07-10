---
id: output-primary-after-generation
type: idea
tags: [同步]
---

# output 由人启动；生成后 ideas 与 output 永远同步（双向）

output 的装配**由人启动**，不再由 idea 变更自动触发首次生成。核心不变量：
**ideas 与 output 永不失同步**——人从哪一面改，agent 都在同一回合把改动传播到
另一面：

- 人提出 idea / 决策 → 同时更新 ideas **和** output；若 output 尚未生成，只更新 ideas。
- 人修改 output → agent **反向校准**进 ideas（更新既有卡或代笔新卡；代笔仍是人的
  判断，agent 只是誊写，不违背"只有人能创建 idea"）。
- 冲突以 output 为准（生成后它是主工作面）。

idea 层不因 output 出现而废除，只是换角色：从工作面变成**决策记录**——
① 溯源链（output 元素 → idea → source）是产品楔子；② 归档卡保存被否掉的路，
是防事后翻案的负空间；③ 同一批 ideas 可装配多个 output。先例即
ADR（append-only 的为什么）与活设计文档（当前的是什么）长期共存。

ADR 与活文档并存的实践见 [ADR](../sources/methods/adr-method.md)；溯源即卖点见
[判断溯源楔子](judgment-provenance-wedge.md)；全记录防翻案见
[four-persona-scenarios](four-persona-scenarios.md) 的不可逆决策场景。

校准 [output-auto-refresh](output-auto-refresh.md) 的方向语义：自动刷新只作用于
**已存在**的 output（idea 变更→重推受影响元素），首次生成归人；新增反向流
（output 变更→ideas）同样由 agent 承担、logs 记账。
