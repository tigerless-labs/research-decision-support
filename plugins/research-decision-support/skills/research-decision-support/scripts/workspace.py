import re
from pathlib import Path

LAYERS = ["sources", "ideas", "output", "board"]

_MD_LINK = re.compile(r"\]\(\s*([^)\s]+?\.md)(?:#[^)]*)?\s*\)")
_EXTERNAL = re.compile(r"^[a-z][a-z0-9+.-]*://")
_FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
_LIST_ITEM = re.compile(r"\s*-\s+(.+)")
_TITLE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
_LINK_TEXT = re.compile(r"\[([^\]]*)\]\([^)]*\)")
_SUMMARY_LIMIT = 280


def parse_frontmatter(text):
    match = _FRONTMATTER.match(text)
    if not match:
        return {}
    fields, items, pending = {}, {}, None
    for line in match.group(1).splitlines():
        bullet = _LIST_ITEM.match(line)
        if bullet and pending:
            items.setdefault(pending, []).append(bullet.group(1).strip())
        elif ":" in line and not line.startswith((" ", "\t")):
            key, _, value = line.partition(":")
            key = key.strip()
            fields[key] = value.strip()
            pending = None if fields[key] else key
        else:
            pending = None
    for key, values in items.items():
        fields[key] = "[" + ", ".join(values) + "]"
    return fields


def broken_frontmatter(text):
    return text.startswith("---\n") and not _FRONTMATTER.match(text)


def parse_tags(frontmatter):
    raw = frontmatter.get("tags", "")
    inner = raw[1:-1] if raw.startswith("[") and raw.endswith("]") else raw
    return [tag.strip().strip("'\"") for tag in inner.split(",") if tag.strip()]


def strip_frontmatter(text):
    return _FRONTMATTER.sub("", text, count=1)


def title_of(text, fallback):
    match = _TITLE.search(strip_frontmatter(text))
    return match.group(1).strip() if match else fallback


def first_paragraph(text):
    collected = []
    for line in strip_frontmatter(text).splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith(("#", "|", ">", "---", "```")):
            if collected:
                break
            continue
        collected.append(stripped)
    paragraph = _LINK_TEXT.sub(r"\1", " ".join(collected))
    return paragraph.replace("**", "").strip()[:_SUMMARY_LIMIT]


def card_files(workspace, layers=LAYERS):
    workspace = Path(workspace)
    for md in sorted(workspace.rglob("*.md")):
        rel = md.relative_to(workspace)
        if rel.name == "index.md" or rel.parts[0] not in layers:
            continue
        yield md, rel


def card_links(md, rel, workspace, known):
    for raw in _MD_LINK.findall(md.read_text(encoding="utf-8")):
        if _EXTERNAL.match(raw):
            continue
        target = (md.parent / raw).resolve()
        if not target.is_relative_to(workspace):
            continue
        target_rel = str(target.relative_to(workspace))
        if target_rel in known:
            yield target_rel


def local_md_targets(text):
    for raw in _MD_LINK.findall(text):
        if not _EXTERNAL.match(raw):
            yield raw
