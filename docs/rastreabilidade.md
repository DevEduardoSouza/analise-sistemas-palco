# Matriz de rastreabilidade

Liga cada requisito funcional às atividades dos diagramas BPMN em que ele aparece. É a evidência de coerência entre a modelagem dos processos e os requisitos mapeados, exigida na entrega. A tabela é gerada a partir da mesma definição que desenha os diagramas, em `tools/gen_bpmn.py`, e por isso não pode divergir deles.

| Requisito | Processos | Atividades |
|---|---|---|
| RF04 | P1 | P1: Definir local e montagem |
| RF05 | P1 | P1: Cadastrar show e sessões |
| RF06 | P1 | P1: Cadastrar show e sessões |
| RF07 | P1 | P1: Configurar lotes e preços |
| RF08 | P1 | P1: Verificar pendências para abrir vendas; P1: Completar pendências; P1: Publicar página de vendas do show |
| RF09 | P1, P2 | P1: Publicar página de vendas do show; P2: Abrir página do show pelo link |
| RF10 | P2 | P2: Escolher tipo e quantidade; P2: Reservar ingressos por 15 minutos; P2: Liberar reserva e avisar cliente |
| RF11 | P2 | P2: Aplicar cupom e pagar com Pix ou cartão; P2: Processar pagamento |
| RF12 | P2, P3, P4 | P2: Emitir ingresso com QR Code; P2: Enviar ingresso por e-mail; P3: Cancelar ingressos e devolver à cota; P4: Apresentar ingresso ou nome na lista; P4: Vender ingresso na porta |
| RF13 | P2, P4 | P2: Informar categoria e anexar comprovante; P4: Conferir documento do portador |
| RF14 | P2 | P2: Aplicar cupom e pagar com Pix ou cartão |
| RF15 | P3 | P3: Solicitar cancelamento; P3: Localizar compra e verificar política; P3: Analisar pedido fora da política; P3: Notificar recusa com justificativa; P3: Cancelar ingressos e devolver à cota; P3: Solicitar estorno ao provedor; P3: Processar estorno; P3: Devolver valor ao comprador identificado |
| RF16 | P4 | P4: Conferir documento do portador |
| RF17 | P4 | P4: Ler QR Code ou buscar nome na lista; P4: Validar ingresso ou convite; P4: Registrar entrada e atualizar lotação; P4: Negar entrada e informar motivo |
| RF18 | P4 | P4: Baixar ingressos e lista de convidados; P4: Validar ingresso ou convite; P4: Sincronizar entradas ao reconectar |
| RF19 | P5 | P5: Montar escala da equipe; P5: Enviar convite com data, função e valor; P5: Confirmar disponibilidade; P5: Substituir pessoa ou contratar terceirizado; P5: Registrar presença da equipe |
| RF20 | P1, P5 | P1: Avaliar cachê e preço viável; P1: Registrar contrato, cachê e sinal; P5: Substituir pessoa ou contratar terceirizado |
| RF21 | P5 | P5: Montar cronograma do dia; P5: Conferir horário anunciado ao público; P5: Montar equipamento e passar o som; P5: Realizar o show |
| RF22 | P3, P6 | P3: Registrar reembolso no financeiro do show; P6: Consolidar receitas por canal e despesas; P6: Exibir resultado prévio ao dono e ao sócio; P6: Confirmar recebimento do acerto; P6: Fechar show e congelar valores |
| RF23 | P5, P6 | P5: Registrar ocorrências do show; P6: Consultar resultado e relatórios |
| RF24 | P1, P2, P3, P5 | P1: Liberar cotas à loja parceira e à bilheteria; P2: Liberar reserva e avisar cliente; P2: Enviar ingresso por e-mail; P3: Avisar compradores e abrir prazo de reembolso; P3: Notificar recusa com justificativa; P3: Registrar reembolso no financeiro do show; P5: Enviar convite com data, função e valor; P5: Conferir horário anunciado ao público |
| RF26 | P1, P3 | P1: Consultar agenda e pré-reservar data; P1: Propor outra data à banda; P1: Liberar pré-reserva da data; P1: Cadastrar show e sessões; P3: Remarcar data ou cancelar o show |
| RF27 | P1, P2, P3 | P1: Distribuir ingressos por canal; P1: Liberar cotas à loja parceira e à bilheteria; P2: Baixar da cota do parceiro; P2: Reservar ingressos por 15 minutos; P3: Cancelar ingressos e devolver à cota |
| RF28 | P1, P4 | P1: Definir cotas da lista de convidados; P4: Baixar ingressos e lista de convidados; P4: Apresentar ingresso ou nome na lista; P4: Ler QR Code ou buscar nome na lista |
| RF29 | P1, P2, P3, P6 | P1: Liberar cotas à loja parceira e à bilheteria; P2: Registrar venda com nome e CPF; P2: Baixar da cota do parceiro; P3: Devolver valor ao comprador identificado; P6: Calcular acerto da loja parceira; P6: Repassar vendas descontada a comissão; P6: Confirmar recebimento do acerto |
| RF30 | P3, P4, P6 | P3: Devolver valor ao comprador identificado; P4: Vender ingresso na porta; P6: Fechar caixa da bilheteria |
| RF31 | P3 | P3: Remarcar data ou cancelar o show; P3: Avisar compradores e abrir prazo de reembolso |
| RF32 | P4 | P4: Verificar lotação disponível; P4: Registrar entrada e atualizar lotação |
| RF33 | P1, P5, P6 | P1: Registrar contrato, cachê e sinal; P5: Lançar pagamentos feitos na noite; P6: Fechar caixa da bilheteria; P6: Consolidar receitas por canal e despesas; P6: Conferir despesas e comprovantes; P6: Lançar despesa pendente |

## Requisitos sem atividade correspondente

Os requisitos abaixo são funcionalidades de apoio, consultadas ou acionadas de dentro das telas, sem passo próprio na modelagem de processo.

- RF01
- RF02
- RF25

## Requisitos retirados

O RF03, cadastro de produtora com aprovação por administrador, foi retirado depois da entrevista com o dono da Cena Livre, porque o sistema atende uma única casa de shows e não uma plataforma de várias produtoras. O código não é reaproveitado.
