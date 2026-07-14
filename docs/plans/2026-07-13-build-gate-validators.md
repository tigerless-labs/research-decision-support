# build_canvas 前置校验门 + 空 workspace 崩溃修复

## 背景

契约要求每次写后跑两个 validator、每次真相变动重建画布，但校验靠 agent 自觉，
会漏。裁决（人）：把两个 check 并入 build_canvas 作为前置门——报错直接出现在
build 输出里，agent 当场看到当场修，机械保证不漏。另修 E2E 发现的存量 bug：
零卡片 workspace 建画布时 layout 对空集取 max 崩溃（TODO 已记）。

## 方案

- **前置门**：`build()` 开始先跑 `check_workspace.check()` 与
  `check_doc_links.check_links()`（都只扫传入的 workspace，范围与本次投影一致），
  有问题→逐条打印并异常退出，**不产出 HTML**——坏真相不投影（fail-safe）。
  复用两个模块的既有函数，零逻辑复制；独立 CLI 保留不动。
- **空 workspace**：零卡片时 layout 不再崩溃，正常产出只含空态占位的画布
  （刚 init 的 workspace 首次建板即可看到棋盘）。
- **SKILL.md**："After every write, run both validators" 改为 build 内置校验、
  纯写不建板时仍手跑；canvas 章节注明 build 失败即校验失败清单。

## 单元（tests 先行）

1. output 文档：`modules/canvas.md` build 节增"先校验后投影、失败不产出"边界；
   `file-structure.md` build_canvas 条目同步；`logs.md` 追记；testing.md 地图更新。
2. tests：坏 workspace（非法卡）→ build 异常且 outdir 无 canvas.html；
   悬链 workspace → 同上；合法 workspace → 照常产出；零卡片 workspace →
   正常产出且含 board 空态。
3. 实现 + 全测试绿 + 端到端（真实 workspace build、坏卡注入后 build 拒绝）。
4. TODO 清项 → PR（叠在 workspace-discovery PR 上）→ CI。
