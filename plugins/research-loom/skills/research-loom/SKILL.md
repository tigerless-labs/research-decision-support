---
name: research-loom
description: 把几十篇论文织成自己的、可溯源的设计 —— 提炼每篇论点优缺点、分方向对比、蒸馏成认可的思路与新 idea、组装成设计并链回论文、对争议点做决策。五者是结构层不是步骤，按需跨层维护、每层固定格式。Use when 整理大量文献做综述、从论文出发做架构/方法设计、把读到的东西沉淀成自己带出处的设计、或要在 docs/research-loom/ 里推进"文献→设计"工作时（"整理这些论文""做个方向对比""把这些想法组装成设计""这个设计点怎么决策"）。
license: MIT
allowed-tools: Bash(python3 ${CLAUDE_SKILL_DIR}/scripts/*)
metadata:
  author: tigerless.ai
  repository: https://github.com/tigerless-ai/research-loom
---

# research-loom —— 文献→设计 合成工作法

被触发后进入**合成模式**。五者是内容的**结构层，不是时间步骤**——按真实节奏跨层穿梭（调研一批就先搭设计、随后再调研、随时回改 idea），任意顺序、可交错。skill 不排时序，只做一件事：**把你产出的每一块归到对的层、保持原子、按格式落盘、连好链接**。层间是 provenance 依赖（设计建立在 idea、idea 引用源卡、决策作用于设计），不是先后。

三种卡与 frontmatter 契约见 [note-types](references/note-types.md)。骨架借自成熟实践：Zettelkasten（原子+链接）· Webster-Watson（概念矩阵）· ADR + 决策权衡（ATAM/set-based）。

**铁律**：

- **三种卡分家**：文献笔记（论文说）≠ 永久笔记（我说）≠ 设计（组装）。详见 [note-types](references/note-types.md)。
- **相对 Markdown 链接**互连原子，`[[ ]]` 不作链接机制。
- **append-only**：ADR 只增不删。
- 每次写入后跑校验器：`python3 ${CLAUDE_SKILL_DIR}/scripts/check_doc_links.py docs`（`check_research_loom.py` 校验 frontmatter，尚未实现时跳过）。

**写卡四律**（每张卡都守）：

- **实时更新**：决策一在对话里定下，立刻落进对应卡，别滞留在聊天里。
- **留后单列、明确、最小**：deferred 内容单独成节并标「留后 / 留窗口」，笔墨压到最小，不与已定内容混排。
- **已定即精炼**：确定的内容用最精炼语言记录，不留推演过程。
- **结构一眼可读**：每卡把「确定 / 留后 / 待解」分开，整体清晰易懂。

## 开场

先用一行说清这次在**哪一层、做什么**（不是"推进到第几阶段"），再开始。哪层先动取决于你手头在做什么——可自底向上（源→idea→设计），也可自顶向下（先搭设计再补 idea/源）。内容全部落在 `docs/research-loom/`。

## 主动引导（skill 的另一半：看火候推进度）

归档是被动的一半；主动的一半是**认出时机、替用户推一步**。触发即动，不等指令：

- **来了新材料**（用户让读/引用/讨论新论文、repo、帖子）→ 当场落 source 卡入对应子目录、更新索引。这条不用问。
- **未归类来源堆积**（新卡明显超出已有方向的覆盖）→ 主动提议归类："这几篇和 X 方向像不像？还是该立新方向？"给出试探性分组，**用户裁决后**才落 synthesis 卡——方向是用户的判断，不是 agent 的。
- **判断散落在对话里**（"我觉得""这个不靠谱""有意思"）→ 提醒升格：值得留的判断落 idea 卡（status: 候选），引用当场带上；不值得留的明确说不留。
- **采纳的 idea 无处安放**（没有任何 design 引用它）→ 时机合适时点出来：组装进设计，或降级/砍掉。
- **两个方案拉锯、用户犹豫** → 开决策工作单（drivers × options × trade-offs），收敛成 ADR。

分寸：每次只推**一步**，推的理由说一句就够；用户不接就放下，不重复劝。

## 五层（任意顺序维护）

下面是每层**维护什么**，不是执行顺序。任一层随时可增改。

### 来源 — `sources/`（`papers/` `github/` `blogs/` …）
- 每个来源一张文献笔记（核心论点、做法、优缺点、与 autoharness 相关性），跟随该目录现有卡片格式。事实层，不掺判断。
- **自动归类**：按类型归入 `sources/` 下子目录；类型是开放集，无匹配则新建一类（如 `video/`、`dataset/`），别硬塞。

### 方向 — `synthesis/`
- 把来源横向聚成方向，每方向一张 MOC（模板 [direction-moc](templates/direction-moc.md)）+ 概念矩阵（来源 × 维度 + **我的评判**列）。按概念组织，不按作者。
- **每个分类文件写清和其他分类的区别**：界定本方向的边界，点名与之相邻/易混的方向并说清分界，确保各方向互斥不重叠。
- 视图：概念矩阵（纯 Markdown 手维护的表）。

### idea — `ideas/`
- 把认可的思路与新念头各提为一张永久笔记（模板 [idea-note](templates/idea-note.md)）：**用自己的话、原子化、引用所凭的来源**。`status: 候选/采纳/存疑`。
- 关键：不是论文摘要，是你的主张。

### 设计 — `design/`
把 idea 织成设计，分两类文件（模板 [design-provenance](templates/design-provenance.md)）：
- **脊柱一篇**：原则 + 流水线 + 全局不变量，含架构图（Mermaid）；每元素登记稳定 ID。
- **每步/模块各一篇**：只写本步的行为边界、接口契约、验收标准；全局不变量上提到脊柱，此处不重述。
- `index.md` 只做指针。三类都连 provenance：**设计元素 → ideas → 源卡**。

### 决策 — `decisions/`
对设计上有争议的点开决策工作表（模板 [decision-worksheet](templates/decision-worksheet.md)），骨架 **驱动力 → 选项 → 权衡 → 取舍**：
- **驱动力**（加权质量属性）= 决策的重点：不在真空里决，而是针对一组质量属性（成本/可维护性/收敛…），参考 ATAM 的敏感点/权衡点。
- **选项 set-based**：至少留 2 个变体并行养着，随证据收窄，别早押一个（丰田 Set-Based Design）。
- **权衡**：选项 × 驱动力打分，证据来自源卡。
- **可逆性闸门**：双向门（可逆）直接试，单向门才上全套（Bezos）。
- **Bayesian 重开**：新源卡可推翻旧决策，记"什么证据会重开"。

定了**坍缩成 ADR**（模板 [adr](templates/adr.md)，`supersedes` 旧的，append-only），作用回设计。决策与设计相互引用（`affects` ↔ provenance）、反复对改，无强制时序。

## 收尾

每轮结束：跑两个校验器确认无悬空链接、frontmatter 合规；用一行说清这次动了**哪些层**。

## 渲染是投影，不入库

需要给人看/给自己读全局时，把 workspace 渲染成工作台（overview / read / compare / ideas /
design / decisions / map + card 阅读器）：

```bash
python3 ${CLAUDE_SKILL_DIR}/scripts/build_loom_site.py <workspace> -o /tmp/loom-site --title <名字>
```

输出到**临时目录**，或作为 Artifact 发布分享——**生成的 HTML 永不提交进仓库**。markdown 是
唯一真身，投影随时一条命令重建；把投影 checked-in 等于让同一事实住两个家。

read 页支持读中打标（状态/方向/一句话判断，浏览器草稿），导出的补丁交回 agent；收到补丁时
逐条写回对应卡的 frontmatter 与正文。
