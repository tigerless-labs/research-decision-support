# conflict schema 代码落地 — `conflicts` 字段 + 画布红边

对应 idea 卡 `conflict-schema-red-edges`（2026-07-14 人已裁决）。docs 侧（中文 SKILL.md
第三事实、workspace output 各模块）已在主检出累积；本 PR 只落代码与测试。

## 单元

1. **workspace.py** — `parse_conflicts(frontmatter)`，与 `parse_tags` 同构（列表字段解析）。
2. **check_workspace.py** — `conflict_problems()`：存活 ideas 卡的 `conflicts` 每个条目
   必须解析到一张**存活** ideas 卡的 `id`；目标已归档 → 冲突已裁决、提示删条目；
   id 不存在 → 不可解析；指向自己 → 非法；ideas 之外出现该字段 → 非法。
   归档卡上的历史字段不校验（与画布排除口径一致）。
3. **build_canvas.py** — `collect()` 建立存活 ideas 的 id→路径映射，把 `conflicts`
   投影为 `{"from", "to", "kind": "conflict"}` 边；普通引用边不带 kind（向后兼容）。
   校验器是构建 gate，collect 内不重复报错。
4. **canvas/template.html** — 边几何抽成共用函数；冲突边**常驻绘制**（不同于按需引用边
   ——待裁决冲突必须一眼可见），描边 `var(--edge-conflict, #d0342c)`：模板兜底即基础层
   默认红，style pack 定义 `--edge-conflict` 即覆写；选中时邻边若为冲突边同样走红色。
   选中层与常驻层分离（清选不清冲突边）。

## 顺序

tests（test_workspace_tools + test_build_canvas 各新增用例，先红）→ 实现四个单元 →
全量 pytest → 用带冲突卡的临时 workspace 端到端构建、浏览器目检红边 → commit → PR
（不自动合并）。
