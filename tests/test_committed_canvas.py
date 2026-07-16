import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
CANVAS = REPO / "docs" / "canvas.html"
WORKSPACE = REPO / "docs" / "design-harness"


def git(*args):
    return subprocess.run(
        ["git", *args], cwd=REPO, capture_output=True, text=True
    )


def live_card_ids():
    ids = []
    for layer in ("ideas", "sources"):
        for card in (WORKSPACE / layer).rglob("*.md"):
            relative = card.relative_to(WORKSPACE / layer)
            if "archive" in relative.parts or card.name == "index.md":
                continue
            ids.append(card.stem)
    return ids


def test_committed_canvas_is_tracked():
    tracked = git("ls-files", "--", str(CANVAS.relative_to(REPO)))
    assert tracked.stdout.strip(), "docs/canvas.html must be committed"


def test_committed_canvas_is_not_gitignored():
    ignored = git("check-ignore", "-q", str(CANVAS.relative_to(REPO)))
    assert ignored.returncode != 0, "docs/canvas.html must not be gitignored"


def test_committed_canvas_projects_every_live_card():
    assert CANVAS.is_file()
    html = CANVAS.read_text(encoding="utf-8")
    ids = live_card_ids()
    assert ids
    missing = [card_id for card_id in ids if card_id not in html]
    assert not missing, f"canvas.html is stale, rebuild it: missing {missing}"
