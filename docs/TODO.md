# TODO

- [ ] 配置 CI：pytest + check_doc_links + check_workspace + check_style_pack（remote/PR 流程已在用）。
- [ ] examples/autoharness 迁 v2 三层 schema（现为 v1 格式，v2 校验器不适用；README 活例子依赖它）。
- [ ] read 页导出补丁的自动落盘工具（现靠 agent 手动写回）。
- [ ] examples/autoharness 4 条预存悬链（plans/roadmap、experiments/E6）— master 上已存在，非 design 迁移引入
- [ ] decisions 层开首张卡：why-now 假设（agent 消除捕获成本），状态 open 等原型证据
- [ ] 证据源插件：arXiv/S2 auto-card、arXiv 查新、Elicit MCP 适配、Zotero/Elicit 导入器
- [ ] 场景 skills repo 改造方案（收/证/决重构已裁决：证据分级、决策层均不做——logs 即台账；「收」落为只减改动：skill 不再对人要求格式或特定指令，不新增层）
- [ ] output 形态推荐集（定 target 时 agent 供人选的形态库）——首款已入：系统设计（系统图+modules 层，适用项目开发/论文设计），待扩
- [ ] canvas 画板模板库（定 target 时 agent 供人选的风格集）——现两款：分页画廊（v2 已实现 build_canvas + 模板）、单画布三团（spec 已入 canvases/，待建），待扩
- [ ] vendored mermaid.min.js 3.5MB 减重评估（现仅 output 用到 mermaid 时才嵌入 HTML）。
- [ ] 其余 7 风格的 `### single-canvas` 定制呈现章节（pin-and-paper 已带，预览 artifact 已给按层卡形方向，随 single-canvas 实现落地）。
- [ ] skill 解冻时：references/output-forms/system-design.md 的流程图规格更新为"时间轴泳道 flowchart（人上 agent 下、编号之字形左右推进、同步回边）"，与 system.md 现状对齐。
- [ ] docs 入 git（PR #13）后的陈述清扫："不入 git / docs 不入 git" 残句仍在 output/file-structure.md、logs.md 头部、SKILL.md 等处，逐一改为入 git 后的事实。
- [ ] workspace 发现脚本对齐（idea 卡 workspaces-many-and-freely-named；文档已先行随 v0.9.0）：init_workspace.py/discover_workspace.py 支持注册表多条目、目录名自由、移除按名查找——tests 先行，走 worktree+PR。
- [ ] build 统计行把 `__board_empty__` 占位节点计入 nodes 数（空工作区报 "1 nodes"、5 卡+空 board 报 "6 nodes"，误导排查）；统计应只数真卡，占位另计。
