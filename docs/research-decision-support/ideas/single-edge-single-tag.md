---
id: single-edge-single-tag
type: idea
tags: [schema]
---

# 全局只有两种结构化事实：引用（唯一关联）+ tag（唯一分类）

卡与卡之间的关联**只有引用一种**：A 卡正文里指向 B 卡的
markdown 链接即一条边；同行文字可带一句语义说明，但系统层面不设关系类型
枚举（无依赖/互斥/支撑等 typed edges）。引用**只准向前**：只能指向本卡赖以
成立的东西（证据、所依赖或所修正的先行卡）；"我支持了谁 / 谁引用了我"是下游
关系，一律不落笔，backlink 由投影扫描派生，不双写。引用可指向其他 idea 卡，但**不得成环**——两卡互引
意味着要么同一判断该合并，要么有一边其实是下游关系（删引用，交给 backlink）。

分类**只有 tag 一种**：单层（tag 即顶层分类，无嵌套）、**一卡至多一个**（单卡
不交叉——一张卡若与两个 tag 都有关系，说明混了两个判断，拆成两张卡）、可选
（确实属于一类才分类，无 tag 即未分类）；无目录树，小团靠 tag 涌现
（[source-tags-self-classify](source-tags-self-classify.md) 推广到全部三层）。

**距离与坐标不是事实，不入真身**：画板从引用（引力）和 tag（同团）两种离散
事实用力导向派生布局；真身动、布局重算。坐标永不写回 markdown——这是
「画板不持有事实」的对偶：markdown 也不持有布局。存坐标的方案（如 .canvas
JSON）会把每次拖拽变成"事实变更"，污染账本。

先例：Zettelkasten/Obsidian——wiki-link 即图，图由链接涌现，graph view 布局
即时计算、不落盘；typed-edge 分类法（IBIS 三实体）死于捕获成本。

[Zettelkasten](../sources/methods/zettelkasten.md) 链接即结构；
[IBIS 反面教材](../sources/methods/ibis-qoc.md) 多类型模型的捕获成本；
tag 涌现见 [source-tags-self-classify](source-tags-self-classify.md)。

细化 [source-tags-self-classify](source-tags-self-classify.md) 的 tag 机制到全部
三层；两种事实由 agent 的同一推导步产出（tag 分类与连线都是看关系，见流程图
"推导连线"节点）；引用边的存储位即卡内正文的引用行（卡＝标题+摘要，无固定
段落），agent 推导新关联＝在摘要中补一处引用。
