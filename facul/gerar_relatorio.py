# -*- coding: utf-8 -*-
"""Preenche o modelo de relatório de extensão da Parte II."""
from copy import deepcopy
from pathlib import Path

from docx import Document
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph

SRC = Path(r"C:\Users\User\Downloads\relatório de extensão (1).docx")
OUT = Path(__file__).resolve().parent / "relatorio-de-extensao.docx"
OUT_DOWNLOADS = Path(r"C:\Users\User\Downloads\relatório de extensão - preenchido.docx")


def set_text(paragraph, text):
    if paragraph.runs:
        paragraph.runs[0].text = text
        for run in paragraph.runs[1:]:
            run.text = ""
    else:
        paragraph.add_run(text)


def insert_after(paragraph, text):
    new_p = deepcopy(paragraph._p)
    paragraph._p.addnext(new_p)
    new_para = Paragraph(new_p, paragraph._parent)
    set_text(new_para, text)
    return new_para


def fill_next(doc, prefix, blocks):
    paras = doc.paragraphs
    for i, p in enumerate(paras):
        if p.text.strip().startswith(prefix):
            target = paras[i + 1]
            set_text(target, blocks[0])
            anchor = target
            for block in blocks[1:]:
                anchor = insert_after(anchor, block)
            return
    raise SystemExit(f"não achei: {prefix}")


def main():
    doc = Document(str(SRC))

    for p in doc.paragraphs:
        if p.text.strip().startswith("(   ) Escola Politécnica"):
            set_text(p, "( X ) Escola Politécnica")

    fill_next(
        doc,
        "2.",
        [
            "Vitrine web do Studio Hellen Varella: maquiagem, cabelo e fotografia no mesmo atendimento"
        ],
    )
    fill_next(
        doc,
        "3.",
        [
            "O projeto constrói o sistema web de uma microempreendedora individual de Fraiburgo/SC, a Hellen Luci Varella, dona de um studio que reúne maquiagem, cabelo e fotografia num único atendimento. A reserva permanece no WhatsApp, canal que ela já usa. O site guarda o que o Instagram não segura: a frase da marca, o diferencial, os serviços, os preços e o caminho para agendar.",
            "A Parte II registra a análise de requisitos, o protótipo simples das telas e as conversas de WhatsApp em que a Hellen aceitou o projeto, enviou o briefing, pediu um portfólio dos ensaios e liberou o uso das fotos do Instagram. O cronograma também cobre a etapa III. A publicação com as fotos escolhidas por ela e o relatório atualizado ficam para a etapa seguinte.",
        ],
    )
    fill_next(
        doc,
        "4.",
        [
            "A extensão universitária, tornada obrigatória pela Resolução CNE/CES nº 7, de 18 de dezembro de 2018, pede que o estudante aplique o conhecimento do curso numa demanda real da comunidade. A demanda aqui é de uma MEI da área de estética, ativa desde 21/05/2019 (CNPJ 33.687.461/0001-33), que apresenta o trabalho sobretudo pelo Instagram e fecha horário no WhatsApp.",
            "Ela mesma descreveu o problema de posicionamento: em Fraiburgo há muitos profissionais de beleza e muitos fotógrafos, e o que a distingue é entregar produção e ensaio no mesmo lugar. Sem uma página estável, preço, incluso e regra de reserva se perdem em conversa e em story.",
            "O projeto se liga à formação da Escola Politécnica em engenharia de requisitos e em desenvolvimento de sistema web. Os ODS usados como critério são o 8 (meta 8.3, formalização e crescimento de microempresas) e o 5 (meta 5.5, trabalho de uma mulher à frente do próprio negócio, com público majoritariamente de mulheres). A ferramenta foi desenhada para ela manter sem mensalidade de plataforma.",
        ],
    )
    fill_next(
        doc,
        "5.",
        [
            "Fraiburgo é cidade pequena do meio-oeste catarinense. Consulta pública em 13/10/2026 (GuiaPJ e fichas de estabelecimentos) mostra a Hellen como MEI de estética, telefone (49) 99829-3732, e dezenas de outras empresas ativas no mesmo CNAE no município. Salões e estúdios de maquiagem (entre eles Salão Beleza Pura, Fran Thais Studio e Juliana Dalbosco) convivem com fotógrafos. Há ainda uma ficha chamada Estúdio Inspire Fotografia e Maquiagem: fica como pergunta para ela, porque o nome junta dois ofícios e pode ou não ser o mesmo combo que ela oferece.",
            "A relação com a comunidade começou no WhatsApp do studio. A Hellen aceitou participar, se dispôs a passar dados do MEI, do trabalho e das fotos, e a assinar a carta de apresentação e tirar a selfie pedida pela disciplina. Enviou o briefing de quatro páginas, escrito por ela, com posicionamento, público, persona, paleta e o que a marca não pode parecer. Disse que o professor de marketing dela achou a iniciativa legal. Pediu um portfólio centrado nas fotos dos ensaios. Em 25/09/2026 confirmou que as fotos do Instagram têm uso de imagem liberado e que separaria um pouco de cada tipo de atendimento.",
            "A vitrine em construção usa esse texto. Endereço, e-mail, horário e o link curto de WhatsApp aparecem em cadastros públicos com divergências (Rua Suíça 117 no CNPJ e 129 numa ficha; dois links de WhatsApp). Nada disso será publicado até ela confirmar. A Parte III coloca no ar o que ela aprovar, com as fotos que ela separar.",
        ],
    )
    fill_next(
        doc,
        "6.",
        [
            "Objetivo geral: disponibilizar um sistema web que apresente o Studio Hellen Varella na identidade definida pela microempreendedora e encaminhe a reserva ao WhatsApp.",
            "Objetivos específicos: (1) levantar e classificar os requisitos de conteúdo, de função e de design a partir da demanda dela; (2) prototipar as telas e validá-las com a Hellen; (3) na etapa III, concluir o sistema com o que ela aprovar, inclusive fotos e dados de contato, e publicar em endereço estável; (4) avaliar se uma visitante entende o diferencial, o preço e como reservar, e se a Hellen se reconhece na marca.",
        ],
    )
    fill_next(
        doc,
        "7.",
        [
            "Beneficiária direta: Hellen Luci Varella, microempreendedora individual em Fraiburgo/SC, atividade de estética e outros cuidados com a beleza, com ensino e cabelo entre as atividades secundárias do cartão. Porte micro, Simples Nacional, capital social registrado de R$ 3.000,00. O sistema é a presença digital própria do negócio, sem custo de plataforma para ela.",
            "Beneficiário indireto: as clientes do studio. No briefing, são mulheres de todas as idades, de crianças a idosas, em maior número adolescentes e mães, que buscam um ambiente acolhedor e a praticidade de resolver cabelo, maquiagem e fotografia no mesmo atendimento. O projeto não coleta dado dessas clientes.",
        ],
    )
    fill_next(
        doc,
        "8.",
        [
            "A metodologia segue os objetivos e os dois ODS. A elicitação usou o briefing escrito pela Hellen, a conversa de WhatsApp com ela, a oferta que ela já pratica, a pesquisa pública de mercado em Fraiburgo e o brainstorm do que a página precisa resolver antes da conversa. A especificação está em requisitos funcionais, não funcionais, regras de negócio e casos de uso. A validação já começou nessa conversa: ela definiu o portfólio por tipo de atendimento e liberou as fotos do Instagram. O protótipo simples das oito telas, no Figma, é o material para ela percorrer e corrigir o que ainda estiver aberto, em especial preços e dados de contato.",
            "O desenvolvimento é incremental: HTML, CSS e JavaScript no navegador, conteúdo em arquivos de dados, sem login e sem formulário. Isso atende a meta 8.3 porque entrega um canal estável a uma MEI, com manutenção simples. Atende a meta 5.5 porque o trabalho é o de uma mulher à frente do studio e a comunicação evita o estereótipo de salão genérico que ela rejeitou. Cada encontro com ela entra no cronograma como atividade, não como etapa informal.",
            "Na etapa III a mesma metodologia continua: o retorno vira ajuste, teste no celular dela e atualização deste relatório.",
        ],
    )
    fill_next(
        doc,
        "9.",
        [
            "Sistema de página única, em português, responsivo, com uso principal no celular. Tecnologias: HTML, CSS e JavaScript, sem framework, sem banco de dados e sem servidor de aplicação. A publicação prevista é de pasta estática (GitHub Pages, Netlify ou Cloudflare Pages). Compatibilidade: navegadores atuais de celular e de computador; os scripts também funcionam ao abrir o arquivo direto.",
            "Arquitetura: folhas de estilo em camadas (tokens da paleta dela, base, layout, componentes, utilidades); comportamento em scripts separados (menu, portfólio, links de WhatsApp, montagem de combo). O conteúdo editável fica em JSON (serviços, estúdio, perguntas), para trocar preço sem reescrever a página. O protótipo desta etapa está no Figma (arquivo “Protótipo Studio Hellen Varella - Parte II”): oito telas simples, na mesma ordem e na mesma paleta do site já programado, com espaço de foto no lugar da imagem final.",
            "Integração de terceiros: links wa.me e tel: para o número (49) 99829-3732; Instagram e Threads do perfil @hellenvarella.makeup; famílias de fonte servidas pelo Google Fonts (Poppins e, como substituta web da Perandory Condensed, Bodoni Moda). Não há API de pagamento, de login nem de agenda. Segurança desta versão: nenhum dado de cliente é armazenado; link externo usa rel noopener; depoimento, e-mail e endereço só entram com autorização explícita. Requisitos detalhados, casos de uso e pendências estão em facul/01-analise-de-requisitos.md.",
        ],
    )
    fill_next(
        doc,
        "12. COMUNICAÇÃO",
        [
            "Com a microempreendedora: WhatsApp, que já é o canal do studio. Os prints do aceite, do envio do briefing e da liberação das fotos estão no documento da Parte II. O protótipo simples segue por esse mesmo canal para o retorno dela sobre as telas. Videochamada ou encontro presencial, se ocorrerem, também entram como evidência.",
            "Com a comunidade das clientes: o próprio site e o Instagram dela. Não há campanha paga nesta etapa. Depoimento de cliente só é republicado com autorização.",
            "Divulgação acadêmica: este relatório e a apresentação na disciplina. A versão pública do trabalho não precisa expor print com dado pessoal além do contato comercial que ela já divulga.",
        ],
    )
    fill_next(
        doc,
        "12. CRONOGRAMA",
        [
            "Situação em 24/10/2026. O prazo oficial é o da intranet. As linhas da etapa III estão previstas e este quadro pode ser atualizado nessa etapa, como o enunciado permite.",
        ],
    )
    fill_next(
        doc,
        "13.",
        [
            "Acadêmico: Luiz. Função nesta etapa: análise de requisitos, protótipo das telas e preenchimento do relatório. Carga horária: a lançar no Sistema da Univali.",
            "Demais integrantes do grupo: completar com nome, curso e função.",
            "Docente orientador: a informar no Sistema da Univali. Função: orientação e avaliação da extensão.",
        ],
    )
    fill_next(
        doc,
        "14.",
        [
            "Não há custo para a microempreendedora nem licença paga nesta etapa. O desenvolvimento usa navegador, HTML, CSS e JavaScript, e o WhatsApp que ela já possui. Domínio, se for contratado na etapa III, será decidido com ela e lançado à parte. Valores exigidos pela coordenação serão digitados no Sistema da Univali."
        ],
    )
    fill_next(
        doc,
        "15.",
        [
            "BRASIL. Resolução CNE/CES nº 7, de 18 de dezembro de 2018. Estabelece as diretrizes para a extensão na educação superior.",
            "NAÇÕES UNIDAS. Objetivos de Desenvolvimento Sustentável 5 e 8. Disponível em: https://brasil.un.org/pt-br/sdgs.",
            "PRESSMAN, Roger S.; MAXIM, Bruce R. Engenharia de software: uma abordagem profissional. 8. ed. Porto Alegre: AMGH, 2016.",
            "SOMMERVILLE, Ian. Engenharia de software. 10. ed. São Paulo: Pearson, 2019.",
            "VARELLA, Hellen. Meu briefing (documento da cliente, 4 páginas). Arquivo local Meu briefing.pdf.",
            "Cadastro público do CNPJ 33.687.461/0001-33. Consulta em 13 out. 2026. Disponível em: https://guiapj.com.br/consulta-cnpj/33687461000133.",
        ],
    )

    avaliacao = [
        (
            "Requisitos fiéis à demanda da Hellen",
            "Documento com requisitos classificados e pendências explícitas",
            "O site não anuncia serviço, preço ou equipe que ela não tenha confirmado",
            "Rastreio requisito–briefing e lista de perguntas abertas",
        ),
        (
            "Protótipo alinhado com ela",
            "Aceite, briefing, portfólio por tipo de atendimento e liberação das fotos do Instagram",
            "A microempreendedora se reconhece na marca e autoriza o que vai ao ar",
            "Prints de WhatsApp no documento da Parte II e arquivo do Figma",
        ),
        (
            "Visitante entende oferta e reserva",
            "Diferencial, preço e botão de WhatsApp encontrados sem ajuda",
            "Menos conversa só para perguntar preço e incluso",
            "Roteiro de teste no celular, com a Hellen, na etapa III",
        ),
        (
            "Presença digital própria no ar (etapa III)",
            "URL estável, com fotos e contatos que ela autorizar",
            "MEI com canal que não depende só de story",
            "Página acessível no celular e checklist de conteúdo",
        ),
    ]
    t0 = doc.tables[0]
    while len(t0.rows) < 1 + len(avaliacao):
        t0.add_row()
    for i, row in enumerate(avaliacao):
        for j, value in enumerate(row):
            t0.rows[i + 1].cells[j].text = value

    t1 = doc.tables[1]
    if len(t1.rows) < 3:
        t1.add_row()
    t1.rows[1].cells[0].text = "Studio Hellen Varella (Hellen Luci Varella, MEI)"
    t1.rows[1].cells[1].text = (
        "Fonte dos requisitos (briefing); validação do protótipo; "
        "confirmação de preços, contato e fotos; canal de comunicação com as clientes."
    )
    t1.rows[2].cells[0].text = "Univali — Escola Politécnica"
    t1.rows[2].cells[1].text = (
        "Orientação acadêmica, acompanhamento da extensão e avaliação do relatório."
    )

    semanas = [
        "set/2026",
        "25/09/2026",
        "out/2026",
        "out/2026",
        "out–nov/2026",
        "24/10/2026",
        "nov/2026",
        "nov/2026",
        "nov/2026",
        "nov–dez/2026",
        "dez/2026",
        "dez/2026",
    ]
    cron = [
        ("Primeiro contato e aceite da microempreendedora", "II", [0]),
        ("Briefing, portfólio e liberação das fotos", "II", [1]),
        ("Análise de requisitos e pesquisa em Fraiburgo", "II", [2]),
        ("Protótipo simples das oito telas", "II", [3]),
        ("Retorno dela sobre preços, contato e as telas", "II", [4]),
        ("Relatório de extensão desta etapa", "II", [5]),
        ("Ajustar o site com o que ela aprovar", "III", [6]),
        ("Colocar as fotos que ela separar", "III", [7]),
        ("Teste no celular dela (menu, preço, WhatsApp)", "III", [8]),
        ("Publicação em endereço estável", "III", [9]),
        ("Repasse de como alterar preço e texto", "III", [10]),
        ("Avaliação de resultados e relatório atualizado", "III", [11]),
    ]
    t2 = doc.tables[2]
    # O modelo tem 5 colunas (atividade + 4 semanas de maio).
    # Reconstruímos o quadro em linhas: atividade | etapa | semanas marcadas,
    # usando as 5 colunas existentes de forma legível em retrato.
    header = ["Atividade", "Etapa", "Quando", "Situação em 24/10/2026", "Produto"]
    for j, value in enumerate(header):
        t2.rows[0].cells[j].text = value
    situacao = {
        0: "Feito",
        1: "Feito",
        2: "Feito nesta entrega",
        3: "Feito nesta entrega",
        4: "Em aberto: preços, contato e percurso das telas",
        5: "Esta versão",
    }
    produto = [
        "Prints do WhatsApp",
        "Briefing e prints de 25/09/2026",
        "Documento da Parte II",
        "Arquivo no Figma",
        "Retorno no WhatsApp",
        "relatorio-de-extensao.pdf",
        "Vitrine ajustada",
        "Checklist de conteúdo",
        "Roteiro de teste respondido",
        "URL no ar",
        "Nota curta de atualização",
        "Relatório da etapa III",
    ]
    while len(t2.rows) < 1 + len(cron):
        t2.add_row()
    for i, (nome, etapa, idxs) in enumerate(cron):
        marcas = ", ".join(semanas[k] for k in idxs)
        estado = situacao.get(i, "Prevista")
        t2.rows[i + 1].cells[0].text = nome
        t2.rows[i + 1].cells[1].text = etapa
        t2.rows[i + 1].cells[2].text = marcas
        t2.rows[i + 1].cells[3].text = estado
        t2.rows[i + 1].cells[4].text = produto[i]

    doc.save(str(OUT))
    doc.save(str(OUT_DOWNLOADS))
    print(OUT)
    print(OUT_DOWNLOADS)


if __name__ == "__main__":
    main()
