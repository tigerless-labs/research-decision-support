# ideas 与 output 彻底解耦

## 裁决（人，2026-07-16）

取代 sync-on-command（2026-07-14）：

- idea 变更与 output 变更**完全解耦，不再同步**——正向不再有 sync 义务，反向
  回校（back-transcription/calibration）取消：人改 output 就留在 output。
- 两层唯一重新连接的时刻是人下令 assembly（重推导仍是人拍板的生成动作，保留）。
- agent 跨层仅剩一个义务：**output 落后 ideas 很多**时提醒一次（"output is N
  ideas behind"），绝不唠叨。

## 改动单元

1. **ideas 层（truth 先行）**：新卡 `layers-decoupled-drift-reminder`；旧卡
   `sync-on-command-layers-independent` 归档到 `ideas/archive/`；
   `output-primary-after-generation` 就地瘦身（back-calibration 半句退役）；
   `ideas/index.md` 重生成 sync 组；logs.md 记账。
2. **output 层（人已下令的 output 更新）**：modules/agent.md、idea.md、output.md
   的 sync 行改为解耦表述；system.md 两张图删 back-calibrate 节点与 sync 边、
   IDEA↔OUT 关系改单向 assembly；output/index.md、file-structure.md、target.md、
   workspace index.md 的 sync 措辞与链接更新（指向新卡）。
3. **测试**：test_plugin_manifests 增 SKILL.md 解耦不变量（含 decoupled、
   不含 back-transcribe）；既有 badge/manifest 同步测试覆盖版本。
4. **plugin**：SKILL.md（frontmatter description、output 层节、workflow 第 3 步
   重写、teach-in-place 两句）；双 plugin.json description 同步改；README
   "every later sync..." 段改写。
5. **版本**：0.9.2 → 0.9.3 双清单 + README badge。
6. **投影**：画布重建、artifact 同 URL 重发；check_doc_links 全绿。

## 验收

- 全量测试绿；两个 validator 绿。
- 工作区内不再有活文档声称自动回校或 sync-on-command（archive 除外）。
