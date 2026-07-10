import json
import math
import re
import sys
from pathlib import Path

from workspace import (card_files, card_links, first_paragraph, parse_frontmatter,
                       parse_tags, strip_frontmatter, title_of)

SKILL_DIR = Path(__file__).resolve().parent.parent
VENDOR = Path(__file__).resolve().parent / "vendor"
TEMPLATE = SKILL_DIR / "canvas" / "template.html"
DEFAULT_STYLE = "pin-and-paper"
DEFAULT_CSS = SKILL_DIR / "styles" / DEFAULT_STYLE / "canvas.css"
SUBTYPE_ZH = {"methods": "方法", "products": "产品", "github": "仓库",
              "blogs": "博客", "papers": "论文"}

CW, CH, DH = 252, 150, 116
GX, GY, PAD, HEAD = 20, 20, 16, 52
ROW_MAX, WORLD_GAP, WORLD_TITLE_Y = 1780, 420, -230


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
    def docs_of(layer):
        docs = {}
        for md in sorted((workspace / layer).rglob("*.md")):
            rel = md.relative_to(workspace)
            if rel.name != "index.md":
                docs[str(rel)] = md.read_text(encoding="utf-8")
        return docs
    return {"nodes": nodes, "edges": edges, "output": docs_of("output"),
            "board": docs_of("board"), "subtypeZh": SUBTYPE_ZH}


def groups_of(nodes):
    by = {}
    for n in nodes:
        by.setdefault(n["tags"][0] if n["tags"] else "未分类", []).append(n)
    ordered = sorted(by.items(), key=lambda kv: (kv[0] == "未分类", -len(kv[1]), kv[0]))
    return ordered


def layout(data):
    placed, labels, worlds = [], [], []
    src = [n for n in data["nodes"] if n["layer"] == "sources"]
    idea = [n for n in data["nodes"] if n["layer"] == "ideas"]

    def place_world(title_zh, title_en, groups, grammar, card_h, ox, oy):
        gx, gy, rowh, wmax = 0, 0, 0, 0
        for gname, members in groups:
            cols = 1 if len(members) <= 2 else 2
            rows = math.ceil(len(members) / cols)
            gw = cols * CW + (cols - 1) * GX + 2 * PAD
            gh = HEAD + rows * (card_h + GY) - GY + 2 * PAD
            if gx + gw > ROW_MAX and gx > 0:
                gx, gy, rowh = 0, gy + rowh + 80, 0
            labels.append({"x": ox + gx + PAD, "y": oy + gy, "t": gname,
                           "n": len(members)})
            for i, m in enumerate(members):
                cx = ox + gx + PAD + (i % cols) * (CW + GX)
                cy = oy + gy + HEAD + PAD + (i // cols) * (card_h + GY)
                placed.append({**m, "x": cx, "y": cy, "w": CW, "h": card_h,
                               "g": grammar if grammar else m.get("g", "kraft")})
            rowh = max(rowh, gh)
            wmax = max(wmax, gx + gw)
            gx += gw + 46
        worlds.append({"x": ox, "y": oy + WORLD_TITLE_Y, "w": max(wmax, 1150),
                       "zh": title_zh, "en": title_en})
        return max(wmax, 1150)

    x0 = 0
    x0 += place_world("证据", "WORLD 1 · SOURCES", groups_of(src),
                      "note", CH, x0, 0) + WORLD_GAP
    x0 += place_world("想法", "WORLD 2 · IDEAS", groups_of(idea),
                      "slip", CH, x0, 0) + WORLD_GAP

    docs = []
    for path, text in data["output"].items():
        docs.append({"id": path, "layer": "output", "subtype": "", "g": "kraft",
                     "title": title_of(text, Path(path).stem),
                     "tags": [], "summary": first_paragraph(text), "body": ""})
    total = x0 + place_world("装配", "WORLD 3 · OUTPUT", [("output 装配产物", docs)],
                             None, DH, x0, 0)

    board_docs = []
    for path, text in data["board"].items():
        board_docs.append({"id": path, "layer": "board", "subtype": "", "g": "slip",
                           "title": title_of(text, Path(path).stem),
                           "tags": [], "summary": first_paragraph(text), "body": ""})
    if not board_docs:
        board_docs = [
            {"id": "__board_empty__", "layer": "board", "subtype": "", "g": "empty",
             "title": "还没有板——一文一板，自由度在你",
             "tags": [], "summary": "开一块对比或演算板：直接在 board/ 下写 md，或说一声"
                                    "「把 X 和 Y 摆成对比」由 agent 代笔。", "body": ""}]
    bottom = max(q["y"] + q["h"] for q in placed) + 470
    place_world("自由面 · 一文一板", "BOARD", [("board 板文", board_docs)],
                None, DH, max(0, (total - 1150) // 2), bottom)
    return placed, labels, worlds


_LINK = re.compile(r"\]\(\s*([^)\s]+?\.md)(?:#[^)]*)?\s*\)")


def doc_edges(data, node_ids):
    edges = []
    for family in ("output", "board"):
        for path, text in data[family].items():
            base = Path(path).parent
            seen = set()
            for raw in _LINK.findall(text):
                if re.match(r"^[a-z][a-z0-9+.-]*://", raw):
                    continue
                parts = list(base.parts)
                for seg in raw.split("/"):
                    if seg == "..":
                        parts and parts.pop()
                    elif seg not in (".", ""):
                        parts.append(seg)
                target = "/".join(parts)
                if target in node_ids and target != path and target not in seen:
                    seen.add(target)
                    edges.append({"from": path, "to": target})
    return edges


def embed_json(data):
    return json.dumps(data, ensure_ascii=False).replace("<", "\\u003c")


def build(workspace, outdir, css=None, title=None):
    workspace = Path(workspace).resolve()
    outdir = Path(outdir).resolve()
    if outdir == workspace or outdir.is_relative_to(workspace):
        raise ValueError(
            f"refusing to write into the workspace: the canvas is a projection "
            f"and never enters the truth ({outdir})")
    data = collect(workspace)
    placed, labels, worlds = layout(data)
    data["edges"] = data["edges"] + doc_edges(data, {p["id"] for p in placed})
    payload = {
        "nodes": [{k: v for k, v in p.items() if k != "body"} for p in placed],
        "bodies": {p["id"]: p.get("body", "") for p in placed if p.get("body")},
        "edges": data["edges"],
        "labels": labels, "worlds": worlds,
        "output": data["output"], "board": data["board"],
        "subtypeZh": SUBTYPE_ZH,
    }
    needs_mermaid = any("```mermaid" in t for t in
                        list(data["output"].values()) + list(data["board"].values()))
    css_file = Path(css).resolve() if css else DEFAULT_CSS
    html = (TEMPLATE.read_text(encoding="utf-8")
            .replace("<!--__TITLE__-->", title or f"{workspace.name} · 融合画布")
            .replace("/*__CSS__*/", css_file.read_text(encoding="utf-8"))
            .replace("/*__MARKED__*/", (VENDOR / "marked.min.js").read_text(encoding="utf-8"))
            .replace("/*__PURIFY__*/", (VENDOR / "purify.min.js").read_text(encoding="utf-8"))
            .replace("/*__MERMAID__*/",
                     (VENDOR / "mermaid.min.js").read_text(encoding="utf-8")
                     if needs_mermaid else "")
            .replace("/*__DATA__*/null", embed_json(payload)))
    outdir.mkdir(parents=True, exist_ok=True)
    out = outdir / "canvas.html"
    out.write_text(html, encoding="utf-8")
    print(f"ok: {out} — {len(placed)} nodes, {len(data['edges'])} edges, "
          f"{len(worlds)} worlds, mermaid={needs_mermaid}, "
          f"css={css_file.name}")
    return out


def main(argv):
    if len(argv) < 2:
        print("usage: build_canvas.py <workspace> [-o outdir] "
              "[--css style.css] [--title 'Page title']")
        return 1
    workspace = argv[1]
    outdir = argv[argv.index("-o") + 1] if "-o" in argv else "/tmp/rds-canvas"
    css = argv[argv.index("--css") + 1] if "--css" in argv else None
    title = argv[argv.index("--title") + 1] if "--title" in argv else None
    build(workspace, outdir, css, title)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
