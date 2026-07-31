#!/usr/bin/env python3
"""Create a clean Claude-compatible zip of the Skill directory."""

from __future__ import annotations

import argparse
import sys
import zipfile
from pathlib import Path


EXCLUDED_PARTS = {".git", ".DS_Store", "__pycache__", "dist", "output", ".pytest_cache"}


def included(path: Path, root: Path) -> bool:
    relative = path.relative_to(root)
    return not any(part in EXCLUDED_PARTS or part.endswith(".pyc") for part in relative.parts)


def main() -> int:
    parser = argparse.ArgumentParser(description="Package this Skill as a clean zip archive.")
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    skill_file = root / "SKILL.md"
    if not skill_file.is_file():
        print(f"ERROR: Missing {skill_file}", file=sys.stderr)
        return 1

    output = args.output.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        print(f"ERROR: Refusing to overwrite existing archive: {output}", file=sys.stderr)
        return 1

    files = [path for path in root.rglob("*") if path.is_file() and included(path, root)]
    if not files:
        print("ERROR: No files found to package", file=sys.stderr)
        return 1

    with zipfile.ZipFile(output, "x", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(files):
            archive.write(path, path.relative_to(root).as_posix())

    print(f"PACKAGED: {output} ({len(files)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
