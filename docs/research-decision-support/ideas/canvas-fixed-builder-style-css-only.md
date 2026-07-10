---
id: canvas-fixed-builder-style-css-only
type: idea
tags: [画板]
---

# 画布构建收敛为一个固定脚本：工作区路径是唯一必填输入，换风格只换 CSS

[融合画布](single-canvas-subsumes-gallery.md)的构建方式定形为**一个固定脚本**
（`build_canvas.py`）：agent 输入工作区路径即渲染出完整画布 HTML，收卡、连线、
布局、嵌数据全部内建，不存在第二条构建路径。模板（结构 + 交互 JS）与风格
（CSS）分离——模板留一个 CSS 注入槽，默认灌当前风格；换风格**只换 CSS 文件**
（`--css` 传入），禁止为观感另开模板或另写脚本。

动机：融合版 UI 曾只活在临时目录与 artifact 里，重发一次靠手工拼接数据，
schema 不合即整页空白（2026-07-10 踩过）；固定脚本让"md 改动 → 同回合重建
发布"退化为一条命令，风格包则经由 CSS 槽继续整包可换
（[风格与画布正交](style-canvas-orthogonality.md)）。
