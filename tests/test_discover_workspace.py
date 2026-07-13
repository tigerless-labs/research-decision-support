import json

import check_workspace
import init_workspace
from discover_workspace import (CONFIG_RELPATH, DEFAULT_LOCATION, configured_workspace,
                                discover, looks_like_workspace, record_workspace)
from init_workspace import init


def host(tmp_path, workspace_rel=None):
    root = tmp_path / "host"
    root.mkdir()
    if workspace_rel:
        init(root / workspace_rel)
    return root


def test_initialized_workspace_satisfies_structural_check(tmp_path):
    root = host(tmp_path, "docs/design-harness")
    assert looks_like_workspace(root / "docs/design-harness")
    assert not looks_like_workspace(root)


def test_structural_check_rejects_impostor_directory(tmp_path):
    root = host(tmp_path)
    (root / "research" / "design-harness").mkdir(parents=True)
    assert not looks_like_workspace(root / "research" / "design-harness")
    assert discover(root) == []


def test_config_pointer_wins_over_default_location(tmp_path):
    root = host(tmp_path, "docs/design-harness")
    custom = root / "research" / "design-harness"
    init(custom)
    record_workspace(root, custom)
    found = discover(root)
    assert len(found) == 1
    assert found[0].resolve() == custom.resolve()


def test_stale_config_falls_back_to_default(tmp_path):
    root = host(tmp_path, "docs/design-harness")
    (root / CONFIG_RELPATH).parent.mkdir(parents=True)
    (root / CONFIG_RELPATH).write_text(
        json.dumps({"workspace": "gone/design-harness"}), encoding="utf-8")
    found = discover(root)
    assert len(found) == 1
    assert found[0].resolve() == (root / DEFAULT_LOCATION).resolve()


def test_malformed_config_fails_safe(tmp_path):
    root = host(tmp_path, "docs/design-harness")
    (root / CONFIG_RELPATH).parent.mkdir(parents=True)
    for garbage in ("not json {", "[]", json.dumps({"workspace": 7}), json.dumps({})):
        (root / CONFIG_RELPATH).write_text(garbage, encoding="utf-8")
        assert configured_workspace(root) is None
        found = discover(root)
        assert len(found) == 1
        assert found[0].resolve() == (root / DEFAULT_LOCATION).resolve()


def test_find_by_name_when_no_config_and_no_default(tmp_path):
    root = host(tmp_path, "research/design-harness")
    found = discover(root)
    assert len(found) == 1
    assert found[0].resolve() == (root / "research" / "design-harness").resolve()


def test_find_by_name_skips_hidden_and_dependency_dirs(tmp_path):
    root = host(tmp_path)
    init(root / ".claude" / "worktrees" / "x" / "docs" / "design-harness")
    init(root / "node_modules" / "pkg" / "design-harness")
    assert discover(root) == []


def test_many_candidates_reported_not_resolved(tmp_path):
    root = host(tmp_path, "research/design-harness")
    init(root / "notes" / "design-harness")
    found = discover(root)
    assert len(found) == 2
    assert {p.resolve() for p in found} == {
        (root / "research" / "design-harness").resolve(),
        (root / "notes" / "design-harness").resolve()}


def test_record_roundtrip_stores_relative_inside_root(tmp_path):
    root = host(tmp_path, "research/design-harness")
    workspace = root / "research" / "design-harness"
    config = record_workspace(root, workspace)
    stored = json.loads(config.read_text(encoding="utf-8"))["workspace"]
    assert not stored.startswith("/")
    assert configured_workspace(root).resolve() == workspace.resolve()


def test_record_roundtrip_stores_absolute_outside_root(tmp_path):
    root = host(tmp_path)
    outside = tmp_path / "elsewhere" / "design-harness"
    init(outside)
    config = record_workspace(root, outside)
    stored = json.loads(config.read_text(encoding="utf-8"))["workspace"]
    assert stored.startswith("/")
    assert configured_workspace(root).resolve() == outside.resolve()


def test_init_main_no_arg_adopts_existing_workspace(tmp_path, monkeypatch, capsys):
    root = host(tmp_path, "research/design-harness")
    monkeypatch.chdir(root)
    assert init_workspace.main(["init_workspace.py"]) == 0
    capsys.readouterr()
    assert not (root / DEFAULT_LOCATION).exists()
    assert configured_workspace(root).resolve() == (
        root / "research" / "design-harness").resolve()


def test_init_main_no_arg_bootstraps_default_and_records(tmp_path, monkeypatch, capsys):
    root = host(tmp_path)
    monkeypatch.chdir(root)
    assert init_workspace.main(["init_workspace.py"]) == 0
    capsys.readouterr()
    assert looks_like_workspace(root / DEFAULT_LOCATION)
    assert configured_workspace(root).resolve() == (root / DEFAULT_LOCATION).resolve()


def test_init_main_refuses_when_many_candidates(tmp_path, monkeypatch, capsys):
    root = host(tmp_path, "research/design-harness")
    init(root / "notes" / "design-harness")
    monkeypatch.chdir(root)
    assert init_workspace.main(["init_workspace.py"]) != 0
    capsys.readouterr()
    assert not (root / DEFAULT_LOCATION).exists()
    assert configured_workspace(root) is None


def test_init_main_explicit_arg_records_pointer(tmp_path, monkeypatch, capsys):
    root = host(tmp_path)
    monkeypatch.chdir(root)
    assert init_workspace.main(["init_workspace.py", "notes/design-harness"]) == 0
    capsys.readouterr()
    assert configured_workspace(root).resolve() == (
        root / "notes" / "design-harness").resolve()


def test_check_workspace_main_no_arg_uses_discovery(tmp_path, monkeypatch, capsys):
    root = host(tmp_path, "research/design-harness")
    bad = root / "research" / "design-harness" / "ideas" / "bad.md"
    bad.write_text("---\ntags: [x]\n---\n# no id, no type\n", encoding="utf-8")
    monkeypatch.chdir(root)
    assert check_workspace.main(["check_workspace.py"]) == 1
    out = capsys.readouterr().out
    assert "bad.md" in out


def test_check_workspace_main_no_arg_errors_when_nothing_found(tmp_path, monkeypatch, capsys):
    root = host(tmp_path)
    monkeypatch.chdir(root)
    assert check_workspace.main(["check_workspace.py"]) != 0
    capsys.readouterr()
