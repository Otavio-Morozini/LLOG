# -*- coding: utf-8 -*-
"""Documento da Parte II: requisitos, protótipo e evidências."""
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

BASE = Path(__file__).resolve().parent
ANEXOS = BASE / "anexos"
OUT = BASE / "Parte-II-requisitos-prototipo-evidencias.docx"
PLUM = RGBColor(0x3B, 0x1C, 0x28)
INK = RGBColor(0x2A, 0x18, 0x1C)


def font(run, size=11, bold=False, italic=False, color=INK):
    run.font.name = "Calibri"
    run._element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = color


def add_p(doc, text, size=11, bold=False, italic=False, center=False, space=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(space)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.line_spacing = 1.08
    if center:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    font(p.add_run(text), size, bold, italic)
    return p


def add_h(doc, text, level=1):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(16 if level == 1 else 12)
    p.paragraph_format.space_after = Pt(4)
    font(p.add_run(text), 16 if level == 1 else 13, True, color=PLUM)
    return p


def add_bullets(doc, items):
    for item in items:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(0.75)
        p.paragraph_format.space_after = Pt(2)
        font(p.add_run("• " + item), 11)


def set_cell(cell, text, size=9, bold=False):
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    font(p.add_run(text), size, bold, color=PLUM if bold else INK)


def add_table(doc, headers, rows, widths=None):
    table = doc.add_table(rows=1 + len(rows), cols=len(headers))
    table.style = "Table Grid"
    for j, h in enumerate(headers):
        set_cell(table.rows[0].cells[j], h, 9, True)
    for i, row in enumerate(rows):
        for j, value in enumerate(row):
            set_cell(table.rows[i + 1].cells[j], value, 9)
    if widths:
        for row in table.rows:
            for j, w in enumerate(widths):
                row.cells[j].width = Cm(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    return table


def add_picture(doc, name, width, caption):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(8)
    p.add_run().add_picture(str(ANEXOS / name), width=Cm(width))
    c = doc.add_paragraph()
    c.alignment = WD_ALIGN_PARAGRAPH.CENTER
    c.paragraph_format.space_after = Pt(10)
    font(c.add_run(caption), 9, italic=True, color=PLUM)


def add_pair(doc, left, right):
    table = doc.add_table(rows=2, cols=2)
    for i, (name, caption) in enumerate((left, right)):
        cell = table.rows[0].cells[i]
        cell.text = ""
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.add_run().add_picture(str(ANEXOS / name), width=Cm(7.1))
        cap = table.rows[1].cells[i].paragraphs[0]
        cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        font(cap.add_run(caption), 9, italic=True, color=PLUM)
    doc.add_paragraph().paragraph_format.space_after = Pt(6)


def page_number(paragraph):
    run = paragraph.add_run()
    font(run, 9, color=PLUM)
    begin = OxmlElement("w:fldChar")
    begin.set(qn("w:fldCharType"), "begin")
    instr = OxmlElement("w:instrText")
    instr.set(qn("xml:space"), "preserve")
    instr.text = " PAGE "
    end = OxmlElement("w:fldChar")
    end.set(qn("w:fldCharType"), "end")
    run._r.append(begin)
    run._r.append(instr)
    run._r.append(end)


def main():
    doc = Document()
    section = doc.sections[0]
    section.top_margin = Cm(1.8)
    section.bottom_margin = Cm(1.6)
    section.left_margin = Cm(1.8)
    section.right_margin = Cm(1.8)
    section.page_width = Cm(21.0)
    section.page_height = Cm(29.7)
    footer = section.footer.paragraphs[0]
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    font(footer.add_run("Parte II · Studio Hellen Varella · "), 9, color=PLUM)
    page_number(footer)

    add_p(doc, "UNIVERSIDADE DO VALE DO ITAJAÍ", 12, True, center=True, space=2)
    add_p(doc, "Escola Politécnica", 12, center=True, space=2)
    add_p(doc, "Projeto de extensão — Parte II", 12, center=True, space=14)
    add_p(doc, "Sistema web do Studio Hellen Varella", 20, True, center=True, space=6)
    add_p(
        doc,
        "Análise de requisitos, protótipo das telas e evidências da participação da microempreendedora",
        12,
        center=True,
        space=14,
    )
    add_p(doc, "Microempreendedora: Hellen Luci Varella", 11, center=True, space=2)
    add_p(doc, "Studio de beleza e fotografia · Fraiburgo/SC", 11, center=True, space=2)
    add_p(doc, "Outubro de 2026", 11, center=True, space=8)
    add_p(
        doc,
        "Protótipo: https://www.figma.com/design/op7PRKoYWr2s3cPM5DJcXm",
        10,
        center=True,
        space=0,
    )
    doc.add_page_break()

    add_h(doc, "1. O que esta entrega cobre")
    add_p(
        doc,
        "Este documento responde aos três primeiros itens da Parte II. O relatório de extensão, com o cronograma da etapa II e da etapa III, vai em arquivo separado, no modelo da universidade.",
    )
    add_bullets(
        doc,
        [
            "Análise dos requisitos do sistema web, a partir do que a microempreendedora pediu.",
            "Protótipo simples das telas, no Figma, parecido com o site já programado e genérico de propósito.",
            "Evidências da participação dela: os prints de WhatsApp enviados para esta entrega.",
        ],
    )
    add_p(
        doc,
        "A Hellen Luci Varella é microempreendedora individual em Fraiburgo/SC, MEI ativa desde 21/05/2019, CNPJ 33.687.461/0001-33, CNAE principal 9602-5/02. O studio reúne maquiagem, cabelo e fotografia no mesmo atendimento. A reserva continua no WhatsApp. O site guarda o que o story não guarda: a frase da marca, o diferencial, os serviços, o preço e o caminho para agendar.",
    )

    add_h(doc, "2. Análise dos requisitos")
    add_h(doc, "2.1 Partes interessadas", 2)
    add_table(
        doc,
        ["Parte", "Interesse"],
        [
            ["Hellen Luci Varella, dona do studio", "Ser reconhecida pelo atendimento, manter a agenda e ver a cliente voltar, indicar e postar o trabalho."],
            ["Cliente do studio", "Entender o que está incluso, o preço e como reservar, num ambiente acolhedor."],
            ["Quem chega pelo Instagram", "Encontrar a mesma mensagem da marca e abrir o WhatsApp com o serviço já nomeado."],
            ["Equipe da extensão", "Entregar um sistema fiel à demanda dela e registrar a participação."],
        ],
        [5.2, 12.2],
    )
    add_p(
        doc,
        "O público que ela descreveu no briefing: mulheres de todas as idades, de crianças a idosas. A maior parte são adolescentes e mães. Procuram um lugar acolhedor, “como se estivessem em casa”, e escolhem a Hellen porque encontram cabelo, maquiagem e fotografia no mesmo lugar.",
    )

    add_h(doc, "2.2 Técnicas usadas", 2)
    add_table(
        doc,
        ["Técnica", "O que foi feito", "O que saiu daí"],
        [
            ["Análise de documento", "Leitura do briefing de 4 páginas escrito por ela e enviado no WhatsApp.", "Posicionamento, público, persona, paleta, o que a marca não pode parecer."],
            ["Entrevista por conversa", "WhatsApp: aceite, ideias dela e retorno sobre fotos.", "Portfólio dos ensaios, uma foto por tipo de atendimento, uso de imagem liberado."],
            ["Análise de artefato", "Preços, combos, sinal, telefone e @ que ela já usa.", "Regras de negócio. Preço segue pendente de confirmação antes de mudar."],
            ["Pesquisa de área", "Cadastros e listagens públicas de estética e fotografia em Fraiburgo, em 13/10/2026.", "Diagnóstico da seção 2.4. Divergência de cadastro vira pergunta, não fato."],
            ["Brainstorm", "O que a página precisa resolver antes do WhatsApp.", "Sem login, sem formulário e sem pagamento no site."],
            ["Prototipação", "Oito telas simples no Figma, na paleta e na ordem do site já programado.", "Material para ela corrigir o que ainda está aberto."],
        ],
        [3.6, 6.6, 7.2],
    )

    add_h(doc, "2.3 Problema que o sistema resolve", 2)
    add_p(
        doc,
        "A Hellen atende por Instagram e WhatsApp. Preço, o que entra em cada combo e a regra de reserva se perdem em conversa e em story. Ela descreveu o mercado local assim: há muitos profissionais da mesma área e bastante fotógrafos, e o que a diferencia é entregar tudo no mesmo lugar. A cliente sai pronta e recebe mais fotos do que o mercado costuma entregar.",
    )
    add_p(
        doc,
        "O sistema organiza essa oferta num endereço estável, na identidade que ela definiu, e devolve a conversa para o WhatsApp com a mensagem já preenchida. Ficou de fora porque ela não pediu e porque aumentaria o trabalho de manter o site: loja virtual, login, pagamento, agendamento automático, blog e área administrativa. A mensagem automática do WhatsApp dela (“valores estão no catálogo”) mostra o canal que já existe. O site não vira catálogo de revenda.",
    )

    add_h(doc, "2.4 Pesquisa de área e concorrência", 2)
    add_p(
        doc,
        "Consulta em 13/10/2026. O telefone público (49) 99829-3732 é o mesmo já usado no site. Uma listagem do município aponta 64 empresas ativas em Fraiburgo com o CNAE principal dela: o mercado local de beleza é concorrido, como ela mesma escreveu. Capital social registrado de R$ 3.000,00. Optante pelo Simples Nacional.",
    )
    add_p(
        doc,
        "A ficha pública do studio mostra nota 5,0 em cinco avaliações e um horário de listagem (segunda a sexta à tarde, sábado até a noite, domingo fechado). O endereço do CNPJ é Rua Suíça, 117, Das Nações. A ficha do studio mostra Rua Suíça, 129. O e-mail do cadastro é hellevarella@outlook.com. O link curto de WhatsApp dessa ficha é outro, diferente do que está no site. Endereço, e-mail, horário e qual link publicar só entram depois que ela escolher.",
    )
    add_table(
        doc,
        ["Nome público", "O que a listagem mostra", "Leitura para o requisito"],
        [
            ["Fran Thais Studio", "Beleza; avaliações citam maquiagem e atendimento.", "Concorre em maquiagem, sem o combo com ensaio."],
            ["Juliana Dalbosco Estúdio de Maquiagem", "Estúdio de maquiagem.", "Make, sem o trio num atendimento só."],
            ["Salão Beleza Pura", "Salão de centro: cabelo, unha, sobrancelha, maquiagem.", "É o tipo de salão do qual ela pediu para se diferenciar."],
            ["Estúdio Inspire Fotografia e Maquiagem", "O nome junta foto e maquiagem. Categoria da ficha: fotógrafo.", "Perguntar se entrega o mesmo trio ou só une as duas palavras."],
            ["Demais salões e estúdios da cidade", "Beleza em geral.", "Confirmam a frase dela: há muitos profissionais da mesma área."],
        ],
        [4.6, 6.2, 6.6],
    )
    add_p(
        doc,
        "Em cidade pequena, a descoberta do studio acontece no Instagram. O site não substitui a rede. Ele segura preço, incluso, sinal e prazo das fotos, e abre o WhatsApp no ponto em que a cliente já escolheu. A visão que ela escreveu — agenda cheia, equipe no futuro, equipamento profissional — aparece como visão. O site não afirma que a equipe já existe.",
    )

    add_h(doc, "2.5 Preferências de design", 2)
    add_p(doc, "Confirmadas por ela no briefing. O protótipo usa a mesma paleta, em versão simples.")
    add_table(
        doc,
        ["Pedido dela", "Decisão"],
        [
            ["Mensagem central: “Você vai ter dó de tirar a maquiagem.”", "Título da primeira tela."],
            ["Fundo #FDF8F5, texto #3B1C28, apoio #FED5CB, botão #6D2C45.", "Cores do protótipo e do site. Nenhuma cor fora dessa paleta."],
            ["Título em Perandory Condensed, que ela só tem no Canva. Corpo e botão em Poppins.", "No protótipo, serifada genérica no título e sans no texto. A fonte final espera o arquivo dela ou o aceite da substituta."],
            ["Confiança, exclusividade e profissionalismo.", "Três blocos na tela Experiência."],
            ["Não parecer amadora, genérica ou mais um salão.", "Sem letra cursiva de salão. O tom artístico fica no filtro do portfólio."],
            ["Elegante e acolhedora ao mesmo tempo.", "O texto recebe quem nunca se produziu."],
            ["A marca transforma momento comum em memória.", "Título da tela A Hellen."],
        ],
        [8.4, 9.0],
    )

    add_h(doc, "2.6 Conteúdo a incluir", 2)
    add_table(
        doc,
        ["Bloco", "Origem", "Onde aparece"],
        [
            ["Posicionamento, mensagem, persona, visão", "Briefing", "Início e A Hellen"],
            ["Tudo no mesmo lugar; sai pronta; mais fotos que o mercado", "Briefing", "Diferencial"],
            ["Maquiagem, cabelo e fotografia, com os tipos de atendimento", "Briefing e oferta atual", "Serviços e portfólio"],
            ["Combos, corte, Quinta Especial, mini bolo, sinal e prazo", "Oferta que ela já pratica", "Valores. Números a confirmar."],
            ["Portfólio de fotos dos ensaios, um pouco de cada processo", "WhatsApp, pedido dela", "Portfólio"],
            ["Fotos do Instagram, com uso de imagem liberado", "WhatsApp, 25/09/2026", "Portfólio, quando ela separar os arquivos"],
            ["Cursos Pro e automake, turma no WhatsApp", "Oferta atual", "Site programado. Fora do protótipo simples."],
            ["Cidade, telefone e @hellenvarella.makeup", "Material já usado; telefone confere com o cadastro", "Contato e rodapé"],
        ],
        [6.2, 5.4, 5.8],
    )

    add_h(doc, "2.7 Requisitos funcionais", 2)
    add_table(
        doc,
        ["ID", "Requisito", "Prioridade"],
        [
            ["RF01", "A primeira tela mostra a mensagem central, a cidade e dois caminhos: agendar e ver a experiência.", "Essencial"],
            ["RF02", "Uma tela explica o diferencial: maquiagem, cabelo e fotografia no mesmo atendimento.", "Essencial"],
            ["RF03", "Uma tela apresenta os três ofícios e um convite por ofício. O aviso de corte curto aparece no cabelo.", "Essencial"],
            ["RF04", "Uma tela lista combos com preço e incluso, e abre o WhatsApp citando o item.", "Essencial"],
            ["RF05", "O portfólio separa social, noiva, gestante, cabelo, making of e artístico.", "Essencial"],
            ["RF06", "A tela da Hellen traz a frase da marca e a visão, sem tratar a equipe futura como se já existisse.", "Essencial"],
            ["RF07", "A reserva é o WhatsApp ou a ligação. Não há formulário nem cadastro.", "Essencial"],
            ["RF08", "Cada botão de agendar monta uma mensagem coerente com o serviço ou o combo.", "Essencial"],
            ["RF09", "“Como funciona” explica roupa, referência, aniversário, sinal, prazo das fotos e pontualidade.", "Essencial"],
            ["RF10", "O FAQ responde, no mínimo: mesmo dia, vergonha de foto, sinal, prazo das fotos e corte curto.", "Essencial"],
            ["RF11", "Cursos Pro e automake convidam a saber a próxima turma no WhatsApp, sem data inventada.", "Importante"],
            ["RF12", "A prova social aponta o Instagram, sem depoimento inventado.", "Importante"],
            ["RF13", "O menu leva às seções e, no celular, abre e fecha sem esconder o conteúdo.", "Essencial"],
            ["RF14", "Há página de agradecimento e página de erro, na mesma identidade.", "Desejável"],
            ["RF15", "“Montar meu combo” sugere o pacote a partir de maquiagem, cabelo e ajuda de look.", "Desejável"],
            ["RF16", "Faixa de agenda só aparece com datas reais preenchidas por ela. Não reserva sozinha.", "Desejável"],
            ["RF17", "E-mail, endereço, horário e pagamento só são publicados depois da confirmação dela.", "Essencial"],
            ["RF18", "As fotos do hero e do portfólio entram nos lugares já marcados, com peles e idades diversas.", "Essencial"],
        ],
        [1.6, 13.4, 2.4],
    )

    add_h(doc, "2.8 Requisitos não funcionais", 2)
    add_table(
        doc,
        ["ID", "Requisito"],
        [
            ["RNF01", "Funciona no celular e no computador. O uso principal é o celular, porque a visita vem do Instagram."],
            ["RNF02", "HTML, CSS e JavaScript no navegador. Publicação prevista como pasta estática, sem mensalidade de plataforma."],
            ["RNF03", "Abre por clique no arquivo e também servido. Os scripts não dependem de módulo que quebre em file://."],
            ["RNF04", "Paleta e tom da seção 2.5. Contraste de texto e botão em nível AA ou acima."],
            ["RNF05", "Português do Brasil. Texto curto, elegante e acolhedor."],
            ["RNF06", "Sem conta de visitante, sem pagamento e sem armazenamento de dado de cliente no site."],
            ["RNF07", "Link externo abre em nova aba com rel noopener."],
            ["RNF08", "O que ainda não existe fica marcado. Não é preenchido com dado inventado."],
            ["RNF09", "Movimento de entrada na página respeita prefers-reduced-motion."],
            ["RNF10", "Preço e texto podem ser alterados em arquivo de dados, sem reescrever o layout."],
        ],
        [1.8, 15.6],
    )

    add_h(doc, "2.9 Regras de negócio", 2)
    add_p(doc, "Estes números vêm da oferta que ela já pratica. A conversa anexada não os confirmou de novo. Permanecem até ela dizer que mudaram.")
    add_table(
        doc,
        ["ID", "Regra", "Estado"],
        [
            ["RN01", "Combo 1: maquiagem + 30 fotos, cerca de 2h30, R$ 300, entrega em até 7 dias úteis.", "A confirmar"],
            ["RN02", "Combo 2, o mais pedido: maquiagem + cabelo + 45 fotos, cerca de 3h30, R$ 370.", "A confirmar"],
            ["RN03", "Combo 3: produção completa, 50 fotos, ajuda de look, cerca de 4 a 5 horas, R$ 420.", "A confirmar"],
            ["RN04", "Combo 4: só ensaio, 30 fotos, sem maquiagem nem cabelo, R$ 260.", "A confirmar"],
            ["RN05", "Corte feminino com escova, R$ 60, camadas leves. Não faz corte curto.", "A confirmar"],
            ["RN06", "Quinta Especial: maquiagem + ensaio, 10 fotos, R$ 150, sujeita à vaga.", "A confirmar"],
            ["RN07", "Aniversário: mini bolo, R$ 35, com aviso antecipado.", "A confirmar"],
            ["RN08", "Reserva com sinal de R$ 30. Remarcação em até 60 dias com o mesmo sinal.", "A confirmar"],
            ["RN09", "Fotos: seleção, edição, álbum no celular, uma rodada de ajuste.", "A confirmar"],
            ["RN10", "Curso: turma e valor combinados no WhatsApp. O site não publica data de turma.", "Prática atual"],
            ["RN11", "As fotos do Instagram podem ser usadas. Ela vai separar um pouco de cada tipo.", "Confirmado em 25/09/2026"],
        ],
        [1.6, 12.4, 3.4],
    )

    add_h(doc, "2.10 Casos de uso", 2)
    add_p(doc, "Ator principal: a cliente visitante. A Hellen recebe a mensagem. O caso UC08 é dela, na validação.")
    add_table(
        doc,
        ["Caso", "Fluxo em uma linha", "Resultado"],
        [
            ["UC01 Entender se o studio é para ela", "Lê a frase, o diferencial e a experiência.", "Sabe que produção e foto acontecem juntas, inclusive para quem nunca se produziu."],
            ["UC02 Escolher um combo", "Abre Valores e aciona Agendar.", "O WhatsApp abre com o nome e o valor daquele combo."],
            ["UC03 Ver um tipo de trabalho", "Aciona o filtro do portfólio.", "A grade mostra só aquela categoria."],
            ["UC04 Reservar sem combo", "Usa o botão geral.", "Mensagem geral de agendamento, ou ligação."],
            ["UC05 Tirar uma dúvida", "Abre o FAQ. Se a resposta ainda não pode ser publicada, chama no WhatsApp.", "A dúvida foi respondida ou virou pergunta na conversa."],
            ["UC06 Saber de um curso", "Lê o curso e pede a próxima turma.", "A mensagem não traz data inventada."],
            ["UC07 Mandar referência", "Em Como funciona, pede para enviar roupa e make antes.", "A conversa já nasce com esse pedido."],
            ["UC08 Hellen revisa as telas", "Percorre o protótipo e diz o que fica, o que muda e o que não pode ir ao ar.", "A equipe atualiza o requisito. É a entrada da etapa III."],
        ],
        [4.2, 6.4, 6.8],
    )

    add_h(doc, "2.11 Rastreio e o que ainda está aberto", 2)
    add_table(
        doc,
        ["Tela do protótipo", "Requisitos"],
        [
            ["01 Início", "RF01"],
            ["02 Diferencial", "RF02"],
            ["03 Serviços", "RF03, RF08"],
            ["04 Valores", "RF04, RN01 a RN04"],
            ["05 Portfólio", "RF05, RF18, RN11"],
            ["06 Experiência", "Confiança, exclusividade e profissionalismo"],
            ["07 A Hellen", "RF06"],
            ["08 Contato", "RF07"],
        ],
        [6, 11.4],
    )
    add_p(doc, "Como funciona, FAQ, cursos, prova social, página de obrigada e menu de celular estão especificados acima e já existem na página programada. Não foram redesenhados neste protótipo, que ficou nas oito telas de apresentação e reserva.")
    add_p(doc, "Perguntas que só ela fecha:")
    add_bullets(
        doc,
        [
            "Os preços e os prazos da seção 2.9 continuam valendo?",
            "Qual link de WhatsApp é o atual?",
            "Publicar e-mail, endereço e horário? Se sim, Rua Suíça 117 ou 129, e qual grade?",
            "Atende só em Fraiburgo, a região, ou vai até a cliente?",
            "Quais formas de pagamento podem ser escritas?",
            "“Maquiadora desde 2013” e “fotógrafa desde 2021” podem ficar?",
            "O destaque do Instagram com a opinião das clientes se chama FEEDBACKS?",
            "Enquanto a Perandory não estiver em arquivo para a web, o título pode usar uma serifada de revista?",
            "O Estúdio Inspire compete no mesmo combo?",
            "Quer depoimento de cliente dentro do site, com autorização, ou só o Instagram?",
        ],
    )

    add_h(doc, "3. Protótipo das telas")
    add_p(
        doc,
        "O protótipo está no Figma, no arquivo “Protótipo Studio Hellen Varella - Parte II”: https://www.figma.com/design/op7PRKoYWr2s3cPM5DJcXm . São oito telas de celular, uma ao lado da outra, na página “Protótipo simples”.",
    )
    add_p(
        doc,
        "Ele repete a ordem, os nomes e a paleta do site já programado, e para por aí. O desenho é simples de propósito: barra com o nome e o botão Agendar, um título, um texto curto, cartões e um retângulo rosa no lugar da foto. Não há foto de cliente neste protótipo. O lugar da imagem está marcado para receber, na etapa III, os arquivos que ela separar do Instagram.",
    )
    add_p(
        doc,
        "O site programado continua sendo a vitrine completa, com menu, filtros, combos e links de WhatsApp. O Figma é a peça para mostrar a ela e ouvir o que muda, sem a densidade da página pronta.",
    )

    add_pair(
        doc,
        ("01-inicio.png", "Figura 1. Início. A frase do briefing é a primeira coisa que se lê."),
        ("02-diferencial.png", "Figura 2. Diferencial. Make, cabelo e foto no mesmo dia."),
    )
    add_pair(
        doc,
        ("03-servicos.png", "Figura 3. Serviços. Três ofícios, com o aviso de corte curto."),
        ("04-valores.png", "Figura 4. Valores. Preço da oferta atual, ainda sujeito à confirmação."),
    )
    add_pair(
        doc,
        ("05-portfolio.png", "Figura 5. Portfólio. Um filtro por tipo de atendimento, como ela pediu."),
        ("06-experiencia.png", "Figura 6. Experiência. Confiança, exclusividade e profissionalismo."),
    )
    add_pair(
        doc,
        ("07-hellen.png", "Figura 7. A Hellen. Persona e visão, sem equipe fictícia."),
        ("08-contato.png", "Figura 8. Contato. A reserva abre o WhatsApp. Não há formulário."),
    )
    add_p(doc, "O que cada tela pede que ela confira:")
    add_bullets(
        doc,
        [
            "Início: a frase “Você vai ter dó de tirar a maquiagem.” continua sendo a frase do site.",
            "Diferencial: “tudo no mesmo lugar” está do jeito que ela falaria.",
            "Serviços: os três ofícios e a frase “não trabalho com cortes curtos”.",
            "Valores: se R$ 300, R$ 370, R$ 420 e R$ 260 ainda são os números.",
            "Portfólio: os seis filtros cobrem o que ela quer mostrar, inclusive o processo.",
            "Experiência: as cores passam confiança, exclusividade e profissionalismo.",
            "A Hellen: a visão de equipe futura não parece uma equipe já contratada.",
            "Contato: o botão certo é conversa no WhatsApp, não um formulário.",
        ],
    )

    add_h(doc, "4. Evidências da participação da microempreendedora")
    add_p(
        doc,
        "O canal é o WhatsApp do studio, o mesmo que ela usa com as clientes. As figuras abaixo são os prints enviados para esta entrega. O balão verde é a equipe. O balão cinza é a Hellen. O que cada print prova está escrito antes da imagem, para a leitura não depender de decifrar a tela.",
    )

    add_h(doc, "4.1 Aceite do projeto", 2)
    add_p(
        doc,
        "A equipe chamou a Hellen, se apresentou como Elta quando a mensagem automática pediu o nome, e explicou o projeto de extensão: entrar em contato com uma MEI e criar um site seguindo os pedidos, as ideias e os desejos que fossem apresentados. Deixou claro que, no final, publicar o site é escolha dela, e que a entrega é deixar tudo pronto. Pediu a carta de apresentação assinada e uma selfie, para registrar que a participação não foi coagida.",
    )
    add_p(
        doc,
        "A Hellen respondeu: “Claro que topo. Pode fazer o projeto comigo sim. O que precisar de informação do MEI, do meu trabalho, fotos e tal, só me pedir que te passo. A carta e a selfie eu faço também.” A equipe fechou o combinado.",
    )
    add_picture(
        doc,
        "whatsapp-01-aceite.png",
        14.5,
        "Figura 9. WhatsApp. Aceite da Hellen, com oferta de dados do MEI, fotos, carta e selfie.",
    )

    add_h(doc, "4.2 Briefing e o pedido de portfólio", 2)
    add_p(
        doc,
        "Na continuação, a equipe avisou que mandaria as atualizações e veria o que ela achava, e que precisava entregar uma parte inicial até o dia 14, com o trabalho seguindo até o fim do semestre. A Hellen disse que por ela estava bem, e que tinha falado com o professor de marketing dela, que achou a iniciativa legal. Disse também que tinha um briefing e que enviaria se precisassem. A equipe pediu que, se ela já tivesse ideias e pedidos com certeza de como o site deve ser, ela os mandasse.",
    )
    add_p(
        doc,
        "Ela enviou o arquivo “Meu briefing.pdf”, de 4 páginas. Em seguida escreveu: “Pensei em algo como portfólio, principalmente na parte de fotos. Os ensaios.” A equipe respondeu que a marca já tinha uma personalidade pronta. Há ainda, na conversa, o recado dela para ver com a Ana ou combinar todos juntos. A equipe acusou o bom dia.",
    )
    add_picture(
        doc,
        "whatsapp-02-briefing.png",
        14.5,
        "Figura 10. WhatsApp. Envio do briefing e pedido de um portfólio das fotos dos ensaios.",
    )

    add_h(doc, "4.3 Fotos e uso de imagem", 2)
    add_p(
        doc,
        "A Hellen pediu dicas de que tipo de foto ficaria legal. A equipe respondeu com base no briefing: fotos para cada tipo de atendimento, mostrando o portfólio de todo o processo, e perguntou se havia liberdade para usar foto de cliente, inclusive as que já estão no Instagram.",
    )
    add_p(
        doc,
        "Em 25/09/2026 ela respondeu: “Ah então blz. Vou procurar aqui um pouco de cada.” E, sobre as fotos: “As que estão no meu Instagram. Todas liberaram uso de imagem.”",
    )
    add_picture(
        doc,
        "whatsapp-03-fotos.png",
        14.5,
        "Figura 11. WhatsApp, 25/09/2026. Um pouco de cada atendimento, com uso de imagem liberado.",
    )

    add_h(doc, "4.4 O que esses prints fecham, e o que não fecham", 2)
    add_table(
        doc,
        ["Assunto", "O que a conversa mostra"],
        [
            ["Participação", "Ela aceitou o projeto e se dispôs a passar dados do MEI, do trabalho e das fotos, além da carta e da selfie."],
            ["Concepção", "O briefing de 4 páginas é dela. O portfólio de fotos dos ensaios foi pedido por ela."],
            ["Conteúdo do portfólio", "Ficou combinado um pouco de cada tipo de atendimento, mostrando o processo."],
            ["Imagem", "As fotos do Instagram têm uso de imagem liberado, segundo ela, em 25/09/2026."],
            ["Acompanhamento", "A equipe manda as atualizações e ela diz o que acha. Ela citou alinhar com a Ana ou reunir todo mundo."],
            ["Ainda aberto", "Ela ainda não percorreu as oito telas. Preço, endereço, horário, e-mail, link de WhatsApp e formas de pagamento continuam na lista da seção 2.11."],
        ],
        [4.2, 13.2],
    )
    add_p(
        doc,
        "O briefing escrito continua sendo a fonte da identidade visual. A transcrição bloco a bloco está no material do projeto. Estes prints são a prova de que o documento saiu dela, no meio da conversa do projeto, e de que o portfólio e as fotos foram decididos com ela, não inventados pela equipe.",
    )

    add_h(doc, "5. O que a etapa III recebe")
    add_p(
        doc,
        "A etapa III pega este levantamento e o retorno que ainda falta. Entram no site as correções de preço e de contato, as fotos que ela separar e o teste no celular dela: menu, preço e abertura do WhatsApp. A publicação em endereço estável e o repasse de como alterar um preço ficam nessa etapa. O relatório de extensão pode ser atualizado então, como o enunciado prevê. O cronograma das duas etapas está no relatório.",
    )

    add_h(doc, "6. Referências")
    for ref in [
        "BRASIL. Resolução CNE/CES nº 7, de 18 de dezembro de 2018. Estabelece as diretrizes para a extensão na educação superior.",
        "NAÇÕES UNIDAS. Objetivos de Desenvolvimento Sustentável 5 e 8. Disponível em: https://brasil.un.org/pt-br/sdgs.",
        "PRESSMAN, Roger S.; MAXIM, Bruce R. Engenharia de software: uma abordagem profissional. 8. ed. Porto Alegre: AMGH, 2016.",
        "SOMMERVILLE, Ian. Engenharia de software. 10. ed. São Paulo: Pearson, 2019.",
        "VARELLA, Hellen. Meu briefing. Documento da cliente, 4 páginas, enviado por WhatsApp.",
        "VARELLA, Hellen. Conversas de WhatsApp com a equipe da extensão, inclusive o retorno de 25/09/2026. Figuras 9 a 11 deste documento.",
        "Cadastro público do CNPJ 33.687.461/0001-33. Consulta em 13 out. 2026. Disponível em: https://guiapj.com.br/consulta-cnpj/33687461000133.",
        "ACIAF. Atendimento diferenciado no Salão Beleza Pura. Disponível em: https://portal.aciaf.com.br/atendimento-diferenciado-no-salao-beleza-pura/.",
    ]:
        add_p(doc, ref, 10, space=3)

    doc.save(str(OUT))
    print(OUT)


if __name__ == "__main__":
    main()
