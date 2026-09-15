# P5 — Produção do show

**Pool:** Produção Cena Livre  
**Raias:** Dono, Sócio, Equipe e fornecedores, Sistema Palco  
**Arquivo BPMN:** [`bpmn/P5-producao-do-show.bpmn`](../../bpmn/P5-producao-do-show.bpmn)

Cobre a equipe e o dia do show. Hoje a escala é combinada por mensagem e há quem esqueça o compromisso, então o convite sai pelo sistema e cada pessoa confirma, com laço de substituição quando alguém não confirma. Os pagamentos feitos em dinheiro durante a noite são lançados no mesmo dia, para não se perderem até o fechamento.

## Atividades e requisitos atendidos

| Elemento | Tipo | Raia | Requisitos |
|---|---|---|---|
| Vendas abertas | Evento de início | Dono | — |
| Montar escala da equipe | Tarefa de usuário | Dono | RF19 |
| Enviar convite com data, função e valor | Tarefa de sistema | Sistema Palco | RF19, RF24 |
| Confirmar disponibilidade | Tarefa de usuário | Equipe e fornecedores | RF19 |
| Todos confirmaram? | Desvio exclusivo | Sistema Palco | — |
| Substituir pessoa ou contratar terceirizado | Tarefa de usuário | Dono | RF19, RF20 |
| Montar cronograma do dia | Tarefa de usuário | Sócio | RF21 |
| Conferir horário anunciado ao público | Tarefa de usuário | Dono | RF21, RF24 |
| Montar equipamento e passar o som | Tarefa manual | Equipe e fornecedores | RF21 |
| Registrar presença da equipe | Tarefa de usuário | Sócio | RF19 |
| Realizar o show | Tarefa manual | Equipe e fornecedores | RF21 |
| Lançar pagamentos feitos na noite | Tarefa de usuário | Sócio | RF33 |
| Registrar ocorrências do show | Tarefa de usuário | Dono | RF23 |
| Show realizado | Evento de fim | Dono | — |

## Fluxo

```mermaid
flowchart LR
  subgraph L0["Dono"]
    direction LR
    P5_start([Vendas abertas])
    P5_t1[Montar escala da equipe]
    P5_t4[Substituir pessoa ou contratar terceirizado]
    P5_t6[Conferir horário anunciado ao público]
    P5_t11[Registrar ocorrências do show]
    P5_end([Show realizado])
  end
  subgraph L1["Sócio"]
    direction LR
    P5_t5[Montar cronograma do dia]
    P5_t8[Registrar presença da equipe]
    P5_t10[Lançar pagamentos feitos na noite]
  end
  subgraph L2["Equipe e fornecedores"]
    direction LR
    P5_t3[Confirmar disponibilidade]
    P5_t7[Montar equipamento e passar o som]
    P5_t9[Realizar o show]
  end
  subgraph L3["Sistema Palco"]
    direction LR
    P5_t2[Enviar convite com data, função e valor]
    P5_g1{Todos confirmaram?}
  end
  P5_start --> P5_t1
  P5_t1 --> P5_t2
  P5_t2 --> P5_t3
  P5_t3 --> P5_g1
  P5_g1 -->|não| P5_t4
  P5_t4 --> P5_t1
  P5_g1 -->|sim| P5_t5
  P5_t5 --> P5_t6
  P5_t6 --> P5_t7
  P5_t7 --> P5_t8
  P5_t8 --> P5_t9
  P5_t9 --> P5_t10
  P5_t10 --> P5_t11
  P5_t11 --> P5_end
```
