# Briefing da cliente — transcrição e mapeamento

> Entrega 2. Fonte: **`e:\gtonga\Meu briefing.pdf`**, escrito pela própria
> Hellen (cliente e dona do studio). Páginas 1–3 = texto (abaixo, transcrito
> literal). Página 4 = painel semântico visual → `docs/PAINEL-SEMANTICO.md`.
>
> Regra: nada aqui foi reinterpretado. Cada bloco tem **onde ele aparece no
> site** (seção + arquivo). O que a Hellen não escreveu está marcado
> `Suposição:` ou fica de fora.

---

## Bloco a bloco — texto do PDF → lugar no site

### POSICIONAMENTO
> "Para quem precisa de dar um Up na autoestima, a Hellen Varella é um Studio
> de beleza e fotografia que proporciona uma experiência completa de cuidado,
> fazendo cada cliente se sentir bonita, confiante e digna de ser lembrada."

**No site:** subtítulo do hero (`index.html` §hero) e `data/studio.json →
marca.posicionamento`. "Digna de ser lembrada" ecoa no rodapé
("Beleza que vira lembrança").

### OBJETIVO E VISÃO
> "Construir uma marca reconhecida pela qualidade do atendimento e da
> experiência oferecida, mantendo agenda cheia, ter uma equipe para trabalhar
> em outras áreas da beleza. Investimento de equipamentos e materiais
> profissionais para oferecer cada vez mais excelência em cabelo, maquiagem
> e fotografia."

**No site:** seção **A Hellen** (`index.html` §hellen), parágrafo "A visão do
studio: manter a agenda cheia, formar equipe… investir em equipamento e
material profissional". "Agenda cheia" também sustenta a seção **Agenda**.
É visão de futuro — entra como narrativa da marca, **não** como afirmação de
que a equipe já existe (ver anti-alucinação).

### MENSAGEM CENTRAL
> "Você vai ter dó de tirar a maquiagem."

**No site:** é o **`<h1>` do hero**. Repetida no rodapé e em `obrigada.html`.
É a frase mais visível do site. `data/studio.json → marca.mensagem_central`.

### PÚBLICO ALVO
> "Mulheres de todas as idades, desde crianças até idosas. A maior parte das
> clientes são adolescentes e mães de família que desejam se sentir bonitas,
> confiantes e bem cuidadas. Procuram um ambiente acolhedor, onde se sintam à
> vontade como se estivessem em casa. Escolhem a Hellen porque encontram
> cabelo, maquiagem e fotografia no mesmo lugar, com praticidade e um
> atendimento personalizado."

**No site:**
- "todas as idades / crianças a idosas" → direção de fotografia pede **peles
  e idades diversas** (`PAINEL-SEMANTICO.md`);
- "ambiente acolhedor, como em casa" → tom da seção **A experiência** e da
  persona ("acolhe quem nunca se produziu");
- "cabelo, maquiagem e fotografia no mesmo lugar" → seção **O diferencial**.

### CONCORRÊNCIA
> "Há muitos profissionais na minha cidade da mesma área. Bastante fotógrafos
> também, mas sou a única que entrega tudo no mesmo lugar. A cliente sai
> pronta e recebe muito mais fotos do que tem no mercado."

**No site:** seção **O diferencial** — a frase "a cliente sai pronta e recebe
muito mais fotos do que o mercado costuma entregar" está literal no
`index.html` §diferencial.

### O QUE VOCÊ QUER?
> "Voltem sempre, indiquem meu trabalho e sintam orgulho de postar meu
> trabalho."

**No site:** seção **Divas** ("Elas voltam sempre, indicam o trabalho e têm
orgulho de postar") e `obrigada.html` ("quando seu trabalho ficar pronto,
marca @hellenvarella.makeup"). O convite a marcar/compartilhar é a tradução
direta desse desejo.

### QUEM É SUA MARCA?
> "A Hellen Varella é uma marca que transforma momentos comuns em memórias
> especiais."

**No site:** `<h2>` da seção **A Hellen** ("Uma marca que transforma momentos
comuns em memórias especiais"). `data/studio.json → marca.marca_frase`.

### SE A HELLEN VARELLA FOSSE UMA PESSOA
> "Ela seria uma mulher elegante e confortável ao mesmo tempo, que gosta de se
> cuidar e se arrumar, mas que também acolhe aquela mulher que nunca fez
> maquiagem ou que não tem costume de se produzir."

**No site:** primeiro parágrafo da persona (§hellen), quase literal. E o
**título da seção A experiência**: "Da mulher que se produz todo dia a quem
nunca passou um batom." Guia as **duas pontas do tom**: elegante *e* acolhedor.

### SENTIMENTOS QUE A IDENTIDADE VISUAL DEVE TRANSMITIR
> "Confiança → a cliente sente que está em boas mãos.
> Exclusividade → cada atendimento é pensado para aquela pessoa.
> Profissionalismo → demonstra experiência e qualidade."

**No site:** os três `.pillar` da seção **A experiência**, com o texto de cada
sentimento adaptado ao contexto (ex.: Profissionalismo → "maquiadora desde
2013, fotógrafa desde 2021, equipamento e material profissional").

### O QUE NÃO DEVE PARECER
> "Não deve ser amadora, genérica ou mais um salão de beleza. Ela quer ser uma
> identidade que mostra personalidade, cuidado e um olhar artístico."

**No site (decisões de design, `DESIGN-SYSTEM.md`):**
- **sem fonte script/cursiva** (o clichê nº 1 de "salão");
- serifada editorial (Bodoni/Perandory) + plum profundo → registro de revista,
  não de tabela de preços de salão;
- filtro **Artístico** no portfólio = o "olhar artístico" explícito;
- nada de ícone genérico de "spa", nada de stock sorridente.

### A TRANSFORMAÇÃO ENTREGUE
> "Depois de passar pela Hellen Varella, a cliente se sente bem acolhida e se
> enxerga mais bonita. Mais do que mudar a aparência, ela vive um momento em
> que consegue se sentir confiante e guardar uma lembrança especial daquela
> fase da vida."

**No site:** segundo parágrafo da persona (§hellen), quase literal.

### O GRANDE DIFERENCIAL
> "A cliente não precisa procurar maquiagem, cabelo e fotos separadamente:
> recebe um cuidado completo, com orientação para se sentir confortável diante
> da câmera, mesmo sendo uma pessoa que tem vergonha ou não tem costume de
> fazer fotos."

**No site:** seção **O diferencial** (o "cuidado completo", "um dia só") +
linha em **A experiência**: "Se você tem vergonha ou nunca teve o costume de
fazer fotos… a orientação diante da câmera faz parte do atendimento." +
FAQ "Tenho vergonha de foto e nunca me maquiei. Serve pra mim?".

---

## Identidade visual (tabela do PDF, p. 3)

| Elemento | Fonte (briefing) | Cor (briefing) | No site |
|----------|------------------|----------------|---------|
| Título | Perandory Condensed (só no Canva) | `#3B1C28` | `--font-display`; substituta **Bodoni Moda** (`Suposição:`) |
| Subtítulo | Image + Poppins (ou só Poppins Medium) | `#6D2C45` | `.subtitle` = Poppins Medium, cor `--cta` |
| Corpo | Poppins Regular e Medium | `#3B1C28` | `--font-body` = Poppins; `body { color: --ink }` |
| Fundo | — | `#FDF8F5` | `--bg` |
| Apoio | — | `#FED5CB` | `--support` |
| CTA/Botões | Poppins SemiBold | `#6D2C45` ou `#7A3450`, texto branco | `.button` = `--cta` / `--cta-alt`, `font-weight: 600`, `color: #FDF8F5` |

## Paleta (p. 3)

| Papel | Hex | Token |
|-------|-----|-------|
| Fundo | `#FDF8F5` | `--bg` |
| Texto principal | `#3B1C28` | `--ink` (e `--plum`, usado como fundo escuro) |
| Cor de apoio | `#FED5CB` | `--support` |
| CTA | `#6D2C45` | `--cta` |
| Cor quente | `#B86B58` | `--warm` |

Conferido no site com `getComputedStyle` (ver `FERRAMENTAS-USADAS.md`):
`body` = `rgb(253,248,245)` / `rgb(59,28,40)`; `.button` = `rgb(109,44,69)`;
§experiencia = `rgb(254,213,203)`. Bate com o briefing.

## Hierarquia (p. 3) — implementada em `assets/css/base.css`

- Título: `--font-display`, `#3B1C28` (claro sobre plum quando em seção escura).
- Subtítulo: Poppins Medium, `#6D2C45` (`.subtitle`, `.eyebrow` no CTA).
- Texto: Poppins Regular, `#3B1C28`.
- Botões: fundo `#6D2C45`, texto branco (`.button`).

---

## O que NÃO estava no briefing (e como foi tratado)

| Item | Origem | Tratamento |
|------|--------|-----------|
| Cidade Fraiburgo/SC, telefone (49) 99829-3732, `@hellenvarella.makeup`, link `wa.me/message/RAVKCLUTZ6AGG1` | repositório (sessão anterior, de prints da cliente) | **preservado**, marcado como "herdado do repo" em `data/studio.json` |
| Preços (R$ 300–420), combos, "não faço corte curto", sinal R$ 30, mini bolo R$ 35, "maquiadora desde 2013 / fotógrafa 2021" | repositório | **preservado**, `data/servicos.json`; confirmar antes de mudar |
| Sistema de depoimentos no site | ninguém | **`Suposição:`** — `data/depoimentos.json` + `depoimentos.js` ficam ociosos; hoje a prova social é o Instagram |
| Agenda/disponibilidade no site | ninguém (briefing só diz "agenda cheia") | **`Suposição:`** — `data/agenda.json` + `agenda.js` ociosos; a reserva continua no WhatsApp |
| E-mail, endereço exato, horário | ninguém | **`[PLACEHOLDER]`** em `data/studio.json` — não inventados |
| Substituta de Perandory (Bodoni Moda) | decisão de design | **`Suposição:`** rotulada em `DESIGN-SYSTEM.md` e `tokens.css` |
