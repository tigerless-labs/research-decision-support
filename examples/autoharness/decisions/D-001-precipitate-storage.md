---
id: D-001-precipitate-storage
type: decision
status: open
affects: [validate-store, architecture]
---
# 决策：自动沉淀的经验存在哪一层

问题原述与全部论据在 [precipitate-storage-layer](../ideas/precipitate-storage-layer.md)；本卡只跑决策模型。作用于 [validate-store](../design/validate-store.md) 与 [architecture](../design/architecture.md) 的存储契约。

## 驱动力

- 可传播（skill 是天然分发单元）: 高 —— user 新增
- 注入可靠度（能否走确定性通道）: 高
- 对原生零侵入（[ADR-002](ADR-002-additive-zero-intrusion.md)）: 硬约束
- curate 退役的可操作性（能直接停用一个符号）: 中

## 选项（set-based）

- A 独立 instinct 层：私有存储 + hook 确定性注入（[ECC](../sources/github/affaan-m-ecc.md) 路线）
- B 长成原生 skill：复用注册/读取/description 概率触发（[Hermes](../sources/github/nousresearch-hermes-agent.md) 路线）
- C 混合苗圃：先入独立层 curate，存活过阈值「毕业」固化为 skill

## 权衡

| | 可传播 | 注入可靠度 | 零侵入 | 退役操作性 | 证据 |
|---|---|---|---|---|---|
| A | 弱（私有层不便分享） | 强（hook 100%） | 强 | 强 | [ECC](../sources/github/affaan-m-ecc.md) |
| B | 强 | 弱（概率 50-80%） | 待证（维护要改原生链路） | 弱 | [Hermes](../sources/github/nousresearch-hermes-agent.md) |
| C | 强（毕业后） | 分段（苗圃强/成品弱） | 强 | 强（苗圃期） | 三系分裂本身：[trace-to-experience](../synthesis/trace-to-experience.md) |

敏感点：B 的「维护自产 skill」是否越过零侵入边界。可逆性：双向门（存储形态可迁移）。
user 取向 **B**（可传播压倒），落地路径倾向 **C 作过渡**；还缺的证据：原生 skill 机制能否承载退役开关。定后坍缩 ADR。
