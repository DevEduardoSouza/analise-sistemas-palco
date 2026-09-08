# P5 — Produção e realização do evento

**Pool:** Produção do evento  
**Raias:** Produtor, Equipe e fornecedores, Sistema Palco  
**Arquivo BPMN:** [`bpmn/P5-producao-e-realizacao-do-evento.bpmn`](../../bpmn/P5-producao-e-realizacao-do-evento.bpmn)

Cobre a operação em torno do show, do fechamento das atrações à execução do dia. O laço sobre o cronograma é a parte mais usada na prática, porque atraso de passagem de som empurra todo o resto e a produção precisa ver o efeito na hora.

## Atividades e requisitos atendidos

| Elemento | Tipo | Raia | Requisitos |
|---|---|---|---|
| Evento publicado | Evento de início | Produtor | — |
| Cadastrar atrações e fornecedores | Tarefa de usuário | Produtor | RF20 |
| Registrar contratos e cachês | Tarefa de usuário | Produtor | RF20 |
| Montar escala da equipe | Tarefa de usuário | Produtor | RF19 |
| Montar cronograma do dia | Tarefa de usuário | Produtor | RF21 |
| Notificar equipe e fornecedores | Tarefa de sistema | Sistema Palco | RF24 |
| Executar montagem e passagem de som | Tarefa manual | Equipe e fornecedores | RF21 |
| Registrar presença da equipe | Tarefa de usuário | Produtor | RF19 |
| Marcar etapas concluídas | Tarefa de usuário | Produtor | RF21 |
| Etapa atrasada? | Desvio exclusivo | Sistema Palco | — |
| Recalcular etapas seguintes | Tarefa de sistema | Sistema Palco | RF21 |
| Realizar o show | Tarefa manual | Equipe e fornecedores | RF21 |
| Encerrar sessão e registrar ocorrências | Tarefa de usuário | Produtor | RF23 |
| Evento realizado | Evento de fim | Produtor | — |

## Fluxo

```mermaid
flowchart LR
  subgraph L0["Produtor"]
    direction LR
    P5_start([Evento publicado])
    P5_t1[Cadastrar atrações e fornecedores]
    P5_t2[Registrar contratos e cachês]
    P5_t3[Montar escala da equipe]
    P5_t4[Montar cronograma do dia]
    P5_t7[Registrar presença da equipe]
    P5_t8[Marcar etapas concluídas]
    P5_t11[Encerrar sessão e registrar ocorrências]
    P5_end([Evento realizado])
  end
  subgraph L1["Equipe e fornecedores"]
    direction LR
    P5_t6[Executar montagem e passagem de som]
    P5_t10[Realizar o show]
  end
  subgraph L2["Sistema Palco"]
    direction LR
    P5_t5[Notificar equipe e fornecedores]
    P5_g1{Etapa atrasada?}
    P5_t9[Recalcular etapas seguintes]
  end
  P5_start --> P5_t1
  P5_t1 --> P5_t2
  P5_t2 --> P5_t3
  P5_t3 --> P5_t4
  P5_t4 --> P5_t5
  P5_t5 --> P5_t6
  P5_t6 --> P5_t7
  P5_t7 --> P5_t8
  P5_t8 --> P5_g1
  P5_g1 -->|sim| P5_t9
  P5_t9 --> P5_t8
  P5_g1 -->|não| P5_t10
  P5_t10 --> P5_t11
  P5_t11 --> P5_end
```
