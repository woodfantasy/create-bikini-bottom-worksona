# Installation and Distribution

The repository root contains `SKILL.md`, so it can be installed directly as one Agent Skill.

## Local helper

From the Skill root, preview paths without changing anything:

```bash
python3 scripts/install_skill.py --target all --dry-run
```

Install for one host:

```bash
python3 scripts/install_skill.py --target codex
python3 scripts/install_skill.py --target claude-code
python3 scripts/install_skill.py --target antigravity
python3 scripts/install_skill.py --target openclaw
```

The helper refuses to overwrite an existing installation unless `--force` is supplied. Forced replacement first creates a timestamped sibling backup.

## Host locations

| Host | Personal/global location | Project location |
|---|---|---|
| Codex | `~/.agents/skills/create-bikini-bottom-worksona` | `<repo>/.agents/skills/create-bikini-bottom-worksona` |
| Claude Code | `~/.claude/skills/create-bikini-bottom-worksona` | `<repo>/.claude/skills/create-bikini-bottom-worksona` |
| Google Antigravity | `~/.gemini/config/skills/create-bikini-bottom-worksona` | `<repo>/.agents/skills/create-bikini-bottom-worksona` |
| OpenClaw | `~/.openclaw/skills/create-bikini-bottom-worksona` | `<workspace>/skills/create-bikini-bottom-worksona` |

`~/.agents/skills` is a useful shared location for hosts that implement the open Agent Skills convention. Antigravity CLI versions may use a product-specific global path; prefer project-scoped `.agents/skills` when portability matters.

## GitHub install patterns

After publishing the repository:

```bash
npx skills add https://github.com/<owner>/<repo>
```

OpenClaw can install a repository whose root contains `SKILL.md`:

```bash
openclaw skills install git:<owner>/<repo> --global
```

## claude.ai upload

Create a clean zip:

```bash
python3 scripts/package_skill.py --output dist/create-bikini-bottom-worksona.zip
```

Upload the zip through Claude Settings → Features → Skills. Custom Skill availability depends on plan and code-execution settings.

## Validation before publishing

Run both validators:

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py .
skills-ref validate "$(pwd)"
python3 scripts/validate_avatar_pack.py
```

Run the second command only when `skills-ref` is installed. Also test one direct trigger, one indirect trigger, one sparse-context request, and one unrelated request that should not activate the Skill.

Official references:

- Agent Skills specification: <https://agentskills.io/specification>
- Claude Agent Skills: <https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview>
- Google Antigravity Skills: <https://codelabs.developers.google.com/getting-started-with-antigravity-skills>
- OpenClaw Skills: <https://docs.openclaw.ai/skills>
- Codex skills: <https://learn.chatgpt.com/docs/build-skills>
