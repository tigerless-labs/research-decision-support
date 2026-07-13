# target — acceptance criteria for the output

The human's requirements for the output are registered here; the output is the fulfilment of this
list, and every requirement is checkable. When a requirement changes, the agent re-pushes the
affected parts of the output in the same turn (the same discipline as
[output-auto-refresh](ideas/output-auto-refresh.md): both idea changes and target changes are
refresh triggers).

## Purpose

Design a **thought-clarifier / decision board**: turn historically validated thinking methods into
scenario-organized decision support, with the core thesis that **decision authority stays with the
human — AI lays out the options and evidence to help the human decide fast** (the human
adjudicates, the agent runs the errands). The main battlefield is research-based decisions
(evidence-based): technology selection, literature review, due diligence, competitive analysis —
decisions must stand on traceable evidence; intuitive, political, and pure-preference decisions
are out of scope. Unlike peer projects that treat mental models as AI reasoning lenses, we deliver
a stateful decision protocol whose product is the human's choice plus reasoning — versioned,
traceable, measured by decision speed and traceability rather than AI accuracy.

## Current requirements (2026-07-09)

The output must include:

- One **system flow diagram** (swimlanes split human/agent, pure logic with no UI) and one
  **system architecture diagram** (six modules, no detail in the diagram) — **living in one
  markdown file and drawn on one page**;
- **One detail md under output/modules/ for each module**;
- **The canvas board is only a visualization layer** — it changes with the markdown truth and
  holds no facts of its own;
- **The skill's file-structure design** — the complete layout of the skill package and the
  workspace, resolved into a directly implementable tree.

## Fulfilment map

- System flow diagram + system architecture diagram → [output/system.md](output/system.md)
  (rendered on the same HTML page)
- Module details → [output/modules/](output/modules/source.md) (source / idea / output /
  canvas / agent / protocol)
- Canvas visualization-layer constraint → [output/modules/canvas.md](output/modules/canvas.md)
- Skill file structure → [output/file-structure.md](output/file-structure.md)
