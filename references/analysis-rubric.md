# Conversation Analysis Rubric

## Evidence corpus and order

Use [conversation-sampling.md](conversation-sampling.md) to establish the accessible corpus before scoring. The internal ledger should contain 18–36 distinct observations when the corpus supports it; the profile's three `evidence` strings are only the final shareable compression.

Within the accessible corpus, use evidence in this order:

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

Record one short, source-linked paraphrase for every non-neutral score. Prefer notes that recur across independent sessions or topics. Preserve conflicting evidence instead of averaging it away. Never publish verbatim private content.

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
| high | 24+ meaningful interaction units across 4+ topic groups and 3 time slices when available; 12+ ledger notes show repeated behavior and no unresolved major contradiction |
| medium | 12–23 meaningful interaction units across 3+ topic groups, or 20+ units from one narrow topic; 8+ ledger notes with limited contradiction |
| low | fewer than 12 meaningful interaction units, a single narrow task, mostly pasted content, inaccessible history, or unresolved conflicting signals |

State the inspected coverage and limitation in one line. Never hide uncertainty behind a high match score, and never treat a long single thread as equivalent to cross-session evidence.

## Quality check

Before finalizing, verify that:

- at least two evidence points describe behavior, not adjectives;
- the internal ledger contains enough distinct, source-linked notes for the assigned confidence band;
- supporting and conflicting patterns have both been considered;
- the flattering strength and workplace wound are causally connected;
- the result sounds like the user, not a generic horoscope;
- the match would still make sense if the character name were temporarily hidden;
- no sensitive trait, diagnosis, or employer-specific secret appears.
