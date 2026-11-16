# Imagens

O site hoje roda **sem nenhuma foto** — usa molduras/gradientes de marcador
(`assets/img/placeholder/`). Isso é de propósito: o layout já está pronto para
receber as fotos reais da Hellen assim que ela escolher.

## O que colocar aqui

| Pasta / arquivo | Onde aparece | Proporção | Peso alvo |
|-----------------|--------------|-----------|-----------|
| `hero.jpg` | Moldura do topo (retrato de cliente pronta, luz quente) | 4:5 (retrato) | < 250 KB |
| `portfolio/noiva-brilho-do-sim.jpg` | Portfólio · Noiva | 3:2 ou 4:5 | < 220 KB |
| `portfolio/gestante-corpo-tempo-luz.jpg` | Portfólio · Gestante | 3:2 | < 220 KB |
| `portfolio/social-a-melhor-versao.jpg` | Portfólio · Social | 3:2 | < 220 KB |
| `portfolio/cabelo-camadas-leves.jpg` | Portfólio · Cabelo | 3:2 | < 220 KB |
| `portfolio/making-o-antes-da-foto.jpg` | Portfólio · Making of | 3:2 | < 220 KB |
| `portfolio/artistico-o-outro-lado.jpg` | Portfólio · Artístico | 3:2 | < 220 KB |
| `og.jpg` | Prévia ao compartilhar link (WhatsApp, Instagram) | 1200×630 | < 300 KB |

Os caminhos esperados estão em `data/portfolio.json` (`imagem_placeholder`).

## Direção (do painel semântico do briefing — `docs/PAINEL-SEMANTICO.md`)

- Luz quente e dourada; pele com brilho, não fosca.
- Peles diversas (o público vai de crianças a idosas).
- Close editorial, joia dourada como acento, mão no enquadramento.
- Nada de foto fria, plana ou "cartão de visita de salão".

## Como otimizar

```bash
node tools/optimize-images.mjs
```

Sem a lib `sharp` instalada, o script só mostra o passo a passo manual
(exportar a 2000 px no maior lado, qualidade ~80, salvar como `.jpg` ou `.webp`).

## Depois de adicionar

1. Trocar os marcadores no `index.html` pelos `<img>` reais
   (ou usar `tools/build-pages.mjs` para gerar o portfólio a partir do JSON).
2. Marcar cada foto do portfólio com `data-lightbox="portfolio"` para ligar
   a galeria em tela cheia (`assets/js/lightbox.js`).
3. Rodar `node tools/check-links.mjs`.
