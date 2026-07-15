import json

import pytest

from build_canvas import DEFAULT_CSS, TEMPLATE, build, collect, doc_edges, layout
from conftest import XSS_TITLE
from init_workspace import init


@pytest.fixture
def workspace_with_output(workspace):
    (workspace / "output" / "modules").mkdir()
    (workspace / "output" / "system.md").write_text(
        "# System diagram\n\n```mermaid\nflowchart LR\n    A[\"one\"] --> B[\"two\"]\n"
        "    click A \"modules/mod-one.md\"\n```\n\n"
        "Details in [idea one](../ideas/idea-one.md).\n", encoding="utf-8")
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


def test_collect_takes_any_source_type_dir_verbatim(workspace):
    (workspace / "sources" / "podcasts").mkdir()
    (workspace / "sources" / "podcasts" / "delta.md").write_text(
        "# Delta episode\n\nA card under a type dir no preset knows.\n",
        encoding="utf-8")
    by_id = {n["id"]: n for n in collect(workspace)["nodes"]}
    assert by_id["sources/podcasts/delta.md"]["subtype"] == "podcasts"
    assert by_id["sources/papers/alpha.md"]["subtype"] == "papers"
    assert by_id["ideas/idea-one.md"]["subtype"] == ""


def test_build_has_no_subtype_mapping(workspace, tmp_path):
    html = build(workspace, tmp_path / "proj").read_text(encoding="utf-8")
    assert "subtypeZh" not in html


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
    assert f"{workspace.name} · unified canvas" in html


def test_build_style_is_swapped_by_css_only(workspace, tmp_path):
    other = tmp_path / "other.css"
    other.write_text(":root { --page:#101418; } /* alt-style */", encoding="utf-8")
    html = build(workspace, tmp_path / "proj", css=other).read_text(encoding="utf-8")
    assert "/* alt-style */" in html
    assert DEFAULT_CSS.read_text(encoding="utf-8") not in html


def switcher_payload(html):
    line = next((l for l in html.split("\n") if l.startswith("const STYLES = ")), None)
    assert line is not None
    return json.loads(line[len("const STYLES = "):].rstrip(";"))


def test_build_default_embeds_live_style_switcher(workspace, tmp_path):
    html = build(workspace, tmp_path / "proj").read_text(encoding="utf-8")
    assert '<select id="skin"' in html
    payload = switcher_payload(html)
    index = json.loads((DEFAULT_CSS.parent.parent / "selection-index.json")
                       .read_text(encoding="utf-8"))
    slugs = {entry["slug"] for entry in index["styles"]}
    assert set(payload["css"]) == slugs
    assert {o["slug"] for o in payload["options"]} == slugs
    assert payload["default"] in payload["css"]


def test_build_pinned_css_disables_switcher(workspace, tmp_path):
    pinned = tmp_path / "pinned.css"
    pinned.write_text(":root { --page:#101418; }", encoding="utf-8")
    html = build(workspace, tmp_path / "proj", css=pinned).read_text(encoding="utf-8")
    assert switcher_payload(html) is None


def test_build_skips_mermaid_when_no_output_uses_it(workspace, tmp_path):
    plain = build(workspace, tmp_path / "plain").read_text(encoding="utf-8")
    assert "__esbuild_esm_mermaid" not in plain


def test_build_embeds_mermaid_when_output_uses_it(workspace_with_output, tmp_path):
    diagrammed = build(workspace_with_output, tmp_path / "diag").read_text(encoding="utf-8")
    assert "__esbuild_esm_mermaid" in diagrammed


def test_build_refuses_to_write_into_the_workspace(workspace):
    with pytest.raises(ValueError, match="projection"):
        build(workspace, workspace / "output")


def test_build_html_suffix_writes_that_file_not_a_directory(workspace, tmp_path):
    out = build(workspace, tmp_path / "proj" / "my-canvas.html")
    assert out == tmp_path / "proj" / "my-canvas.html"
    assert out.is_file()
    assert "<html" in out.read_text(encoding="utf-8")


def test_build_refuses_html_target_inside_the_workspace(workspace):
    with pytest.raises(ValueError, match="projection"):
        build(workspace, workspace / "canvas.html")


def test_template_and_default_css_exist_on_disk():
    assert TEMPLATE.exists()
    assert DEFAULT_CSS.exists()


def test_template_carries_style_hooks():
    # Plan-C hook contract: a chrome shell on every card and an index slot on
    # every world title (hidden unless a style opts in), an edge-shape CSS
    # variable read at draw time, and a named skin sheet so the runtime
    # switcher can never clobber the hook defaults.
    text = TEMPLATE.read_text(encoding="utf-8")
    assert '"chrome"' in text
    assert '"idx"' in text
    assert "--edge-shape" in text
    assert 'id="skinsheet"' in text
    assert ".card .chrome{display:none}" in text
    assert ".wtitle .idx{display:none}" in text
    assert 'querySelector("style")' not in text


def test_template_maps_every_mermaid_text_surface_to_style_tokens():
    # Mermaid's built-in themes hardcode flowchart label colors (#333/#000)
    # and near-white cluster fills, which dark palettes cannot survive; the
    # template must pin every text and container surface to style tokens so
    # no theme default reaches the screen (docs/design-harness/output/modules/canvas.md).
    text = TEMPLATE.read_text(encoding="utf-8")
    for mapping in ('primaryTextColor: tok("--ink")',
                    'nodeTextColor: tok("--ink")',
                    'textColor: tok("--ink")',
                    'titleColor: tok("--ink")',
                    'clusterBkg: tok("--wash")',
                    'clusterBorder: tok("--grid")'):
        assert mapping in text


def test_build_payload_splits_bodies_from_nodes(workspace, tmp_path):
    html = build(workspace, tmp_path / "proj").read_text(encoding="utf-8")
    line = next(l for l in html.split("\n") if l.startswith("const DATA = "))
    payload = json.loads(line[len("const DATA = "):].rstrip(";"))
    assert {"nodes", "bodies", "edges", "labels", "worlds",
            "output", "board"} <= payload.keys()
    assert "subtypeZh" not in payload
    assert not any("body" in n for n in payload["nodes"])
    assert payload["bodies"]


def test_template_opens_on_default_skin_every_time():
    text = TEMPLATE.read_text(encoding="utf-8")
    assert "localStorage" not in text
    assert "STYLES.default" in text


def test_build_gate_rejects_invalid_cards_and_writes_nothing(workspace, tmp_path, capsys):
    (workspace / "ideas" / "bad.md").write_text(
        "---\ntags: [x]\n---\n# no id, no type\n", encoding="utf-8")
    outdir = tmp_path / "proj"
    with pytest.raises(ValueError):
        build(workspace, outdir)
    assert not (outdir / "canvas.html").exists()
    out = capsys.readouterr().out
    assert "INVALID" in out and "bad.md" in out


def test_build_gate_rejects_dangling_links_and_writes_nothing(workspace, tmp_path, capsys):
    (workspace / "ideas" / "idea-one.md").write_text(
        "---\nid: idea-one\ntype: idea\n---\n# First judgment\n\n"
        "Stands on [gone](../sources/papers/gone.md).\n", encoding="utf-8")
    outdir = tmp_path / "proj"
    with pytest.raises(ValueError):
        build(workspace, outdir)
    assert not (outdir / "canvas.html").exists()
    out = capsys.readouterr().out
    assert "DANGLING" in out and "gone.md" in out


def test_build_renders_freshly_initialized_workspace(tmp_path):
    root = tmp_path / "fresh" / "design-harness"
    init(root)
    html = build(root, tmp_path / "proj").read_text(encoding="utf-8")
    assert "No boards yet" in html


def test_collect_projects_conflicts_as_kind_edges(workspace):
    (workspace / "ideas" / "challenger.md").write_text(
        "---\nid: challenger\ntype: idea\nconflicts: [idea-one]\n---\n"
        "# Challenger\n\nDisputes the first judgment.\n", encoding="utf-8")
    data = collect(workspace)
    assert {"from": "ideas/challenger.md", "to": "ideas/idea-one.md",
            "kind": "conflict"} in data["edges"]
    assert {"from": "ideas/idea-two.md", "to": "ideas/idea-one.md"} in data["edges"]


def test_collect_never_projects_unresolvable_or_archived_conflicts(workspace):
    (workspace / "ideas" / "challenger.md").write_text(
        "---\nid: challenger\ntype: idea\nconflicts: [idea-old, no-such-id]\n---\n"
        "# Challenger\n\nBoth targets are out of the live set.\n", encoding="utf-8")
    data = collect(workspace)
    assert not [e for e in data["edges"] if e.get("kind") == "conflict"]


def test_template_draws_conflict_edges_red():
    text = TEMPLATE.read_text(encoding="utf-8")
    assert "var(--edge-conflict" in text
    assert "#d0342c" in text


def test_build_embeds_conflict_edges(workspace, tmp_path):
    (workspace / "ideas" / "challenger.md").write_text(
        "---\nid: challenger\ntype: idea\nconflicts: [idea-one]\n---\n"
        "# Challenger\n\nDisputes the first judgment.\n", encoding="utf-8")
    html = build(workspace, tmp_path / "proj").read_text(encoding="utf-8")
    assert '"kind": "conflict"' in html
