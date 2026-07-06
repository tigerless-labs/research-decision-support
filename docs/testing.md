# 测试约定

- 框架 pytest，测试住 `tests/test_<module>.py`，fixture 在 `tests/conftest.py`（临时 workspace，
  不碰真实数据与外部服务）。
- 只断言关系与不变量（集合互补、计数对账、端点存在），不断言会随上游漂移的硬编码值。
- 每个生成器常驻对抗用例：卡片标题/正文注入 `</script>`、事件属性等，生成页必须以文本呈现。
- 运行：`python3 -m pytest tests -q`；提交前连同 `python3 tools/check_doc_links.py docs` 一起过。

## 测试地图

| 测试文件 | 覆盖 |
|---|---|
| tests/test_build_loom_map.py | 收集器（卡片发现、边、摘要、frontmatter）+ map 页注入防护 |
| tests/test_build_loom_site.py | 方向聚合不变量、四页自包含、导航、注入防护 |
