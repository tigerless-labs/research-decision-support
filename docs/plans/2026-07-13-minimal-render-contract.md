# 最小渲染契约：成文 + 解析适配 + 静默失败改报错

## 背景

脚本/HTML 正常显示所依赖的最小契约只隐含在 `workspace.py` 与 `build_canvas.py` 的行为里，
没有成文；同时存在三类静默失败：未知顶层目录整卡消失、坏 frontmatter 污染正文、
多行 YAML 列表格式的 tags 被静默当作无 tag。原则：硬规则收敛到最少，
能兜底的适配、会丢数据的报错。subtype 角标兜底已由 PR #24 完成，不在本计划内。

## 单元

1. **docs**：`references/protocol.md` 的 Card schema 一节重组为两层——渲染必需
   （engine 底线：目录名、UTF-8、frontmatter 合法或缺席）与方法论约束
   （单 tag、ideas 必填 id/type、引用前向禁环、board 终端）；写明静默失败改报错的行为承诺。
2. **tests → code：tags 多行适配**：`parse_frontmatter` 支持 YAML 块列表
   （`tags:` 换行 `- x`），规则消失、变为适配。
3. **tests → code：验证器新增两查**：`check_workspace.py` 报告
   (a) 未知顶层目录下的 md（数据静默丢失）；(b) 以 `---` 开头但无法闭合解析的
   frontmatter（内容污染）。
4. **验证**：pytest 全绿 + 对 `docs/research-decision-support` 实跑两个校验器 + 实跑
   `build_canvas.py` 确认画布正常。

## 验收

- protocol.md 两层结构成文，总长不增（精简换空间）。
- 多行 tags 卡片在画布上正确入团。
- 两类静默失败均输出 `INVALID` 且退出码非零。
