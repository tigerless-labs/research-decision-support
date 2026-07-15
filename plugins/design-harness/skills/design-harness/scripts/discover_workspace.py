import json
import sys
from pathlib import Path

WORKSPACE_DIR_NAME = "design-harness"
CONFIG_RELPATH = Path(".design-harness") / "config.json"
DEFAULT_LOCATION = Path("docs") / WORKSPACE_DIR_NAME
SCAN_SKIP_DIRS = {".git", ".claude", ".design-harness", "node_modules",
                  "__pycache__", ".venv", "venv"}
REQUIRED_DIRS = ("sources", "ideas", "output")
REQUIRED_FILES = ("logs.md",)


def looks_like_workspace(path):
    path = Path(path)
    return (all((path / d).is_dir() for d in REQUIRED_DIRS)
            and all((path / f).is_file() for f in REQUIRED_FILES))


def configured_workspace(root):
    config_file = Path(root) / CONFIG_RELPATH
    if not config_file.is_file():
        return None
    try:
        stored = json.loads(config_file.read_text(encoding="utf-8")).get("workspace")
    except (json.JSONDecodeError, AttributeError):
        return None
    if not isinstance(stored, str) or not stored:
        return None
    candidate = Path(stored)
    if not candidate.is_absolute():
        candidate = Path(root) / candidate
    return candidate if looks_like_workspace(candidate) else None


def existing_config(config_file):
    if not config_file.is_file():
        return {}
    try:
        loaded = json.loads(config_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return loaded if isinstance(loaded, dict) else {}


def record_workspace(root, workspace):
    root, workspace = Path(root).resolve(), Path(workspace).resolve()
    config_file = root / CONFIG_RELPATH
    config_file.parent.mkdir(parents=True, exist_ok=True)
    stored = (workspace.relative_to(root).as_posix()
              if workspace.is_relative_to(root) else str(workspace))
    config = existing_config(config_file)
    config["workspace"] = stored
    config_file.write_text(
        json.dumps(config, indent=2) + "\n", encoding="utf-8")
    return config_file


def candidates_by_name(root):
    root = Path(root)
    found = []
    for path in sorted(root.rglob(WORKSPACE_DIR_NAME)):
        relative_parts = path.relative_to(root).parts
        if any(part in SCAN_SKIP_DIRS for part in relative_parts[:-1]):
            continue
        if path.is_dir() and looks_like_workspace(path):
            found.append(path)
    return found


def discover(root="."):
    root = Path(root)
    configured = configured_workspace(root)
    if configured:
        return [configured]
    default = root / DEFAULT_LOCATION
    if looks_like_workspace(default):
        return [default]
    return candidates_by_name(root)


def resolve_or_report(root="."):
    found = discover(root)
    if len(found) == 1:
        return found[0]
    if not found:
        print("no workspace found: pass the workspace path explicitly, "
              "or bootstrap one with init_workspace.py")
    else:
        print(f"{len(found)} candidate workspaces — pass one explicitly:")
        for candidate in found:
            print(f"  {candidate}")
    return None


def main(argv):
    root = argv[1] if len(argv) > 1 else "."
    workspace = resolve_or_report(root)
    if workspace is None:
        return 1
    print(workspace)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
