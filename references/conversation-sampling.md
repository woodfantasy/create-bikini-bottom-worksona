# Conversation Sampling and Confidence

Use this reference whenever more than one thread, a searchable history tool, or a user-approved conversation export is available. The goal is to measure a durable interaction style without pretending the Agent can see private history it cannot access.

## Evidence boundary

1. Inventory only sources the host exposes or the user explicitly authorizes.
2. Prefer the current thread, then host-native search/history, then an approved export. Never scan unrelated folders, browser history, credentials, or another app by implication.
3. Record coverage before interpretation: interaction-unit count, sessions/threads, topic groups, and time slices (recent, middle, older when available).
4. Treat the user-authored turn as the primary style evidence. Use the following Agent turn only to understand the request, and use the user's correction, acceptance, or rejection as especially strong reaction evidence.

An **interaction unit** is one user turn paired with the relevant Agent reply and the user's next correction or acceptance. Count units, not characters or tokens.

## Collection targets

Read every accessible unit when the corpus is small. When it is large, collect a stratified sample rather than only the latest or most dramatic thread:

- target 20–60 interaction units;
- cover at least 4 topic groups when available (for example: planning, making, review, troubleshooting, personal expression);
- cover 3 time slices when available (recent, middle, older);
- include both successful and corrective turns, not just polished final requests;
- keep the source/session label and a short paraphrase in temporary working notes, never in the public card.

If more than 60 units are available, sample proportionally from each topic and time slice, then add all corrective or boundary-setting turns. If fewer than 20 are available, read all of them and lower confidence rather than inventing coverage.

## Evidence ledger

Create 18–36 distinct notes when the corpus supports it. Each note should contain:

| Item | What to record |
|---|---|
| source | session/thread and a coarse turn or time reference |
| behavior | a private-content-safe paraphrase of what the user did |
| context | topic or task type |
| dimensions | one or more rubric dimensions it supports |
| recurrence | one-off, repeated in a session, or repeated across sessions |
| polarity | supporting, conflicting, or neutral |

Deduplicate notes that merely restate the same request. Do not use message length, grammar, language fluency, response speed, or device metadata as personality evidence. Do not publish the ledger, source labels, or verbatim private text.

Only provide an evidence appendix when the user asks for more detail. Then summarize recurring patterns without source identifiers, names, secrets, or verbatim private text.

## Confidence bands

Confidence depends on coverage, recurrence, and contradiction—not volume alone:

| Confidence | Minimum pattern |
|---|---|
| `high` | at least 24 meaningful units across 4+ topic groups and 3 time slices when available, with 12+ ledger notes supported by repeated behavior and no unresolved major contradiction |
| `medium` | 12–23 meaningful units across 3+ topic groups, or 20+ units concentrated in one topic, with 8+ ledger notes and limited contradiction |
| `low` | fewer than 12 meaningful units, a single narrow task, mostly pasted content, inaccessible history, or unresolved conflicting patterns |

If the host exposes only one current thread, say so explicitly even when that thread is long. A high match score never overrides low coverage.

## Handoff language

Before the card, summarize the evidence boundary in one sentence, for example:

> 本次分析读取了当前线程的 31 个互动单元，覆盖 4 类任务和近、中、早三个时间段；卡片展示的是从内部证据台账中压缩出的 3 条聊天记录。

When coverage is thin, say what would improve it:

> 当前只看到 8 个互动单元，主要集中在一次任务；如果你授权更多历史会话，我可以重新抽取并提高置信度。
