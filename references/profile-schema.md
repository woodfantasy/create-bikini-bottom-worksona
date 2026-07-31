# Worksona Profile Schema

Save UTF-8 JSON. Reject unknown structured objects, but allow optional scalar fields for future versions.

## Required fields

| Field | Type | Constraint | Card purpose |
|---|---|---|---|
| `schema_version` | string | exactly `1.0` | renderer compatibility |
| `language` | string | e.g. `zh-CN`, `en` | copy and labels |
| `display_name` | string | 1–24 chars | identity |
| `character_id` | string | roster id | palette and mapping |
| `character_name` | string | 1–30 chars | canonical or approved display name |
| `worksona_title` | string | 2–18 CJK chars or 2–36 Latin chars | primary share identity |
| `match_score` | integer | 55–97 | playful match strength |
| `confidence` | string | `low`, `medium`, `high` | evidence quality |
| `tagline` | string | max 42 CJK or 84 Latin chars | repostable emotional line |
| `evidence` | array[string] | exactly 3; each max 30 CJK or 60 Latin chars | three shareable chat receipts selected from a larger internal evidence ledger |
| `work_mode` | string | max 34 CJK or 68 Latin chars | recurring work behavior |
| `hidden_skill` | string | max 34 CJK or 68 Latin chars | concrete strength |
| `workplace_wound` | string | max 34 CJK or 68 Latin chars | the way reliability gets punished |
| `boundary_line` | string | max 34 CJK or 68 Latin chars | self-advocacy line |
| `battery` | integer | 0–100 | comic energy stat |
| `patch_count` | integer | 0–99 | comic “pots patched” stat |
| `signal_tags` | array[string] | exactly 3; each 2–8 CJK or 2–18 Latin chars | thumbnail-readable traits |

## Optional fields

| Field | Type | Meaning |
|---|---|---|
| `secondary_character` | string | close secondary match |
| `serial` | string | defaults to deterministic profile hash |
| `avatar` | string | local PNG, JPG, WebP, or SVG path |
| `accent` | string | `#RRGGBB`; overrides roster accent |
| `secondary` | string | `#RRGGBB`; overrides roster secondary |
| `source_note` | string | short evidence limitation, not private quotes |
| `coverage_note` | string | short, privacy-safe summary of inspected conversation coverage |
| `image_mode` | string | `licensed`, `fan`, `original`, or `placeholder` |
| `share_title` | string | optional Xiaohongshu title |
| `share_hook` | string | optional first line of caption |

## Example

```json
{
  "schema_version": "1.0",
  "language": "zh-CN",
  "display_name": "Ivan",
  "character_id": "spongebob",
  "character_name": "海绵宝宝",
  "worksona_title": "深海全自动补锅机",
  "match_score": 92,
  "confidence": "high",
  "tagline": "不是我爱加班，是每个坑都刚好长成了我的工位。",
  "evidence": [
    "把模糊想法拆成可执行清单",
    "追到交付闭环才肯收工",
    "一边吐槽一边把事情救回来"
  ],
  "work_mode": "先把现场救回来，再研究是谁挖的坑",
  "hidden_skill": "把“顺手改一下”还原成十二项真实需求",
  "workplace_wound": "越靠谱，越容易成为默认兜底人",
  "boundary_line": "我可以负责，但不接受无限续杯。",
  "battery": 37,
  "patch_count": 8,
  "signal_tags": ["负责到底", "细节雷达", "苦中作梗"],
  "image_mode": "placeholder",
  "avatar": "assets/avatar-placeholder.svg"
}
```

Run `python3 scripts/validate_profile.py <profile.json>` before rendering.

The `evidence` field is intentionally limited to three card-sized receipts for readability. It is **not** the extraction limit: keep the fuller 18–36-note evidence ledger in temporary analysis notes, with source coverage and contradictions, and never publish private source text in the profile or caption.
