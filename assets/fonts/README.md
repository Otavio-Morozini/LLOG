# Fontes

## O que o briefing pede

| Papel | Fonte do briefing | Situação |
|-------|-------------------|----------|
| Título | **Perandory Condensed** | Só existe no Canva. Não tem versão web/licença aberta. |
| Corpo / subtítulo / botões | **Poppins** (Regular, Medium, SemiBold) | Google Fonts — carregada no `<head>` do `index.html`. |

## Perandory Condensed na web — o que fazer

Enquanto a Hellen não exporta o arquivo, a web usa uma **substituta**
(ver `docs/DESIGN-SYSTEM.md`): **Bodoni Moda** (Google Fonts) — serifada,
editorial, do mesmo registro "elegante". É `Suposição:`, não a fonte oficial.

A pilha em `assets/css/tokens.css` é:

```
--font-display: "Perandory Condensed", "Bodoni Moda", "Times New Roman", Georgia, serif;
```

O `@font-face` de `Perandory Condensed` hoje só tenta `local()` — quem tiver
a fonte instalada no sistema já a vê; os demais caem para Bodoni Moda. Sem 404.

### Quando o arquivo chegar

1. Peça à Hellen o arquivo da fonte (ideal: `.woff2`; serve `.otf`/`.ttf`).
   No Canva não dá para exportar a fonte — ela precisa ter comprado/baixado
   o arquivo de origem (ex.: o autor da Perandory, ou o pacote onde comprou).
   Se só houver `.otf`/`.ttf`, converta para `.woff2`
   (ex.: <https://google.github.io/woff2/> ou `fonttools`).
2. Salve como `assets/fonts/perandory-condensed.woff2`.
3. Em `assets/css/tokens.css`, no `@font-face`, **descomente** a linha `url(...)`.
4. Pronto — o site inteiro passa a usar Perandory no lugar de Bodoni Moda,
   sem mais nenhuma mudança.

### Licença

Confirme com a Hellen se a licença da Perandory permite uso em site
(web embedding). Muitas fontes de marketplace cobram licença web à parte.
Se não permitir, a substituta Bodoni Moda fica como definitiva.
