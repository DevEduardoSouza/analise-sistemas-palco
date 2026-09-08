# P3 — Cancelamento e reembolso

**Pool:** Pós-venda Palco  
**Raias:** Cliente, Sistema Palco, Financeiro, Provedor de pagamento  
**Arquivo BPMN:** [`bpmn/P3-cancelamento-e-reembolso.bpmn`](../../bpmn/P3-cancelamento-e-reembolso.bpmn)

Separa o que pode ser resolvido por regra do que precisa de decisão humana. Dentro da janela de sete dias e a mais de quarenta e oito horas da sessão, o cancelamento é automático. Fora dela, o financeiro analisa e pode recusar com justificativa. Nos dois caminhos o ingresso é invalidado antes de qualquer estorno, para não abrir a porta de usar o ingresso e receber o dinheiro de volta.

## Atividades e requisitos atendidos

| Elemento | Tipo | Raia | Requisitos |
|---|---|---|---|
| Cliente desiste da compra | Evento de início | Cliente | — |
| Solicitar cancelamento | Tarefa de usuário | Cliente | RF15 |
| Verificar política de cancelamento | Tarefa de sistema | Sistema Palco | RF15 |
| Dentro da janela automática? | Desvio exclusivo | Sistema Palco | — |
| Analisar solicitação | Tarefa de usuário | Financeiro | RF15 |
| Reembolso aprovado? | Desvio exclusivo | Financeiro | — |
| Registrar recusa com justificativa | Tarefa de usuário | Financeiro | RF15 |
| Invalidar ingressos e devolver estoque | Tarefa de sistema | Sistema Palco | RF15, RF12 |
| Notificar cliente da recusa | Tarefa de sistema | Sistema Palco | RF24 |
| Solicitar estorno ao provedor | Tarefa de sistema | Sistema Palco | RF15 |
| Processar estorno | Tarefa de sistema | Provedor de pagamento | RF15 |
| Solicitação recusada | Evento de fim | Cliente | — |
| Registrar reembolso e notificar cliente | Tarefa de sistema | Sistema Palco | RF22, RF24 |
| Reembolso concluído | Evento de fim | Cliente | — |

## Fluxo

```mermaid
flowchart LR
  subgraph L0["Cliente"]
    direction LR
    P3_start([Cliente desiste da compra])
    P3_t1[Solicitar cancelamento]
    P3_end2([Solicitação recusada])
    P3_end1([Reembolso concluído])
  end
  subgraph L1["Sistema Palco"]
    direction LR
    P3_t2[Verificar política de cancelamento]
    P3_g1{Dentro da janela automática?}
    P3_t5[Invalidar ingressos e devolver estoque]
    P3_t6[Notificar cliente da recusa]
    P3_t7[Solicitar estorno ao provedor]
    P3_t9[Registrar reembolso e notificar cliente]
  end
  subgraph L2["Financeiro"]
    direction LR
    P3_t3[Analisar solicitação]
    P3_g2{Reembolso aprovado?}
    P3_t4[Registrar recusa com justificativa]
  end
  subgraph L3["Provedor de pagamento"]
    direction LR
    P3_t8[Processar estorno]
  end
  P3_start --> P3_t1
  P3_t1 --> P3_t2
  P3_t2 --> P3_g1
  P3_g1 -->|não| P3_t3
  P3_t3 --> P3_g2
  P3_g2 -->|não| P3_t4
  P3_t4 --> P3_t6
  P3_t6 --> P3_end2
  P3_g1 -->|sim| P3_t5
  P3_g2 -->|sim| P3_t5
  P3_t5 --> P3_t7
  P3_t7 --> P3_t8
  P3_t8 --> P3_t9
  P3_t9 --> P3_end1
```
