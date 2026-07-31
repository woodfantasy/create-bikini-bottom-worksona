---
name: create-bikini-bottom-worksona
description: Analyze a user's visible conversation style, work habits, and self-described personality; map the evidence to a SpongeBob/Bikini Bottom character archetype; and create a standardized, funny, empathetic worksona card plus Xiaohongshu-ready sharing copy. Use when users ask for a personality card, 人设卡, 打工人格, 海绵宝宝角色匹配, conversation-style analysis, social share card, or a visual that expresses being hardworking, overworked, unfairly blamed, or repeatedly asked to clean up other people's messes.
---

# Create Bikini Bottom Worksona

Turn observable conversation behavior into a defensible character match and a polished 3:4 social card. Keep the result playful and emotionally accurate without presenting it as psychological diagnosis.

## Load the right references

Read these files before drafting:

- Read [references/analysis-rubric.md](references/analysis-rubric.md) and [references/character-roster.md](references/character-roster.md) for every analysis.
- Read [references/conversation-sampling.md](references/conversation-sampling.md) when the host exposes multiple turns, searchable history, or a user-approved conversation export.
- Read [references/profile-schema.md](references/profile-schema.md) and [references/card-spec.md](references/card-spec.md) before creating card data or visuals.
- Read [references/avatar-system.md](references/avatar-system.md) before selecting, generating, or falling back to an avatar.
- Read [references/ip-privacy-safety.md](references/ip-privacy-safety.md) before selecting or generating imagery.
- Read [references/share-copy.md](references/share-copy.md) when the user wants Xiaohongshu copy, a carousel, or share hooks.
- Read [references/installation.md](references/installation.md) only when installing, packaging, or publishing this Skill.

## Follow the workflow

### 1. Establish the evidence boundary and corpus

Use the largest conversation corpus the current host actually exposes, not only the latest few messages. This may include every visible turn in the current thread, host-native conversation search results, or a user-approved export. Never imply access to hidden chats, deleted content, private account history, or another app.

First report the coverage you can actually inspect: number of interaction units, sessions or threads, topics, and time slices. An interaction unit is a user turn plus the relevant Agent reply and any user correction or acceptance. Read all available turns when the corpus is small; use the stratified sampling procedure in `references/conversation-sampling.md` when it is large.

When creating the profile, put a short privacy-safe coverage summary in optional `coverage_note` (for example, “当前线程 31 个互动单元，覆盖 4 类任务；未读取其他会话”). Never put names, source identifiers, or private quotes in this field.

If the accessible corpus is too thin for a reliable result, ask for one of these inputs:

- permission to use the host's conversation-search/history tool;
- a user-approved export covering roughly 20–60 representative interaction units across several topics and time periods;
- three short answers: “最常催 Agent 做什么？最受不了什么？最近替别人补过什么锅？”;
- a user-approved folder or host-provided conversation-search tool.

Continue with a clearly labeled low-confidence draft when the user prefers not to provide more context. Do not silently fill missing history from assumptions.

### 2. Extract behavioral signals

Build an internal evidence ledger of **18–36 distinct behavioral observations** when the corpus supports it; do not inflate the count with near-duplicates. Each observation should be a paraphrase tied to a source unit, topic/time slice, observed behavior, rubric dimensions, recurrence count, and contradiction note. Weight repeated patterns across independent sessions or topics above one-off wording. The card still compresses this ledger into exactly three shareable chat receipts.

Score the dimensions in the analysis rubric, rank the roster, and select:

- one primary character;
- one optional secondary character when the top two scores are close;
- a 0–100 match score rounded to a whole number;
- a confidence label: `low`, `medium`, or `high`.

Do not infer protected or sensitive traits. Do not diagnose mental health, intelligence, disability, or workplace performance.

### 3. Write the worksona

Produce all required fields from the profile schema. Make each field do a different job:

- `worksona_title`: an instantly legible workplace identity;
- `tagline`: the line users most want to repost;
- `evidence`: three specific reasons selected from the larger internal ledger;
- `work_mode`: how the user moves work forward;
- `hidden_skill`: a flattering, concrete superpower;
- `workplace_wound`: the recurring way reliability gets punished;
- `boundary_line`: a quotable boundary, not generic advice.

Write in the user's language unless asked otherwise. Match their humor intensity, but never humiliate them. Keep every card field within the character limits in the schema.

### 4. Choose an image mode

Apply the first suitable mode:

1. **Licensed mode** — Use rights-cleared character art supplied by the user or their organization.
2. **Personal fan-expression mode** — Use user-supplied imagery or a host image tool only for personal, non-commercial sharing; add the fan-made disclaimer. Load `references/avatar-system.md` and personalize the prompt with the selected role's anchor, top signal tags, work mood, and one workplace prop.
3. **Original archetype mode** — Default for public repositories, commercial work, or unclear rights. Use an original underwater office character and retain the textual character mapping separately.
4. **No-image-tool fallback** — For personal fan-expression mode, set `image_mode` to `fan` and omit `avatar` to resolve `assets/default-avatars/<character_id>.png` deterministically. For public, commercial, or uncertain-rights work, use an approved original/licensed asset or explicit `placeholder` mode instead.

Never copy marketplace screenshots, episode stills, logos, or third-party fan art into the Skill or public output repository. The bundled default pack is newly generated, unofficial fan-expression art; it is not a rights grant.

### 5. Build and render

Create a clean output directory outside the Skill folder. Save the normalized data as `worksona-profile.json`.

Validate it:

```bash
python3 scripts/validate_profile.py worksona-profile.json
```

Render the card and sharing caption:

```bash
python3 scripts/render_card.py \
  --input worksona-profile.json \
  --output worksona-card.svg \
  --png worksona-card.png \
  --caption worksona-caption.md
```

Treat SVG as the portable source of truth. The renderer exports PNG when a supported local rasterizer is available. If PNG export is unavailable, deliver the SVG and use the host's browser, screenshot, or image tool to rasterize it at 1242×1656.

### 6. Verify before delivery

Check all of the following:

- Confirm the image is 3:4 and, for PNG, exactly 1242×1656.
- Confirm no text clips, overlaps, or falls outside the safe area.
- Confirm the emotional line is readable at phone-thumbnail scale.
- Confirm the three evidence points come from visible or user-provided context and are representative of the larger evidence ledger.
- State the inspected coverage and confidence limitation in the handoff; do not equate message volume with certainty.
- Confirm the result does not reveal secrets, names, phone numbers, employer details, or verbatim private messages unless the user explicitly approved them.
- Confirm official character imagery is used only in a rights-appropriate mode.
- Confirm the card includes a low-key non-affiliation disclaimer when required.

Revise once when any check fails.

## Deliver the result

Return:

1. the primary card image (`PNG` when available, otherwise `SVG`);
2. the normalized profile JSON;
3. the Xiaohongshu-ready caption;
4. a two-sentence explanation of the match, inspected coverage, and confidence;
5. an invitation to “重抽一次” using the secondary character or a different humor intensity;
6. an anonymized evidence appendix only when the user asks for more detail, with private source text and source identifiers removed.

Avoid exposing internal scoring tables unless the user asks. Never call the result a scientific assessment.

## Example request

> 分析我在这段对话里的沟通风格，看看我最像哪个海绵宝宝角色。重点写出那种“事情全是我做，锅还是我背”的感觉，生成一张能发小红书的人设卡。
