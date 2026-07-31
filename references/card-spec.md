# Social Card Design Specification

## Canvas

- Master size: **1242×1656 px**, exact 3:4 portrait.
- Color space: sRGB.
- Safe area: 72 px on every edge; keep critical text at least 92 px from the outer edge.
- Primary format: SVG source plus PNG export.
- Optional lightweight copy: 1080×1440 PNG derived from the master.

Do not mix aspect ratios within one Xiaohongshu carousel.

## Visual system

Use one fixed system across every character:

- warm paper base `#FBF6E8`;
- deep ink `#15333A` for all outlines and body text;
- 8–10 px outlines;
- rounded rectangles with 32–48 px radii;
- 14–18 px hard offset shadows, never blurred glassmorphism;
- sparse bubbles, ticket perforations, stamps, or underwater filing marks;
- one character accent, one secondary color, and one coral pop;
- subtle print grain only; keep text areas clean.

Aim for “collectible employee archive card,” not “children's party invitation.”

## Layout hierarchy

1. **Archive masthead** — universe label, serial, and small confidence marker.
2. **Identity block** — avatar, display name, character match, match score, worksona title, and three tags.
3. **Emotional billboard** — the `tagline`; it must remain readable in a feed thumbnail.
4. **Chat-receipt strip** — three numbered behavioral receipts under “聊天记录把我卖了”; use “这一句话先露馅了” for low-confidence profiles.
5. **Work fields** — four equal modules: 打工模式, 隐藏技能, 常见工伤, 本人声明.
6. **Stats/footer** — remaining battery, patch count, confidence, and low-key disclaimer.

Use short bilingual micro-labels only when they support the document-file aesthetic. Keep the meaningful copy in the user's primary language.

Maintain component spacing as a layout invariant:

- keep at least 12 px of clear space between the chat-receipt title pill and the first numbered badge;
- render percentages in a fixed-width value capsule beside the progress track, never floating past the track edge;
- keep at least 18 px between footer groups and use a divider when two statistics share one bar.

## Typography

Use this system stack so the SVG remains portable:

```text
"PingFang SC", "Noto Sans CJK SC", "Microsoft YaHei", "Arial", sans-serif
```

- Worksona title: 54–68 px, heavy.
- Tagline: 42–54 px, heavy, maximum 3 lines.
- Field values: 28–34 px, semibold, maximum 2–3 lines.
- Labels and metadata: 20–26 px.
- Never place body copy below 24 px on the 1242 px master.
- Use line height between 1.15 and 1.32.

Do not use condensed novelty fonts for Chinese body text.
Prefer punctuation-aware CJK line breaks. Do not begin a line with closing punctuation or split paired number expressions and common short compounds when another valid break exists.

## Avatar treatment

- Use a 4:3 or square crop inside a thick outlined window.
- Keep faces and key gestures away from the crop boundary.
- Add no text inside generated avatars.
- Use `assets/avatar-placeholder.svg` when art is unavailable.
- The bundled sample profile uses `assets/spongebob-fan-avatar.png` in explicit personal fan-expression mode; the placeholder remains the safe fallback.
- Never reuse the fan-expression sample avatar for commercial, paid, branded, or otherwise rights-sensitive outputs.
- Treat official character images according to `ip-privacy-safety.md`.

## Copy constraints

- Make the worksona title understandable without reading the rest of the card.
- Make the tagline the emotional share hook.
- Connect the strength and wound: “because I am good at X, people keep doing Y to me.”
- Avoid generic compliments such as “very responsible” without behavioral proof.
- Avoid direct insults toward managers, colleagues, or named employers.
- Avoid fake metrics that could be mistaken for real employment data; label battery and patch count as playful stats.

## Accessibility and quality

- Maintain at least 4.5:1 contrast for body text.
- Never encode the match only by color; always show the character name and score.
- Include useful alt text when the host supports it.
- Verify the rendered PNG dimensions with an image inspector.
- Inspect the final card visually at full size and at roughly 25% scale.

## Recommended share set

- Card 1: the main identity card.
- Card 2, optional: “聊天记录把我卖了” expanded with 3–5 paraphrased receipts.
- Card 3, optional: secondary-character rematch and “你是哪一种” call to action.

Keep every slide at 1242×1656 or every slide at 1080×1440.
