---
id: style-canvas-orthogonality
type: idea
tags: [画板]
---

# 风格与画布正交：style 纯 UI，canvas 定信息架构，绑定上收 skill

风格包只承载 UI——palette（抽象 accent 角色）、字型、几何、气质、呈现形态——不含任何
内容语义；canvas 模板独占信息架构与交互契约。内容层→accent 的绑定唯一写在 SKILL.md，
风格因此对任何内容成立、任意 canvas 通用。风格可为某个 canvas 附一节定制呈现（切换器
与卡片形态即风格签名），缺省走该 canvas 默认呈现；布局变体（竖标签/数字轨/命令行/
焦点卡/选关）只要信息架构不变就归风格，不立新 canvas。

2026-07-10 收敛（人裁）：画布归并为唯一的融合画布后，正交性退化为 token 接口约定——
styles/ 目录归于 canvas/ 之下、canvas_renderings 选择器退役，但"style 只写 token
与呈现、不触画布结构、整包可换"的分界不变。新 5 风格取材
[frontend-slides](../sources/github/frontend-slides.md) 预设与 Bold 包；规格化路数沿用
[一引擎多 schema](one-engine-many-schemas.md)，呈现挂在
[分页画廊模板](archive/tabbed-gallery-template.md) 之上。
