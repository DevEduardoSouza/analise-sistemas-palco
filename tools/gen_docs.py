"""Gera a documentacao dos processos e a matriz de rastreabilidade.

Le a mesma definicao usada para desenhar os diagramas (gen_bpmn.PROCESSES),
de modo que a documentacao nunca fique fora de sincronia com os arquivos .bpmn.

Uso:
    python tools/gen_docs.py
"""

import re
from pathlib import Path

from gen_bpmn import PROCESSES, FILENAMES, BPMN_TAG

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

TIPO = {
    "start": "Evento de início",
    "timerStart": "Evento de início por tempo",
    "end": "Evento de fim",
    "task": "Tarefa",
    "user": "Tarefa de usuário",
    "service": "Tarefa de sistema",
    "manual": "Tarefa manual",
    "gateway": "Desvio exclusivo",
    "parallel": "Desvio paralelo",
}

# Requisitos retirados depois da entrevista com o dono da Cena Livre. O codigo
# nao volta a ser usado.
RETIRADOS = {"RF03"}
ULTIMO_RF = 33

RESUMO = {
    "P1": (
        "Vai da proposta de uma banda até a venda aberta em todos os canais. Nasce da queixa do "
        "dono de que a agenda fica num caderno e de que a divisão de ingressos entre Instagram, "
        "loja parceira e porta é feita no chute. Por isso a data é pré-reservada antes da "
        "negociação do cachê, e a venda só abre depois que o sistema confirma contrato, montagem, "
        "cotas por canal e lotes. O sócio aparece em raia própria porque é ele quem decide cachê e preço."
    ),
    "P2": (
        "Reúne num único estoque os dois canais que vendem antes do dia do show: a página de vendas "
        "divulgada no Instagram e a loja parceira. Na entrevista, o comprovante chegava como print "
        "no WhatsApp e a loja informava as vendas dias depois. Aqui o pagamento online é confirmado "
        "pelo provedor, sem print, e a loja registra cada venda na hora, com nome e CPF, baixando "
        "da própria cota. Os dois caminhos terminam no mesmo ingresso com QR Code."
    ),
    "P3": (
        "Tem dois gatilhos. O cliente que desiste da compra e a banda que adia ou cancela o show, "
        "situação relatada pelo dono. Na remarcação o sistema avisa todos os compradores e abre um "
        "prazo em que a devolução é automática. A devolução segue o canal de origem: estorno pelo "
        "provedor para compras online e devolução pela bilheteria ou pela loja para as demais, "
        "sempre para o comprador identificado na venda, o que evita devolver à pessoa errada."
    ),
    "P4": (
        "Roda na porta da casa, sob fila e com internet instável. O aplicativo baixa ingressos e lista "
        "de convidados antes da abertura e valida sem rede. Quem chega sem ingresso só compra na "
        "porta se ainda houver lugar, porque a lotação é contada a cada entrada, resposta direta ao "
        "episódio em que a casa lotou com gente de ingresso na mão. O desvio de três saídas reflete "
        "o que o porteiro vê: libera, nega ou confere documento."
    ),
    "P5": (
        "Cobre a equipe e o dia do show. Hoje a escala é combinada por mensagem e há quem esqueça "
        "o compromisso, então o convite sai pelo sistema e cada pessoa confirma, com laço de "
        "substituição quando alguém não confirma. Os pagamentos feitos em dinheiro durante a noite "
        "são lançados no mesmo dia, para não se perderem até o fechamento."
    ),
    "P6": (
        "Substitui a reunião na cozinha do sócio, dias depois do show, com caderno e recibos. Logo "
        "após o fechamento do caixa da porta o sistema mostra um resultado prévio, a terceira "
        "prioridade do dono. O fechamento definitivo espera a conferência das despesas e o acerto "
        "da loja parceira, que repassa as vendas descontada a comissão combinada."
    ),
}


def mermaid(proc):
    shape = {
        "start": "([{}])", "timerStart": "([{}])", "end": "([{}])",
        "gateway": "{{{}}}", "parallel": "{{{}}}",
    }
    linhas = ["```mermaid", "flowchart LR"]
    for i, lane in enumerate(proc.lanes):
        linhas.append(f'  subgraph L{i}["{lane}"]')
        linhas.append("    direction LR")
        for nid in proc.order:
            n = proc.nodes[nid]
            if n.lane != lane:
                continue
            molde = shape.get(n.kind, "[{}]")
            linhas.append(f'    {nid}{molde.format(n.name)}')
        linhas.append("  end")
    for s, d, label in proc.flows:
        seta = f' -->|{label}| ' if label else " --> "
        linhas.append(f"  {s}{seta}{d}")
    linhas.append("```")
    return "\n".join(linhas)


def doc_processo(proc):
    arq = FILENAMES[proc.key]
    out = [f"# {proc.key} — {proc.name}", ""]
    out.append(f"**Pool:** {proc.pool}  ")
    out.append("**Raias:** " + ", ".join(proc.lanes) + "  ")
    out.append(f"**Arquivo BPMN:** [`bpmn/{arq}`](../../bpmn/{arq})")
    out.append("")
    out.append(RESUMO[proc.key])
    out.append("")
    out.append("## Atividades e requisitos atendidos")
    out.append("")
    out.append("| Elemento | Tipo | Raia | Requisitos |")
    out.append("|---|---|---|---|")
    for nid in proc.order:
        n = proc.nodes[nid]
        out.append(f"| {n.name} | {TIPO[n.kind]} | {n.lane} | {n.refs or '—'} |")
    out.append("")
    out.append("## Fluxo")
    out.append("")
    out.append(mermaid(proc))
    out.append("")
    return "\n".join(out)


def rastreabilidade():
    rf_para = {}
    for proc in PROCESSES:
        for nid in proc.order:
            n = proc.nodes[nid]
            for rf in re.findall(r"RF\d{2}", n.refs):
                rf_para.setdefault(rf, []).append((proc.key, n.name))

    out = ["# Matriz de rastreabilidade", ""]
    out.append(
        "Liga cada requisito funcional às atividades dos diagramas BPMN em que ele aparece. "
        "É a evidência de coerência entre a modelagem dos processos e os requisitos mapeados, "
        "exigida na entrega. A tabela é gerada a partir da mesma definição que desenha os "
        "diagramas, em `tools/gen_bpmn.py`, e por isso não pode divergir deles."
    )
    out.append("")
    out.append("| Requisito | Processos | Atividades |")
    out.append("|---|---|---|")
    for rf in sorted(rf_para):
        pares = rf_para[rf]
        procs = sorted({p for p, _ in pares})
        ativ = "; ".join(f"{p}: {nome}" for p, nome in pares)
        out.append(f"| {rf} | {', '.join(procs)} | {ativ} |")
    out.append("")

    todos = {f"RF{i:02d}" for i in range(1, ULTIMO_RF + 1)} - RETIRADOS
    sem_processo = sorted(todos - set(rf_para))
    out.append("## Requisitos sem atividade correspondente")
    out.append("")
    if sem_processo:
        out.append(
            "Os requisitos abaixo são funcionalidades de apoio, consultadas ou acionadas de "
            "dentro das telas, sem passo próprio na modelagem de processo."
        )
        out.append("")
        for rf in sem_processo:
            out.append(f"- {rf}")
    else:
        out.append(f"Nenhum. Todos os {len(todos)} requisitos funcionais ativos aparecem em ao menos um processo.")
    out.append("")
    out.append("## Requisitos retirados")
    out.append("")
    out.append(
        "O RF03, cadastro de produtora com aprovação por administrador, foi retirado depois da "
        "entrevista com o dono da Cena Livre, porque o sistema atende uma única casa de shows e "
        "não uma plataforma de várias produtoras. O código não é reaproveitado."
    )
    out.append("")
    return "\n".join(out)


def main():
    dir_proc = DOCS / "processos"
    dir_proc.mkdir(parents=True, exist_ok=True)
    for proc in PROCESSES:
        nome = FILENAMES[proc.key].replace(".bpmn", ".md")
        (dir_proc / nome).write_text(doc_processo(proc), encoding="utf-8")
        print("docs/processos/" + nome)
    (DOCS / "rastreabilidade.md").write_text(rastreabilidade(), encoding="utf-8")
    print("docs/rastreabilidade.md")


if __name__ == "__main__":
    main()
