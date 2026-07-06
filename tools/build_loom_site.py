import os
import sys
from pathlib import Path

from build_loom_map import collect, embed_json, without_bodies
from build_loom_map import render as render_map

SITE_PAGES = ["index", "read", "compare", "ideas", "design", "decisions"]
NAV_LINKS = [("index", "Overview"), ("read", "Read"), ("compare", "Compare"),
             ("ideas", "Ideas"), ("design", "Design"), ("decisions", "Decisions"),
             ("map", "Map")]


def assemble(data):
    nodes = {n["id"]: n for n in data["nodes"]}
    directions = []
    for node in data["nodes"]:
        if node["layer"] != "synthesis":
            continue
        members = sorted({e["to"] for e in data["edges"]
                          if e["from"] == node["id"] and nodes[e["to"]]["layer"] == "sources"})
        directions.append({"id": node["id"], "title": node["title"],
                           "summary": node["summary"], "members": members})
    covered = {m for d in directions for m in d["members"]}
    unassigned = [n["id"] for n in data["nodes"] if n["layer"] == "sources" and n["id"] not in covered]
    return {**data, "directions": directions, "unassigned": unassigned}


def nav_html(active, with_theme):
    links = "".join(
        f'<a href="{page}.html"{" class=\"on\"" if page == active else ""}>{label}</a>'
        for page, label in NAV_LINKS)
    theme = '<span class="spacer"></span><button id="theme-toggle">◐ theme</button>' if with_theme else ""
    return f'<nav class="sitenav"><span class="brand">🧶 loom</span>{links}{theme}</nav>'


def build_site(workspace, outdir, title):
    workspace = Path(workspace).resolve()
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    site = assemble(collect(workspace))
    site["title"] = title
    site["workspace_rel"] = Path(os.path.relpath(workspace, outdir.resolve())).as_posix()
    tools = Path(__file__).parent
    template = (tools / "loom_site_template.html").read_text(encoding="utf-8")
    for page in SITE_PAGES:
        html = (template
                .replace("<!--__NAV__-->", nav_html(page, with_theme=True))
                .replace('"__PAGE__"', f'"{page}"')
                .replace("/*__DATA__*/null", embed_json(without_bodies(site))))
        (outdir / f"{page}.html").write_text(html, encoding="utf-8")
    card = ((tools / "loom_card_template.html").read_text(encoding="utf-8")
            .replace("<!--__NAV__-->", nav_html("", with_theme=True))
            .replace("/*__MARKED__*/", (tools / "vendor/marked.min.js").read_text(encoding="utf-8"))
            .replace("/*__PURIFY__*/", (tools / "vendor/purify.min.js").read_text(encoding="utf-8"))
            .replace("/*__DATA__*/null", embed_json(site)))
    (outdir / "card.html").write_text(card, encoding="utf-8")
    map_data = {k: site[k] for k in ("nodes", "edges", "layers")}
    map_data["title"] = title
    (outdir / "map.html").write_text(render_map(map_data, nav_html("map", with_theme=False)),
                                     encoding="utf-8")
    print(f"ok: {outdir} — {'/'.join(SITE_PAGES)}/map + card viewer · {len(site['nodes'])} cards, "
          f"{len(site['directions'])} directions, {len(site['unassigned'])} unassigned, "
          f"{len(site['edges'])} links")


def main(argv):
    if len(argv) < 2:
        print("usage: build_loom_site.py <workspace-dir> [-o output-dir] [--title 'Site title']")
        return 1
    workspace = argv[1]
    outdir = argv[argv.index("-o") + 1] if "-o" in argv else "loom-site"
    title = argv[argv.index("--title") + 1] if "--title" in argv else Path(workspace).name
    build_site(workspace, outdir, title)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
