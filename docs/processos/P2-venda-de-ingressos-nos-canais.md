# P2 — Venda de ingressos nos canais

**Pool:** Bilheteria Cena Livre  
**Raias:** Cliente, Loja parceira, Sistema Palco, Provedor de pagamento  
**Arquivo BPMN:** [`bpmn/P2-venda-de-ingressos-nos-canais.bpmn`](../../bpmn/P2-venda-de-ingressos-nos-canais.bpmn)

Reúne num único estoque os dois canais que vendem antes do dia do show: a página de vendas divulgada no Instagram e a loja parceira. Na entrevista, o comprovante chegava como print no WhatsApp e a loja informava as vendas dias depois. Aqui o pagamento online é confirmado pelo provedor, sem print, e a loja registra cada venda na hora, com nome e CPF, baixando da própria cota. Os dois caminhos terminam no mesmo ingresso com QR Code.

## Atividades e requisitos atendidos

| Elemento | Tipo | Raia | Requisitos |
|---|---|---|---|
| Cliente quer comprar ingresso | Evento de início | Cliente | — |
| Canal de compra | Desvio exclusivo | Cliente | — |
| Abrir página do show pelo link | Tarefa de usuário | Cliente | RF09 |
| Registrar venda com nome e CPF | Tarefa de usuário | Loja parceira | RF29 |
| Baixar da cota do parceiro | Tarefa de sistema | Sistema Palco | RF27, RF29 |
| Escolher tipo e quantidade | Tarefa de usuário | Cliente | RF10 |
| Reservar ingressos por 15 minutos | Tarefa de sistema | Sistema Palco | RF10, RF27 |
| Meia-entrada? | Desvio exclusivo | Cliente | — |
| Informar categoria e anexar comprovante | Tarefa de usuário | Cliente | RF13 |
| Aplicar cupom e pagar com Pix ou cartão | Tarefa de usuário | Cliente | RF11, RF14 |
| Processar pagamento | Tarefa de sistema | Provedor de pagamento | RF11 |
| Pagamento aprovado? | Desvio exclusivo | Sistema Palco | — |
| Liberar reserva e avisar cliente | Tarefa de sistema | Sistema Palco | RF10, RF24 |
| Compra não concluída | Evento de fim | Sistema Palco | — |
| Emitir ingresso com QR Code | Tarefa de sistema | Sistema Palco | RF12 |
| Enviar ingresso por e-mail | Tarefa de sistema | Sistema Palco | RF12, RF24 |
| Ingresso entregue | Evento de fim | Cliente | — |

## Fluxo

```mermaid
flowchart LR
  subgraph L0["Cliente"]
    direction LR
    P2_start([Cliente quer comprar ingresso])
    P2_g0{Canal de compra}
    P2_t1[Abrir página do show pelo link]
    P2_t2[Escolher tipo e quantidade]
    P2_g1{Meia-entrada?}
    P2_t4[Informar categoria e anexar comprovante]
    P2_t5[Aplicar cupom e pagar com Pix ou cartão]
    P2_end1([Ingresso entregue])
  end
  subgraph L1["Loja parceira"]
    direction LR
    P2_p1[Registrar venda com nome e CPF]
  end
  subgraph L2["Sistema Palco"]
    direction LR
    P2_p2[Baixar da cota do parceiro]
    P2_t3[Reservar ingressos por 15 minutos]
    P2_g2{Pagamento aprovado?}
    P2_t7[Liberar reserva e avisar cliente]
    P2_end2([Compra não concluída])
    P2_t8[Emitir ingresso com QR Code]
    P2_t9[Enviar ingresso por e-mail]
  end
  subgraph L3["Provedor de pagamento"]
    direction LR
    P2_t6[Processar pagamento]
  end
  P2_start --> P2_g0
  P2_g0 -->|online| P2_t1
  P2_g0 -->|loja parceira| P2_p1
  P2_p1 --> P2_p2
  P2_p2 --> P2_t8
  P2_t1 --> P2_t2
  P2_t2 --> P2_t3
  P2_t3 --> P2_g1
  P2_g1 -->|sim| P2_t4
  P2_t4 --> P2_t5
  P2_g1 -->|não| P2_t5
  P2_t5 --> P2_t6
  P2_t6 --> P2_g2
  P2_g2 -->|recusado| P2_t7
  P2_t7 --> P2_end2
  P2_g2 -->|aprovado| P2_t8
  P2_t8 --> P2_t9
  P2_t9 --> P2_end1
```
