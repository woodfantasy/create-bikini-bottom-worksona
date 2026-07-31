[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | 한국어 | [Español](README.es.md) | [Português](README.pt.md) | [Français](README.fr.md)

# Bikini Bottom Worksona

대화 스타일을 공감할 수 있는 ‘직장인 캐릭터 카드’로 바꾸는 Agent Skill입니다. 현재 Agent가 볼 수 있는 대화에서 행동 신호를 추출해, 스폰지밥 세계관에서 영감을 받은 업무 성격으로 매핑합니다.

심리 진단이 아니라 재미있는 자기표현 도구입니다. 보이지 않는 대화 기록이나 다른 앱의 대화에는 접근하지 않습니다.

## 주요 기능

- 대화에서 5–12개의 관찰 가능한 소통·업무 신호 추출
- 캐릭터 후보, 매칭 점수, 신뢰도 제시
- 제목, 공감 문장, 3개의 “채팅 기록이 나를 팔아넘긴 순간”, 업무 모드, 숨은 능력, 직장 상처, 경계 문장 작성
- 1242×1656 px(3:4) SNS 공유용 SVG/PNG 카드 생성
- 바로 복사할 수 있는 Markdown 공유 문구 생성

## 설치

```bash
npx skills add https://github.com/woodfantasy/create-bikini-bottom-worksona
```

수동 설치:

```bash
# Claude Code
git clone https://github.com/woodfantasy/create-bikini-bottom-worksona.git .claude/skills/create-bikini-bottom-worksona

# Codex
git clone https://github.com/woodfantasy/create-bikini-bottom-worksona.git .agents/skills/create-bikini-bottom-worksona
```

저장소 루트에서는 내장 설치 도구를 사용할 수 있습니다.

```bash
python3 scripts/install_skill.py --target claude-code
python3 scripts/install_skill.py --target codex
python3 scripts/install_skill.py --target antigravity
python3 scripts/install_skill.py --target openclaw
```

Claude는 저장소를 클론한 뒤 ZIP을 만들어 Settings → Features/Capabilities → Skills에서 업로드합니다. OpenClaw:

```bash
openclaw skills install git:woodfantasy/create-bikini-bottom-worksona --global
```

```bash
python3 scripts/package_skill.py --output /tmp/create-bikini-bottom-worksona.zip
```

## 사용법

```text
이 대화에서 볼 수 있는 내용만 사용해서 나의 직장인 캐릭터 카드를 만들어 주세요.
스폰지밥 캐릭터로 매칭하고, 채팅 기록 3가지, 숨은 능력, 직장 상처, 공유하고 싶은 경계 문장을 넣어 주세요.
```

대화 증거가 적으면 대표 메시지 10–30개를 제공하거나 짧은 질문에 답하세요. 원하면 낮은 신뢰도의 초안으로 진행할 수도 있습니다.

흐름은 ‘확인 가능한 범위 설정 → 행동 신호 추출 → 캐릭터 매칭 → 카드 문구 작성 → 이미지·캡션 렌더링 → 크기·개인정보·권리 검토’입니다.

## 로컬 렌더링

```bash
python3 scripts/validate_profile.py worksona-profile.json
python3 scripts/render_card.py \
  --input worksona-profile.json \
  --output worksona-card.svg \
  --png worksona-card.png \
  --caption worksona-caption.md
```

카드는 **1242×1656 px, 3:4 세로형**입니다. JSON 필드는 [`references/profile-schema.md`](references/profile-schema.md)를 참고하세요.

## 개인정보와 저작권

현재 보이는 대화와 사용자가 명시적으로 승인한 파일만 분석합니다. 사적인 원문, 이름, 회사, 연락처, 토큰을 공개하지 않습니다. 공개용 이미지는 기본 제공 플레이스홀더, 독창적인 해저 사무실 캐릭터 또는 권리 확인이 끝난 소재를 사용하세요. 비공식 팬 표현 프로젝트이며 권리자의 제휴나 승인을 의미하지 않습니다.

## 라이선스

코드와 문서는 [MIT License](LICENSE)로 제공합니다. 스폰지밥 관련 이름과 캐릭터의 권리는 각 권리자에게 있습니다.
