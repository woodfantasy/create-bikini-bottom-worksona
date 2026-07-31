#!/usr/bin/env python3
"""Install this Skill into common agent discovery locations."""

from __future__ import annotations

import argparse
import shutil
import sys
from datetime import datetime
from pathlib import Path


SKILL_NAME = "create-bikini-bottom-worksona"
PERSONAL_ROOTS = {
    "codex": Path(".agents/skills"),
    "claude-code": Path(".claude/skills"),
    "antigravity": Path(".gemini/config/skills"),
    "openclaw": Path(".openclaw/skills"),
}
PROJECT_ROOTS = {
    "codex": Path(".agents/skills"),
    "claude-code": Path(".claude/skills"),
    "antigravity": Path(".agents/skills"),
    "openclaw": Path("skills"),
}
IGNORE_NAMES = {".git", ".DS_Store", "__pycache__", "dist", "output", ".pytest_cache"}


def ignored(_: str, names: list[str]) -> set[str]:
    return {name for name in names if name in IGNORE_NAMES or name.endswith(".pyc")}


def destination_for(host: str, scope: str, base: Path) -> Path:
    roots = PERSONAL_ROOTS if scope == "personal" else PROJECT_ROOTS
    return base / roots[host] / SKILL_NAME


def install_one(source: Path, destination: Path, force: bool, dry_run: bool) -> None:
    try:
        if source.resolve() == destination.resolve():
            raise RuntimeError(f"Refusing to install a Skill onto itself: {destination}")
    except FileNotFoundError:
        pass

    if dry_run:
        action = "replace with backup" if destination.exists() and force else "install"
        print(f"DRY RUN: {action} {source} -> {destination}")
        return

    destination.parent.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        if not force:
            raise RuntimeError(f"Destination already exists: {destination}. Re-run with --force to back it up and replace it.")
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        backup = destination.with_name(f"{destination.name}.backup-{timestamp}")
        destination.rename(backup)
        print(f"BACKUP: {backup}")

    staging = destination.with_name(f".{destination.name}.installing")
    if staging.exists():
        raise RuntimeError(f"Staging path already exists; inspect it before retrying: {staging}")
    try:
        shutil.copytree(source, staging, ignore=ignored)
        staging.rename(destination)
    except Exception:
        if staging.exists():
            shutil.rmtree(staging)
        raise
    print(f"INSTALLED: {destination}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Install this Skill for common agent hosts.")
    parser.add_argument("--target", choices=["all", *PERSONAL_ROOTS], default="all")
    parser.add_argument("--scope", choices=["personal", "project"], default="personal")
    parser.add_argument("--project-root", type=Path, help="Required for project scope")
    parser.add_argument("--home", type=Path, help="Override home directory for testing")
    parser.add_argument("--force", action="store_true", help="Back up and replace an existing installation")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    source = Path(__file__).resolve().parent.parent
    if not (source / "SKILL.md").is_file():
        print(f"ERROR: SKILL.md not found at {source}", file=sys.stderr)
        return 1

    if args.scope == "project":
        if not args.project_root:
            print("ERROR: --project-root is required for project scope", file=sys.stderr)
            return 1
        base = args.project_root.expanduser().resolve()
    else:
        base = (args.home or Path.home()).expanduser().resolve()

    hosts = list(PERSONAL_ROOTS) if args.target == "all" else [args.target]
    try:
        for host in hosts:
            destination = destination_for(host, args.scope, base)
            install_one(source, destination, args.force, args.dry_run)
    except (OSError, RuntimeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
