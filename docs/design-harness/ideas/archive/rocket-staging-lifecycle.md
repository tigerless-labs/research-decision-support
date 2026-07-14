---
id: rocket-staging-lifecycle
type: idea
tags: [sync]
---

# Rocket-staging lifecycle: the system has a single operation -- ignition

Every output change is one **re-ignition**; ignition automatically separates the stage: once
assembly completes, all current ideas are archived (`ideas/archive/`), their judgments and
references **consolidated and inherited** by output, with no hot reloading afterwards --
[two-way sync](../output-primary-after-generation.md) and
[hot refresh](output-auto-refresh.md) are superseded by this card. If output exists,
ignition updates it (assembly input = current output + target + new ideas on the work surface,
which may be zero cards -- a pure format change just registers in target); if not, ignition
creates it. **Completeness obligation**: every exist-state card must be either inherited or
explicitly discarded by the human; the agent must never drop one silently, and the ignition
receipt reports uninherited items and weak spots (non-blocking). **Traceability**: the logs
record the ignition line (round, list of archived cards, per-card-to-output-element inheritance
mapping), and output anchors click through in reverse. Sources stay resident and are never
archived (retraction goes through downgrade); reconsideration means opening new ideas and
running a new ignition, and archived cards never thaw. Mission boundary: drive output into
existence and stop at delivery -- separate from the programming workflow; the code agent does
not reference this workspace design.

Why auto-archiving is sound: archiving is non-destructive and correction is cheap (read the
archive, open a new card, ignite again), an optimistic-commit model. The evidence
overwhelmingly supports separation: [ADR](../../sources/methods/adr-method.md) accepted means
immutable; the [decision journal](../../sources/methods/decision-journal.md) seals entries
against after-the-fact polishing; [Shape Up](../../sources/methods/shape-up.md) pitches do not
revive after ship; [GTD](../../sources/methods/gtd.md) requires the work surface to be
emptied; [Zettelkasten](../../sources/methods/zettelkasten.md) fleeting notes are discarded
after use; [HDD](../../sources/methods/hdd.md) closes a hypothesis once its loop closes; the
updates of the [EBM living review](../../sources/methods/ebm-grade.md) are in substance
re-ignitions; [IBIS](../../sources/methods/ibis-qoc.md) is the counterproof that living
intermediate layers die of maintenance cost.
