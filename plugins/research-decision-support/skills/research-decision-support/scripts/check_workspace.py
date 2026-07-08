import sys
from pathlib import Path

from build_map import card_files, parse_frontmatter

CONTRACTS = {
    "direction": {"required": ["id", "type"], "status": None},
    "idea": {"required": ["id", "type", "status"],
             "status": {"候选", "采纳", "存疑", "candidate", "adopted", "doubtful"}},
    "decision": {"required": ["id", "type", "status", "affects"],
                 "status": {"open", "resolved"}},
    "adr": {"required": ["id", "type", "status"],
            "status": {"proposed", "accepted", "superseded"}},
}


def check(workspace):
    workspace = Path(workspace).resolve()
    problems = []
    for md, rel in card_files(workspace):
        if rel.parts[0] == "sources":
            continue
        frontmatter = parse_frontmatter(md.read_text(encoding="utf-8"))
        card_type = frontmatter.get("type", "")
        contract = CONTRACTS.get(card_type)
        if contract is None:
            problems.append(f"{rel}: missing or unknown type: {card_type or '(none)'}")
            continue
        for field in contract["required"]:
            if not frontmatter.get(field):
                problems.append(f"{rel}: missing required field: {field}")
        status = frontmatter.get("status")
        if contract["status"] and status and status not in contract["status"]:
            allowed = " | ".join(sorted(contract["status"]))
            problems.append(f"{rel}: status '{status}' not in [{allowed}]")
    return problems


def main(argv):
    workspace = argv[1] if len(argv) > 1 else "docs/research-decision-support"
    problems = check(workspace)
    for problem in problems:
        print(f"INVALID {problem}")
    print(f"{'ok: all cards conform' if not problems else f'{len(problems)} problem(s)'}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
