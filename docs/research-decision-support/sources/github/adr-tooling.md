# [GitHub] adr-tools / log4brains — ADR 工具族与"决策失联"痛点

github.com/npryce/adr-tools（bash CLI，事实标准）· github.com/thomvaill/log4brains（Node，
静态站发布）· adr.github.io（规范枢纽）。

核心逻辑：模板脚手架 + 编号 + supersede 状态机；log4brains 主张 ADR 不可变（只变状态），
"文档永不过期——它至少某天为真"。惯例存 `docs/adr/`，与代码同仓同版本。

痛点（2026 口径，Catio 指南）：工具停在模板/CLI 层，**没人解决决策与活系统失联
（drift）**；DevOps.com："决策、坑、why 最难进文档"。两个主力工具都无 agent 参与、无
证据链（decision ← evidence）概念。

**与 本项目 的关系**：本项目 decisions 层的思维模式（drivers × options × trade-offs、
append-only、affects 锚定）单拎出来即是 agent-native decision-log skill 的空位。来源：
[Catio 2026 指南](https://www.catio.tech/blog/architecture-decision-record)、
[log4brains](https://github.com/thomvaill/log4brains)、
[DevOps.com](https://devops.com/documentation-is-dead-long-live-documentation/)。
