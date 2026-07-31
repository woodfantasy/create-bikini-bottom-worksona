# Conversation Analysis Rubric

## Evidence order

Use evidence in this order:

1. Repeated choices and corrections across multiple turns.
2. How the user frames goals, constraints, risks, and quality.
3. How the user reacts when work is incomplete or ambiguous.
4. Self-description supplied for this analysis.
5. Vocabulary, punctuation, or one-off jokes only as weak supporting evidence.

Never treat message length, grammar, language fluency, response speed, or device metadata as intelligence or personality.

## Score ten observable dimensions

Score each dimension from 0 to 4. Use `2` when evidence is mixed or absent.

| Dimension | 0 | 2 | 4 |
|---|---|---|---|
| drive | avoids ownership | completes assigned work | volunteers, rescues, persists |
| structure | improvises freely | mixes planning and action | specifies fields, order, checks |
| warmth | transactional | polite and balanced | relational, encouraging, team-first |
| skepticism | accepts defaults | verifies important claims | challenges assumptions and asks for proof |
| optimism | expects friction | pragmatic | visibly enthusiastic and possibility-led |
| ambition | protects scope | moderate goals | expands vision, growth, status, or impact |
| autonomy | seeks direction | collaborates | independently defines and drives the path |
| risk-control | tolerates uncertainty | checks key risks | anticipates failure, policy, privacy, safety |
| expressiveness | restrained | context-dependent | vivid humor, emotion, identity language |
| ease | urgency/strain | steady | relaxed, unhurried, low-friction |

Record one short evidence note for every non-neutral score. Paraphrase private content instead of quoting it.

## Rank characters

Compare the observed vector with the target vectors below. Treat these as anchors, not clinical categories.

| Character | drive | structure | warmth | skepticism | optimism | ambition | autonomy | risk-control | expressive | ease |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| spongebob | 4 | 3 | 4 | 1 | 4 | 2 | 3 | 2 | 4 | 1 |
| squidward | 2 | 3 | 1 | 4 | 0 | 1 | 3 | 3 | 3 | 1 |
| patrick | 1 | 0 | 4 | 1 | 3 | 0 | 2 | 0 | 3 | 4 |
| sandy | 4 | 4 | 3 | 3 | 3 | 3 | 4 | 4 | 2 | 1 |
| mr-krabs | 4 | 3 | 2 | 4 | 2 | 4 | 4 | 4 | 3 | 1 |
| plankton | 4 | 3 | 1 | 4 | 3 | 4 | 4 | 2 | 4 | 0 |
| karen | 3 | 4 | 2 | 4 | 1 | 3 | 4 | 4 | 1 | 2 |
| gary | 3 | 4 | 3 | 3 | 2 | 1 | 4 | 4 | 0 | 3 |
| mrs-puff | 3 | 4 | 3 | 4 | 1 | 1 | 3 | 4 | 3 | 0 |
| pearl | 2 | 2 | 3 | 2 | 3 | 3 | 2 | 1 | 4 | 2 |
| larry | 4 | 2 | 3 | 1 | 4 | 3 | 3 | 1 | 3 | 2 |
| bubble-bass | 2 | 3 | 1 | 4 | 1 | 2 | 3 | 3 | 3 | 1 |

Calculate a rough fit by subtracting the average absolute dimension gap from 4, then normalize to 0–100. Use judgment to break ties with repeated evidence and the character descriptions. Do not imply mathematical precision.

Apply these adjustments:

- Add up to 5 points when a repeated behavior strongly matches the character's workplace pattern.
- Subtract up to 8 points when the character would contradict an explicit user boundary or self-description.
- Keep final scores between 55 and 97.
- Select a secondary character when its score is within 5 points of the primary.

## Assign confidence

| Confidence | Evidence |
|---|---|
| high | 12+ meaningful messages across at least 3 topics, with repeated signals |
| medium | 5–11 messages or many messages from one narrow task |
| low | fewer than 5 meaningful messages, mostly pasted content, or conflicting signals |

State the limitation in one line when confidence is low. Never hide uncertainty behind a high match score.

## Quality check

Before finalizing, verify that:

- at least two evidence points describe behavior, not adjectives;
- the flattering strength and workplace wound are causally connected;
- the result sounds like the user, not a generic horoscope;
- the match would still make sense if the character name were temporarily hidden;
- no sensitive trait, diagnosis, or employer-specific secret appears.
