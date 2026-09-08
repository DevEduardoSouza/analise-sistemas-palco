# Requisitos Funcionais — Sistema Palco

Sistema de gestão de eventos e shows. Documento de apoio ao Documento de Visão.
A entrega exige no mínimo 15 requisitos funcionais detalhados; aqui estão 25.

Convenções:

- **Código**: identificador estável, nunca reaproveitado.
- **Ator**: perfil que executa a funcionalidade.
- **Prioridade**: Essencial (o produto não existe sem ele), Importante (perda relevante de valor), Desejável (melhoria).
- **Processo**: processo BPMN em que o requisito aparece, garantindo a coerência entre modelagem e requisitos.

| Código | Nome | Ator | Prioridade | Processo |
|---|---|---|---|---|
| RF01 | Gestão de usuários e perfis de acesso | Administrador | Essencial | P1 |
| RF02 | Autenticação e recuperação de senha | Todos | Essencial | P1, P2 |
| RF03 | Cadastro de produtor e dados de recebimento | Administrador | Essencial | P1, P6 |
| RF04 | Cadastro de locais e setores | Produtor | Essencial | P1 |
| RF05 | Cadastro de evento | Produtor | Essencial | P1 |
| RF06 | Gestão de sessões do evento | Produtor | Essencial | P1 |
| RF07 | Gestão de lotes e tabela de preços | Produtor | Essencial | P1, P2 |
| RF08 | Submissão, aprovação e publicação do evento | Produtor, Administrador | Essencial | P1 |
| RF09 | Vitrine pública e busca de eventos | Cliente | Essencial | P2 |
| RF10 | Carrinho com reserva temporária de ingressos | Cliente | Essencial | P2 |
| RF11 | Checkout e processamento de pagamento | Cliente | Essencial | P2 |
| RF12 | Emissão de ingresso digital com QR Code | Sistema | Essencial | P2, P4 |
| RF13 | Meia-entrada e validação de comprovante | Cliente, Portaria | Importante | P2, P4 |
| RF14 | Cupons de desconto e cortesias | Produtor | Importante | P2 |
| RF15 | Cancelamento de pedido e reembolso | Cliente, Financeiro | Essencial | P3 |
| RF16 | Transferência e nominação de ingresso | Cliente | Importante | P2, P4 |
| RF17 | Check-in e validação de acesso | Portaria | Essencial | P4 |
| RF18 | Operação offline da portaria e sincronização | Portaria | Importante | P4 |
| RF19 | Gestão de equipe e escala do evento | Produtor | Importante | P5 |
| RF20 | Gestão de atrações, fornecedores e contratos | Produtor | Importante | P5 |
| RF21 | Cronograma de produção do dia do evento | Produtor | Importante | P5 |
| RF22 | Painel financeiro e fechamento do evento | Financeiro, Produtor | Essencial | P6 |
| RF23 | Relatórios gerenciais e exportação | Produtor, Financeiro | Importante | P6 |
| RF24 | Notificações e comunicação com o público | Sistema, Produtor | Importante | P1, P2, P3, P5 |
| RF25 | Registro de auditoria das operações críticas | Sistema | Desejável | Todos |

---

## RF01 — Gestão de usuários e perfis de acesso

**Ator:** Administrador. **Prioridade:** Essencial. **Processo:** P1.

Permite cadastrar, editar, inativar e listar usuários do sistema, atribuindo a cada um os perfis Administrador, Produtor, Financeiro, Portaria ou Cliente. Um mesmo usuário pode acumular perfis, por exemplo Produtor e Financeiro em uma produtora pequena. O cadastro registra nome, CPF, e-mail, telefone, perfis, produtora vinculada e situação. O sistema não permite excluir fisicamente um usuário que já tenha operações registradas; nesse caso apenas a inativação é permitida, preservando o histórico. Cada perfil determina quais telas e ações ficam disponíveis, e a tentativa de acesso a uma função sem permissão é bloqueada e registrada conforme RF25.

## RF02 — Autenticação e recuperação de senha

**Ator:** Todos. **Prioridade:** Essencial. **Processos:** P1, P2.

Permite o acesso ao sistema mediante e-mail e senha, com bloqueio temporário da conta após cinco tentativas incorretas consecutivas. O cliente também pode se autenticar por conta Google. A recuperação de senha é feita por link de uso único enviado ao e-mail cadastrado, com validade de trinta minutos. Perfis administrativos, Administrador e Financeiro, exigem segundo fator de autenticação por aplicativo autenticador. O encerramento da sessão ocorre por inatividade de trinta minutos nos perfis administrativos.

## RF03 — Cadastro de produtor e dados de recebimento

**Ator:** Administrador. **Prioridade:** Essencial. **Processos:** P1, P6.

Permite cadastrar a produtora responsável pelos eventos, com razão social, nome fantasia, CNPJ ou CPF, endereço, responsável legal, contatos e dados bancários para repasse, incluindo banco, agência, conta e chave Pix. O produtor só pode submeter eventos para publicação após ter o cadastro aprovado pelo Administrador, com documentos anexados. Alterações nos dados bancários exigem nova aprovação e ficam registradas no histórico, porque afetam diretamente o repasse tratado em RF22.

## RF04 — Cadastro de locais e setores

**Ator:** Produtor. **Prioridade:** Essencial. **Processo:** P1.

Permite cadastrar os locais onde os eventos ocorrem, com nome, endereço completo, capacidade total, coordenadas geográficas e informações de acessibilidade. Cada local é dividido em setores, por exemplo Pista, Camarote, Arquibancada e Área Acessível, e cada setor possui nome, capacidade própria e indicação de lugar marcado ou não marcado. A soma das capacidades dos setores não pode ultrapassar a capacidade total do local. Locais já usados em eventos publicados não podem ter setores excluídos, apenas inativados.

## RF05 — Cadastro de evento

**Ator:** Produtor. **Prioridade:** Essencial. **Processo:** P1.

Permite cadastrar um evento com nome, descrição, categoria, classificação indicativa, local, imagem de divulgação, política de meia-entrada, política de cancelamento e produtora responsável. O evento nasce na situação Rascunho e só se torna visível ao público após passar pelo fluxo de RF08. O sistema deve permitir editar, duplicar, pesquisar por nome, período, categoria e situação, e listar os eventos da produtora do usuário logado. A duplicação copia setores, sessões e lotes, poupando retrabalho em eventos recorrentes.

## RF06 — Gestão de sessões do evento

**Ator:** Produtor. **Prioridade:** Essencial. **Processo:** P1.

Permite cadastrar uma ou mais sessões para o mesmo evento, cada uma com data, horário de abertura dos portões, horário de início, horário previsto de término e setores disponíveis. Um show que se repete em três noites é um evento com três sessões, e cada sessão controla o próprio estoque de ingressos. O sistema impede cadastrar duas sessões no mesmo local com horários sobrepostos e alerta o produtor quando a data da sessão for anterior à data atual.

## RF07 — Gestão de lotes e tabela de preços

**Ator:** Produtor. **Prioridade:** Essencial. **Processos:** P1, P2.

Permite definir, para cada setor de cada sessão, os lotes de venda com nome, quantidade de ingressos, preço inteiro, preço de meia-entrada, taxa de serviço, data de início e data de fim da vigência. A virada de lote ocorre automaticamente quando a quantidade se esgota ou quando a data final é atingida, o que acontecer primeiro. O sistema impede que a soma das quantidades dos lotes ultrapasse a capacidade do setor e mantém histórico dos preços praticados, informação necessária para o cálculo de reembolso em RF15.

## RF08 — Submissão, aprovação e publicação do evento

**Ator:** Produtor e Administrador. **Prioridade:** Essencial. **Processo:** P1.

Permite ao produtor submeter o evento à análise quando ele já tiver local, ao menos uma sessão e ao menos um lote configurado. O Administrador analisa e pode aprovar, reprovar com justificativa ou solicitar ajustes. Na aprovação o evento passa a Publicado e fica visível na vitrine de RF09 na data e hora de início de vendas definidas. O produtor pode despublicar um evento sem vendas registradas; havendo vendas, a retirada do ar só ocorre pelo processo de cancelamento de RF15. Todas as transições de situação são notificadas conforme RF24 e registradas conforme RF25.

## RF09 — Vitrine pública e busca de eventos

**Ator:** Cliente. **Prioridade:** Essencial. **Processo:** P2.

Permite ao público consultar os eventos publicados sem necessidade de login, com busca por texto livre, filtros de cidade, categoria, faixa de preço e período, e ordenação por data ou por relevância. A página do evento apresenta descrição, sessões, setores, lotes disponíveis, preços com taxa destacada, política de meia-entrada, política de cancelamento e mapa do local. Setores esgotados aparecem marcados como indisponíveis, e não ocultos, para não gerar dúvida no comprador.

## RF10 — Carrinho com reserva temporária de ingressos

**Ator:** Cliente. **Prioridade:** Essencial. **Processo:** P2.

Permite ao cliente selecionar sessão, setor, tipo de ingresso e quantidade, respeitando o limite máximo por CPF definido pelo produtor no evento. Ao adicionar itens ao carrinho, o sistema cria uma reserva temporária que retira os ingressos do estoque disponível por quinze minutos, exibindo o tempo restante. Expirado o prazo sem conclusão do pagamento, a reserva é liberada automaticamente e o estoque volta a ficar disponível. O carrinho aceita ingressos de sessões diferentes do mesmo evento em um único pedido.

## RF11 — Checkout e processamento de pagamento

**Ator:** Cliente. **Prioridade:** Essencial. **Processo:** P2.

Permite concluir a compra informando os dados do comprador, nome, CPF, e-mail e telefone, e escolhendo entre cartão de crédito, Pix ou boleto. O sistema envia a cobrança ao provedor de pagamento e mantém o pedido na situação Aguardando pagamento até o retorno da confirmação. Pagamento aprovado leva o pedido a Pago e dispara a emissão de RF12. Pagamento recusado devolve o cliente ao checkout com a mensagem do provedor, mantendo a reserva enquanto durar o prazo de RF10. Pix e boleto não pagos dentro do prazo levam o pedido a Expirado e liberam o estoque. O sistema nunca armazena o número completo do cartão, guardando apenas bandeira e quatro últimos dígitos.

## RF12 — Emissão de ingresso digital com QR Code

**Ator:** Sistema. **Prioridade:** Essencial. **Processos:** P2, P4.

Gera, para cada ingresso de um pedido pago, um registro individual com código único, QR Code assinado digitalmente, identificação do evento, sessão, setor, tipo de ingresso, nome do portador e situação. O ingresso é disponibilizado na área do cliente e enviado por e-mail em PDF. O código do QR não é sequencial nem previsível, e sua assinatura permite validar a autenticidade em RF17 mesmo com a portaria operando offline. A reemissão do arquivo é permitida sem gerar novo código, evitando duplicidade de acesso.

## RF13 — Meia-entrada e validação de comprovante

**Ator:** Cliente e Portaria. **Prioridade:** Importante. **Processos:** P2, P4.

Permite a compra de ingresso de meia-entrada respeitando a cota legal definida por sessão, informando a categoria do benefício, estudante, idoso, pessoa com deficiência ou jovem de baixa renda, e anexando o comprovante quando o produtor exigir. O ingresso de meia-entrada é sempre nominal e recebe marcação visível no QR Code, para que a portaria exija a apresentação do documento comprobatório em RF17. Esgotada a cota, o sistema oferece apenas ingressos inteiros.

## RF14 — Cupons de desconto e cortesias

**Ator:** Produtor. **Prioridade:** Importante. **Processo:** P2.

Permite ao produtor criar cupons com código, tipo de desconto percentual ou valor fixo, quantidade de usos, validade e restrição por evento, sessão ou setor. Permite ainda emitir cortesias, ingressos com valor zero destinados a convidados, imprensa e permutas, com controle de cota separado do estoque de venda. O cliente aplica o cupom no checkout de RF11, com validação imediata e mensagem clara quando o cupom estiver expirado, esgotado ou não aplicável. Cortesias e cupons entram no fechamento de RF22 como dedução de receita.

## RF15 — Cancelamento de pedido e reembolso

**Ator:** Cliente e Financeiro. **Prioridade:** Essencial. **Processo:** P3.

Permite ao cliente solicitar o cancelamento da compra pela área do cliente e ao Financeiro processar o reembolso. O sistema aplica a política do evento, com devolução integral quando a solicitação ocorre até sete dias após a compra e até quarenta e oito horas antes da sessão. Fora dessa janela, a solicitação segue para análise manual do Financeiro, que pode aprovar ou recusar com justificativa. Aprovado o cancelamento, os ingressos são invalidados, impedindo o check-in de RF17, o estoque retorna ao lote de origem e o estorno é solicitado ao provedor de pagamento. O cancelamento do evento inteiro pelo produtor dispara o reembolso integral automático de todos os pedidos pagos e a notificação de RF24.

## RF16 — Transferência e nominação de ingresso

**Ator:** Cliente. **Prioridade:** Importante. **Processos:** P2, P4.

Permite ao comprador atribuir cada ingresso a um portador, informando nome e CPF, e transferir um ingresso ainda não utilizado para outra pessoa por e-mail. A transferência invalida o QR Code anterior e emite um novo para o destinatário, evitando que os dois códigos circulem. O produtor pode desabilitar a transferência por evento e o sistema bloqueia transferências a partir de duas horas antes da abertura dos portões.

## RF17 — Check-in e validação de acesso

**Ator:** Portaria. **Prioridade:** Essencial. **Processo:** P4.

Permite ao operador de portaria ler o QR Code do ingresso pela câmera do dispositivo e obter uma resposta imediata em até dois segundos, com três resultados possíveis. Acesso liberado, quando o ingresso é válido, pertence à sessão em curso e ainda não foi utilizado, registrando data, hora, operador e portão. Acesso negado, quando o ingresso é inválido, cancelado, de outra sessão ou já utilizado, exibindo o motivo e o horário do uso anterior. Verificação manual, quando o ingresso é de meia-entrada ou nominal, exigindo conferência do documento antes da liberação. O sistema permite também a busca por CPF ou código do pedido para atender quem chegou sem o ingresso em mãos.

## RF18 — Operação offline da portaria e sincronização

**Ator:** Portaria. **Prioridade:** Importante. **Processo:** P4.

Permite que o aplicativo de portaria baixe previamente a lista de ingressos válidos da sessão e continue validando acessos sem conexão de rede, situação comum em espaços abertos e casas de show. Os check-ins realizados offline ficam em fila local e são enviados ao servidor assim que a conexão retorna. Em caso de conflito, quando o mesmo ingresso foi validado em dois dispositivos, o sistema mantém o primeiro registro pelo horário do evento, marca o segundo como duplicidade e o apresenta no relatório de ocorrências da sessão.

## RF19 — Gestão de equipe e escala do evento

**Ator:** Produtor. **Prioridade:** Importante. **Processo:** P5.

Permite montar a equipe de cada sessão definindo funções, por exemplo portaria, segurança, bar, limpeza e produção, quantidade de pessoas por função, nomes, horário de entrada e saída e valor de diária. O sistema alerta quando uma pessoa é escalada em duas sessões com horários sobrepostos e permite registrar a presença efetiva no dia, informação que alimenta o custo de pessoal no fechamento de RF22.

## RF20 — Gestão de atrações, fornecedores e contratos

**Ator:** Produtor. **Prioridade:** Importante. **Processo:** P5.

Permite cadastrar as atrações do evento, com nome artístico, contato, cachê, forma de pagamento, horário de apresentação e requisitos técnicos, além dos fornecedores de som, luz, palco, alimentação e segurança, com valores contratados. Permite anexar contratos e registrar a situação de cada compromisso, contratado, sinal pago ou quitado. Os valores lançados compõem a previsão de custos e o resultado do evento em RF22.

## RF21 — Cronograma de produção do dia do evento

**Ator:** Produtor. **Prioridade:** Importante. **Processo:** P5.

Permite montar a linha do tempo da sessão, com tarefas como montagem de palco, passagem de som, abertura de portões, entrada da banda de abertura, show principal e desmontagem, cada uma com horário previsto, responsável e situação. Durante o evento o responsável marca cada etapa como concluída, e o atraso em uma etapa recalcula e destaca visualmente as etapas seguintes, apoiando a decisão da produção em tempo real.

## RF22 — Painel financeiro e fechamento do evento

**Ator:** Financeiro e Produtor. **Prioridade:** Essencial. **Processo:** P6.

Apresenta, por evento e por sessão, a receita bruta de ingressos, as taxas de serviço, os descontos concedidos, os reembolsos, os custos lançados de atrações, fornecedores e equipe, e o resultado líquido. Permite ao Financeiro realizar o fechamento da sessão, congelando os valores e gerando o repasse ao produtor conforme os dados bancários de RF03 e o percentual de comissão da plataforma. O fechamento só é liberado após o encerramento da janela de reembolso, evitando repassar valores sujeitos a estorno. Sessões fechadas ficam bloqueadas para novos lançamentos e a reabertura exige perfil Administrador com justificativa registrada.

## RF23 — Relatórios gerenciais e exportação

**Ator:** Produtor e Financeiro. **Prioridade:** Importante. **Processo:** P6.

Disponibiliza relatórios de vendas por período, por lote, por setor e por forma de pagamento, curva de vendas ao longo do tempo, taxa de comparecimento comparando ingressos vendidos e check-ins realizados, ocorrências de portaria e demonstrativo de resultado por evento. Todos os relatórios permitem filtro por período e evento e exportação em CSV e PDF. A taxa de comparecimento cruza dados de RF12 e RF17 e orienta o dimensionamento de equipe em eventos futuros.

## RF24 — Notificações e comunicação com o público

**Ator:** Sistema e Produtor. **Prioridade:** Importante. **Processos:** P1, P2, P3, P5.

Envia automaticamente por e-mail a confirmação de compra com os ingressos, o aviso de pagamento recusado ou expirado, a confirmação de cancelamento e reembolso, o lembrete da sessão vinte e quatro horas antes e o aviso de alteração ou cancelamento do evento. Permite ainda ao produtor enviar comunicados a todos os compradores de uma sessão, por exemplo mudança de horário dos portões. Toda comunicação registra data, destinatário e situação de entrega, e o cliente pode optar por não receber mensagens promocionais, mantendo as transacionais.

## RF25 — Registro de auditoria das operações críticas

**Ator:** Sistema. **Prioridade:** Desejável. **Processo:** todos.

Registra em trilha de auditoria as operações sensíveis do sistema, incluindo criação e alteração de eventos, lotes e preços, aprovação e publicação, cancelamentos e reembolsos, emissão de cortesias, alterações de dados bancários, fechamento e reabertura financeira e tentativas de acesso negadas. Cada registro guarda usuário, data e hora, endereço de origem, operação, valor anterior e valor novo. A trilha é somente leitura, consultável por Administrador com filtros de período, usuário e tipo de operação, e retida por cinco anos.
