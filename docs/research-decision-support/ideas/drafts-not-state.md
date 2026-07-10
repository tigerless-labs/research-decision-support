---
id: drafts-not-state
type: idea
tags: [协议]
---

# HTML 不持有事实：浏览器标注是草稿，markdown 是真身

页面可整体重建而零损失；读中落下的标注存浏览器本地，经导出补丁回流卡片。这保住了
agent-native 形态（agent 读写 markdown，人看渲染），也避免了引入服务端。与
[Elicit](../sources/products/elicit.md) 的差异正在于此：它的表格是产品数据库，本项目 的
"表格"只是 markdown 的投影。

**同步纪律**（2026-07-09 人的裁决）：每次 markdown 真身改动，HTML 投影必须
**同回合重建发布**；修改顺序恒为**先改 markdown、再同步 HTML**；绝对禁止只改
HTML——投影上不存在"独立编辑"这个动作。
