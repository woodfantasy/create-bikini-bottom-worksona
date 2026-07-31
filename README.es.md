[English](README.md) | [简体中文](README.zh-CN.md) | [日本語](README.ja.md) | [한국어](README.ko.md) | Español | [Português](README.pt.md) | [Français](README.fr.md)

# Bikini Bottom Worksona

Convierte el estilo de conversación visible para tu agente en una tarjeta de personalidad laboral divertida y empática. El Skill extrae señales de comunicación y las relaciona con un arquetipo inspirado en el universo de Bob Esponja.

Es una herramienta de autoexpresión, no un diagnóstico psicológico. Solo analiza la conversación que el host muestra realmente o los archivos que el usuario autoriza.

## Funciones

- Extrae entre 5 y 12 señales observables de comunicación y trabajo.
- Elige un personaje, una puntuación de coincidencia y un nivel de confianza.
- Escribe título, frase para compartir, tres “recibos del chat”, modo de trabajo, habilidad oculta, herida laboral y límite personal.
- Genera una tarjeta SVG/PNG de 1242×1656 px (3:4), lista para redes.
- Genera un texto Markdown con gancho y hashtags.
- Protege la privacidad y usa por defecto un personaje submarino original o un marcador de posición para imágenes públicas.

## Instalación

```bash
npx skills add https://github.com/woodfantasy/create-bikini-bottom-worksona
```

Instalación manual:

```bash
# Claude Code
git clone https://github.com/woodfantasy/create-bikini-bottom-worksona.git .claude/skills/create-bikini-bottom-worksona

# Codex
git clone https://github.com/woodfantasy/create-bikini-bottom-worksona.git .agents/skills/create-bikini-bottom-worksona
```

Desde la raíz del repositorio también puedes ejecutar:

```bash
python3 scripts/install_skill.py --target claude-code
python3 scripts/install_skill.py --target codex
python3 scripts/install_skill.py --target antigravity
python3 scripts/install_skill.py --target openclaw
```

En Claude, clona el repositorio, crea el ZIP y súbelo desde Settings → Features/Capabilities → Skills. En OpenClaw:

```bash
openclaw skills install git:woodfantasy/create-bikini-bottom-worksona --global
```

```bash
python3 scripts/package_skill.py --output /tmp/create-bikini-bottom-worksona.zip
```

## Uso

```text
Usa solo lo visible en esta conversación para crear mi tarjeta de personalidad laboral.
Asígnamela a un personaje de Bob Esponja e incluye tres recibos del chat, mi habilidad oculta,
mi herida laboral y una frase límite que quiera compartir.
```

Si hay poca evidencia, aporta 10–30 mensajes representativos o responde tres preguntas breves. También puedes pedir un borrador con confianza baja.

El flujo es: delimitar la evidencia → extraer señales → elegir personaje → escribir la tarjeta → generar imagen y texto → revisar tamaño, privacidad y derechos.

## Generación local

```bash
python3 scripts/validate_profile.py worksona-profile.json
python3 scripts/render_card.py \
  --input worksona-profile.json \
  --output worksona-card.svg \
  --png worksona-card.png \
  --caption worksona-caption.md
```

La tarjeta maestra mide **1242×1656 px en formato vertical 3:4**. Consulta [`references/profile-schema.md`](references/profile-schema.md) para el JSON.

## Privacidad y propiedad intelectual

Parafrasea la evidencia y nunca publiques mensajes privados, nombres, empresas, contactos, tokens u otros secretos. El resultado es entretenimiento, no una evaluación clínica o laboral. Este es un proyecto de expresión fan no oficial y no está afiliado a los titulares de Bob Esponja. Para repositorios públicos usa el marcador incluido, un personaje submarino original o material con derechos confirmados; no añadas capturas de episodios, PNG raspados, logotipos ni fan art de terceros.

## Licencia

El código y la documentación se publican bajo la [Licencia MIT](LICENSE). Los nombres y personajes relacionados con Bob Esponja siguen perteneciendo a sus respectivos titulares.
