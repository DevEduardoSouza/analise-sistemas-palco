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
        "codigo": "P2",
        "nome": "Venda de ingressos nos canais",
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
        nome = "{}-{}".format(pacote["codigo"],
                              pacote["nome"].lower().replace(" ", "-"))
        arquivo = SAIDA / (nome + ".drawio")
        arquivo.write_text(drawio(pacote), encoding="utf-8")
        previa = BUILD / (nome + ".svg")
        previa.write_text(svg(pacote), encoding="utf-8")
        print("{}: {} atores, {} casos, {} relacoes".format(
            arquivo.name, len(pacote["atores"]), len(pacote["casos"]),
            len(pacote["associacoes"]) + len(pacote["relacoes"])))


main()
