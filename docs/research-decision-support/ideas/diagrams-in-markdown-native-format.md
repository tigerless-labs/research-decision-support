---
id: diagrams-in-markdown-native-format
type: idea
tags: [协议]
---

# 系统设计图在 markdown 真身就得是可视化图格式

output 的系统设计图**固定用 markdown 原生的声明式图格式**（当前：mermaid 代码块）
——真身本身就是图，不是散文描述配外挂图片，也不是只存在于 HTML 的手绘物。
理由：真身在任何支持渲染的宿主（GitHub / Obsidian / IDE）直接可视化；图的变更
走文本 diff，账本可记最小 delta；节点→模块的点穿映射可在图源里声明
（`click` 行），投影只是转绘不添事实（[markdown 唯一真身](drafts-not-state.md)）。
图内每节点带主标+副标两行，信息集与投影版逐块一致。对比 ASCII 框图：后者布局
全可控、信息密度高，但改一框须手工重排全图、diff 是对齐噪音记不了最小 delta、
无 click 语义、CJK 字宽下框线易歪——只适合一次成型的静态快照；高频演化 + 要
点穿的系统图用声明式。
