# Documento de Visão: Sistema "Palco"

**Disciplina:** Análise de Sistemas — 3º Semestre ADS — IFBA Irecê
**Professor:** Wild Barreto
**Cliente:** Cena Livre, casa de shows
**Data:** ___/___/______  **Versão:** 0.2
**Autor:** Eduardo de Souza Silva

---

## Sumário

1. [Introdução](#1-introdução)
   1. [Objetivos deste documento](#11-objetivos-deste-documento)
   2. [Escopo do produto](#12-escopo-do-produto)
   3. [Definições, acrônimos e abreviações](#13-definições-acrônimos-e-abreviações)
2. [Contexto](#2-contexto)
   1. [Declaração do problema](#21-declaração-do-problema)
   2. [Descrição dos usuários](#22-descrição-dos-usuários)
3. [Requisitos específicos](#3-requisitos-específicos)
   1. [Requisitos funcionais](#31-requisitos-funcionais)
   2. [Requisitos não funcionais](#32-requisitos-não-funcionais)
4. [Lista de riscos](#4-lista-de-riscos)
5. [Lista de restrições](#5-lista-de-restrições)
   1. [De hardware](#51-de-hardware)
   2. [De software](#52-de-software)
6. [Anexos: diagramas BPMN](#6-anexos-diagramas-bpmn)

---

## 1. Introdução

Este documento apresenta uma visão geral do sistema "Palco", construído para a Cena Livre, casa de shows com capacidade para cerca de quatrocentas pessoas, que também realiza shows maiores em espaços alugados. O sistema cobre desde a proposta de um show até o fechamento das contas depois da apresentação. O texto descreve o problema relatado pelo dono do negócio, os usuários envolvidos, as funções que o sistema deve oferecer e as condições sob as quais deve funcionar.

As necessidades foram levantadas por entrevista com o dono da Cena Livre. A transcrição completa e a síntese dos problemas relatados, numerados de A01 a A16, estão em [entrevista.md](entrevista.md) e são citadas ao longo deste documento.

### 1.1 Objetivos deste documento

Descrever e especificar as necessidades da Cena Livre na organização da agenda, na venda de ingressos pelos diferentes canais, no controle da entrada do público e na apuração do resultado financeiro de cada show, necessidades que devem ser atendidas pelo produto "Palco", bem como definir para os desenvolvedores o produto a ser feito.

Público-alvo: cliente, usuários e desenvolvedores do projeto "Palco".

### 1.2 Escopo do produto

O produto a ser desenvolvido é o sistema "Palco".

A missão do sistema é dar ao dono e ao sócio da Cena Livre controle, em tempo real e pelo celular, de quantos ingressos foram vendidos em cada canal, de quem entrou na casa e de quanto cada show deu de resultado.

Estão no escopo:

- Agenda de datas da casa e dos espaços alugados, sem conflito de datas.
- Cadastro de shows, sessões, locais e montagens, atrações, fornecedores e contratos.
- Distribuição dos ingressos entre venda online, loja parceira, bilheteria da porta e lista de convidados, com estoque único.
- Página de vendas do show divulgada no Instagram, com pagamento por Pix ou cartão confirmado automaticamente.
- Venda registrada pela loja parceira e acerto da comissão.
- Venda e caixa da bilheteria na porta.
- Ingresso digital com QR Code, lista de convidados com cotas e meia-entrada com conferência.
- Entrada do público pelo celular da portaria, com operação offline e controle de lotação.
- Cancelamento, reembolso e remarcação de show.
- Escala da equipe com confirmação, cronograma do dia e lançamento de despesas.
- Resultado prévio logo após o show, fechamento financeiro e relatórios.

Estão fora do escopo desta versão:

- Emissão de nota fiscal e integração com sistemas contábeis.
- Controle de vendas do bar e de estoque de bebidas.
- Aplicativo nativo para o público, atendido pela página responsiva.
- Publicação automática de posts no Instagram.
- Venda de ingressos para outras produtoras ou casas de show.

### 1.3 Definições, acrônimos e abreviações

| Nº | Sigla ou termo | Definição |
|---|---|---|
| 1 | Show | Apresentação comercializada pela Cena Livre, com uma atração principal e, às vezes, bandas de abertura. |
| 2 | Sessão | Ocorrência datada de um show. Um show em duas noites é um show com duas sessões. |
| 3 | Montagem | Disposição do local que define sua capacidade, por exemplo público em pé ou com mesas ao lado do bar. |
| 4 | Canal de venda | Meio pelo qual o ingresso é vendido: online, loja parceira ou bilheteria da porta. |
| 5 | Cota | Parte da capacidade reservada a um canal de venda ou à lista de convidados. |
| 6 | Lote | Faixa de venda com quantidade, preço e vigência. O primeiro costuma ser promocional. |
| 7 | Lista de convidados | Relação nominal de pessoas com entrada gratuita, indicadas por dono, sócio, banda ou imprensa. |
| 8 | Meia-entrada | Ingresso com desconto legal de cinquenta por cento, sujeito a cota e comprovação. |
| 9 | Loja parceira | Estabelecimento que vende ingressos em loja física e repassa o valor descontada uma comissão. |
| 10 | Acerto | Apuração e repasse do valor vendido pela loja parceira, descontada a comissão combinada. |
| 11 | Sangria | Retirada de dinheiro do caixa da bilheteria durante a noite, por exemplo para pagar a equipe. |
| 12 | Check-in | Registro da entrada do portador do ingresso ou convite na portaria. |
| 13 | QR Code | Código bidimensional do ingresso digital, lido pela câmera do celular da portaria. |
| 14 | Pré-reserva | Bloqueio provisório de uma data na agenda enquanto o show está em negociação. |
| 15 | PSP | Provedor de serviços de pagamento, responsável por processar cobranças e estornos. |
| 16 | BPMN | Business Process Model and Notation, notação de modelagem de processos de negócio. |
| 17 | LGPD | Lei Geral de Proteção de Dados, Lei 13.709 de 2018. |
| 18 | RF | Requisito funcional. |
| 19 | RNF | Requisito não funcional. |

---

## 2. Contexto

### 2.1 Declaração do problema

A Cena Livre é administrada por dois sócios: um cuida da parte artística e o outro do dinheiro. Toda a operação acontece por caderno, planilha e WhatsApp, e o próprio dono resume a situação dizendo que administra o negócio "no sentimento".

O show nasce de uma ligação de empresário ou de uma ideia do sócio. A data é conferida num caderno com anotações que ninguém sabe se foram fechadas, e a casa já quase marcou dois shows no mesmo sábado (A01). O cachê é combinado por mensagem, sem contrato, e às vezes há sinal pago antes de qualquer venda (A02). A quantidade de ingressos muda conforme a montagem da casa (A03), e a divisão entre lote promocional, loja parceira e porta é feita no chute, de modo que cada canal acredita ter mais ingressos do que existem (A04). A lista de convidados fica na cabeça do dono, sem limite, e cada nome a mais é um ingresso que deixou de ser vendido (A05).

Na venda online, o comprador envia o print do comprovante pelo WhatsApp, e o mesmo print já foi usado por duas pessoas (A06). A loja parceira informa suas vendas por planilha dias depois, sem possibilidade de conferência (A07), e a venda na porta é feita em dinheiro ou Pix sem registro integrado (A08). O resultado é que ninguém sabe quantos ingressos foram vendidos até alguém somar tudo, dois dias depois do show.

Na porta, a conferência é feita em lista impressa. A meia-entrada é liberada sem olhar o documento quando a fila cresce (A09), a internet já caiu e só uma lista impressa por acaso evitou a entrada sem controle (A10), e a casa já lotou com pessoas de ingresso na mão do lado de fora, com risco de multa e de segurança (A11). Quando um show é adiado, parte do público quer o dinheiro de volta (A13), e a devolução, sem registro de quem comprou, já foi feita à pessoa errada (A12).

A equipe é chamada por mensagem e há quem esqueça o compromisso (A14). Parte dos pagamentos sai em dinheiro do caixa da porta durante a noite, sem registro (A15). No fechamento, os sócios juntam caderno, extrato e recibos avulsos, e a planilha montada dias depois só dá uma ideia aproximada do resultado (A16).

O problema afeta os sócios, que perdem dinheiro sem saber onde, a bilheteria e a portaria, que trabalham sem ferramenta e sob pressão, e o público, que enfrenta fila, insegurança na compra e dificuldade para ser reembolsado. O dono declarou três prioridades: saber na hora quantos ingressos restam em todos os canais, impedir que o mesmo comprovante entre duas vezes e ver o lucro ou prejuízo logo depois do show. Uma solução adequada precisa concentrar agenda, vendas, entrada e dinheiro num mesmo registro, funcionar no celular de quem não usa computador e continuar validando ingressos quando a internet cair.

### 2.2 Descrição dos usuários

| Nº | Usuário | Descrição |
|---|---|---|
| 1 | Dono | Responsável pela parte artística. Consulta a agenda, fecha com as bandas, define montagem, cotas e lista de convidados, abre as vendas e acompanha tudo pelo celular. Declarou não ter familiaridade com computador. |
| 2 | Sócio | Responsável pelo dinheiro. Avalia cachê e preço, define lotes, organiza o cronograma com o técnico de som, lança pagamentos e fecha o show. Quer ver principalmente o resultado final. |
| 3 | Administrativo | Pessoa que hoje posta no Instagram, imprime listas e monta a planilha de fechamento. Confere despesas e comprovantes e emite relatórios, geralmente pelo computador. |
| 4 | Bilheteria | Vende ingressos na porta, controla o caixa da noite, atende pedidos de reembolso presenciais e devolve valores. |
| 5 | Portaria | Confere ingressos, convidados e meia-entrada na entrada do público, pelo celular, inclusive sem internet. |
| 6 | Loja parceira | Estabelecimento externo que vende ingressos na loja física, registra cada venda no sistema e faz o acerto após o show. |
| 7 | Equipe e fornecedores | Técnicos de som e luz, seguranças fixos e terceirizados e pessoal do bar. Recebem o convite de escala e confirmam a disponibilidade. |
| 8 | Cliente | Público comprador. Compra pela página do show, recebe o ingresso digital, transfere ingressos e pede cancelamento. |
| 9 | Provedor de pagamento | Ator externo. Processa cobranças por Pix e cartão, confirma pagamentos e executa estornos. |

---

## 3. Requisitos específicos

### 3.1 Requisitos funcionais

O quadro abaixo descreve cada requisito funcional com as operações permitidas, os dados que deve conter e as regras de funcionamento. São 32 requisitos funcionais ativos, acima do mínimo de 15 pedido na entrega. O RF03, cadastro de produtora com aprovação por administrador de plataforma, foi retirado depois da entrevista, porque o sistema atende uma única casa de shows; o código não é reaproveitado.

| Código | Nome | Descrição |
|---|---|---|
| RF01 | Gestão de usuários e perfis | Esta funcionalidade deve permitir ao dono cadastrar os usuários que terão acesso ao sistema e atribuir a cada um os perfis Dono, Sócio, Administrativo, Bilheteria, Portaria, Loja parceira ou Cliente. Pode-se cadastrar, editar, pesquisar, listar e inativar. Deve conter nome completo, CPF, telefone, e-mail, perfis de acesso, loja parceira vinculada (quando o perfil for Loja parceira), data do cadastro e situação (ativo ou inativo). Um mesmo usuário pode acumular perfis. Usuários que já registraram operações não podem ser excluídos, apenas inativados, e cada perfil só enxerga as telas e ações permitidas a ele. |
| RF02 | Autenticação e recuperação de senha | Esta funcionalidade deve permitir que os usuários acessem o sistema informando e-mail ou telefone e senha; o cliente também pode entrar com a conta Google. Deve conter login, senha protegida, data e hora do último acesso, quantidade de tentativas incorretas e, para os perfis Dono e Sócio, a configuração do segundo fator de autenticação. Após cinco tentativas incorretas seguidas, a conta fica bloqueada por quinze minutos. A recuperação de senha é feita por link ou código de uso único enviado ao e-mail ou ao telefone, válido por trinta minutos. Os perfis Bilheteria e Portaria permanecem conectados durante toda a noite do show. |
| RF04 | Cadastro de locais e montagens | Esta funcionalidade deve permitir ao dono cadastrar os locais onde os shows acontecem, a casa própria e os espaços alugados, e as montagens de cada local. Pode-se cadastrar, editar, pesquisar, listar e inativar. O local deve conter nome, tipo (próprio ou alugado), endereço (rua, número, bairro, cidade, UF e CEP), capacidade máxima autorizada, nome e telefone do responsável e valor do aluguel, quando alugado. A montagem deve conter local, nome (por exemplo Em pé ou Com mesas ao lado do bar), capacidade e observações. A capacidade da montagem não pode ultrapassar a capacidade máxima do local. |
| RF05 | Cadastro de show | Esta funcionalidade deve permitir ao dono cadastrar os shows da casa. Pode-se cadastrar, editar, duplicar, pesquisar e listar. Deve conter nome do show, atração principal, bandas de abertura, gênero musical, descrição, imagem de divulgação, classificação indicativa, local, montagem, limite de ingressos por CPF, política de meia-entrada, política de cancelamento, data do cadastro e situação (Em negociação, Confirmado, À venda, Realizado, Fechado ou Cancelado). O show nasce Em negociação e só passa a Confirmado quando o contrato da atração é registrado. A pesquisa filtra por nome, período, local e situação, e a duplicação copia montagem, lotes e cotas. |
| RF06 | Gestão de sessões | Esta funcionalidade deve permitir ao dono cadastrar uma ou mais sessões para o mesmo show, como no caso de um show em duas noites. Pode-se cadastrar, editar, listar e excluir sessões que ainda não tenham vendas. Deve conter show, data, horário de abertura da porta, horário de início, horário previsto de término e situação. Cada sessão tem estoque de ingressos e lotação próprios. O horário de abertura da porta é o horário anunciado ao público e é comparado com o cronograma do dia. |
| RF07 | Gestão de lotes e preços | Esta funcionalidade deve permitir ao sócio definir os lotes de venda de cada sessão. Pode-se cadastrar, editar, listar e encerrar lotes. Deve conter sessão, nome do lote, indicação de lote promocional, quantidade de ingressos, preço inteiro, preço de meia-entrada, data e hora de início, data e hora de fim e preço de venda na porta. A virada para o lote seguinte é automática quando a quantidade se esgota ou quando chega a data final, o que ocorrer primeiro. A soma das quantidades não pode passar da capacidade da montagem, e o histórico de preços é mantido para o cálculo de reembolsos. |
| RF08 | Verificação e abertura das vendas | Esta funcionalidade deve permitir ao dono abrir as vendas de um show depois que o sistema confere se tudo está pronto. O sistema verifica se há data confirmada na agenda, contrato da atração registrado, local e montagem definidos, ingressos distribuídos por canal, ao menos um lote configurado e cotas de convidados definidas, e lista ao dono o que estiver pendente. Deve conter data e hora da abertura, usuário que abriu as vendas, pendências encontradas e link da página de vendas. Sem pendências, o show passa a À venda, a página pública é publicada e as cotas são liberadas à loja parceira e à bilheteria, com o link já pronto para a divulgação no Instagram. |
| RF09 | Página pública de vendas | Esta funcionalidade deve permitir a qualquer pessoa, sem login, acessar pelo link divulgado no Instagram a página de um show à venda e a agenda com os próximos shows da casa. A página deve conter imagem de divulgação, nome do show, atrações, data, horário de abertura da porta, local com endereço, lotes disponíveis com preço inteiro e de meia-entrada, taxa de serviço destacada, política de meia-entrada e política de cancelamento. Lotes esgotados aparecem como indisponíveis, e não escondidos. A agenda pode ser pesquisada por data e por nome do show. |
| RF10 | Carrinho com reserva temporária | Esta funcionalidade deve permitir ao cliente escolher sessão, tipo de ingresso (inteira ou meia-entrada) e quantidade, respeitando o limite por CPF do show. Deve conter sessão, lote, tipo de ingresso, quantidade, valor unitário, taxa de serviço, valor total, data e hora de início e data e hora de expiração da reserva. Ao iniciar a compra, o sistema retira os ingressos da cota de venda online por quinze minutos e mostra o tempo restante. Se o pagamento não for aprovado nesse prazo, a reserva expira e os ingressos voltam à cota. |
| RF11 | Pagamento online com confirmação automática | Esta funcionalidade deve permitir ao cliente pagar a compra por Pix ou cartão de crédito. Deve conter nome do comprador, CPF, e-mail, telefone, forma de pagamento, valor, código da transação no provedor, bandeira e quatro últimos dígitos do cartão, data e hora e situação (Aguardando pagamento, Paga, Recusada ou Expirada). A confirmação do pagamento vem do próprio provedor, sem comprovante enviado pelo cliente. Pagamento aprovado dispara a emissão do ingresso; pagamento recusado ou expirado libera a reserva. O sistema nunca guarda o número completo nem o código de segurança do cartão. |
| RF12 | Emissão de ingresso com QR Code | Esta funcionalidade deve gerar automaticamente um ingresso digital para cada ingresso pago online, vendido pela loja parceira ou vendido na porta. Deve conter código único não sequencial, QR Code assinado digitalmente, show, sessão, data, lote, tipo de ingresso (inteira ou meia-entrada), canal de venda, nome e CPF do portador, data da emissão e situação (Válido, Utilizado, Cancelado ou Transferido). O ingresso é enviado por e-mail em PDF, que pode ser salvo no celular para uso sem internet, e fica disponível na área do cliente. O cliente pode reenviar o PDF sem gerar um novo código. |
| RF13 | Meia-entrada e comprovante | Esta funcionalidade deve permitir ao cliente comprar meia-entrada dentro da cota da sessão e à portaria conferir o direito ao benefício na entrada. Deve conter categoria do benefício (estudante, idoso, pessoa com deficiência, jovem de baixa renda ou professor, quando houver lei local), nome e CPF do beneficiário, número do documento comprobatório, arquivo do comprovante quando exigido, resultado da conferência na porta e operador que conferiu. O ingresso de meia-entrada é sempre nominal e aparece destacado para a portaria, que só libera a entrada após conferir o documento. Esgotada a cota, o sistema vende apenas inteira. |
| RF14 | Cupons de desconto | Esta funcionalidade deve permitir ao sócio criar cupons de desconto para ações de divulgação. Pode-se cadastrar, editar, pesquisar, listar e desativar. Deve conter código do cupom, tipo de desconto (percentual ou valor fixo), valor do desconto, quantidade máxima de usos, quantidade já usada, data de início, data de fim, show ou sessão em que é válido e situação. O cliente aplica o cupom no pagamento online e recebe mensagem clara quando o cupom estiver vencido, esgotado ou não valer para aquele show. Os descontos concedidos entram no resultado do show. |
| RF15 | Cancelamento e reembolso | Esta funcionalidade deve permitir ao cliente, pela área do cliente, ou à bilheteria, no atendimento presencial, pedir o cancelamento de uma compra, e ao dono e ao sócio decidir os pedidos fora da política. Pode-se solicitar, pesquisar, listar, aprovar e recusar. Deve conter código da compra, ingressos cancelados, nome e CPF do comprador, canal de origem, motivo, data do pedido, valor a devolver, forma de devolução, decisão, justificativa em caso de recusa, nome e CPF de quem recebeu o valor, data da devolução e responsável. A devolução é automática até sete dias após a compra e até quarenta e oito horas antes do show, ou quando o show foi remarcado. Os ingressos cancelados são invalidados e voltam à cota do canal de origem. |
| RF16 | Transferência e nominação | Esta funcionalidade deve permitir ao comprador informar quem vai usar cada ingresso e transferir um ingresso ainda não utilizado para outra pessoa. Deve conter ingresso, nome e CPF do portador atual, nome, CPF e e-mail do novo portador, data e hora da transferência e código do novo QR Code. A transferência invalida o QR Code anterior e emite um novo para o novo portador. A transferência não é permitida a partir de duas horas antes da abertura da porta. Na entrada, o portador é conferido pelo CPF, e não pela grafia do nome. |
| RF17 | Check-in e validação de acesso | Esta funcionalidade deve permitir à portaria ler o QR Code do ingresso pela câmera do celular, ou buscar o ingresso ou o convidado pelo CPF ou pelo nome, e liberar ou negar a entrada. Deve conter ingresso ou convite, sessão, data e hora da entrada, operador, ponto de entrada, resultado (liberado, negado ou conferência de documento) e motivo da negativa. A resposta aparece em até dois segundos. É negado o ingresso inválido, cancelado, de outra sessão ou já utilizado, mostrando o horário da entrada anterior. Ingresso de meia-entrada ou nominal exige a conferência do documento antes da liberação. |
| RF18 | Operação offline da portaria | Esta funcionalidade deve permitir que o aplicativo de portaria continue validando entradas sem conexão com a internet. Deve conter lista de ingressos válidos e de convidados da sessão baixada no aparelho, data e hora do último download, fila de entradas registradas sem conexão, data e hora da sincronização e ocorrências de duplicidade. A lista é baixada antes da abertura da porta. As entradas registradas sem internet são enviadas ao servidor quando a conexão volta. Se o mesmo ingresso for validado em dois aparelhos, vale o primeiro registro e o segundo aparece como duplicidade no relatório de ocorrências. |
| RF19 | Escala da equipe com confirmação | Esta funcionalidade deve permitir ao dono montar a equipe de cada sessão e a cada pessoa da equipe confirmar sua participação. Pode-se cadastrar, editar, listar e remover pessoas da escala. Deve conter sessão, nome, CPF, telefone, função (som, luz, segurança, bilheteria, bar ou portaria), horário de chegada, horário de saída, forma de cobrança (por show ou por diária), valor combinado, situação do convite (enviado, confirmado ou recusado) e presença registrada. O convite é enviado por mensagem com link de confirmação, e quem não confirmar pode ser substituído. A presença registrada no dia gera a despesa a pagar. |
| RF20 | Atrações, fornecedores e contratos | Esta funcionalidade deve permitir ao dono e ao sócio registrar os compromissos de cada show com atrações e fornecedores. Pode-se cadastrar, editar, pesquisar e listar. A atração deve conter nome artístico, nome e telefone do empresário, cachê, valor e data do sinal, forma e data de pagamento do restante e requisitos técnicos. O fornecedor deve conter nome ou razão social, CPF ou CNPJ, telefone, tipo de serviço (segurança, som, luz ou aluguel de espaço), valor combinado e prazo de pagamento. Ambos devem conter o arquivo do contrato ou a imagem da mensagem que confirmou o acordo e a situação (Combinado, Sinal pago ou Quitado). O cachê informado é usado pelo sócio para avaliar se o show é viável. |
| RF21 | Cronograma de produção | Esta funcionalidade deve permitir ao sócio montar a linha do tempo do dia do show. Pode-se cadastrar, editar, listar e marcar etapas como concluídas. Cada etapa deve conter sessão, nome da etapa (montagem, passagem de som, abertura da porta, banda de abertura, show principal ou desmontagem), horário previsto, horário real, responsável e situação. O sistema avisa quando o horário de abertura da porta no cronograma difere do horário anunciado ao público. Uma etapa atrasada destaca as etapas seguintes, e a portaria só é liberada depois de concluída a passagem de som. |
| RF22 | Resultado financeiro e fechamento | Esta funcionalidade deve apresentar ao dono e ao sócio o resultado de cada show e permitir ao sócio fechá-lo. Deve conter, por sessão, receita da venda online, receita da loja parceira, receita da porta, quantidade de inteiras, meias-entradas e convidados, descontos de cupons, reembolsos, comissão da loja parceira, taxas do provedor de pagamento, despesas por categoria, resultado, valores ainda a receber, data do fechamento e responsável. Logo após o fechamento do caixa da porta, o sistema mostra um resultado prévio. O fechamento definitivo só é liberado após a conferência das despesas e o acerto da loja parceira, e congela os valores; reabrir um show fechado exige justificativa. |
| RF23 | Relatórios e exportação | Esta funcionalidade deve permitir ao dono, ao sócio e ao administrativo consultar relatórios e exportá-los em planilha e em PDF. Deve conter os relatórios de vendas por canal, lote e forma de pagamento; curva de vendas por dia; comparecimento, com ingressos vendidos e entradas registradas; uso da lista de convidados por solicitante; ocorrências da portaria e do show; e resultado por show, comparando shows na casa e em espaços alugados. Todos os relatórios filtram por período e por show. O resumo do resultado é apresentado em tela simples no celular. |
| RF24 | Notificações e comunicação | Esta funcionalidade deve enviar mensagens automáticas por e-mail e por mensagem no telefone e permitir ao dono enviar comunicados aos compradores de uma sessão. Deve conter tipo da mensagem, destinatário, canal (e-mail ou telefone), texto, data e hora do envio e situação da entrega. São enviados automaticamente a confirmação de compra com o ingresso, o aviso de pagamento recusado ou expirado, a confirmação de cancelamento e reembolso, o lembrete vinte e quatro horas antes do show, o aviso de remarcação ou cancelamento, o convite de escala da equipe e o aviso de cota liberada à loja parceira. |
| RF25 | Auditoria das operações críticas | Esta funcionalidade deve registrar automaticamente as operações sensíveis e permitir ao dono e ao sócio consultá-las. Pode-se pesquisar e listar, sem editar nem excluir. Deve conter usuário, data e hora, tipo de operação, registro afetado, valor anterior e valor novo. São registradas alterações de preço e de cota, inclusão de convidado acima da cota, cancelamentos e reembolsos, sangrias do caixa, lançamento e exclusão de despesas, fechamento e reabertura de show e tentativas de acesso negadas. Os registros são guardados por cinco anos. |
| RF26 | Agenda de datas da casa | Esta funcionalidade deve permitir ao dono e ao sócio consultar e reservar datas num calendário de cada local, substituindo o caderno de datas. Pode-se pré-reservar, confirmar, liberar, pesquisar e listar. Deve conter local, data, horário de início e de fim, show ou atração, situação (Livre, Pré-reservada ou Confirmada), validade da pré-reserva, usuário que reservou e data da reserva. O sistema impede duas reservas para o mesmo local e horário. A pré-reserva é liberada quando o show é descartado, quando vence sem confirmação ou quando o show é remarcado para outra data. |
| RF27 | Distribuição de ingressos por canal | Esta funcionalidade deve permitir ao dono dividir a capacidade da montagem entre os canais de venda e acompanhar o estoque em tempo real pelo celular. Pode-se definir, editar e remanejar cotas. Deve conter sessão, capacidade total, cota e saldo da venda online, cota e saldo da loja parceira, cota e saldo da bilheteria da porta, cota e saldo de convidados, total vendido e total disponível. A soma das cotas não pode passar da capacidade. Todas as vendas baixam de um único estoque, o saldo não vendido pode ser remanejado entre canais e o sistema avisa quando uma cota chega a noventa por cento. |
| RF28 | Lista de convidados com cotas | Esta funcionalidade deve permitir ao dono definir quem pode indicar convidados e quantos, e à portaria conferir os convidados na entrada. Pode-se cadastrar, editar, pesquisar, listar e remover convidados. O solicitante deve conter nome (dono, sócio, banda ou imprensa) e cota de convites. O convidado deve conter nome completo, CPF, solicitante, data da inclusão, aprovação do dono quando acima da cota e situação da entrada. A lista fecha em horário definido antes da abertura da porta. Cada convite vale uma única entrada e ocupa um lugar da cota de convidados. |
| RF29 | Venda pela loja parceira e acerto | Esta funcionalidade deve permitir cadastrar a loja parceira, registrar as vendas feitas por ela e calcular o acerto após o show. Pode-se cadastrar, editar e listar parceiros e vendas. A loja deve conter nome, CNPJ ou CPF, endereço, telefone, responsável, percentual de comissão e prazo de repasse. Cada venda deve conter sessão, tipo de ingresso, quantidade, valor, forma de pagamento, nome e CPF do comprador, vendedor e data e hora. A venda baixa da cota do parceiro e gera o ingresso na hora. O acerto deve conter total vendido, comissão, valor a repassar, data prevista, data do recebimento e usuário que confirmou. |
| RF30 | Venda e caixa da bilheteria | Esta funcionalidade deve permitir à bilheteria vender ingressos na porta pelo celular e controlar o dinheiro da noite. Pode-se abrir o caixa, vender, registrar sangria e fechar o caixa. O caixa deve conter sessão, operador, valor inicial, data e hora de abertura, valor contado no fechamento, valor esperado, diferença e data e hora de fechamento. A venda deve conter tipo de ingresso, quantidade, valor, forma de pagamento (dinheiro, Pix ou cartão) e nome e CPF do comprador. A sangria deve conter valor, motivo e quem recebeu o dinheiro. A venda só é concluída se houver lugar na casa. |
| RF31 | Remarcação e cancelamento de show | Esta funcionalidade deve permitir ao dono e ao sócio remarcar uma sessão para outra data ou cancelar o show. Deve conter sessão, data original, nova data, motivo, tipo (remarcação ou cancelamento), prazo para pedido de reembolso, data da decisão e responsável. Na remarcação, os ingressos continuam válidos, a nova data é confirmada na agenda e os compradores são avisados, com um prazo em que o reembolso é aprovado automaticamente. No cancelamento, todos os reembolsos são gerados sem necessidade de pedido. Os compromissos com atração e fornecedores são marcados para renegociação. |
| RF32 | Controle de lotação em tempo real | Esta funcionalidade deve mostrar em tempo real, nos celulares da portaria e da bilheteria, quantas pessoas estão dentro da casa. Deve conter sessão, capacidade da montagem, total de entradas, total de saídas definitivas, pessoas dentro, percentual de ocupação e horário da última atualização. A contagem aumenta a cada entrada registrada e diminui com as saídas definitivas. O sistema avisa ao atingir noventa por cento da capacidade e bloqueia a venda na porta quando a capacidade é atingida. Sem internet, cada aparelho indica que a contagem pode estar desatualizada. |
| RF33 | Lançamento de despesas e pagamentos | Esta funcionalidade deve permitir ao sócio e ao administrativo lançar e conferir as despesas de cada show. Pode-se cadastrar, editar, pesquisar, listar e excluir, enquanto o show não for fechado. Deve conter show, categoria (cachê, sinal, equipe, segurança, som, luz, aluguel, divulgação ou outros), descrição, valor, data do pagamento, quem recebeu, forma de pagamento, origem do dinheiro (caixa da porta ou conta), foto do recibo ou nota, situação (prevista ou paga) e usuário que lançou. As despesas previstas da escala e dos contratos aparecem como pendentes até serem pagas. O lançamento pode ser feito pelo celular durante a noite do show. |

### 3.2 Requisitos não funcionais

O detalhamento está em [requisitos/requisitos-nao-funcionais.md](requisitos/requisitos-nao-funcionais.md).

#### Usabilidade

| Código | RNF / Aplicação | Descrição |
|---|---|---|
| RNF01 | Portal público | A compra deve ser concluída em no máximo cinco telas, sem exigir cadastro prévio do comprador. |
| RNF02 | Portal público | Os preços devem exibir a taxa de serviço destacada do valor do ingresso em todas as etapas. |
| RNF03 | Aplicativo de portaria | O resultado da leitura deve ser indicado por cor e por texto, legível sob luz forte e à distância de um braço. |
| RNF04 | Todo o sistema | A interface deve seguir a WCAG 2.1 nível AA, com contraste, navegação por teclado e textos alternativos. |
| RNF05 | Painel do dono | Cadastrar um show simples e abrir as vendas pelo celular deve levar menos de dez minutos, sem treinamento formal. |

#### Segurança

| Código | RNF / Aplicação | Descrição |
|---|---|---|
| RNF06 | Todo o sistema | Senhas armazenadas com hash de sentido único com sal, nunca em texto claro. |
| RNF07 | Todo o sistema | Todo o tráfego sobre HTTPS com TLS 1.2 ou superior. |
| RNF08 | Bilheteria | Não armazenar número completo, código de segurança nem validade do cartão, delegando a captura ao provedor certificado PCI DSS. |
| RNF09 | Ingresso digital | O QR Code deve conter assinatura digital verificável offline, rejeitando cópias forjadas sem consultar o servidor. |
| RNF10 | Painel financeiro | Perfis Dono e Sócio exigem segundo fator de autenticação. |
| RNF11 | Todo o sistema | O controle de acesso deve ser aplicado no servidor a cada requisição, não apenas na interface. |

#### Performance

| Código | RNF / Aplicação | Descrição |
|---|---|---|
| RNF12 | Portal público | A página do show deve carregar em até dois segundos no percentil 95 em conexão móvel de quatro megabits. |
| RNF13 | Bilheteria | Suportar quinhentas compras simultâneas, somando todos os canais, sem vender acima da capacidade da montagem. |
| RNF14 | Aplicativo de portaria | Validar um ingresso em até dois segundos e sustentar seiscentas entradas por hora por celular de portaria. |
| RNF15 | Relatórios | Gerar relatórios de doze meses em até dez segundos, com processamento assíncrono acima desse tempo. |

#### Portabilidade

| Código | RNF / Aplicação | Descrição |
|---|---|---|
| RNF16 | Portal público | Interface responsiva a partir de trezentos e vinte pixels, nas versões atual e anterior de Chrome, Firefox, Safari e Edge. |
| RNF17 | Aplicativo de portaria | Rodar em Android 9 ou superior e iOS 14 ou superior, em aparelhos de entrada com câmera traseira. |
| RNF18 | Servidor | Distribuição em contêineres, instalável em qualquer provedor compatível com Docker. |
| RNF19 | Dados | Exportação completa dos dados da casa em CSV e JSON, inclusive para uso do contador. |

#### Confiabilidade e conformidade legal

| Código | RNF / Aplicação | Descrição |
|---|---|---|
| RNF20 | Bilheteria | Disponibilidade mensal mínima de noventa e nove vírgula cinco por cento. |
| RNF21 | Aplicativo de portaria | Portaria e venda na porta devem operar no mínimo seis horas sem conexão, sincronizando ao reconectar. |
| RNF22 | Banco de dados | Cópia de segurança diária com retenção de trinta dias e teste de restauração trimestral. |
| RNF23 | Todo o sistema | Tratamento de dados pessoais conforme a LGPD, com base legal registrada e exclusão atendida em até quinze dias. |
| RNF24 | Bilheteria | Cota de meia-entrada limitada a quarenta por cento dos ingressos por sessão, conforme a Lei 12.933 de 2013. |
| RNF25 | Bilheteria | Direito de arrependimento de sete dias respeitado na política de cancelamento. |
| RNF26 | Auditoria | Retenção de registros de auditoria, comprovantes de despesas e fechamentos de caixa por cinco anos. |

---

## 4. Lista de riscos

| Nº | Risco | Probabilidade | Impacto | Resposta |
|---|---|---|---|---|
| R01 | Venda acima da capacidade por soma de vendas simultâneas em canais diferentes | Média | Alto | Estoque único consolidado, reserva com bloqueio em transação e bloqueio da venda na porta pela lotação (RF10, RF27, RF32, RNF13). |
| R02 | Queda de internet na porta durante a entrada do público | Alta | Alto | Portaria e venda na porta offline com lista pré-carregada e sincronização posterior (RF18, RF30, RNF21). |
| R03 | Indisponibilidade ou lentidão do provedor de pagamento | Média | Alto | Fila de reprocessamento, mensagem clara ao comprador e venda pela loja parceira e pela porta como alternativa (RF11, RF29, RF30). |
| R04 | Fraude por ingresso duplicado ou comprovante reutilizado | Média | Alto | Confirmação de pagamento pelo provedor, QR Code assinado, invalidação na transferência e detecção de duplicidade (RF11, RF12, RF16, RF18, RNF09). |
| R05 | Autuação por descumprimento da cota de meia-entrada | Baixa | Alto | Controle automático de cota por sessão e conferência obrigatória do documento na portaria (RF13, RNF24). |
| R06 | Remarcação ou cancelamento de show com reembolso em massa | Média | Alto | Aviso automático aos compradores, prazo de reembolso automático e devolução pelo canal de origem (RF15, RF24, RF31). |
| R07 | Vazamento de dados pessoais dos compradores e convidados | Baixa | Muito alto | Criptografia em trânsito, mínimo de dados coletados, controle de acesso no servidor e trilha de auditoria (RNF06, RNF07, RNF11, RF25). |
| R08 | Loja parceira deixar de registrar vendas no sistema e voltar à planilha | Média | Alto | Ingresso só é emitido pelo sistema, portaria recusa comprovante de papel e acerto calculado apenas sobre vendas registradas (RF12, RF17, RF29). |
| R09 | Dono, bilheteria ou portaria sem familiaridade com tecnologia rejeitarem o sistema | Alta | Alto | Uso exclusivo pelo celular, telas de resultado único, busca por CPF como alternativa ao QR Code e treinamento no primeiro show (RF17, RNF03, RNF05). |
| R10 | Pagamentos em dinheiro continuarem sem lançamento durante a noite | Alta | Médio | Sangria obrigatória no caixa da porta, despesas pendentes geradas pela escala e conferência antes do fechamento (RF19, RF30, RF33). |
| R11 | Escopo crescer durante o semestre e inviabilizar a entrega | Alta | Médio | Escopo negativo declarado na seção 1.2 e priorização por Essencial, Importante e Desejável. |

---

## 5. Lista de restrições

### 5.1 De hardware

| Nº | Nome | Descrição |
|---|---|---|
| 1 | Aparelhos da equipe | Dono, sócio, bilheteria e portaria usam celulares próprios ou da casa, de entrada, com câmera traseira e Android 9 ou superior, sem leitor laser dedicado nem computador na porta. |
| 2 | Conectividade no local | A casa e os espaços alugados têm sinal instável, portanto portaria e venda na porta não podem depender de conexão contínua. |
| 3 | Máquina de cartão | A venda na porta com cartão usa a maquininha já existente ou alugada, sem integração direta nesta versão; o valor é lançado manualmente no caixa. |
| 4 | Servidor de aplicação | A hospedagem inicial é uma instância única com dois núcleos e quatro gigabytes de memória, o que limita o processamento síncrono de relatórios. |
| 5 | Impressão | Não haverá impressora na portaria. O ingresso é digital e a conferência é feita na tela do celular. |

### 5.2 De software

| Nº | Nome | Descrição |
|---|---|---|
| 1 | Provedor de pagamento | A captura de dados de cartão e o Pix são processados pelo provedor contratado, e o sistema recebe apenas a confirmação da transação. |
| 2 | Navegadores suportados | A página pública e o painel atendem as versões atual e anterior de Chrome, Firefox, Safari e Edge. Não há suporte a Internet Explorer. |
| 3 | Plataforma móvel | O aplicativo de portaria atende Android 9 ou superior e iOS 14 ou superior. |
| 4 | Licenciamento | Devem ser usadas apenas bibliotecas com licença livre compatível com uso comercial, por restrição de orçamento da Cena Livre. |
| 5 | Idioma e moeda | A versão inicial atende apenas português do Brasil e real, sem internacionalização. |
| 6 | Integração fiscal | Não há integração com emissor de nota fiscal nem com o sistema do contador nesta versão; a troca de dados é feita por exportação. |

---

## 6. Anexos: diagramas BPMN

Os diagramas do processo estão em [processos/](processos/) na forma de arquivos `.bpmn` abríveis no Bizagi Modeler e no bpmn.io, acompanhados da descrição textual de cada processo. Os processos foram modelados a partir da entrevista com o dono da Cena Livre. A coerência entre a modelagem e os requisitos é demonstrada na [matriz de rastreabilidade](rastreabilidade.md), que liga cada atividade dos diagramas ao requisito funcional correspondente.

| Processo | Nome | Requisitos cobertos |
|---|---|---|
| P1 | Planejamento do show e abertura de vendas | RF04, RF05, RF06, RF07, RF08, RF09, RF20, RF24, RF26, RF27, RF28, RF29, RF33 |
| P2 | Venda de ingressos nos canais | RF09, RF10, RF11, RF12, RF13, RF14, RF24, RF27, RF29 |
| P3 | Cancelamento, remarcação e reembolso | RF12, RF15, RF22, RF24, RF26, RF27, RF29, RF30, RF31 |
| P4 | Entrada do público no dia do show | RF12, RF13, RF16, RF17, RF18, RF28, RF30, RF32 |
| P5 | Produção do show | RF19, RF20, RF21, RF23, RF24, RF33 |
| P6 | Fechamento financeiro do show | RF22, RF23, RF29, RF30, RF33 |
