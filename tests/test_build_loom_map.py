from build_loom_map import build, collect

from conftest import XSS_TITLE


def node_ids(data):
    return {n["id"] for n in data["nodes"]}


def test_collect_includes_only_layer_cards(workspace):
    data = collect(workspace)
    ids = node_ids(data)
    assert "sources/papers/alpha.md" in ids
    assert all("index.md" not in i for i in ids)
    assert all(not i.startswith("notes.md") for i in ids)
    assert len(ids) == len(data["nodes"])


def test_every_edge_endpoint_is_a_known_card(workspace):
    data = collect(workspace)
    ids = node_ids(data)
    assert data["edges"]
    for edge in data["edges"]:
        assert edge["from"] in ids and edge["to"] in ids


def test_external_links_and_duplicates_excluded(workspace):
    data = collect(workspace)
    pairs = [(e["from"], e["to"]) for e in data["edges"]]
    assert len(pairs) == len(set(pairs))
    assert all("example.com" not in b for _, b in pairs)
    alpha_to_beta = [p for p in pairs if p == ("sources/papers/alpha.md", "sources/papers/beta.md")]
    assert len(alpha_to_beta) == 1


def test_summary_is_first_prose_paragraph(workspace):
    data = collect(workspace)
    by_id = {n["id"]: n for n in data["nodes"]}
    assert by_id["sources/papers/alpha.md"]["summary"].startswith("First paragraph")
    assert "Second paragraph" not in by_id["sources/papers/alpha.md"]["summary"]


def test_frontmatter_status_carried(workspace):
    data = collect(workspace)
    by_id = {n["id"]: n for n in data["nodes"]}
    assert by_id["ideas/idea-one.md"]["status"] == "候选"


def test_layer_counts_reconcile(workspace):
    data = collect(workspace)
    per_layer = {l: sum(1 for n in data["nodes"] if n["layer"] == l) for l in data["layers"]}
    assert sum(per_layer.values()) == len(data["nodes"])
    assert per_layer["sources"] > per_layer["synthesis"] > 0


def test_map_html_resists_script_breakout(workspace, tmp_path):
    out = tmp_path / "map.html"
    build(workspace, out, "t")
    html = out.read_text(encoding="utf-8")
    assert XSS_TITLE not in html
    assert html.count("<script>") == html.count("</script>")
    assert "<img src=x onerror" not in html
