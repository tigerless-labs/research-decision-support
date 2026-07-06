# 三种卡 + frontmatter 契约

## 三种卡分家（命门）

| 卡型 | 装什么 | 位置 | frontmatter |
|---|---|---|---|
| **文献笔记** | 论文/repo/博客**说了什么**——论点、做法、优缺点 | `sources/`（内分 `papers/` `github/` `blogs/` …） | 跟随现有卡片格式（散文，无强制 frontmatter） |
| **永久笔记** | **我说什么**——我的主张/新 idea，用自己的话、引用文献 | `ideas/` | `type: idea` |
| **设计** | 永久笔记**组装**成的设计：脊柱（原则+流水线+不变量）+ 每步/模块文档 | `design/` | `type: design` |

外加 ② 的**方向卡**（`synthesis/`，`type: direction`）与 ⑤ 的**决策卡 / ADR**（`decisions/`，`type: decision` / `adr`）。

**为什么分家**：永久笔记不是论文摘要。文献笔记（论文说）与永久笔记（我说）解耦，念头才能脱离原始出处、自由重组进设计而不必重构。

## frontmatter 契约（由 `tools/check_workspace.py` 强制）

只有新阶段原子带 frontmatter；旧来源卡为散文格式，豁免。必填字段缺失或 status 越界 → 校验器报错。

- `type: direction` — 必填 `id` `type`
- `type: idea` — 必填 `id` `type` `status`；`status ∈ {候选, 采纳, 存疑}`
- `type: design` — 必填 `id` `type`
- `type: decision` — 必填 `id` `type` `status` `affects`；`status ∈ {open, resolved}`
- `type: adr` — 必填 `id` `type` `status`；`status ∈ {proposed, accepted, superseded}`

`affects` 锚定到 `design/` 脊柱图的元素稳定 ID，把决策接到设计上。

## 链接约定

原子之间用**相对 Markdown 链接**（`[label](../sources/papers/<id>.md)`）：GitHub 可渲染、Obsidian 可反链、`tools/check_doc_links.py` 可校验。`[[ ]]` **不作链接机制**——现有散文里有示意性 `[[ ]]`，强校验会误报。

provenance 链：`design 元素 → ideas/<id>.md → sources/papers/<id>.md`，沿相对链接任何设计选择可一路追回论文。
