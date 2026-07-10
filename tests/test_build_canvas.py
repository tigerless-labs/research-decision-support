import pytest

from build_canvas import TEMPLATES, build, collect
from conftest import XSS_TITLE


@pytest.fixture
def workspace_with_output(workspace):
    (workspace / "output" / "modules").mkdir()
    (workspace / "output" / "system.md").write_text(
        "# 系统图\n\n```mermaid\nflowchart LR\n    A[\"one\"] --> B[\"two\"]\n"
        "    click A \"modules/mod-one.md\"\n```\n", encoding="utf-8")
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


def test_build_is_self_contained_and_escapes_cards(workspace, tmp_path):
    out = build(workspace, tmp_path / "proj", "tabbed-gallery")
    html = out.read_text(encoding="utf-8")
    assert '/*__' not in html
    assert 'src="http' not in html and "src='http" not in html
    assert XSS_TITLE not in html
    assert "</script><script>alert(1)" not in html


def test_build_tab_order_is_sources_ideas_system(workspace, tmp_path):
    html = build(workspace, tmp_path / "proj", "tabbed-gallery").read_text(encoding="utf-8")
    assert -1 < html.index("证据卡") < html.index("想法卡") < html.index("系统图")


def test_build_skips_mermaid_when_no_output_uses_it(workspace, tmp_path):
    plain = build(workspace, tmp_path / "plain", "tabbed-gallery").read_text(encoding="utf-8")
    assert "__esbuild_esm_mermaid" not in plain


def test_build_embeds_mermaid_when_output_uses_it(workspace_with_output, tmp_path):
    diagrammed = build(workspace_with_output, tmp_path / "diag",
                       "tabbed-gallery").read_text(encoding="utf-8")
    assert "__esbuild_esm_mermaid" in diagrammed


def test_build_refuses_to_write_into_the_workspace(workspace):
    with pytest.raises(ValueError, match="projection"):
        build(workspace, workspace / "output", "tabbed-gallery")


def test_build_rejects_unknown_template(workspace, tmp_path):
    with pytest.raises(ValueError) as err:
        build(workspace, tmp_path / "proj", "no-such-template")
    assert "tabbed-gallery" in str(err.value)


def test_template_registry_matches_disk():
    assert "tabbed-gallery" in TEMPLATES
    for template in TEMPLATES.values():
        assert template.exists()
