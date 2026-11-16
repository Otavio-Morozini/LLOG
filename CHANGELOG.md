# Changelog

## 2026-09-09 — Refatoração no briefing + estrutura

Reestruturação grande da vitrine a partir de `Meu briefing.pdf`.

### Identidade (agora fiel ao briefing)
- Paleta trocada para a do briefing: `#FDF8F5` / `#3B1C28` / `#FED5CB` /
  `#6D2C45` / `#B86B58` (antes: burgundy próprio `#6b2c38` etc.).
- Tipografia: **Poppins** (corpo/botões) + display serifada
  (`Perandory Condensed` → `Bodoni Moda` substituta). **Removida a fonte
  script/cursiva** (Great Vibes) — clichê de "salão".
- `<h1>` do hero agora é a **mensagem central**: "Você vai ter dó de tirar a
  maquiagem." (antes: "Beleza que transforma…").
- Hero, Agenda e rodapé em **plum `#3B1C28`** com fotos em moldura creme —
  direção tirada do painel semântico (pp. 3–4 do PDF).

### Estrutura
- `styles.css` (1 arquivo) → `assets/css/` em 5 camadas.
- `app.js` (1 arquivo) → `assets/js/` em 10 módulos (6 ativos, 4 ociosos).
- Conteúdo movido para `data/*.json` como fonte de verdade (com `_fonte` em cada).
- Nova seção estrutural **"Tudo no mesmo lugar"** (o diferencial do briefing).
- Nova seção **FAQ**. Persona reescrita com o texto do briefing (persona,
  marca, transformação, visão).
- `404.html`, `obrigada.html`, `manifest.webmanifest`, `robots.txt`,
  `sitemap.xml`, `.gitignore`, `.editorconfig`.
- `docs/` (8 documentos), `AGENTS.md`, `README.md`.
- `tools/`: `serve`, `build-pages`, `new-section`, `check-links`, `optimize-images`.
- `content/_MODELO-secao.html` + `tools/new-section.mjs` para novas seções.

### Design
- Canvas de design (Claude Design) em `design/canvas/` — home desktop/mobile,
  direção de marca, design system. Publicado como Artifact.

### Interações
- `whatsapp.js` monta todos os links `wa.me` a partir de `data-*`.
- `pricing.js` — "Montar meu combo" (a cliente marca serviços e vê o combo/preço).
- `portfolio.js` — filtro por categoria com hash compartilhável.
- `reveal.js` — entrada ao rolar com 3 camadas de segurança.

### Removido
- `styles.css` e `app.js` na raiz (substituídos por `assets/`).

### Correções durante a sessão
- `<h1>` do hero estava invisível (texto plum sobre fundo plum) — corrigido.
- `@font-face` da Perandory gerava 404 — agora só `local()`, sem requisição.
- `reveal` podia prender elementos altos — `threshold: 0` + fallbacks.
- Menu mobile: troca de `clip-path` por `opacity`/`visibility` (mais robusto).

### Pendente (ver `docs/CHECKLIST-CONTEUDO.md`)
- Fotos reais (hoje: marcadores SVG).
- E-mail, endereço, horário — placeholders.
- Domínio para trocar `[DOMINIO-QUANDO-PUBLICAR]`.
- Arquivo da fonte Perandory Condensed.
