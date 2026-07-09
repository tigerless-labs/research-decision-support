from check_workspace import check
from init_workspace import LAYERS, init


def test_init_creates_full_skeleton(tmp_path):
    root = tmp_path / "ws"
    created = init(root)
    assert created
    for layer in LAYERS:
        assert (root / layer).is_dir()
        assert (root / layer / "index.md").exists()
    assert (root / "index.md").exists()


def test_init_is_idempotent_and_never_clobbers(tmp_path):
    root = tmp_path / "ws"
    init(root)
    marker = root / "ideas" / "index.md"
    marker.write_text("# my customized index\n", encoding="utf-8")
    created = init(root)
    assert created == []
    assert marker.read_text(encoding="utf-8") == "# my customized index\n"


def test_check_passes_valid_workspace(workspace):
    assert check(workspace) == []


def test_check_flags_missing_required_field(workspace):
    bad = workspace / "decisions" / "bad.md"
    bad.write_text("---\nid: bad\ntype: decision\nstatus: open\n---\n# no affects\n", encoding="utf-8")
    problems = check(workspace)
    assert any("bad.md" in p and "affects" in p for p in problems)


def test_check_accepts_idea_without_status(workspace):
    (workspace / "ideas" / "bare.md").write_text(
        "---\nid: bare\ntype: idea\n---\n# existence means accepted\n", encoding="utf-8")
    assert check(workspace) == []


def test_design_dir_is_outside_the_schema(workspace):
    from build_map import collect
    (workspace / "design").mkdir()
    (workspace / "design" / "spine.md").write_text(
        "---\nid: spine\ntype: design\n---\n# retired layer\n", encoding="utf-8")
    assert check(workspace) == []
    ids = {n["id"] for n in collect(workspace)["nodes"]}
    assert "design/spine.md" not in ids
    assert "design" not in collect(workspace)["layers"]


def test_check_flags_out_of_enum_status(workspace):
    bad = workspace / "ideas" / "weird.md"
    bad.write_text("---\nid: weird\ntype: idea\nstatus: maybe\n---\n# x\n", encoding="utf-8")
    problems = check(workspace)
    assert any("weird.md" in p for p in problems)


def test_check_accepts_both_enum_vocabularies(workspace):
    (workspace / "ideas" / "en.md").write_text(
        "---\nid: en\ntype: idea\nstatus: adopted\n---\n# english enum\n", encoding="utf-8")
    (workspace / "ideas" / "zh.md").write_text(
        "---\nid: zh\ntype: idea\nstatus: 存疑\n---\n# chinese enum\n", encoding="utf-8")
    assert check(workspace) == []


def test_check_exempts_prose_source_cards(workspace):
    (workspace / "sources" / "papers" / "prose.md").write_text(
        "# a plain prose card\n\nno frontmatter at all\n", encoding="utf-8")
    assert check(workspace) == []


def test_example_workspace_is_valid():
    from pathlib import Path
    example = Path(__file__).resolve().parents[1] / "examples" / "autoharness"
    assert check(example) == []
