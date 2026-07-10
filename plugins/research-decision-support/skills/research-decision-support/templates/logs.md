# logs — append-only 变更账本（覆盖 ideas 与 output 两层）

约定：每行 `- 日期 · 卡/文档 · 动作 · 改动（旧 → 新 的最小 delta）· 原因`；
必须记**改动本身**而不只动作与原因；有 output 后同一变更每层各记一条
（idea 一行 + output 一行）；只追加，永不改写旧行——docs 不入 git，本账本是
回溯的唯一依据。
