"""Gera os diagramas de casos de uso do sistema Palco.

A definicao de cada pacote vive na lista PACOTES deste arquivo, com os atores,
os casos de uso e os relacionamentos. A partir dela sao gerados:

    casos-de-uso/*.drawio  arquivo editavel no draw.io (app.diagrams.net)
    build/*.svg            previa para conferir o desenho sem abrir o draw.io

Nunca edite os arquivos gerados a mao: mude PACOTES e rode de novo.

Uso:
    python tools/gen_casos_de_uso.py
"""

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SAIDA = ROOT / "casos-de-uso"
BUILD = ROOT / "build"

# medidas do desenho, em pixels
ATOR_L, ATOR_A = 40, 70
CASO_L, CASO_A = 210, 64

# Cada pacote: codigo, nome, fronteira do sistema, atores e casos.
# O campo refs de cada caso traz os requisitos funcionais que ele atende.
PACOTES = [
    {
        "codigo": "PA",
        "nome": "Acesso e administração",
        "arquivo": "PA-acesso-e-administracao",
        "largura": 1060,
        "altura": 520,
        "fronteira": {"x": 250, "y": 40, "largura": 470, "altura": 420},
        "atores": [
            {"id": "usuario", "nome": "Usuário do sistema", "x": 70, "y": 100},
            {"id": "dono", "nome": "Dono", "x": 70, "y": 240},
            {"id": "google", "nome": "Conta Google", "x": 830, "y": 100},
            {"id": "email", "nome": "Serviço de e-mail e mensagem", "x": 830, "y": 320},
        ],
        "casos": [
            {"id": "uc01", "nome": "UC01 — Autenticar no sistema",
             "refs": ["RF02"], "x": 330, "y": 90},
            {"id": "uc02", "nome": "UC02 — Manter usuários e perfis",
             "refs": ["RF01"], "x": 330, "y": 210},
            {"id": "uc43", "nome": "UC43 — Notificar por e-mail e mensagem",
             "refs": ["RF24"], "x": 330, "y": 330},
        ],
        "associacoes": [
            ("usuario", "uc01"),
            ("dono", "uc02"),
            ("google", "uc01"),
            ("email", "uc43"),
        ],
        "relacoes": [],
    },
    {
        "codigo": "P1",
        "nome": "Planejamento e abertura de vendas",
        "arquivo": "P1-planejamento-e-abertura-de-vendas",
        "largura": 1150,
        "altura": 900,
        "fronteira": {"x": 250, "y": 40, "largura": 560, "altura": 820},
        "atores": [
            {"id": "dono", "nome": "Dono", "x": 70, "y": 180},
            {"id": "socio", "nome": "Sócio", "x": 70, "y": 420},
            {"id": "administrativo", "nome": "Administrativo", "x": 70, "y": 620},
            {"id": "tempo", "nome": "Tempo", "x": 920, "y": 100},
            {"id": "email", "nome": "Serviço de e-mail e mensagem", "x": 920, "y": 600},
        ],
        "casos": [
            {"id": "uc03", "nome": "UC03 — Consultar agenda e pré-reservar data",
             "refs": ["RF26"], "x": 290, "y": 80},
            {"id": "uc04", "nome": "UC04 — Manter locais e montagens",
             "refs": ["RF04"], "x": 290, "y": 190},
            {"id": "uc05", "nome": "UC05 — Registrar contratos, cachês e fornecedores",
             "refs": ["RF20"], "x": 290, "y": 300},
            {"id": "uc06", "nome": "UC06 — Cadastrar show",
             "refs": ["RF05"], "x": 290, "y": 410},
            {"id": "uc08", "nome": "UC08 — Configurar lotes e preços",
             "refs": ["RF07"], "x": 290, "y": 520},
            {"id": "uc09", "nome": "UC09 — Distribuir ingressos por canal",
             "refs": ["RF27"], "x": 290, "y": 630},
            {"id": "uc10", "nome": "UC10 — Definir cotas da lista de convidados",
             "refs": ["RF28"], "x": 290, "y": 740},
            {"id": "uc07", "nome": "UC07 — Manter sessões do show",
             "refs": ["RF06"], "x": 550, "y": 410},
            {"id": "uc11", "nome": "UC11 — Abrir vendas do show",
             "refs": ["RF08", "RF09"], "x": 550, "y": 580},
            {"id": "uc12", "nome": "UC12 — Verificar pendências para abertura",
             "refs": ["RF08"], "x": 550, "y": 720},
        ],
        "associacoes": [
            ("dono", "uc03"),
            ("dono", "uc04"),
            ("dono", "uc05"),
            ("dono", "uc06"),
            ("dono", "uc09"),
            ("dono", "uc10"),
            ("dono", "uc11"),
            ("socio", "uc05"),
            ("socio", "uc08"),
            ("administrativo", "uc05"),
            ("tempo", "uc03"),
            ("tempo", "uc08"),
            ("email", "uc11"),
        ],
        "relacoes": [
            ("uc06", "uc07", "include"),
            ("uc11", "uc12", "include"),
        ],
    },
    {
        "codigo": "P2",
        "nome": "Venda de ingressos nos canais",
        "arquivo": "P2-venda-de-ingressos-nos-canais",
        "largura": 1120,
        "altura": 780,
        "fronteira": {"x": 250, "y": 40, "largura": 540, "altura": 700},
        "atores": [
            {"id": "cliente", "nome": "Cliente", "x": 70, "y": 200},
            {"id": "socio", "nome": "Sócio", "x": 70, "y": 470},
            {"id": "loja", "nome": "Loja parceira", "x": 70, "y": 600},
            {"id": "provedor", "nome": "Provedor de pagamento", "x": 900, "y": 230},
            {"id": "email", "nome": "Serviço de e-mail e mensagem", "x": 900, "y": 390},
            {"id": "tempo", "nome": "Tempo", "x": 900, "y": 110},
        ],
        "casos": [
            {"id": "uc13", "nome": "UC13 — Consultar agenda pública e página do show",
             "refs": ["RF09"], "x": 290, "y": 70},
            {"id": "uc14", "nome": "UC14 — Comprar ingresso online",
             "refs": ["RF10", "RF11"], "x": 290, "y": 200},
            {"id": "uc16", "nome": "UC16 — Aplicar cupom de desconto",
             "refs": ["RF14"], "x": 290, "y": 330},
            {"id": "uc17", "nome": "UC17 — Comprar meia-entrada",
             "refs": ["RF13"], "x": 290, "y": 430},
            {"id": "uc19", "nome": "UC19 — Manter cupons de desconto",
             "refs": ["RF14"], "x": 290, "y": 540},
            {"id": "uc20", "nome": "UC20 — Vender ingresso pela loja parceira",
             "refs": ["RF29"], "x": 290, "y": 640},
            {"id": "uc15", "nome": "UC15 — Reservar ingressos por quinze minutos",
             "refs": ["RF10"], "x": 550, "y": 120},
            {"id": "uc18", "nome": "UC18 — Emitir ingresso com QR Code",
             "refs": ["RF12"], "x": 550, "y": 390},
        ],
        # associacao ator - caso de uso
        "associacoes": [
            ("cliente", "uc13"),
            ("cliente", "uc14"),
            ("socio", "uc19"),
            ("loja", "uc20"),
            ("provedor", "uc14"),
            ("email", "uc18"),
            ("tempo", "uc15"),
        ],
        # relacionamentos entre casos: (origem, destino, tipo)
        "relacoes": [
            ("uc14", "uc15", "include"),
            ("uc14", "uc18", "include"),
            ("uc20", "uc18", "include"),
            ("uc16", "uc14", "extend"),
            ("uc17", "uc14", "extend"),
        ],
    },
    {
        "codigo": "P3",
        "nome": "Cancelamento, remarcação e reembolso",
        "arquivo": "P3-cancelamento-remarcacao-e-reembolso",
        "largura": 1120,
        "altura": 680,
        "fronteira": {"x": 250, "y": 40, "largura": 540, "altura": 580},
        "atores": [
            {"id": "cliente", "nome": "Cliente", "x": 70, "y": 90},
            {"id": "bilheteria", "nome": "Bilheteria", "x": 70, "y": 230},
            {"id": "dono", "nome": "Dono", "x": 70, "y": 370},
            {"id": "socio", "nome": "Sócio", "x": 70, "y": 500},
            {"id": "provedor", "nome": "Provedor de pagamento", "x": 890, "y": 260},
            {"id": "email", "nome": "Serviço de e-mail e mensagem", "x": 890, "y": 480},
        ],
        "casos": [
            {"id": "uc21", "nome": "UC21 — Solicitar cancelamento da compra",
             "refs": ["RF15"], "x": 290, "y": 80},
            {"id": "uc22", "nome": "UC22 — Registrar cancelamento no atendimento",
             "refs": ["RF15"], "x": 290, "y": 200},
            {"id": "uc23", "nome": "UC23 — Analisar pedido fora da política",
             "refs": ["RF15"], "x": 290, "y": 330},
            {"id": "uc25", "nome": "UC25 — Remarcar ou cancelar show",
             "refs": ["RF31"], "x": 290, "y": 470},
            {"id": "uc24", "nome": "UC24 — Devolver valor ao comprador",
             "refs": ["RF15"], "x": 540, "y": 250},
        ],
        "associacoes": [
            ("cliente", "uc21"),
            ("bilheteria", "uc22"),
            ("dono", "uc23"),
            ("dono", "uc25"),
            ("socio", "uc23"),
            ("socio", "uc25"),
            ("provedor", "uc24"),
            ("email", "uc25"),
        ],
        "relacoes": [
            ("uc21", "uc24", "include"),
            ("uc22", "uc24", "include"),
            ("uc25", "uc24", "include"),
            ("uc23", "uc21", "extend"),
            ("uc23", "uc22", "extend"),
        ],
    },
    {
        "codigo": "P4",
        "nome": "Entrada do público no dia do show",
        "arquivo": "P4-entrada-do-publico-no-dia-do-show",
        "largura": 1120,
        "altura": 820,
        "fronteira": {"x": 250, "y": 40, "largura": 540, "altura": 720},
        "atores": [
            {"id": "portaria", "nome": "Portaria", "x": 70, "y": 160},
            {"id": "bilheteria", "nome": "Bilheteria", "x": 70, "y": 430},
            {"id": "cliente", "nome": "Cliente", "x": 70, "y": 610},
            {"id": "email", "nome": "Serviço de e-mail e mensagem", "x": 890, "y": 600},
        ],
        "casos": [
            {"id": "uc26", "nome": "UC26 — Preparar operação offline da portaria",
             "refs": ["RF18"], "x": 290, "y": 80},
            {"id": "uc27", "nome": "UC27 — Validar ingresso na entrada",
             "refs": ["RF17"], "x": 290, "y": 200},
            {"id": "uc29", "nome": "UC29 — Registrar entrada de convidado",
             "refs": ["RF28"], "x": 290, "y": 320},
            {"id": "uc31", "nome": "UC31 — Vender ingresso na porta",
             "refs": ["RF30"], "x": 290, "y": 460},
            {"id": "uc32", "nome": "UC32 — Nomear e transferir ingresso",
             "refs": ["RF16"], "x": 290, "y": 600},
            {"id": "uc28", "nome": "UC28 — Conferir meia-entrada na porta",
             "refs": ["RF13"], "x": 540, "y": 190},
            {"id": "uc30", "nome": "UC30 — Controlar lotação em tempo real",
             "refs": ["RF32"], "x": 540, "y": 400},
        ],
        "associacoes": [
            ("portaria", "uc26"),
            ("portaria", "uc27"),
            ("portaria", "uc29"),
            ("bilheteria", "uc31"),
            ("bilheteria", "uc30"),
            ("cliente", "uc32"),
            ("email", "uc32"),
        ],
        "relacoes": [
            ("uc27", "uc30", "include"),
            ("uc29", "uc30", "include"),
            ("uc31", "uc30", "include"),
            ("uc28", "uc27", "extend"),
        ],
    },
    {
        "codigo": "P5",
        "nome": "Produção do show",
        "arquivo": "P5-producao-do-show",
        "largura": 1120,
        "altura": 700,
        "fronteira": {"x": 250, "y": 40, "largura": 540, "altura": 600},
        "atores": [
            {"id": "dono", "nome": "Dono", "x": 70, "y": 90},
            {"id": "socio", "nome": "Sócio", "x": 70, "y": 260},
            {"id": "administrativo", "nome": "Administrativo", "x": 70, "y": 490},
            {"id": "equipe", "nome": "Equipe", "x": 890, "y": 100},
            {"id": "email", "nome": "Serviço de e-mail e mensagem", "x": 890, "y": 380},
        ],
        "casos": [
            {"id": "uc33", "nome": "UC33 — Montar escala da equipe",
             "refs": ["RF19"], "x": 290, "y": 90},
            {"id": "uc35", "nome": "UC35 — Montar cronograma do dia",
             "refs": ["RF21"], "x": 290, "y": 230},
            {"id": "uc36", "nome": "UC36 — Registrar ocorrências do show",
             "refs": ["RF23"], "x": 290, "y": 370},
            {"id": "uc37", "nome": "UC37 — Lançar despesas e pagamentos da noite",
             "refs": ["RF33"], "x": 290, "y": 510},
            {"id": "uc34", "nome": "UC34 — Confirmar convite da escala",
             "refs": ["RF19"], "x": 550, "y": 90},
        ],
        "associacoes": [
            ("dono", "uc33"),
            ("socio", "uc33"),
            ("socio", "uc35"),
            ("socio", "uc36"),
            ("socio", "uc37"),
            ("administrativo", "uc37"),
            ("equipe", "uc34"),
            ("email", "uc33"),
        ],
        "relacoes": [],
    },
    {
        "codigo": "P6",
        "nome": "Fechamento financeiro do show",
        "arquivo": "P6-fechamento-financeiro-do-show",
        "largura": 1120,
        "altura": 700,
        "fronteira": {"x": 250, "y": 40, "largura": 540, "altura": 600},
        "atores": [
            {"id": "bilheteria", "nome": "Bilheteria", "x": 70, "y": 90},
            {"id": "socio", "nome": "Sócio", "x": 70, "y": 240},
            {"id": "dono", "nome": "Dono", "x": 70, "y": 390},
            {"id": "administrativo", "nome": "Administrativo", "x": 70, "y": 520},
        ],
        "casos": [
            {"id": "uc38", "nome": "UC38 — Fechar caixa da bilheteria",
             "refs": ["RF30"], "x": 290, "y": 90},
            {"id": "uc39", "nome": "UC39 — Calcular acerto da loja parceira",
             "refs": ["RF29"], "x": 290, "y": 230},
            {"id": "uc40", "nome": "UC40 — Consultar resultado financeiro do show",
             "refs": ["RF22"], "x": 290, "y": 370},
            {"id": "uc42", "nome": "UC42 — Consultar relatórios e exportar",
             "refs": ["RF23", "RF25"], "x": 290, "y": 510},
            {"id": "uc41", "nome": "UC41 — Fechar show e congelar valores",
             "refs": ["RF22"], "x": 550, "y": 160},
        ],
        "associacoes": [
            ("bilheteria", "uc38"),
            ("socio", "uc39"),
            ("socio", "uc40"),
            ("socio", "uc41"),
            ("socio", "uc42"),
            ("dono", "uc40"),
            ("dono", "uc41"),
            ("dono", "uc42"),
            ("administrativo", "uc42"),
        ],
        "relacoes": [
            ("uc41", "uc38", "include"),
            ("uc41", "uc39", "include"),
        ],
    },
]


def caso(pacote, ident):
    for c in pacote["casos"]:
        if c["id"] == ident:
            return c
    raise KeyError(ident)


def ator(pacote, ident):
    for a in pacote["atores"]:
        if a["id"] == ident:
            return a
    raise KeyError(ident)


def centro_caso(c):
    return c["x"] + CASO_L / 2, c["y"] + CASO_A / 2


def centro_ator(a):
    return a["x"] + ATOR_L / 2, a["y"] + ATOR_A / 2


# ---------------------------------------------------------------- draw.io

def drawio(pacote):
    """Monta o XML mxGraph que o draw.io abre."""
    celulas = []

    f = pacote["fronteira"]
    celulas.append(
        '<mxCell id="fronteira" value="{}" '
        'style="rounded=0;whiteSpace=wrap;html=1;verticalAlign=top;fillColor=none;'
        'fontSize=14;fontStyle=1" vertex="1" parent="1">'
        '<mxGeometry x="{}" y="{}" width="{}" height="{}" as="geometry"/></mxCell>'.format(
            html.escape("Palco — " + pacote["codigo"] + " " + pacote["nome"]),
            f["x"], f["y"], f["largura"], f["altura"])
    )

    for a in pacote["atores"]:
        celulas.append(
            '<mxCell id="{}" value="{}" '
            'style="shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;'
            'html=1;outlineConnect=0;" vertex="1" parent="1">'
            '<mxGeometry x="{}" y="{}" width="{}" height="{}" as="geometry"/></mxCell>'.format(
                a["id"], html.escape(a["nome"]), a["x"], a["y"], ATOR_L, ATOR_A)
        )

    for c in pacote["casos"]:
        celulas.append(
            '<mxCell id="{}" value="{}" '
            'style="ellipse;whiteSpace=wrap;html=1;fontSize=11;" vertex="1" parent="1">'
            '<mxGeometry x="{}" y="{}" width="{}" height="{}" as="geometry"/></mxCell>'.format(
                c["id"], html.escape(c["nome"]), c["x"], c["y"], CASO_L, CASO_A)
        )

    for i, (origem, destino) in enumerate(pacote["associacoes"]):
        celulas.append(
            '<mxCell id="assoc{}" style="endArrow=none;html=1;rounded=0;" '
            'edge="1" parent="1" source="{}" target="{}">'
            '<mxGeometry relative="1" as="geometry"/></mxCell>'.format(i, origem, destino)
        )

    for i, (origem, destino, tipo) in enumerate(pacote["relacoes"]):
        celulas.append(
            '<mxCell id="rel{}" value="&lt;&lt;{}&gt;&gt;" '
            'style="endArrow=open;endFill=0;dashed=1;html=1;rounded=0;fontSize=10;" '
            'edge="1" parent="1" source="{}" target="{}">'
            '<mxGeometry relative="1" as="geometry"/></mxCell>'.format(i, tipo, origem, destino)
        )

    return (
        '<mxfile host="app.diagrams.net">'
        '<diagram name="{} {}" id="{}">'
        '<mxGraphModel dx="{}" dy="{}" grid="1" gridSize="10" page="1" '
        'pageWidth="1169" pageHeight="826" math="0" shadow="0">'
        '<root><mxCell id="0"/><mxCell id="1" parent="0"/>{}</root>'
        '</mxGraphModel></diagram></mxfile>'.format(
            pacote["codigo"], html.escape(pacote["nome"]), pacote["codigo"],
            pacote["largura"], pacote["altura"], "".join(celulas))
    )


# -------------------------------------------------------------------- svg

def quebrar(texto, largura=26):
    """Quebra o rotulo em linhas que cabem dentro da elipse."""
    linhas, atual = [], ""
    for palavra in texto.split():
        teste = (atual + " " + palavra).strip()
        if len(teste) > largura and atual:
            linhas.append(atual)
            atual = palavra
        else:
            atual = teste
    if atual:
        linhas.append(atual)
    return linhas


def boneco_svg(a):
    """Desenha o ator: cabeca, tronco, bracos, pernas e nome embaixo."""
    x, y = a["x"] + ATOR_L / 2, a["y"]
    partes = [
        '<circle cx="{}" cy="{}" r="9" fill="#ffffff" stroke="#1f2933" stroke-width="2"/>'.format(x, y + 10),
        '<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#1f2933" stroke-width="2"/>'.format(x, y + 19, x, y + 45),
        '<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#1f2933" stroke-width="2"/>'.format(x - 16, y + 28, x + 16, y + 28),
        '<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#1f2933" stroke-width="2"/>'.format(x, y + 45, x - 14, y + 66),
        '<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#1f2933" stroke-width="2"/>'.format(x, y + 45, x + 14, y + 66),
    ]
    linhas = quebrar(a["nome"], 16)
    for i, linha in enumerate(linhas):
        partes.append(
            '<text x="{}" y="{}" text-anchor="middle" font-family="Segoe UI, Arial" '
            'font-size="12" fill="#1f2933">{}</text>'.format(x, y + 84 + i * 14, html.escape(linha))
        )
    return "".join(partes)


def aresta_svg(x1, y1, x2, y2, tipo=None):
    if tipo is None:
        return ('<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#1f2933" '
                'stroke-width="1.4"/>'.format(x1, y1, x2, y2))
    meio_x, meio_y = (x1 + x2) / 2, (y1 + y2) / 2
    return (
        '<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="#1f2933" stroke-width="1.4" '
        'stroke-dasharray="7 5" marker-end="url(#seta)"/>'
        '<text x="{}" y="{}" text-anchor="middle" font-family="Segoe UI, Arial" '
        'font-size="11" fill="#1f2933">&lt;&lt;{}&gt;&gt;</text>'.format(
            x1, y1, x2, y2, meio_x, meio_y - 6, tipo)
    )


def svg(pacote):
    partes = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="{}" height="{}" '
        'viewBox="0 0 {} {}">'.format(pacote["largura"], pacote["altura"],
                                      pacote["largura"], pacote["altura"]),
        '<defs><marker id="seta" markerWidth="10" markerHeight="10" refX="9" refY="3" '
        'orient="auto"><path d="M0,0 L9,3 L0,6" fill="none" stroke="#1f2933" '
        'stroke-width="1.4"/></marker></defs>',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
    ]

    f = pacote["fronteira"]
    partes.append(
        '<rect x="{}" y="{}" width="{}" height="{}" fill="none" stroke="#1f2933" '
        'stroke-width="1.6"/>'.format(f["x"], f["y"], f["largura"], f["altura"]))
    partes.append(
        '<text x="{}" y="{}" text-anchor="middle" font-family="Segoe UI, Arial" '
        'font-size="14" font-weight="600" fill="#1f2933">{}</text>'.format(
            f["x"] + f["largura"] / 2, f["y"] + 24,
            html.escape("Palco — " + pacote["codigo"] + " " + pacote["nome"])))

    # arestas primeiro, para ficarem atras das figuras
    for origem, destino in pacote["associacoes"]:
        ax, ay = centro_ator(ator(pacote, origem))
        cx, cy = centro_caso(caso(pacote, destino))
        partes.append(aresta_svg(ax, ay, cx, cy))

    for origem, destino, tipo in pacote["relacoes"]:
        ox, oy = centro_caso(caso(pacote, origem))
        dx, dy = centro_caso(caso(pacote, destino))
        partes.append(aresta_svg(ox, oy, dx, dy, tipo))

    for a in pacote["atores"]:
        partes.append(boneco_svg(a))

    for c in pacote["casos"]:
        cx, cy = centro_caso(c)
        partes.append(
            '<ellipse cx="{}" cy="{}" rx="{}" ry="{}" fill="#ffffff" stroke="#1f2933" '
            'stroke-width="1.6"/>'.format(cx, cy, CASO_L / 2, CASO_A / 2))
        linhas = quebrar(c["nome"], 26)
        topo = cy - (len(linhas) - 1) * 7
        for i, linha in enumerate(linhas):
            partes.append(
                '<text x="{}" y="{}" text-anchor="middle" font-family="Segoe UI, Arial" '
                'font-size="11" fill="#1f2933">{}</text>'.format(cx, topo + i * 14 + 4,
                                                                 html.escape(linha)))

    partes.append("</svg>")
    return "".join(partes)


def main():
    SAIDA.mkdir(exist_ok=True)
    BUILD.mkdir(exist_ok=True)
    for pacote in PACOTES:
        nome = pacote["arquivo"]
        arquivo = SAIDA / (nome + ".drawio")
        arquivo.write_text(drawio(pacote), encoding="utf-8")
        previa = BUILD / (nome + ".svg")
        previa.write_text(svg(pacote), encoding="utf-8")
        print("{}: {} atores, {} casos, {} relacoes".format(
            arquivo.name, len(pacote["atores"]), len(pacote["casos"]),
            len(pacote["associacoes"]) + len(pacote["relacoes"])))


main()
