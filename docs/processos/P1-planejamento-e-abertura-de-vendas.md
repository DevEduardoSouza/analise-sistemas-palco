# P1 — Planejamento do show e abertura de vendas

**Pool:** Cena Livre  
**Raias:** Dono, Sócio, Sistema Palco  
**Arquivo BPMN:** [`bpmn/P1-planejamento-e-abertura-de-vendas.bpmn`](../../bpmn/P1-planejamento-e-abertura-de-vendas.bpmn)

Vai da proposta de uma banda até a venda aberta em todos os canais. Nasce da queixa do dono de que a agenda fica num caderno e de que a divisão de ingressos entre Instagram, loja parceira e porta é feita no chute. Por isso a data é pré-reservada antes da negociação do cachê, e a venda só abre depois que o sistema confirma contrato, montagem, cotas por canal e lotes. O sócio aparece em raia própria porque é ele quem decide cachê e preço.

## Atividades e requisitos atendidos

| Elemento | Tipo | Raia | Requisitos |
|---|---|---|---|
| Proposta de show recebida | Evento de início | Dono | — |
| Consultar agenda e pré-reservar data | Tarefa de usuário | Dono | RF26 |
| Data livre? | Desvio exclusivo | Dono | — |
| Propor outra data à banda | Tarefa de usuário | Dono | RF26 |
| Avaliar cachê e preço viável | Tarefa de usuário | Sócio | RF20 |
| Show viável? | Desvio exclusivo | Sócio | — |
| Liberar pré-reserva da data | Tarefa de sistema | Sistema Palco | RF26 |
| Show descartado | Evento de fim | Sistema Palco | — |
| Registrar contrato, cachê e sinal | Tarefa de usuário | Dono | RF20, RF33 |
| Cadastrar show e sessões | Tarefa de usuário | Dono | RF05, RF06, RF26 |
| Definir local e montagem | Tarefa de usuário | Dono | RF04 |
| Distribuir ingressos por canal | Tarefa de usuário | Dono | RF27 |
| Configurar lotes e preços | Tarefa de usuário | Sócio | RF07 |
| Definir cotas da lista de convidados | Tarefa de usuário | Dono | RF28 |
| Verificar pendências para abrir vendas | Tarefa de sistema | Sistema Palco | RF08 |
| Tudo pronto? | Desvio exclusivo | Sistema Palco | — |
| Completar pendências | Tarefa de usuário | Dono | RF08 |
| Publicar página de vendas do show | Tarefa de sistema | Sistema Palco | RF08, RF09 |
| Liberar cotas à loja parceira e à bilheteria | Tarefa de sistema | Sistema Palco | RF27, RF29, RF24 |
| Vendas abertas | Evento de fim | Sistema Palco | — |

## Fluxo

```mermaid
flowchart LR
  subgraph L0["Dono"]
    direction LR
    P1_start([Proposta de show recebida])
    P1_t1[Consultar agenda e pré-reservar data]
    P1_g0{Data livre?}
    P1_t2[Propor outra data à banda]
    P1_t5[Registrar contrato, cachê e sinal]
    P1_t6[Cadastrar show e sessões]
    P1_t7[Definir local e montagem]
    P1_t8[Distribuir ingressos por canal]
    P1_t10[Definir cotas da lista de convidados]
    P1_t12[Completar pendências]
  end
  subgraph L1["Sócio"]
    direction LR
    P1_t3[Avaliar cachê e preço viável]
    P1_g1{Show viável?}
    P1_t9[Configurar lotes e preços]
  end
  subgraph L2["Sistema Palco"]
    direction LR
    P1_t4[Liberar pré-reserva da data]
    P1_end2([Show descartado])
    P1_t11[Verificar pendências para abrir vendas]
    P1_g2{Tudo pronto?}
    P1_t13[Publicar página de vendas do show]
    P1_t14[Liberar cotas à loja parceira e à bilheteria]
    P1_end([Vendas abertas])
  end
  P1_start --> P1_t1
  P1_t1 --> P1_g0
  P1_g0 -->|não| P1_t2
  P1_t2 --> P1_t1
  P1_g0 -->|sim| P1_t3
  P1_t3 --> P1_g1
  P1_g1 -->|não| P1_t4
  P1_t4 --> P1_end2
  P1_g1 -->|sim| P1_t5
  P1_t5 --> P1_t6
  P1_t6 --> P1_t7
  P1_t7 --> P1_t8
  P1_t8 --> P1_t9
  P1_t9 --> P1_t10
  P1_t10 --> P1_t11
  P1_t11 --> P1_g2
  P1_g2 -->|não| P1_t12
  P1_t12 --> P1_t11
  P1_g2 -->|sim| P1_t13
  P1_t13 --> P1_t14
  P1_t14 --> P1_end
```
