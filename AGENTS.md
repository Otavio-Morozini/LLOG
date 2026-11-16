# AGENTS.md — Studio Hellen Varella (handoff)

Leia isto **antes** de editar qualquer arquivo.

## O que é

Vitrine (one-page) do Studio Hellen Varella — maquiagem, cabelo e fotografia
no mesmo atendimento, em Fraiburgo/SC. **HTML/CSS/JS estático, sem build.**
Toda conversa termina no WhatsApp.

Fonte da identidade: **`e:\gtonga\Meu briefing.pdf`** (da própria Hellen).
Transcrito e mapeado em `docs/BRIEFING.md`; o painel visual em
`docs/PAINEL-SEMANTICO.md`.

## Ordem de leitura

1. `docs/MAPA-DO-REPOSITORIO.md` — o que existe, antes/depois.
2. `docs/BRIEFING.md` — cada bloco do briefing → onde está no site.
3. `docs/DESIGN-SYSTEM.md` — cores, tipo, componentes (e o artefato de design).
4. `docs/SLOT-MAP.md` — cada `data-slot` do HTML.
5. `docs/CHECKLIST-CONTEUDO.md` — o que falta (fotos, dados da Hellen).
6. `data/*.json` — fonte de verdade do conteúdo; cada um tem `_fonte`.

## Regras rígidas (não quebrar)

### Identidade — SÓ o que está no briefing
- Paleta: `#FDF8F5` fundo · `#3B1C28` texto/plum · `#FED5CB` apoio ·
  `#6D2C45` CTA (`#7A3450` alt) · `#B86B58` quente. **Não inventar cor.**
- Tipo: título `--font-display` (Perandory → Bodoni Moda substituta) ·
  corpo/botões **Poppins**. **Sem fonte script/cursiva** (clichê de "salão").
- Mensagem central: **"Você vai ter dó de tirar a maquiagem."** — é o `<h1>`.
- Não pode "parecer amadora, genérica ou mais um salão de beleza".

### Estrutura
- Toda seção: `id` + `class="section"` (+ variação de fundo) + `.container` +
  `.section-head` (eyebrow + h2). Blocos animados: `class="reveal"`.
- O **diferencial "tudo no mesmo lugar"** é estrutural (seção `.combo-band`),
  não só um slogan.
- CSS em camadas (`tokens → base → layout → components → utilities`), nessa ordem.
- JS: scripts clássicos (sem `import`/`export`), cada um retorna cedo se não
  achar seu alvo. Precisa funcionar em `file://` **e** servido.

### Conteúdo
- Não inventar: e-mail, endereço, horário, depoimento, equipe já contratada,
  data de turma. O que não está no briefing nem no repo fica `[PLACEHOLDER]`
  ou é rotulado `Suposição:`.
- Preços, telefone, `@`, "desde 2013/2021" vêm do repositório — **confirmar
  com a Hellen antes de mudar**.

### Git
- Este projeto **não tem remote próprio**. Ele vive como pasta
  `hellen-varella/` dentro do repositório principal
  [`Lfkcc/Luiz`](https://github.com/Lfkcc/Luiz)
  (`E:\.projects\Luiz`).
- Commits e `git push` / `git pull` são **no repo Luiz**, na branch `main`.
- Pasta de trabalho no Cursor: `E:\.projects\hellen-varella` (espelho da
  subpasta). Não criar outro `origin` aqui.

## Fluxos comuns

**Adicionar as fotos:** `assets/img/README.md` → `node tools/optimize-images.mjs`
→ trocar marcadores no `index.html` → `data-lightbox="portfolio"` nas fotos →
`node tools/check-links.mjs`.

**Nova seção:** `node tools/new-section.mjs <id> "<Título>" --fundo=support`
→ colar em `<main>` → `<a href="#id">` no menu → `check-links`.

**Mudar preço/combo/obra:** editar `data/servicos.json` ou `data/portfolio.json`
→ `node tools/build-pages.mjs` → conferir `content/generated/*.html` contra o
`index.html` (ou pôr os marcadores `<!-- build:valores:start/end -->` para
splice automático).

**Mudar o design (maquete):** editar `design/canvas/*.dc.html`, depois
re-seed com o helper do skill `design`:
```
node "<base do skill design>/seed-canvas.mjs" \
  --template "<base>/payload.template.html" \
  --out design/canvas/hellen-varella-vitrine.html \
  --title "Vitrine Hellen Varella" \
  --artboard design/canvas/Main.dc.html --artboard design/canvas/Mobile.dc.html \
  --artboard design/canvas/Direcao.dc.html --artboard design/canvas/Sistema.dc.html \
  --canvas design/canvas/canvas.json
```
e republicar o Artifact com `contract: "0.1.31"`.

## O que NÃO fazer

- Não migrar para React/Next/SSG sem pedido explícito.
- Não trazer nada do projeto-modelo "Entre Cenas" além do **padrão de
  organização** (docs, dados como fonte de verdade, `_MODELO`, slots).
  Nada de cinema, reviews, notas.
- Não remover a faixa do diferencial nem o botão de WhatsApp flutuante.
- Não publicar depoimentos sem autorização das clientes.

## Rodar

```bash
node tools/serve.mjs        # http://127.0.0.1:4173/
node tools/check-links.mjs  # antes de qualquer commit/publicação
```

## Critério de "pronto para publicar"

`docs/CHECKLIST-CONTEUDO.md` zerado e `node tools/check-links.mjs` sem erros.
