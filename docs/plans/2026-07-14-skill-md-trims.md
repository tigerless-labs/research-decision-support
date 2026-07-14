# SKILL.md 瘦身 — 四处按人工评审意见修剪

用户逐段评审 SKILL.md（中文译本）提出的修改，落回英文原版：

1. 投影句收窄：「其余一切表面……永不提交入库」→ 只说画布 HTML，"一般不提交入库"
   （dogfood 仓库的 workspace 索引本就入库，原句与事实不符）。file-structure.md
   里同一事实的句子同步软化。
2. board 段删去终点句（"任何东西不得引用板……蒸馏成 idea 卡"）——该规则仍由
   protocol.md 承载、check_workspace 强制执行，SKILL.md 里属重复。
3. Getting started 删去"写入后手动跑两个校验器"的命令块——init 与 canvas 构建
   均已内置双校验（PR #59、#61），真相一变即同回合重建，gate 全覆盖。
4. 画布章节去冗余：风格由人在画布右上角拉选框自选，agent 只需提示一次；
   删去 AI 选风格指引（selection-index.json 段），保留 --css 锁定、design.md→
   重编译纪律、构建/交付/链接复用的独有事实。

版本 0.8.3 → 0.8.4（双 manifest + README 徽章）。纯行为文案变更，无新代码，
现有测试套件守住 manifest/badge 不变量。
