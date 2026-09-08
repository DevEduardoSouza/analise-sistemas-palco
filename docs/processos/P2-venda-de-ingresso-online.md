# P2 — Venda de ingresso online

**Pool:** Bilheteria Palco  
**Raias:** Cliente, Sistema Palco, Provedor de pagamento  
**Arquivo BPMN:** [`bpmn/P2-venda-de-ingresso-online.bpmn`](../../bpmn/P2-venda-de-ingresso-online.bpmn)

É o processo de maior volume do sistema e o que sustenta a receita. A reserva temporária existe para impedir que dois compradores fechem o mesmo assento e, ao mesmo tempo, para devolver o estoque quando a compra é abandonada no meio. O provedor de pagamento aparece como raia própria porque é um ator externo, com tempo de resposta fora do controle da equipe.

## Atividades e requisitos atendidos

| Elemento | Tipo | Raia | Requisitos |
|---|---|---|---|
| Cliente procura um show | Evento de início | Cliente | — |
| Pesquisar eventos na vitrine | Tarefa de usuário | Cliente | RF09 |
| Selecionar sessão, setor e quantidade | Tarefa de usuário | Cliente | RF10 |
| Reservar ingressos por 15 minutos | Tarefa de sistema | Sistema Palco | RF10 |
| Informar dados e aplicar cupom | Tarefa de usuário | Cliente | RF11, RF14 |
| Meia-entrada? | Desvio exclusivo | Cliente | — |
| Anexar comprovante do benefício | Tarefa de usuário | Cliente | RF13 |
| Enviar cobrança ao provedor | Tarefa de sistema | Sistema Palco | RF11 |
| Processar pagamento | Tarefa de sistema | Provedor de pagamento | RF11 |
| Pagamento aprovado? | Desvio exclusivo | Sistema Palco | — |
| Emitir ingressos com QR Code | Tarefa de sistema | Sistema Palco | RF12 |
| Liberar reserva e avisar recusa | Tarefa de sistema | Sistema Palco | RF10, RF24 |
| Enviar ingressos por e-mail | Tarefa de sistema | Sistema Palco | RF24 |
| Compra não concluída | Evento de fim | Sistema Palco | — |
| Compra concluída | Evento de fim | Cliente | — |

## Fluxo

```mermaid
flowchart LR
  subgraph L0["Cliente"]
    direction LR
    P2_start([Cliente procura um show])
    P2_t1[Pesquisar eventos na vitrine]
    P2_t2[Selecionar sessão, setor e quantidade]
    P2_t4[Informar dados e aplicar cupom]
    P2_g0{Meia-entrada?}
    P2_t5[Anexar comprovante do benefício]
    P2_end1([Compra concluída])
  end
  subgraph L1["Sistema Palco"]
    direction LR
    P2_t3[Reservar ingressos por 15 minutos]
    P2_t6[Enviar cobrança ao provedor]
    P2_g1{Pagamento aprovado?}
    P2_t8[Emitir ingressos com QR Code]
    P2_t9[Liberar reserva e avisar recusa]
    P2_t10[Enviar ingressos por e-mail]
    P2_end2([Compra não concluída])
  end
  subgraph L2["Provedor de pagamento"]
    direction LR
    P2_t7[Processar pagamento]
  end
  P2_start --> P2_t1
  P2_t1 --> P2_t2
  P2_t2 --> P2_t3
  P2_t3 --> P2_t4
  P2_t4 --> P2_g0
  P2_g0 -->|sim| P2_t5
  P2_t5 --> P2_t6
  P2_g0 -->|não| P2_t6
  P2_t6 --> P2_t7
  P2_t7 --> P2_g1
  P2_g1 -->|aprovado| P2_t8
  P2_g1 -->|recusado| P2_t9
  P2_t8 --> P2_t10
  P2_t9 --> P2_end2
  P2_t10 --> P2_end1
```
