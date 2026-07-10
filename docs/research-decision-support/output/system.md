# 系统图 — 流程 + 架构

## 系统流程图

```mermaid
flowchart TB
  subgraph HT["人（创建与裁量）"]
    M["丢入材料<br/>零门槛，任意形态"]
    A["创建 / 更新 idea<br/>只有人能创建"]
    O["启动装配 output<br/>首次由人启动"]
    P["修改 output<br/>生成后的主工作面"]
    R["归档 idea<br/>另一个状态，人与 agent 皆可触发"]
  end
  subgraph GT["agent（跑腿）"]
    B["收录 · 分级<br/>来源不等权"]
    C["推导连线 · tag 分类<br/>补证据锚点"]
    E["装配 output<br/>同回合刷新受影响元素"]
    K["反向校准 ideas<br/>代笔誊写，判断仍属人"]
    V["移卡入 ideas/archive/<br/>log 留痕，不删除"]
    L["记 logs · 重生成各层 index —— 每次 idea 创建与更新 / 装配 / 校准 / 归档同价留痕"]
  end
  M --> B
  A --> C
  O --> E
  P -- "反向同步" --> K
  R --> V
  B -- "支撑" --> C
  C -- "正向同步" --> E
  C --> L
  E --> L
  K --> L
  V --> L
  click M "modules/source.md"
  click B "modules/source.md"
  click A "modules/idea.md"
  click C "modules/idea.md"
  click R "modules/idea.md"
  click V "modules/idea.md"
  click K "modules/idea.md"
  click O "modules/output.md"
  click P "modules/output.md"
  click E "modules/output.md"
  click L "modules/protocol.md"
```

## 系统架构图

```mermaid
flowchart TB
    subgraph FLOW["提炼流"]
        SRC["① source 证据层<br/>一源一卡 · tag 自分类 · 入库即分级 · 主张锚定出处"]
        IDEA["② idea 中间层<br/>只有人能创建 · 存在/归档二态 · append-only logs"]
        OUT["③ output 整合层<br/>形态由 target 定 · 元素链回 idea 及 logs，再点穿 source"]
        SRC --> IDEA
        IDEA <-->|"永远双向同步：正向重推 / 反向校准 · 冲突以 output 为准"| OUT
    end
    BOARD["board 自由面<br/>人自有版面 · 一文一板：对比或任意演算 · 无 schema"]
    BOARD -.只向前引用三层取材 · 结论沉淀成 idea 才进提炼流.-> FLOW
    subgraph XCUT["横切"]
        CANVAS["canvas 画板投影<br/>只是可视化层 · 唯一现役模板：融合画布（单画布底盘+画廊优点）"]
        AGENT["agent 执行引擎<br/>思考不拍板 · 收录/连线/锚定/反校准/记账/刷新"]
        PROTO["protocol 协议与账本<br/>markdown 真身 · 引用+tag 两种事实 · logs · 派生 index"]
    end
    CANVAS -.投影.-> FLOW
    AGENT -.收录/连线/锚定/记账/刷新.-> FLOW
    PROTO -.schema/校验/logs/派生 index.-> FLOW
    click SRC "modules/source.md"
    click IDEA "modules/idea.md"
    click OUT "modules/output.md"
    click BOARD "modules/board.md"
    click CANVAS "modules/canvas.md"
    click AGENT "modules/agent.md"
    click PROTO "modules/protocol.md"
```

模块细节（一模块一文）：[source](modules/source.md) · [idea](modules/idea.md) ·
[output](modules/output.md) · [board](modules/board.md) · [canvas](modules/canvas.md) ·
[agent](modules/agent.md) · [protocol](modules/protocol.md)。
