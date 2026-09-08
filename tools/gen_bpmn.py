"""Gerador dos diagramas BPMN 2.0 do Sistema Palco.

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

PRODUTOR = "Produtor"
ADMIN = "Administrador da plataforma"
SISTEMA = "Sistema Palco"
CLIENTE = "Cliente"
PSP = "Provedor de pagamento"
FIN = "Financeiro"
PORTARIA = "Portaria"
APP = "Aplicativo de portaria"
PUBLICO = "Público"
EQUIPE = "Equipe e fornecedores"

P1 = Process(
    "P1", "Criação e publicação de evento", "Plataforma Palco",
    [PRODUTOR, ADMIN, SISTEMA],
    [
        Node("P1_start", "start", "Produtor quer vender ingressos", PRODUTOR, 0),
        Node("P1_t1", "user", "Cadastrar produtora e dados de recebimento", PRODUTOR, 1, refs="RF03"),
        Node("P1_t2", "user", "Analisar cadastro da produtora", ADMIN, 2, refs="RF03"),
        Node("P1_g1", "gateway", "Cadastro aprovado?", ADMIN, 3),
        Node("P1_t3", "user", "Corrigir dados cadastrais", PRODUTOR, 3, row=1, refs="RF03"),
        Node("P1_t4", "user", "Cadastrar local e setores", PRODUTOR, 4, refs="RF04"),
        Node("P1_t5", "user", "Cadastrar evento", PRODUTOR, 5, refs="RF05"),
        Node("P1_t6", "user", "Cadastrar sessões", PRODUTOR, 6, refs="RF06"),
        Node("P1_t7", "user", "Configurar lotes e preços", PRODUTOR, 7, refs="RF07"),
        Node("P1_t8", "user", "Submeter evento à análise", PRODUTOR, 8, refs="RF08"),
        Node("P1_t9", "user", "Analisar evento", ADMIN, 9, refs="RF08"),
        Node("P1_g2", "gateway", "Evento aprovado?", ADMIN, 10),
        Node("P1_t10", "user", "Ajustar evento conforme parecer", PRODUTOR, 10, row=1, refs="RF08"),
        Node("P1_t11", "service", "Publicar evento na vitrine", SISTEMA, 11, refs="RF08, RF09"),
        Node("P1_t12", "service", "Notificar produtor da publicação", SISTEMA, 12, refs="RF24"),
        Node("P1_end", "end", "Evento publicado", SISTEMA, 13),
    ],
    [
        ("P1_start", "P1_t1", ""),
        ("P1_t1", "P1_t2", ""),
        ("P1_t2", "P1_g1", ""),
        ("P1_g1", "P1_t3", "não"),
        ("P1_t3", "P1_t2", ""),
        ("P1_g1", "P1_t4", "sim"),
        ("P1_t4", "P1_t5", ""),
        ("P1_t5", "P1_t6", ""),
        ("P1_t6", "P1_t7", ""),
        ("P1_t7", "P1_t8", ""),
        ("P1_t8", "P1_t9", ""),
        ("P1_t9", "P1_g2", ""),
        ("P1_g2", "P1_t10", "não"),
        ("P1_t10", "P1_t8", ""),
        ("P1_g2", "P1_t11", "sim"),
        ("P1_t11", "P1_t12", ""),
        ("P1_t12", "P1_end", ""),
    ],
)

P2 = Process(
    "P2", "Venda de ingresso online", "Bilheteria Palco",
    [CLIENTE, SISTEMA, PSP],
    [
        Node("P2_start", "start", "Cliente procura um show", CLIENTE, 0),
        Node("P2_t1", "user", "Pesquisar eventos na vitrine", CLIENTE, 1, refs="RF09"),
        Node("P2_t2", "user", "Selecionar sessão, setor e quantidade", CLIENTE, 2, refs="RF10"),
        Node("P2_t3", "service", "Reservar ingressos por 15 minutos", SISTEMA, 3, refs="RF10"),
        Node("P2_t4", "user", "Informar dados e aplicar cupom", CLIENTE, 4, refs="RF11, RF14"),
        Node("P2_g0", "gateway", "Meia-entrada?", CLIENTE, 5),
        Node("P2_t5", "user", "Anexar comprovante do benefício", CLIENTE, 5, row=1, refs="RF13"),
        Node("P2_t6", "service", "Enviar cobrança ao provedor", SISTEMA, 6, refs="RF11"),
        Node("P2_t7", "service", "Processar pagamento", PSP, 7, refs="RF11"),
        Node("P2_g1", "gateway", "Pagamento aprovado?", SISTEMA, 8),
        Node("P2_t8", "service", "Emitir ingressos com QR Code", SISTEMA, 9, refs="RF12"),
        Node("P2_t9", "service", "Liberar reserva e avisar recusa", SISTEMA, 9, row=1, refs="RF10, RF24"),
        Node("P2_t10", "service", "Enviar ingressos por e-mail", SISTEMA, 10, refs="RF24"),
        Node("P2_end2", "end", "Compra não concluída", SISTEMA, 10, row=1),
        Node("P2_end1", "end", "Compra concluída", CLIENTE, 11),
    ],
    [
        ("P2_start", "P2_t1", ""),
        ("P2_t1", "P2_t2", ""),
        ("P2_t2", "P2_t3", ""),
        ("P2_t3", "P2_t4", ""),
        ("P2_t4", "P2_g0", ""),
        ("P2_g0", "P2_t5", "sim"),
        ("P2_t5", "P2_t6", ""),
        ("P2_g0", "P2_t6", "não"),
        ("P2_t6", "P2_t7", ""),
        ("P2_t7", "P2_g1", ""),
        ("P2_g1", "P2_t8", "aprovado"),
        ("P2_g1", "P2_t9", "recusado"),
        ("P2_t8", "P2_t10", ""),
        ("P2_t9", "P2_end2", ""),
        ("P2_t10", "P2_end1", ""),
    ],
)

P3 = Process(
    "P3", "Cancelamento e reembolso", "Pós-venda Palco",
    [CLIENTE, SISTEMA, FIN, PSP],
    [
        Node("P3_start", "start", "Cliente desiste da compra", CLIENTE, 0),
        Node("P3_t1", "user", "Solicitar cancelamento", CLIENTE, 1, refs="RF15"),
        Node("P3_t2", "service", "Verificar política de cancelamento", SISTEMA, 2, refs="RF15"),
        Node("P3_g1", "gateway", "Dentro da janela automática?", SISTEMA, 3),
        Node("P3_t3", "user", "Analisar solicitação", FIN, 4, refs="RF15"),
        Node("P3_g2", "gateway", "Reembolso aprovado?", FIN, 5),
        Node("P3_t4", "user", "Registrar recusa com justificativa", FIN, 6, refs="RF15"),
        Node("P3_t5", "service", "Invalidar ingressos e devolver estoque", SISTEMA, 6, refs="RF15, RF12"),
        Node("P3_t6", "service", "Notificar cliente da recusa", SISTEMA, 7, row=1, refs="RF24"),
        Node("P3_t7", "service", "Solicitar estorno ao provedor", SISTEMA, 7, refs="RF15"),
        Node("P3_t8", "service", "Processar estorno", PSP, 8, refs="RF15"),
        Node("P3_end2", "end", "Solicitação recusada", CLIENTE, 8, row=1),
        Node("P3_t9", "service", "Registrar reembolso e notificar cliente", SISTEMA, 9, refs="RF22, RF24"),
        Node("P3_end1", "end", "Reembolso concluído", CLIENTE, 10),
    ],
    [
        ("P3_start", "P3_t1", ""),
        ("P3_t1", "P3_t2", ""),
        ("P3_t2", "P3_g1", ""),
        ("P3_g1", "P3_t3", "não"),
        ("P3_t3", "P3_g2", ""),
        ("P3_g2", "P3_t4", "não"),
        ("P3_t4", "P3_t6", ""),
        ("P3_t6", "P3_end2", ""),
        ("P3_g1", "P3_t5", "sim"),
        ("P3_g2", "P3_t5", "sim"),
        ("P3_t5", "P3_t7", ""),
        ("P3_t7", "P3_t8", ""),
        ("P3_t8", "P3_t9", ""),
        ("P3_t9", "P3_end1", ""),
    ],
)

P4 = Process(
    "P4", "Check-in e controle de acesso", "Portaria do evento",
    [PUBLICO, PORTARIA, APP],
    [
        Node("P4_start", "start", "Portões abertos", PORTARIA, 0),
        Node("P4_t1", "service", "Baixar lista de ingressos da sessão", APP, 1, refs="RF18"),
        Node("P4_t2", "manual", "Apresentar ingresso digital", PUBLICO, 2, refs="RF12"),
        Node("P4_t3", "user", "Ler QR Code do ingresso", PORTARIA, 3, refs="RF17"),
        Node("P4_t4", "service", "Validar assinatura e situação", APP, 4, refs="RF17, RF12"),
        Node("P4_g1", "gateway", "Resultado da validação", APP, 5),
        Node("P4_t5", "user", "Conferir documento do portador", PORTARIA, 6, refs="RF13, RF16"),
        Node("P4_g2", "gateway", "Documento confere?", PORTARIA, 7),
        Node("P4_t6", "service", "Registrar check-in e liberar acesso", APP, 8, refs="RF17"),
        Node("P4_t7", "user", "Registrar recusa e orientar bilheteria", PORTARIA, 8, row=1, refs="RF17"),
        Node("P4_t8", "service", "Sincronizar check-ins com o servidor", APP, 9, refs="RF18"),
        Node("P4_end2", "end", "Acesso negado", PUBLICO, 9, row=1),
        Node("P4_end1", "end", "Público no evento", PUBLICO, 10),
    ],
    [
        ("P4_start", "P4_t1", ""),
        ("P4_t1", "P4_t2", ""),
        ("P4_t2", "P4_t3", ""),
        ("P4_t3", "P4_t4", ""),
        ("P4_t4", "P4_g1", ""),
        ("P4_g1", "P4_t5", "nominal ou meia"),
        ("P4_g1", "P4_t6", "válido"),
        ("P4_g1", "P4_t7", "inválido ou usado"),
        ("P4_t5", "P4_g2", ""),
        ("P4_g2", "P4_t6", "sim"),
        ("P4_g2", "P4_t7", "não"),
        ("P4_t6", "P4_t8", ""),
        ("P4_t8", "P4_end1", ""),
        ("P4_t7", "P4_end2", ""),
    ],
)

P5 = Process(
    "P5", "Produção e realização do evento", "Produção do evento",
    [PRODUTOR, EQUIPE, SISTEMA],
    [
        Node("P5_start", "start", "Evento publicado", PRODUTOR, 0),
        Node("P5_t1", "user", "Cadastrar atrações e fornecedores", PRODUTOR, 1, refs="RF20"),
        Node("P5_t2", "user", "Registrar contratos e cachês", PRODUTOR, 2, refs="RF20"),
        Node("P5_t3", "user", "Montar escala da equipe", PRODUTOR, 3, refs="RF19"),
        Node("P5_t4", "user", "Montar cronograma do dia", PRODUTOR, 4, refs="RF21"),
        Node("P5_t5", "service", "Notificar equipe e fornecedores", SISTEMA, 5, refs="RF24"),
        Node("P5_t6", "manual", "Executar montagem e passagem de som", EQUIPE, 6, refs="RF21"),
        Node("P5_t7", "user", "Registrar presença da equipe", PRODUTOR, 7, refs="RF19"),
        Node("P5_t8", "user", "Marcar etapas concluídas", PRODUTOR, 8, refs="RF21"),
        Node("P5_g1", "gateway", "Etapa atrasada?", SISTEMA, 9),
        Node("P5_t9", "service", "Recalcular etapas seguintes", SISTEMA, 10, row=1, refs="RF21"),
        Node("P5_t10", "manual", "Realizar o show", EQUIPE, 10, refs="RF21"),
        Node("P5_t11", "user", "Encerrar sessão e registrar ocorrências", PRODUTOR, 11, refs="RF23"),
        Node("P5_end", "end", "Evento realizado", PRODUTOR, 12),
    ],
    [
        ("P5_start", "P5_t1", ""),
        ("P5_t1", "P5_t2", ""),
        ("P5_t2", "P5_t3", ""),
        ("P5_t3", "P5_t4", ""),
        ("P5_t4", "P5_t5", ""),
        ("P5_t5", "P5_t6", ""),
        ("P5_t6", "P5_t7", ""),
        ("P5_t7", "P5_t8", ""),
        ("P5_t8", "P5_g1", ""),
        ("P5_g1", "P5_t9", "sim"),
        ("P5_t9", "P5_t8", ""),
        ("P5_g1", "P5_t10", "não"),
        ("P5_t10", "P5_t11", ""),
        ("P5_t11", "P5_end", ""),
    ],
)

P6 = Process(
    "P6", "Fechamento financeiro e repasse", "Financeiro Palco",
    [SISTEMA, FIN, PRODUTOR],
    [
        Node("P6_start", "timerStart", "Fim da janela de reembolso", SISTEMA, 0),
        Node("P6_t1", "service", "Consolidar receita, taxas e descontos", SISTEMA, 1, refs="RF22"),
        Node("P6_t2", "service", "Consolidar custos do evento", SISTEMA, 2, refs="RF22, RF19, RF20"),
        Node("P6_t3", "user", "Conferir demonstrativo da sessão", FIN, 3, refs="RF22"),
        Node("P6_g1", "gateway", "Valores conferem?", FIN, 4),
        Node("P6_t4", "user", "Corrigir lançamentos", FIN, 5, row=1, refs="RF22"),
        Node("P6_t5", "user", "Fechar sessão e congelar valores", FIN, 5, refs="RF22"),
        Node("P6_t6", "service", "Gerar repasse ao produtor", SISTEMA, 6, refs="RF22, RF03"),
        Node("P6_t7", "service", "Notificar produtor do fechamento", SISTEMA, 7, refs="RF24"),
        Node("P6_t8", "user", "Consultar relatórios e exportar", PRODUTOR, 8, refs="RF23"),
        Node("P6_end", "end", "Fechamento concluído", PRODUTOR, 9),
    ],
    [
        ("P6_start", "P6_t1", ""),
        ("P6_t1", "P6_t2", ""),
        ("P6_t2", "P6_t3", ""),
        ("P6_t3", "P6_g1", ""),
        ("P6_g1", "P6_t4", "não"),
        ("P6_t4", "P6_t2", ""),
        ("P6_g1", "P6_t5", "sim"),
        ("P6_t5", "P6_t6", ""),
        ("P6_t6", "P6_t7", ""),
        ("P6_t7", "P6_t8", ""),
        ("P6_t8", "P6_end", ""),
    ],
)

PROCESSES = [P1, P2, P3, P4, P5, P6]

FILENAMES = {
    "P1": "P1-criacao-e-publicacao-de-evento.bpmn",
    "P2": "P2-venda-de-ingresso-online.bpmn",
    "P3": "P3-cancelamento-e-reembolso.bpmn",
    "P4": "P4-checkin-e-controle-de-acesso.bpmn",
    "P5": "P5-producao-e-realizacao-do-evento.bpmn",
    "P6": "P6-fechamento-financeiro-e-repasse.bpmn",
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
