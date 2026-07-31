[English](README.md) | [简体中文](README.zh-CN.md) | 日本語 | [한국어](README.ko.md) | [Español](README.es.md) | [Português](README.pt.md) | [Français](README.fr.md)

# Bikini Bottom Worksona

会話のスタイルを、共感できる「働く人のキャラクターカード」に変える Agent Skill です。Agent が現在見られる会話から行動のサインを抽出し、スポンジ・ボブの世界観に着想を得た仕事人格へマッピングします。

心理診断ではなく、楽しい自己表現のためのツールです。見えていない履歴や他のアプリの会話にはアクセスしません。

## できること

- 許可された最大の会話コーパスから18〜36個の重複しない行動サインを内部台帳にまとめ、共有用の3つの証拠へ圧縮
- キャラクター候補、マッチ度、信頼度を提示
- タイトル、共感できる一言、3 つの「チャット記録が私を売った理由」、仕事モード、隠れスキル、職場の傷、境界線を作成
- 小紅書や SNS で共有しやすい 1242×1656 px（3:4）の SVG/PNG カードを生成
- そのまま投稿できる Markdown キャプションを出力

## インストール

共通 Skills CLI：

```bash
npx skills add https://github.com/woodfantasy/create-bikini-bottom-worksona
```

手動で配置する場合：

```bash
# Claude Code
git clone https://github.com/woodfantasy/create-bikini-bottom-worksona.git .claude/skills/create-bikini-bottom-worksona

# Codex
git clone https://github.com/woodfantasy/create-bikini-bottom-worksona.git .agents/skills/create-bikini-bottom-worksona
```

リポジトリのルートでは、同梱ヘルパーも使えます。

```bash
python3 scripts/install_skill.py --target claude-code
python3 scripts/install_skill.py --target codex
python3 scripts/install_skill.py --target antigravity
python3 scripts/install_skill.py --target openclaw
```

Claude はリポジトリをクローンして ZIP を作成し、Settings → Features/Capabilities → Skills からアップロードします。OpenClaw は次のコマンドでもインストールできます。

```bash
openclaw skills install git:woodfantasy/create-bikini-bottom-worksona --global
```

```bash
python3 scripts/package_skill.py --output /tmp/create-bikini-bottom-worksona.zip
```

## 使い方

```text
この会話で見えている範囲だけを使って、私の仕事人格カードを作ってください。
スポンジ・ボブのキャラクターにマッピングし、3つのチャット記録、隠れスキル、職場の傷、投稿したくなる境界線を入れてください。
```

信頼度を上げるには、現在のホストが実際に見られる全ターンと、明示的に許可した履歴を確認するよう依頼してください。会話・テーマ・時期をまたぐ18〜36個の内部証拠を作り、Agentへの修正や反応も含めます。履歴が少ない場合は、会話検索を許可するか、20〜60件ほどの代表的な対話単位を渡してください。少ない証拠のまま低信頼度の下書きを作ることもできます。

処理は「アクセス可能な会話範囲の報告 → 全ターンの確認または大規模コーパスの層別サンプリング → 18〜36個の証拠台帳 → キャラクター判定 → 3つの共有用証拠へ圧縮 → カード文案 → 画像とキャプションの生成 → サイズ・プライバシー・権利の確認」の順です。

## ローカル生成

```bash
python3 scripts/validate_profile.py worksona-profile.json
python3 scripts/render_card.py \
  --input worksona-profile.json \
  --output worksona-card.svg \
  --png worksona-card.png \
  --caption worksona-caption.md
```

カードは **1242×1656 px、3:4 縦長**です。JSON のフィールドは [`references/profile-schema.md`](references/profile-schema.md) を参照してください。

## プライバシーと権利

現在見えている会話、またはユーザーが明示的に許可したファイルだけを使います。私信の原文、個人名、会社名、連絡先、トークンなどを公開しません。公開用の画像は同梱のプレースホルダー、オリジナルの海中オフィスキャラクター、または権利確認済み素材を使ってください。これは非公式のファン表現であり、権利者による承認や提携を意味しません。

## ライセンス

コードとドキュメントは [MIT License](LICENSE) で提供します。スポンジ・ボブ関連の名称とキャラクターの権利は各権利者に帰属します。
