# Casos de uso do sistema Palco

Este documento agrupa os 32 requisitos funcionais ativos em casos de uso e organiza os casos em pacotes. Cada pacote corresponde a um processo modelado em BPMN, de P1 a P6, mais um pacote de apoio que não tem processo próprio. É esse agrupamento que os diagramas de casos de uso desenham, um diagrama por pacote.

Os atores citados estão definidos em [atores.md](atores.md). O detalhamento de cada requisito está em [../requisitos/requisitos-funcionais.md](../requisitos/requisitos-funcionais.md) e a ligação dos requisitos com as atividades dos diagramas BPMN, em [../rastreabilidade.md](../rastreabilidade.md).

Convenções:

- O código do caso de uso é estável, de `UC01` a `UC43`, e não é reaproveitado se um caso for retirado.
- Um caso de uso não é a mesma coisa que um requisito. Um requisito extenso pode virar vários casos, como o RF15, que se divide em pedido, análise e devolução; e um caso pode atender mais de um requisito, como a abertura das vendas.
- `<<include>>` indica comportamento sempre executado pelo caso que o inclui. `<<extend>>` indica comportamento opcional, que só ocorre em determinada condição.

## 1. Pacote Acesso e administração

Apoio a todos os processos, sem atividade própria no BPMN.

| Caso de uso | Ator primário | Atores secundários | Requisitos |
|---|---|---|---|
| UC01 — Autenticar no sistema | Todos | Conta Google | RF02 |
| UC02 — Manter usuários e perfis | Dono | — | RF01 |

## 2. Pacote P1 — Planejamento e abertura de vendas

| Caso de uso | Ator primário | Atores secundários | Requisitos |
|---|---|---|---|
| UC03 — Consultar agenda e pré-reservar data | Dono | Tempo | RF26 |
| UC04 — Manter locais e montagens | Dono | — | RF04 |
| UC05 — Registrar contratos, cachês e fornecedores | Dono, Sócio, Administrativo | — | RF20 |
| UC06 — Cadastrar show | Dono | — | RF05 |
| UC07 — Manter sessões do show | Dono | — | RF06 |
| UC08 — Configurar lotes e preços | Sócio | Tempo | RF07 |
| UC09 — Distribuir ingressos por canal | Dono | — | RF27 |
| UC10 — Definir cotas da lista de convidados | Dono | — | RF28 |
| UC11 — Abrir vendas do show | Dono | Serviço de e-mail e mensagem | RF08, RF09 |
| UC12 — Verificar pendências para abertura | — | — | RF08 |

Relacionamentos: UC06 `<<include>>` UC07. UC11 `<<include>>` UC12 e publica a página pública do RF09.

## 3. Pacote P2 — Venda de ingressos nos canais

| Caso de uso | Ator primário | Atores secundários | Requisitos |
|---|---|---|---|
| UC13 — Consultar agenda pública e página do show | Cliente | — | RF09 |
| UC14 — Comprar ingresso online | Cliente | Provedor de pagamento | RF10, RF11 |
| UC15 — Reservar ingressos por quinze minutos | — | Tempo | RF10 |
| UC16 — Aplicar cupom de desconto | Cliente | — | RF14 |
| UC17 — Comprar meia-entrada | Cliente | — | RF13 |
| UC18 — Emitir ingresso com QR Code | — | Serviço de e-mail e mensagem | RF12 |
| UC19 — Manter cupons de desconto | Sócio | — | RF14 |
| UC20 — Vender ingresso pela loja parceira | Loja parceira | — | RF29 |

Relacionamentos: UC14 `<<include>>` UC15 e UC18; UC16 e UC17 `<<extend>>` UC14. UC20 `<<include>>` UC18.

## 4. Pacote P3 — Cancelamento, remarcação e reembolso

| Caso de uso | Ator primário | Atores secundários | Requisitos |
|---|---|---|---|
| UC21 — Solicitar cancelamento da compra | Cliente | — | RF15 |
| UC22 — Registrar cancelamento no atendimento | Bilheteria | — | RF15 |
| UC23 — Analisar pedido fora da política | Dono, Sócio | — | RF15 |
| UC24 — Devolver valor ao comprador | — | Provedor de pagamento | RF15 |
| UC25 — Remarcar ou cancelar show | Dono, Sócio | Serviço de e-mail e mensagem | RF31 |

Relacionamentos: UC21 e UC22 `<<include>>` UC24 quando o pedido está dentro da política; UC23 `<<extend>>` UC21 e UC22 quando está fora. UC25 `<<include>>` UC24 para os compradores do show cancelado.

## 5. Pacote P4 — Entrada do público no dia do show

| Caso de uso | Ator primário | Atores secundários | Requisitos |
|---|---|---|---|
| UC26 — Preparar operação offline da portaria | Portaria | — | RF18 |
| UC27 — Validar ingresso na entrada | Portaria | — | RF17 |
| UC28 — Conferir meia-entrada na porta | Portaria | — | RF13 |
| UC29 — Registrar entrada de convidado | Portaria | — | RF28 |
| UC30 — Controlar lotação em tempo real | Portaria, Bilheteria | — | RF32 |
| UC31 — Vender ingresso na porta | Bilheteria | — | RF30 |
| UC32 — Nomear e transferir ingresso | Cliente | Serviço de e-mail e mensagem | RF16 |

Relacionamentos: UC27 `<<include>>` UC30; UC28 `<<extend>>` UC27 quando o ingresso é de meia-entrada. UC29 `<<include>>` UC30. UC31 `<<include>>` UC18 e consulta UC30 antes de vender.

## 6. Pacote P5 — Produção do show

| Caso de uso | Ator primário | Atores secundários | Requisitos |
|---|---|---|---|
| UC33 — Montar escala da equipe | Dono, Sócio | Serviço de e-mail e mensagem | RF19 |
| UC34 — Confirmar convite da escala | Equipe | — | RF19 |
| UC35 — Montar cronograma do dia | Sócio | — | RF21 |
| UC36 — Registrar ocorrências do show | Sócio | — | RF23 |
| UC37 — Lançar despesas e pagamentos da noite | Sócio, Administrativo | — | RF33 |

Relacionamentos: UC33 `<<include>>` UC43 para o envio dos convites.

## 7. Pacote P6 — Fechamento financeiro do show

| Caso de uso | Ator primário | Atores secundários | Requisitos |
|---|---|---|---|
| UC38 — Fechar caixa da bilheteria | Bilheteria | — | RF30 |
| UC39 — Calcular acerto da loja parceira | Sócio | — | RF29 |
| UC40 — Consultar resultado financeiro do show | Dono, Sócio | — | RF22 |
| UC41 — Fechar show e congelar valores | Dono, Sócio | — | RF22 |
| UC42 — Consultar relatórios e exportar | Dono, Sócio, Administrativo | — | RF23, RF25 |

Relacionamentos: UC41 `<<include>>` UC39 e UC38, porque o show só fecha depois do acerto do parceiro e do caixa da noite. A trilha de auditoria do RF25 é consultada dentro do UC42.

## 8. Caso de uso transversal

| Caso de uso | Ator primário | Atores secundários | Requisitos |
|---|---|---|---|
| UC43 — Notificar por e-mail e mensagem | — | Serviço de e-mail e mensagem | RF24 |

O UC43 não é iniciado por ator humano. É incluído pelos casos que precisam avisar alguém: UC11, UC14, UC18, UC21, UC24, UC25, UC32 e UC33. Nos diagramas ele aparece uma única vez, no pacote em que está sendo desenhado, para não poluir o desenho.

## 9. Cobertura dos requisitos

Os 32 requisitos funcionais ativos estão cobertos. O RF03 foi retirado e não tem caso de uso.

| Requisito | Casos de uso |
|---|---|
| RF01 | UC02 |
| RF02 | UC01 |
| RF04 | UC04 |
| RF05 | UC06 |
| RF06 | UC07 |
| RF07 | UC08 |
| RF08 | UC11, UC12 |
| RF09 | UC11, UC13 |
| RF10 | UC14, UC15 |
| RF11 | UC14 |
| RF12 | UC18 |
| RF13 | UC17, UC28 |
| RF14 | UC16, UC19 |
| RF15 | UC21, UC22, UC23, UC24 |
| RF16 | UC32 |
| RF17 | UC27 |
| RF18 | UC26 |
| RF19 | UC33, UC34 |
| RF20 | UC05 |
| RF21 | UC35 |
| RF22 | UC40, UC41 |
| RF23 | UC36, UC42 |
| RF24 | UC43 |
| RF25 | UC42 |
| RF26 | UC03 |
| RF27 | UC09 |
| RF28 | UC10, UC29 |
| RF29 | UC20, UC39 |
| RF30 | UC31, UC38 |
| RF31 | UC25 |
| RF32 | UC30 |
| RF33 | UC37 |
