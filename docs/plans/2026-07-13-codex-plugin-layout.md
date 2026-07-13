# Codex plugin 布局 — 让 skill 在 Codex（CLI + ChatGPT 桌面 app）可安装

## 背景

Codex 自 2025-12 起原生支持 Agent Skills（同一 SKILL.md 标准），并有自己的 plugin
分发机制：清单 `.codex-plugin/plugin.json`（必需）、市场索引
`.agents/plugins/marketplace.json`（官方同时支持 legacy 路径
`.claude-plugin/marketplace.json`）。CLI 与桌面 app 共用同一 `CODEX_HOME`，适配一次
两端生效。依据：[Build plugins](https://learn.chatgpt.com/docs/build-plugins)、
[Build skills](https://learn.chatgpt.com/docs/build-skills)。

## 目标

Codex 用户一条 `codex plugin marketplace add tigerless-labs/design-harness`
（或桌面 app 加市场源）即可安装本 skill；Claude Code 路径零回归。

## 单元

1. **README（docs 先行）**：Installation 增加 Codex 小节（marketplace add + 桌面 app
   路径；保留现有 copy-folder 兜底）。
2. **测试先行**：新增 `tests/test_plugin_manifests.py` —— 双清单同步不变量
   （`.claude-plugin/plugin.json` 与 `.codex-plugin/plugin.json` 的
   name/version/description/author/license 一致；`skills` 指针指向真实存在的
   SKILL.md 目录；两份 marketplace 索引的 plugin 名与 source 路径可解析）；
   README 安装命令断言补 Codex 行。
3. **代码**：
   - `plugins/design-harness/.codex-plugin/plugin.json`（字段自现有
     plugin.json 映射 + `"skills": "./skills/"` + `interface` 展示元数据）。
   - 仓库根 `.agents/plugins/marketplace.json`（新格式：`source.source=local`、
     `policy.installation=AVAILABLE`、`policy.authentication=ON_INSTALL`、
     `category`）。
   - SKILL.md 命令行去 Claude 专属：`${CLAUDE_SKILL_DIR}` 改为"相对本 skill 目录"
     的中性写法；`allowed-tools` frontmatter 保留（Claude 专属元数据，他端忽略）。
4. **验证**：全量 pytest；本地按 Codex 目录约定放置 skill 验证可被发现（结构核对）。

## 边界

- 不做 `agents/openai.yaml`（方案3，锦上添花，另立任务）。
- 不改 skill 协议本体与 canvas/styles。
- 版本号双清单必须同步 —— 由不变量测试强制。
