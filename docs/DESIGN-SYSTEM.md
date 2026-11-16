# Design system — Studio Hellen Varella

> Entrega 3 (companheiro do artefato). O sistema vive em código em
> `assets/css/tokens.css`; este documento explica **por quê** cada escolha,
> tudo ancorado no briefing.

---

## Artefato de design

Foi criado um **canvas de design** (ferramenta Claude Design, multi-prancheta),
publicado como Artifact:

- `design/canvas/Main.dc.html` — home desktop
- `design/canvas/Mobile.dc.html` — home mobile
- `design/canvas/Direcao.dc.html` — direção de marca (leitura do painel semântico)
- `design/canvas/Sistema.dc.html` — a folha de estilo (paleta, tipo, componentes)
- `design/canvas/canvas.json` — layout das pranchetas
- `design/canvas/hellen-varella-vitrine.html` — payload publicado (abre no navegador; exporta PNG/PDF)

Os `.dc.html` são os **arquivos-fonte** do canvas: para mudar o design,
edita-se um deles e roda-se de novo o `seed-canvas.mjs` do skill (ver
`AGENTS.md`). Não é o site — é a maquete que guiou a refatoração.

---

## Cores

```css
--bg:      #FDF8F5;  /* Fundo (briefing) */
--ink:     #3B1C28;  /* Texto principal (briefing) — TAMBÉM fundo escuro (painel) */
--support: #FED5CB;  /* Cor de apoio (briefing) */
--cta:     #6D2C45;  /* CTA / botões / subtítulo (briefing) */
--cta-alt: #7A3450;  /* CTA alternativo (briefing: "#6D2C45 ou #7A3450") */
--warm:    #B86B58;  /* Cor quente (briefing) — olhos, hovers, ícones */
```

Derivados (transparências de `--ink`/`--bg`, branco de moldura, linhas) e dois
acentos do painel semântico (`--caramelo`, `--dourado`) — **detalhe apenas**.

**Uso das áreas:**
- claro: `--bg` (padrão), `--support` (A experiência, A Hellen),
  `--support-2` (Valores, Divas, FAQ — apoio mais claro), branco (cartões);
- escuro: `--plum` (= `--ink`) no hero, na Agenda e no rodapé — é o "palco"
  do painel semântico. Texto sobre plum = `--bg` (creme).

**Contraste:** creme sobre plum ≈ 12:1; `--ink` sobre `--bg` ≈ 12:1; branco
sobre `--cta` ≈ 8:1. Todos acima de AA.

---

## Tipografia

| Papel | Família | Fallback | Peso |
|-------|---------|----------|------|
| Título (`--font-display`) | **Perandory Condensed** → **Bodoni Moda** (`Suposição:`) | Times New Roman, Georgia, serif | 400 / 500 |
| Corpo, subtítulo, botões (`--font-body`) | **Poppins** (briefing) | system-ui, Segoe UI, Roboto | 300 / 400 / 500 / 600 |

### Sobre Perandory Condensed

O briefing diz "só tem no Canva". Não há versão web. A pilha é:

```css
--font-display: "Perandory Condensed", "Bodoni Moda", "Times New Roman", Georgia, serif;
```

O `@font-face` de `Perandory Condensed` hoje só tenta `local()` (quem tiver a
fonte instalada a vê; os demais caem para Bodoni Moda — sem requisição, sem
404). **Bodoni Moda** foi escolhida como substituta por ser serifada de alto
contraste, editorial, "de revista" — o registro "elegante / olhar artístico"
que o briefing pede, e o oposto de "salão genérico".

**Quando a Hellen exportar o arquivo da fonte:** `assets/fonts/README.md` tem
o passo a passo (é trocar uma linha em `tokens.css`).

### Por que NÃO tem fonte script/cursiva

O site anterior usava Great Vibes (cursiva). O briefing **não lista fonte
script** e diz explicitamente que não pode "parecer mais um salão de beleza" —
e cursiva "de beleza" é o clichê nº 1. Ficou só display serifada + Poppins.

---

## Escala e ritmo

Tipo fluido com `clamp()` (`--step--1` a `--step-4`). Espaçamento em escala
(`--space-2xs`…`--space-2xl`). Container `1240px`. Medida de leitura `40rem`.
Raio `4px` (discreto, editorial — nada de cartão muito arredondado).

---

## Componentes (em `assets/css/components.css`)

- **`.button`** — pílula, `--cta`, texto creme, Poppins SemiBold. Variações:
  `--ghost` (contorno), `--support` (apoio), `--lg`.
- **`.combo-band`** — a faixa "tudo no mesmo lugar": três blocos ligados por
  um `+` (o diferencial, visual e estrutural).
- **`.pillar`** — os 3 sentimentos, borda-topo `--cta`.
- **`.pack`** — cartão de valor; `--feature` (destaque, o combo mais pedido),
  `--soft` (apoio, promoções).
- **`.work`** — cartão de portfólio; `--wide`, `--dark` (o recorte Artístico).
- **`.photo-frame`** — a moldura polaroid do painel semântico.
- **`.faq details`**, **`.steps`**, **`.callout`**, **`.persona`**.

---

## Movimento

`.reveal` — entrada suave ao rolar via `IntersectionObserver`, com **3 camadas
de segurança** (`assets/js/reveal.js`) para que nenhum conteúdo fique preso
invisível. Respeita `prefers-reduced-motion`. Sem JS, tudo aparece normalmente
(`.no-js .reveal { opacity: 1 }`).

---

## Acessibilidade

- `skip-link`, foco visível (`:focus-visible`), `aria-expanded`/`aria-pressed`
  nos toggles e filtros, `aria-label` nos ícones, alvos ≥ 44px.
- Ordem de heading coerente (um `h1`, `h2` por seção).
- `::selection` na cor de apoio.
