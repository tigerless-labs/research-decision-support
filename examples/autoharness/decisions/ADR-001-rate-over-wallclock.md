---
id: ADR-001-rate-over-wallclock
type: adr
status: accepted
affects: [mng]
supersedes:
---
# 符号存活判据用调用率，不用墙钟时间

补记：从 [mng](../downstream-design/mng.md) 已定内容坍缩而来（决策先落在了设计卡里）。

## 背景

MNG 要决定自产符号活多久。[Hermes](../sources/github/nousresearch-hermes-agent.md) curator 用时间状态机（上浮/下沉/退役随墙钟走）；但 Claude Code 非常驻——agent 关着时墙钟照走，会冤枉「没机会被用」的符号。威胁质量属性：淘汰判定的公平性与确定性。

## 决定

存活依据 = 调用率（被调次数 / 层请求数），机会相对、对临时宿主免疫；配缓刑保护小样本新符号、容量上限只在成熟池内按率竞争。证据：[dynamic-validation-lifecycle](../ideas/dynamic-validation-lifecycle.md)（时间是有用度的弱代理，率直接量）。

## 后果

- 好：不在线跑评测也能持续裁汰；判定确定、可现算。
- 差：分母要 CAP 逐回合计数、sidecar 记创建锚——多一份簿记。

## 重开条件

出现「低率但高价值」的实证（率与有用度解耦），或宿主变为常驻进程使墙钟恢复意义。
