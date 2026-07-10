# 画布卡片：右上角 badge 与标题重叠修复

## 问题

模板把 badge（子类型 + 首个 tag）绝对定位在卡片右上角，标题从卡片顶部内边距起排。
八个风格包一致存在：长标题的第一行与 badge 处于同一水平带，产生重叠。

## 方案

模板中 badge 先于标题插入 DOM，故用相邻兄弟选择器只对带 badge 的卡片把标题下移：
每个风格的 `canvas.css` 增加一条 `.card .badge + .t` 规则，给出正的顶部间距，
让标题首行落在 badge 之下；无 badge 的卡片不受影响。

## 单元

1. 测试先行：`tests/test_style_pack.py` 增加不变量测试——每个入库风格的
   `canvas.css` 必须含 badge 后继标题的间距规则，且间距值为正。
2. 八个风格的 `canvas.css` 各加一条规则使测试通过。
3. 端到端验证：用 `build_canvas.py` 构建示例工作区，截图确认长标题卡片
   标题与 badge 不再重叠。

## 不改的

- `template.html` 结构与 `build_canvas.py` 不动。
- design.md 规格不动——像素级间距属实现细节，唯一权威在 CSS。
