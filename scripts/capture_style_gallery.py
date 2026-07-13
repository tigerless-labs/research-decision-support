import argparse
import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SKILL = REPO / "plugins/research-decision-support/skills/research-decision-support"
BUILDER = SKILL / "scripts/build_canvas.py"
STYLES_INDEX = SKILL / "canvas/styles/selection-index.json"

STYLE_VIEWPORT = {"width": 1600, "height": 1000}
HERO_VIEWPORT = {"width": 1920, "height": 1080}
STYLE_ZOOM = 0.8
HERO_ZOOM = 0.5
DARK_NATIVE_SLUGS = {"8-bit-orbit"}

FRAME_VIEW = """
(zoom) => {
  const anchorLeftShift = 350, anchorTopPad = 320, screenTop = 150;
  const ideas = DATA.nodes.filter(n => n.layer === "ideas");
  const pool = ideas.length ? ideas : DATA.nodes;
  const xs = pool.map(n => n.x), ys = pool.map(n => n.y);
  const cx = (Math.min(...xs) + Math.max(...xs)) / 2 - anchorLeftShift;
  const top = Math.min(...ys) - anchorTopPad;
  scale = zoom;
  sx = innerWidth / 2 - cx * scale;
  sy = screenTop - top * scale;
  apply(false);
}
"""

SELECT_HUB = """
() => {
  const deg = {};
  DATA.edges.forEach(e => {
    deg[e.from] = (deg[e.from] || 0) + 1;
    deg[e.to] = (deg[e.to] || 0) + 1;
  });
  const ideas = DATA.nodes.filter(n => n.layer === "ideas");
  const pool = ideas.length ? ideas : DATA.nodes;
  const best = pool.reduce((a, b) => (deg[b.id] || 0) > (deg[a.id] || 0) ? b : a);
  select(best.id);
}
"""

SET_SKIN = """
(slug) => {
  const sel = document.getElementById("skin");
  sel.value = slug;
  sel.dispatchEvent(new Event("change"));
}
"""


def build_canvas(workspace, tmp, title):
    subprocess.run(
        [sys.executable, str(BUILDER), str(workspace), "-o", str(tmp), "--title", title],
        check=True,
    )
    return tmp / "canvas.html"


def capture(page, url, slug, zoom, out_path):
    page.goto(url)
    page.evaluate(SET_SKIN, slug)
    page.evaluate(FRAME_VIEW, zoom)
    page.evaluate(SELECT_HUB)
    page.evaluate("document.fonts.ready")
    page.wait_for_timeout(400)
    page.screenshot(path=str(out_path))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("workspace", nargs="?", default=REPO / "examples/autoharness")
    ap.add_argument("-o", "--out", default=REPO / "docs/assets/canvas-styles")
    ap.add_argument("--title", default="research-decision-support · autoharness")
    args = ap.parse_args()

    from playwright.sync_api import sync_playwright

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    styles = json.loads(STYLES_INDEX.read_text(encoding="utf-8"))["styles"]

    with tempfile.TemporaryDirectory() as tmp:
        url = build_canvas(Path(args.workspace), Path(tmp), args.title).as_uri()
        with sync_playwright() as p:
            browser = p.chromium.launch()
            for style in styles:
                slug = style["slug"]
                scheme = "dark" if slug in DARK_NATIVE_SLUGS else "light"
                ctx = browser.new_context(viewport=STYLE_VIEWPORT, color_scheme=scheme)
                capture(ctx.new_page(), url, slug, STYLE_ZOOM, out / f"{slug}.png")
                ctx.close()
                print(f"captured {slug}.png")
            ctx = browser.new_context(viewport=HERO_VIEWPORT, color_scheme="light")
            capture(ctx.new_page(), url, "pin-and-paper", HERO_ZOOM, out / "hero.png")
            ctx.close()
            print("captured hero.png")
            browser.close()


if __name__ == "__main__":
    main()
