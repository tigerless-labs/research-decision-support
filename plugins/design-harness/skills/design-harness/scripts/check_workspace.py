import sys
from pathlib import Path

from discover_workspace import resolve_or_report
from workspace import (LAYERS, broken_frontmatter, card_files, card_links,
                       parse_conflicts, parse_frontmatter, parse_tags)

IDEA_REQUIRED = ["id", "type"]


def layout_problems(workspace):
    workspace = Path(workspace).resolve()
    problems = []
    for md in sorted(workspace.rglob("*.md")):
        rel = md.relative_to(workspace)
        if len(rel.parts) > 1 and rel.parts[0] not in LAYERS:
            problems.append(
                f"{rel}: unknown top-level dir — invisible to every projection; "
                f"move under one of: {', '.join(LAYERS)}")
    return problems


def schema_problems(workspace):
    problems = []
    for md, rel in card_files(workspace):
        text = md.read_text(encoding="utf-8")
        if broken_frontmatter(text):
            problems.append(
                f"{rel}: frontmatter opens but never closes — "
                "it will leak into the rendered body")
        frontmatter = parse_frontmatter(text)
        if len(parse_tags(frontmatter)) > 1:
            problems.append(f"{rel}: at most one tag per card — split the card")
        if rel.parts[0] != "ideas":
            continue
        for field in IDEA_REQUIRED:
            if not frontmatter.get(field):
                problems.append(f"{rel}: missing required field: {field}")
        if frontmatter.get("status"):
            problems.append(
                f"{rel}: retired field: status — two states only "
                "(existence = live, archive/ = archived)")
    return problems


def conflict_problems(workspace):
    cards = [(rel, parse_frontmatter(md.read_text(encoding="utf-8")))
             for md, rel in card_files(workspace)]
    idea_ids = {
        state: {fm.get("id") for rel, fm in cards
                if rel.parts[0] == "ideas" and ("archive" in rel.parts) == archived}
        for state, archived in (("live", False), ("archived", True))}
    problems = []
    for rel, fm in cards:
        conflicts = parse_conflicts(fm)
        if not conflicts:
            continue
        if rel.parts[0] != "ideas":
            problems.append(f"{rel}: conflicts is an ideas-only field — "
                            "only judgments contend")
            continue
        if "archive" in rel.parts:
            continue
        for target in conflicts:
            if target == fm.get("id"):
                problems.append(f"{rel}: conflicts with itself — remove the entry")
            elif target in idea_ids["archived"]:
                problems.append(
                    f"{rel}: conflict target {target} is archived — already "
                    "adjudicated, remove the entry")
            elif target not in idea_ids["live"]:
                problems.append(
                    f"{rel}: conflict target {target} resolves to no live idea card")
    return problems


def board_inbound_problems(workspace):
    workspace = Path(workspace).resolve()
    cards = {str(rel): md for md, rel in card_files(workspace)}
    problems = []
    for rel, md in cards.items():
        if rel.startswith("board/"):
            continue
        for target in card_links(md, rel, workspace, cards):
            if target.startswith("board/"):
                problems.append(
                    f"{rel}: references board/ — the board is terminal; distill its "
                    f"conclusions into an idea card instead ({target})")
    return problems


def cycle_problems(workspace):
    workspace = Path(workspace).resolve()
    cards = {str(rel): md for md, rel in card_files(workspace)}
    graph = {rel: sorted(set(card_links(md, rel, workspace, cards)))
             for rel, md in cards.items()}
    problems, done, stack, path = [], set(), set(), []

    def visit(node):
        if node in done:
            return
        stack.add(node)
        path.append(node)
        for target in graph[node]:
            if target == node:
                problems.append(f"reference cycle: {node} links itself")
            elif target in stack:
                loop = path[path.index(target):] + [target]
                problems.append(f"reference cycle: {' -> '.join(loop)}")
            else:
                visit(target)
        path.pop()
        stack.discard(node)
        done.add(node)

    for node in sorted(graph):
        visit(node)
    return problems


def check(workspace):
    workspace = Path(workspace).resolve()
    return (layout_problems(workspace) + schema_problems(workspace)
            + conflict_problems(workspace) + board_inbound_problems(workspace)
            + cycle_problems(workspace))


def main(argv):
    workspace = argv[1] if len(argv) > 1 else resolve_or_report(".")
    if workspace is None:
        return 1
    problems = check(workspace)
    for problem in problems:
        print(f"INVALID {problem}")
    print(f"{'ok: all cards conform' if not problems else f'{len(problems)} problem(s)'}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
