import sys
from pathlib import Path

from workspace import card_files, card_links, parse_frontmatter, parse_tags

IDEA_REQUIRED = ["id", "type"]


def schema_problems(workspace):
    problems = []
    for md, rel in card_files(workspace):
        frontmatter = parse_frontmatter(md.read_text(encoding="utf-8"))
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
    return (schema_problems(workspace) + board_inbound_problems(workspace)
            + cycle_problems(workspace))


def main(argv):
    workspace = argv[1] if len(argv) > 1 else "docs/research-decision-support"
    problems = check(workspace)
    for problem in problems:
        print(f"INVALID {problem}")
    print(f"{'ok: all cards conform' if not problems else f'{len(problems)} problem(s)'}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
