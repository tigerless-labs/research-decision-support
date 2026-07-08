import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "plugins/research-decision-support/skills/research-decision-support/scripts"))

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
         "First paragraph of alpha.\n\nSecond paragraph.\n\nSee [beta](beta.md) and [beta again](beta.md).")
    card("sources/papers/beta.md", "Beta paper",
         "Beta claims something. External [link](https://example.com/x.md).")
    card("sources/github/gamma.md", "Gamma repo", "A repo card.")
    card("sources/papers/orphan.md", "Orphan paper", "Nobody links me.")
    card("sources/papers/evil.md", XSS_TITLE, "Body with </script> escape attempt.")
    card("synthesis/dir-one.md", "Direction one",
         "Covers [alpha](../sources/papers/alpha.md) and [beta](../sources/papers/beta.md).",
         frontmatter="id: dir-one\ntype: direction")
    card("synthesis/dir-two.md", "Direction two",
         "Covers [beta](../sources/papers/beta.md) and [gamma](../sources/github/gamma.md) and [evil](../sources/papers/evil.md).",
         frontmatter="id: dir-two\ntype: direction")
    card("ideas/idea-one.md", "My idea",
         "Because [alpha](../sources/papers/alpha.md) says so. Also [index](../sources/papers/index.md).",
         frontmatter="id: idea-one\ntype: idea\nstatus: 候选")
    card("ideas/idea-orphan.md", "Unused idea",
         "Cites [gamma](../sources/github/gamma.md) but no decision weighs it.",
         frontmatter="id: idea-orphan\ntype: idea\nstatus: 采纳")
    card("decisions/adr-one.md", "ADR: pick alpha",
         "Weighs [my idea](../ideas/idea-one.md).",
         frontmatter="id: adr-one\ntype: adr\nstatus: accepted")
    (root / "sources/papers/index.md").write_text("# not a card\n", encoding="utf-8")
    (root / "notes.md").write_text("# outside layers\n", encoding="utf-8")
    return root
