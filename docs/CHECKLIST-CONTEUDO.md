# Checklist de conteúdo — o que falta antes de publicar

> O site funciona hoje, mas com **marcadores** no lugar de fotos e de alguns
> dados que só a Hellen tem. Rode `node tools/check-links.mjs` a qualquer
> momento — ele lista o que ainda está entre `[colchetes]`.

## 1. Fotos (o maior item)

- [ ] `assets/img/hero.jpg` — retrato de cliente pronta, 4:5, luz quente
- [ ] `assets/img/portfolio/noiva-brilho-do-sim.jpg`
- [ ] `assets/img/portfolio/gestante-corpo-tempo-luz.jpg`
- [ ] `assets/img/portfolio/social-a-melhor-versao.jpg`
- [ ] `assets/img/portfolio/cabelo-camadas-leves.jpg`
- [ ] `assets/img/portfolio/making-o-antes-da-foto.jpg`
- [ ] `assets/img/portfolio/artistico-o-outro-lado.jpg`
- [ ] `assets/img/og.jpg` — 1200×630, prévia ao compartilhar link
- [ ] Direção: peles e idades diversas, luz quente, close editorial (ver `PAINEL-SEMANTICO.md`)
- [ ] Rodar `node tools/optimize-images.mjs`
- [ ] Trocar os `.photo-frame__img` e os `.work` de texto por `<img>` reais
- [ ] Marcar cada foto do portfólio com `data-lightbox="portfolio"`

## 2. Dados que só a Hellen confirma (`data/studio.json`)

- [ ] E-mail — publicar ou não?
- [ ] Endereço do studio — publicar o endereço ou manter só "Fraiburgo, SC"?
- [ ] Horário de atendimento
- [ ] Confirmar que o número `5549998293732` e o link `wa.me/message/RAVKCLUTZ6AGG1` estão certos

## 3. Serviços e preços (`data/servicos.json`)

- [ ] Confirmar todos os preços (R$ 260 a R$ 420, corte R$ 60, Quinta R$ 150, bolo R$ 35)
- [ ] Confirmar prazos ("7 dias úteis", durações)
- [ ] Confirmar "desde 2013" (maquiagem) e "desde 2021" (fotografia)
- [ ] Cursos: manter "valor e turma no WhatsApp" ou publicar datas?

## 4. FAQ (`data/faq.json`)

- [ ] "Atende em outras cidades?" — resposta real
- [ ] "Formas de pagamento?" — resposta real

## 5. Prova social

- [ ] Confirmar que o destaque do Instagram se chama mesmo "FEEDBACKS"
- [ ] (Opcional) Trazer depoimentos para dentro do site: preencher
      `data/depoimentos.json` **com autorização das clientes**, adicionar
      `<div class="divas" data-depoimentos></div>` na §divas, servir o site.
      Isso é `Suposição:` — o briefing não pede.

## 6. Agenda

- [ ] (Opcional / `Suposição:`) Ligar a faixa de disponibilidade:
      preencher `data/agenda.json`, adicionar `<div class="agenda-strip" data-agenda></div>`
      na §agenda. Não cria reserva — a reserva continua no WhatsApp.

## 7. Publicação

- [ ] Escolher domínio e trocar `[DOMINIO-QUANDO-PUBLICAR]` em `index.html`
      (canonical + og:image), `robots.txt`, `sitemap.xml`
- [ ] Criar repositório remoto e `git remote add origin <url>`
- [ ] Deploy: GitHub Pages / Netlify / Cloudflare Pages (pasta estática)
- [ ] (Opcional) Ligar `assets/js/analytics.js`: definir
      `window.HV_ANALYTICS = { endpoint: "..." }` antes do `<script>` e descomentar
- [ ] Testar em celular real (o menu, os CTAs de WhatsApp, o filtro de portfólio)
- [ ] Rodar `node tools/check-links.mjs` até zerar os erros

## 8. Fonte de título

- [ ] Pedir à Hellen o arquivo da **Perandory Condensed** (ver `assets/fonts/README.md`).
      Se a licença não permitir uso web, **Bodoni Moda** fica como definitiva.
