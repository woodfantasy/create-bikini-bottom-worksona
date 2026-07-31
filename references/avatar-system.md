# Avatar System

Use this reference whenever the card needs an avatar. It defines the visual contract for the twelve-role pack, image-generation prompts, and the no-image-tool fallback.

## Modes and fallback order

1. If the profile supplies a valid `avatar`, use it.
2. If `image_mode` is `fan` and no avatar is supplied, use `assets/default-avatars/<character_id>.png`.
3. If `image_mode` is `licensed` or `original` and no approved avatar is supplied, use the neutral placeholder or ask for a rights-cleared/original asset; never silently substitute fan art for commercial work.
4. Keep `assets/avatar-placeholder.svg` as an explicit rights-safe fallback for unknown roles, restricted hosts, and users who do not want fan imagery.

The bundled pack is newly generated, unofficial fan-expression art. It is not official character art, not a license, and not automatically safe for paid, branded, merchandise, or advertising use. Use `image_mode: fan` only for personal, non-commercial expression when the host policy permits it.

## Canonical anchors

These anchors are creative guardrails for recognizable mapping, not an official style guide or legal certification. Keep the role's core silhouette, colors, temperament, and workplace metaphor; do not invent a different personality just to fit the user's joke.

| `character_id` | Canonical anchor | Personalized prompt seed | Workplace prop / pose | Do not drift into |
|---|---|---|---|---|
| `spongebob` | porous yellow rectangular sponge, blue eyes, buck teeth, white shirt, red tie, brown shorts; eager optimism and service instinct | “Show an upbeat service-desk finisher turning `{top signal tags}` into cheerful follow-through.” | clipboard + small wrench; cheerful follow-through | cynicism, menace, burnout-as-identity |
| `squidward` | turquoise octopus, long nose, droopy eyelids, brown polo; artistic standards and dry frustration | “Show a dry, detail-sensitive reviewer protecting craft while carrying `{workplace_wound}`.” | approval stamp + clarinet at side; unimpressed review | cruelty, rage, random incompetence |
| `patrick` | pink starfish, rounded shape, green floral shorts; warmth, literal humor, relaxed pacing | “Show a warm, literal teammate finding an unexpectedly simple route through `{work_mode}`.” | mug + one sticky note; calm observation | helplessness, stupidity, childish mockery |
| `sandy` | brown squirrel, white suit, clear dome helmet, acorn cue; experiments, courage, independence | “Show an independent experimenter testing `{top signal tags}` with practical courage and a clear next step.” | blueprint + wrench; confident builder stance | unsafe science, macho posturing, aggression |
| `mr-krabs` | red crab, large claws, blue shirt, purple pants; ownership, resource awareness, bargaining energy | “Show a brisk resource owner negotiating scope, time, and `{workplace_wound}` without losing the team.” | ledger + calculator; brisk manager pose | exploitation praise, threat, greed caricature |
| `plankton` | tiny green one-eyed plankton, antennae, lab-coat inventor cue; ambition and persistence | “Show a tiny, persistent inventor turning `{top signal tags}` into an ambitious workaround.” | blueprint + miniature tool; dramatic solo-founder pose | deception, violence, villain worship |
| `karen` | green computer terminal with a screen face, keyboard and status lights; systems thinking and calm correction | “Show a composed operations console spotting the pattern in `{top signal tags}` and calmly correcting the plan.” | data card + pencil; composed operator pose | readable UI text, emotionless machine stereotype |
| `gary` | blue-green snail, pink shell, gentle observant eyes; quiet maintenance and steady follow-through | “Show a quiet keeper maintaining the small details that let `{work_mode}` keep moving.” | tiny wrench + office plant; low-key keeper pose | sadness, helplessness, gross-out comedy |
| `mrs-puff` | tan pufferfish, blue teacher outfit, small hat; caring instruction and failure awareness | “Show a caring coach turning a failed attempt into a safe, repeatable lesson about `{top signal tags}`.” | checklist + safety whistle; vigilant coach pose | panic ridicule, anxiety as a joke, incompetence |
| `pearl` | gray whale, pink top, expressive eyes; emotional honesty, social awareness, trend sensitivity | “Show a socially alert feedback radar translating `{top signal tags}` into an honest, shareable reaction.” | headphones + feedback card; vivid culture-radar pose | gender stereotypes, vanity-only framing, aggression |
| `larry` | muscular orange lobster, blue tank top; momentum, encouragement, visible progress | “Show an encouraging progress captain making `{work_mode}` feel energizing and visibly achievable.” | progress clipboard + whistle; energetic captain pose | body shaming, overwork worship, aggression |
| `bubble-bass` | large green fish, purple shirt, heavy-lidded exacting expression; edge-case hunting and acceptance testing | “Show an exacting reviewer finding the edge case hidden inside `{workplace_wound}`, with dry but fair focus.” | magnifying glass + checklist; dry reviewer pose | insults, body shaming, hostility |

## Personalization prompt template

Use the selected role's anchor plus the user's strongest recurring signals. Keep the user's name, employer, private messages, and exact card copy out of the image.

Start with the matching role's personalized prompt seed above, then fill the template below. The seed supplies the character-specific action; the template supplies the shared visual language and safety constraints.

```text
Use case: illustration-story
Asset type: square fallback avatar for a worksona card
Primary request: an original fan-expression portrait of {character anchor} as a {workplace archetype}
Scene/backdrop: simple turquoise underwater records office; sparse filing marks, bubbles, and coral
Subject: preserve {canonical anchor}; add only {top 2–3 signal tags} through {workplace prop/pose}
Style/medium: unified 2D editorial fan illustration, collectible employee-archive card, crisp ink outlines, subtle print texture
Composition/framing: square 1:1, centered chest-up portrait, generous padding, face and key prop away from crop edges
Lighting/mood: {humor intensity} and {work mood}; bright, readable, not grim
Constraints: no text, names, employers, logos, watermark, episode frame, copied screenshot, packaging, or extra characters
Avoid: {role-specific do-not-drift items}; distorted anatomy; cropped face; duplicated limbs; photorealism
```

Use `worksona_title`, `signal_tags`, `work_mode`, and `workplace_wound` to choose the prop and mood, not to add typography inside the avatar. If the host cannot generate images, skip the prompt and resolve the matching default asset deterministically by `character_id`.

## Quality check

- Verify the avatar is square or safely crop-able to the card's 4:3 window.
- Keep the face and defining prop inside a generous safe margin.
- Reject any output with text, logos, watermarks, episode screenshots, or a role/personality contradiction.
- Preview at card size; do not judge only from the full-resolution source.
- Keep the non-affiliation footer for `fan` mode and use original/licensed assets for commercial or uncertain-rights work.
