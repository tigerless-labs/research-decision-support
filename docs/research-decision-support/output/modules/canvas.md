# canvas 画板投影

**职责**：全部卡片的可视面——帮人理清思路的主战场，胜负手是直观、好看、清晰。

**规则（模板无关的不变量）**：

- 画板**只是可视化层**：基于 markdown 真身的变化而变化（真身动，板即动），
  自身不持有任何事实，也不接受绕过真身的写入。
- 连线＝卡内引用（agent 推导即在摘要补引用行）。
- 布局由引用（引力）与 tag（同团）两种离散事实派生，距离/坐标不入真身。
- 一卡至多一 tag，聚类无歧义；无 tag 卡落未分类散区。
- 兼任协议的就地说明书：output 未生成时其位常驻空态占位（教启动权归人），
  布局顺序即流程顺序，同步时被动更新的一边节点闪亮。

**模板（唯一：融合画布——模板集机制退役，画布只此一种、skill 内一层 canvas/ 文件
即够，风格包挂于其下）**——模板只定信息架构与交互契约，视觉全权归风格包（以 token
接口分界，见 [file-structure](../file-structure.md)）：

- **融合画布**＝单画布底盘 + 画廊优点合并：单一无限画布，Figma 式缩放/拖拽，
  三团对应三大块、团内按 tag 聚小团；缩放三档即画廊三页（鸟瞰·团簇 / 分类·tag 组 /
  细读·卡片＝网格速读）；空态就地教学、注入红队同级保留。

**融合画布交互契约（人的 UI 裁决，2026-07-10）**：

- 布局：三世界横排（证据 / 想法 / 装配），**board 独立板块居三世界正下方居中**。
- tag 筹码**按团分行**（行首团名标签），搜索常驻工具栏、回车飞到命中卡。
- 单击语义分档：**鸟瞰档单击卡片＝飞入细读并选中**（小卡无内容，描边无意义）；
  分类/细读档单击＝亮邻边；双击＝进详情弹窗；连线默认不画。
- **装配文档参与引用边**：构建时解析 output/board 文档正文链接生成 文档→卡 边，
  选中文档即亮它装配自的卡；卡详情侧栏含"装配（引用本卡）"派生 backlink 节。
- **mermaid 图卡内点击放大**：全屏顶层弹出、自动适配视口、滚轮缩放、拖拽平移、
  点空白或 Esc 关闭；图内 click 点穿保留。
- mermaid 渲染观感由所选风格驱动、固定两开关，真身与图种不变：
  `look: handDrawn`（mermaid v11 内置手绘外观），`themeVariables` 注入当前风格
  token（底/边/字/线色 + 字体栈）。

**构建（固定脚本，2026-07-10 定形）**：

- 只有一个构建入口 `build_canvas.py`：**工作区路径是唯一必填输入**，一条命令
  渲染出完整画布 HTML（收卡、推边、布局、嵌数据、内联依赖全内建），不存在
  第二条构建路径；产物只进临时目录或 artifact，绝不入真身。
- 模板与风格分离：`canvas/template.html` 定结构与交互并留 CSS 注入槽，默认灌
  `canvas/style.css`；**换风格只换 CSS**（`--css` 传另一份风格样式），禁止为
  观感复制模板或另写脚本。模板即结构契约：agent 不改 HTML 投影，可写面只有
  markdown 真身与风格 CSS。
- 风格 CSS **预编译入库**：每个 style 目录下一份 `canvas.css`（design.md 规格的
  编译产物——规格是真身，改规格必重编译），选用时 `--css` 直接指过去，零等待；
  校验器查 canonical token 明暗双份齐全、禁外链。默认 `canvas/style.css` 是
  其中一员，永不因换风格被改写。
- 待清残差：小屏体验、大卡量性能、默认模板暗色 palette（style.css 现仅明色一套，
  token 名已按风格包规范接口对齐）。两张先行模板（分页画廊/单画布三团）随合并完成归档。

**溯源**：[单画布超集画廊](../../ideas/single-canvas-subsumes-gallery.md) ·
[分页画廊模板](../../ideas/archive/tabbed-gallery-template.md) ·
[引用+tag 两种事实](../../ideas/single-edge-single-tag.md) ·
[协议就地教学](../../ideas/protocol-discoverability-in-situ.md) ·
[创作画板](../../ideas/creation-canvas.md) ·
[单画布三团](../../ideas/archive/single-canvas-clustered-graph.md) ·
[连线按需显现](../../ideas/canvas-edges-on-demand.md) ·
[投影不持有事实](../../ideas/drafts-not-state.md) ·
[风格画布正交](../../ideas/style-canvas-orthogonality.md) ·
[固定脚本换风格只换 CSS](../../ideas/canvas-fixed-builder-style-css-only.md)。
