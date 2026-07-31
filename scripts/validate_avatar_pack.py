#!/usr/bin/env python3
"""Validate the deterministic 12-role fallback avatar pack."""

from __future__ import annotations

import argparse
import struct
import sys
from pathlib import Path


AVATAR_IDS = {
    "spongebob",
    "squidward",
    "patrick",
    "sandy",
    "mr-krabs",
    "plankton",
    "karen",
    "gary",
    "mrs-puff",
    "pearl",
    "larry",
    "bubble-bass",
}
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def png_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    if data[:8] != PNG_SIGNATURE or len(data) < 24:
        raise ValueError("not a PNG")
    return struct.unpack(">II", data[16:24])


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the Worksona default avatar pack.")
    parser.add_argument(
        "directory",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "assets" / "default-avatars",
    )
    args = parser.parse_args()
    directory = args.directory.expanduser().resolve()
    errors: list[str] = []

    for avatar_id in sorted(AVATAR_IDS):
        path = directory / f"{avatar_id}.png"
        if not path.is_file():
            errors.append(f"missing avatar: {path.name}")
            continue
        try:
            width, height = png_size(path)
        except (OSError, ValueError) as exc:
            errors.append(f"{path.name}: {exc}")
            continue
        if width != height or width < 256:
            errors.append(f"{path.name}: expected square PNG >=256px, got {width}x{height}")

    unexpected = sorted(
        path.name
        for path in directory.glob("*")
        if path.is_file() and path.suffix.lower() == ".png" and path.stem not in AVATAR_IDS
    )
    if unexpected:
        errors.append("unexpected PNG assets: " + ", ".join(unexpected))

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"VALID: {len(AVATAR_IDS)} default avatars in {directory}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
