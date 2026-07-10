import json
import sys
from pathlib import Path

from workspace import (card_files, card_links, first_paragraph, parse_frontmatter,
                       parse_tags, strip_frontmatter, title_of)

SKILL_DIR = Path(__file__).resolve().parent.parent
VENDOR = Path(__file__).resolve().parent / "vendor"
TEMPLATES = {
    "tabbed-gallery": SKILL_DIR / "canvases" / "tabbed-gallery" / "template.html",
}
SUBTYPE_ZH = {"methods": "方法", "products": "产品", "github": "仓库",
              "blogs": "博客", "papers": "论文"}


def collect(workspace):
    workspace = Path(workspace).resolve()
    cards = {str(rel): md for md, rel in card_files(workspace, ["sources", "ideas"])
             if "archive" not in rel.parts}
    nodes, edges = [], []
    for rel, md in cards.items():
        text = md.read_text(encoding="utf-8")
        frontmatter = parse_frontmatter(text)
        parts = Path(rel).parts
        nodes.append({
            "id": rel,
            "layer": parts[0],
            "subtype": parts[1] if parts[0] == "sources" and len(parts) > 2 else "",
            "title": title_of(text, Path(rel).stem),
            "tags": parse_tags(frontmatter),
            "summary": first_paragraph(text),
            "body": strip_frontmatter(text).strip(),
        })
        for target in dict.fromkeys(card_links(md, rel, workspace, cards)):
            if target != rel:
                edges.append({"from": rel, "to": target})
    output_docs = {}
    for md in sorted((workspace / "output").rglob("*.md")):
        rel = md.relative_to(workspace)
        if rel.name != "index.md":
            output_docs[str(rel)] = md.read_text(encoding="utf-8")
    return {"nodes": nodes, "edges": edges, "output": output_docs,
            "subtypeZh": SUBTYPE_ZH}


def embed_json(data):
    return json.dumps(data, ensure_ascii=False).replace("<", "\\u003c")


def build(workspace, outdir, template, title=None):
    workspace = Path(workspace).resolve()
    outdir = Path(outdir).resolve()
    if outdir == workspace or outdir.is_relative_to(workspace):
        raise ValueError(
            f"refusing to write into the workspace: the canvas is a projection "
            f"and never enters the truth ({outdir})")
    if template not in TEMPLATES:
        raise ValueError(
            f"unknown template '{template}' — available: {', '.join(sorted(TEMPLATES))}")
    data = collect(workspace)
    needs_mermaid = any("```mermaid" in text for text in data["output"].values())
    html = (TEMPLATES[template].read_text(encoding="utf-8")
            .replace("<!--__TITLE__-->", title or workspace.name)
            .replace("/*__MARKED__*/", (VENDOR / "marked.min.js").read_text(encoding="utf-8"))
            .replace("/*__PURIFY__*/", (VENDOR / "purify.min.js").read_text(encoding="utf-8"))
            .replace("/*__MERMAID__*/",
                     (VENDOR / "mermaid.min.js").read_text(encoding="utf-8")
                     if needs_mermaid else "")
            .replace("/*__DATA__*/null", embed_json(data)))
    outdir.mkdir(parents=True, exist_ok=True)
    out = outdir / "canvas.html"
    out.write_text(html, encoding="utf-8")
    return out


def main(argv):
    if len(argv) < 2:
        print("usage: build_canvas.py <workspace> [-o outdir] "
              "[--template tabbed-gallery] [--title 'Page title']")
        return 1
    workspace = argv[1]
    outdir = argv[argv.index("-o") + 1] if "-o" in argv else "/tmp/rds-canvas"
    template = argv[argv.index("--template") + 1] if "--template" in argv else "tabbed-gallery"
    title = argv[argv.index("--title") + 1] if "--title" in argv else None
    out = build(workspace, outdir, template, title)
    data = collect(workspace)
    counts = {layer: sum(1 for n in data["nodes"] if n["layer"] == layer)
              for layer in ("sources", "ideas")}
    print(f"ok: {out} — {counts['sources']} sources, {counts['ideas']} ideas, "
          f"{len(data['edges'])} references, {len(data['output'])} output docs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
