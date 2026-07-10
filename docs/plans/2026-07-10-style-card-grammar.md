# 风格包三卡文法（card grammar）落地

## 背景

融合画布下 8 个风格的 canvas.css 对三层卡片（note=sources / slip=ideas / kraft=output）
几乎只用 accent 颜色区分，形态雷同，视觉上"每个 style 几乎没有变化"。已定稿的两个预览
artifact（Single Canvas · 风格预览 7fad3bee、Tabbed Gallery · 定稿四款 14adb0d0）给出了
每个风格按层的独立卡片形态，本变更把它们落进风格包。

## 目标

每个风格的三层卡片必须是三种**形态**（结构、边框、底色处理、前缀符号等），不允许仅靠
accent 换色区分；同时保留双 palette、canonical token、模板选择器契约（template.html 一行不改）。

## 每风格三卡文法（源自 artifact）

| 风格 | note（sources） | slip（ideas） | kraft（output） |
|---|---|---|---|
| notebook-tabs | 索引卡：顶部彩色标签舌 | 便利贴：色纸+胶带、无边框 | 盖章文件：双线框、accent 章色 meta |
| swiss-modern | 白卡 2px 黑框 | 透明+底边线+圆点批注 | 实黑块白字、红 meta |
| terminal-green | 日志行：▸ 前缀、虚线底边 | diff 行：+ 前缀、左条+微 tint | 迷你终端窗：chrome 圆点 |
| bold-signal | 细描边半透明条 | 半透明色板、无边框 | 实色海报块黑字（已有） |
| 8-bit-orbit | 卡带砖：3px 框+硬影+角标 | 对话框:双重框+闪烁▮ | boss 关卡：霓光+★ |
| blue-professional | 4% tint 卡 | 顶栏卡：3px 钴蓝 border-top | 实钴蓝块奶油字 |
| block-frame | 青色块 | 粉色块（微旋） | 黄色块+绿圆徽章 |
| pin-and-paper | 别针便签（已有） | 墨蓝虚线贴纸 | 牛皮纸块+硬墨影 |

卡片旋转：手作类（notebook-tabs / pin-and-paper / block-frame）保留模板注入的微旋；
机器类（swiss-modern / terminal-green / blue-professional / bold-signal / 8-bit-orbit）
用 CSS 覆盖为 0。

## 单元

1. **docs**：8 个 design.md 增补/校订 `### single-canvas` 渲染节，selection-index.json 的
   canvas_renderings 补 `single-canvas`；本表为装配蓝图，权威落在各 design.md。
2. **tests**：tests/test_style_pack.py 新增不变量——每个 shipped canvas.css 中三层卡的规则
   在归一化 accent/tint 记号后必须两两不同（防"只换色"回归）。先红后绿。
3. **code**：重写 8 个 canvas.css 的层卡形态段（含 bird 档、sel/nb 兼容、reduced-motion 保留）。
4. **verify**：check_style_pack.py + pytest 全绿；build_canvas.py 重建融合画布，本地打开
   逐风格切换核验；artifact 同 URL 重发。
