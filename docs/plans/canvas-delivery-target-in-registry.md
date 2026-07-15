# 画布交付位置记入注册表

## 目标

让 agent 可以把画布 HTML 的交付位置（输出路径或已发布链接）也记到
`.design-harness/config.json` 注册表里，跨会话重建时命中同一个文件 / 同一条链接。
SKILL.md 明确提示这一做法。

## 现状问题

- SKILL.md 已有"每次重建复用既有链接"的纪律，但链接/路径只存在于会话记忆里，
  换会话就丢。
- `record_workspace` 整体覆写 config：agent 手工记入的额外键会在重跑 bootstrap 时
  被静默抹掉（silent data loss）。

## 改动单元（每单元先测试后代码）

1. **docs 先行**：`docs/design-harness/output/file-structure.md` 注册表段落补一句
   ——注册表除工作区路径外，可记录画布交付位置；注册表仍非 truth。
2. **测试**：
   - `tests/test_discover_workspace.py`：`record_workspace` 保留 config 中已有的
     无关键（如 `canvas`），重跑 bootstrap 不丢。
   - `tests/test_plugin_manifests.py`：SKILL.md 必须把交付位置与 config 注册表
     关联起来（文本不变量）。
3. **代码**：`discover_workspace.record_workspace` 改为合并写入——读出既有合法
   config，只更新 `workspace` 键，其余键原样保留。
4. **SKILL.md**：工作流第 5 步交付段补提示——把交付位置记入注册表 `canvas` 键，
   后续会话重建同一文件、重发同一链接。
5. **版本**：两份 plugin.json 同步 bump 0.9.0 → 0.9.1，README release badge 跟进
   （既有测试强制对齐）。

## 验收

- 全量测试绿。
- 重跑 `init_workspace.py` 后 config 中手工记录的 `canvas` 键仍在。
