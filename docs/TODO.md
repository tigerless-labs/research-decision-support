# TODO

- [ ] 配置 CI：pytest + check_doc_links + check_workspace + check_style_pack（remote/PR 流程已在用）。
- [ ] 发布时用 Pages CI 现场生成 demo 站（HTML 不入库，README 挂链接）——demo 源待定（examples/autoharness 仍是 v1 四层 schema）。
- [ ] examples/autoharness 迁 v2 三层 schema（现为 v1 格式，v2 校验器不适用；README 活例子依赖它）。
- [ ] read 页导出补丁的自动落盘工具（现靠 agent 手动写回）。
- [ ] examples/autoharness 4 条预存悬链（plans/roadmap、experiments/E6）— master 上已存在，非 design 迁移引入
- [ ] decisions 层开首张卡：why-now 假设（agent 消除捕获成本），状态 open 等原型证据
- [ ] 证据源插件：arXiv/S2 auto-card、arXiv 查新、Elicit MCP 适配、Zotero/Elicit 导入器
- [ ] 收/证/决 + 裁决桌全量重构计划（docs/plans/ 另立）；场景 skills repo 改造方案
- [ ] output 形态推荐集（定 target 时 agent 供人选的形态库）——首款已入：系统设计（系统图+modules 层，适用项目开发/论文设计），待扩
- [ ] canvas 画板模板库（定 target 时 agent 供人选的风格集）——现两款：分页画廊（v2 已实现 build_canvas + 模板）、单画布三团（spec 已入 canvases/，待建），待扩
- [ ] vendored mermaid.min.js 3.5MB 减重评估（现仅 output 用到 mermaid 时才嵌入 HTML）。
- [ ] 其余 7 风格的 `### single-canvas` 定制呈现章节（pin-and-paper 已带，预览 artifact 已给按层卡形方向，随 single-canvas 实现落地）。
- [ ] skill 解冻时：references/output-forms/system-design.md 的流程图规格更新为"时间轴泳道 flowchart（人上 agent 下、编号之字形左右推进、同步回边）"，与 system.md 现状对齐。
- [ ] docs 入 git（PR #13）后的陈述清扫："不入 git / docs 不入 git" 残句仍在 output/file-structure.md、logs.md 头部、SKILL.md 等处，逐一改为入 git 后的事实。
