# Arquitetura e decisões

## Stack: HTML/CSS/JS estático, sem build

**Mantida** da versão anterior. Alternativas descartadas:

- **Vite + React / Next** — traria build, deploy mais complexo e uma barreira
  para a Hellen (ou qualquer pessoa) editar. O site é uma vitrine de ~13
  seções; não justifica.
- **Gerador estático (11ty/Astro)** — tentador para consumir `data/*.json`,
  mas adiciona toolchain. Em vez disso: `data/*.json` é a fonte de verdade,
  `index.html` traz o mesmo conteúdo à mão (funciona sem nada), e
  `tools/build-pages.mjs` mantém as pontas em sincronia quando alguém quiser.

Resultado: `git clone` → abrir `index.html` → funciona. Deploy = subir a pasta.

## CSS em camadas (`assets/css/`)

`tokens` (variáveis do briefing) → `base` (reset, tipo) → `layout`
(header, seções, hero, rodapé) → `components` (botões, cartões…) →
`utilities` (helpers, reveal, lightbox). Ordem importa: carregadas nessa
sequência no `<head>`.

## JS: scripts clássicos, não módulos ES

Cada `assets/js/*.js` é um IIFE que se auto-inicializa e **só age se achar o
alvo no DOM**. Motivo: `import`/`export` e `fetch` de arquivos locais
**quebram em `file://`** (a Hellen pode abrir o `index.html` clicando duas
vezes). Assim tudo funciona nos dois modos.

- **Ativos:** `main` (bootstrap), `nav`, `reveal`, `portfolio`, `whatsapp`, `pricing`.
- **Ociosos** (prontos, esperando conteúdo/gatilho): `lightbox` (espera
  `[data-lightbox]`), `agenda` (espera `[data-agenda]` + servidor),
  `depoimentos` (espera `[data-depoimentos]` + servidor), `analytics`
  (opt-in, espera `window.HV_ANALYTICS`).

Nenhum módulo ocioso dá erro se o alvo não existe — retornam cedo.

## Conteúdo dirigido por dados

`data/*.json` com um campo `_fonte` em cada arquivo dizendo **de onde veio**
cada informação (briefing / repo / placeholder / Suposição). É a defesa
contra alucinação: quem editar sabe o que pode mexer e o que precisa
confirmar com a Hellen.

## WhatsApp-first

Sem formulário, sem backend. `assets/js/whatsapp.js` monta os links `wa.me`
a partir de `data-wa-msg` (mensagem pronta) ou `data-wa-curto` (link curto),
lendo o número de `<body data-wa-number>`. Sem JS, os CTAs caem na seção
**Agenda**, que tem o botão principal.

## Acessibilidade e performance

- Sem dependências de terceiros no site (0 KB de framework). Só 2 famílias de
  fonte do Google Fonts.
- `IntersectionObserver` com 3 camadas de fallback para nunca prender conteúdo.
- `prefers-reduced-motion` respeitado.
- Imagens (quando entrarem): `<img>` com `width/height`, `.webp` + `.jpg`,
  `loading="lazy"` fora do hero.

## O que ficou de fora (não pedido)

E-commerce, login, agendamento automático, blog, multi-idioma, PWA offline
completo (só o `manifest` básico). Se algum for pedido, `content/_MODELO-secao.html`
e `tools/new-section.mjs` dão o ponto de partida.
