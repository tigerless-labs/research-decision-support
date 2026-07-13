# 测试约定

- 框架 pytest，测试住 `tests/test_<module>.py`，fixture 在 `tests/conftest.py`（临时 workspace，
  不碰真实数据与外部服务）。
- 只断言关系与不变量（集合互补、计数对账、端点存在），不断言会随上游漂移的硬编码值。
- 每个生成器常驻对抗用例：卡片标题/正文注入 `</script>`、事件属性等，生成页必须以文本呈现。
- 运行：`python3 -m pytest tests -q`；提交前连同
  `python3 plugins/design-harness/skills/design-harness/scripts/check_doc_links.py docs/design-harness` 一起过。

## 测试地图

| 测试文件 | 覆盖 |
|---|---|
| tests/test_workspace_tools.py | 初始化器幂等 + 校验器契约（ideas 必填、单 tag、status 退役、引用向前无环、未知顶层目录、未闭合 frontmatter）+ tags 块列表解析 + 悬链检查 |
| tests/test_build_canvas.py | 收集器不变量（排除 archive/index、frontmatter tag、引用边、output 文档）+ 单文件自包含 + 注入防护 + 投影护栏（拒写工作区）+ 模板注册表 |
| tests/test_style_pack.py | 风格包校验器：索引↔目录双射、schema、色值白名单、禁外链红队用例、canvas_renderings 存在性+章节对应、画板模板 token 集与 schema 锁定、卡片 badge–标题间距不变量 |
| tests/test_plugin_manifests.py | 双 plugin manifest（Claude/Codex 布局）字段同步（name/version/description/license）+ README Codex 安装命令 |
| tests/test_readme.py | README 不变量：每风格至少一图、本地图片存在、点名全部风格、安装/用法章节、release 徽章版本 == plugin.json 版本 |

（v1 的测试随 skill v1 整体停放在 `archive/skill-v1/tests/`，不在根测试跑道上。）
