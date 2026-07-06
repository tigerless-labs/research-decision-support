from build_map import collect
from build_site import assemble, build_site

from conftest import XSS_TITLE

NAV_PAGES = ["index.html", "read.html", "compare.html", "ideas.html", "design.html",
             "decisions.html", "map.html"]
PAGES = NAV_PAGES + ["card.html"]


def test_directions_come_from_synthesis_links(workspace):
    site = assemble(collect(workspace))
    by_title = {d["title"]: d for d in site["directions"]}
    assert set(by_title["Direction one"]["members"]) == {
        "sources/papers/alpha.md", "sources/papers/beta.md"}
    assert "sources/github/gamma.md" in by_title["Direction two"]["members"]


def test_members_plus_unassigned_cover_all_sources(workspace):
    data = collect(workspace)
    site = assemble(data)
    sources = {n["id"] for n in data["nodes"] if n["layer"] == "sources"}
    covered = {m for d in site["directions"] for m in d["members"]}
    assert covered | set(site["unassigned"]) == sources
    assert not covered & set(site["unassigned"])


def test_shared_source_in_both_directions_not_unassigned(workspace):
    site = assemble(collect(workspace))
    holders = [d for d in site["directions"] if "sources/papers/beta.md" in d["members"]]
    assert len(holders) == 2
    assert "sources/papers/beta.md" not in site["unassigned"]


def test_orphan_source_is_unassigned(workspace):
    site = assemble(collect(workspace))
    assert "sources/papers/orphan.md" in site["unassigned"]


def test_build_site_writes_all_pages_self_contained(workspace, tmp_path):
    build_site(workspace, tmp_path / "site", "demo")
    for page in PAGES:
        html = (tmp_path / "site" / page).read_text(encoding="utf-8")
        assert "<script src" not in html
        assert '<link rel="stylesheet"' not in html
        assert "@import" not in html


def test_pages_resist_script_breakout(workspace, tmp_path):
    build_site(workspace, tmp_path / "site", "demo")
    for page in PAGES:
        html = (tmp_path / "site" / page).read_text(encoding="utf-8")
        assert XSS_TITLE not in html, page
        assert html.count("<script>") == html.count("</script>"), page
        assert "<img src=x onerror" not in html, page


def test_pages_carry_data_and_nav(workspace, tmp_path):
    build_site(workspace, tmp_path / "site", "demo")
    for page in PAGES:
        html = (tmp_path / "site" / page).read_text(encoding="utf-8")
        for target in NAV_PAGES:
            assert target in html, (page, target)
    read = (tmp_path / "site" / "read.html").read_text(encoding="utf-8")
    assert "Alpha paper" in read
    assert "First paragraph of alpha." in read
    ideas = (tmp_path / "site" / "ideas.html").read_text(encoding="utf-8")
    assert "My idea" in ideas and "候选" in ideas
    design = (tmp_path / "site" / "design.html").read_text(encoding="utf-8")
    assert "The spine" in design
    decisions = (tmp_path / "site" / "decisions.html").read_text(encoding="utf-8")
    assert "ADR: pick alpha" in decisions and "accepted" in decisions


def test_card_viewer_embeds_bodies_and_renderer(workspace, tmp_path):
    build_site(workspace, tmp_path / "site", "demo")
    card = (tmp_path / "site" / "card.html").read_text(encoding="utf-8")
    assert "Second paragraph." in card
    assert "marked v" in card and "DOMPurify" in card
    for page in ["index.html", "read.html", "map.html"]:
        html = (tmp_path / "site" / page).read_text(encoding="utf-8")
        assert "Second paragraph." not in html, page
