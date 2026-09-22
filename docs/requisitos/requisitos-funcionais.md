# Requisitos Funcionais — Sistema Palco

Sistema de gestão de shows da **Cena Livre**, casa de shows com capacidade para cerca de quatrocentas pessoas, que também realiza shows maiores em espaços alugados. Documento de apoio ao Documento de Visão.

Os requisitos foram levantados na [entrevista com o dono do negócio](../entrevista.md). A coluna **Origem** aponta os problemas relatados, numerados de A01 a A16 na síntese da entrevista. A entrega exige no mínimo 15 requisitos funcionais detalhados; aqui estão 32 ativos.

Convenções:

- **Código**: identificador estável, nunca reaproveitado. O RF03 foi retirado e o código não volta a ser usado.
- **Ator**: perfil que executa a funcionalidade.
- **Prioridade**: Essencial (o produto não existe sem ele), Importante (perda relevante de valor), Desejável (melhoria).
- **Processo**: processo BPMN em que o requisito aparece, garantindo a coerência entre modelagem e requisitos.

| Código | Nome | Ator | Prioridade | Processo | Origem |
|---|---|---|---|---|---|
| RF01 | Gestão de usuários e perfis de acesso | Dono | Essencial | Apoio | Atores da entrevista |
| RF02 | Autenticação e recuperação de senha | Todos | Essencial | Apoio | Atores da entrevista |
| RF03 | *Retirado* | — | — | — | — |
| RF04 | Cadastro de locais e montagens | Dono | Essencial | P1 | A03 |
| RF05 | Cadastro de show | Dono | Essencial | P1 | A01 |
| RF06 | Gestão de sessões do show | Dono | Importante | P1 | A01 |
| RF07 | Gestão de lotes e tabela de preços | Sócio | Essencial | P1 | A04 |
| RF08 | Verificação e abertura das vendas | Dono, Sistema | Essencial | P1 | A04 |
| RF09 | Página pública de vendas do show | Cliente | Essencial | P1, P2 | A06 |
| RF10 | Carrinho com reserva temporária de ingressos | Cliente | Essencial | P2 | A04 |
| RF11 | Pagamento online com confirmação automática | Cliente | Essencial | P2 | A06 |
| RF12 | Emissão de ingresso digital com QR Code | Sistema | Essencial | P2, P3, P4 | A06 |
| RF13 | Meia-entrada e validação de comprovante | Cliente, Portaria | Importante | P2, P4 | A09 |
| RF14 | Cupons de desconto | Sócio | Desejável | P2 | Prioridade de lote promocional |
| RF15 | Cancelamento de compra e reembolso | Cliente, Dono e sócio, Bilheteria | Essencial | P3 | A12 |
| RF16 | Transferência e nominação de ingresso | Cliente | Importante | P4 | A11 |
| RF17 | Check-in e validação de acesso | Portaria | Essencial | P4 | A06 |
| RF18 | Operação offline da portaria e sincronização | Portaria | Essencial | P4 | A10 |
| RF19 | Escala da equipe com confirmação | Dono, Sócio, Equipe | Importante | P5 | A14 |
| RF20 | Atrações, fornecedores e contratos | Dono, Sócio | Importante | P1, P5 | A02 |
| RF21 | Cronograma de produção do dia do show | Sócio | Importante | P5 | Relato do dia do show |
| RF22 | Resultado financeiro e fechamento do show | Sócio, Dono | Essencial | P3, P6 | A16 |
| RF23 | Relatórios gerenciais e exportação | Dono, Sócio, Administrativo | Importante | P5, P6 | A16 |
| RF24 | Notificações e comunicação | Sistema | Importante | P1, P2, P3, P5 | A13, A14 |
| RF25 | Registro de auditoria das operações críticas | Sistema | Desejável | Apoio | A12, A15 |
| RF26 | Agenda de datas da casa | Dono, Sócio | Essencial | P1, P3 | A01 |
| RF27 | Distribuição de ingressos por canal | Dono | Essencial | P1, P2, P3 | A04 |
| RF28 | Lista de convidados com cotas | Dono, Portaria | Essencial | P1, P4 | A05 |
| RF29 | Venda pela loja parceira e acerto | Loja parceira, Sócio | Essencial | P1, P2, P3, P6 | A07 |
| RF30 | Venda e caixa da bilheteria na porta | Bilheteria | Essencial | P3, P4, P6 | A08 |
| RF31 | Remarcação e cancelamento de show | Dono e sócio | Importante | P3 | A13 |
| RF32 | Controle de lotação em tempo real | Portaria, Bilheteria | Essencial | P4 | A11 |
| RF33 | Lançamento de despesas e pagamentos | Sócio, Administrativo | Essencial | P1, P5, P6 | A02, A15 |

---

## RF01 — Gestão de usuários e perfis de acesso

**Ator:** Dono. **Prioridade:** Essencial. **Processo:** apoio a todos.

Permite cadastrar, editar, inativar e listar usuários do sistema, atribuindo a cada um os perfis Dono, Sócio, Administrativo, Bilheteria, Portaria, Loja parceira e Cliente. Um mesmo usuário pode acumular perfis; na Cena Livre, por exemplo, a mesma pessoa pode trabalhar na bilheteria e na portaria. O cadastro registra nome, CPF, telefone, e-mail, perfis e situação. O usuário da loja parceira fica vinculado ao parceiro e só enxerga a cota e as vendas desse parceiro. Usuários com operações registradas não podem ser excluídos, apenas inativados, preservando o histórico. A tentativa de acesso a uma função sem permissão é bloqueada e registrada conforme RF25.

**Dados registrados.** Deve conter nome completo, CPF, telefone, e-mail, perfis de acesso, loja parceira vinculada (quando o perfil for Loja parceira), data do cadastro e situação (ativo ou inativo).

## RF02 — Autenticação e recuperação de senha

**Ator:** Todos. **Prioridade:** Essencial. **Processo:** apoio a todos.

Permite o acesso mediante e-mail ou telefone e senha, com bloqueio temporário após cinco tentativas incorretas consecutivas. O cliente também pode se autenticar por conta Google. A recuperação de senha é feita por link de uso único enviado ao e-mail ou por código enviado ao telefone cadastrado, com validade de trinta minutos. Os perfis Dono e Sócio, que acessam os valores financeiros, exigem segundo fator de autenticação. A sessão dos perfis Bilheteria e Portaria permanece aberta durante toda a noite do show, para não interromper a fila com novo login.

**Dados registrados.** Deve conter login, senha protegida, data e hora do último acesso, quantidade de tentativas incorretas e, para os perfis Dono e Sócio, a configuração do segundo fator de autenticação.

## RF03 — Retirado

Cadastro de produtora com aprovação por administrador de plataforma. Retirado depois da entrevista, porque o sistema atende uma única casa de shows e não várias produtoras. O código não é reaproveitado.

## RF04 — Cadastro de locais e montagens

**Ator:** Dono. **Prioridade:** Essencial. **Processo:** P1. **Origem:** A03.

Permite cadastrar os locais onde os shows acontecem, a casa própria e os espaços alugados, como clubes e salões, com nome, endereço, capacidade máxima autorizada e, para espaços alugados, o valor do aluguel. Cada local possui uma ou mais montagens, por exemplo "Em pé" e "Com mesas ao lado do bar", cada uma com capacidade própria, porque o dono relatou que a lotação da casa muda conforme a disposição. A capacidade de uma montagem não pode ultrapassar a capacidade máxima do local. A montagem escolhida para o show define o total de lugares usado em RF27 e RF32.

**Dados registrados.** O local deve conter nome, tipo (próprio ou alugado), endereço (rua, número, bairro, cidade, UF e CEP), capacidade máxima autorizada, nome e telefone do responsável e valor do aluguel, quando alugado. A montagem deve conter local, nome (por exemplo Em pé ou Com mesas ao lado do bar), capacidade e observações.

## RF05 — Cadastro de show

**Ator:** Dono. **Prioridade:** Essencial. **Processo:** P1. **Origem:** A01.

Permite cadastrar o show com nome, atração principal, bandas de abertura, descrição, imagem de divulgação, classificação indicativa, local e montagem, política de meia-entrada e política de cancelamento. O show percorre as situações Em negociação, Confirmado, À venda, Realizado, Fechado e Cancelado. Nasce Em negociação, vinculado a uma pré-reserva de data de RF26, e só passa a Confirmado quando o contrato da atração é registrado em RF20. O sistema permite editar, duplicar e pesquisar shows por nome, período, local e situação. A duplicação copia montagem, lotes e cotas, poupando retrabalho em shows recorrentes.

**Dados registrados.** Deve conter nome do show, atração principal, bandas de abertura, gênero musical, descrição, imagem de divulgação, classificação indicativa, local, montagem, limite de ingressos por CPF, política de meia-entrada, política de cancelamento, data do cadastro e situação (Em negociação, Confirmado, À venda, Realizado, Fechado ou Cancelado).

## RF06 — Gestão de sessões do show

**Ator:** Dono. **Prioridade:** Importante. **Processo:** P1. **Origem:** A01.

Permite cadastrar uma ou mais sessões para o mesmo show, cada uma com data, horário de abertura da porta, horário de início e horário previsto de término. Um show que se repete em duas noites é um show com duas sessões, e cada sessão controla o próprio estoque de ingressos e a própria lotação. O horário de abertura da porta cadastrado aqui é o horário anunciado ao público, conferido contra o cronograma de RF21.

**Dados registrados.** Deve conter show, data, horário de abertura da porta, horário de início, horário previsto de término e situação.

## RF07 — Gestão de lotes e tabela de preços

**Ator:** Sócio. **Prioridade:** Essencial. **Processo:** P1. **Origem:** A04.

Permite definir os lotes de venda de cada sessão, com nome, quantidade, preço inteiro, preço de meia-entrada, data de início e data de fim. O primeiro lote pode ser marcado como promocional, prática relatada pelo dono para "criar movimento". A virada de lote ocorre automaticamente quando a quantidade se esgota ou quando a data final é atingida, o que acontecer primeiro. O preço de venda na porta é definido à parte, e pode ser informado na abertura das vendas ou apenas no dia do show, ponto que o dono ficou de confirmar com o sócio. O sistema mantém histórico dos preços praticados, necessário para o reembolso de RF15.

**Dados registrados.** Deve conter sessão, nome do lote, indicação de lote promocional, quantidade de ingressos, preço inteiro, preço de meia-entrada, data e hora de início, data e hora de fim e preço de venda na porta.

## RF08 — Verificação e abertura das vendas

**Ator:** Dono e Sistema. **Prioridade:** Essencial. **Processo:** P1. **Origem:** A04.

Antes de abrir as vendas, o sistema verifica se o show tem data confirmada em RF26, contrato da atração registrado em RF20, local e montagem definidos em RF04, ingressos distribuídos por canal em RF27, ao menos um lote configurado em RF07 e cotas de convidados definidas em RF28. As pendências são listadas ao dono para que ele complete. Sem pendências, o dono abre as vendas, o show passa a À venda, a página pública de RF09 é publicada e as cotas ficam disponíveis à loja parceira e à bilheteria. O dono relatou que o post do Instagram precisa sair com a venda pronta, então o link da página é gerado já nesse momento, para ser entregue a quem faz a divulgação.

**Dados registrados.** Deve conter data e hora da abertura, usuário que abriu as vendas, pendências encontradas e link da página de vendas.

## RF09 — Página pública de vendas do show

**Ator:** Cliente. **Prioridade:** Essencial. **Processos:** P1, P2. **Origem:** A06.

Disponibiliza, sem necessidade de login, uma página para cada show à venda, acessada pelo link divulgado no Instagram, com imagem, descrição, data, horário de abertura da porta, local, lotes disponíveis e preços, política de meia-entrada e política de cancelamento. Disponibiliza também a agenda pública com os próximos shows da casa. Lotes esgotados aparecem marcados como indisponíveis, e não ocultos. A página substitui o site feito por um conhecido, citado na entrevista, que não confirmava o pagamento sozinho.

**Dados registrados.** A página deve conter imagem de divulgação, nome do show, atrações, data, horário de abertura da porta, local com endereço, lotes disponíveis com preço inteiro e de meia-entrada, taxa de serviço destacada, política de meia-entrada e política de cancelamento.

## RF10 — Carrinho com reserva temporária de ingressos

**Ator:** Cliente. **Prioridade:** Essencial. **Processo:** P2. **Origem:** A04.

Permite ao cliente selecionar sessão, tipo de ingresso e quantidade, respeitando o limite por CPF definido para o show. Ao iniciar a compra, o sistema reserva os ingressos na cota do canal online de RF27 por quinze minutos, exibindo o tempo restante. Expirado o prazo sem pagamento aprovado, a reserva é liberada e os ingressos voltam à cota. A reserva impede que dois compradores levem o último ingresso ao mesmo tempo.

**Dados registrados.** Deve conter sessão, lote, tipo de ingresso, quantidade, valor unitário, taxa de serviço, valor total, data e hora de início e data e hora de expiração da reserva.

## RF11 — Pagamento online com confirmação automática

**Ator:** Cliente. **Prioridade:** Essencial. **Processo:** P2. **Origem:** A06.

Permite concluir a compra informando nome, CPF, e-mail e telefone e pagando por Pix ou cartão de crédito. O sistema envia a cobrança ao provedor de pagamento e aguarda a confirmação enviada pelo próprio provedor, sem depender de comprovante encaminhado pelo cliente. Esse é o ponto que elimina o print de comprovante reutilizado relatado pelo dono. Pagamento aprovado leva a compra a Paga e dispara a emissão de RF12. Pagamento recusado ou Pix não pago no prazo da reserva libera os ingressos. O sistema nunca armazena o número completo do cartão.

**Dados registrados.** Deve conter nome do comprador, CPF, e-mail, telefone, forma de pagamento, valor, código da transação no provedor, bandeira e quatro últimos dígitos do cartão, data e hora e situação (Aguardando pagamento, Paga, Recusada ou Expirada).

## RF12 — Emissão de ingresso digital com QR Code

**Ator:** Sistema. **Prioridade:** Essencial. **Processos:** P2, P3, P4. **Origem:** A06.

Gera, para cada ingresso pago, emitido pela loja parceira ou vendido na porta, um código único com QR Code assinado digitalmente, contendo show, sessão, tipo de ingresso, canal de venda e nome do portador. O ingresso é enviado por e-mail em PDF e fica disponível na área do cliente. Como o dono relatou que há quem chegue sem internet para abrir o código, o PDF pode ser salvo no aparelho e a portaria também encontra o ingresso pelo CPF em RF17. O código não é sequencial nem previsível. Ingressos cancelados em RF15 ficam inválidos para a portaria.

**Dados registrados.** Deve conter código único não sequencial, QR Code assinado digitalmente, show, sessão, data, lote, tipo de ingresso (inteira ou meia-entrada), canal de venda, nome e CPF do portador, data da emissão e situação (Válido, Utilizado, Cancelado ou Transferido).

## RF13 — Meia-entrada e validação de comprovante

**Ator:** Cliente e Portaria. **Prioridade:** Importante. **Processos:** P2, P4. **Origem:** A09.

Permite a compra de meia-entrada respeitando a cota definida por sessão, informando a categoria do benefício, por exemplo estudante, idoso, pessoa com deficiência, jovem de baixa renda ou professor quando houver lei local, e anexando o comprovante quando exigido. O ingresso de meia é sempre nominal e aparece destacado na tela da portaria, que só libera a entrada após marcar a conferência do documento em RF17. Esgotada a cota, o sistema oferece apenas ingressos inteiros. A quantidade de meias vendidas e conferidas aparece separada no resultado de RF22, atendendo à dificuldade do dono de separar meia-entrada no caixa.

**Dados registrados.** Deve conter categoria do benefício (estudante, idoso, pessoa com deficiência, jovem de baixa renda ou professor, quando houver lei local), nome e CPF do beneficiário, número do documento comprobatório, arquivo do comprovante quando exigido, resultado da conferência na porta e operador que conferiu.

## RF14 — Cupons de desconto

**Ator:** Sócio. **Prioridade:** Desejável. **Processo:** P2.

Permite criar cupons com código, desconto percentual ou valor fixo, quantidade de usos, validade e restrição por show ou sessão, para ações de divulgação. O cliente aplica o cupom no pagamento de RF11, com validação imediata e mensagem clara quando o cupom estiver expirado, esgotado ou não aplicável. Os descontos concedidos entram no resultado de RF22 como dedução de receita. Ingressos gratuitos para convidados não são cupons e seguem RF28.

**Dados registrados.** Deve conter código do cupom, tipo de desconto (percentual ou valor fixo), valor do desconto, quantidade máxima de usos, quantidade já usada, data de início, data de fim, show ou sessão em que é válido e situação.

## RF15 — Cancelamento de compra e reembolso

**Ator:** Cliente, Dono e sócio, Bilheteria. **Prioridade:** Essencial. **Processo:** P3. **Origem:** A12.

Permite ao cliente solicitar o cancelamento pela área do cliente ou pelo link do e-mail, e à bilheteria registrar pedidos feitos pessoalmente. O sistema localiza a compra pelo código ou CPF e aplica a política do show: devolução integral quando a solicitação ocorre até sete dias após a compra e até quarenta e oito horas antes da sessão, ou quando o show foi remarcado em RF31. Fora dessas condições, o pedido segue para análise do dono e do sócio, que aprovam ou recusam com justificativa. Aprovado o cancelamento, os ingressos são invalidados e voltam à cota do canal de origem. A devolução segue o canal da compra: estorno pelo provedor de pagamento para compras online, e devolução pela bilheteria ou pela loja parceira para as demais, sempre ao comprador identificado na venda. O dono relatou devolução feita à pessoa errada por nome parecido, então o registro exige o CPF de quem recebe.

**Dados registrados.** Deve conter código da compra, ingressos cancelados, nome e CPF do comprador, canal de origem, motivo, data do pedido, valor a devolver, forma de devolução, decisão, justificativa em caso de recusa, nome e CPF de quem recebeu o valor, data da devolução e responsável.

## RF16 — Transferência e nominação de ingresso

**Ator:** Cliente. **Prioridade:** Importante. **Processo:** P4. **Origem:** A11.

Permite ao comprador atribuir cada ingresso a um portador, informando nome e CPF, e transferir um ingresso não utilizado para outra pessoa. A transferência invalida o QR Code anterior e emite um novo, evitando dois códigos válidos para o mesmo lugar. O dono relatou confusão na porta com nomes escritos diferente do documento, por isso a portaria confere o portador pelo CPF e não pela grafia do nome. A transferência é bloqueada a partir de duas horas antes da abertura da porta.

**Dados registrados.** Deve conter ingresso, nome e CPF do portador atual, nome, CPF e e-mail do novo portador, data e hora da transferência e código do novo QR Code.

## RF17 — Check-in e validação de acesso

**Ator:** Portaria. **Prioridade:** Essencial. **Processo:** P4. **Origem:** A06.

Permite à portaria ler o QR Code pela câmera do celular, ou buscar por CPF ou nome, e obter em até dois segundos um de três resultados. Acesso liberado, quando o ingresso ou convite é válido, pertence à sessão e ainda não foi usado. Acesso negado, quando é inválido, cancelado, de outra sessão ou já usado, exibindo o motivo e o horário da entrada anterior. Verificação manual, quando o ingresso é de meia-entrada ou nominal, exigindo conferência do documento. Cada entrada registra data, hora, operador e ponto de entrada e atualiza a lotação de RF32. É o requisito que atende a segunda prioridade do dono: ninguém entra duas vezes com o mesmo comprovante.

**Dados registrados.** Deve conter ingresso ou convite, sessão, data e hora da entrada, operador, ponto de entrada, resultado (liberado, negado ou conferência de documento) e motivo da negativa.

## RF18 — Operação offline da portaria e sincronização

**Ator:** Portaria. **Prioridade:** Essencial. **Processo:** P4. **Origem:** A10.

Permite que o aplicativo de portaria baixe antes da abertura da porta os ingressos válidos e a lista de convidados da sessão e continue validando sem conexão, situação que já aconteceu na Cena Livre e obrigou a equipe a usar a lista impressa. As entradas feitas offline ficam em fila local e são enviadas ao servidor quando a conexão volta. Com mais de um celular na porta, os aparelhos trocam as entradas entre si pela rede local quando disponível. Havendo conflito, o sistema mantém o primeiro registro pelo horário e marca o segundo como duplicidade no relatório de ocorrências.

**Dados registrados.** Deve conter lista de ingressos válidos e de convidados da sessão baixada no aparelho, data e hora do último download, fila de entradas registradas sem conexão, data e hora da sincronização e ocorrências de duplicidade.

## RF19 — Escala da equipe com confirmação

**Ator:** Dono, Sócio e Equipe. **Prioridade:** Importante. **Processo:** P5. **Origem:** A14.

Permite montar a equipe de cada sessão por função, técnico de som, técnico de luz, segurança, bilheteria, bar e portaria, com nome, telefone, horário de chegada e forma de cobrança, por show ou por diária. O sistema envia o convite a cada pessoa com data, função, horário e valor, e a pessoa confirma ou recusa pelo link recebido. O dono vê quem ainda não confirmou e substitui a pessoa ou registra a contratação de empresa terceirizada, tratada como fornecedor em RF20. No dia, o sócio registra a presença efetiva, e o valor devido de cada presença gera uma despesa pendente em RF33.

**Dados registrados.** Deve conter sessão, nome, CPF, telefone, função (som, luz, segurança, bilheteria, bar ou portaria), horário de chegada, horário de saída, forma de cobrança (por show ou por diária), valor combinado, situação do convite (enviado, confirmado ou recusado) e presença registrada.

## RF20 — Atrações, fornecedores e contratos

**Ator:** Dono e Sócio. **Prioridade:** Importante. **Processos:** P1, P5. **Origem:** A02.

Permite cadastrar as atrações do show, com nome artístico, contato do empresário, cachê, valor e data do sinal, forma de pagamento do restante e requisitos técnicos, e os fornecedores, como empresa de segurança terceirizada, aluguel de som e luz e aluguel de espaço, com valores e prazos combinados. Permite anexar o contrato ou, na falta dele, a imagem da mensagem que confirmou data e cachê, prática relatada pelo dono. Cada compromisso tem situação Combinado, Sinal pago ou Quitado. O sócio usa o cachê informado para avaliar a viabilidade do show antes de confirmá-lo, e os valores compõem as despesas previstas de RF33.

**Dados registrados.** A atração deve conter nome artístico, nome e telefone do empresário, cachê, valor e data do sinal, forma e data de pagamento do restante e requisitos técnicos. O fornecedor deve conter nome ou razão social, CPF ou CNPJ, telefone, tipo de serviço (segurança, som, luz ou aluguel de espaço), valor combinado e prazo de pagamento. Ambos devem conter o arquivo do contrato ou a imagem da mensagem que confirmou o acordo e a situação (Combinado, Sinal pago ou Quitado).

## RF21 — Cronograma de produção do dia do show

**Ator:** Sócio. **Prioridade:** Importante. **Processo:** P5.

Permite montar a linha do tempo da sessão, com montagem do equipamento, passagem de som, abertura da porta, banda de abertura, show principal e desmontagem, cada etapa com horário previsto e responsável. O sistema alerta quando o horário de abertura da porta no cronograma diverge do horário anunciado em RF06. Durante o dia, o responsável marca cada etapa como concluída, e um atraso destaca as etapas seguintes. A liberação da portaria em P4 depende da conclusão da passagem de som, porque o dono relatou que o público não pode entrar durante o teste de equipamento.

**Dados registrados.** Cada etapa deve conter sessão, nome da etapa (montagem, passagem de som, abertura da porta, banda de abertura, show principal ou desmontagem), horário previsto, horário real, responsável e situação.

## RF22 — Resultado financeiro e fechamento do show

**Ator:** Sócio e Dono. **Prioridade:** Essencial. **Processos:** P3, P6. **Origem:** A16.

Apresenta por show e por sessão as receitas separadas por canal, online, loja parceira e porta, os descontos, os reembolsos, a comissão da loja parceira, as despesas lançadas em RF33 e o resultado. Logo após o fechamento do caixa da porta, o sistema exibe um resultado prévio, a terceira prioridade do dono, com os valores a receber ainda marcados como pendentes. O fechamento definitivo é feito pelo sócio depois da conferência das despesas e da confirmação do acerto da loja parceira em RF29, congelando os valores. Shows fechados ficam bloqueados para novos lançamentos, e a reabertura exige justificativa registrada em RF25.

**Dados registrados.** Deve conter, por sessão, receita da venda online, receita da loja parceira, receita da porta, quantidade de inteiras, meias-entradas e convidados, descontos de cupons, reembolsos, comissão da loja parceira, taxas do provedor de pagamento, despesas por categoria, resultado, valores ainda a receber, data do fechamento e responsável.

## RF23 — Relatórios gerenciais e exportação

**Ator:** Dono, Sócio e Administrativo. **Prioridade:** Importante. **Processos:** P5, P6. **Origem:** A16.

Disponibiliza relatórios de vendas por canal, lote e forma de pagamento, curva de vendas ao longo do tempo, taxa de comparecimento comparando ingressos vendidos e entradas registradas, uso da lista de convidados por solicitante, ocorrências da portaria e do show e resultado por show, com comparação entre shows na casa e em espaços alugados. Todos os relatórios permitem filtro por período e show e exportação em planilha e PDF, para uso da pessoa que hoje monta a planilha e do contador. O resumo do resultado é apresentado em tela simples no celular, pensando no sócio, que "só quer ver número final".

**Dados registrados.** Deve conter os relatórios de vendas por canal, lote e forma de pagamento; curva de vendas por dia; comparecimento, com ingressos vendidos e entradas registradas; uso da lista de convidados por solicitante; ocorrências da portaria e do show; e resultado por show, comparando shows na casa e em espaços alugados.

## RF24 — Notificações e comunicação

**Ator:** Sistema. **Prioridade:** Importante. **Processos:** P1, P2, P3, P5. **Origem:** A13, A14.

Envia automaticamente por e-mail e por mensagem ao telefone a confirmação de compra com o ingresso, o aviso de pagamento recusado ou expirado, a confirmação de cancelamento e reembolso, o lembrete do show vinte e quatro horas antes, o aviso de remarcação ou cancelamento de show de RF31, o convite de escala de RF19 e o aviso de liberação de cota à loja parceira. Permite ainda ao dono enviar comunicado a todos os compradores de uma sessão, por exemplo mudança de horário da porta. Toda comunicação registra data, destinatário e situação de entrega.

**Dados registrados.** Deve conter tipo da mensagem, destinatário, canal (e-mail ou telefone), texto, data e hora do envio e situação da entrega.

## RF25 — Registro de auditoria das operações críticas

**Ator:** Sistema. **Prioridade:** Desejável. **Processo:** apoio a todos. **Origem:** A12, A15.

Registra em trilha somente leitura as operações sensíveis: alteração de preços e cotas, inclusão de convidado acima da cota, cancelamentos e reembolsos, vendas e sangrias do caixa da porta, lançamento e exclusão de despesas, fechamento e reabertura de show e tentativas de acesso negadas. Cada registro guarda usuário, data e hora, operação, valor anterior e valor novo. A trilha é consultável pelo dono e pelo sócio, com filtros de período, usuário e tipo de operação, e é retida por cinco anos.

**Dados registrados.** Deve conter usuário, data e hora, tipo de operação, registro afetado, valor anterior e valor novo.

## RF26 — Agenda de datas da casa

**Ator:** Dono e Sócio. **Prioridade:** Essencial. **Processos:** P1, P3. **Origem:** A01.

Substitui o caderno de datas. Apresenta um calendário por local com cada data nas situações Livre, Pré-reservada ou Confirmada. Ao receber uma proposta, o dono consulta a agenda e pré-reserva a data, informando a atração e a validade da pré-reserva. O sistema impede duas pré-reservas ou confirmações para o mesmo local e horário, resolvendo o episódio relatado de quase marcar dois shows no mesmo sábado. A pré-reserva é liberada quando o show é descartado, quando vence sem confirmação ou quando o show é remarcado para outra data em RF31. O dono e o sócio veem a mesma agenda pelo celular.

**Dados registrados.** Deve conter local, data, horário de início e de fim, show ou atração, situação (Livre, Pré-reservada ou Confirmada), validade da pré-reserva, usuário que reservou e data da reserva.

## RF27 — Distribuição de ingressos por canal

**Ator:** Dono. **Prioridade:** Essencial. **Processos:** P1, P2, P3. **Origem:** A04.

Permite dividir a capacidade da montagem escolhida em cotas por canal: venda online, loja parceira, bilheteria da porta e lista de convidados. A soma das cotas não pode ultrapassar a capacidade. Todas as vendas e reservas, de qualquer canal, baixam de um único estoque consolidado, e o dono vê em tempo real, pelo celular, quanto foi vendido e quanto resta em cada canal e no total, atendendo à primeira prioridade relatada. O dono pode remanejar saldo não vendido de um canal para outro a qualquer momento, e o sistema avisa quando uma cota atinge noventa por cento. Ingressos cancelados voltam à cota do canal de origem.

**Dados registrados.** Deve conter sessão, capacidade total, cota e saldo da venda online, cota e saldo da loja parceira, cota e saldo da bilheteria da porta, cota e saldo de convidados, total vendido e total disponível.

## RF28 — Lista de convidados com cotas

**Ator:** Dono e Portaria. **Prioridade:** Essencial. **Processos:** P1, P4. **Origem:** A05.

Tira a lista de convidados "da cabeça" do dono. Permite definir, por sessão, quem pode indicar convidados, por exemplo dono, sócio, banda e imprensa, e a cota de cada um. Cada indicado é cadastrado com nome e CPF e ocupa um lugar da cota de convidados de RF27. Incluir nomes acima da cota do solicitante exige aprovação do dono pelo celular, e a inclusão fica registrada em RF25. A lista fecha em horário definido antes da abertura da porta e é baixada pela portaria em RF18. Na porta, o convidado é encontrado pelo CPF ou pelo nome, e cada convite só dá direito a uma entrada. O relatório de RF23 mostra quantos convidados cada solicitante usou, dado que o dono apontou como ingresso que deixou de vender.

**Dados registrados.** O solicitante deve conter nome (dono, sócio, banda ou imprensa) e cota de convites. O convidado deve conter nome completo, CPF, solicitante, data da inclusão, aprovação do dono quando acima da cota e situação da entrada.

## RF29 — Venda pela loja parceira e acerto

**Ator:** Loja parceira e Sócio. **Prioridade:** Essencial. **Processos:** P1, P2, P3, P6. **Origem:** A07.

Permite cadastrar a loja parceira com percentual de comissão e prazo de repasse combinados. O vendedor da loja registra cada venda no momento em que ela acontece, pelo celular, informando nome e CPF do comprador, tipo de ingresso e forma de pagamento. A venda baixa da cota do parceiro em RF27 e gera o ingresso com QR Code de RF12. O dono deixa de depender da planilha enviada dias depois, porque vê as vendas da loja em tempo real. Após o show, o sistema calcula o acerto, total vendido menos a comissão, e o sócio registra o recebimento do repasse, que libera o fechamento de RF22. Cancelamentos de ingressos vendidos na loja são registrados pela própria loja, que devolve o valor ao comprador identificado.

**Dados registrados.** A loja deve conter nome, CNPJ ou CPF, endereço, telefone, responsável, percentual de comissão e prazo de repasse. Cada venda deve conter sessão, tipo de ingresso, quantidade, valor, forma de pagamento, nome e CPF do comprador, vendedor e data e hora. O acerto deve conter total vendido, comissão, valor a repassar, data prevista, data do recebimento e usuário que confirmou.

## RF30 — Venda e caixa da bilheteria na porta

**Ator:** Bilheteria. **Prioridade:** Essencial. **Processos:** P3, P4, P6. **Origem:** A08.

Permite à bilheteria abrir o caixa da noite informando o valor inicial em dinheiro, vender ingressos na porta pelo celular recebendo em dinheiro, Pix ou cartão, e emitir o ingresso na hora, que segue para a validação normal da portaria. A venda só é concluída se houver lugar segundo RF32. Toda retirada de dinheiro do caixa, como o pagamento de alguém da equipe durante a noite, é registrada como sangria com motivo e vira despesa em RF33, porque o dono relatou que esse dinheiro "nem deixa rastro". Ao final, a bilheteria fecha o caixa informando o valor contado, e o sistema aponta a diferença em relação ao esperado.

**Dados registrados.** O caixa deve conter sessão, operador, valor inicial, data e hora de abertura, valor contado no fechamento, valor esperado, diferença e data e hora de fechamento. A venda deve conter tipo de ingresso, quantidade, valor, forma de pagamento (dinheiro, Pix ou cartão) e nome e CPF do comprador. A sangria deve conter valor, motivo e quem recebeu o dinheiro.

## RF31 — Remarcação e cancelamento de show

**Ator:** Dono e sócio. **Prioridade:** Importante. **Processo:** P3. **Origem:** A13.

Permite remarcar a sessão para nova data, consultando e confirmando a data em RF26, ou cancelar o show inteiro. Na remarcação, os ingressos continuam válidos para a nova data e o sistema avisa todos os compradores por RF24, abrindo um prazo em que o pedido de reembolso é aprovado automaticamente em RF15, porque o dono relatou que nem todos querem ir na nova data. No cancelamento, todos os compradores são avisados e os reembolsos são gerados sem necessidade de pedido. Compromissos com atração e fornecedores são sinalizados para renegociação em RF20.

**Dados registrados.** Deve conter sessão, data original, nova data, motivo, tipo (remarcação ou cancelamento), prazo para pedido de reembolso, data da decisão e responsável.

## RF32 — Controle de lotação em tempo real

**Ator:** Portaria e Bilheteria. **Prioridade:** Essencial. **Processo:** P4. **Origem:** A11.

Mantém a contagem de pessoas dentro da casa a partir das entradas registradas em RF17, exibida a todos os celulares da portaria e da bilheteria, comparada à capacidade da montagem de RF04. O sistema alerta ao atingir noventa por cento e bloqueia a venda na porta ao atingir a capacidade, evitando o episódio relatado de casa lotada com risco de multa dos bombeiros. Havendo saída definitiva registrada pela portaria, a contagem é reduzida. Operando offline, cada aparelho soma as próprias entradas às últimas recebidas dos demais e sinaliza que a contagem pode estar defasada.

**Dados registrados.** Deve conter sessão, capacidade da montagem, total de entradas, total de saídas definitivas, pessoas dentro, percentual de ocupação e horário da última atualização.

## RF33 — Lançamento de despesas e pagamentos

**Ator:** Sócio e Administrativo. **Prioridade:** Essencial. **Processos:** P1, P5, P6. **Origem:** A02, A15.

Permite lançar cada despesa do show, cachê, sinal da atração, equipe, segurança terceirizada, som, luz, aluguel de espaço e outros, com valor, data, quem recebeu, forma de pagamento, origem do dinheiro, caixa da porta ou conta, e foto do recibo ou nota. As despesas previstas em RF19 e RF20 aparecem como pendentes até serem pagas. O lançamento pode ser feito pelo celular durante a noite, para que pagamentos em dinheiro não se percam. Antes do fechamento, a pessoa do administrativo confere as despesas e os comprovantes e lança o que faltar. Despesas lançadas alimentam o resultado de RF22.

**Dados registrados.** Deve conter show, categoria (cachê, sinal, equipe, segurança, som, luz, aluguel, divulgação ou outros), descrição, valor, data do pagamento, quem recebeu, forma de pagamento, origem do dinheiro (caixa da porta ou conta), foto do recibo ou nota, situação (prevista ou paga) e usuário que lançou.
