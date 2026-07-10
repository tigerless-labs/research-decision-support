import json

import pytest

from build_canvas import DEFAULT_CSS, TEMPLATE, build, collect, doc_edges, layout
from conftest import XSS_TITLE


@pytest.fixture
def workspace_with_output(workspace):
    (workspace / "output" / "modules").mkdir()
    (workspace / "output" / "system.md").write_text(
        "# 系统图\n\n```mermaid\nflowchart LR\n    A[\"one\"] --> B[\"two\"]\n"
        "    click A \"modules/mod-one.md\"\n```\n\n"
        "细节见 [idea one](../ideas/idea-one.md)。\n", encoding="utf-8")
    (workspace / "output" / "modules" / "mod-one.md").write_text(
        "---\nid: mod-one\ntype: module\n---\n# module one\n\nBoundary bullets.\n",
        encoding="utf-8")
    return workspace


def test_collect_excludes_archive_and_indexes(workspace):
    data = collect(workspace)
    ids = {n["id"] for n in data["nodes"]}
    assert "ideas/idea-one.md" in ids
    assert not any("archive" in i for i in ids)
    assert not any(i.endswith("index.md") for i in ids)


def test_collect_reads_frontmatter_tags_and_edges(workspace):
    data = collect(workspace)
    by_id = {n["id"]: n for n in data["nodes"]}
    assert by_id["ideas/idea-one.md"]["tags"] == ["positioning"]
    assert by_id["sources/github/gamma.md"]["tags"] == []
    assert {"from": "ideas/idea-two.md", "to": "ideas/idea-one.md"} in data["edges"]


def test_collect_gathers_output_docs(workspace_with_output):
    data = collect(workspace_with_output)
    assert "output/system.md" in data["output"]
    assert "output/modules/mod-one.md" in data["output"]
    assert "mermaid" in data["output"]["output/system.md"]


def test_collect_gathers_board_docs(workspace):
    data = collect(workspace)
    assert "board/first-compare.md" in data["board"]
    assert not any(p.endswith("index.md") for p in data["board"])


def test_layout_places_every_card_with_geometry(workspace_with_output):
    data = collect(workspace_with_output)
    placed, labels, worlds = layout(data)
    card_ids = {n["id"] for n in data["nodes"]}
    placed_ids = {p["id"] for p in placed}
    assert card_ids <= placed_ids
    assert all({"x", "y", "w", "h", "g"} <= p.keys() for p in placed)
    assert "output/system.md" in placed_ids
    assert [w["en"] for w in worlds] == [
        "WORLD 1 · SOURCES", "WORLD 2 · IDEAS", "WORLD 3 · OUTPUT", "BOARD"]


def test_layout_shows_teaching_card_when_board_empty(workspace_with_output):
    data = collect(workspace_with_output)
    data["board"] = {}
    placed, _, _ = layout(data)
    assert any(p["id"] == "__board_empty__" for p in placed)


def test_doc_edges_link_docs_to_cards(workspace_with_output):
    data = collect(workspace_with_output)
    placed, _, _ = layout(data)
    edges = doc_edges(data, {p["id"] for p in placed})
    assert {"from": "output/system.md", "to": "ideas/idea-one.md"} in edges


def test_build_is_self_contained_and_escapes_cards(workspace, tmp_path):
    out = build(workspace, tmp_path / "proj")
    html = out.read_text(encoding="utf-8")
    assert '/*__' not in html
    assert 'src="http' not in html and "src='http" not in html
    assert XSS_TITLE not in html
    assert "</script><script>alert(1)" not in html


def test_build_embeds_default_css_and_title(workspace, tmp_path):
    html = build(workspace, tmp_path / "proj").read_text(encoding="utf-8")
    assert DEFAULT_CSS.read_text(encoding="utf-8") in html
    assert f"{workspace.name} · 融合画布" in html


def test_build_style_is_swapped_by_css_only(workspace, tmp_path):
    other = tmp_path / "other.css"
    other.write_text(":root { --page:#101418; } /* alt-style */", encoding="utf-8")
    html = build(workspace, tmp_path / "proj", css=other).read_text(encoding="utf-8")
    assert "/* alt-style */" in html
    assert DEFAULT_CSS.read_text(encoding="utf-8") not in html


def test_build_skips_mermaid_when_no_output_uses_it(workspace, tmp_path):
    plain = build(workspace, tmp_path / "plain").read_text(encoding="utf-8")
    assert "__esbuild_esm_mermaid" not in plain


def test_build_embeds_mermaid_when_output_uses_it(workspace_with_output, tmp_path):
    diagrammed = build(workspace_with_output, tmp_path / "diag").read_text(encoding="utf-8")
    assert "__esbuild_esm_mermaid" in diagrammed


def test_build_refuses_to_write_into_the_workspace(workspace):
    with pytest.raises(ValueError, match="projection"):
        build(workspace, workspace / "output")


def test_template_and_default_css_exist_on_disk():
    assert TEMPLATE.exists()
    assert DEFAULT_CSS.exists()


def test_build_payload_splits_bodies_from_nodes(workspace, tmp_path):
    html = build(workspace, tmp_path / "proj").read_text(encoding="utf-8")
    line = next(l for l in html.split("\n") if l.startswith("const DATA = "))
    payload = json.loads(line[len("const DATA = "):].rstrip(";"))
    assert {"nodes", "bodies", "edges", "labels", "worlds",
            "output", "board", "subtypeZh"} <= payload.keys()
    assert not any("body" in n for n in payload["nodes"])
    assert payload["bodies"]
