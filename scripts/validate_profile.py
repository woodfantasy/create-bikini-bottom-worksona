#!/usr/bin/env python3
"""Validate a Bikini Bottom Worksona profile using only Python stdlib."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


CHARACTER_IDS = {
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

REQUIRED_TYPES = {
    "schema_version": str,
    "language": str,
    "display_name": str,
    "character_id": str,
    "character_name": str,
    "worksona_title": str,
    "match_score": int,
    "confidence": str,
    "tagline": str,
    "evidence": list,
    "work_mode": str,
    "hidden_skill": str,
    "workplace_wound": str,
    "boundary_line": str,
    "battery": int,
    "patch_count": int,
    "signal_tags": list,
}

TEXT_LIMITS = {
    "display_name": 24,
    "character_name": 30,
    "worksona_title": 36,
    "tagline": 84,
    "work_mode": 68,
    "hidden_skill": 68,
    "workplace_wound": 68,
    "boundary_line": 68,
    "secondary_character": 30,
    "serial": 32,
    "source_note": 120,
    "coverage_note": 160,
    "share_title": 80,
    "share_hook": 120,
}


def load_profile(path: Path) -> dict[str, Any]:
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ValueError(f"Cannot read profile: {exc}") from exc
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}") from exc
    if not isinstance(data, dict):
        raise ValueError("Profile root must be a JSON object")
    return data


def validate_profile(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    for field, expected in REQUIRED_TYPES.items():
        if field not in data:
            errors.append(f"Missing required field: {field}")
            continue
        value = data[field]
        if expected is int and isinstance(value, bool):
            errors.append(f"{field} must be an integer, not a boolean")
        elif not isinstance(value, expected):
            errors.append(f"{field} must be {expected.__name__}")

    if errors:
        return errors

    if data["schema_version"] != "1.0":
        errors.append("schema_version must be exactly '1.0'")
    if not data["language"].strip():
        errors.append("language cannot be blank")
    if data["character_id"] not in CHARACTER_IDS:
        errors.append("character_id must be one of: " + ", ".join(sorted(CHARACTER_IDS)))
    if not 55 <= data["match_score"] <= 97:
        errors.append("match_score must be between 55 and 97")
    if data["confidence"] not in {"low", "medium", "high"}:
        errors.append("confidence must be low, medium, or high")
    if not 0 <= data["battery"] <= 100:
        errors.append("battery must be between 0 and 100")
    if not 0 <= data["patch_count"] <= 99:
        errors.append("patch_count must be between 0 and 99")

    for field, limit in TEXT_LIMITS.items():
        if field not in data:
            continue
        value = data[field]
        if not isinstance(value, str):
            errors.append(f"{field} must be a string")
            continue
        if not value.strip():
            errors.append(f"{field} cannot be blank")
        if len(value) > limit:
            errors.append(f"{field} is too long ({len(value)} > {limit} characters)")

    for field in ("display_name", "character_name", "worksona_title", "tagline", "work_mode", "hidden_skill", "workplace_wound", "boundary_line"):
        if isinstance(data.get(field), str) and not data[field].strip():
            errors.append(f"{field} cannot be blank")

    evidence = data["evidence"]
    if len(evidence) != 3:
        errors.append("evidence must contain exactly 3 items")
    for index, value in enumerate(evidence):
        if not isinstance(value, str) or not value.strip():
            errors.append(f"evidence[{index}] must be a non-empty string")
        elif len(value) > 60:
            errors.append(f"evidence[{index}] is too long ({len(value)} > 60 characters)")

    tags = data["signal_tags"]
    if len(tags) != 3:
        errors.append("signal_tags must contain exactly 3 items")
    for index, value in enumerate(tags):
        if not isinstance(value, str) or not value.strip():
            errors.append(f"signal_tags[{index}] must be a non-empty string")
        elif len(value) > 18:
            errors.append(f"signal_tags[{index}] is too long ({len(value)} > 18 characters)")

    for field in ("accent", "secondary"):
        value = data.get(field)
        if value is not None and (not isinstance(value, str) or not re.fullmatch(r"#[0-9A-Fa-f]{6}", value)):
            errors.append(f"{field} must be a #RRGGBB color")

    mode = data.get("image_mode")
    if mode is not None and mode not in {"licensed", "fan", "original", "placeholder"}:
        errors.append("image_mode must be licensed, fan, original, or placeholder")

    for field, value in data.items():
        if field not in REQUIRED_TYPES and field not in {
            "secondary_character",
            "serial",
            "avatar",
            "accent",
            "secondary",
            "source_note",
            "coverage_note",
            "image_mode",
            "share_title",
            "share_hook",
        } and isinstance(value, (dict, list)):
            errors.append(f"Unknown structured field is not supported: {field}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a worksona profile JSON file.")
    parser.add_argument("profile", type=Path)
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    try:
        data = load_profile(args.profile)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    errors = validate_profile(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    if not args.quiet:
        print(f"VALID: {args.profile} ({data['character_id']}, {data['match_score']}%)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
