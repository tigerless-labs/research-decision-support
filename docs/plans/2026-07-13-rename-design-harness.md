# 项目改名：research-decision-support → design-harness

2026-07-13 用户拍板：项目定名 **design-harness**。取 "harness" 的缰绳隐喻（人握缰、agent 拉车），
蹭 harness-engineering 热词，与 autoharness 活例子成家族；接受 "design" 相对 "decision" 的射程收窄
（主战场就是调研→设计这条主流程）。GitHub 无同名占用。

## 改名面（全部）

1. **GitHub repo**：`tigerless-labs/research-decision-support` → `tigerless-labs/design-harness`
   （`gh repo rename`，旧 URL 自动跳转）；本地 remote URL 同步。
2. **目录**（git mv）：
   - `plugins/research-decision-support/` → `plugins/design-harness/`
   - `plugins/design-harness/skills/research-decision-support/` → `.../skills/design-harness/`
   - `docs/research-decision-support/` → `docs/design-harness/`
3. **双 plugin manifest**（tests 强制同步）：两个 `plugin.json` 的 name/homepage/repository/
   websiteURL/displayName；版本号两边一起 bump 到 0.7.0（破坏性改名）。
4. **双 marketplace 清单**：`.claude-plugin/marketplace.json`、`.agents/plugins/marketplace.json`
   的 name/displayName/source 路径。
5. **README**：标题、安装命令（marketplace add / plugin install / git clone / cp 路径）。
6. **CLAUDE.md**：标题与全部工作区路径引用。
7. **docs/ 全树**：`docs/index.md`、`docs/testing.md`、工作区五层内所有内链路径。
8. **tests/**：conftest 路径、manifest 断言、README 断言。
9. **skill 本体**：`SKILL.md` frontmatter name、scripts 内引用、`examples/autoharness/` 内引用。

## 不改

- `archive/skill-v1/`：历史快照，v1 当时就叫旧名，改了反而失真。
- 本地检出目录名 `~/tigerless_ai/research-decision-support`：会话进行中不能动，
  留给用户会后手动 `mv` + 重开会话。
- 旧 `docs/plans/` 里的历史计划文档：工作产物，保持原文。

## 顺序

tests 先改红 → git mv + 全库替换 → tests 绿 → repo 改名 → commit/push/PR → CI 绿。
