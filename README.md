# Studio Hellen Varella — vitrine

Site de uma página do Studio Hellen Varella (maquiagem, cabelo e fotografia
no mesmo atendimento) — Fraiburgo, SC.

**"Você vai ter dó de tirar a maquiagem."**

## Para ver rodando

```bash
node tools/serve.mjs
# abre em http://127.0.0.1:4173/
```

Ou abra `index.html` direto no navegador.

## O que é

- HTML + CSS + JavaScript puro. **Sem build, sem framework, sem dependências.**
- Deploy: subir a pasta inteira em qualquer host estático
  (GitHub Pages, Netlify, Cloudflare Pages).
- Identidade (cores, tipografia, mensagem) vem do briefing da cliente —
  ver `docs/BRIEFING.md`.

## Estrutura

| Pasta | O que tem |
|-------|-----------|
| `index.html` | a vitrine |
| `404.html`, `obrigada.html` | páginas de apoio (na identidade) |
| `assets/css/` | design system em camadas (`tokens` → `base` → `layout` → `components` → `utilities`) |
| `assets/js/` | módulos ativos (`nav`, `reveal`, `portfolio`, `whatsapp`, `pricing`) e ociosos (`lightbox`, `agenda`, `depoimentos`, `analytics`) |
| `assets/img/`, `assets/fonts/` | READMEs com o que colocar (fotos e a fonte Perandory) |
| `data/*.json` | **fonte de verdade do conteúdo** — cada arquivo diz de onde veio cada dado |
| `docs/` | mapa do repo, briefing mapeado, design system, slot-map, checklist, ferramentas, arquitetura |
| `tools/*.mjs` | `serve` (ativo) + `build-pages`, `new-section`, `check-links`, `optimize-images` |
| `design/canvas/` | o artefato de design (Claude Design) que guiou a refatoração |

## Antes de publicar

1. `docs/CHECKLIST-CONTEUDO.md` — falta principalmente **as fotos** e alguns
   dados que só a Hellen confirma.
2. `node tools/check-links.mjs` — tem que passar sem erros.

## Para outro agente

Comece por **[`AGENTS.md`](AGENTS.md)**.

## Histórico

`git log` e `CHANGELOG.md`. Log de sessão em `.cursor/logs/sessao.md`.
