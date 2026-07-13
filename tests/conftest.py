import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "plugins/design-harness/skills/design-harness/scripts"))

XSS_TITLE = 'Evil </script><script>alert(1)</script> <img src=x onerror=alert(2)>'


@pytest.fixture
def workspace(tmp_path):
    root = tmp_path / "ws"

    def card(rel, title, body="", frontmatter=""):
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        fm = f"---\n{frontmatter}\n---\n" if frontmatter else ""
        path.write_text(f"{fm}# {title}\n\n{body}\n", encoding="utf-8")
        return path

    card("sources/papers/alpha.md", "Alpha paper",
         "Alpha claims something measurable.",
         frontmatter="tags: [evidence]")
    card("sources/papers/beta.md", "Beta paper",
         "Beta refines [alpha](alpha.md). External [link](https://example.com/x.md).")
    card("sources/github/gamma.md", "Gamma repo", "A repo card, no frontmatter.")
    card("sources/papers/evil.md", XSS_TITLE,
         "Body with </script> escape attempt and <img src=x onerror=alert(3)>.")
    card("ideas/idea-one.md", "First judgment",
         "Stands on [alpha](../sources/papers/alpha.md).",
         frontmatter="id: idea-one\ntype: idea\ntags: [positioning]")
    card("ideas/idea-two.md", "Second judgment",
         "Builds on [idea one](idea-one.md) and [gamma](../sources/github/gamma.md).",
         frontmatter="id: idea-two\ntype: idea")
    card("ideas/archive/idea-old.md", "Retired judgment",
         "Superseded; kept for the trail.",
         frontmatter="id: idea-old\ntype: idea\ntags: [positioning]")
    card("board/first-compare.md", "Alpha vs Gamma",
         "One board, one comparison. Weighs [alpha](../sources/papers/alpha.md) "
         "against [gamma](../sources/github/gamma.md) via [idea one](../ideas/idea-one.md).")
    (root / "board/index.md").write_text("# board index (projection)\n", encoding="utf-8")
    (root / "sources/index.md").write_text("# sources index (projection)\n", encoding="utf-8")
    (root / "ideas/index.md").write_text("# ideas index (projection)\n", encoding="utf-8")
    (root / "output").mkdir()
    (root / "output/index.md").write_text("# output index (projection)\n", encoding="utf-8")
    (root / "index.md").write_text("# workspace entry\n", encoding="utf-8")
    (root / "target.md").write_text("# target\n", encoding="utf-8")
    (root / "logs.md").write_text("# logs\n", encoding="utf-8")
    return root
