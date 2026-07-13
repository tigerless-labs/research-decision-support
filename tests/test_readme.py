import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
README = REPO / "README.md"
STYLES_INDEX = (
    REPO
    / "plugins/research-decision-support/skills/research-decision-support/canvas/styles/selection-index.json"
)


def readme_text():
    return README.read_text(encoding="utf-8")


def local_image_paths():
    text = readme_text()
    md_images = re.findall(r"!\[[^\]]*\]\(([^)\s]+)\)", text)
    html_images = re.findall(r'<img[^>]+src="([^"]+)"', text)
    return [p for p in md_images + html_images if not p.startswith("http")]


def test_readme_references_at_least_one_image_per_style():
    styles = json.loads(STYLES_INDEX.read_text(encoding="utf-8"))["styles"]
    assert len(local_image_paths()) > len(styles)


def test_readme_local_images_exist():
    paths = local_image_paths()
    assert paths
    for rel in paths:
        assert (REPO / rel).is_file(), rel


def test_readme_names_every_shipped_style():
    styles = json.loads(STYLES_INDEX.read_text(encoding="utf-8"))["styles"]
    text = readme_text()
    for style in styles:
        assert style["name"] in text, style["name"]


def test_readme_carries_install_and_usage():
    text = readme_text()
    assert "/plugin marketplace add tigerless-labs/research-decision-support" in text
    assert "/plugin install research-decision-support" in text
    assert "## Usage" in text
