# System diagrams — flow + architecture

## System flow diagram

```mermaid
flowchart TB
  subgraph HT["Human (creates and adjudicates)"]
    M["Drop in material<br/>zero threshold, any form"]
    A["Create / update idea<br/>only the human creates"]
    O["Initiate output assembly<br/>first assembly is human-initiated"]
    P["Edit output<br/>the primary work surface once generated"]
    R["Archive idea<br/>the other state; human or agent may trigger"]
  end
  subgraph GT["agent (runs the errands)"]
    B["Intake · grade<br/>sources are not equal-weight"]
    C["Derive references · tag classification<br/>fill in evidence anchors"]
    E["Assemble output<br/>re-derives affected elements on the human's word"]
    K["Back-calibrate ideas<br/>transcribes; the judgment stays the human's"]
    V["Move card to ideas/archive/<br/>logged, never deleted"]
    L["Write logs · regenerate each layer's index — every idea create/update / assembly / calibration / archival is ledgered alike"]
  end
  M --> B
  A --> C
  O --> E
  P -- "backward sync" --> K
  R --> V
  B -- "supports" --> C
  C -- "forward sync on command" --> E
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

## System architecture diagram

```mermaid
flowchart TB
    subgraph FLOW["The distillation flow"]
        SRC["① source — evidence layer<br/>one source one card · tag self-classification · graded at intake · claims anchored to origin"]
        IDEA["② idea — middle layer<br/>only the human creates · two states live/archived · append-only logs"]
        OUT["③ output — integration layer<br/>form set by target · elements link back to ideas and logs, then through to sources"]
        SRC --> IDEA
        IDEA <-->|"sync on the human's command: forward re-derive on order · backward calibrate automatic"| OUT
    end
    BOARD["board — free surface<br/>the human's own boards · one file, one board: comparisons or any scratch reasoning · no schema"]
    BOARD -.references the three layers forward only · conclusions distilled into ideas before entering the flow.-> FLOW
    subgraph XCUT["Cross-cutting"]
        CANVAS["canvas — board projection<br/>visualization layer only · sole active template: the unified canvas (single-canvas base + gallery strengths)"]
        AGENT["agent — execution engine<br/>thinks but never adjudicates · intake/link/anchor/back-calibrate/ledger/refresh"]
        PROTO["protocol — contract and ledger<br/>markdown as truth · three facts: references + tags + conflicts · logs · derived indexes"]
    end
    CANVAS -.projects.-> FLOW
    AGENT -.intake/link/anchor/ledger/refresh.-> FLOW
    PROTO -.schema/validation/logs/derived indexes.-> FLOW
    click SRC "modules/source.md"
    click IDEA "modules/idea.md"
    click OUT "modules/output.md"
    click BOARD "modules/board.md"
    click CANVAS "modules/canvas.md"
    click AGENT "modules/agent.md"
    click PROTO "modules/protocol.md"
```

Module details (one module, one doc): [source](modules/source.md) · [idea](modules/idea.md) ·
[output](modules/output.md) · [board](modules/board.md) · [canvas](modules/canvas.md) ·
[agent](modules/agent.md) · [protocol](modules/protocol.md).
