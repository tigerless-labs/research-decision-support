from pathlib import Path

from check_doc_links import check_links
from check_workspace import check
from init_workspace import SKELETON, init


def test_init_creates_full_skeleton(tmp_path):
    root = tmp_path / "ws"
    created = init(root)
    assert set(created) == set(SKELETON)
    for rel in ("index.md", "target.md", "logs.md",
                "sources/index.md", "ideas/index.md", "output/index.md"):
        assert (root / rel).exists()
    assert (root / "ideas" / "archive").is_dir()


def test_init_is_idempotent_and_never_clobbers(tmp_path):
    root = tmp_path / "ws"
    init(root)
    marker = root / "ideas" / "index.md"
    marker.write_text("# my customized index\n", encoding="utf-8")
    assert init(root) == []
    assert marker.read_text(encoding="utf-8") == "# my customized index\n"


def test_check_passes_valid_workspace(workspace):
    assert check(workspace) == []


def test_check_flags_idea_missing_required_fields(workspace):
    (workspace / "ideas" / "bad.md").write_text(
        "---\ntags: [x]\n---\n# no id, no type\n", encoding="utf-8")
    problems = check(workspace)
    assert any("bad.md" in p and "id" in p for p in problems)
    assert any("bad.md" in p and "type" in p for p in problems)


def test_check_validates_archived_ideas_too(workspace):
    (workspace / "ideas" / "archive" / "bad-old.md").write_text(
        "---\ntype: idea\n---\n# archived but schema still holds\n", encoding="utf-8")
    problems = check(workspace)
    assert any("bad-old.md" in p and "id" in p for p in problems)


def test_check_flags_more_than_one_tag_on_any_layer(workspace):
    (workspace / "ideas" / "two-tags.md").write_text(
        "---\nid: two-tags\ntype: idea\ntags: [a, b]\n---\n# split me\n", encoding="utf-8")
    (workspace / "sources" / "papers" / "two-tags.md").write_text(
        "---\ntags: [a, b]\n---\n# split me too\n", encoding="utf-8")
    problems = check(workspace)
    assert sum("at most one tag" in p for p in problems) == 2


def test_check_accepts_untagged_cards(workspace):
    (workspace / "ideas" / "untagged.md").write_text(
        "---\nid: untagged\ntype: idea\n---\n# unclassified is fine\n", encoding="utf-8")
    assert check(workspace) == []


def test_check_flags_retired_status_field(workspace):
    (workspace / "ideas" / "stale.md").write_text(
        "---\nid: stale\ntype: idea\nstatus: adopted\n---\n# two states only\n",
        encoding="utf-8")
    problems = check(workspace)
    assert any("stale.md" in p and "status" in p for p in problems)


def test_check_flags_reference_cycle(workspace):
    (workspace / "ideas" / "cycle-a.md").write_text(
        "---\nid: cycle-a\ntype: idea\n---\n# a\n\nRests on [b](cycle-b.md).\n",
        encoding="utf-8")
    (workspace / "ideas" / "cycle-b.md").write_text(
        "---\nid: cycle-b\ntype: idea\n---\n# b\n\nRests on [a](cycle-a.md).\n",
        encoding="utf-8")
    problems = check(workspace)
    assert any("cycle" in p.lower() and "cycle-a.md" in p for p in problems)


def test_check_flags_self_reference(workspace):
    (workspace / "ideas" / "selfie.md").write_text(
        "---\nid: selfie\ntype: idea\n---\n# me\n\nSee [myself](selfie.md).\n",
        encoding="utf-8")
    problems = check(workspace)
    assert any("selfie.md" in p for p in problems)


def test_check_accepts_forward_chains(workspace):
    (workspace / "ideas" / "idea-three.md").write_text(
        "---\nid: idea-three\ntype: idea\n---\n# c\n\nBuilds on [two](idea-two.md).\n",
        encoding="utf-8")
    assert check(workspace) == []


def test_links_flags_dangling_and_ignores_external(workspace):
    (workspace / "ideas" / "dangler.md").write_text(
        "---\nid: dangler\ntype: idea\n---\n# d\n\n"
        "[gone](missing.md) and [web](https://example.com/a.md)\n", encoding="utf-8")
    problems = check_links(workspace)
    assert any("dangler.md" in p and "missing.md" in p for p in problems)
    assert not any("example.com" in p for p in problems)


def test_links_pass_on_valid_workspace(workspace):
    assert check_links(workspace) == []


def test_real_workspace_conforms_when_present():
    real = Path(__file__).resolve().parents[1] / "docs" / "research-decision-support"
    if not (real / "ideas").is_dir():
        return
    assert check(real) == []
    assert check_links(real) == []


def test_board_cards_are_schema_free(workspace):
    (workspace / "board" / "scratch.md").write_text(
        "# anything goes\n\nNo frontmatter, no required fields.\n", encoding="utf-8")
    assert check(workspace) == []


def test_board_is_terminal_no_inbound_references(workspace):
    (workspace / "ideas" / "leans-on-board.md").write_text(
        "---\nid: leans-on-board\ntype: idea\n---\n# bad\n\n"
        "Rests on [a board](../board/first-compare.md).\n", encoding="utf-8")
    problems = check(workspace)
    assert any("leans-on-board.md" in p and "board" in p for p in problems)


def test_board_single_tag_rule_still_applies(workspace):
    (workspace / "board" / "tagged.md").write_text(
        "---\ntags: [a, b]\n---\n# two tags\n", encoding="utf-8")
    problems = check(workspace)
    assert any("tagged.md" in p and "at most one tag" in p for p in problems)
