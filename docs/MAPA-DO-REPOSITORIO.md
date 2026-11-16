# Mapa do repositório e do site — Studio Hellen Varella

> Entrega 1 do trabalho: "puxar o repositório explicando". Quem nunca viu
> este projeto deve entender, lendo isto, **o que o repo é** e **o que o site
> faz** — antes e depois da refatoração desta sessão.

---

## 1. Qual é o repositório certo

```
E:\.projects\hellen-varella
```

É a pasta de trabalho da vitrine. O Git **não é desta pasta**: o histórico e
o GitHub ficam no repositório principal do Luiz:

- local: `E:\.projects\Luiz` → subpasta `hellen-varella/`
- remote: `https://github.com/Lfkcc/Luiz` (`origin`, branch `main`)

Não há `origin` em `E:\.projects\hellen-varella`. Puxar/enviar = `git pull` /
`git push` **dentro de `E:\.projects\Luiz`**.

### "Os sites" — um ou vários?

O prompt-modelo fala em "refatorar o site (e os sites, se existirem)".
**Só existe este projeto.** Não há outras pastas, subdomínios ou páginas
associadas no ambiente. A vitrine é **uma página só** (`index.html`), agora
com páginas de apoio ociosas (`404.html`, `obrigada.html`).

---

## 2. O que o site É (produto)

Uma **vitrine (one-page) do Studio Hellen Varella**, em Fraiburgo/SC —
maquiagem, cabelo e fotografia no mesmo atendimento. Público: mulheres de
todas as idades, com foco em adolescentes e mães. O site não vende online
nem tem login: **toda conversa termina no WhatsApp**, como já acontece pelo
Instagram (`@hellenvarella.makeup`).

Stack: **HTML + CSS + JavaScript puro, sem build, sem framework.** Decisão
mantida na refatoração (ver `docs/ARQUITETURA.md`) — hospeda em qualquer
lugar estático e a Hellen/qualquer pessoa consegue editar.

---

## 3. Estado ANTES desta sessão

```
E:\.projects\hellen-varella\
├── index.html      (17 KB) — one-page, ~11 seções
├── styles.css      (9 KB)  — CSS num arquivo só, variáveis --creme/--burgundy/…
├── app.js          (958 B) — menu mobile + filtro de portfólio
├── imagens/                — PASTA VAZIA (as fotos nunca entraram)
└── .cursor/logs/sessao.md  — log das 3 etapas da sessão anterior
```

O que o site fazia:

- Hero com título **"Beleza que transforma, cuidado que faz a diferença."**
- Seções: A Hellen · A experiência (3 ofícios) · Valores (6 combos/itens) ·
  Cursos · Portfólio (6 recortes + filtro) · Divas (link Instagram) ·
  Como funciona · Agenda.
- Links de WhatsApp escritos à mão, um a um.
- Filtro de portfólio em JS.
- **Sem fotos** (a pasta `imagens/` estava vazia; o HTML não referenciava
  nenhuma imagem — as seções eram só tipografia sobre cor).

### Desalinhamentos com o briefing (o motivo da refatoração)

| Item | Antes | Briefing pede |
|------|-------|----------------|
| Paleta | `#f6efe6`, `#6b2c38` (burgundy próprio) | `#FDF8F5`, `#3B1C28`, `#FED5CB`, `#6D2C45`, `#B86B58` |
| Tipografia | Cormorant Garamond + Great Vibes (script) | Perandory Condensed (título) + Poppins (corpo) |
| Mensagem central | "Beleza que transforma…" | **"Você vai ter dó de tirar a maquiagem."** |
| Fonte script cursiva | usada no hero e em títulos | não existe no briefing (é clichê de "salão") |
| Diferencial "tudo no mesmo lugar" | só como frase de apoio | é **o** diferencial — tem que ser estrutural |

---

## 4. Estado DEPOIS desta sessão

```
E:\.projects\hellen-varella\
├── index.html                — vitrine refeita no briefing (13 seções, slots, data-*)
├── 404.html · obrigada.html  — páginas de apoio (na identidade; obrigada.html ociosa)
├── manifest.webmanifest · robots.txt · sitemap.xml
├── README.md · AGENTS.md · CHANGELOG.md · .gitignore · .editorconfig
│
├── assets/
│   ├── css/   tokens.css · base.css · layout.css · components.css · utilities.css
│   ├── js/    main · nav · reveal · portfolio · whatsapp · pricing        (ativos)
│   │          lightbox · agenda · depoimentos · analytics                 (ociosos)
│   ├── fonts/ README.md  (como instalar Perandory / a substituta)
│   ├── img/   README.md + placeholder/ (SVGs de marcador; sem fotos ainda)
│   └── icons/ favicon.svg · whatsapp.svg
│
├── data/      studio · servicos · portfolio · faq  (fonte de verdade do conteúdo)
│              agenda · depoimentos                 (ociosos / Suposição)
│
├── content/   _MODELO-secao.html + generated/ (fragmentos gerados de data/*.json)
│
├── docs/      MAPA-DO-REPOSITORIO (este) · BRIEFING · PAINEL-SEMANTICO ·
│              DESIGN-SYSTEM · SLOT-MAP · CHECKLIST-CONTEUDO ·
│              FERRAMENTAS-USADAS · ARQUITETURA
│
├── tools/     serve.mjs (ativo) · build-pages · new-section · check-links ·
│              optimize-images (ociosos até serem necessários)
│
├── design/canvas/  *.dc.html + canvas.json + hellen-varella-vitrine.html
│                   (artefato de design — ver DESIGN-SYSTEM.md)
│
└── .cursor/logs/sessao.md   — log acumulado
```

### Jornada da cliente no site refeito

1. **Hero (plum #3B1C28):** "Você vai ter dó de tirar a maquiagem." +
   posicionamento + `Agendar meu horário`.
2. **O diferencial — "Tudo no mesmo lugar":** faixa com Maquiagem **+**
   Cabelo **+** Fotografia ligados, e a frase da concorrência ("sai pronta e
   recebe muito mais fotos do que o mercado").
3. **A experiência (apoio #FED5CB):** "da mulher que se produz todo dia a
   quem nunca passou um batom" + os 3 sentimentos (Confiança, Exclusividade,
   Profissionalismo) + a linha sobre vergonha da câmera.
4. **Serviços:** os 3 ofícios em detalhe.
5. **Valores:** 6 pacotes + "Montar meu combo" (interação, `pricing.js`).
6. **Portfólio:** 6 recortes + filtro, incluindo **Artístico** (o "olhar artístico").
7. **A Hellen:** persona "elegante e confortável", a marca que "transforma
   momentos comuns em memórias", a visão do studio (equipe, agenda cheia).
8. **Cursos · Divas (prova social no Instagram) · Como funciona · FAQ.**
9. **Agenda (plum):** WhatsApp-first, telefone, Instagram/Threads.
10. **Rodapé (plum):** "Beleza que vira lembrança." + mensagem central.
11. **Botão de WhatsApp flutuante** em todas as telas.

Todos os CTAs de agendamento levam ao WhatsApp com uma mensagem já escrita
(`assets/js/whatsapp.js` monta os links a partir de `data-*`).

---

## 5. Como rodar

```bash
node tools/serve.mjs         # http://127.0.0.1:4173/
```

Ou abrir `index.html` direto no navegador (funciona; só `agenda.js` e
`depoimentos.js`, que dependem de `fetch`, ficam quietos em `file://` —
por isso hoje estão ociosos de qualquer jeito).

Deploy: publicar a pasta inteira em GitHub Pages / Netlify / Cloudflare Pages.
Nada a compilar.
