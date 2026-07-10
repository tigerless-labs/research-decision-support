import sys
from pathlib import Path

SKELETON = {
    "index.md": (
        "# research-decision-support workspace\n\n"
        "- [sources/](sources/index.md) — ① 证据：一源一卡，agent 收录并分级\n"
        "- [ideas/](ideas/index.md) — ② 判断：只有人能创建；归档卡入 archive/\n"
        "- [output/](output/index.md) — ③ 装配：由人启动，形态由 target 决定\n"
        "- [target.md](target.md) — output 的验收目标\n"
        "- [logs.md](logs.md) — append-only 变更账本，回溯的唯一依据\n"
    ),
    "target.md": (
        "# target — output 的验收目标\n\n"
        "人对 output 的要求在此登记；output 是对本清单的履行，每条要求可核对。\n"
        "要求变更时 agent 同回合重推 output 受影响部分。\n\n"
        "## 主旨\n\n## 当前要求\n\n## 履行对照\n"
    ),
    "logs.md": (
        "# logs — append-only 变更账本（覆盖 ideas 与 output 两层）\n\n"
        "约定：每行 `- 日期 · 卡/文档 · 动作 · 改动（旧 → 新 的最小 delta）· 原因`；\n"
        "必须记**改动本身**；有 output 后同一变更每层各记一条；只追加，永不改写旧行。\n"
    ),
    "sources/index.md": "# sources — 证据卡（tag 小标题分组，投影随卡重生成）\n",
    "ideas/index.md": "# ideas — 人创建，二态（存在 / 归档）\n",
    "output/index.md": "# output — 装配产物（形态由 target 决定）\n",
}


def init(workspace):
    workspace = Path(workspace)
    created = []
    for rel, content in SKELETON.items():
        target = workspace / rel
        if target.exists():
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        created.append(rel)
    (workspace / "ideas" / "archive").mkdir(parents=True, exist_ok=True)
    return created


def main(argv):
    workspace = argv[1] if len(argv) > 1 else "docs/research-decision-support"
    created = init(workspace)
    if created:
        print(f"ok: initialized {workspace} — created {', '.join(created)}")
    else:
        print(f"ok: {workspace} already complete, nothing touched")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
