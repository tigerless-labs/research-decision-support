---
tags: [方法论仓库]
---

# [GitHub] zarazhangrui/frontend-slides — 风格即规格文档 + 三层渐进选型（~25k★）

github.com/zarazhangrui/frontend-slides（24.9k★，Claude Code skill）· 姊妹库
github.com/zarazhangrui/beautiful-html-templates（3.5k★，agent-agnostic 模板资源库，
被整库 vendor 进 skill 作 `bold-template-pack/`）· 2026-07 采样 · 作者非程序员非设计师。

核心逻辑：**HTML 模板的本体是 design.md**——34 个风格各是一份声明式规格（YAML
frontmatter：colors / color-aliases / typography / components token + 签名元素散文），
不是成品 HTML；`template.html` 只是规格缺细节时的兜底。选型走三层渐进加载：
`selection-index.json`（mood/formality/density/scheme + best_for/avoid_for 紧凑元数据）→
入围者的 `preview.md`（小预览卡）→ 仅最终选中者的完整 `design.md`，索引内嵌
"never bulk-read" 使用策略。生产方式：AI 生成 + 人按真实设计参照做品味把关，每条迭代
中发现的品味规则固化进规格（禁紫渐变/禁陈词字体等反 AI-slop 禁令全局化于 SKILL.md）。

**与本项目的关系**：「人出品味、agent 出产量，判断固化成版本化规格」与本项目命题同构。
其风格库架构已于 2026-07-09 移植为 skill 内置风格包（`styles/`，校验器信任门，
PR #3 起）——移植决策与差异（纯 agent 可读、强制明暗双 palette、红队校验）沉淀在
下游 idea 与 output，此处不引（引用只准向前）。
