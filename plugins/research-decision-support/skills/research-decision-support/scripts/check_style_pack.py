import json
import re
import sys
from pathlib import Path

CANONICAL_TOKENS = (
    "surface", "page", "ink", "ink-2", "muted", "grid", "ring", "wash",
    "accent-a", "accent-b", "accent-c", "accent-d", "positive",
)
USAGE_KEYS = (
    "reading-order", "never-bulk-read", "single-file",
    "no-external-requests", "sanitize-untrusted", "dual-scheme",
)
ENUMS = {
    "formality": {"formal", "neutral", "playful"},
    "density": {"compact", "comfortable", "spacious"},
    "scheme": {"light", "dark", "dual"},
}
ENTRY_SCALARS = ("slug", "name", "tagline", "tone", "formality", "density", "scheme")
ENTRY_LISTS = ("mood", "best_for", "avoid_for")
SLUG_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")
COLOR_RE = re.compile(
    r"^(#[0-9a-fA-F]{3}|#[0-9a-fA-F]{6}|#[0-9a-fA-F]{8}"
    r"|(rgba?|hsla?)\(\s*\d{1,3}(\.\d+)?\s*(,\s*\d{1,3}(\.\d+)?%?\s*){2}(,\s*(0|1|0?\.\d+)\s*)?\))$"
)
FORBIDDEN_REACH = (
    "http://", "https://", "@import", "<script", "<iframe",
    "javascript:", "url(//", 'src="//', "src='//",
)
DESIGN_SECTIONS = (
    "## Atmosphere", "## Accent roles", "## Signature moves", "## Do / Don't",
)
PREVIEW_SECTIONS = ("## Palette", "## Typography", "## Signature moves", "## Fit")
INDEX_MAX_BYTES = 8192
PREVIEW_MAX_BYTES = 4096
TOP_LINE = re.compile(r"^([A-Za-z0-9-]+):\s*(.*)$")
SUB_LINE = re.compile(r"^  ([A-Za-z0-9-]+):\s*(.*)$")


def unquote(value):
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse_frontmatter(text):
    problems = []
    if not text.startswith("---\n"):
        return {}, ["missing frontmatter"]
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, ["unterminated frontmatter"]
    data = {}
    block = None
    for line in text[4:end].split("\n"):
        if not line.strip():
            continue
        if "\t" in line:
            problems.append("tab character in frontmatter")
            continue
        top = TOP_LINE.match(line)
        if top:
            key, value = top.group(1), unquote(top.group(2).strip())
            if value:
                data[key] = value
                block = None
            else:
                data[key] = {}
                block = data[key]
            continue
        sub = SUB_LINE.match(line)
        if sub:
            if block is None:
                problems.append(f"indented line outside a block: {line.strip()}")
                continue
            key, value = sub.group(1), unquote(sub.group(2).strip())
            if not value:
                problems.append(f"nested deeper than two levels at: {key}")
                continue
            block[key] = value
            continue
        problems.append(f"unparseable frontmatter line: {line.strip()}")
    return data, problems


def check_reach(rel, text):
    lowered = text.lower()
    return [f"{rel}: forbidden external reach: {marker}"
            for marker in FORBIDDEN_REACH if marker in lowered]


def check_palette(rel, name, block):
    if not isinstance(block, dict):
        return [f"{rel}: {name} must be a token block"]
    problems = [f"{rel}: {name} missing canonical token: {token}"
                for token in CANONICAL_TOKENS if token not in block]
    problems += [f"{rel}: {name}.{token} illegal color value: {value}"
                 for token, value in block.items() if not COLOR_RE.match(value)]
    return problems


def check_design(rel, text, slug):
    frontmatter, problems = parse_frontmatter(text)
    problems = [f"{rel}: {p}" for p in problems]
    for field in ("slug", "name", "version", "scheme"):
        if not frontmatter.get(field):
            problems.append(f"{rel}: missing required field: {field}")
    if frontmatter.get("slug") and frontmatter["slug"] != slug:
        problems.append(f"{rel}: frontmatter slug '{frontmatter['slug']}' != directory '{slug}'")
    scheme = frontmatter.get("scheme")
    if isinstance(scheme, str) and scheme not in ENUMS["scheme"]:
        problems.append(f"{rel}: scheme '{scheme}' not in {sorted(ENUMS['scheme'])}")
    for name in ("colors-light", "colors-dark"):
        if name not in frontmatter:
            problems.append(f"{rel}: missing required block: {name}")
        else:
            problems += check_palette(rel, name, frontmatter[name])
    aliases = frontmatter.get("color-aliases", {})
    if isinstance(aliases, dict):
        problems += [f"{rel}: color alias '{alias}' -> unknown token '{target}'"
                     for alias, target in aliases.items() if target not in CANONICAL_TOKENS]
    for name in ("typography", "components"):
        if not isinstance(frontmatter.get(name), dict) or not frontmatter.get(name):
            problems.append(f"{rel}: missing required block: {name}")
    body = text[text.find("\n---\n", 4) + 5:] if text.startswith("---\n") else text
    problems += [f"{rel}: missing required section: {section}"
                 for section in DESIGN_SECTIONS if section not in body]
    return problems


def check_preview(rel, text, design_size):
    problems = []
    if not text.startswith("# "):
        problems.append(f"{rel}: first line must be a '# ' title")
    size = len(text.encode("utf-8"))
    if size > PREVIEW_MAX_BYTES:
        problems.append(f"{rel}: preview exceeds {PREVIEW_MAX_BYTES} bytes ({size})")
    if size >= design_size:
        problems.append(f"{rel}: preview must be smaller than its design.md")
    problems += [f"{rel}: missing required section: {section}"
                 for section in PREVIEW_SECTIONS if section not in text]
    return problems


def safe_relpath(value):
    return (isinstance(value, str) and value and ".." not in value
            and not value.startswith("/") and "\\" not in value)


def nonempty_str_list(value):
    return (isinstance(value, list) and value
            and all(isinstance(item, str) and item for item in value))


def check_entry(entry):
    problems = []
    slug = entry.get("slug", "(missing slug)")
    label = f"selection-index.json: style '{slug}'"
    for field in ENTRY_SCALARS:
        if not isinstance(entry.get(field), str) or not entry.get(field):
            problems.append(f"{label}: missing field: {field}")
    for field in ENTRY_LISTS:
        if not nonempty_str_list(entry.get(field)):
            problems.append(f"{label}: field must be a nonempty list: {field}")
    for field, allowed in ENUMS.items():
        value = entry.get(field)
        if isinstance(value, str) and value and value not in allowed:
            problems.append(f"{label}: {field} '{value}' not in {sorted(allowed)}")
    if isinstance(entry.get("slug"), str) and not SLUG_RE.match(entry["slug"]):
        problems.append(f"{label}: slug fails pattern [a-z0-9][a-z0-9-]*")
    for field in ("preview", "design"):
        if not safe_relpath(entry.get(field)):
            problems.append(f"{label}: unsafe or missing path in field: {field}")
    renderings = entry.get("canvas_renderings")
    if renderings is not None:
        if not nonempty_str_list(renderings):
            problems.append(f"{label}: canvas_renderings must be a nonempty string list")
        else:
            problems += [f"{label}: canvas_renderings slug fails pattern: {canvas}"
                         for canvas in renderings if not SLUG_RE.match(canvas)]
    return problems


CSS_TOKEN_DEF = re.compile(r"--([a-z0-9-]+)\s*:")
DARK_BLOCK = re.compile(r"@media[^{]*prefers-color-scheme:\s*dark[^{]*\{(.*?)\}\s*\}",
                        re.DOTALL)


def check_canvas_css(rel, text):
    # A compiled canvas.css is a build artifact of design.md for the unified
    # canvas: it must define every canonical token in its light :root and again
    # in a prefers-color-scheme:dark override, and may never reach the network.
    problems = check_reach(rel, text)
    if text.count("{") != text.count("}"):
        problems.append(f"{rel}: unbalanced braces")
    root = re.search(r":root\s*\{([^}]*)\}", text)
    light_tokens = set(CSS_TOKEN_DEF.findall(root.group(1))) if root else set()
    problems += [f"{rel}: light :root missing canonical token: --{token}"
                 for token in CANONICAL_TOKENS if token not in light_tokens]
    dark = DARK_BLOCK.search(text)
    dark_tokens = set(CSS_TOKEN_DEF.findall(dark.group(1))) if dark else set()
    if not dark:
        problems.append(f"{rel}: missing prefers-color-scheme dark palette block")
    else:
        problems += [f"{rel}: dark palette missing canonical token: --{token}"
                     for token in CANONICAL_TOKENS if token not in dark_tokens]
    return problems


def check_canvas_renderings(rel, entry, design_text):
    # The multi-canvas selector is retired: only the unified canvas exists, so a
    # canvas_renderings entry is legacy metadata — sections it names must still
    # resolve inside the design, but no canvas directory lookup remains.
    renderings = entry.get("canvas_renderings")
    if not nonempty_str_list(renderings):
        return []
    problems = []
    for canvas in renderings:
        if not SLUG_RE.match(canvas):
            continue
        if f"### {canvas}" not in design_text:
            problems.append(f"{rel}: missing rendering section for canvas: ### {canvas}")
    return problems


def check(pack_root):
    pack = Path(pack_root).resolve()
    index_path = pack / "selection-index.json"
    if not index_path.is_file():
        return ["selection-index.json: missing"]
    index_text = index_path.read_text(encoding="utf-8")
    try:
        index = json.loads(index_text)
    except ValueError as error:
        return [f"selection-index.json: invalid JSON: {error}"]

    problems = check_reach("selection-index.json", index_text)
    if len(index_text.encode("utf-8")) > INDEX_MAX_BYTES:
        problems.append(f"selection-index.json: index exceeds {INDEX_MAX_BYTES} bytes")
    if not index.get("version"):
        problems.append("selection-index.json: missing version")
    usage = index.get("usage", {})
    problems += [f"selection-index.json: usage missing rule: {key}"
                 for key in USAGE_KEYS
                 if not isinstance(usage.get(key), str) or not usage.get(key)]
    entries = index.get("styles", [])
    if not isinstance(entries, list) or not entries:
        problems.append("selection-index.json: styles must be a nonempty list")
        entries = []

    slugs = [e.get("slug") for e in entries if isinstance(e.get("slug"), str)]
    problems += [f"selection-index.json: duplicate slug: {slug}"
                 for slug in sorted({s for s in slugs if slugs.count(s) > 1})]
    for entry in entries:
        problems += check_entry(entry)

    indexed = set(slugs)
    on_disk = {child.name for child in pack.iterdir() if child.is_dir()}
    problems += [f"selection-index.json: style '{slug}' has no directory"
                 for slug in sorted(indexed - on_disk)]
    problems += [f"{slug}: directory not listed in selection-index.json"
                 for slug in sorted(on_disk - indexed)]

    entries_by_slug = {entry.get("slug"): entry for entry in entries}
    for slug in sorted(indexed & on_disk):
        design_path = pack / slug / "design.md"
        preview_path = pack / slug / "preview.md"
        for path in (design_path, preview_path):
            if not path.is_file():
                problems.append(f"{slug}/{path.name}: missing")
        if not design_path.is_file() or not preview_path.is_file():
            continue
        design_text = design_path.read_text(encoding="utf-8")
        preview_text = preview_path.read_text(encoding="utf-8")
        problems += check_reach(f"{slug}/design.md", design_text)
        problems += check_reach(f"{slug}/preview.md", preview_text)
        problems += check_design(f"{slug}/design.md", design_text, slug)
        problems += check_preview(f"{slug}/preview.md", preview_text,
                                  len(design_text.encode("utf-8")))
        problems += check_canvas_renderings(
            f"{slug}/design.md", entries_by_slug[slug], design_text)
        canvas_css = pack / slug / "canvas.css"
        if canvas_css.is_file():
            problems += check_canvas_css(
                f"{slug}/canvas.css", canvas_css.read_text(encoding="utf-8"))
    return problems


def main(argv):
    default = Path(__file__).resolve().parent.parent / "canvas" / "styles"
    pack = argv[1] if len(argv) > 1 else default
    problems = check(pack)
    for problem in problems:
        print(f"INVALID {problem}")
    print(f"{'ok: style pack conforms' if not problems else f'{len(problems)} problem(s)'}")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
