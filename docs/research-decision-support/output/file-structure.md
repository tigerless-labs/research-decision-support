# 文件结构 — 设计→磁盘的映射

skill v2 的文件布局：两棵树——**skill 包**（可移植内核，随插件分发、只读）与
**工作区**（每项目一份、可写、不入 git）。分树即协议与运行时解耦：内核整体搬走
可复用，事实全部留在工作区。

## skill 包（内核）

```
plugins/research-decision-support/skills/research-decision-support/
├── SKILL.md              agent 模块的全部行为写成操作规程：触发条件、跑腿清单、
│                         就地教学的时机与回执话术（无驻留进程）
├── references/
│   ├── protocol.md       protocol 契约的人读版：卡 schema、引用+tag 两种事实、
│   │                     同步不变量、账本纪律
│   └── output-forms/     output 形态库（推荐集），一形态一规格
│       └── system-design.md   首款：mermaid 图（含 click 点穿）+ modules 层
├── templates/            卡骨架，一类一模板：source 卡 / idea 卡 / target / logs 头部
├── scripts/
│   ├── init_workspace.py     工作区自举（幂等，永不覆盖）
│   ├── check_workspace.py    schema 校验：frontmatter 必填、单 tag、引用向前且无环
│   ├── check_doc_links.py    链接完整性校验
│   ├── build_canvas.py       画板生成器（固定脚本）：工作区路径为唯一必填输入，读真身
│   │                         → 收卡/推边/布局/嵌数据一步到位的单文件 HTML；--css 换风格；
│   │                         只写临时目录或 artifact
│   ├── check_style_pack.py   风格包校验（schema、双 palette、禁外链、token 钉死默认模板）
│   ├── workspace.py          共享读卡器（frontmatter/tag/链接解析，三工具与生成器共用）
│   └── vendor/               离线渲染依赖（markdown/sanitize/mermaid，mermaid 按需嵌入）
└── canvas/               画布层：只有一种画布（融合画布），不设模板集目录——一层文件
    ├── spec.md               信息架构与交互契约（默认呈现）；契约见 modules/canvas
    ├── template.html         融合画布实现：结构 + 交互 JS，留 CSS 注入槽（已落地，
    │                         两张先行模板随之归档）
    ├── style.css             默认风格 CSS——换风格只换这一层（--css 传入即可）
    └── styles/               风格包：agent 可读的纯 UI 规格（palette/字型/几何/气质），
                              三层渐进、双 palette；内容无关，只依赖 token 接口
                              （目录迁挂 canvas/ 下待办）
```

- **规则与模板分离**：模板无关不变量（真身驱动、连线＝引用、布局派生）活在
  build_canvas 与 protocol 契约；canvas/ 只有形。
- **风格挂于画布之下、以 token 接口分界**：画布收敛为一种后，风格×画布正交退化
  为接口约定——style 只写 token 与呈现、不触画布结构，整包仍可互换；token 是抽象
  accent 角色，层→accent 的语义绑定唯一写在 SKILL.md 渲染段。canvas_renderings
  多画布选择器随模板集一并退役，style 的定制呈现节直接针对融合画布。
- **一份契约两种读法**：references/protocol.md 给人与 agent 读，check_workspace.py
  是其机器执行形——同源，改契约必改校验器。
- **形态库开放**：新增 output 形态＝往 output-forms/ 加一份规格，引擎不动
  （一引擎多 schema）。

## 工作区（真身）

```
docs/research-decision-support/
├── target.md             人对 output 的验收目标；output 形态之源
├── logs.md               append-only 变更账本——docs 不入 git，账本是回溯唯一依据
├── index.md              工作区总入口（派生）
├── sources/              ① 证据层：一源一卡；类型目录是薄壳，路径即类型
│   ├── index.md              派生：tag 小标题分组，未分类平铺末尾
│   └── <type>/*.md
├── ideas/                ② 判断层：只有人能创建
│   ├── index.md              派生
│   ├── archive/              归档态（二态之二），移入不删除
│   └── *.md
├── output/               ③ 整合层：人启动装配
│   ├── index.md              派生
│   └── …                     内部结构由 target 选中的形态规格决定；当前（系统设计）
│                             ＝ system.md 脊柱 + modules/ 一模块一文
└── board/                自由面：人自有版面，一文一板（对比或任意演算），无 schema；
    ├── index.md              最下游——可引三层取材，不可被引（派生 index 照常）
    └── *.md
```

各层 index 与画板 HTML 皆投影：随卡重生成，不持有事实、永不入库。

## 模块 → 文件映射

- source / idea / output → 工作区三层目录（行为边界见 [modules/](modules/source.md)）。
- canvas → build_canvas.py + canvas/（含 styles/）。
- agent → SKILL.md。
- protocol → references/protocol.md + templates/ + 两个校验器 + 工作区 logs.md。

**溯源**：[协议与运行时解耦](../ideas/runtime-agnostic-protocol.md) ·
[一引擎多 schema](../ideas/one-engine-many-schemas.md) ·
[投影不持有事实](../ideas/drafts-not-state.md) ·
[分页画廊模板](../ideas/archive/tabbed-gallery-template.md) ·
[单画布三团](../ideas/archive/single-canvas-clustered-graph.md) ·
[协议就地教学](../ideas/protocol-discoverability-in-situ.md) ·
[风格画布正交](../ideas/style-canvas-orthogonality.md)。
