# source 类型目录彻底自由化（去除预设映射）

## 目标

sources/ 的类型子目录不设任何预设集合：agent 收录时自选目录名（可新建），构建
脚本以实际目录名为准收录，画布卡片右上角角标直接投影目录名原文；无类型目录则
不显示，无所谓。

## 现状问题

- `build_canvas.py` 持有硬编码五项中文映射 `SUBTYPE_ZH`，模板角标经
  `DATA.subtypeZh[n.subtype] || ""` 渲染——映射之外的目录名角标落空，与
  protocol「path is the type」的自由语义矛盾。

## 单元（tests 先于 code）

1. **docs**：`docs/research-decision-support/output/modules/source.md` 补一句：类型目录名
   自由、agent 收录时自选，画布角标直接投影目录名。
2. **tests**：`tests/test_build_canvas.py`
   - collect：任意新目录名（非预设）成为 subtype 原文；
   - build：产物 HTML 不含 `subtypeZh`（映射彻底移除的不变量）。
3. **code**：
   - `scripts/build_canvas.py`：删除 `SUBTYPE_ZH` 及 payload/collect 中的
     `subtypeZh` 键；
   - `canvas/template.html`：角标改为直接用 `n.subtype`；
   - `SKILL.md`：sources 层说明补充——类型目录 agent 自选、目录名即画布角标。
4. **verify**：本地构建画布到临时目录，确认任意目录名卡片角标显示目录名原文。
5. **收尾**：commit → push → PR → CI 绿；workspace md 有改动，同回合重建
   画布 artifact（同 URL 重发）。
