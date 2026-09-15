"""Gerador dos diagramas BPMN 2.0 do Sistema Palco, feito para a Cena Livre.

Produz arquivos .bpmn com Diagram Interchange (coordenadas), de modo que os
arquivos abram já desenhados no bpmn.io, Camunda Modeler e Bizagi Modeler.

Uso:
    python tools/gen_bpmn.py

Os arquivos sao gravados em bpmn/.
"""

from pathlib import Path
from xml.sax.saxutils import escape

# ---------------------------------------------------------------- layout ----

COL_W = 200          # distancia horizontal entre colunas
ROW_H = 110          # distancia vertical entre linhas dentro de uma raia
POOL_X = 160
POOL_Y = 80
LANE_HEADER = 30     # largura da faixa com o nome da raia
LANE_PAD = 120       # altura de uma raia com uma unica linha

SIZES = {
    "start": (36, 36),
    "timerStart": (36, 36),
    "end": (36, 36),
    "task": (120, 80),
    "user": (120, 80),
    "service": (120, 80),
    "manual": (120, 80),
    "gateway": (50, 50),
    "parallel": (50, 50),
}

BPMN_TAG = {
    "start": "startEvent",
    "timerStart": "startEvent",
    "end": "endEvent",
    "task": "task",
    "user": "userTask",
    "service": "serviceTask",
    "manual": "manualTask",
    "gateway": "exclusiveGateway",
    "parallel": "parallelGateway",
}


class Node:
    def __init__(self, nid, kind, name, lane, col, row=0, refs=""):
        self.id = nid
        self.kind = kind
        self.name = name
        self.lane = lane
        self.col = col
        self.row = row
        self.refs = refs          # requisitos atendidos, usados na documentacao
        self.w, self.h = SIZES[kind]
        self.cx = 0
        self.cy = 0

    @property
    def left(self):
        return self.cx - self.w / 2

    @property
    def right(self):
        return self.cx + self.w / 2

    @property
    def top(self):
        return self.cy - self.h / 2

    @property
    def bottom(self):
        return self.cy + self.h / 2


class Process:
    def __init__(self, key, name, pool, lanes, nodes, flows):
        self.key = key
        self.name = name
        self.pool = pool
        self.lanes = lanes
        self.nodes = {n.id: n for n in nodes}
        self.order = [n.id for n in nodes]
        self.flows = flows        # (origem, destino, rotulo)


def layout(proc):
    """Calcula centro de cada no e as dimensoes de raias e pool."""
    max_row = {lane: 0 for lane in proc.lanes}
    for n in proc.nodes.values():
        max_row[n.lane] = max(max_row[n.lane], n.row)

    lane_geo = {}
    y = POOL_Y
    for lane in proc.lanes:
        h = LANE_PAD + ROW_H * max_row[lane]
        lane_geo[lane] = (y, h)
        y += h
    pool_h = y - POOL_Y

    max_col = max(n.col for n in proc.nodes.values())
    pool_w = LANE_HEADER + (max_col + 1) * COL_W

    for n in proc.nodes.values():
        lane_y = lane_geo[n.lane][0]
        n.cx = POOL_X + LANE_HEADER + COL_W / 2 + n.col * COL_W
        n.cy = lane_y + 60 + n.row * ROW_H

    return lane_geo, pool_w, pool_h


def waypoints(src, dst):
    """Roteia a seta entre dois nos com no maximo um cotovelo duplo."""
    if dst.col > src.col:                                   # adiante
        if abs(src.cy - dst.cy) < 1:
            return [(src.right, src.cy), (dst.left, dst.cy)]
        mid = (src.right + dst.left) / 2
        return [(src.right, src.cy), (mid, src.cy),
                (mid, dst.cy), (dst.left, dst.cy)]
    if dst.col < src.col:                                   # retorno
        if abs(src.cy - dst.cy) < 1:
            return [(src.left, src.cy), (dst.right, dst.cy)]
        mid = (dst.right + src.left) / 2
        return [(src.left, src.cy), (mid, src.cy),
                (mid, dst.cy), (dst.right, dst.cy)]
    # mesma coluna: liga verticalmente
    if dst.cy > src.cy:
        return [(src.cx, src.bottom), (dst.cx, dst.top)]
    return [(src.cx, src.top), (dst.cx, dst.bottom)]


def label_pos(pts):
    """Posiciona o rotulo da seta sem cobrir o nome do no de origem."""
    if len(pts) == 2:
        (x0, y0), (x1, y1) = pts
        if abs(x0 - x1) < 1:                # trecho vertical: rotulo ao lado
            return x0 + 12, (y0 + y1) / 2 - 10
        return (x0 + x1) / 2 - 40, (y0 + y1) / 2 - 24
    # com cotovelo: rotulo ao lado do trecho vertical, para nao colidir com
    # o rotulo da outra saida do mesmo desvio
    (_, y1), (x2, y2) = pts[1], pts[2]
    return x2 + 8, (y1 + y2) / 2 - 10


# ------------------------------------------------------------------ xml ----

def build_xml(proc):
    lane_geo, pool_w, pool_h = layout(proc)
    pid = "Process_" + proc.key
    out = []
    a = out.append

    a('<?xml version="1.0" encoding="UTF-8"?>')
    a('<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL"'
      ' xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI"'
      ' xmlns:dc="http://www.omg.org/spec/DD/20100524/DC"'
      ' xmlns:di="http://www.omg.org/spec/DD/20100524/DI"'
      f' id="Definitions_{proc.key}" targetNamespace="http://palco.ifba/bpmn"'
      ' exporter="gen_bpmn.py" exporterVersion="1.0">')

    a(f'  <bpmn:collaboration id="Collaboration_{proc.key}">')
    a(f'    <bpmn:participant id="Participant_{proc.key}" '
      f'name="{escape(proc.pool)}" processRef="{pid}" />')
    a('  </bpmn:collaboration>')

    a(f'  <bpmn:process id="{pid}" name="{escape(proc.name)}" isExecutable="false">')

    a(f'    <bpmn:laneSet id="LaneSet_{proc.key}">')
    for i, lane in enumerate(proc.lanes):
        a(f'      <bpmn:lane id="Lane_{proc.key}_{i}" name="{escape(lane)}">')
        for nid in proc.order:
            if proc.nodes[nid].lane == lane:
                a(f'        <bpmn:flowNodeRef>{nid}</bpmn:flowNodeRef>')
        a('      </bpmn:lane>')
    a('    </bpmn:laneSet>')

    incoming, outgoing = {}, {}
    for i, (s, d, _label) in enumerate(proc.flows):
        fid = f'Flow_{proc.key}_{i}'
        outgoing.setdefault(s, []).append(fid)
        incoming.setdefault(d, []).append(fid)

    for nid in proc.order:
        n = proc.nodes[nid]
        tag = BPMN_TAG[n.kind]
        a(f'    <bpmn:{tag} id="{nid}" name="{escape(n.name)}">')
        for fid in incoming.get(nid, []):
            a(f'      <bpmn:incoming>{fid}</bpmn:incoming>')
        for fid in outgoing.get(nid, []):
            a(f'      <bpmn:outgoing>{fid}</bpmn:outgoing>')
        if n.kind == "timerStart":
            a(f'      <bpmn:timerEventDefinition id="Timer_{nid}" />')
        a(f'    </bpmn:{tag}>')

    for i, (s, d, label) in enumerate(proc.flows):
        fid = f'Flow_{proc.key}_{i}'
        nm = f' name="{escape(label)}"' if label else ''
        a(f'    <bpmn:sequenceFlow id="{fid}"{nm} sourceRef="{s}" targetRef="{d}" />')

    a('  </bpmn:process>')

    a(f'  <bpmndi:BPMNDiagram id="Diagram_{proc.key}">')
    a(f'    <bpmndi:BPMNPlane id="Plane_{proc.key}" '
      f'bpmnElement="Collaboration_{proc.key}">')
    a(f'      <bpmndi:BPMNShape id="Participant_{proc.key}_di" '
      f'bpmnElement="Participant_{proc.key}" isHorizontal="true">')
    a(f'        <dc:Bounds x="{POOL_X}" y="{POOL_Y}" '
      f'width="{pool_w}" height="{pool_h}" />')
    a('      </bpmndi:BPMNShape>')

    for i, lane in enumerate(proc.lanes):
        ly, lh = lane_geo[lane]
        a(f'      <bpmndi:BPMNShape id="Lane_{proc.key}_{i}_di" '
          f'bpmnElement="Lane_{proc.key}_{i}" isHorizontal="true">')
        a(f'        <dc:Bounds x="{POOL_X + LANE_HEADER}" y="{ly}" '
          f'width="{pool_w - LANE_HEADER}" height="{lh}" />')
        a('      </bpmndi:BPMNShape>')

    for nid in proc.order:
        n = proc.nodes[nid]
        marker = ' isMarkerVisible="true"' if n.kind == "gateway" else ''
        a(f'      <bpmndi:BPMNShape id="{nid}_di" bpmnElement="{nid}"{marker}>')
        a(f'        <dc:Bounds x="{n.left:g}" y="{n.top:g}" '
          f'width="{n.w}" height="{n.h}" />')
        if n.kind in ("start", "timerStart", "end", "gateway", "parallel"):
            a('        <bpmndi:BPMNLabel>')
            a(f'          <dc:Bounds x="{n.cx - 55:g}" y="{n.bottom + 6:g}" '
              'width="110" height="30" />')
            a('        </bpmndi:BPMNLabel>')
        a('      </bpmndi:BPMNShape>')

    for i, (s, d, label) in enumerate(proc.flows):
        fid = f'Flow_{proc.key}_{i}'
        pts = waypoints(proc.nodes[s], proc.nodes[d])
        a(f'      <bpmndi:BPMNEdge id="{fid}_di" bpmnElement="{fid}">')
        for x, y in pts:
            a(f'        <di:waypoint x="{x:g}" y="{y:g}" />')
        if label:
            lx, ly = label_pos(pts)
            a('        <bpmndi:BPMNLabel>')
            a(f'          <dc:Bounds x="{lx:g}" y="{ly:g}" '
              'width="80" height="20" />')
            a('        </bpmndi:BPMNLabel>')
        a('      </bpmndi:BPMNEdge>')

    a('    </bpmndi:BPMNPlane>')
    a('  </bpmndi:BPMNDiagram>')
    a('</bpmn:definitions>')
    return "\n".join(out) + "\n"


# ------------------------------------------------------------ processos ----

DONO = "Dono"
SOCIO = "Sócio"
DONO_SOCIO = "Dono e sócio"
ADM = "Administrativo"
SISTEMA = "Sistema Palco"
CLIENTE = "Cliente"
PARCEIRO = "Loja parceira"
BILHETERIA = "Bilheteria"
PSP = "Provedor de pagamento"
PORTARIA = "Portaria"
APP = "Aplicativo de portaria"
PUBLICO = "Público"
EQUIPE = "Equipe e fornecedores"

# Os processos foram modelados a partir da entrevista com o dono da Cena Livre
# (docs/entrevista.md). Os codigos Axx nos comentarios apontam o problema
# relatado que cada trecho resolve.

P1 = Process(
    "P1", "Planejamento do show e abertura de vendas", "Cena Livre",
    [DONO, SOCIO, SISTEMA],
    [
        Node("P1_start", "start", "Proposta de show recebida", DONO, 0),
        Node("P1_t1", "user", "Consultar agenda e pré-reservar data", DONO, 1, refs="RF26"),
        Node("P1_g0", "gateway", "Data livre?", DONO, 2),
        Node("P1_t2", "user", "Propor outra data à banda", DONO, 2, row=1, refs="RF26"),
        Node("P1_t3", "user", "Avaliar cachê e preço viável", SOCIO, 3, refs="RF20"),
        Node("P1_g1", "gateway", "Show viável?", SOCIO, 4),
        Node("P1_t4", "service", "Liberar pré-reserva da data", SISTEMA, 5, refs="RF26"),
        Node("P1_end2", "end", "Show descartado", SISTEMA, 6),
        Node("P1_t5", "user", "Registrar contrato, cachê e sinal", DONO, 5, refs="RF20, RF33"),
        Node("P1_t6", "user", "Cadastrar show e sessões", DONO, 6, refs="RF05, RF06, RF26"),
        Node("P1_t7", "user", "Definir local e montagem", DONO, 7, refs="RF04"),
        Node("P1_t8", "user", "Distribuir ingressos por canal", DONO, 8, refs="RF27"),
        Node("P1_t9", "user", "Configurar lotes e preços", SOCIO, 9, refs="RF07"),
        Node("P1_t10", "user", "Definir cotas da lista de convidados", DONO, 10, refs="RF28"),
        Node("P1_t11", "service", "Verificar pendências para abrir vendas", SISTEMA, 11, refs="RF08"),
        Node("P1_g2", "gateway", "Tudo pronto?", SISTEMA, 12),
        Node("P1_t12", "user", "Completar pendências", DONO, 12, row=1, refs="RF08"),
        Node("P1_t13", "service", "Publicar página de vendas do show", SISTEMA, 13, refs="RF08, RF09"),
        Node("P1_t14", "service", "Liberar cotas à loja parceira e à bilheteria", SISTEMA, 14, refs="RF27, RF29, RF24"),
        Node("P1_end", "end", "Vendas abertas", SISTEMA, 15),
    ],
    [
        ("P1_start", "P1_t1", ""),
        ("P1_t1", "P1_g0", ""),
        ("P1_g0", "P1_t2", "não"),
        ("P1_t2", "P1_t1", ""),
        ("P1_g0", "P1_t3", "sim"),
        ("P1_t3", "P1_g1", ""),
        ("P1_g1", "P1_t4", "não"),
        ("P1_t4", "P1_end2", ""),
        ("P1_g1", "P1_t5", "sim"),
        ("P1_t5", "P1_t6", ""),
        ("P1_t6", "P1_t7", ""),
        ("P1_t7", "P1_t8", ""),
        ("P1_t8", "P1_t9", ""),
        ("P1_t9", "P1_t10", ""),
        ("P1_t10", "P1_t11", ""),
        ("P1_t11", "P1_g2", ""),
        ("P1_g2", "P1_t12", "não"),
        ("P1_t12", "P1_t11", ""),
        ("P1_g2", "P1_t13", "sim"),
        ("P1_t13", "P1_t14", ""),
        ("P1_t14", "P1_end", ""),
    ],
)

P2 = Process(
    "P2", "Venda de ingressos nos canais", "Bilheteria Cena Livre",
    [CLIENTE, PARCEIRO, SISTEMA, PSP],
    [
        Node("P2_start", "start", "Cliente quer comprar ingresso", CLIENTE, 0),
        Node("P2_g0", "gateway", "Canal de compra", CLIENTE, 1),
        Node("P2_t1", "user", "Abrir página do show pelo link", CLIENTE, 2, refs="RF09"),
        Node("P2_p1", "user", "Registrar venda com nome e CPF", PARCEIRO, 2, refs="RF29"),
        Node("P2_p2", "service", "Baixar da cota do parceiro", SISTEMA, 3, row=1, refs="RF27, RF29"),
        Node("P2_t2", "user", "Escolher tipo e quantidade", CLIENTE, 3, refs="RF10"),
        Node("P2_t3", "service", "Reservar ingressos por 15 minutos", SISTEMA, 4, refs="RF10, RF27"),
        Node("P2_g1", "gateway", "Meia-entrada?", CLIENTE, 5),
        Node("P2_t4", "user", "Informar categoria e anexar comprovante", CLIENTE, 5, row=1, refs="RF13"),
        Node("P2_t5", "user", "Aplicar cupom e pagar com Pix ou cartão", CLIENTE, 6, refs="RF11, RF14"),
        Node("P2_t6", "service", "Processar pagamento", PSP, 7, refs="RF11"),
        Node("P2_g2", "gateway", "Pagamento aprovado?", SISTEMA, 8),
        Node("P2_t7", "service", "Liberar reserva e avisar cliente", SISTEMA, 9, refs="RF10, RF24"),
        Node("P2_end2", "end", "Compra não concluída", SISTEMA, 10),
        Node("P2_t8", "service", "Emitir ingresso com QR Code", SISTEMA, 9, row=1, refs="RF12"),
        Node("P2_t9", "service", "Enviar ingresso por e-mail", SISTEMA, 10, row=1, refs="RF12, RF24"),
        Node("P2_end1", "end", "Ingresso entregue", CLIENTE, 11),
    ],
    [
        ("P2_start", "P2_g0", ""),
        ("P2_g0", "P2_t1", "online"),
        ("P2_g0", "P2_p1", "loja parceira"),
        ("P2_p1", "P2_p2", ""),
        ("P2_p2", "P2_t8", ""),
        ("P2_t1", "P2_t2", ""),
        ("P2_t2", "P2_t3", ""),
        ("P2_t3", "P2_g1", ""),
        ("P2_g1", "P2_t4", "sim"),
        ("P2_t4", "P2_t5", ""),
        ("P2_g1", "P2_t5", "não"),
        ("P2_t5", "P2_t6", ""),
        ("P2_t6", "P2_g2", ""),
        ("P2_g2", "P2_t7", "recusado"),
        ("P2_t7", "P2_end2", ""),
        ("P2_g2", "P2_t8", "aprovado"),
        ("P2_t8", "P2_t9", ""),
        ("P2_t9", "P2_end1", ""),
    ],
)

P3 = Process(
    "P3", "Cancelamento, remarcação e reembolso", "Pós-venda Cena Livre",
    [CLIENTE, DONO_SOCIO, BILHETERIA, SISTEMA, PSP],
    [
        Node("P3_start", "start", "Cliente pede devolução", CLIENTE, 0),
        Node("P3_start2", "start", "Banda adia ou cancela o show", DONO_SOCIO, 1),
        Node("P3_r1", "user", "Remarcar data ou cancelar o show", DONO_SOCIO, 2, refs="RF31, RF26"),
        Node("P3_r2", "service", "Avisar compradores e abrir prazo de reembolso", SISTEMA, 3, row=1, refs="RF31, RF24"),
        Node("P3_end3", "end", "Compradores avisados", SISTEMA, 4, row=1),
        Node("P3_t1", "user", "Solicitar cancelamento", CLIENTE, 1, refs="RF15"),
        Node("P3_t2", "service", "Localizar compra e verificar política", SISTEMA, 2, refs="RF15"),
        Node("P3_g1", "gateway", "Direito automático?", SISTEMA, 3),
        Node("P3_t3", "user", "Analisar pedido fora da política", DONO_SOCIO, 4, refs="RF15"),
        Node("P3_g2", "gateway", "Devolução aprovada?", DONO_SOCIO, 5),
        Node("P3_t4", "service", "Notificar recusa com justificativa", SISTEMA, 6, row=1, refs="RF15, RF24"),
        Node("P3_end2", "end", "Pedido recusado", SISTEMA, 7, row=1),
        Node("P3_t5", "service", "Cancelar ingressos e devolver à cota", SISTEMA, 6, refs="RF15, RF12, RF27"),
        Node("P3_g3", "gateway", "Canal da compra", SISTEMA, 7),
        Node("P3_t6", "service", "Solicitar estorno ao provedor", SISTEMA, 8, refs="RF15"),
        Node("P3_t7", "service", "Processar estorno", PSP, 9, refs="RF15"),
        Node("P3_t8", "user", "Devolver valor ao comprador identificado", BILHETERIA, 8, refs="RF15, RF29, RF30"),
        Node("P3_t9", "service", "Registrar reembolso no financeiro do show", SISTEMA, 10, refs="RF22, RF24"),
        Node("P3_end1", "end", "Reembolso concluído", CLIENTE, 11),
    ],
    [
        ("P3_start2", "P3_r1", ""),
        ("P3_r1", "P3_r2", ""),
        ("P3_r2", "P3_end3", ""),
        ("P3_start", "P3_t1", ""),
        ("P3_t1", "P3_t2", ""),
        ("P3_t2", "P3_g1", ""),
        ("P3_g1", "P3_t3", "não"),
        ("P3_t3", "P3_g2", ""),
        ("P3_g2", "P3_t4", "não"),
        ("P3_t4", "P3_end2", ""),
        ("P3_g1", "P3_t5", "sim"),
        ("P3_g2", "P3_t5", "sim"),
        ("P3_t5", "P3_g3", ""),
        ("P3_g3", "P3_t6", "online"),
        ("P3_g3", "P3_t8", "porta ou parceiro"),
        ("P3_t6", "P3_t7", ""),
        ("P3_t7", "P3_t9", ""),
        ("P3_t8", "P3_t9", ""),
        ("P3_t9", "P3_end1", ""),
    ],
)

P4 = Process(
    "P4", "Entrada do público no dia do show", "Portaria Cena Livre",
    [PUBLICO, PORTARIA, BILHETERIA, APP],
    [
        Node("P4_start", "start", "Passagem de som concluída", PORTARIA, 0),
        Node("P4_t1", "service", "Baixar ingressos e lista de convidados", APP, 1, refs="RF18, RF28"),
        Node("P4_t2", "manual", "Apresentar ingresso ou nome na lista", PUBLICO, 2, refs="RF12, RF28"),
        Node("P4_g1", "gateway", "Tem ingresso ou convite?", PORTARIA, 3),
        Node("P4_t3", "user", "Ler QR Code ou buscar nome na lista", PORTARIA, 4, refs="RF17, RF28"),
        Node("P4_b1", "service", "Verificar lotação disponível", APP, 4, refs="RF32"),
        Node("P4_gb", "gateway", "Há lugar na casa?", BILHETERIA, 5),
        Node("P4_b2", "user", "Vender ingresso na porta", BILHETERIA, 6, refs="RF30, RF12"),
        Node("P4_end3", "end", "Casa lotada", BILHETERIA, 5, row=1),
        Node("P4_t4", "service", "Validar ingresso ou convite", APP, 7, refs="RF17, RF18"),
        Node("P4_g2", "gateway", "Resultado da validação", APP, 8),
        Node("P4_t5", "user", "Conferir documento do portador", PORTARIA, 9, refs="RF13, RF16"),
        Node("P4_g3", "gateway", "Documento confere?", PORTARIA, 10),
        Node("P4_t6", "service", "Registrar entrada e atualizar lotação", APP, 11, refs="RF17, RF32"),
        Node("P4_t7", "user", "Negar entrada e informar motivo", PORTARIA, 11, row=1, refs="RF17"),
        Node("P4_t8", "service", "Sincronizar entradas ao reconectar", APP, 12, refs="RF18"),
        Node("P4_end2", "end", "Entrada negada", PORTARIA, 12, row=1),
        Node("P4_end1", "end", "Público dentro da casa", PUBLICO, 13),
    ],
    [
        ("P4_start", "P4_t1", ""),
        ("P4_t1", "P4_t2", ""),
        ("P4_t2", "P4_g1", ""),
        ("P4_g1", "P4_t3", "sim"),
        ("P4_g1", "P4_b1", "não"),
        ("P4_b1", "P4_gb", ""),
        ("P4_gb", "P4_b2", "sim"),
        ("P4_gb", "P4_end3", "não"),
        ("P4_b2", "P4_t4", ""),
        ("P4_t3", "P4_t4", ""),
        ("P4_t4", "P4_g2", ""),
        ("P4_g2", "P4_t6", "válido"),
        ("P4_g2", "P4_t5", "meia ou nominal"),
        ("P4_g2", "P4_t7", "inválido ou já usado"),
        ("P4_t5", "P4_g3", ""),
        ("P4_g3", "P4_t6", "sim"),
        ("P4_g3", "P4_t7", "não"),
        ("P4_t6", "P4_t8", ""),
        ("P4_t8", "P4_end1", ""),
        ("P4_t7", "P4_end2", ""),
    ],
)

P5 = Process(
    "P5", "Produção do show", "Produção Cena Livre",
    [DONO, SOCIO, EQUIPE, SISTEMA],
    [
        Node("P5_start", "start", "Vendas abertas", DONO, 0),
        Node("P5_t1", "user", "Montar escala da equipe", DONO, 1, refs="RF19"),
        Node("P5_t2", "service", "Enviar convite com data, função e valor", SISTEMA, 2, refs="RF19, RF24"),
        Node("P5_t3", "user", "Confirmar disponibilidade", EQUIPE, 3, refs="RF19"),
        Node("P5_g1", "gateway", "Todos confirmaram?", SISTEMA, 4),
        Node("P5_t4", "user", "Substituir pessoa ou contratar terceirizado", DONO, 4, row=1, refs="RF19, RF20"),
        Node("P5_t5", "user", "Montar cronograma do dia", SOCIO, 5, refs="RF21"),
        Node("P5_t6", "user", "Conferir horário anunciado ao público", DONO, 6, refs="RF21, RF24"),
        Node("P5_t7", "manual", "Montar equipamento e passar o som", EQUIPE, 7, refs="RF21"),
        Node("P5_t8", "user", "Registrar presença da equipe", SOCIO, 8, refs="RF19"),
        Node("P5_t9", "manual", "Realizar o show", EQUIPE, 9, refs="RF21"),
        Node("P5_t10", "user", "Lançar pagamentos feitos na noite", SOCIO, 10, refs="RF33"),
        Node("P5_t11", "user", "Registrar ocorrências do show", DONO, 11, refs="RF23"),
        Node("P5_end", "end", "Show realizado", DONO, 12),
    ],
    [
        ("P5_start", "P5_t1", ""),
        ("P5_t1", "P5_t2", ""),
        ("P5_t2", "P5_t3", ""),
        ("P5_t3", "P5_g1", ""),
        ("P5_g1", "P5_t4", "não"),
        ("P5_t4", "P5_t1", ""),
        ("P5_g1", "P5_t5", "sim"),
        ("P5_t5", "P5_t6", ""),
        ("P5_t6", "P5_t7", ""),
        ("P5_t7", "P5_t8", ""),
        ("P5_t8", "P5_t9", ""),
        ("P5_t9", "P5_t10", ""),
        ("P5_t10", "P5_t11", ""),
        ("P5_t11", "P5_end", ""),
    ],
)

P6 = Process(
    "P6", "Fechamento financeiro do show", "Financeiro Cena Livre",
    [DONO, SOCIO, ADM, PARCEIRO, SISTEMA],
    [
        Node("P6_start", "start", "Show encerrado", SOCIO, 0),
        Node("P6_t1", "user", "Fechar caixa da bilheteria", SOCIO, 1, refs="RF30, RF33"),
        Node("P6_t2", "service", "Consolidar receitas por canal e despesas", SISTEMA, 2, refs="RF22, RF33"),
        Node("P6_t3", "service", "Exibir resultado prévio ao dono e ao sócio", SISTEMA, 3, refs="RF22"),
        Node("P6_t4", "user", "Conferir despesas e comprovantes", ADM, 4, refs="RF33"),
        Node("P6_g1", "gateway", "Falta lançamento?", ADM, 5),
        Node("P6_t5", "user", "Lançar despesa pendente", ADM, 5, row=1, refs="RF33"),
        Node("P6_t6", "service", "Calcular acerto da loja parceira", SISTEMA, 6, refs="RF29"),
        Node("P6_t7", "user", "Repassar vendas descontada a comissão", PARCEIRO, 7, refs="RF29"),
        Node("P6_t8", "user", "Confirmar recebimento do acerto", SOCIO, 8, refs="RF29, RF22"),
        Node("P6_t9", "user", "Fechar show e congelar valores", SOCIO, 9, refs="RF22"),
        Node("P6_t10", "user", "Consultar resultado e relatórios", DONO, 10, refs="RF23"),
        Node("P6_end", "end", "Show fechado", DONO, 11),
    ],
    [
        ("P6_start", "P6_t1", ""),
        ("P6_t1", "P6_t2", ""),
        ("P6_t2", "P6_t3", ""),
        ("P6_t3", "P6_t4", ""),
        ("P6_t4", "P6_g1", ""),
        ("P6_g1", "P6_t5", "sim"),
        ("P6_t5", "P6_t4", ""),
        ("P6_g1", "P6_t6", "não"),
        ("P6_t6", "P6_t7", ""),
        ("P6_t7", "P6_t8", ""),
        ("P6_t8", "P6_t9", ""),
        ("P6_t9", "P6_t10", ""),
        ("P6_t10", "P6_end", ""),
    ],
)

PROCESSES = [P1, P2, P3, P4, P5, P6]

FILENAMES = {
    "P1": "P1-planejamento-e-abertura-de-vendas.bpmn",
    "P2": "P2-venda-de-ingressos-nos-canais.bpmn",
    "P3": "P3-cancelamento-remarcacao-e-reembolso.bpmn",
    "P4": "P4-entrada-do-publico-no-dia-do-show.bpmn",
    "P5": "P5-producao-do-show.bpmn",
    "P6": "P6-fechamento-financeiro-do-show.bpmn",
}


def main():
    out_dir = Path(__file__).resolve().parent.parent / "bpmn"
    out_dir.mkdir(exist_ok=True)
    for proc in PROCESSES:
        path = out_dir / FILENAMES[proc.key]
        path.write_text(build_xml(proc), encoding="utf-8")
        print(f"{path.name}: {len(proc.nodes)} elementos, {len(proc.flows)} fluxos")


if __name__ == "__main__":
    main()
