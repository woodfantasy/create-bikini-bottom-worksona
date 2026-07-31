[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | [Español](README.es.md) | Português | [Français](README.fr.md)

# Bikini Bottom Worksona

Transforme o estilo de conversa visível para o seu agente em um card de personalidade profissional, engraçado e empático. O Skill extrai sinais de comunicação e os relaciona a um arquétipo inspirado no universo de Bob Esponja.

É uma ferramenta de autoexpressão, não um diagnóstico psicológico. Ele só analisa a conversa que o host realmente mostra ou arquivos autorizados pelo usuário.

## Recursos

- Extrai 5–12 sinais observáveis de comunicação e trabalho.
- Escolhe personagem, pontuação de correspondência e nível de confiança.
- Escreve título, frase compartilhável, três “recibos do chat”, modo de trabalho, habilidade oculta, ferida profissional e limite pessoal.
- Gera card SVG/PNG de 1242×1656 px (3:4), pronto para redes sociais.
- Gera legenda Markdown com gancho e hashtags.
- Protege a privacidade e usa por padrão um personagem submarino original ou placeholder em imagens públicas.

## Instalação

```bash
npx skills add https://github.com/woodfantasy/create-bikini-bottom-worksona
```

Instalação manual:

```bash
# Claude Code
git clone https://github.com/woodfantasy/create-bikini-bottom-worksona.git .claude/skills/create-bikini-bottom-worksona

# Codex
git clone https://github.com/woodfantasy/create-bikini-bottom-worksona.git .agents/skills/create-bikini-bottom-worksona
```

Na raiz do repositório:

```bash
python3 scripts/install_skill.py --target claude-code
python3 scripts/install_skill.py --target codex
python3 scripts/install_skill.py --target antigravity
python3 scripts/install_skill.py --target openclaw
```

No Claude, clone o repositório, crie o ZIP e envie-o em Settings → Features/Capabilities → Skills. No OpenClaw:

```bash
openclaw skills install git:woodfantasy/create-bikini-bottom-worksona --global
```

```bash
python3 scripts/package_skill.py --output /tmp/create-bikini-bottom-worksona.zip
```

## Como usar

```text
Use apenas o que está visível nesta conversa para criar meu card de personalidade profissional.
Associe-me a um personagem de Bob Esponja e inclua três recibos do chat, minha habilidade oculta,
minha ferida no trabalho e uma frase de limite que eu queira compartilhar.
```

Com pouca evidência, forneça 10–30 mensagens representativas ou responda a três perguntas curtas. Também é possível pedir um rascunho com baixa confiança.

O fluxo é: delimitar evidências → extrair sinais → escolher personagem → escrever o card → gerar imagem e legenda → revisar tamanho, privacidade e direitos.

## Geração local

```bash
python3 scripts/validate_profile.py worksona-profile.json
python3 scripts/render_card.py \
  --input worksona-profile.json \
  --output worksona-card.svg \
  --png worksona-card.png \
  --caption worksona-caption.md
```

O card mestre tem **1242×1656 px, proporção vertical 3:4**. Consulte [`references/profile-schema.md`](references/profile-schema.md) para o formato JSON.

## Privacidade e propriedade intelectual

Parafraseie as evidências e nunca publique mensagens privadas, nomes, empresas, contatos, tokens ou outros segredos. O resultado é entretenimento, não avaliação clínica ou profissional. Este é um projeto não oficial de expressão de fã e não é afiliado aos detentores de Bob Esponja. Para repositórios públicos, use o placeholder incluído, um personagem submarino original ou material com direitos confirmados; não adicione frames de episódios, PNGs coletados, logos ou fan art de terceiros.

## Licença

Código e documentação são distribuídos sob a [Licença MIT](LICENSE). Nomes e personagens relacionados a Bob Esponja continuam pertencendo aos respectivos titulares.
