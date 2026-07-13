# research-decision-support

## 定位

把经过历史验证的思维方法做成按场景组织的决策辅助 skill 家族，本仓库是第一个。核心命题：**决策权在人——AI 铺开选项和证据，帮人
快速拍板**（人拍板、agent 跑腿）。主战场是**基于调研的决策**（evidence-based）：选型、
文献综述、尽调、竞品分析——决策必须站在可溯源的证据上；直觉型、政治型、纯偏好型决策
不在射程内。与把思维模型当 AI 推理透镜的同类项目不同，我们交付有状态的决策协议，产出
是人的选择加理由——版本化、留痕可溯，以决策速度和可追溯性衡量，而非 AI 准确率。

仓库以分发为先：README 钩子和活例子（`examples/autoharness/`）为传播性优化。生成的
HTML 是用完即弃的投影——只构建到临时目录或 artifact，永不入库。

## Key docs (read before changing the relevant area)

- **[docs/](docs/index.md)** — documentation map; single entry point for the whole `docs/` tree.
- **[docs/research-decision-support/output/](docs/research-decision-support/output/index.md)** — the assembled output (currently: the system design — architecture and the *why*). Start at the spine,
  then the step you're touching. *(Create these as the design solidifies; keep the index current.)*
- **[docs/research-decision-support/](docs/research-decision-support/index.md)** — the literature→design workspace: every
  cited source, its synthesis into directions, distilled ideas, design assembly, and decisions, in
  five provenance-linked layers (`sources/` `synthesis/` `ideas/` `design/` `decisions/`). The
  operating procedure is carried by the global **`research-decision-support` skill** — invoke it whenever you
  add a source, compare a direction, or push literature toward design.
- **[docs/TODO.md](docs/TODO.md)** — tracked follow-ups not yet on the roadmap.
  **Keep this current in real time** (see rule below).
- **[docs/testing.md](docs/testing.md)** — test conventions and the per-file test map.
- **[docs/plans/](docs/plans/)** — per-change implementation plans (working artifacts, exempt from the design-doc style rules).

## Task lifecycle — the fixed order for every non-trivial change

Plan → sync → docs → tests → code → verify → commit → docs/index sweep → green CI.
Trivial one-line changes skip the plan; nothing skips the order. A change that arrives
out of order is *incomplete*.

1. **Plan.** Non-trivial changes start with a plan in `docs/plans/` (working artifacts,
   exempt from the design-doc style rules). The plan's first unit updates the relevant
   workspace `output/` doc; every unit places tests before code.
2. **Branch, isolate, sync.** Bind each change to exactly one explicit task on its own branch,
   developed in its own worktree — **created with Claude Code's own worktree tooling** (the
   `/ce-worktree` skill or the built-in worktree feature), which places it under
   `.claude/worktrees/<branch>` (`.claude/` is git-ignored); never hand-create one with raw
   `git worktree add`, and never develop on the default/trunk branch (`main`/`master`/`trunk`,
   or whatever the repo's current default branch is). Before developing, `git fetch` and rebase
   that branch onto the latest `main` so you build on the current baseline, never a stale one.
   Land the work via feature branch + PR; no direct pushes to `main`.
3. **Docs first.** Read, then update, the relevant workspace `output/` doc(s) before any test or
   code — pin down behavior boundaries, interface contracts, and acceptance criteria. Never
   touch code first.
4. **Tests next (TDD).** Write the failing unit test(s) first, then the system test(s), then
   the implementation. Put each in the matching `tests/test_<module>.py`, use fixtures rather
   than live external services, and assert **relationships/invariants** (sums reconcile,
   A > B, value `> 0`) — never hardcoded values that break when an upstream dependency
   changes. A feature shipped without a test is *incomplete*.
5. **Code.** Write the code that makes the tests pass.
6. **Verify end-to-end.** Run the app on a local server and confirm the behavior end-to-end
   against a running instance — not just via unit tests.
7. **Commit.** Run the relevant unit *and* system tests before each commit; commit at every
   green-test point (the natural TDD commit moments) and `git push` after every completed task
   and at every phase gate — progress must never exist only on this machine.
8. **Sweep docs & indexes.** Confirm whether the change needs updates to the design docs and
   the doc/file-tree indexes (`docs/research-decision-support/output/index.md`) — update them in the same change.
9. **Drive CI green.** After opening the PR, watch CI and code-quality checks (CI runs, lint,
   static analysis, doc-automation checks). On any failure, locate, fix, and push immediately
   — repeat until every required check passes.

## Working rules

- **Docs are top-level design only.** Describe *what* a piece does and *why* — never how. No
  pseudocode, no code snippets, no concrete data, values, or magic numbers. Name **modules and
  objects** — never functions, constants, ratios, or file paths; that detail lives in the code.
  Two carve-outs: **architecture diagrams** are legitimate top-level design and stay; and the
  **setup runbooks** (install, quickstart, ops) keep the literal commands a user runs, since
  the command *is* the deliverable there — but their prose still obeys the no-implementation
  rule.
- **Design docs are ruthlessly concise — every sentence earns its place.** No filler, no
  hedging, no motivational preamble, no restating what the code, a diagram, or another doc
  already says. One fact lives in exactly one place; cross-link instead of repeating. If a
  sentence adds no distinct design fact, cut it. When you edit a doc, leave it shorter than
  you found it unless you added a genuinely new idea.
- **workspace `output/` and `docs/plans/` are written in Chinese.** Every doc under those two trees
  must be in Chinese prose. Keep proper nouns, code, identifiers, links, and command runbooks
  as-is — only the prose is Chinese.
- **Commits and PRs are written in English.** Commit messages, branch names, and PR
  titles/bodies are English only — no Chinese in git history.
- **Clear code, no comments.** Code must read clearly on its own — prefer explicit, unambiguous
  names with underscores, and carry intent through structure, naming, tests, and docs. Write no
  comments; if one feels necessary, rename or split until it isn't.
- **Decouple — one functional block, one object, one file. Never duplicate.** Every functional
  block is its own object in its own file. Never write the same functionality twice (DRY) —
  extract the shared piece and reuse it.
- **One authoritative source per fact.** A concept or piece of logic has exactly one home:
  **docs** carry intent, boundaries, constraints, and the reasons for decisions; **code** is the
  sole authority for implementation; **data** lives in the data layer and is the sole authority
  for facts. Never let the same thing live in two of them — cross-reference instead.
- **Config holds every knob.** Tunable parameters, environment differences, and policy/feature
  switches live in config — never hardcoded or scattered across the code.
- **Real-time TODO**: when you discover a follow-up, a gap, or defer something, write it into
  `docs/TODO.md` immediately (don't leave it only in chat). When you finish a TODO,
  remove or check it off. Roadmap-level items go in the design docs; smaller/uncommitted ones
  in `docs/TODO.md`.
- **Research goes to `research-decision-support/` in real time.** Every new paper or repo you cite or rely
  on must be summarized into [`docs/research-decision-support/`](docs/research-decision-support/index.md) — one source,
  one card (arXiv / date / authors + core logic + relevance to the project), filed under the
  sources layer by type (`sources/papers/`, `sources/github/`, `sources/blogs/`, …) and added to
  its index. Never leave a cited source only in chat.
- **Verify empirical claims by experiment before asserting** — measurements live under
  `experiments/`, and the invariant or doc that rests on them links back as `evidence:`.

## Security — agents run autonomously, so the system must fail safe

- **Trust nothing by default.** Treat external input, upstream responses, and agent decisions as
  hostile. The **core layer** especially validates input, checks bounds, rejects illegal state,
  and fails safe on error (fail-safe, deny by default).
- **Least privilege.** Default to least privilege and deny by default. Secrets and raw PII never
  enter the repo, ordinary logs, or ordinary traces.
- **Guardrails at every chokepoint.** Place guardrails at agent input/output, tool/skill calls,
  cross-module calls, external communication, destructive actions, and permission decisions — so
  an autonomously running agent cannot harm the system, the data, or users. High-risk paths must
  be able to allow / deny / redact / degrade / escalate / hand to human review.
- **Red-team the tests.** Both unit and system tests carry adversarial cases — privilege
  escalation, injection, guardrail bypass, cross-tenant leakage, dangerous tool calls, and
  failure injection — proving the system fails safe under malicious or abnormal input.
