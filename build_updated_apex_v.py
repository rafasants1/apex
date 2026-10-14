# -*- coding: utf-8 -*-
"""
Script to apply complete ABNT NBR 6023/10520 standards,
fix contrast, remove legacy images, and generate modular submissions for APEX V.

Revisão (PLANO_CORRECOES_SLIDES_APEX_V.md, fases B e C):
- fontes de corpo >= 16 pt (template), com texto condensado para caber sem sobreposição;
- cabeçalhos do template restaurados e caixas reposicionadas (geometria por slide em GEOM);
- XML de parágrafo válido (a:spcBef / a:spcAft) com recuo deslocado nos marcadores;
- ícones das ODS 7 e 12 no slide 5 (assets/ods_7.* e assets/ods_12.*);
- pacotes modulares (M1/M2) sem relações órfãs.
Este é o gerador vigente (substitui build_updated_apex_v.py).
"""

import os
import re
import zipfile
import shutil
import xml.etree.ElementTree as ET

# Namespaces
P_NS = "http://schemas.openxmlformats.org/presentationml/2006/main"
A_NS = "http://schemas.openxmlformats.org/drawingml/2006/main"
R_NS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
CT_NS = "http://schemas.openxmlformats.org/package/2006/content-types"

ET.register_namespace('p', P_NS)
ET.register_namespace('a', A_NS)
ET.register_namespace('r', R_NS)

BASE = os.path.dirname(os.path.abspath(__file__))
SRC_PPTX = os.path.join(BASE, "TEMPLATE PADRÃO PARA DESENVOLVIMENTO DOS TRABALHOS DE EXTENSÃO _ POR ETAPAS-1 (1).pptx")
OUT_PPTX = os.path.join(BASE, "TEMPLATE_PREENCHIDO_APEX_V_PERFORMA_ENERGY.pptx")
OUT_M1 = os.path.join(BASE, "APEX_V_Modulo_1_Etapa_1_Slides_1_a_6.pptx")
OUT_M2 = os.path.join(BASE, "APEX_V_Modulo_2_Etapa_2_Slides_1_a_10.pptx")

EMU_PT = 12700

# Tamanhos (centésimos de pt) e cores
T_SUB = 1800      # subtítulo / instrução
T_BODY = 1600     # corpo (template: 16 pt)
C_LBL = "A33D6B"  # magenta do template
C_TXT = "262626"
C_NAVY = "1F497D"
C_GRAY = "595959"
BUL_MAR = 285750  # recuo deslocado dos marcadores (22,5 pt)


def make_p(runs, algn=None, spc_bef=None, spc_aft=None, bullet=False, bullet_char="•", mar_l=None, indent=None):
    p = ET.Element(f"{{{A_NS}}}p")
    pPr = ET.SubElement(p, f"{{{A_NS}}}pPr")
    if bullet:
        if mar_l is None:
            mar_l = BUL_MAR
        if indent is None:
            indent = -BUL_MAR
    if algn:
        pPr.attrib["algn"] = algn
    if mar_l is not None:
        pPr.attrib["marL"] = str(mar_l)
    if indent is not None:
        pPr.attrib["indent"] = str(indent)
    # Ordem exigida pelo esquema: spcBef, spcAft, buFont*, buChar
    if spc_bef is not None:
        spcBef = ET.SubElement(pPr, f"{{{A_NS}}}spcBef")
        spcPts = ET.SubElement(spcBef, f"{{{A_NS}}}spcPts")
        spcPts.attrib["val"] = str(spc_bef)
    if spc_aft is not None:
        spcAft = ET.SubElement(pPr, f"{{{A_NS}}}spcAft")
        spcPts = ET.SubElement(spcAft, f"{{{A_NS}}}spcPts")
        spcPts.attrib["val"] = str(spc_aft)
    if bullet:
        ET.SubElement(pPr, f"{{{A_NS}}}buFontTx")
        buChar = ET.SubElement(pPr, f"{{{A_NS}}}buChar")
        buChar.attrib["char"] = bullet_char
    else:
        ET.SubElement(pPr, f"{{{A_NS}}}buNone")

    for r_item in runs:
        text, sz, bold, color_srgb, color_scheme, italic = r_item[:6]
        link_rid = r_item[6] if len(r_item) > 6 else None
        r = ET.SubElement(p, f"{{{A_NS}}}r")
        rPr = ET.SubElement(r, f"{{{A_NS}}}rPr")
        rPr.attrib["lang"] = "pt-BR"
        if sz is not None:
            rPr.attrib["sz"] = str(sz)
        rPr.attrib["b"] = "1" if bold else "0"
        if italic:
            rPr.attrib["i"] = "1"

        if color_srgb:
            sf = ET.SubElement(rPr, f"{{{A_NS}}}solidFill")
            clr = ET.SubElement(sf, f"{{{A_NS}}}srgbClr")
            clr.attrib["val"] = color_srgb
        elif color_scheme:
            sf = ET.SubElement(rPr, f"{{{A_NS}}}solidFill")
            clr = ET.SubElement(sf, f"{{{A_NS}}}schemeClr")
            clr.attrib["val"] = color_scheme
        if link_rid:
            hl = ET.SubElement(rPr, f"{{{A_NS}}}hlinkClick")
            hl.attrib[f"{{{R_NS}}}id"] = link_rid

        t = ET.SubElement(r, f"{{{A_NS}}}t")
        t.text = text
    return p


def simple_p(text, sz=T_BODY, bold=False, color_srgb=None, color_scheme=None, algn=None, spc_bef=None, spc_aft=None, bullet=False, bullet_char="•", italic=False, link_rid=None):
    return make_p([(text, sz, bold, color_srgb, color_scheme, italic, link_rid)], algn=algn, spc_bef=spc_bef, spc_aft=spc_aft, bullet=bullet, bullet_char=bullet_char)


def item(label, text, sz=T_BODY, bef=700, algn=None):
    """Item com marcador: rótulo em negrito (magenta) seguido do texto."""
    return make_p([
        (label + " ", sz, True, C_LBL, None, False),
        (text, sz, False, C_TXT, None, False),
    ], spc_bef=bef, bullet=True, algn=algn)


def sub(text, sz=T_SUB):
    """Subtítulo/instrução no estilo do template (azul de destaque)."""
    return simple_p(text, sz=sz, bold=True, color_scheme="accent1")


def note(text, bef=900):
    return simple_p(text, sz=T_BODY, italic=True, color_srgb=C_GRAY, spc_bef=bef)


def replace_shape_text(root, shape_name=None, shape_id=None, paragraphs=[]):
    ns = {'p': P_NS, 'a': A_NS}
    for sp in root.findall('.//p:sp', ns):
        cNvPr = sp.find('.//p:nvSpPr/p:cNvPr', ns)
        if cNvPr is None:
            continue
        cur_name = cNvPr.attrib.get('name')
        cur_id = cNvPr.attrib.get('id')

        match = False
        if shape_id is not None and cur_id == str(shape_id):
            match = True
        elif shape_name is not None and cur_name == shape_name:
            match = True

        if match:
            txBody = sp.find('.//p:txBody', ns)
            if txBody is None:
                txBody = ET.SubElement(sp, f"{{{P_NS}}}txBody")
                bodyPr = ET.SubElement(txBody, f"{{{A_NS}}}bodyPr")
                bodyPr.attrib["wrap"] = "square"
                ET.SubElement(txBody, f"{{{A_NS}}}lstStyle")
            else:
                for old_p in list(txBody.findall(f'{{{A_NS}}}p')):
                    txBody.remove(old_p)
            for new_p in paragraphs:
                txBody.append(new_p)
            return True
    return False


def set_geometry(root, shape_id, x, y, w, h):
    """Reposiciona/redimensiona uma forma (sp ou pic) pelo id. Medidas em pontos."""
    ns = {'p': P_NS, 'a': A_NS}
    spTree = root.find('.//p:spTree', ns)
    for el in spTree:
        tag = el.tag.split('}')[1]
        if tag not in ('sp', 'pic'):
            continue
        c = el.find('.//p:cNvPr', ns)
        if c is None or c.attrib.get('id') != str(shape_id):
            continue
        xfrm = el.find('p:spPr/a:xfrm', ns)
        if xfrm is None:
            return False
        off = xfrm.find('a:off', ns)
        ext = xfrm.find('a:ext', ns)
        off.attrib['x'], off.attrib['y'] = str(int(x * EMU_PT)), str(int(y * EMU_PT))
        ext.attrib['cx'], ext.attrib['cy'] = str(int(w * EMU_PT)), str(int(h * EMU_PT))
        return True
    return False


def add_pic(root, rid, pic_id, name, descr, x, y, w, h):
    """Insere uma imagem (já relacionada por rid) no fim da árvore de formas."""
    spTree = root.find(f'.//{{{P_NS}}}spTree')
    pic = ET.SubElement(spTree, f"{{{P_NS}}}pic")
    nv = ET.SubElement(pic, f"{{{P_NS}}}nvPicPr")
    c = ET.SubElement(nv, f"{{{P_NS}}}cNvPr")
    c.attrib.update({"id": str(pic_id), "name": name, "descr": descr})
    cp = ET.SubElement(nv, f"{{{P_NS}}}cNvPicPr")
    lk = ET.SubElement(cp, f"{{{A_NS}}}picLocks")
    lk.attrib["noChangeAspect"] = "1"
    ET.SubElement(nv, f"{{{P_NS}}}nvPr")
    bf = ET.SubElement(pic, f"{{{P_NS}}}blipFill")
    blip = ET.SubElement(bf, f"{{{A_NS}}}blip")
    blip.attrib[f"{{{R_NS}}}embed"] = rid
    st = ET.SubElement(bf, f"{{{A_NS}}}stretch")
    ET.SubElement(st, f"{{{A_NS}}}fillRect")
    spPr = ET.SubElement(pic, f"{{{P_NS}}}spPr")
    xf = ET.SubElement(spPr, f"{{{A_NS}}}xfrm")
    off = ET.SubElement(xf, f"{{{A_NS}}}off")
    off.attrib.update({"x": str(int(x * EMU_PT)), "y": str(int(y * EMU_PT))})
    ext = ET.SubElement(xf, f"{{{A_NS}}}ext")
    ext.attrib.update({"cx": str(int(w * EMU_PT)), "cy": str(int(h * EMU_PT))})
    pg = ET.SubElement(spPr, f"{{{A_NS}}}prstGeom")
    pg.attrib["prst"] = "rect"
    ET.SubElement(pg, f"{{{A_NS}}}avLst")


def clean_legacy_pics(root, slide_num):
    """Remove legacy sample images (Reels, Padlet, Concremiza) from slides 14, 15, and 16"""
    ns = {'p': P_NS}
    spTree = root.find('.//p:spTree', ns)
    if spTree is None:
        return

    pics_to_remove = []
    for pic in spTree.findall('p:pic', ns):
        cNvPr = pic.find('.//p:nvPicPr/p:cNvPr', ns)
        if cNvPr is not None:
            name = cNvPr.attrib.get('name', '')
            # Picture 4 is usually the template logo/border - keep it
            if name != "Picture 4":
                pics_to_remove.append(pic)

    for pic in pics_to_remove:
        spTree.remove(pic)
        print(f"Removed legacy pic from slide {slide_num}")


# ----------------------------------------------------------------------------
# Geometria (pt) por slide: {id_da_forma: (x, y, w, h)}
# Títulos limitados a ~600 pt de largura para não colidir com o logo da Unyleya.
# ----------------------------------------------------------------------------
GEOM = {
    1: {12: (88, 215, 822, 190)},
    2: {4: (262, 355, 565, 175)},
    3: {4: (80, 100, 830, 40), 2: (120, 165, 760, 60), 3: (120, 235, 760, 220)},
    4: {8: (146, 100, 740, 31), 2: (110, 148, 780, 340)},
    5: {3: (84, 84, 772, 40), 2: (61, 135, 650, 350), 12: (710, 422, 235, 30)},
    6: {2: (93, 95, 800, 40), 3: (70, 148, 570, 340)},
    7: {12: (88, 215, 822, 190)},
    8: {2: (83, 95, 845, 40), 5: (100, 150, 790, 330)},
    9: {5: (174, 29, 600, 65), 6: (77, 90, 859, 40), 4: (80, 135, 810, 350)},
    10: {4: (174, 29, 600, 65), 6: (77, 90, 859, 40), 7: (80, 135, 810, 350)},
    11: {12: (88, 215, 822, 190)},
    12: {2: (166, 28, 600, 65), 5: (83, 92, 800, 40), 6: (83, 135, 800, 350)},
    13: {2: (166, 28, 600, 65), 5: (83, 92, 800, 40), 6: (83, 135, 800, 350)},
    14: {3: (166, 32, 600, 60), 7: (84, 98, 820, 240), 11: (84, 352, 780, 30), 10: (84, 384, 780, 32)},
    15: {3: (166, 32, 600, 60), 2: (84, 98, 800, 40), 7: (84, 140, 800, 340)},
    16: {3: (166, 32, 600, 60), 7: (84, 98, 800, 380)},
    17: {3: (157, 32, 645, 45), 8: (100, 92, 780, 36), 6: (100, 135, 780, 350)},
    18: {3: (157, 32, 701, 45), 7: (100, 92, 780, 36), 2: (100, 135, 780, 350)},
    19: {7: (96, 76, 755, 31), 2: (70, 108, 830, 370)},
    20: {4: (40, 95, 360, 400)},
}

# Imagens a inserir por slide: (arquivo em assets/, nome da forma, descrição, id, x, y, w, h)
ODS_ICON_SIZE = 86
PICS = {
    5: [
        ("ods_7", "ODS 7", "Ícone da ODS 7 — Energia limpa e acessível", 101, 780, 130 + 96 * 0, ODS_ICON_SIZE, ODS_ICON_SIZE),
        ("ods_12", "ODS 12", "Ícone da ODS 12 — Consumo e produção responsáveis", 102, 780, 130 + 96 * 2, ODS_ICON_SIZE, ODS_ICON_SIZE),
    ],
}
# A imagem existente da ODS 9 (id 5) é reposicionada na posição intermediária.
GEOM[5][5] = (780, 130 + 96, ODS_ICON_SIZE, ODS_ICON_SIZE)


def build_slides_data():
    slides = {}

    # SLIDE 1: Capa 1ª Etapa (Módulo 1) — a instrução original do template (id 4) é preservada
    slides[1] = [
        (12, "CaixaDeTexto 11", [
            simple_p("PROJETO DE EXTENSÃO UNIVERSITÁRIA — APEX V (BANCO DE DADOS)", sz=2000, bold=True, color_srgb=C_NAVY, algn="ctr"),
            simple_p("Programa Institucional: Educando para a Cidadania (Resolução CNE/CES nº 7/2018)", sz=T_BODY, color_srgb=C_GRAY, algn="ctr", spc_bef=500),
            simple_p("1ª ETAPA: PLANEJAMENTO DA EXTENSÃO (MÓDULO 1)", sz=T_SUB, bold=True, color_srgb=C_LBL, algn="ctr", spc_bef=900),
            simple_p("Slides 2 a 6: identificação, ementa, ODS 7, 9 e 12 e local de implementação", sz=T_BODY, color_srgb=C_TXT, algn="ctr", spc_bef=500),
            simple_p("Empresa parceira: Performa Energy | Ano letivo: 2026", sz=T_BODY, bold=True, color_srgb=C_NAVY, algn="ctr", spc_bef=700),
        ])
    ]

    # SLIDE 2: Identificação do Curso e Título do Trabalho
    slides[2] = [
        (4, "CaixaDeTexto 3", [
            simple_p("Curso Superior de Tecnologia em Banco de Dados", sz=2000, bold=True, color_scheme="bg1", algn="r"),
            simple_p("Disciplina: AMBIENTE PROFISSIONAL E DE EXTENSÃO EM BANCO DE DADOS V", sz=1400, color_scheme="bg1", algn="r", spc_bef=350),
            simple_p("TÍTULO DO TRABALHO DE EXTENSÃO:", sz=1300, bold=True, color_scheme="bg1", algn="r", spc_bef=450),
            simple_p("Performalog Atendimento: Agente Inteligente de Cobrança e Arquitetura de Banco de Dados para Gestão de Energia Solar na Performa Energy", sz=1600, bold=True, color_scheme="bg1", algn="r", spc_bef=200),
        ])
    ]

    # SLIDE 3: Apresentação
    slides[3] = [
        (7, "CaixaDeTexto 6", [
            simple_p("APRESENTAÇÃO", sz=2400, bold=True, color_srgb=C_LBL)
        ]),
        (4, "CaixaDeTexto 3", [
            sub("Dados acadêmicos do discente extensionista e da orientação docente")
        ]),
        (2, "CaixaDeTexto 1", [
            simple_p("Curso Superior de Tecnologia em Banco de Dados", sz=2200, bold=True, color_srgb=C_LBL),
            simple_p("Faculdade Unyleya — Carga horária de extensão curricular: 100 horas", sz=T_BODY, color_srgb=C_GRAY, spc_bef=400),
        ]),
        (3, "CaixaDeTexto 2", [
            make_p([("Discente: ", 1800, True, C_LBL, None, False), ("Rafael Silva", 1800, False, C_TXT, None, False)], spc_bef=0),
            make_p([("Matrícula: ", 1800, True, C_LBL, None, False), ("1103239", 1800, False, C_TXT, None, False)], spc_bef=900),
            make_p([("Orientadora e coordenadora do curso: ", 1800, True, C_LBL, None, False), ("Profa. Dra. Carla Corrêa Tavares dos Reis", 1800, False, C_TXT, None, False)], spc_bef=900),
            make_p([("Local de aplicação: ", 1800, True, C_LBL, None, False), ("Performa Energy (gestão de créditos de energia solar e CRM Performalog)", 1800, False, C_TXT, None, False)], spc_bef=900),
            make_p([("Modalidade: ", 1800, True, C_LBL, None, False), ("presencial, na sede da empresa, com oficina técnica de Banco de Dados, IA e protótipo no Figma", 1800, False, C_TXT, None, False)], spc_bef=900),
        ])
    ]

    # SLIDE 4: Disciplina e Ementa
    slides[4] = [
        (6, "CaixaDeTexto 5", [
            simple_p("OBJETIVO DE DESENVOLVIMENTO SUSTENTÁVEL DO PROJETO EXTENSIONISTA “EDUCANDO PARA A CIDADANIA”", sz=2000, bold=True, color_srgb=C_LBL)
        ]),
        (8, "CaixaDeTexto 7", [
            sub("Disciplina e ementa oficial (Resolução CNE/CES MEC nº 7/2018)")
        ]),
        (2, "CaixaDeTexto 1", [
            simple_p("Disciplina:", sz=T_BODY, bold=True, color_srgb="000000"),
            simple_p("AMBIENTE PROFISSIONAL E DE EXTENSÃO EM BANCO DE DADOS V", sz=T_BODY, color_srgb="000000"),
            simple_p("Ementa:", sz=T_BODY, bold=True, color_srgb="000000", spc_bef=1000),
            simple_p("Problematização de temas conectados com a vida real na sociedade atual para solução por meio de projetos. Estabelecimento de direcionamentos e regras para a realização do desafio. Desenvolvimento de soft skills como trabalho em equipe, resolução de problemas complexos, comunicação, criatividade, entre outros. Tradução dos conhecimentos científicos para a comunidade. Inteligência Artificial: desafios e oportunidades. Programa de Extensão Institucional como proposta de diálogo entre a comunidade acadêmica e sociedade. Produção de materiais educacionais com uso das mídias digitais.", sz=T_BODY, color_srgb="000000", algn="just"),
            simple_p("Alinhamento ao curso:", sz=T_BODY, bold=True, color_srgb="000000", spc_bef=1000),
            simple_p("O projeto leva à Performa Energy conhecimentos de modelagem relacional, integridade de dados, integração de APIs e IA responsável, criando uma base confiável e auditável para atendimento e cobrança.", sz=T_BODY, color_srgb="000000", algn="just"),
        ])
    ]

    # SLIDE 5: ODS / Tema Gerador
    slides[5] = [
        (6, "CaixaDeTexto 5", [
            simple_p("OBJETIVO DE DESENVOLVIMENTO SUSTENTÁVEL DO PROJETO EXTENSIONISTA “EDUCANDO PARA A CIDADANIA”", sz=2000, bold=True, color_srgb=C_LBL)
        ]),
        (3, "CaixaDeTexto 2", [
            sub("Tema gerador: modelagem de dados, IA responsável e sustentabilidade energética (Agenda 2030)")
        ]),
        (2, "CaixaDeTexto 1", [
            item("ODS 7 — Energia limpa e acessível (metas 7.2 e 7.b):",
                 "estimula a geração solar distribuída (Lei nº 14.300/2022); o projeto organiza dados de faturamento e de créditos (kWh) para o cliente entender o benefício da assinatura.", bef=0),
            item("ODS 9 — Indústria, inovação e infraestrutura (metas 9.4 e 9.5):",
                 "moderniza a TI da Performa Energy com a WhatsApp Cloud API oficial e a modelagem relacional de mensageria integrada ao CRM Performalog."),
            item("ODS 12 — Consumo e produção responsáveis (meta 12.8):",
                 "dá transparência ao faturamento da compensação, com acesso claro ao consumo, aos créditos e à composição tarifária."),
            item("Governança de dados (ODS 16 e LGPD, Lei nº 13.709/2018):",
                 "opt-in/opt-out e agente de IA que não expõe dados de faturas nem inventa valores."),
        ]),
        (12, "CaixaDeTexto 11", [
            simple_p("Fonte: https://brasil.un.org/pt-br/sdgs", sz=1150, bold=True, color_scheme="accent1", algn="ctr", link_rid="rId4")
        ])
    ]

    # SLIDE 6: Local de Implementação
    slides[6] = [
        (8, "CaixaDeTexto 7", [
            simple_p("LOCAL DE IMPLEMENTAÇÃO", sz=2400, bold=True, color_srgb=C_LBL)
        ]),
        (2, "CaixaDeTexto 1", [
            sub("Empresa concedente, ambiente de dados e público atendido")
        ]),
        (3, "CaixaDeTexto 2", [
            item("Empresa e atividade:", "Consórcio Performa Energy — gestão e distribuição de créditos de energia solar por assinatura na área da CEMIG (Geração Distribuída, Lei nº 14.300/2022).", bef=0),
            item("Endereço:", "Av. Brasil, 888, Sala 1308, Santa Efigênia, Belo Horizonte – MG, CEP 30140-001. CNPJ: 55.845.710/0001-04."),
            item("Ambiente de dados:", "CRM Performalog (MySQL), com relatórios de rateio da CEMIG e faturas da Digital Grid; passará a integrar a WhatsApp Cloud API da Meta."),
            item("Espaço da intervenção:", "sede com rede corporativa, estações de trabalho com acesso ao CRM e sala de reuniões para a capacitação presencial."),
            item("Público:", "direto — colaboradores de Atendimento, Cobrança e Operações; indireto — clientes assinantes atendidos via WhatsApp."),
        ])
    ]

    # SLIDE 7: Capa 2ª Etapa (Módulo 2) — instrução original preservada (id 4)
    slides[7] = [
        (12, "CaixaDeTexto 11", [
            simple_p("PROJETO DE EXTENSÃO UNIVERSITÁRIA — APEX V (BANCO DE DADOS)", sz=2000, bold=True, color_srgb=C_NAVY, algn="ctr"),
            simple_p("2ª ETAPA: DESAFIO, PARTICIPANTES E ARQUITETURA DE DADOS (MÓDULO 2)", sz=T_SUB, bold=True, color_srgb=C_LBL, algn="ctr", spc_bef=900),
            simple_p("Slides 8 a 10: participantes, desafio identificado e aprofundamento teórico em modelagem relacional, APIs de mensageria e governança de IA", sz=T_BODY, color_srgb=C_TXT, algn="ctr", spc_bef=500),
            simple_p("Empresa parceira: Performa Energy | Ano letivo: 2026", sz=T_BODY, bold=True, color_srgb=C_NAVY, algn="ctr", spc_bef=700),
        ])
    ]

    # SLIDE 8: Participantes (contagens por equipe removidas até confirmação — A2)
    slides[8] = [
        (3, "CaixaDeTexto 2", [
            simple_p("PARTICIPANTES", sz=2400, bold=True, color_srgb=C_LBL)
        ]),
        (2, "CaixaDeTexto 1", [
            sub("Cargos e funções envolvidos, sem menção a nomes (diretriz institucional)")
        ]),
        (5, "CaixaDeTexto 4", [
            item("Atendimento e Sucesso do Cliente:", "linha de frente do suporte via WhatsApp, dúvidas sobre a cobrança dupla (CEMIG + Performa) e triagem de solicitações e cancelamentos.", bef=0),
            item("Cobrança e Contas a Receber:", "recuperação de crédito, negociação de débitos vencidos, réguas de cobrança e acordos via Pix e boleto."),
            item("Faturamento e Operações de Energia:", "rateio mensal de créditos (CEMIG), conciliação de kWh injetados e importação das faturas da Digital Grid."),
            item("TI, Segurança e Operações:", "administração do banco MySQL do Performalog, regras de acesso, infraestrutura da API da Meta e conformidade com a LGPD."),
        ])
    ]

    # SLIDE 9: Desafio Identificado
    slides[9] = [
        (5, "CaixaDeTexto 4", [
            simple_p("DESAFIO/ QUESTÃO PROBLEMA IDENTIFICADA", sz=2400, bold=True, color_srgb=C_LBL)
        ]),
        (6, "CaixaDeTexto 5", [
            sub("Diagnóstico: sobrecarga no atendimento, inadimplência e dados desconectados")
        ]),
        (4, "CaixaDeTexto 3", [
            item("Sobrecarga no atendimento:", "o cliente recebe duas cobranças (CEMIG e Performa Energy) e tem dificuldade de entender o rateio de créditos em kWh, o que gera muitos chamados repetitivos.", bef=0),
            item("Inadimplência e negociação manual:", "a cobrança dependia de planilhas Excel e de uma ferramenta de mensagens legada (Maxbot), isolada do CRM, com atrasos nos lembretes e pouca rastreabilidade das promessas de pagamento."),
            item("Risco de alucinação e de violação à LGPD:", "chatbots sem ligação determinística ao banco podem inventar valores, aplicar descontos não autorizados ou expor dados de faturas."),
            item("Solução proposta:", "módulo «Performalog Atendimento» integrado à WhatsApp Cloud API, com tabelas relacionais wa_* e agente de cobrança ancorado em dados reais do banco (grounding determinístico)."),
        ])
    ]

    # SLIDE 10: Aprofundamento Teórico (ABNT NBR 10520:2023 - Caixa Mista Autor-Data)
    slides[10] = [
        (4, "CaixaDeTexto 3", [
            simple_p("DESAFIO/ QUESTÃO PROBLEMA IDENTIFICADA", sz=2400, bold=True, color_srgb=C_LBL)
        ]),
        (6, "CaixaDeTexto 5", [
            sub("Aprofundamento teórico: modelagem relacional, grounding e governança de dados")
        ]),
        (7, "CaixaDeTexto 6", [
            item("Modelagem relacional e integridade (Codd, 1970; Silberschatz et al., 2020):",
                 "segundo Codd (1970), Date (2004) e Elmasri e Navathe (2018), a consistência vem de modelos relacionais normalizados. O subsistema wa_* (wa_contact, wa_conversation, wa_message, wa_campaign) garante integridade referencial com clientes e faturas.", bef=0),
            item("Grounding determinístico vs. alucinação de IA (Russell; Norvig, 2022; O'Neil, 2020):",
                 "para evitar “armas de destruição matemática” (O'Neil, 2020) e alucinações em dados financeiros, a LLM só conduz o diálogo; valores, encargos e saldos em kWh vêm de consultas SQL determinísticas."),
            item("Privacidade por design e ética (Floridi, 2023; Meta Platforms, 2026):",
                 "conforme a LGPD (Lei nº 13.709/2018), o sistema adota tokens em variáveis de ambiente, verificação SHA-256 de webhooks e gestão de opt-in/opt-out."),
        ])
    ]

    # SLIDE 11: Capa 3ª Etapa (Módulo 3) — instrução original preservada (id 4)
    slides[11] = [
        (12, "CaixaDeTexto 11", [
            simple_p("PROJETO DE EXTENSÃO UNIVERSITÁRIA — APEX V (BANCO DE DADOS)", sz=2000, bold=True, color_srgb=C_NAVY, algn="ctr"),
            simple_p("3ª ETAPA: PLANEJAMENTO TÉCNICO-PEDAGÓGICO, PRODUTO FIGMA E IMPACTO", sz=T_SUB, bold=True, color_srgb=C_LBL, algn="ctr", spc_bef=900),
            simple_p("Slides 12 a 19: planejamento pedagógico, cronograma, material educativo digital (Figma), registros, autoavaliação, avaliação da comunidade e referências", sz=T_BODY, color_srgb=C_TXT, algn="ctr", spc_bef=500),
            simple_p("Empresa parceira: Performa Energy | Ano letivo: 2026", sz=T_BODY, bold=True, color_srgb=C_NAVY, algn="ctr", spc_bef=700),
        ])
    ]

    # SLIDE 12: Planejamento Pedagógico (Conteúdos) — redação de planejamento (B3)
    slides[12] = [
        (2, "CaixaDeTexto 1", [
            simple_p("INFORMAÇÕES ESSENCIAIS SOBRE O PLANEJAMENTO", sz=2400, bold=True, color_srgb=C_LBL)
        ]),
        (5, "CaixaDeTexto 4", [
            sub("Conteúdos, mídia digital e estratégia metodológica")
        ]),
        (6, "CaixaDeTexto 5", [
            item("Conteúdos a serem abordados:",
                 "arquitetura de dados de mensageria (subsistema wa_* no MySQL); operação do agente de cobrança (identificação por CPF, consulta em tempo real, multa rescisória e saldo CEMIG em kWh); tratamento padronizado de contestações; governança, alçada de negociação e transbordo humano.", bef=0),
            item("Mídia digital a ser desenvolvida:",
                 "protótipo navegável no Figma da nova aba «Atendimento» do CRM Performalog, com tela de chat, Ficha 360° do cliente e console da régua de cobrança."),
            item("Estratégia metodológica:",
                 "andragogia (Knowles; Holton III; Swanson, 2009): aprendizagem experiencial centrada em problemas reais, com simulação de atendimentos e testes de transbordo no protótipo."),
        ])
    ]

    # SLIDE 13: Planejamento Pedagógico (Cronograma)
    slides[13] = [
        (2, "CaixaDeTexto 1", [
            simple_p("INFORMAÇÕES ESSENCIAIS SOBRE O PLANEJAMENTO", sz=2400, bold=True, color_srgb=C_LBL)
        ]),
        (5, "CaixaDeTexto 4", [
            sub("Etapas, responsáveis e cronograma integrado de 6 semanas")
        ]),
        (6, "CaixaDeTexto 5", [
            item("Semana 1 — Diagnóstico de dados:", "levantamento dos relatórios da CEMIG e das faturas da Digital Grid no MySQL. (Discente e TI)", bef=0, sz=T_BODY),
            item("Semana 2 — Modelagem relacional:", "especificação das tabelas wa_* e envio da 1ª etapa no AVA. (Discente)", bef=500),
            item("Semana 3 — Regras do agente de cobrança:", "estruturação das categorias de contestação e das réguas de negociação; envio da 2ª etapa no AVA. (Discente)", bef=500),
            item("Semana 4 — Certificação iTalents e Figma:", "conclusão do curso de Figma e construção das telas navegáveis da aba Atendimento. (Discente)", bef=500),
            item("Semana 5 — Intervenção presencial:", "oficina na Performa Energy, testes com a equipe e registro das 3 fotos obrigatórias. (Discente e colaboradores)", bef=500),
            item("Semana 6 — Avaliação e entrega final:", "tabulação dos questionários Likert, autoavaliação nas 5 dimensões e entrega de slides, certificado e link do Figma. (Discente)", bef=500),
        ])
    ]

    # SLIDE 14: Material Educativo Digital (Conceito e Link)
    slides[14] = [
        (3, "CaixaDeTexto 2", [
            simple_p("MATERIAL EDUCATIVO DIGITAL", sz=2400, bold=True, color_srgb=C_LBL)
        ]),
        (7, "CaixaDeTexto 6", [
            sub("Protótipo navegável «Performalog Atendimento» (Figma)"),
            simple_p("Propõe-se um protótipo navegável de alta fidelidade que representa a integração da WhatsApp Cloud API ao CRM Performalog, oferecendo à equipe uma interface única para supervisionar o agente inteligente, negociar dívidas e dar suporte técnico.", sz=T_SUB, color_srgb=C_TXT, spc_bef=900),
            make_p([
                ("Orientações de uso: ", T_SUB, True, C_LBL, None, False),
                ("o protótipo será acessado pelo navegador, por link público, com perfis diferenciados (Admin, Cobrança e Sucesso do Cliente), modo claro e escuro, console da API e simulador móvel para testes de ponta a ponta.", T_SUB, False, C_TXT, None, False),
            ], spc_bef=900),
        ]),
        (11, "CaixaDeTexto 10", [
            simple_p("Link público para acesso e navegação interativa no protótipo Figma:", sz=T_BODY, bold=True, color_srgb=C_NAVY)
        ]),
        (10, "CaixaDeTexto 9", [
            simple_p("https://www.figma.com/proto/performalog-atendimento-cobranca", sz=T_BODY, bold=True, color_srgb="0070C0")
        ]),
    ]

    # SLIDE 15: Material Educativo Digital (Módulos e Telas)
    slides[15] = [
        (3, "CaixaDeTexto 2", [
            simple_p("MATERIAL EDUCATIVO DIGITAL", sz=2400, bold=True, color_srgb=C_LBL)
        ]),
        (2, "CaixaDeTexto 1", [
            sub("Telas e módulos operacionais previstos no protótipo")
        ]),
        (7, "CaixaDeTexto 6", [
            item("Inbox unificado e chat:", "painel de 3 colunas (filtros, chat com identificação de mensagens do bot e do humano, controle da janela de 24 h da Meta) para intervenção imediata do atendente.", bef=0),
            item("Ficha 360° do cliente:", "dados do banco sincronizados — unidades consumidoras, saldo de créditos CEMIG em kWh, faturas abertas na Digital Grid e histórico de contestações."),
            item("Painel ao vivo e autorizações:", "filas por setor, situação dos atendentes e aprovação de acordos que excedam a alçada autônoma do agente."),
            item("Régua de cobrança e disparos:", "parametrização da régua (D-3, D0, D+5, D+10) e segmentação de destinatários com templates aprovados pela Meta."),
        ])
    ]

    # SLIDE 16: Registros do Desenvolvimento da Atividade (3 Fotos Presenciais)
    slides[16] = [
        (3, "CaixaDeTexto 2", [
            simple_p("REGISTROS DO DESENVOLVIMENTO DA ATIVIDADE", sz=2400, bold=True, color_srgb=C_LBL)
        ]),
        (7, "CaixaDeTexto 6", [
            sub("Registros fotográficos previstos para a apresentação presencial"),
            item("Foto 1 — Abertura e arquitetura do banco:", "discente apresentando a modelagem das tabelas wa_*, o fluxo do agente e a integração com os relatórios da CEMIG, com as equipes reunidas.", bef=900),
            item("Foto 2 — Oficina prática no protótipo:", "analistas, em suas estações de trabalho, navegando no protótipo Figma e simulando atendimento, consulta de créditos em kWh e negociação."),
            item("Foto 3 — Debate sobre transbordo e avaliação:", "discussão sobre governança de dados e alçadas de desconto, seguida do preenchimento da ficha de avaliação."),
            note("As fotos reais, com consentimento dos participantes, serão inseridas no Módulo 4, após a realização da oficina."),
        ])
    ]

    # SLIDE 17: Autoavaliação do Estudante (5 Dimensões) — redação prospectiva (B3)
    slides[17] = [
        (3, "CaixaDeTexto 2", [
            simple_p("AUTOAVALIAÇÃO", sz=2400, bold=True, color_srgb=C_LBL)
        ]),
        (8, "CaixaDeTexto 7", [
            sub("Reflexão sobre as cinco dimensões formativas da Unyleya")
        ]),
        (6, "CaixaDeTexto 5", [
            item("Relevância da temática (global e local):", "a união entre energia limpa (ODS 7) e inovação em banco de dados e IA (ODS 9) deve mostrar como soluções locais do setor solar contribuem para metas globais.", bef=0),
            item("Formação acadêmica em Banco de Dados:", "prevê-se consolidar, na prática, modelagem relacional, integridade referencial, consultas, integração via APIs e governança sob a LGPD.", bef=500),
            item("Soft skills:", "espera-se evoluir em comunicação técnica e pedagógica, negociação e escuta das dificuldades operacionais dos usuários.", bef=500),
            item("Conexão com a comunidade:", "a atividade busca aproximar a teoria das necessidades reais da equipe da Performa Energy, gerando valor compartilhado.", bef=500),
            item("Empoderamento e transformação social:", "busca-se ampliar a percepção do tecnólogo em Banco de Dados como arquiteto de soluções éticas que protegem a privacidade e a cidadania.", bef=500),
        ])
    ]

    # SLIDE 18: Planejamento e Metas da Avaliação da Comunidade (N removido até confirmação — A2)
    slides[18] = [
        (3, "CaixaDeTexto 2", [
            simple_p("AVALIAÇÃO DA COMUNIDADE ATENDIDA", sz=2400, bold=True, color_srgb=C_LBL)
        ]),
        (7, "CaixaDeTexto 6", [
            sub("Planejamento da avaliação: instrumento, metas e focos de coleta")
        ]),
        (2, "CaixaDeTexto 1", [
            item("Instrumento:", "questionário anônimo em escala Likert de 1 a 5, aplicado aos colaboradores participantes da oficina.", bef=0),
            item("Metas:", "média ≥ 4,8 em aderência operacional, usabilidade do Figma, clareza didática e eficiência; 5,0 em segurança e LGPD.", bef=500),
            item("Foco — Cobrança:", "redução do esforço manual em planilhas e eficácia da régua de negociação.", bef=500),
            item("Foco — Sucesso do Cliente:", "clareza na explicação do rateio CEMIG em kWh e das faturas, na Ficha 360°.", bef=500),
            item("Foco — TI e Operações:", "integridade das tabelas wa_*, segurança dos webhooks da Meta e não alucinação de valores pela IA.", bef=500),
            note("Métricas e depoimentos reais serão tabulados no Módulo 4, após a oficina presencial (Semana 5).", bef=700),
        ])
    ]

    # SLIDE 19: Referências Bibliográficas (ABNT NBR 6023:2018 / Emenda 1:2020 - Destaque em Negrito)
    # Título principal em negrito; subtítulos sem destaque; jurisdição BRASIL; ordem alfabética.
    # Números de páginas totais removidos (não verificados).
    R = 1050
    SP = 140

    def ref(parts, bef=SP):
        runs = [(t, R, b, C_TXT, None, False) for t, b in parts]
        return make_p(runs, spc_bef=bef)

    slides[19] = [
        (3, "CaixaDeTexto 2", [
            simple_p("REFERÊNCIAS", sz=2400, bold=True, color_srgb=C_LBL)
        ]),
        (7, "CaixaDeTexto 6", [
            simple_p("Referências conforme a ABNT NBR 6023:2018 (Emenda 1:2020)", sz=T_BODY, bold=True, color_scheme="accent1")
        ]),
        (2, "CaixaDeTexto 1", [
            ref([("BRASIL. Agência Nacional de Energia Elétrica. ", False), ("Resolução Normativa nº 1.000, de 7 de dezembro de 2021", True),
                 (". Estabelece as regras de prestação do serviço público de distribuição de energia elétrica. Diário Oficial da União: seção 1, Brasília, DF, 20 dez. 2021.", False)], bef=0),
            ref([("BRASIL. ", False), ("Lei nº 13.709, de 14 de agosto de 2018", True),
                 (". Lei Geral de Proteção de Dados Pessoais (LGPD). Diário Oficial da União: seção 1, Brasília, DF, 15 ago. 2018.", False)]),
            ref([("BRASIL. ", False), ("Lei nº 14.300, de 6 de janeiro de 2022", True),
                 (". Institui o marco legal da microgeração e minigeração distribuída. Diário Oficial da União: seção 1, Brasília, DF, 7 jan. 2022.", False)]),
            ref([("CODD, E. F. A relational model of data for large shared data banks. ", False), ("Communications of the ACM", True),
                 (", New York, v. 13, n. 6, p. 377-387, jun. 1970.", False)]),
            ref([("DATE, C. J. ", False), ("Introdução a sistemas de bancos de dados", True), (". 8. ed. Rio de Janeiro: Elsevier, 2004.", False)]),
            ref([("ELMASRI, Ramez; NAVATHE, Shamkant B. ", False), ("Sistemas de banco de dados", True), (". 7. ed. São Paulo: Pearson, 2018.", False)]),
            ref([("FLORIDI, Luciano. ", False), ("The ethics of artificial intelligence", True), (": principles, challenges, and opportunities. Oxford: Oxford University Press, 2023.", False)]),
            ref([("KNOWLES, Malcolm S.; HOLTON III, Elwood F.; SWANSON, Richard A. ", False),
                 ("Aprendizagem de resultados", True),
                 (": uma abordagem prática para aumentar a efetividade da educação corporativa. Rio de Janeiro: Elsevier, 2009.", False)]),
            ref([("META PLATFORMS. ", False), ("WhatsApp Business Platform", True),
                 (": Cloud API Reference (Graph API v26.0). Menlo Park: Meta for Developers, 2026. Disponível em: https://developers.facebook.com. Acesso em: 8 out. 2026.", False)]),
            ref([("O'NEIL, Cathy. ", False), ("Armas de destruição matemática", True),
                 (": como o big data aumenta a desigualdade e ameaça a democracia. Santo André: Rua do Sabão, 2020.", False)]),
            ref([("ORGANIZAÇÃO DAS NAÇÕES UNIDAS. ", False), ("Transformando nosso mundo", True),
                 (": a Agenda 2030 para o Desenvolvimento Sustentável. Nova York: ONU, 2015. Disponível em: https://brasil.un.org/pt-br/sdgs. Acesso em: 8 out. 2026.", False)]),
            ref([("RUSSELL, Stuart; NORVIG, Peter. ", False), ("Inteligência artificial", True), (": uma abordagem moderna. 4. ed. Rio de Janeiro: GEN LTC, 2022.", False)]),
            ref([("SILBERSCHATZ, Abraham; KORTH, Henry F.; SUDARSHAN, S. ", False), ("Sistema de banco de dados", True), (". 7. ed. Rio de Janeiro: GEN LTC, 2020.", False)]),
        ])
    ]

    # SLIDE 20: Encerramento (texto escuro sobre a área branca à esquerda da imagem)
    slides[20] = [
        (4, "CaixaDeTexto 3", [
            simple_p("PROJETO DE EXTENSÃO UNIVERSITÁRIA — APEX V (BANCO DE DADOS)", sz=T_SUB, bold=True, color_srgb=C_NAVY, algn="ctr"),
            simple_p("Faculdade Unyleya — Educação Superior a Distância", sz=T_BODY, color_srgb=C_GRAY, algn="ctr", spc_bef=400),
            simple_p("Agradecemos à Performa Energy pela acolhida, pela disponibilização do ambiente do CRM Performalog e pela confiança no projeto.", sz=T_BODY, color_srgb=C_TXT, algn="ctr", spc_bef=1200),
            simple_p("Agradecemos à Profa. Dra. Carla Corrêa Tavares dos Reis pela orientação ao longo da extensão.", sz=T_BODY, color_srgb=C_TXT, algn="ctr", spc_bef=800),
            simple_p("«Tecnologia de dados e inteligência artificial a serviço da sustentabilidade e da cidadania.»", sz=T_BODY, bold=True, italic=True, color_srgb=C_LBL, algn="ctr", spc_bef=1200),
            simple_p("Rafael Silva — Matrícula 1103239 | 2026", sz=T_BODY, bold=True, color_srgb=C_NAVY, algn="ctr", spc_bef=1000),
        ])
    ]

    return slides


def _find_asset(stem):
    """Localiza assets/<stem>.(png|jpg|jpeg); retorna (caminho, extensão) ou (None, None)."""
    for ext in ("png", "jpg", "jpeg"):
        p = os.path.join(BASE, "assets", f"{stem}.{ext}")
        if os.path.exists(p):
            return p, ext
    return None, None


def _ensure_default_ct(ct_xml, ext):
    mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg"}[ext]
    if re.search(r'<Default[^>]*Extension="%s"' % ext, ct_xml, re.I):
        return ct_xml
    return ct_xml.replace("</Types>", f'<Default Extension="{ext}" ContentType="{mime}"/></Types>')


def generate_all_pptx():
    src_pptx = SRC_PPTX
    out_pptx = OUT_PPTX

    slides_data = build_slides_data()
    temp_pptx = out_pptx + ".tmp"

    # Imagens extras (ícones das ODS)
    extra_media = {}   # nome no pacote -> bytes
    slide_extra_rels = {}  # slide -> [(rid, alvo)]
    slide_pics = {}    # slide -> [(rid, nome, descr, id, x, y, w, h)]
    used_exts = set()
    for sn, pics in PICS.items():
        for stem, name, descr, pid, x, y, w, h in pics:
            path, ext = _find_asset(stem)
            if path is None:
                print(f"Aviso: asset {stem} não encontrado em assets/; ícone omitido no slide {sn}.")
                continue
            media_name = f"ppt/media/apexv_{stem}.{ext}"
            with open(path, "rb") as fh:
                extra_media[media_name] = fh.read()
            rid = f"rId{900 + pid}"
            slide_extra_rels.setdefault(sn, []).append((rid, f"../media/apexv_{stem}.{ext}"))
            slide_pics.setdefault(sn, []).append((rid, name, descr, pid, x, y, w, h))
            used_exts.add(ext)

    with zipfile.ZipFile(src_pptx, 'r') as zin:
        with zipfile.ZipFile(temp_pptx, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
            for item_info in zin.infolist():
                filename = item_info.filename
                data = zin.read(filename)

                if filename.startswith("ppt/slides/slide") and filename.endswith(".xml") and not filename.startswith("ppt/slides/_rels"):
                    slide_num_str = filename[len("ppt/slides/slide"):-len(".xml")]
                    try:
                        slide_num = int(slide_num_str)
                    except ValueError:
                        slide_num = None

                    root = ET.fromstring(data)

                    # Clean legacy pictures on slides 14, 15, and 16
                    if slide_num in [14, 15, 16]:
                        clean_legacy_pics(root, slide_num)

                    if slide_num in slides_data:
                        updates = slides_data[slide_num]
                        for shape_id, shape_name, paragraphs in updates:
                            ok = replace_shape_text(root, shape_name=shape_name, shape_id=shape_id, paragraphs=paragraphs)
                            if not ok:
                                print(f"Warning: could not find shape ID={shape_id} Name={shape_name} in slide {slide_num}")

                        for shape_id, (x, y, w, h) in GEOM.get(slide_num, {}).items():
                            if not set_geometry(root, shape_id, x, y, w, h):
                                print(f"Warning: could not set geometry for shape ID={shape_id} in slide {slide_num}")

                        for rid, name, descr, pid, x, y, w, h in slide_pics.get(slide_num, []):
                            add_pic(root, rid, pid, name, descr, x, y, w, h)

                        print(f"Updated slide {slide_num} ({filename}) successfully.")

                    data = ET.tostring(root, encoding="utf-8")

                elif filename.startswith("ppt/slides/_rels/slide") and filename.endswith(".xml.rels"):
                    sn_str = filename[len("ppt/slides/_rels/slide"):-len(".xml.rels")]
                    if sn_str.isdigit() and int(sn_str) in slide_extra_rels:
                        xml = data.decode("utf-8")
                        add = "".join(
                            f'<Relationship Id="{rid}" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/image" Target="{tgt}"/>'
                            for rid, tgt in slide_extra_rels[int(sn_str)]
                        )
                        data = xml.replace("</Relationships>", add + "</Relationships>").encode("utf-8")

                elif filename == "[Content_Types].xml" and used_exts:
                    xml = data.decode("utf-8")
                    for ext in used_exts:
                        xml = _ensure_default_ct(xml, ext)
                    data = xml.encode("utf-8")

                zout.writestr(item_info, data)

            for media_name, blob in extra_media.items():
                zout.writestr(media_name, blob)

    if os.path.exists(out_pptx):
        os.remove(out_pptx)
    os.rename(temp_pptx, out_pptx)
    print(f"PPTX successfully generated at: {out_pptx}")
    print(f"File size: {os.path.getsize(out_pptx)} bytes ({os.path.getsize(out_pptx)/(1024*1024):.2f} MB)")


def generate_modular_pptx(max_slide, out_path):
    """Generate partial PPTX containing only slides up to max_slide (e.g. 6 for M1, 10 for M2)"""
    full_pptx = OUT_PPTX
    temp_pptx = out_path + ".tmp"

    def slide_no(target):
        m = re.search(r'slides/slide(\d+)\.xml$', target)
        return int(m.group(1)) if m else None

    with zipfile.ZipFile(full_pptx, 'r') as zin:
        # Relações da apresentação: descobre quais rIds apontam para slides acima do limite
        rels_xml = zin.read('ppt/_rels/presentation.xml.rels').decode('utf-8')
        rels_root = ET.fromstring(rels_xml)
        drop_rids = set()
        for rel in list(rels_root):
            n = slide_no(rel.attrib.get('Target', ''))
            if n is not None and n > max_slide:
                drop_rids.add(rel.attrib['Id'])
                rels_root.remove(rel)
        ET.register_namespace('', REL_NS)
        new_rels_xml = ET.tostring(rels_root, encoding='utf-8')

        # presentation.xml: remove os sldId correspondentes (por rId, não por posição)
        pres_root = ET.fromstring(zin.read('ppt/presentation.xml'))
        sldIdLst = pres_root.find('.//p:sldIdLst', {'p': P_NS})
        if sldIdLst is not None:
            for child in list(sldIdLst):
                if child.attrib.get(f'{{{R_NS}}}id') in drop_rids:
                    sldIdLst.remove(child)
        new_pres_xml = ET.tostring(pres_root, encoding='utf-8')

        # [Content_Types].xml: remove overrides dos slides descartados
        ct_xml = zin.read('[Content_Types].xml').decode('utf-8')
        def _drop_ct(m):
            n = slide_no(m.group(1))
            return "" if (n is not None and n > max_slide) else m.group(0)
        ct_xml = re.sub(r'<Override[^>]*PartName="(/ppt/slides/slide\d+\.xml)"[^>]*/>', _drop_ct, ct_xml)

        with zipfile.ZipFile(temp_pptx, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
            for item_info in zin.infolist():
                filename = item_info.filename

                # Check if this is a slide beyond max_slide
                if filename.startswith("ppt/slides/slide") and filename.endswith(".xml") and not filename.startswith("ppt/slides/_rels"):
                    slide_num_str = filename[len("ppt/slides/slide"):-len(".xml")]
                    try:
                        s_num = int(slide_num_str)
                        if s_num > max_slide:
                            continue
                    except ValueError:
                        pass

                if filename.startswith("ppt/slides/_rels/slide") and filename.endswith(".xml.rels"):
                    slide_num_str = filename[len("ppt/slides/_rels/slide"):-len(".xml.rels")]
                    try:
                        s_num = int(slide_num_str)
                        if s_num > max_slide:
                            continue
                    except ValueError:
                        pass

                if filename == 'ppt/presentation.xml':
                    zout.writestr(item_info, new_pres_xml)
                elif filename == 'ppt/_rels/presentation.xml.rels':
                    zout.writestr(item_info, new_rels_xml)
                elif filename == '[Content_Types].xml':
                    zout.writestr(item_info, ct_xml.encode('utf-8'))
                else:
                    zout.writestr(item_info, zin.read(filename))

    if os.path.exists(out_path):
        os.remove(out_path)
    os.rename(temp_pptx, out_path)
    print(f"Modular PPTX (Slides 1-{max_slide}) generated at: {out_path}")
    print(f"File size: {os.path.getsize(out_path)} bytes ({os.path.getsize(out_path)/(1024*1024):.2f} MB)")


if __name__ == "__main__":
    generate_all_pptx()
    generate_modular_pptx(6, OUT_M1)
    generate_modular_pptx(10, OUT_M2)
