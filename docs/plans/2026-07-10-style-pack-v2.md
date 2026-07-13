# style pack v2 — 风格去语义化 + 引入 5 个 frontend-slides 系风格

## 目标

风格包只承载 UI（palette/字型/几何/气质/呈现形态），内容语义全部上收到 skill 层；
风格与画布正交：任意 canvas 可用任意 style。同时新增 5 个取材 frontend-slides
预设/Bold 包的风格：notebook-tabs、swiss-modern、terminal-green、bold-signal、
8-bit-orbit——每个带 tabbed-gallery 的定制呈现章节。

## 决策（已与人确认）

- token 去语义化：`c-src/c-idea/c-out/human/c-ok` → `accent-a/b/c/d/positive`。
- 层→accent 绑定唯一写在 SKILL.md 渲染段（sources→a、ideas→b、output→c、
  human→d、ok→positive；output 视觉最重、positive 只给已批准态）。
- design.md 章节 `## Layer semantics` → `## Accent roles`；`## Invariants`
  删除（已由 selection-index usage 承载，一事一家）。
- 布局归 style：新增可选 `## Canvas renderings` 章节 + `### <canvas-slug>` 小节；
  索引条目可选 `canvas_renderings` 列表，校验器验证 canvas 目录存在且 design.md
  含对应小节。老 4 风格走 canvas 默认呈现，不加该字段。
- 不新增 canvas：五种布局原型都是 tabbed-gallery 的呈现变体（IA 未变）。

## 单元（每单元先测试后实现）

1. docs：architecture.md styles 行、canvas.md 模板段补"风格×画布正交"。
2. tests/test_style_pack.py：token 集合、别名、章节、canvas_renderings
   三用例（合法/未知 canvas/缺小节）改写。
3. check_style_pack.py：CANONICAL_TOKENS、DESIGN_SECTIONS、canvas_renderings 校验。
4. canvases/tabbed-gallery/template.html：CSS 变量同名改写（token 钉死测试锚点）。
5. 老 4 风格 design.md/preview.md 改写；SKILL.md 绑定行。
6. 新 5 风格 design.md/preview.md + selection-index.json（9 条目，≤8KB）。
7. 验证：pytest 全绿 + check_style_pack + build_canvas 端到端出 HTML。
8. testing.md 测试地图行、TODO 清理、提交、PR、CI 盯绿。

## 不做

- 每风格 reference.html（规格即真身，避免双源头）。
- 老 4 风格的 canvas 定制章节（默认呈现已成立，需要时再补）。
