# Mapa de slots — `index.html`

> Cada espaço editável do HTML tem `data-slot="area.campo"`. Preencha/edite
> **dentro** do elemento; não apague o atributo até a publicação. Fonte de
> verdade do conteúdo: `data/*.json` (espelhe as duas pontas ou use
> `tools/build-pages.mjs`).

## Global

| Slot / marca | Onde | O que colocar |
|--------------|------|----------------|
| `brand.name` | `.brand` no header | Nome da marca (hoje: Hellen Varella) |
| `body[data-wa-number]` | `<body>` | Número do WhatsApp só dígitos (fonte: `data/studio.json`) |
| `body[data-wa-link]` | `<body>` | Link curto `wa.me/message/...` |
| `body[data-tel]` | `<body>` | Telefone para `tel:` |
| `footer.frase` | rodapé | Frase institucional (hoje: "Beleza que vira lembrança.") |
| `[data-ano]` | rodapé | Ano (preenchido por `main.js`) |

## Seções

| Slot | Bloco | Conteúdo esperado |
|------|-------|-------------------|
| `hero.eyebrow` | §inicio | Assinatura curta (Studio… · cidade) |
| `hero.title` | §inicio | **Mensagem central** do briefing |
| `hero.lead` | §inicio | Posicionamento resumido + diferencial |
| `diferencial.lead` | §diferencial | O "cuidado completo" + frase da concorrência |
| `experiencia.lead` | §experiencia | "elegante e confortável" + exclusividade |
| `servicos.lista` | §servicos | 3 cartões (Maquiagem, Cabelo, Fotografia) — `data/servicos.json → servicos_detalhe` |
| `valores.combos` | §valores | 6 `.pack` — `data/servicos.json → combos + avulsos` |
| `valores.extra` | §valores | Linha do mini bolo / aniversário |
| `portfolio.obras` | §portfolio | 6 `.work` — `data/portfolio.json → obras` |
| `hellen` (persona) | §hellen | Persona + marca + transformação + visão (texto do briefing) |
| `cursos.lista` | §cursos | Curso Pro + automake — `data/servicos.json → cursos` |
| `faq.lista` | §faq | `<details>` — `data/faq.json → itens` (sem os `_placeholder`) |
| `como.passos` | §como-funciona | 6 passos — `data/servicos.json` (reserva) + regras do repo |

## Contêineres de módulos ociosos

| Marca | Onde | Liga o quê |
|-------|------|-----------|
| `[data-depoimentos]` | §divas | `assets/js/depoimentos.js` → lê `data/depoimentos.json` |
| `[data-agenda]` | §agenda | `assets/js/agenda.js` → lê `data/agenda.json` |
| `[data-combo-builder]` | §valores | `assets/js/pricing.js` (este **já está ativo**) |
| `[data-lightbox="portfolio"]` | (adicionar nas fotos) | `assets/js/lightbox.js` |

## Links de ação

Todo CTA de agendamento:

```html
<a class="button" href="#agenda"
   data-wa                              <!-- marca para o whatsapp.js -->
   data-wa-msg="Oi, Hellen! ..."        <!-- mensagem pronta -->  OU
   data-wa-curto                        <!-- usa o link curto wa.me/message/... -->
   data-track="rotulo">Texto</a>        <!-- opcional: para o analytics.js -->
```

`assets/js/whatsapp.js` reescreve o `href` no carregamento. Sem JS, o `href="#agenda"`
leva à seção de agenda, que tem o botão principal do WhatsApp.
