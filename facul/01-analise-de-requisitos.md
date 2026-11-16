# Análise de requisitos — sistema web do Studio Hellen Varella

Documento da Parte II da extensão. Data de referência: 13 de outubro de 2026.

O sistema é a vitrine do studio (maquiagem, cabelo e fotografia no mesmo atendimento), em Fraiburgo/SC. A reserva continua no WhatsApp. Este texto classifica o que a microempreendedora já pediu, o que a pesquisa de mercado acrescentou e o que ainda depende da validação dela sobre o protótipo.

Fonte primária de identidade e de demanda: briefing escrito pela própria Hellen (`E:\gtonga\Meu briefing.pdf`, transcrito em `docs/BRIEFING.md`). Nada que ela não tenha dito entra aqui como requisito confirmado. O que veio de cadastro público, de material anterior ou de decisão de projeto está rotulado.

---

## 1. Partes interessadas

| Parte | Interesse |
| --- | --- |
| Hellen Luci Varella, MEI, dona do studio | Ser reconhecida pelo atendimento e pela experiência; manter a agenda cheia; fazer a cliente voltar, indicar e ter orgulho de postar o trabalho. |
| Cliente do studio | Entender o que está incluso, o preço e como reservar, num ambiente que pareça acolhedor e profissional. |
| Equipe da extensão (Escola Politécnica, Univali) | Entregar um sistema web fiel à demanda e registrar a participação da microempreendedora. |
| Visitante que chega pelo Instagram | Cair numa página que repete a mesma mensagem da marca e abre a conversa no WhatsApp com o serviço já nomeado. |

Público descrito por ela: mulheres de todas as idades, de crianças a idosas. A maior parte são adolescentes e mães. Procuram um lugar acolhedor, “como se estivessem em casa”, e escolhem a Hellen porque encontram cabelo, maquiagem e fotografia no mesmo lugar.

## 2. Técnicas de elicitação usadas

| Técnica | O que foi feito | Resultado |
| --- | --- | --- |
| Análise de documento | Leitura integral do briefing escrito pela Hellen (posicionamento, visão, mensagem, público, concorrência, persona, sentimentos da marca, o que a identidade não pode parecer, transformação, diferencial, paleta e tipografia). | Requisitos de conteúdo, de tom e de design confirmados na origem. |
| Análise de artefato | Textos de preço, combos, sinal, telefone e @ já usados por ela; ficha pública do studio; cadastro de MEI. | Regras de negócio candidatas. Preço e contato seguem pendentes de confirmação antes de qualquer mudança. |
| Pesquisa de área e concorrência | Consulta, em 13/10/2026, a cadastros e listagens públicas de estética e fotografia em Fraiburgo. | Diagnóstico da seção 4. Achados que contradizem ou completam o briefing ficam como pergunta, não como fato fechado. |
| Brainstorm da equipe | O que a página precisa resolver antes da conversa no WhatsApp: diferencial, preço, portfólio, medo de foto, como reservar. | Casos de uso UC01–UC07 e a decisão de não criar login nem formulário. |
| Prototipação para validação | Telas em `facul/prototipo/` e vitrine em `index.html`, para a Hellen percorrer no celular. | Instrumento pronto. O retorno dela ainda entra pelo questionário em `04-questionario-validacao.md`. |

Entrevista gravada, videochamada e questionário respondido ainda não estão no pacote desta data. O briefing escrito é a evidência de concepção. A validação do protótipo é o próximo passo com ela (seção de evidências).

## 3. Problema que o sistema resolve

A Hellen atende por Instagram e WhatsApp. O preço, o que entra em cada combo e a regra de reserva se perdem em conversa e em story. Ela descreveu o mercado local assim: há muitos profissionais da mesma área e bastante fotógrafos, e o que a diferencia é entregar tudo no mesmo lugar — a cliente sai pronta e recebe mais fotos do que o mercado costuma entregar.

O sistema web organiza essa oferta num endereço estável, na identidade visual que ela definiu, e devolve a conversa para o WhatsApp com a mensagem já preenchida (combo, serviço ou curso).

Ficou de fora de propósito, porque ela não pediu e porque aumentaria a barreira para uma MEI manter o site: loja virtual, login, pagamento no site, agendamento automático, blog e área administrativa.

## 4. Pesquisa de área e concorrência

Consulta em 13/10/2026. Fontes no fim do documento.

**A microempreendedora.** MEI ativa desde 21/05/2019, CNPJ 33.687.461/0001-33, Fraiburgo/SC, optante pelo Simples Nacional. CNAE principal 9602-5/02 (estética e outros serviços de beleza). CNAEs secundários compatíveis com o que o studio oferece: cabeleireiro e outras atividades de ensino (os cursos Pro e automake). Capital social registrado de R$ 3.000,00. O telefone público (49) 99829-3732 é o mesmo já usado no site. Uma listagem do município (maiscnpj, mesma data) aponta 64 empresas ativas em Fraiburgo com esse CNAE principal: o mercado local de beleza é concorrido, como ela mesma escreveu.

**Presença pública do studio.** Ficha “Studio Hellen Varella” com nota 5,0 em cinco avaliações (textos de 17/09/2024: ambiente, maquiagem, atendimento acolhedor). Horário exibido nessa ficha: segunda a sexta, 13h30–20h20; sábado, manhã até 20h30; domingo fechado. O horário 9h01 de sábado parece erro de listagem. Endereço do cadastro MEI: Rua Suíça, 117, Das Nações. A ficha do studio mostra Rua Suíça, 129. E-mail público do cadastro: hellevarella@outlook.com. O link curto de WhatsApp dessa ficha (`wa.me/message/GDRWUOXUDGZSF1`) é outro, diferente do que está no site (`wa.me/message/RAVKCLUTZ6AGG1`). Nenhum desses três itens (endereço, e-mail, horário, qual link) entra no ar sem a Hellen escolher o que publica. Estão na lista de validação.

**Concorrência observada em Fraiburgo, sem esgotar o mercado.**

| Nome público | O que a listagem mostra | Leitura para o requisito |
| --- | --- | --- |
| Fran Thais Studio | Beleza; avaliações destacam maquiagem e atendimento. | Concorre em maquiagem. Não aparece como combo com ensaio. |
| Juliana Dalbosco Estúdio de Maquiagem | Estúdio de maquiagem. | Mesmo recorte: make, sem o trio num atendimento só. |
| Salão Beleza Pura | Salão de centro (cabelo, unha, sobrancelha, maquiagem de profissional da casa). Matéria da ACIAF. | É o tipo de salão do qual a Hellen pediu para se diferenciar. |
| Estúdio Inspire Fotografia e Maquiagem | Nome junta foto e maquiagem; categoria da ficha é fotógrafo; Rua Nadarci Brandt, 168. | Perguntar à Hellen se esse estúdio entrega o mesmo trio (make + cabelo + muitas fotos) ou só une duas palavras no nome. |
| Demais salões e estúdios (Studio Beauty, Studio Sil Cardoso, Chiquíssima, Gabrielly Zago Beauty, entre outros) | Beleza em geral. | Confirmam a frase dela: “há muitos profissionais na minha cidade da mesma área”. |

**Tendência que o sistema aproveita.** Em cidade pequena, a descoberta do studio acontece no Instagram. O site não substitui a rede: segura a informação que o story não guarda (preço, incluso, sinal, prazo das fotos) e abre o WhatsApp no ponto em que a cliente já escolheu. A visão escrita por ela — agenda cheia, equipe no futuro, equipamento profissional — aparece como visão, não como equipe já contratada.

## 5. Preferências de design (briefing)

Confirmadas por ela. Detalhe de implementação em `docs/DESIGN-SYSTEM.md`.

| Pedido dela | Decisão no sistema |
| --- | --- |
| Mensagem central: “Você vai ter dó de tirar a maquiagem.” | Título principal da primeira tela. |
| Fundo `#FDF8F5`, texto `#3B1C28`, apoio `#FED5CB`, CTA `#6D2C45` ou `#7A3450`, quente `#B86B58`. | Tokens de cor. Nenhuma cor fora dessa paleta. |
| Título em Perandory Condensed (ela só tem no Canva); subtítulo e corpo em Poppins; botão em Poppins SemiBold, texto claro. | Poppins no corpo e nos botões. Perandory se estiver instalada; no navegador, Bodoni Moda como substituta serifada. Substituta marcada como suposição de projeto até ela entregar o arquivo da fonte ou aceitar a Bodoni. |
| Transmitir confiança, exclusividade e profissionalismo. | Três pilares na tela “A experiência”. |
| Não parecer amadora, genérica ou mais um salão. Personalidade, cuidado, olhar artístico. | Sem fonte cursiva de salão. Registro de revista. Filtro “Artístico” no portfólio, sem pintar o site inteiro com esse tom. |
| Elegante e acolhedora ao mesmo tempo; recebe quem nunca se produziu. | Texto da persona e a pergunta de vergonha de foto no FAQ. |
| Marca que transforma momento comum em memória. | Título da tela “A Hellen”. |

## 6. Conteúdo pedido

| Bloco | Origem | Onde aparece |
| --- | --- | --- |
| Posicionamento, mensagem, frase da marca, persona, transformação, visão | Briefing | Início, A Hellen, rodapé |
| Diferencial: tudo no mesmo lugar; sai pronta; mais fotos que o mercado | Briefing | Tela O diferencial e FAQ |
| Serviços: maquiagem (social, noiva “Brilho do Sim”, madura, gestante, artística), cabelo (camadas leves, progressiva, escova, ondas; não faz corte curto), fotografia (ensaio, making of, gestante, aniversário) | Material já usado por ela + briefing | Serviços, portfólio |
| Combos R$ 300, R$ 370, R$ 420 e R$ 260; corte R$ 60; Quinta Especial R$ 150; mini bolo R$ 35; sinal R$ 30 com reagendamento em 60 dias; entrega em até 7 dias úteis | Material anterior da cliente | Valores, Como funciona, FAQ |
| Cursos Pro e automake, turma e valor no WhatsApp | Material anterior | Cursos |
| Prova social: clientes voltam, indicam e postam | Briefing (“o que você quer?”) | Divas, com link para o destaque FEEDBACKS do Instagram |
| Cidade Fraiburgo/SC, telefone, @hellenvarella.makeup | Material anterior; telefone confere com o cadastro público | Agenda e rodapé |
| Fotos reais do trabalho | Ela ainda não entregou os arquivos finais | Lugares marcados no portfólio e no hero |

Depoimento escrito de cliente dentro do site só entra com autorização da cliente. Até lá, a prova social é o Instagram.

## 7. Requisitos funcionais

| ID | Requisito | Prioridade | Origem |
| --- | --- | --- | --- |
| RF01 | A primeira tela exibe a mensagem central, a cidade e dois caminhos: agendar e ver a experiência. | Essencial | Briefing |
| RF02 | Uma tela explica o diferencial: maquiagem, cabelo e fotografia no mesmo atendimento. | Essencial | Briefing |
| RF03 | Uma tela apresenta os três ofícios com texto fiel ao que ela oferece e um convite por ofício. | Essencial | Briefing + oferta atual |
| RF04 | Uma tela lista combos e avulsos com preço, incluso e prazo, e abre o WhatsApp já citando o item. | Essencial | Oferta atual |
| RF05 | O portfólio separa as categorias social, noiva, gestante, cabelo, making of e artístico. | Essencial | Oferta + “olhar artístico” |
| RF06 | A tela da Hellen traz a frase da marca, a persona e a visão, sem afirmar que a equipe futura já existe. | Essencial | Briefing |
| RF07 | O fluxo de reserva é o WhatsApp (ou a ligação para o número publicado). Não há formulário nem cadastro. | Essencial | Canal real dela |
| RF08 | Cada botão de agendar monta uma mensagem coerente com o serviço, o combo ou o curso clicado. | Essencial | Brainstorm + canal real |
| RF09 | “Como funciona” explica roupa, referência, objeto de trabalho, aniversário, sinal, prazo das fotos e pontualidade. | Essencial | Regras já praticadas |
| RF10 | O FAQ responde, no mínimo: mesmo dia, vergonha de foto, sinal, prazo das fotos e corte curto. | Essencial | Briefing + regras |
| RF11 | Cursos Pro e automake aparecem com convite para saber a próxima turma no WhatsApp, sem data inventada. | Importante | Oferta atual |
| RF12 | A prova social aponta o Instagram (@hellenvarella.makeup e o destaque de feedbacks), sem depoimento inventado. | Importante | Briefing |
| RF13 | Menu leva às seções e, em tela estreita, abre e fecha sem esconder o conteúdo. | Essencial | Uso no celular |
| RF14 | Há página de agradecimento depois do contato e página de erro para endereço inexistente, na mesma identidade. | Desejável | Continuidade da visita |
| RF15 | “Montar meu combo” sugere o pacote a partir de maquiagem, cabelo e ajuda de look. | Desejável | Apoio à escolha |
| RF16 | Faixa de semanas livres/cheias só aparece quando a Hellen preencher datas reais. Não reserva sozinha. | Desejável | Suposição de projeto; o briefing só diz “agenda cheia” |
| RF17 | E-mail, endereço completo, horário e formas de pagamento só são publicados depois da confirmação dela. | Essencial | Lacuna do briefing |
| RF18 | Fotos do hero, do portfólio e da prévia de link entram nos lugares já reservados, com peles e idades diversas. | Essencial | Público do briefing; arquivos ainda faltam |

## 8. Requisitos não funcionais

| ID | Requisito |
| --- | --- |
| RNF01 | Funciona em celular e em computador. O uso principal esperado é o celular, porque a visita vem do Instagram. |
| RNF02 | HTML, CSS e JavaScript no navegador, sem cadastro de plataforma e sem mensalidade de hospedagem de aplicação. A publicação prevista é pasta estática. |
| RNF03 | Abre por clique no arquivo e também servido. Os scripts não dependem de módulo que quebre em `file://`. |
| RNF04 | Paleta, tipo e tom da seção 5. Contraste de texto e botão em nível AA ou acima. |
| RNF05 | Idioma português do Brasil. Textos curtos, na voz da marca (elegante e acolhedora). |
| RNF06 | Sem conta de visitante, sem pagamento, sem armazenamento de dado de cliente no site. |
| RNF07 | Link externo abre em nova aba com `rel="noopener"`. |
| RNF08 | Conteúdo que ainda não existe fica marcado, visível para a equipe, e não é preenchido com dado inventado. |
| RNF09 | Movimento de entrada na página respeita `prefers-reduced-motion`. |
| RNF10 | A Hellen, ou alguém a pedido dela, altera preço e texto em `data/*.json` sem reescrever o layout. |

## 9. Regras de negócio

| ID | Regra | Estado |
| --- | --- | --- |
| RN01 | Combo 1: maquiagem + 30 fotos, cerca de 2h30, R$ 300, entrega em até 7 dias úteis. | Confirmar antes de alterar |
| RN02 | Combo 2 (o mais pedido): maquiagem + cabelo (lavagem, escova, babyliss/cachos) + 45 fotos, cerca de 3h30, R$ 370. | Confirmar |
| RN03 | Combo 3: produção completa, 50 fotos, ajuda de look, cerca de 4 a 5 horas, R$ 420. | Confirmar |
| RN04 | Combo 4: só ensaio, 30 fotos, sem maquiagem nem cabelo, R$ 260. | Confirmar |
| RN05 | Corte feminino com escova, R$ 60, camadas leves. Não faz corte curto. | Confirmar |
| RN06 | Quinta Especial: maquiagem + ensaio, 10 fotos, R$ 150, sujeita à vaga da semana. | Confirmar |
| RN07 | Aniversário: mini bolo, R$ 35, com aviso antecipado. | Confirmar |
| RN08 | Reserva com sinal de R$ 30. Remarcação em até 60 dias com o mesmo sinal. | Confirmar |
| RN09 | Fotos: seleção, edição, álbum no celular, uma rodada de ajuste. | Confirmar |
| RN10 | Curso: turma e valor combinados no WhatsApp. O site não publica data de turma. | Confirmado como prática atual |
| RN11 | “Maquiadora desde 2013” e “fotógrafa desde 2021” só permanecem se ela confirmar. | Confirmar |

## 10. Casos de uso

Ator principal dos UC01–UC07: cliente visitante. A Hellen é ator secundário no recebimento da mensagem.

### UC01 — Entender se o studio é para ela

Pré-condição: abriu a vitrine. Fluxo: lê a mensagem central e o posicionamento; segue para o diferencial e para a experiência; encontra confiança, exclusividade e profissionalismo; se tiver vergonha de foto, acha isso dito com clareza. Pós-condição: sabe que o atendimento junta produção e fotografia e que quem nunca se produziu também é público.

### UC02 — Escolher um combo e chamar a Hellen

Pré-condição: quer preço antes de conversar. Fluxo: abre Valores; compara incluso e preço; aciona Agendar no combo. Alternativa: usa “Montar meu combo” e sai com o pacote sugerido. Pós-condição: o WhatsApp abre com o nome e o valor daquele combo. A data segue em aberto na conversa.

### UC03 — Ver um tipo de trabalho no portfólio

Pré-condição: quer noiva, gestante, social, cabelo, bastidor ou artístico. Fluxo: aciona o filtro; a grade mostra só aquela categoria. Pós-condição: a visitante vê o recorte. Enquanto as fotos reais não entram, o lugar de cada obra permanece visível e não finge ser foto.

### UC04 — Reservar pelo caminho geral

Pré-condição: já decidiu chamar, sem combo específico. Fluxo: usa o botão do topo, do início ou da agenda. Pós-condição: WhatsApp com a mensagem geral de agendamento, ou ligação para (49) 99829-3732.

### UC05 — Tirar uma dúvida objetiva

Pré-condição: dúvida de mesmo dia, vergonha, sinal, prazo ou corte. Fluxo: abre o item no FAQ. Alternativa: a dúvida é cidade atendida ou forma de pagamento — hoje a resposta ainda não pode ser inventada; o caminho é o WhatsApp. Pós-condição: ou a dúvida foi respondida, ou ela chama com a pergunta.

### UC06 — Saber de um curso

Fluxo: lê Curso Pro ou automake e aciona o convite. Pós-condição: mensagem pede a próxima turma, sem data no site.

### UC07 — Combinar referência antes do ensaio

Fluxo: em Como funciona, aciona o envio de referências. Pós-condição: mensagem pede para mandar roupa e make antes.

### UC08 — Hellen revisa o protótipo (ator: microempreendedora)

Pré-condição: recebeu o link do protótipo e o questionário. Fluxo: percorre as telas no celular; marca o que está fiel, o que falta e o que não pode ir ao ar; devolve preço, contato e fotos que autoriza. Pós-condição: a equipe atualiza o requisito e, na etapa III, o sistema. Este caso de uso é o critério de saída da Parte II.

## 11. Prioridade para a validação

**Entra na conversa com ela agora:** RF01–RF10, RF13, RF17, RF18, paleta, mensagem central, ausência de cara de salão, preços e o link de WhatsApp certo.

**Pode esperar o retorno dela:** cursos no ar, combo builder, página de obrigada, faixa de agenda, depoimentos dentro do site, analytics.

**Não propor nesta versão:** pagamento online, calendário que reserva sozinho, login, catálogo de produtos de revenda (o CNAE de cosméticos existe no cartão, ela não pediu loja).

## 12. Rastreio requisito → tela do protótipo

| Tela | Requisitos |
| --- | --- |
| Início | RF01, RNF01, RNF04 |
| O diferencial | RF02 |
| A experiência | Seção 5 (sentimentos) |
| Serviços | RF03, RF08 |
| Valores | RF04, RF08, RF15, RN01–RN08 |
| Portfólio | RF05, RF18 |
| A Hellen | RF06 |
| Cursos | RF11, RN10 |
| Divas | RF12 |
| Como funciona | RF09, RN07–RN09 |
| FAQ | RF10, RF17 |
| Agenda | RF07, RF16 |
| Menu | RF13 |
| Obrigada e 404 | RF14 |

## 13. Perguntas abertas para a Hellen

1. Os preços e os prazos da seção 9 continuam valendo?
2. Qual link de WhatsApp é o atual?
3. Publicar e-mail, endereço e horário? Se sim, Rua Suíça 117 ou 129, e qual grade de horas?
4. Atende só em Fraiburgo, a região, ou vai até a cliente?
5. Quais formas de pagamento?
6. “Desde 2013” e “desde 2021” podem ficar?
7. O destaque do Instagram se chama FEEDBACKS?
8. Ela autoriza quais fotos, e aceita Bodoni Moda no lugar da Perandory enquanto não houver arquivo da fonte?
9. O Estúdio Inspire (foto e maquiagem no nome) compete no mesmo combo ou é outro serviço?
10. Quer depoimento de cliente dentro do site, com autorização, ou só o Instagram?

## 14. Referências da pesquisa

- Briefing da cliente, arquivo `Meu briefing.pdf` (Hellen Varella).
- Cadastro público do CNPJ 33.687.461/0001-33. GuiaPJ. Disponível em: https://guiapj.com.br/consulta-cnpj/33687461000133 . Consulta em 13/10/2026.
- Ficha pública Studio Hellen Varella, Fraiburgo. Consulta em 13/10/2026.
- ACIAF. Atendimento diferenciado no Salão Beleza Pura. Disponível em: https://portal.aciaf.com.br/atendimento-diferenciado-no-salao-beleza-pura/ .
- PRESSMAN, Roger S.; MAXIM, Bruce R. *Engenharia de software: uma abordagem profissional*. 8. ed. Porto Alegre: AMGH, 2016. (elicitação, especificação e validação de requisitos.)
- SOMMERVILLE, Ian. *Engenharia de software*. 10. ed. São Paulo: Pearson, 2019. (requisitos de usuário e de sistema; casos de uso.)
- NAÇÕES UNIDAS. Objetivos de Desenvolvimento Sustentável. ODS 5 e ODS 8. Disponível em: https://brasil.un.org/pt-br/sdgs .
