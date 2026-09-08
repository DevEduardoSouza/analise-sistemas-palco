# Matriz de rastreabilidade

Liga cada requisito funcional às atividades dos diagramas BPMN em que ele aparece. É a evidência de coerência entre a modelagem dos processos e os requisitos mapeados, exigida na entrega. A tabela é gerada a partir da mesma definição que desenha os diagramas, em `tools/gen_bpmn.py`, e por isso não pode divergir deles.

| Requisito | Processos | Atividades |
|---|---|---|
| RF03 | P1, P6 | P1: Cadastrar produtora e dados de recebimento; P1: Analisar cadastro da produtora; P1: Corrigir dados cadastrais; P6: Gerar repasse ao produtor |
| RF04 | P1 | P1: Cadastrar local e setores |
| RF05 | P1 | P1: Cadastrar evento |
| RF06 | P1 | P1: Cadastrar sessões |
| RF07 | P1 | P1: Configurar lotes e preços |
| RF08 | P1 | P1: Submeter evento à análise; P1: Analisar evento; P1: Ajustar evento conforme parecer; P1: Publicar evento na vitrine |
| RF09 | P1, P2 | P1: Publicar evento na vitrine; P2: Pesquisar eventos na vitrine |
| RF10 | P2 | P2: Selecionar sessão, setor e quantidade; P2: Reservar ingressos por 15 minutos; P2: Liberar reserva e avisar recusa |
| RF11 | P2 | P2: Informar dados e aplicar cupom; P2: Enviar cobrança ao provedor; P2: Processar pagamento |
| RF12 | P2, P3, P4 | P2: Emitir ingressos com QR Code; P3: Invalidar ingressos e devolver estoque; P4: Apresentar ingresso digital; P4: Validar assinatura e situação |
| RF13 | P2, P4 | P2: Anexar comprovante do benefício; P4: Conferir documento do portador |
| RF14 | P2 | P2: Informar dados e aplicar cupom |
| RF15 | P3 | P3: Solicitar cancelamento; P3: Verificar política de cancelamento; P3: Analisar solicitação; P3: Registrar recusa com justificativa; P3: Invalidar ingressos e devolver estoque; P3: Solicitar estorno ao provedor; P3: Processar estorno |
| RF16 | P4 | P4: Conferir documento do portador |
| RF17 | P4 | P4: Ler QR Code do ingresso; P4: Validar assinatura e situação; P4: Registrar check-in e liberar acesso; P4: Registrar recusa e orientar bilheteria |
| RF18 | P4 | P4: Baixar lista de ingressos da sessão; P4: Sincronizar check-ins com o servidor |
| RF19 | P5, P6 | P5: Montar escala da equipe; P5: Registrar presença da equipe; P6: Consolidar custos do evento |
| RF20 | P5, P6 | P5: Cadastrar atrações e fornecedores; P5: Registrar contratos e cachês; P6: Consolidar custos do evento |
| RF21 | P5 | P5: Montar cronograma do dia; P5: Executar montagem e passagem de som; P5: Marcar etapas concluídas; P5: Recalcular etapas seguintes; P5: Realizar o show |
| RF22 | P3, P6 | P3: Registrar reembolso e notificar cliente; P6: Consolidar receita, taxas e descontos; P6: Consolidar custos do evento; P6: Conferir demonstrativo da sessão; P6: Corrigir lançamentos; P6: Fechar sessão e congelar valores; P6: Gerar repasse ao produtor |
| RF23 | P5, P6 | P5: Encerrar sessão e registrar ocorrências; P6: Consultar relatórios e exportar |
| RF24 | P1, P2, P3, P5, P6 | P1: Notificar produtor da publicação; P2: Liberar reserva e avisar recusa; P2: Enviar ingressos por e-mail; P3: Notificar cliente da recusa; P3: Registrar reembolso e notificar cliente; P5: Notificar equipe e fornecedores; P6: Notificar produtor do fechamento |

## Requisitos sem atividade correspondente

Os requisitos abaixo são funcionalidades de apoio, consultadas ou acionadas de dentro das telas, sem passo próprio na modelagem de processo.

- RF01
- RF02
- RF25
