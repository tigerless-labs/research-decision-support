---
id: competitive-landscape
type: direction
---

# 方向：文献工作台竞品格局（谁做到哪一步就停了）

**界定**：收"帮研究者处理文献/材料"的工具、方法与自动研究 agent；通用 agent 框架、
写作工具列界外。与其他方向无重叠（本工作区目前仅此一个方向）。

五个簇，按"停在流水线哪一步"分：

| 簇 | 代表 | 做到 | 停在 |
|---|---|---|---|
| 发现图谱 | [Connected Papers](../sources/products/connected-papers.md) · [ResearchRabbit](../sources/products/researchrabbit.md) · [Litmaps](../sources/products/litmaps.md) | 找到该读什么 | 图只读，读后无处落判断 |
| 提取矩阵 | [Elicit](../sources/products/elicit.md) | 论文事实进表格、格子带出处 | 格子是论文的话，不是我的话 |
| 边读边筛 | [Rayyan/Covidence](../sources/products/rayyan.md) | 读中标注的人机工学 | 二值纳入/排除，不产综合 |
| 库与手工矩阵 | [Zotero](../sources/products/zotero.md) + [synthesis matrix 惯例](../sources/blogs/synthesis-matrix.md) | 存好、标平面标签、手填表 | 层级（方向→判断→设计）靠人肉 |
| 自动研究 agent | [gpt-researcher](../sources/github/gpt-researcher.md) · [STORM](../sources/github/storm.md) · [open_deep_research 族](../sources/github/open-deep-research.md) | 自动搜→读→写出带引用报告 | 报告即终点：过程即弃、判断不可见、不可增量演化 |

**我的评判**：五簇合起来恰好画出 loom 的位置——自动研究 agent 自动化的是**读与写**，
loom 结构化的是中间被它们压扁的东西：**你的判断**。没有一家把判断作为一等对象沉淀并
带出处流向设计；STORM 的 Co-STORM mind map 最接近（有结构化中间层）但属系统而非用户、
不可版本化、不通向 ADR。也没有 agent-native（markdown 为真身、静态 HTML 为投影）的形态。
全部竞品要么是上游（发现、库、自动报告→可拆成 sources 卡入料），要么是平行件（提取、
筛选），不是替代品。
