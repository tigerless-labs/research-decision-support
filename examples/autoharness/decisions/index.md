# decisions — ⑤ 精炼（决策工作表 → ADR）

对设计上有争议的点跑决策模型（驱动力→选项→权衡→取舍），开放态为决策工作表，定了坍缩成一条 ADR。**ADR 只增不删**，旧决策标记被取代而非抹除。决策锚定到 [design/](../design/index.md) 的元素。方法由 `research-decision-support` skill 承载。


- [D-001 沉淀物存哪层](D-001-precipitate-storage.md) — `open`：A instinct 层 / B 长成 skill / C 苗圃毕业；user 倾向 B。
- [ADR-001 率不用墙钟](ADR-001-rate-over-wallclock.md) — `accepted`：存活判据 = 调用率，作用于 MNG。
- [ADR-002 纯叠加零侵入](ADR-002-additive-zero-intrusion.md) — `accepted`：产品硬边界，作用于全局。
- [ADR-003 episode 边界反思](ADR-003-episode-boundary.md) — `accepted`：整段蒸馏优于逐调用碎片，作用于 CAP/REF。
