# 计划：风格包 — skill 内置 agent 可读的视觉规格库

## 诊断

- 渲染层只有一套硬编码主题，散落三个模板重复三份；agent 渲染临时投影时没有可选型的
  视觉语言资产。
- 参照 zarazhangrui/frontend-slides 的已验证架构：风格 = 声明式规格文档（token 化
  design.md），三层渐进加载（索引 → 预览卡 → 完整规格）控制 token 消耗与选择疲劳。

## 决定

- **纯 agent 可读规格**：`build_site.py` 与三个 HTML 模板一行不改；风格包是平行资源，
  只服务 agent 手工渲染的临时投影。
- **完整三层渐进**：`styles/selection-index.json`（选型轴 + usage 策略块）→
  `<slug>/preview.md`（≤4KB 预览卡）→ `<slug>/design.md`（YAML frontmatter token 规格
  + 五节正文）；never-bulk-read 入协议。
- 每风格强制 `colors-light` + `colors-dark` 双主题、12 个 canonical token 与模板
  `:root` 语义槽一一对应；frontmatter 深度 ≤2，stdlib 严格解析，解析失败即非法。
- 首批四风格：loom-paper（默认主题迁移，测试锚定防漂移）、terminal-ledger（暗·正式·
  紧凑）、field-notes（亮·活泼·疏朗）、boardroom-slate（亮·正式·舒适）——每条选型轴
  ≥2 取值。
- 新增 `check_style_pack.py` 校验器（信任门）：索引↔目录双射、schema、色值白名单、
  全包禁外链、渐进经济性；红队测试全覆盖。
- 分发面英文：styles/ 内容与 SKILL.md 增补均为英文。

## 单元（docs → tests → code → verify → commit）

1. 本计划 + `docs/design/style-pack.md` 新增 + `workbench.md`「共享主题片段」调和 +
   `design/index.md`、`testing.md` 更新（docs 不入 git，本地维护）。
2. tests：合成 pack 工厂 + 红队用例（外链/script/expression/穿越/孤儿/重复 slug/深度
   3 frontmatter/缺 token/悬空别名/缺 usage 键 + 对照组）→ 实现 `check_style_pack.py`。
3. shipped-pack 测试（索引↔目录、双主题、loom-paper 锚定 site_template、preview <
   design、usage 齐全）→ 写索引 + loom-paper。
4. 轴区分力测试 → 创作三个新风格，每风格一个绿点。
5. SKILL.md `## Rendering` 接线：渐进选型协议 + never-bulk-read + 信任门。
6. 端到端：pytest 全绿、校验器 exit 0、build_site 回归（模板零 diff）、按协议人工
   选型一次并渲染投影目验明暗、push、PR、CI 绿。

## 验收

- 索引单独完成四轴 shortlist；一次完整选型最多读 索引 + 3 preview + 1 design.md。
- shipped pack 过校验器；每个红队破坏被点名到具体路径。
- loom-paper token 与 `site_template.html` 测试锚定；构建器与模板 diff 为零。
- SKILL.md 载有 never-bulk-read 协议。
