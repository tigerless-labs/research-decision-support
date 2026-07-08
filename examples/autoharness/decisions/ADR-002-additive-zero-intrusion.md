---
id: ADR-002-additive-zero-intrusion
type: adr
status: accepted
affects: [architecture, spine]
supersedes:
---
# 一切增强纯叠加，对原生 skill 零侵入

补记：user 划定的产品边界，主张全文在 [additive-over-native-skill](../ideas/additive-over-native-skill.md)；此处坍缩为约束性 ADR。

## 背景

autoharness 挂进宿主 agent 的方式有两类：接管/改写原生 skill 链路（能做更强的召回与维护），或在原生之外纯叠加。威胁质量属性：用户信任与可卸载性——改坏原生体验的增强会被整体弃用。

## 决定

选纯叠加：skill 的新增、读取、description 概率触发维持原样，不替换、不拦截、不降级；hook 注入是**另开的并行通道**（[hook-forced-injection](../ideas/hook-forced-injection.md) 的采纳前提）；生命周期只管带自产标记的符号（[lifecycle-by-provenance](../ideas/lifecycle-by-provenance.md)）。

## 后果

- 好：随装随卸、宿主感知不变；所有设计卡共享同一条硬边界。
- 差：抄不了 [Hermes](../sources/github/nousresearch-hermes-agent.md) 的 loader 内计数，观测只能在 hook 面埋点（见 [mng](../downstream-design/mng.md)）；维护原生 skill 需另走显式授权路径。

## 重开条件

宿主提供官方的 skill 链路扩展点（侵入不再等于风险），或用户明确授权接管式维护。
