import json
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PLUGIN_ROOT = REPO / "plugins/design-harness"
CLAUDE_MANIFEST = PLUGIN_ROOT / ".claude-plugin/plugin.json"
CODEX_MANIFEST = PLUGIN_ROOT / ".codex-plugin/plugin.json"
CLAUDE_MARKETPLACE = REPO / ".claude-plugin/marketplace.json"
CODEX_MARKETPLACE = REPO / ".agents/plugins/marketplace.json"
SKILL_MD = PLUGIN_ROOT / "skills/design-harness/SKILL.md"


def load(path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_codex_manifest_exists():
    assert CODEX_MANIFEST.is_file()


def test_manifests_share_identity():
    claude, codex = load(CLAUDE_MANIFEST), load(CODEX_MANIFEST)
    for field in ("name", "version", "description", "license"):
        assert claude[field] == codex[field], field
    assert claude["author"]["name"] == codex["author"]["name"]


def test_codex_manifest_skills_pointer_resolves_to_skill():
    codex = load(CODEX_MANIFEST)
    skills = codex["skills"]
    assert skills.startswith("./")
    skills_dir = PLUGIN_ROOT / skills
    assert skills_dir.is_dir()
    assert any(skills_dir.rglob("SKILL.md"))


def test_codex_marketplace_entry_resolves_and_matches_manifest():
    market = load(CODEX_MARKETPLACE)
    codex = load(CODEX_MANIFEST)
    entries = [p for p in market["plugins"] if p["name"] == codex["name"]]
    assert len(entries) == 1
    entry = entries[0]
    source_path = entry["source"]["path"]
    assert source_path.startswith("./")
    assert (REPO / source_path / ".codex-plugin/plugin.json").is_file()
    assert entry["policy"]["installation"] == "AVAILABLE"
    assert "authentication" in entry["policy"]
    assert entry["category"]


def test_marketplaces_agree_on_plugin_set():
    claude_names = {p["name"] for p in load(CLAUDE_MARKETPLACE)["plugins"]}
    codex_names = {p["name"] for p in load(CODEX_MARKETPLACE)["plugins"]}
    assert claude_names == codex_names


def test_skill_md_carries_no_host_specific_command_paths():
    text = SKILL_MD.read_text(encoding="utf-8")
    body = text.split("---", 2)[2]
    assert "CLAUDE_SKILL_DIR" not in body


def test_skill_md_asks_for_target_at_bootstrap_and_again_at_assembly():
    body = SKILL_MD.read_text(encoding="utf-8").split("---", 2)[2]
    workflow = body.split("## Workflow")[1]
    discover_step = workflow.split("**Ingest evidence**")[0]
    assert "target.md" in discover_step
    assert "ask" in discover_step
    assemble_step = workflow.split("**Assemble**")[1].split("**Project and deliver**")[0]
    assert "target.md" in assemble_step
    assert "ask" in assemble_step


def test_skill_md_ties_delivery_target_to_registry():
    body = SKILL_MD.read_text(encoding="utf-8").split("---", 2)[2]
    delivery_step = body.split("build_canvas.py")[1]
    assert '"canvas"' in delivery_step
    assert "config.json" in delivery_step


def test_readme_carries_codex_install():
    text = (REPO / "README.md").read_text(encoding="utf-8")
    assert "codex plugin marketplace add tigerless-labs/design-harness" in text
