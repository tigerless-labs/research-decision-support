# output form: system-design

**For targets like**: project development, paper/system design — anything whose deliverable
is an architecture plus the reasons behind it.

## Shape

```
output/
├── index.md          entry point (projection)
├── system.md         the spine: system flowchart + architecture diagram in ONE document
└── modules/*.md      one module, one file — the diagram's blocks click through to these
```

## Rules

- `system.md` contains exactly two mermaid blocks — a **flowchart** (swimlanes split
  human / agent, pure logic, no UI) and an **architecture diagram** (modules with one-line
  sublabels via `<br/>`, details stay out of the diagram). The diagrams **are** the
  document: no prose restating what a node already says.
- Every diagram block carries a `click` declaration to its module file — the diagram→module
  mapping lives in the markdown, not in any projection.
- Each `modules/*.md` states the module's responsibility and its behavior boundary as
  **bullets** (one principle per bullet), then a provenance line linking the ideas and
  sources it stands on.
- Every element links back to the idea that assembled it (and through the ledger to its
  sources) — that chain is the product.
