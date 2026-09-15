# P3 — Cancelamento, remarcação e reembolso

**Pool:** Pós-venda Cena Livre  
**Raias:** Cliente, Dono e sócio, Bilheteria, Sistema Palco, Provedor de pagamento  
**Arquivo BPMN:** [`bpmn/P3-cancelamento-remarcacao-e-reembolso.bpmn`](../../bpmn/P3-cancelamento-remarcacao-e-reembolso.bpmn)

Tem dois gatilhos. O cliente que desiste da compra e a banda que adia ou cancela o show, situação relatada pelo dono. Na remarcação o sistema avisa todos os compradores e abre um prazo em que a devolução é automática. A devolução segue o canal de origem: estorno pelo provedor para compras online e devolução pela bilheteria ou pela loja para as demais, sempre para o comprador identificado na venda, o que evita devolver à pessoa errada.

## Atividades e requisitos atendidos

| Elemento | Tipo | Raia | Requisitos |
|---|---|---|---|
| Cliente pede devolução | Evento de início | Cliente | — |
| Banda adia ou cancela o show | Evento de início | Dono e sócio | — |
| Remarcar data ou cancelar o show | Tarefa de usuário | Dono e sócio | RF31, RF26 |
| Avisar compradores e abrir prazo de reembolso | Tarefa de sistema | Sistema Palco | RF31, RF24 |
| Compradores avisados | Evento de fim | Sistema Palco | — |
| Solicitar cancelamento | Tarefa de usuário | Cliente | RF15 |
| Localizar compra e verificar política | Tarefa de sistema | Sistema Palco | RF15 |
| Direito automático? | Desvio exclusivo | Sistema Palco | — |
| Analisar pedido fora da política | Tarefa de usuário | Dono e sócio | RF15 |
| Devolução aprovada? | Desvio exclusivo | Dono e sócio | — |
| Notificar recusa com justificativa | Tarefa de sistema | Sistema Palco | RF15, RF24 |
| Pedido recusado | Evento de fim | Sistema Palco | — |
| Cancelar ingressos e devolver à cota | Tarefa de sistema | Sistema Palco | RF15, RF12, RF27 |
| Canal da compra | Desvio exclusivo | Sistema Palco | — |
| Solicitar estorno ao provedor | Tarefa de sistema | Sistema Palco | RF15 |
| Processar estorno | Tarefa de sistema | Provedor de pagamento | RF15 |
| Devolver valor ao comprador identificado | Tarefa de usuário | Bilheteria | RF15, RF29, RF30 |
| Registrar reembolso no financeiro do show | Tarefa de sistema | Sistema Palco | RF22, RF24 |
| Reembolso concluído | Evento de fim | Cliente | — |

## Fluxo

```mermaid
flowchart LR
  subgraph L0["Cliente"]
    direction LR
    P3_start([Cliente pede devolução])
    P3_t1[Solicitar cancelamento]
    P3_end1([Reembolso concluído])
  end
  subgraph L1["Dono e sócio"]
    direction LR
    P3_start2([Banda adia ou cancela o show])
    P3_r1[Remarcar data ou cancelar o show]
    P3_t3[Analisar pedido fora da política]
    P3_g2{Devolução aprovada?}
  end
  subgraph L2["Bilheteria"]
    direction LR
    P3_t8[Devolver valor ao comprador identificado]
  end
  subgraph L3["Sistema Palco"]
    direction LR
    P3_r2[Avisar compradores e abrir prazo de reembolso]
    P3_end3([Compradores avisados])
    P3_t2[Localizar compra e verificar política]
    P3_g1{Direito automático?}
    P3_t4[Notificar recusa com justificativa]
    P3_end2([Pedido recusado])
    P3_t5[Cancelar ingressos e devolver à cota]
    P3_g3{Canal da compra}
    P3_t6[Solicitar estorno ao provedor]
    P3_t9[Registrar reembolso no financeiro do show]
  end
  subgraph L4["Provedor de pagamento"]
    direction LR
    P3_t7[Processar estorno]
  end
  P3_start2 --> P3_r1
  P3_r1 --> P3_r2
  P3_r2 --> P3_end3
  P3_start --> P3_t1
  P3_t1 --> P3_t2
  P3_t2 --> P3_g1
  P3_g1 -->|não| P3_t3
  P3_t3 --> P3_g2
  P3_g2 -->|não| P3_t4
  P3_t4 --> P3_end2
  P3_g1 -->|sim| P3_t5
  P3_g2 -->|sim| P3_t5
  P3_t5 --> P3_g3
  P3_g3 -->|online| P3_t6
  P3_g3 -->|porta ou parceiro| P3_t8
  P3_t6 --> P3_t7
  P3_t7 --> P3_t9
  P3_t8 --> P3_t9
  P3_t9 --> P3_end1
```
