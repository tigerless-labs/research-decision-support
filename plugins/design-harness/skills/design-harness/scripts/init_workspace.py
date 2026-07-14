import sys
from pathlib import Path

from check_doc_links import main as check_doc_links_main
from check_workspace import main as check_workspace_main
from discover_workspace import DEFAULT_LOCATION, discover, record_workspace

SKELETON = {
    "index.md": (
        "# design-harness workspace\n\n"
        "- [sources/](sources/index.md) — ① evidence: one source, one card; the agent files and grades\n"
        "- [ideas/](ideas/index.md) — ② judgment: only the human creates; archived cards go to archive/\n"
        "- [output/](output/index.md) — ③ assembly: human-initiated, form set by target\n"
        "- [target.md](target.md) — acceptance criteria for output\n"
        "- [logs.md](logs.md) — append-only change ledger, the only way back\n"
    ),
    "target.md": (
        "# target — acceptance criteria for output\n\n"
        "The human's requirements for output are registered here; output fulfils this list,\n"
        "and every requirement is checkable. When a requirement changes, the agent re-derives\n"
        "the affected parts of output in the same turn.\n\n"
        "## Purpose\n\n## Current requirements\n\n## Fulfilment map\n"
    ),
    "logs.md": (
        "# logs — append-only change ledger (covers both the ideas and output layers)\n\n"
        "Convention: each line is `- date · card/doc · action · delta (minimal old → new) · reason`;\n"
        "record the **delta itself**; once output exists, one line per layer per change;\n"
        "append only, never rewrite old lines.\n"
    ),
    "sources/index.md": "# sources — evidence cards (grouped under tag headings; projection regenerated with the cards)\n",
    "ideas/index.md": "# ideas — human-created, two states (live / archived)\n",
    "output/index.md": "# output — assembled artifacts (form set by target)\n",
    "board/index.md": (
        "# board — free surface (one file, one board; the human's own)\n\n"
        "Each md is a board: a comparison set or any scratch reasoning, no schema. Boards may\n"
        "reference the three layers for material; the layers never reference a board — a\n"
        "board's conclusion is distilled into an idea card before it enters the flow.\n"
    ),
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
    if len(argv) > 1:
        workspace = Path(argv[1])
    else:
        found = discover(".")
        if len(found) > 1:
            print(f"{len(found)} candidate workspaces — pass one explicitly:")
            for candidate in found:
                print(f"  {candidate}")
            return 1
        workspace = found[0] if found else DEFAULT_LOCATION
    created = init(workspace)
    record_workspace(".", workspace)
    if created:
        print(f"ok: initialized {workspace} — created {', '.join(created)}")
    else:
        print(f"ok: {workspace} already complete, nothing touched")
    verdicts = [check_workspace_main([argv[0], str(workspace)]),
                check_doc_links_main([argv[0], str(workspace)])]
    return 1 if any(verdicts) else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
