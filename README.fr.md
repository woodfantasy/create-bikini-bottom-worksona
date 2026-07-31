[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | [Português](README.pt.md) | Français

# Bikini Bottom Worksona

Transformez le style de conversation visible par votre agent en une carte de personnalité professionnelle, drôle et empathique. Le Skill extrait les signaux de communication et les associe à un archétype inspiré de l’univers de Bob l’éponge.

C’est un outil d’expression personnelle, pas un diagnostic psychologique. Il n’analyse que les conversations réellement visibles par l’hôte ou les fichiers autorisés par l’utilisateur.

## Fonctionnalités

- Extrait 5 à 12 signaux observables de communication et de travail.
- Choisit un personnage, un score de correspondance et un niveau de confiance.
- Rédige un titre, une phrase à partager, trois « preuves du chat », le mode de travail, le talent caché, la blessure professionnelle et la limite personnelle.
- Génère une carte SVG/PNG de 1242×1656 px (3:4), adaptée aux réseaux sociaux.
- Génère une légende Markdown prête à copier.
- Protège la vie privée et utilise par défaut un personnage sous-marin original ou un placeholder pour les visuels publics.

## Installation

```bash
npx skills add https://github.com/woodfantasy/create-bikini-bottom-worksona
```

Installation manuelle :

```bash
# Claude Code
git clone https://github.com/woodfantasy/create-bikini-bottom-worksona.git .claude/skills/create-bikini-bottom-worksona

# Codex
git clone https://github.com/woodfantasy/create-bikini-bottom-worksona.git .agents/skills/create-bikini-bottom-worksona
```

Depuis la racine du dépôt :

```bash
python3 scripts/install_skill.py --target claude-code
python3 scripts/install_skill.py --target codex
python3 scripts/install_skill.py --target antigravity
python3 scripts/install_skill.py --target openclaw
```

Dans Claude, clonez le dépôt, créez le ZIP puis téléversez-le dans Settings → Features/Capabilities → Skills. Dans OpenClaw :

```bash
openclaw skills install git:woodfantasy/create-bikini-bottom-worksona --global
```

```bash
python3 scripts/package_skill.py --output /tmp/create-bikini-bottom-worksona.zip
```

## Utilisation

```text
Utilise uniquement ce qui est visible dans cette conversation pour créer ma carte de personnalité professionnelle.
Associe-moi à un personnage de Bob l’éponge et ajoute trois preuves du chat, mon talent caché,
ma blessure au travail et une limite que j’aurai envie de partager.
```

Si les preuves sont rares, fournissez 10 à 30 messages représentatifs ou répondez à trois questions courtes. Vous pouvez aussi demander une première version à faible confiance.

Le flux est : définir les preuves disponibles → extraire les signaux → choisir le personnage → rédiger la carte → générer l’image et la légende → vérifier format, confidentialité et droits.

## Génération locale

```bash
python3 scripts/validate_profile.py worksona-profile.json
python3 scripts/render_card.py \
  --input worksona-profile.json \
  --output worksona-card.svg \
  --png worksona-card.png \
  --caption worksona-caption.md
```

La carte principale mesure **1242×1656 px, au format vertical 3:4**. Consultez [`references/profile-schema.md`](references/profile-schema.md) pour le JSON.

## Confidentialité et propriété intellectuelle

Paraphrasez les preuves et ne publiez jamais de messages privés, noms, entreprises, coordonnées, tokens ou autres secrets. Le résultat relève du divertissement, pas d’une évaluation clinique ou professionnelle. Il s’agit d’un projet d’expression de fan non officiel, sans affiliation aux ayants droit de Bob l’éponge. Pour un dépôt public, utilisez le placeholder fourni, un personnage sous-marin original ou un contenu dont les droits sont confirmés ; n’ajoutez pas d’images d’épisodes, de PNG récupérés, de logos ou de fan art tiers.

## Licence

Le code et la documentation sont distribués sous [licence MIT](LICENSE). Les noms et personnages liés à Bob l’éponge restent la propriété de leurs ayants droit respectifs.
