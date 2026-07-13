# README 视觉化重写（对齐 frontend-slides 配方）

## 目标

根 README 从论文式叙事改为分发页：一段 pitch → 短 bullets → 安装 → 用法 → 风格画廊（图片主导）→ 一句话哲学。全英文。参考 zarazhangrui/frontend-slides 的结构。

## 单元

1. **截图脚本** `scripts/capture_style_gallery.py`：对 dogfood 工作区 build 画布，
   Playwright 无头逐风格截图（统一 viewport 与 close tier；8-Bit Orbit 用暗色模拟），
   输出到 `docs/assets/canvas-styles/`。风格包变更时同回合重跑。
2. **测试先行** `tests/test_readme.py`：README 引用的本地图片文件必须存在；
   五个在售风格名必须都出现在 README 中（与 selection-index.json 对齐，不硬编码数量）。
3. **README 重写**：新结构见上；砍掉开头长文、FAQ、v1/v2 编年史（v1 压成一行归档链接）。
4. **验证**：pytest 全绿；逐张 Read 截图确认可读性。

## 不做

- 插件目录 README（marketplace 单插件，无读者）。
- workspace output 文档无需改动——README 是分发资产，不承载设计事实。
