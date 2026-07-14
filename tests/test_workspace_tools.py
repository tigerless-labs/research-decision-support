from pathlib import Path

from check_doc_links import check_links
from check_workspace import check
from init_workspace import SKELETON, init
from init_workspace import main as init_main
from workspace import parse_frontmatter, parse_tags


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


def test_init_main_bootstraps_and_validates_in_one_command(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    assert init_main(["init_workspace.py", "docs/design-harness"]) == 0
    out = capsys.readouterr().out
    assert out.count("ok:") >= 3
    assert "INVALID" not in out
    assert "DANGLING" not in out


def test_init_main_fails_nonzero_on_invalid_card(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    ws = tmp_path / "docs" / "design-harness"
    (ws / "ideas").mkdir(parents=True)
    (ws / "ideas" / "bad.md").write_text(
        "---\ntags: [x]\n---\n# no id, no type\n", encoding="utf-8")
    assert init_main(["init_workspace.py", str(ws)]) == 1
    out = capsys.readouterr().out
    assert any("INVALID" in line and "bad.md" in line for line in out.splitlines())


def test_init_main_fails_nonzero_on_dangling_link(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    ws = tmp_path / "docs" / "design-harness"
    (ws / "ideas").mkdir(parents=True)
    (ws / "ideas" / "dangler.md").write_text(
        "---\nid: dangler\ntype: idea\n---\n# d\n\n[gone](missing.md)\n",
        encoding="utf-8")
    assert init_main(["init_workspace.py", str(ws)]) == 1
    out = capsys.readouterr().out
    assert any("DANGLING" in line and "missing.md" in line for line in out.splitlines())


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
    real = Path(__file__).resolve().parents[1] / "docs" / "design-harness"
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


def test_parse_tags_accepts_yaml_block_list(workspace):
    (workspace / "ideas" / "block-tags.md").write_text(
        "---\nid: block-tags\ntype: idea\ntags:\n  - flow\n---\n# block list\n",
        encoding="utf-8")
    frontmatter = parse_frontmatter(
        (workspace / "ideas" / "block-tags.md").read_text(encoding="utf-8"))
    assert parse_tags(frontmatter) == ["flow"]
    assert check(workspace) == []


def test_single_tag_rule_sees_yaml_block_lists(workspace):
    (workspace / "ideas" / "block-two.md").write_text(
        "---\nid: block-two\ntype: idea\ntags:\n  - a\n  - b\n---\n# split me\n",
        encoding="utf-8")
    problems = check(workspace)
    assert any("block-two.md" in p and "at most one tag" in p for p in problems)


def test_check_flags_markdown_under_unknown_top_level_dir(workspace):
    (workspace / "source" / "papers").mkdir(parents=True)
    (workspace / "source" / "papers" / "lost.md").write_text(
        "# invisible to the canvas\n", encoding="utf-8")
    problems = check(workspace)
    assert any("source/papers/lost.md" in p and "unknown top-level" in p
               for p in problems)


def test_check_allows_root_level_files(workspace):
    (workspace / "target.md").write_text("# acceptance\n", encoding="utf-8")
    assert check(workspace) == []


def test_check_flags_unclosed_frontmatter(workspace):
    (workspace / "sources" / "papers" / "torn.md").write_text(
        "---\ntags: [x]\n# frontmatter never closes\n", encoding="utf-8")
    problems = check(workspace)
    assert any("torn.md" in p and "frontmatter" in p for p in problems)


def test_parse_conflicts_reads_optional_list_field():
    from workspace import parse_conflicts
    with_field = parse_frontmatter(
        "---\nid: x\ntype: idea\nconflicts: [a-card, b-card]\n---\n# t\n")
    without_field = parse_frontmatter("---\nid: x\ntype: idea\n---\n# t\n")
    assert parse_conflicts(with_field) == ["a-card", "b-card"]
    assert parse_conflicts(without_field) == []


def test_check_accepts_conflict_resolving_to_live_idea(workspace):
    (workspace / "ideas" / "challenger.md").write_text(
        "---\nid: challenger\ntype: idea\nconflicts: [idea-one]\n---\n"
        "# Challenger\n\nDisputes the first judgment.\n", encoding="utf-8")
    assert check(workspace) == []


def test_check_flags_unresolvable_conflict_target(workspace):
    (workspace / "ideas" / "challenger.md").write_text(
        "---\nid: challenger\ntype: idea\nconflicts: [no-such-id]\n---\n"
        "# Challenger\n\nDisputes a ghost.\n", encoding="utf-8")
    problems = check(workspace)
    assert any("challenger" in p and "no-such-id" in p for p in problems)


def test_check_flags_conflict_with_archived_target_as_adjudicated(workspace):
    (workspace / "ideas" / "challenger.md").write_text(
        "---\nid: challenger\ntype: idea\nconflicts: [idea-old]\n---\n"
        "# Challenger\n\nDisputes a settled judgment.\n", encoding="utf-8")
    problems = check(workspace)
    assert any("idea-old" in p and "adjudicated" in p for p in problems)


def test_check_flags_self_conflict(workspace):
    (workspace / "ideas" / "challenger.md").write_text(
        "---\nid: challenger\ntype: idea\nconflicts: [challenger]\n---\n"
        "# Challenger\n\nDisputes itself.\n", encoding="utf-8")
    problems = check(workspace)
    assert any("challenger" in p and "itself" in p for p in problems)


def test_check_flags_conflicts_field_outside_ideas(workspace):
    (workspace / "sources" / "papers" / "delta.md").write_text(
        "---\nconflicts: [idea-one]\n---\n# Delta paper\n\nA source never contends.\n",
        encoding="utf-8")
    problems = check(workspace)
    assert any("delta.md" in p and "conflicts" in p for p in problems)


def test_check_ignores_conflicts_on_archived_cards(workspace):
    (workspace / "ideas" / "archive" / "idea-settled.md").write_text(
        "---\nid: idea-settled\ntype: idea\nconflicts: [no-such-id]\n---\n"
        "# Settled\n\nHistory keeps its frontmatter.\n", encoding="utf-8")
    assert check(workspace) == []
