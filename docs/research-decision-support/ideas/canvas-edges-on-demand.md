---
id: canvas-edges-on-demand
type: idea
tags: [画板]
---

# 画板连线按需显现：单击看关系，双击进详情

节点间的关联由 agent 实时推导并持久存储，但**默认不画线**——满屏连线是认知负载
不是信息，图的默认态是干净的散点场，线是查询结果不是背景。交互两级：**单击**节点，
只亮出它的直接邻边（这条 idea 和谁有关）；**双击**打开节点详情——正文、logs、
证据锚点。三大块（source / idea / design）同屏还是分屏，暂缓裁决。

本项目 map 页交互已验证"hover 只亮直接邻居"的减负效果（全链高亮被否）；反例是
[InfraNodus](../sources/products/infranodus.md) 式全图连线——首屏即毛线团，
影响力排序被视觉噪声淹没。

Refines [creation-canvas](creation-canvas.md)——"实时自动连线"精确化为**推导实时、
渲染按需**。To be weighed in [decisions/](../index.md)：三大块同屏/分屏；
单击邻边是否分跳数层级。
