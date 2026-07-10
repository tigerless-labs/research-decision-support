# 2026-07-10 · output 形态规格补 file-structure.md

## 目标

system-design 形态缺"设计→磁盘"一层的约定；工作区已有实践
（output/architecture.md），但名字与 system.md 内的架构图撞车。把实践升为规格，
并以体现"文件"的名字（file-structure.md）统一。

## 单元

1. **规格**：references/output-forms/system-design.md — Shape 加 file-structure.md，
   Rules 加一条：带注释的文件树（一行职责）+ 模块→文件映射链回 modules/，溯源照旧。
2. **工作区对齐**：output/architecture.md 改名 file-structure.md（改题）；
   output/index.md、target.md、modules/canvas.md 指针同步；logs.md 追记（旧→新）。
3. **校验与投影**：check_doc_links + check_workspace + 测试套件回归全绿；
   画布 artifact 同回合重建重发（同 URL）。

docs-only 变更，无新代码；测试＝既有校验器与测试套件回归。
