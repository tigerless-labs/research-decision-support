import json
import re
from pathlib import Path

import pytest

from check_style_pack import CANONICAL_TOKENS, USAGE_KEYS, check, parse_frontmatter

SKILL_ROOT = Path(__file__).resolve().parents[1] / (
    "plugins/research-decision-support/skills/research-decision-support")
SHIPPED_PACK = SKILL_ROOT / "styles"

LIGHT = {
    "surface": "#fcfcfb", "page": "#f9f9f7", "ink": "#0b0b0b", "ink-2": "#52514e",
    "muted": "#898781", "grid": "#e1e0d9", "ring": "rgba(11,11,11,0.10)",
    "wash": "#f1f1ed", "accent-d": "#c2410c",
    "accent-a": "#2a78d6", "accent-b": "#eda100", "accent-c": "#4a3aa7", "positive": "#008300",
}
DARK = {
    "surface": "#1a1a19", "page": "#0d0d0d", "ink": "#ffffff", "ink-2": "#c3c2b7",
    "muted": "#898781", "grid": "#2c2c2a", "ring": "rgba(255,255,255,0.10)",
    "wash": "#232322", "accent-d": "#e2673a",
    "accent-a": "#3987e5", "accent-b": "#c98500", "accent-c": "#9085e9", "positive": "#008300",
}


def palette_block(name, palette):
    lines = [f"{name}:"]
    lines += [f'  {token}: "{value}"' for token, value in palette.items()]
    return "\n".join(lines)


def design_md(slug, light=LIGHT, dark=DARK, extra_frontmatter="", body_extra="", canvases=None):
    frontmatter = "\n".join([
        f"slug: {slug}",
        f"name: {slug.title()}",
        "version: 1",
        "scheme: dual",
        palette_block("colors-light", light),
        palette_block("colors-dark", dark),
        "color-aliases:",
        "  accent: accent-c",
        "  link: accent-a",
        "typography:",
        '  body-family: system-ui, sans-serif',
        '  base-size: "14px"',
        "components:",
        '  card-radius: "8px"',
        '  max-width: "1160px"',
        extra_frontmatter,
    ]).strip()
    body = "\n".join([
        "## Atmosphere", "Calm paper, quiet chrome, content leads." + body_extra,
        "## Accent roles",
        "accent-a cool informational blue, accent-b warm amber, accent-c settled violet",
        "carrying the most weight, accent-d burnt sienna, positive reserved green.",
        "## Signature moves",
        "- Hairline grid borders", "- Layer-tinted chips", "- Generous reading measure",
        "## Do / Don't",
        "Do keep chrome quiet. Don't introduce colors outside the palette.",
    ])
    if canvases:
        body += "\n## Canvas renderings\n"
        body += "".join(f"\n### {canvas}\nSwitcher and card forms for {canvas}.\n"
                        for canvas in canvases)
    return f"---\n{frontmatter}\n---\n\n# {slug.title()}\n\n{body}\n"


def preview_md(slug):
    return "\n".join([
        f"# {slug.title()} — calm editorial paper",
        "## Palette",
        "surface #fcfcfb / #1a1a19; ink #0b0b0b / #ffffff; accent-c #4a3aa7 / #9085e9",
        "## Typography",
        "System UI stack, 14px base, quiet weights.",
        "## Signature moves",
        "- Hairline grid borders", "- Layer-tinted chips",
        "## Fit",
        "Best for: long reading sessions. Avoid for: high-energy pitch moments.",
    ]) + "\n"


def index_entry(slug, **overrides):
    entry = {
        "slug": slug,
        "name": slug.title(),
        "tagline": "Calm editorial paper.",
        "mood": ["calm", "editorial"],
        "tone": "understated",
        "formality": "neutral",
        "density": "comfortable",
        "scheme": "dual",
        "best_for": ["long reading sessions"],
        "avoid_for": ["high-energy pitch moments"],
        "preview": f"{slug}/preview.md",
        "design": f"{slug}/design.md",
    }
    entry.update(overrides)
    return entry


def usage_block():
    return {key: f"Rule text for {key}." for key in USAGE_KEYS}


class PackFixture:
    def __init__(self, root):
        self.root = root

    def __truediv__(self, rel):
        return self.root / rel

    def __fspath__(self):
        return str(self.root)

    def add_canvas(self, slug):
        canvas_dir = self.root.parent / "canvases" / slug
        canvas_dir.mkdir(parents=True, exist_ok=True)
        (canvas_dir / "spec.md").write_text(f"# canvas: {slug}\n", encoding="utf-8")

    def add_style(self, slug, design=None, preview=None):
        style_dir = self.root / slug
        style_dir.mkdir(exist_ok=True)
        (style_dir / "design.md").write_text(design or design_md(slug), encoding="utf-8")
        (style_dir / "preview.md").write_text(preview or preview_md(slug), encoding="utf-8")

    def write_index(self, entries, usage=None, version=1):
        payload = {"version": version, "usage": usage or usage_block(), "styles": entries}
        (self.root / "selection-index.json").write_text(
            json.dumps(payload, indent=2), encoding="utf-8")


@pytest.fixture
def pack(tmp_path):
    root = tmp_path / "styles"
    root.mkdir()
    fixture = PackFixture(root)
    fixture.add_style("alpha-paper")
    fixture.add_style("beta-slate")
    fixture.write_index([index_entry("alpha-paper"), index_entry("beta-slate")])
    return fixture


def problems_mentioning(problems, fragment):
    return [p for p in problems if fragment in p]


def test_valid_synthetic_pack_passes(pack):
    assert check(pack) == []


def test_external_url_in_design_body_rejected(pack):
    style = pack / "alpha-paper" / "design.md"
    style.write_text(
        design_md("alpha-paper", body_extra=" background: url(https://evil.example/px.png)"),
        encoding="utf-8")
    assert problems_mentioning(check(pack), "alpha-paper/design.md")


def test_script_tag_in_preview_rejected(pack):
    (pack / "beta-slate" / "preview.md").write_text(
        preview_md("beta-slate") + "\n<script>alert(1)</script>\n", encoding="utf-8")
    assert problems_mentioning(check(pack), "beta-slate/preview.md")


def test_expression_color_value_rejected(pack):
    bad = dict(LIGHT, ink="expression(alert(1))")
    (pack / "alpha-paper" / "design.md").write_text(
        design_md("alpha-paper", light=bad), encoding="utf-8")
    assert problems_mentioning(check(pack), "alpha-paper/design.md")


def test_javascript_color_value_rejected(pack):
    bad = dict(DARK, ink="javascript:alert(1)")
    (pack / "alpha-paper" / "design.md").write_text(
        design_md("alpha-paper", dark=bad), encoding="utf-8")
    assert problems_mentioning(check(pack), "alpha-paper/design.md")


def test_index_entry_for_missing_directory_rejected(pack):
    pack.write_index([index_entry("alpha-paper"), index_entry("beta-slate"),
                      index_entry("ghost-style")])
    assert problems_mentioning(check(pack), "ghost-style")


def test_orphan_directory_rejected(pack):
    pack.add_style("orphan-style")
    assert problems_mentioning(check(pack), "orphan-style")


def test_duplicate_slug_rejected(pack):
    pack.write_index([index_entry("alpha-paper"), index_entry("alpha-paper"),
                      index_entry("beta-slate")])
    assert problems_mentioning(check(pack), "alpha-paper")


def test_frontmatter_slug_mismatch_rejected(pack):
    (pack / "beta-slate" / "design.md").write_text(
        design_md("other-name"), encoding="utf-8")
    assert problems_mentioning(check(pack), "beta-slate/design.md")


def test_path_traversal_in_index_rejected(pack):
    pack.write_index([
        index_entry("alpha-paper", design="../../../etc/passwd"),
        index_entry("beta-slate"),
    ])
    assert problems_mentioning(check(pack), "alpha-paper")


def test_depth_three_frontmatter_fails_safe(pack):
    nested = "colors-extra:\n  group:\n    deep: \"#ffffff\""
    (pack / "alpha-paper" / "design.md").write_text(
        design_md("alpha-paper", extra_frontmatter=nested), encoding="utf-8")
    assert problems_mentioning(check(pack), "alpha-paper/design.md")


def test_missing_canonical_token_rejected(pack):
    short = {token: value for token, value in DARK.items() if token != "ink"}
    (pack / "alpha-paper" / "design.md").write_text(
        design_md("alpha-paper", dark=short), encoding="utf-8")
    problems = problems_mentioning(check(pack), "alpha-paper/design.md")
    assert problems_mentioning(problems, "ink")


def test_dangling_color_alias_rejected(pack):
    (pack / "alpha-paper" / "design.md").write_text(
        design_md("alpha-paper",
                  extra_frontmatter="").replace("accent: accent-c", "accent: accent-nonexistent"),
        encoding="utf-8")
    assert problems_mentioning(check(pack), "alpha-paper/design.md")


def test_missing_usage_key_rejected(pack):
    usage = usage_block()
    del usage["never-bulk-read"]
    pack.write_index([index_entry("alpha-paper"), index_entry("beta-slate")], usage=usage)
    assert problems_mentioning(check(pack), "never-bulk-read")


def test_illegal_enum_values_rejected(pack):
    pack.write_index([
        index_entry("alpha-paper", formality="corporate", density="dense", scheme="sepia"),
        index_entry("beta-slate"),
    ])
    problems = problems_mentioning(check(pack), "alpha-paper")
    assert len(problems) >= 3


def test_preview_must_be_lighter_than_design(pack):
    (pack / "beta-slate" / "preview.md").write_text(
        preview_md("beta-slate") + "filler line\n" * 400, encoding="utf-8")
    assert problems_mentioning(check(pack), "beta-slate/preview.md")


def test_canonical_tokens_cover_template_slots():
    assert set(CANONICAL_TOKENS) == {
        "surface", "page", "ink", "ink-2", "muted", "grid", "ring", "wash", "accent-d",
        "accent-a", "accent-b", "accent-c", "positive",
    }


def test_canvas_renderings_happy_path(pack):
    pack.add_canvas("tabbed-gallery")
    pack.add_style("alpha-paper", design=design_md("alpha-paper", canvases=["tabbed-gallery"]))
    pack.write_index([index_entry("alpha-paper", canvas_renderings=["tabbed-gallery"]),
                      index_entry("beta-slate")])
    assert check(pack) == []


def test_canvas_renderings_unknown_canvas_rejected(pack):
    pack.add_style("alpha-paper", design=design_md("alpha-paper", canvases=["ghost-canvas"]))
    pack.write_index([index_entry("alpha-paper", canvas_renderings=["ghost-canvas"]),
                      index_entry("beta-slate")])
    assert problems_mentioning(check(pack), "ghost-canvas")


def test_canvas_renderings_missing_design_section_rejected(pack):
    pack.add_canvas("tabbed-gallery")
    pack.write_index([index_entry("alpha-paper", canvas_renderings=["tabbed-gallery"]),
                      index_entry("beta-slate")])
    assert problems_mentioning(check(pack), "tabbed-gallery")


def test_canvas_renderings_must_be_string_list(pack):
    pack.add_canvas("tabbed-gallery")
    pack.write_index([index_entry("alpha-paper", canvas_renderings="tabbed-gallery"),
                      index_entry("beta-slate")])
    assert problems_mentioning(check(pack), "canvas_renderings")


def shipped_index():
    return json.loads((SHIPPED_PACK / "selection-index.json").read_text(encoding="utf-8"))


def shipped_designs():
    for entry in shipped_index()["styles"]:
        text = (SHIPPED_PACK / entry["slug"] / "design.md").read_text(encoding="utf-8")
        frontmatter, problems = parse_frontmatter(text)
        assert problems == []
        yield entry["slug"], frontmatter


def template_palettes():
    css = (SKILL_ROOT / "canvases/tabbed-gallery/template.html").read_text(encoding="utf-8")
    blocks = re.findall(r":root\s*\{([^}]*)\}", css)
    token = re.compile(r"--([a-z0-9-]+):\s*([^;]+);")
    light = dict(token.findall(blocks[0]))
    dark = dict(token.findall(blocks[1]))
    return light, dark


def test_shipped_pack_validates():
    assert check(SHIPPED_PACK) == []


def test_shipped_index_matches_directories():
    indexed = {entry["slug"] for entry in shipped_index()["styles"]}
    on_disk = {child.name for child in SHIPPED_PACK.iterdir() if child.is_dir()}
    assert indexed == on_disk
    for slug in on_disk:
        assert (SHIPPED_PACK / slug / "design.md").is_file()
        assert (SHIPPED_PACK / slug / "preview.md").is_file()


def test_shipped_styles_ship_both_palettes_with_canonical_tokens():
    for slug, frontmatter in shipped_designs():
        for block in ("colors-light", "colors-dark"):
            assert set(frontmatter[block]) >= set(CANONICAL_TOKENS), (slug, block)


def test_builder_default_theme_covers_canonical_tokens():
    light, dark = template_palettes()
    assert set(CANONICAL_TOKENS) <= set(light)
    assert set(CANONICAL_TOKENS) <= set(dark)


def test_shipped_previews_are_lighter_than_designs():
    for entry in shipped_index()["styles"]:
        preview = (SHIPPED_PACK / entry["preview"]).stat().st_size
        design = (SHIPPED_PACK / entry["design"]).stat().st_size
        assert 0 < preview < design, entry["slug"]


def test_shipped_index_carries_usage_policy():
    usage = shipped_index()["usage"]
    for key in USAGE_KEYS:
        assert usage.get(key), key


def test_shipped_index_has_discriminating_axes():
    entries = shipped_index()["styles"]
    for axis in ("formality", "density"):
        assert len({entry[axis] for entry in entries}) >= 2, axis
    schemes = {entry["scheme"] for entry in entries}
    assert schemes & {"light", "dual"} and schemes & {"dark", "dual"}
    assert len(schemes) >= 2
