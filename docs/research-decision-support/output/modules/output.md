# output 装配模块

**职责**：存在态 idea 的装配产物；系统的对外交付面，生成后是主工作面。

**行为边界**：

- **形态由用户的 target 决定**（当前 target：系统设计）；定 target 时 agent 可向
  用户推荐形态。
- 推荐集（形态库）首款：**系统设计**＝各类系统设计图 + modules 细节层（一模块
  一文，图块点穿），适用 target：项目开发、论文设计等；本工作区的 output 即其
  活实例。推荐集待扩。
- 系统设计图在 markdown 真身即为可视化图格式（mermaid，含 click 点穿声明），
  不是散文配外挂图。
- 首次装配**由人启动**；output 未生成时人的 idea 只落 idea 层。
- 生成后与 idea 层**永远双向同步**：idea 变更→同回合重推受影响元素（重derive
  不重写全文）；output 变更→agent 反向校准进 ideas；冲突以 output 为准。
- 每个元素链回装配它的 idea 及其 logs，再点穿到 source。

**溯源**：[图即真身格式](../../ideas/diagrams-in-markdown-native-format.md) ·
[output 为主](../../ideas/output-primary-after-generation.md) ·
[output 自动刷新](../../ideas/output-auto-refresh.md) ·
[判断溯源楔子](../../ideas/judgment-provenance-wedge.md)。
