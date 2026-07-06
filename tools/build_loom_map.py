import json
import re
import sys
from pathlib import Path

LAYERS = ["sources", "synthesis", "ideas", "design", "decisions"]
_MD_LINK = re.compile(r"\]\(\s*([^)\s]+?\.md)(?:#[^)]*)?\s*\)")
_EXTERNAL = re.compile(r"^[a-z][a-z0-9+.-]*://")
_FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
_TITLE = re.compile(r"^#\s+(.+)$", re.MULTILINE)


def parse_frontmatter(text):
    match = _FRONTMATTER.match(text)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    return fields


def card_files(workspace):
    for md in sorted(workspace.rglob("*.md")):
        rel = md.relative_to(workspace)
        if rel.name == "index.md" or rel.parts[0] not in LAYERS:
            continue
        yield md, rel


def collect(workspace):
    workspace = workspace.resolve()
    nodes, edges = [], []
    known = {str(rel) for _, rel in card_files(workspace)}
    for md, rel in card_files(workspace):
        text = md.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(text)
        title_match = _TITLE.search(text)
        subtype = rel.parts[1] if rel.parts[0] == "sources" and len(rel.parts) > 2 else ""
        nodes.append({
            "id": str(rel),
            "layer": rel.parts[0],
            "subtype": subtype,
            "title": title_match.group(1).strip() if title_match else rel.stem,
            "status": frontmatter.get("status", ""),
        })
        for raw in _MD_LINK.findall(text):
            if _EXTERNAL.match(raw):
                continue
            target = (md.parent / raw).resolve()
            if not target.is_relative_to(workspace):
                continue
            target_rel = str(target.relative_to(workspace))
            if target_rel in known and target_rel != str(rel):
                edges.append({"from": str(rel), "to": target_rel})
    seen = set()
    unique_edges = [e for e in edges if (key := (e["from"], e["to"])) not in seen and not seen.add(key)]
    return {"nodes": nodes, "edges": unique_edges, "layers": LAYERS}


def build(workspace, output, title):
    data = collect(Path(workspace))
    data["title"] = title
    template = (Path(__file__).parent / "loom_map_template.html").read_text(encoding="utf-8")
    html = template.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False))
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    Path(output).write_text(html, encoding="utf-8")
    counts = {layer: sum(1 for n in data["nodes"] if n["layer"] == layer) for layer in LAYERS}
    print(f"ok: {output} — {len(data['nodes'])} cards, {len(data['edges'])} provenance links, {counts}")


def main(argv):
    if len(argv) < 2:
        print("usage: build_loom_map.py <workspace-dir> [-o output.html] [--title 'Page title']")
        return 1
    workspace = argv[1]
    output = argv[argv.index("-o") + 1] if "-o" in argv else "loom-map.html"
    title = argv[argv.index("--title") + 1] if "--title" in argv else Path(workspace).name
    build(workspace, output, title)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
