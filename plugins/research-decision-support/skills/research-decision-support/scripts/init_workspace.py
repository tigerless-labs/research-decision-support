import sys
from pathlib import Path

LAYERS = ["sources", "synthesis", "ideas", "decisions"]

INDEXES = {
    "index.md": (
        "# research-decision-support workspace\n\n"
        "- [sources/](sources/index.md) — what the material says, one card per source\n"
        "- [synthesis/](synthesis/index.md) — sources clustered into directions, my verdict\n"
        "- [ideas/](ideas/index.md) — my claims, atomic, each citing its sources\n"
        "- [decisions/](decisions/index.md) — contested points: worksheet → ADR\n"
    ),
    "sources/index.md": "# sources — one card per source, facts only\n",
    "synthesis/index.md": "# synthesis — directions with concept matrices\n",
    "ideas/index.md": "# ideas — my claims in my words\n",
    "decisions/index.md": "# decisions — worksheets (open) and ADRs (append-only)\n",
}


def init(workspace):
    workspace = Path(workspace)
    created = []
    for rel, content in INDEXES.items():
        target = workspace / rel
        if target.exists():
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")
        created.append(rel)
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
