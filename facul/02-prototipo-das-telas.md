# Protótipo das telas — Studio Hellen Varella

Parte II. Protótipo de validação com a microempreendedora, feito a partir da análise em `01-analise-de-requisitos.md`.

## Como abrir

O arquivo `prototipo/index.html` abre com dois cliques, sem instalar nada. É a peça para mostrar à Hellen no celular ou no computador: uma tela de cada vez, com a pergunta que a equipe precisa que ela responda.

A vitrine completa, já em HTML de verdade, está na raiz do projeto (`index.html`). Para percorrer com menu, filtros e WhatsApp:

```bash
node tools/serve.mjs
```

Endereço: `http://127.0.0.1:4173/`.

As pranchetas de direção visual (desktop, celular, marca e componentes) estão em `design/canvas/`. Elas guiaram a vitrine. O protótipo desta etapa é o que vai para o feedback dela.

## Fidelidade

- Conteúdo, cor, tipo e ordem das telas: altos, copiados do briefing e da oferta já praticada.
- Fotos: baixas de propósito. O lugar da imagem existe; a foto real só entra quando ela entregar o arquivo.
- Agenda automática, depoimento dentro do site, e-mail, endereço e horário: aparecem como pergunta, não como tela pronta.

## Telas

| # | Tela | O que a Hellen confere |
| --- | --- | --- |
| 1 | Início | A frase “Você vai ter dó de tirar a maquiagem.” é a primeira coisa que se lê. |
| 2 | O diferencial | “Tudo no mesmo lugar” está dito como ela escreveu. |
| 3 | A experiência | Confiança, exclusividade e profissionalismo, sem cara de salão. |
| 4 | Serviços | Make, cabelo e foto, com o aviso de que não faz corte curto. |
| 5 | Valores | Preço e incluso de cada combo. É aqui que ela corrige número. |
| 6 | Portfólio | Filtros social, noiva, gestante, cabelo, making of e artístico. |
| 7 | A Hellen | Persona e visão. A equipe futura não aparece como se já existisse. |
| 8 | Cursos | Pro e automake, sem data de turma inventada. |
| 9 | Divas | Prova social aponta o Instagram, não uma frase de cliente inventada. |
| 10 | Como funciona | Sinal, prazo, bolo, referências. |
| 11 | Perguntas | As cinco respostas fechadas e as duas que só ela pode fechar. |
| 12 | Agenda | O botão abre conversa no WhatsApp. Não há formulário. |
| 13 | Obrigada | Tela depois do contato, pedindo para marcar @hellenvarella.makeup. |

No protótipo, “Agendar” não chama o número verdadeiro: mostra a mensagem que o site real enviaria. Assim a validação pode acontecer sem disparar conversa no WhatsApp dela a cada clique.

## Critério para dar o protótipo como validado

A Hellen percorreu as 13 telas e devolveu o questionário (`04-questionario-validacao.md`), ou o equivalente em áudio ou conversa, dizendo o que permanece, o que muda e o que não pode ser publicado. Esse retorno é a evidência da Parte II e a entrada da etapa III.
