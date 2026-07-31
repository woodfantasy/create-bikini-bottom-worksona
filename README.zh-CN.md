[English](README.md) | 简体中文 | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | [Português](README.pt.md) | [Français](README.fr.md)

<h1 align="center">Bikini Bottom Worksona</h1>

<p align="center"><strong>把聊天风格，变成一张有共鸣的打工人设卡</strong></p>

把 Agent 当前能看到的对话风格、工作习惯和自我描述，映射成一个海绵宝宝宇宙灵感的打工人格：角色匹配、工作身份、适合转发的一句话，以及小红书分享文案。

这是娱乐化的自我表达工具，不是心理诊断。Skill 只分析当前 Agent 实际可见、或用户明确授权的内容。

## 核心能力

- 提取 5–12 条可观察的沟通与工作信号；
- 映射到海绵宝宝/比奇堡角色原型，给出匹配分数和置信度；
- 生成工作人格标题、金句、3 条“聊天记录把我卖了”、工作模式、隐藏技能、常见工伤和边界声明；
- 输出统一的 1242×1656 px（3:4）SVG/PNG 小红书卡片；
- 输出可直接复制的分享文案；
- 默认用原创海底职场角色或占位图，保护隐私和公开发布的 IP 安全。

## 安装

### Skills CLI

```bash
npx skills add https://github.com/woodfantasy/create-bikini-bottom-worksona
```

### 手动安装

```bash
# Claude Code
git clone https://github.com/woodfantasy/create-bikini-bottom-worksona.git .claude/skills/create-bikini-bottom-worksona

# Codex
git clone https://github.com/woodfantasy/create-bikini-bottom-worksona.git .agents/skills/create-bikini-bottom-worksona
```

也可以在仓库根目录运行内置安装器：

```bash
python3 scripts/install_skill.py --target claude-code
python3 scripts/install_skill.py --target codex
python3 scripts/install_skill.py --target antigravity
python3 scripts/install_skill.py --target openclaw
```

先用 `python3 scripts/install_skill.py --target all --dry-run` 查看路径。已有安装不会被覆盖，除非显式加入 `--force`；强制替换前会创建带时间戳的备份。

| Agent | 个人安装位置 | 项目安装位置 |
| --- | --- | --- |
| Claude Code | `~/.claude/skills/create-bikini-bottom-worksona` | `<项目>/.claude/skills/create-bikini-bottom-worksona` |
| Claude | 本地打包 ZIP 后，在 Settings → Features/Capabilities → Skills 上传 | — |
| Codex | `~/.agents/skills/create-bikini-bottom-worksona` | `<项目>/.agents/skills/create-bikini-bottom-worksona` |
| Antigravity | `~/.gemini/config/skills/create-bikini-bottom-worksona` | `<项目>/.agents/skills/create-bikini-bottom-worksona` |
| OpenClaw | `~/.openclaw/skills/create-bikini-bottom-worksona` | `<工作区>/skills/create-bikini-bottom-worksona` |

OpenClaw 也支持：

```bash
openclaw skills install git:woodfantasy/create-bikini-bottom-worksona --global
```

Claude 上传包的生成方式：

```bash
python3 scripts/package_skill.py --output /tmp/create-bikini-bottom-worksona.zip
```

## 使用方式

直接向 Agent 提问：

```text
分析我在这段对话里的沟通风格，看看我最像哪个海绵宝宝角色。
重点写出“事情全是我做，锅还是我背”的打工情绪，生成一张适合小红书的 3:4 人设卡。
```

如果对话证据不足，Skill 会请求 10–30 条代表性消息，或请你回答：“最常催 Agent 做什么？最受不了什么？最近替别人补过什么锅？”也可以要求它直接输出低置信度草稿。

默认流程是：确认可见范围 → 提取行为信号 → 角色匹配 → 写作卡片字段 → 渲染图片和文案 → 做尺寸、隐私和版权检查。

## 本地生成

先准备符合 [`references/profile-schema.md`](references/profile-schema.md) 的 JSON：

```bash
python3 scripts/validate_profile.py worksona-profile.json
python3 scripts/render_card.py \
  --input worksona-profile.json \
  --output worksona-card.svg \
  --png worksona-card.png \
  --caption worksona-caption.md
```

主卡片固定为 **1242×1656 px、3:4 竖版**。SVG 是可移植源文件，环境支持时同时输出 PNG 和 Markdown 分享文案。

## 隐私与版权

- 只分析当前对话可见内容和用户明确授权的文件；
- 证据使用概述，不发布私聊原文、姓名、公司、联系方式、密钥或其他秘密；
- 结果是自我表达和社交娱乐，不是心理、能力或职场评价；
- 本项目为非官方粉丝向工具，与海绵宝宝版权方无隶属或授权关系；
- 公开/商业视觉请使用占位图、原创海底职场角色或用户确认的授权素材，不要加入剧集截图、抓取 PNG、商品截图、官方 Logo、版权字体或第三方同人图。

## 项目结构与校验

`SKILL.md` 是 Agent 指令；`references/` 保存分析、角色、字段、设计、分享和安全规范；`scripts/` 提供安装、渲染、校验和打包工具；`assets/` 保存中性占位图和示例卡。

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py .
skills-ref validate "$(pwd)"
python3 scripts/package_skill.py --output /tmp/create-bikini-bottom-worksona.zip
unzip -t /tmp/create-bikini-bottom-worksona.zip
```

## 许可证

代码和文档采用 [MIT License](LICENSE)。海绵宝宝相关名称与角色仍归各自版权方所有，本仓库不授予相关 IP 权利。
