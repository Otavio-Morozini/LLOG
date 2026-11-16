# Painel semântico — leitura das páginas 3–4 do briefing

> O briefing termina com "Agora meu painel semântico:" e uma **página 4
> inteira de moodboard visual**. Este documento registra o que foi visto ali
> (o PDF foi aberto e a página 4 renderizada em alta resolução — ver
> `FERRAMENTAS-USADAS.md`). Nada aqui é invenção; é descrição do que a Hellen
> montou.

---

## O que está na página 4

Uma **colagem estilo polaroid** sobre um **fundo plum profundo** (o mesmo
`#3B1C28` do "texto principal" da paleta). As fotos têm **moldura branca**.
No canto superior, o **logotipo**:

```
HELLEN VARELLA        ← serifada condensada, caixa alta, MUITO espaçada (isto é a Perandory Condensed)
   Makeup             ← Poppins, caixa baixa, peso médio
```

em creme sobre o plum.

### As imagens da colagem (descrição)

- mulher aplicando máscara de cílios, luz quente;
- coque preso elegante com boca vinho, brinco dourado;
- **close editorial de olho** com esfumado terracota/cobre cintilante;
- mulher de óculos escuros e argolas douradas passando batom;
- **três mulheres de tons de pele diferentes** (loira, negra, morena) juntas
  — diversidade explícita;
- batons em bala nos tons nude / terracota / caramelo;
- paleta de pó compacto em nudes quentes;
- blush/bronzer compactos;
- mulher com cabelo *balayage* caramelo segurando um batom vinho, gola alta
  bordô;
- mão com manicure/luva bordô escura junto ao rosto.

---

## Leitura → decisões no site

| O que o painel mostra | Decisão |
|-----------------------|---------|
| **Fundo plum `#3B1C28` como palco**, fotos em moldura creme | O plum não é só cor de texto: é **fundo de seção**. Hero, Agenda e rodapé são plum; as fotos entram em **`.photo-frame`** (moldura branca, leve rotação — a "polaroid" do painel). |
| Logo serifada condensada, caixa alta, super espaçada | `.brand` e `h1/h2` em `--font-display` caixa alta com `letter-spacing` largo. Sem versão web da Perandory → **Bodoni Moda** como substituta (`Suposição:`). |
| "Makeup" em Poppins caixa baixa sob o nome | Assinatura "Studio de beleza e fotografia" em Poppins sob a marca; `.eyebrow` em Poppins Medium. |
| Paleta das fotos: terracota, nude, caramelo, blush, dourado | `--warm #B86B58` (do briefing) para acentos; **caramelo `#C98B6B` e dourado `#C9A24B`** são leituras do painel — entram **só como detalhe** (`--caramelo`, `--dourado` em `tokens.css`), nunca como cor de área. |
| Joia dourada recorrente | Acento dourado permitido em detalhes finos (não usado ainda; token pronto). |
| Peles e idades diversas | **Direção de fotografia:** as fotos reais devem incluir peles e idades variadas (bate com "de crianças a idosas" do público-alvo). |
| Close, mãos no enquadramento, gesto de aplicar produto | **Direção de fotografia:** enquadramento editorial, não "cartão de visita". Descrito em `assets/img/README.md`. |
| Pele com brilho, luz quente/dourada | **Direção de fotografia / edição:** pele luminosa, não fosca; temperatura quente. |
| Nada plano, nada frio, nada "genérico de salão" | Confirma "O QUE NÃO DEVE PARECER" do texto. |

---

## Onde isso vira artefato

O painel foi traduzido no **canvas de design** (`design/canvas/Direcao.dc.html`
e a paleta em `Sistema.dc.html`) — ver `docs/DESIGN-SYSTEM.md`. A colagem da
Hellen **não foi copiada** (são imagens de stock/referência, não fotos do
trabalho dela); o que se herdou foi **cor, tipo, forma e direção**.

---

## Bloqueio declarado

Nenhum. A página 4 foi aberta e lida. As páginas 1–3 (texto) conferem com o
que a cliente passou no prompt. O único conteúdo do PDF que **não** é usável
como asset é a própria colagem (referência visual, não material da marca).
