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

RESUMO = {
    "P1": (
        "Vai da chegada de uma produtora à plataforma até o evento no ar, pronto para vender. "
        "Concentra os cadastros de base, local, evento, sessões e lotes, e passa por duas "
        "aprovações do administrador, uma do cadastro da produtora e outra do evento em si. "
        "As duas aprovações têm caminho de retorno, porque na prática a maior parte dos eventos "
        "volta para ajuste antes de ser publicada."
    ),
    "P2": (
        "É o processo de maior volume do sistema e o que sustenta a receita. A reserva temporária "
        "existe para impedir que dois compradores fechem o mesmo assento e, ao mesmo tempo, para "
        "devolver o estoque quando a compra é abandonada no meio. O provedor de pagamento aparece "
        "como raia própria porque é um ator externo, com tempo de resposta fora do controle da equipe."
    ),
    "P3": (
        "Separa o que pode ser resolvido por regra do que precisa de decisão humana. Dentro da "
        "janela de sete dias e a mais de quarenta e oito horas da sessão, o cancelamento é "
        "automático. Fora dela, o financeiro analisa e pode recusar com justificativa. Nos dois "
        "caminhos o ingresso é invalidado antes de qualquer estorno, para não abrir a porta de "
        "usar o ingresso e receber o dinheiro de volta."
    ),
    "P4": (
        "Roda no dia do evento, sob pressão de fila e com rede instável. A validação acontece no "
        "próprio aparelho, contra a lista baixada antes da abertura dos portões, e a sincronização "
        "com o servidor é posterior. O desvio de três saídas reflete o que o operador vê na tela: "
        "libera, nega ou confere documento."
    ),
    "P5": (
        "Cobre a operação em torno do show, do fechamento das atrações à execução do dia. O laço "
        "sobre o cronograma é a parte mais usada na prática, porque atraso de passagem de som "
        "empurra todo o resto e a produção precisa ver o efeito na hora."
    ),
    "P6": (
        "Começa por tempo, e não por ação de usuário, quando encerra a janela de reembolso da "
        "sessão. Essa espera é deliberada: fechar antes significaria repassar ao produtor dinheiro "
        "que ainda pode ser estornado. O laço de correção devolve o fluxo à consolidação de custos, "
        "que é onde os erros de lançamento aparecem."
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

    todos = {f"RF{i:02d}" for i in range(1, 26)}
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
        out.append("Nenhum. Todos os 25 requisitos funcionais aparecem em ao menos um processo.")
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
