---
id: conflict-schema-red-edges
type: idea
tags: [schema]
---

# Conflicts get a schema: a `conflicts` field on the newer card, projected as red edges

The human's judgment (2026-07-14): unresolved conflicts between cards deserve a uniform, minimal
recording — prose annotations in indexes are agent discipline, not schema. The smallest mechanism:

- ideas frontmatter gains an optional `conflicts: [<id>]`, written **only on the newer card**
  (forward-only, acyclic — the same directionality discipline as references).
- The field lives exactly as long as the conflict: the human's adjudication removes it — archive
  the losing card and the edge vanishes with it; rewrite in place and the entry is deleted.
- The canvas draws conflict edges **red**: the builder tags the edge kind, the template base
  supplies the default color, every style pack inherits and may override — none needs touching.
- The validator checks every target id resolves; the index derives its pending-conflict
  annotation from the field, replacing hand-written prose.

Supersedes the exclusivity claim of
[references + tags, two kinds of facts](single-edge-single-tag.md): the structured-fact count
goes two → three (adjudicated by the human, 2026-07-14, by ordering this card into output).
