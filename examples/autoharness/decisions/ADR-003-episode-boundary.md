---
id: ADR-003-episode-boundary
type: adr
status: accepted
affects: [cap, ref]
supersedes:
---
# 反思按 episode 边界整段做，不逐 tool 调用抓碎片

补记：从 [episode-boundary-reflection](../ideas/episode-boundary-reflection.md) 的已定主张坍缩而来。

## 背景

经验沉淀的触发与粒度二选一：[ECC](../sources/github/affaan-m-ecc.md) 在每次 PreToolUse/PostToolUse 抓单条 tool I/O、后台从滚动 tail 凑模式；[Hermes](../sources/github/nousresearch-hermes-agent.md) 按迭代计数在 turn 收尾整段 replay transcript。威胁质量属性：蒸馏质量（语义完整性）与成本。

## 决定

选 episode 边界整段反思（[cap](../downstream-design/cap.md) 触发、[ref](../downstream-design/ref.md) 执行）：反思单位是含用户意图与最终结果的完整轨迹，而非被 500 行窗口任意切开的碎片；同上下文 replay 吃 warm prefix cache，连贯且便宜。

## 后果

- 好：蒸馏输入语义完整；不需要 ECC 式后台 observer 常驻。
- 差：episode 内的即时信号（如当场纠错）要等到边界才被看见。

## 重开条件

实证出现「边界等待导致高价值模式丢失」，或宿主提供可靠的调用级语义事件流。
