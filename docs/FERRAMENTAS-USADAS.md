# Ferramentas do ambiente realmente usadas nesta sessão

> Entrega 5. "Usar as ferramentas" não é frase de efeito — abaixo está o que
> foi aberto/rodado e **o que cada uma acrescentou** ao resultado.

| Ferramenta (ambiente Cursor / Claude Code) | Para quê foi usada | O que acrescentou |
|---|---|---|
| **Shell / Bash + Git** | `git status`, `git log`, `git branch`, `git remote` no repo | Confirmou: `E:\.projects\hellen-varella`, Git local, **0 commits, sem remote**. Base da Entrega 1 e do bloqueio de `git pull`. |
| **Leitor de PDF (Read) + `pdftoppm` (Poppler)** | Abrir `e:\gtonga\Meu briefing.pdf` (pp. 1–4) e **renderizar a página 4 em 200 DPI** | Transcrição literal do texto (pp. 1–3) e **leitura do painel semântico visual** (p. 4) → `docs/PAINEL-SEMANTICO.md`. Sem bloqueio de leitura visual. |
| **Ferramentas de arquivo (Read/Write/Edit/Glob)** | Ler o site antigo; escrever a estrutura nova | Mapa do "antes" (`index.html` 17 KB, `styles.css`, `app.js`, `imagens/` vazia) e todo o "depois". |
| **`unzip` / Expand-Archive** | Abrir `E:\gtonga\Entre-Cenas-projeto.zip` (o projeto-modelo citado no prompt) | Entendi o **padrão de estrutura** que o usuário quer herdar: `AGENTS.md`, `_data/*.json` como fonte de verdade, `docs/` (SLOT-MAP, CHECKLIST), `_MODELO.html`, marcadores de slot. Replicado aqui — **sem** importar tema de cinema/reviews. |
| **Claude Design (skill `design`) — canvas multi-prancheta** | Criar `design/canvas/*.dc.html` + `canvas.json`, seed e **publicar como Artifact** | **Artefato de design tangível** (Entrega 3): home desktop, home mobile, direção de marca, design system. Paleta e tipo do briefing. Exporta PNG/PDF; a Hellen abre pelo link. |
| **`artifact-capabilities` (skill)** | Ler o roster de capacidades da conta para publicar o canvas | Publicação do canvas com `self` + `downloads` (permite salvar/edição visual e export). |
| **Navegador embutido (preview) + `serve.mjs`** | Servir o site em `http://127.0.0.1:4173/` e inspecionar | Verificação real: screenshot do hero; `getComputedStyle` confirmou a paleta (`#FDF8F5`/`#3B1C28`/`#FED5CB`/`#6D2C45`); rede sem 404; **teste de mobile 375 px** (sem overflow, menu abre, grids colapsam). |
| **Console / DOM via `javascript_tool`** | Testar os módulos JS sem depender de renderização | Confirmado: 19 links de WhatsApp montados certo, `tel:` certo, filtro de portfólio, "Montar meu combo" (cabelo+make → "R$ 370 · Combo 2"), reveal com rede de segurança (39/39 visíveis). |
| **`read_network_requests` / `read_console_messages`** | Diagnóstico | Achei o bug do `h1` invisível (dark-sobre-dark no hero) e o 404 do `@font-face` — os dois corrigidos. |
| **Node (v24)** | Rodar `tools/*.mjs` | Confirmado que as 5 ferramentas rodam: `serve`, `build-pages` (`--check` e geração), `check-links` (acha os `[placeholders]`), `new-section`, `optimize-images` (degrada sem `sharp`). |
| **`mark_chapter`** | Organizar a sessão | Capítulos: mapa & briefing → design → reestruturação → documentação. |

## O que NÃO foi usado (e por quê)

- **Replit (`create_app_from_prompt`)** — criaria um app hospedado à parte; o
  pedido é melhorar **este repositório**, mantendo estático. Fora de escopo.
- **Gmail / computer-use / Chrome real** — nada no pedido exige e-mail,
  automação de desktop ou sessões logadas.
- **Firecrawl / WebSearch / Microsoft Learn** — o conteúdo é o briefing + o
  repo; não há pesquisa externa a fazer sem risco de alucinar dados da Hellen.
