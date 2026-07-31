#!/usr/bin/env python3
"""Render a standardized 1242x1656 Worksona SVG and optional PNG/caption."""

from __future__ import annotations

import argparse
import base64
import hashlib
import html
import json
import mimetypes
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

from validate_profile import load_profile, validate_profile


WIDTH = 1242
HEIGHT = 1656
INK = "#15333A"
PAPER = "#FBF6E8"
CORAL = "#FF7B6B"
FONT = "'PingFang SC','Noto Sans CJK SC','Microsoft YaHei','Arial',sans-serif"

CJK_BREAK_AFTER = frozenset("，。！？；：、”’」』】》）")
CJK_FORBIDDEN_START = frozenset("，。！？；：、）》】」』”’…")
CJK_FORBIDDEN_END = frozenset("（《【「『“‘")
CJK_NUMERALS = frozenset("零〇一二三四五六七八九十百千万亿两")
CJK_PROTECTED_TERMS = (
    "聊天记录",
    "工作模式",
    "隐藏技能",
    "常见工伤",
    "本人声明",
    "顺手改一下",
    "还原",
    "十二",
    "真实需求",
    "研究",
    "直接运行",
    "可运行",
    "交付",
    "验收条件",
    "默认兜底人",
    "容易",
    "擅自补全",
    "无限续杯",
    "人设",
)

PALETTES = {
    "spongebob": ("#FFD84D", "#79D9D4"),
    "squidward": ("#77C9C5", "#C7A6E8"),
    "patrick": ("#F59BB3", "#BEE66C"),
    "sandy": ("#D69A55", "#82D2E8"),
    "mr-krabs": ("#E55755", "#74D4BC"),
    "plankton": ("#78B75D", "#9A7DDA"),
    "karen": ("#87B8FF", "#FF8097"),
    "gary": ("#8FCFD4", "#F3A4B9"),
    "mrs-puff": ("#EBC68F", "#7C9DCD"),
    "pearl": ("#F5A7C8", "#8DD8E8"),
    "larry": ("#E85D4A", "#F4C84B"),
    "bubble-bass": ("#B79C6B", "#89BF94"),
}


def color_mix(hex_color: str, white_ratio: float = 0.72) -> str:
    value = hex_color.lstrip("#")
    rgb = [int(value[index:index + 2], 16) for index in (0, 2, 4)]
    mixed = [round(channel * (1 - white_ratio) + 255 * white_ratio) for channel in rgb]
    return "#" + "".join(f"{channel:02X}" for channel in mixed)


def text_width_units(value: str) -> float:
    units = 0.0
    for char in value:
        if char.isspace():
            units += 0.34
        elif ord(char) < 128:
            units += 0.56 if char.isalnum() else 0.45
        else:
            units += 1.0
    return units


def tokenize(value: str) -> list[str]:
    tokens: list[str] = []
    current = ""
    mode = ""
    for char in value.strip():
        char_mode = "space" if char.isspace() else "ascii" if ord(char) < 128 and (char.isalnum() or char in "_-'%") else "char"
        if char_mode in {"space", "ascii"} and char_mode == mode:
            current += char
        else:
            if current:
                tokens.append(current)
            current = char
            mode = char_mode
    if current:
        tokens.append(current)
    return tokens


def break_splits_protected_term(value: str, index: int) -> bool:
    for term in CJK_PROTECTED_TERMS:
        start = value.find(term)
        while start >= 0:
            if start < index < start + len(term):
                return True
            start = value.find(term, start + 1)
    return False


def balanced_cjk_two_lines(value: str, max_units: float) -> list[str] | None:
    """Find a readable two-line CJK split when the full text fits in two lines."""
    compact = value.strip()
    if len(compact) < 2:
        return None

    candidates: list[tuple[float, str, str]] = []
    minimum_line = max_units * 0.30
    for index in range(1, len(compact)):
        left = compact[:index].rstrip()
        right = compact[index:].lstrip()
        if not left or not right:
            continue
        left_units = text_width_units(left)
        right_units = text_width_units(right)
        if left_units > max_units or right_units > max_units:
            continue

        previous = compact[index - 1]
        following = compact[index]
        penalty = abs(left_units - right_units)
        if min(left_units, right_units) < minimum_line:
            penalty += (minimum_line - min(left_units, right_units)) * 2.5
        if previous in CJK_BREAK_AFTER:
            penalty -= max_units * 0.48
        if following in CJK_FORBIDDEN_START or previous in CJK_FORBIDDEN_END:
            penalty += max_units * 4
        if previous.isascii() and following.isascii() and previous.isalnum() and following.isalnum():
            penalty += max_units * 4
        if previous in CJK_NUMERALS and following in CJK_NUMERALS:
            penalty += max_units * 4
        if break_splits_protected_term(compact, index):
            penalty += max_units * 4
        candidates.append((penalty, left, right))

    if not candidates:
        return None
    _, left, right = min(candidates, key=lambda item: item[0])
    return [left, right]


def wrap_text(value: str, width_px: float, font_size: float, max_lines: int) -> list[str]:
    max_units = width_px / font_size
    lines: list[str] = []
    line = ""
    for token in tokenize(value):
        candidate = line + token
        if line and text_width_units(candidate) > max_units:
            lines.append(line.rstrip())
            line = token.lstrip()
        else:
            line = candidate
    if line or not lines:
        lines.append(line.rstrip())

    cjk_count = sum(1 for char in value if ord(char) >= 128)
    visible_count = sum(1 for char in value if not char.isspace())
    cjk_dominant = bool(visible_count and cjk_count / visible_count >= 0.55)

    if max_lines == 2 and len(lines) >= 2 and cjk_dominant:
        balanced = balanced_cjk_two_lines(value, max_units)
        if balanced:
            lines = balanced

    if len(lines) > max_lines:
        lines = lines[:max_lines]
        last = lines[-1]
        while last and text_width_units(last + "…") > max_units:
            last = last[:-1]
        lines[-1] = last.rstrip() + "…"

    if len(lines) >= 2 and cjk_dominant and max_lines != 2:
        target = max_units * 0.34
        previous = lines[-2]
        last = lines[-1]
        while text_width_units(last) < target and len(previous) > 5:
            last = previous[-1] + last
            previous = previous[:-1].rstrip()
        lines[-2] = previous
        lines[-1] = last
    return lines


def text_block(
    x: float,
    y: float,
    width: float,
    value: str,
    size: int,
    line_height: int,
    max_lines: int,
    weight: int = 700,
    fill: str = INK,
    anchor: str = "start",
    letter_spacing: float = 0,
) -> str:
    lines = wrap_text(str(value), width, size, max_lines)
    rows = []
    for index, line in enumerate(lines):
        row_y = y + index * line_height
        rows.append(
            f'<text x="{x}" y="{row_y}" fill="{fill}" font-family="{FONT}" '
            f'font-size="{size}" font-weight="{weight}" text-anchor="{anchor}" '
            f'letter-spacing="{letter_spacing}">{html.escape(line)}</text>'
        )
    return "".join(rows)


DEFAULT_AVATAR_IDS = {
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


def resolve_avatar(
    profile_path: Path,
    avatar_value: str | None,
    skill_root: Path,
    character_id: str | None = None,
    image_mode: str = "placeholder",
) -> Path:
    candidates: list[Path] = []
    if avatar_value:
        raw = Path(avatar_value).expanduser()
        if raw.is_absolute():
            candidates.append(raw)
        else:
            candidates.extend([
                profile_path.parent / raw,
                skill_root / raw,
                skill_root / "assets" / raw,
                Path.cwd() / raw,
            ])
    if image_mode == "fan" and character_id in DEFAULT_AVATAR_IDS:
        candidates.append(skill_root / "assets" / "default-avatars" / f"{character_id}.png")
    candidates.append(skill_root / "assets" / "avatar-placeholder.svg")
    for candidate in candidates:
        if candidate.is_file():
            return candidate.resolve()
    raise FileNotFoundError("No usable avatar or bundled placeholder found")


def data_uri(path: Path) -> str:
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


def serial_for(profile: dict[str, Any]) -> str:
    if profile.get("serial"):
        return str(profile["serial"]).upper()
    payload = json.dumps(profile, ensure_ascii=False, sort_keys=True).encode("utf-8")
    digest = hashlib.sha1(payload).hexdigest()[:8].upper()
    return f"BWS-{digest}"


def receipt_copy(confidence: str) -> tuple[str, str, str]:
    if confidence == "low":
        return "证据先露馅了", "EARLY RECEIPTS", "当前证据在这三处先露馅："
    return "聊天记录把我卖了", "CHAT RECEIPTS", "聊天记录就是在这三处把我卖了："


def field_card(x: int, y: int, width: int, height: int, label: str, english: str, value: str, tint: str) -> str:
    parts = [
        f'<rect x="{x + 12}" y="{y + 12}" width="{width}" height="{height}" rx="30" fill="{INK}"/>',
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="30" fill="{tint}" stroke="{INK}" stroke-width="7"/>',
        f'<rect x="{x + 24}" y="{y + 20}" width="190" height="43" rx="21" fill="{INK}"/>',
        text_block(x + 119, y + 50, 165, label, 22, 26, 1, 800, PAPER, "middle"),
        text_block(x + width - 24, y + 48, 230, english, 18, 22, 1, 700, INK, "end", 1.4),
        text_block(x + 28, y + 102, width - 56, value, 30, 39, 2, 750, INK),
    ]
    return "".join(parts)


def build_svg(profile: dict[str, Any], profile_path: Path, skill_root: Path) -> str:
    accent_default, secondary_default = PALETTES[profile["character_id"]]
    accent = profile.get("accent", accent_default)
    secondary = profile.get("secondary", secondary_default)
    accent_light = color_mix(accent, 0.70)
    secondary_light = color_mix(secondary, 0.68)
    image_mode = profile.get("image_mode", "placeholder")
    masthead = "BIKINI BOTTOM // WORKSONA FILE" if image_mode in {"licensed", "fan"} else "BENTHIC WORKFORCE // WORKSONA FILE"
    disclaimer = {
        "fan": "粉丝向人格娱乐内容 · 与版权方无隶属或授权关系",
        "licensed": "角色素材按用户声明的授权范围使用",
        "original": "原创海底打工人格 · 非官方角色商品",
        "placeholder": "人格娱乐内容 · 角色图为中性占位",
    }.get(image_mode, "人格娱乐内容 · 非科学测评")

    avatar_path = resolve_avatar(
        profile_path,
        profile.get("avatar"),
        skill_root,
        str(profile.get("character_id", "")),
        str(image_mode),
    )
    avatar_uri = data_uri(avatar_path)
    serial = serial_for(profile)
    score = int(profile["match_score"])
    battery = int(profile["battery"])
    battery_track_width = 220
    battery_width = round(battery_track_width * battery / 100)
    battery_fill = (
        f'<rect x="286" y="1514" width="{battery_width}" height="26" rx="13" fill="{accent}"/>'
        if battery_width > 0
        else ""
    )
    confidence_map = {"low": "低样本", "medium": "中等", "high": "高"}
    confidence_label = confidence_map[profile["confidence"]]
    receipt_label, receipt_english, _ = receipt_copy(profile["confidence"])

    tags = profile["signal_tags"]
    tag_widths = [max(126, min(176, 52 + len(str(tag)) * 28)) for tag in tags]
    tag_total = sum(tag_widths) + 24 * 2
    tag_x = 826 - tag_total / 2
    tag_parts = []
    for tag, tag_width in zip(tags, tag_widths):
        tag_parts.append(f'<rect x="{tag_x}" y="526" width="{tag_width}" height="52" rx="26" fill="{PAPER}" stroke="{INK}" stroke-width="5"/>')
        tag_parts.append(text_block(tag_x + tag_width / 2, 561, tag_width - 24, str(tag), 23, 26, 1, 800, INK, "middle"))
        tag_x += tag_width + 24

    evidence_parts = []
    evidence_y = [952, 1004, 1056]
    for index, (value, y) in enumerate(zip(profile["evidence"], evidence_y), start=1):
        evidence_parts.extend([
            f'<circle cx="126" cy="{y - 9}" r="20" fill="{INK}"/>',
            text_block(126, y - 1, 28, str(index), 20, 22, 1, 900, PAPER, "middle"),
            text_block(166, y, 930, str(value), 27, 32, 1, 700, INK),
        ])

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{WIDTH}" height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">
  <defs>
    <pattern id="grain" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="5" cy="6" r="1.6" fill="{INK}" opacity="0.065"/>
      <circle cx="17" cy="15" r="1.2" fill="{INK}" opacity="0.045"/>
    </pattern>
    <clipPath id="avatar-clip"><rect x="88" y="216" width="400" height="380" rx="34"/></clipPath>
  </defs>
  <rect width="{WIDTH}" height="{HEIGHT}" fill="{secondary_light}"/>
  <circle cx="70" cy="120" r="24" fill="none" stroke="{INK}" stroke-width="6" opacity="0.25"/>
  <circle cx="1182" cy="220" r="34" fill="none" stroke="{INK}" stroke-width="7" opacity="0.22"/>
  <circle cx="36" cy="1420" r="46" fill="none" stroke="{INK}" stroke-width="8" opacity="0.18"/>
  <circle cx="1201" cy="1518" r="19" fill="none" stroke="{INK}" stroke-width="5" opacity="0.22"/>
  <rect x="72" y="72" width="1112" height="1560" rx="50" fill="{INK}"/>
  <rect x="54" y="50" width="1112" height="1560" rx="50" fill="{PAPER}" stroke="{INK}" stroke-width="10"/>
  <rect x="54" y="50" width="1112" height="1560" rx="50" fill="url(#grain)"/>

  <rect x="88" y="84" width="1044" height="98" rx="28" fill="{INK}"/>
  {text_block(120, 145, 650, masthead, 28, 32, 1, 850, PAPER, 'start', 1.2)}
  {text_block(1100, 145, 290, serial, 24, 28, 1, 750, PAPER, 'end', 1.4)}

  <rect x="102" y="230" width="400" height="380" rx="34" fill="{INK}"/>
  <image x="88" y="216" width="400" height="380" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatar-clip)" href="{avatar_uri}" xlink:href="{avatar_uri}"/>
  <rect x="88" y="216" width="400" height="380" rx="34" fill="none" stroke="{INK}" stroke-width="8"/>

  <rect x="520" y="216" width="612" height="380" rx="36" fill="{accent}" stroke="{INK}" stroke-width="8"/>
  <rect x="548" y="242" width="272" height="46" rx="23" fill="{INK}"/>
  {text_block(684, 274, 244, '角色原型 · CHARACTER', 20, 24, 1, 800, PAPER, 'middle', 0.6)}
  {text_block(548, 332, 430, str(profile['character_name']), 34, 42, 2, 800, INK)}
  <circle cx="1044" cy="312" r="62" fill="{PAPER}" stroke="{INK}" stroke-width="7"/>
  {text_block(1044, 307, 90, str(score), 42, 44, 1, 900, INK, 'middle')}
  {text_block(1044, 338, 96, 'MATCH', 16, 18, 1, 800, INK, 'middle', 1.5)}
  {text_block(548, 410, 520, str(profile['display_name']), 44, 48, 1, 850, INK)}
  {text_block(548, 471, 530, str(profile['worksona_title']), 56, 63, 2, 900, INK)}
  {''.join(tag_parts)}

  <rect x="102" y="642" width="1044" height="190" rx="34" fill="{INK}"/>
  <rect x="88" y="626" width="1044" height="190" rx="34" fill="{CORAL}" stroke="{INK}" stroke-width="8"/>
  <rect x="116" y="652" width="212" height="44" rx="22" fill="{INK}"/>
  {text_block(222, 682, 190, '本 人 工 位 声 明', 20, 24, 1, 850, PAPER, 'middle', 1.8)}
  {text_block(122, 746, 966, '“' + str(profile['tagline']) + '”', 44, 52, 3, 900, INK)}

  <rect x="88" y="850" width="1044" height="232" rx="34" fill="{secondary_light}" stroke="{INK}" stroke-width="8"/>
  <rect x="116" y="866" width="292" height="44" rx="22" fill="{INK}"/>
  {text_block(262, 897, 264, receipt_label, 21, 24, 1, 850, PAPER, 'middle')}
  {text_block(1104, 897, 280, receipt_english, 18, 22, 1, 750, INK, 'end', 1.2)}
  {''.join(evidence_parts)}

  {field_card(88, 1114, 510, 164, '打工模式', 'WORK MODE', str(profile['work_mode']), accent_light)}
  {field_card(622, 1114, 510, 164, '隐藏技能', 'SECRET SKILL', str(profile['hidden_skill']), secondary_light)}
  {field_card(88, 1300, 510, 164, '常见工伤', 'OFFICE DAMAGE', str(profile['workplace_wound']), secondary_light)}
  {field_card(622, 1300, 510, 164, '本人声明', 'BOUNDARY LINE', str(profile['boundary_line']), accent_light)}

  <rect x="88" y="1490" width="1044" height="74" rx="30" fill="{INK}"/>
  {text_block(118, 1537, 156, '今日剩余气泡', 22, 26, 1, 800, PAPER)}
  <rect x="286" y="1514" width="{battery_track_width}" height="26" rx="13" fill="{PAPER}" opacity="0.25"/>
  {battery_fill}
  <rect x="522" y="1506" width="82" height="42" rx="21" fill="{PAPER}"/>
  {text_block(563, 1535, 62, str(battery) + '%', 23, 26, 1, 900, INK, 'middle')}
  <line x1="636" y1="1508" x2="636" y2="1546" stroke="{PAPER}" stroke-width="2" opacity="0.22"/>
  {text_block(676, 1538, 250, '本周已补过的锅', 22, 26, 1, 800, PAPER)}
  {text_block(1098, 1540, 150, str(profile['patch_count']) + ' 口', 27, 30, 1, 900, accent, 'end')}

  {text_block(88, 1594, 740, disclaimer, 19, 22, 1, 650, INK)}
  {text_block(1132, 1594, 260, '证据置信度：' + confidence_label, 19, 22, 1, 750, INK, 'end')}
</svg>'''
    return svg


def write_caption(profile: dict[str, Any], path: Path) -> None:
    title = profile.get("share_title") or f"Agent 说我是「{profile['worksona_title']}」"
    hook = profile.get("share_hook") or f"最扎心的不是像 {profile['character_name']}，而是这句："
    _, _, receipt_intro = receipt_copy(profile["confidence"])
    coverage_note = str(profile.get("coverage_note", "")).strip()
    if coverage_note:
        evidence_scope = f"这次只让 Agent 根据{coverage_note}来判断"
    else:
        evidence_scope = "这次只让 Agent 根据当前可见、且我明确授权的对话来判断"
    hashtags = "#打工人 #人设卡 #AgentSkills #职场情绪 #海底打工人格"
    if profile.get("image_mode") in {"licensed", "fan"}:
        hashtags += " #海绵宝宝"
    caption = f"""# {title}

{evidence_scope}，它给我的打工人格是：{profile['worksona_title']}。

{hook}
“{profile['tagline']}”

{receipt_intro}
① {profile['evidence'][0]}
② {profile['evidence'][1]}
③ {profile['evidence'][2]}

隐藏技能：{profile['hidden_skill']}
常见工伤：{profile['workplace_wound']}

本人现在决定把这句贴在工位上：
“{profile['boundary_line']}”

你觉得自己更像谁？要不要也让 Agent 根据你授权的对话翻一下？

{hashtags}
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(caption, encoding="utf-8")


def run_command(command: list[str]) -> bool:
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False, text=True)
    except OSError:
        return False
    return result.returncode == 0


def export_png(svg_path: Path, png_path: Path) -> tuple[bool, str]:
    png_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        import cairosvg  # type: ignore

        cairosvg.svg2png(url=str(svg_path), write_to=str(png_path), output_width=WIDTH, output_height=HEIGHT)
        return png_path.is_file(), "cairosvg"
    except Exception:
        pass

    if shutil.which("rsvg-convert") and run_command(["rsvg-convert", "-w", str(WIDTH), "-h", str(HEIGHT), "-o", str(png_path), str(svg_path)]):
        return png_path.is_file(), "rsvg-convert"
    if shutil.which("magick") and run_command(["magick", "-background", "none", str(svg_path), "-resize", f"{WIDTH}x{HEIGHT}!", str(png_path)]):
        return png_path.is_file(), "ImageMagick"
    if shutil.which("inkscape") and run_command(["inkscape", str(svg_path), "--export-type=png", f"--export-filename={png_path}", f"--export-width={WIDTH}", f"--export-height={HEIGHT}"]):
        return png_path.is_file(), "Inkscape"
    if shutil.which("sips") and run_command(["sips", "-s", "format", "png", str(svg_path), "--out", str(png_path)]):
        return png_path.is_file(), "sips"

    if shutil.which("qlmanage"):
        with tempfile.TemporaryDirectory(prefix="worksona-preview-") as temp_dir:
            if run_command(["qlmanage", "-t", "-s", str(HEIGHT), "-o", temp_dir, str(svg_path)]):
                candidates = sorted(Path(temp_dir).glob("*.png"))
                if candidates:
                    shutil.copy2(candidates[0], png_path)
                    return True, "qlmanage"
    return False, "none"


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a Bikini Bottom Worksona social card.")
    parser.add_argument("--input", required=True, type=Path, help="Validated profile JSON")
    parser.add_argument("--output", required=True, type=Path, help="Output SVG path")
    parser.add_argument("--png", type=Path, help="Optional PNG output path")
    parser.add_argument("--caption", type=Path, help="Optional Markdown sharing caption")
    args = parser.parse_args()

    try:
        profile = load_profile(args.input)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    errors = validate_profile(profile)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    skill_root = Path(__file__).resolve().parent.parent
    try:
        svg = build_svg(profile, args.input.resolve(), skill_root)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(svg, encoding="utf-8")
    print(f"SVG: {args.output} ({WIDTH}x{HEIGHT})")

    if args.caption:
        write_caption(profile, args.caption)
        print(f"CAPTION: {args.caption}")

    if args.png:
        exported, engine = export_png(args.output.resolve(), args.png.resolve())
        if exported:
            print(f"PNG: {args.png} ({engine})")
        else:
            print("WARNING: PNG rasterizer unavailable; SVG remains the portable final.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
