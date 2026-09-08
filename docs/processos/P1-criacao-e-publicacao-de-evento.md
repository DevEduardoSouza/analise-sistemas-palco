# P1 — Criação e publicação de evento

**Pool:** Plataforma Palco  
**Raias:** Produtor, Administrador da plataforma, Sistema Palco  
**Arquivo BPMN:** [`bpmn/P1-criacao-e-publicacao-de-evento.bpmn`](../../bpmn/P1-criacao-e-publicacao-de-evento.bpmn)

Vai da chegada de uma produtora à plataforma até o evento no ar, pronto para vender. Concentra os cadastros de base, local, evento, sessões e lotes, e passa por duas aprovações do administrador, uma do cadastro da produtora e outra do evento em si. As duas aprovações têm caminho de retorno, porque na prática a maior parte dos eventos volta para ajuste antes de ser publicada.

## Atividades e requisitos atendidos

| Elemento | Tipo | Raia | Requisitos |
|---|---|---|---|
| Produtor quer vender ingressos | Evento de início | Produtor | — |
| Cadastrar produtora e dados de recebimento | Tarefa de usuário | Produtor | RF03 |
| Analisar cadastro da produtora | Tarefa de usuário | Administrador da plataforma | RF03 |
| Cadastro aprovado? | Desvio exclusivo | Administrador da plataforma | — |
| Corrigir dados cadastrais | Tarefa de usuário | Produtor | RF03 |
| Cadastrar local e setores | Tarefa de usuário | Produtor | RF04 |
| Cadastrar evento | Tarefa de usuário | Produtor | RF05 |
| Cadastrar sessões | Tarefa de usuário | Produtor | RF06 |
| Configurar lotes e preços | Tarefa de usuário | Produtor | RF07 |
| Submeter evento à análise | Tarefa de usuário | Produtor | RF08 |
| Analisar evento | Tarefa de usuário | Administrador da plataforma | RF08 |
| Evento aprovado? | Desvio exclusivo | Administrador da plataforma | — |
| Ajustar evento conforme parecer | Tarefa de usuário | Produtor | RF08 |
| Publicar evento na vitrine | Tarefa de sistema | Sistema Palco | RF08, RF09 |
| Notificar produtor da publicação | Tarefa de sistema | Sistema Palco | RF24 |
| Evento publicado | Evento de fim | Sistema Palco | — |

## Fluxo

```mermaid
flowchart LR
  subgraph L0["Produtor"]
    direction LR
    P1_start([Produtor quer vender ingressos])
    P1_t1[Cadastrar produtora e dados de recebimento]
    P1_t3[Corrigir dados cadastrais]
    P1_t4[Cadastrar local e setores]
    P1_t5[Cadastrar evento]
    P1_t6[Cadastrar sessões]
    P1_t7[Configurar lotes e preços]
    P1_t8[Submeter evento à análise]
    P1_t10[Ajustar evento conforme parecer]
  end
  subgraph L1["Administrador da plataforma"]
    direction LR
    P1_t2[Analisar cadastro da produtora]
    P1_g1{Cadastro aprovado?}
    P1_t9[Analisar evento]
    P1_g2{Evento aprovado?}
  end
  subgraph L2["Sistema Palco"]
    direction LR
    P1_t11[Publicar evento na vitrine]
    P1_t12[Notificar produtor da publicação]
    P1_end([Evento publicado])
  end
  P1_start --> P1_t1
  P1_t1 --> P1_t2
  P1_t2 --> P1_g1
  P1_g1 -->|não| P1_t3
  P1_t3 --> P1_t2
  P1_g1 -->|sim| P1_t4
  P1_t4 --> P1_t5
  P1_t5 --> P1_t6
  P1_t6 --> P1_t7
  P1_t7 --> P1_t8
  P1_t8 --> P1_t9
  P1_t9 --> P1_g2
  P1_g2 -->|não| P1_t10
  P1_t10 --> P1_t8
  P1_g2 -->|sim| P1_t11
  P1_t11 --> P1_t12
  P1_t12 --> P1_end
```
