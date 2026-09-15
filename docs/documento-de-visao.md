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

O detalhamento completo, com as regras de cada funcionalidade e a origem na entrevista, está em [requisitos/requisitos-funcionais.md](requisitos/requisitos-funcionais.md). O quadro abaixo é o resumo exigido pelo Documento de Visão. São 32 requisitos funcionais ativos, acima do mínimo de 15 pedido na entrega. O RF03, cadastro de produtora com aprovação por administrador de plataforma, foi retirado depois da entrevista, porque o sistema atende uma única casa de shows; o código não é reaproveitado.

| Código | Nome | Descrição |
|---|---|---|
| RF01 | Gestão de usuários e perfis | Permite ao dono cadastrar, editar, inativar e listar usuários com os perfis Dono, Sócio, Administrativo, Bilheteria, Portaria, Loja parceira e Cliente. Usuários com operações registradas não podem ser excluídos, apenas inativados. |
| RF02 | Autenticação e recuperação de senha | Permite o acesso por e-mail ou telefone e senha, com bloqueio após cinco tentativas, recuperação por link ou código de uso único e segundo fator para os perfis Dono e Sócio. |
| RF04 | Cadastro de locais e montagens | Permite cadastrar a casa e os espaços alugados, com capacidade máxima e valor de aluguel, e as montagens de cada local com capacidade própria, que define o total de lugares do show. |
| RF05 | Cadastro de show | Permite cadastrar o show com atração, descrição, imagem, local, montagem e políticas de meia-entrada e cancelamento, acompanhando as situações de Em negociação a Fechado. |
| RF06 | Gestão de sessões | Permite cadastrar uma ou mais sessões por show, com data e horários de abertura da porta, início e término, cada uma com estoque e lotação próprios. |
| RF07 | Gestão de lotes e preços | Permite ao sócio definir lotes com quantidade, preço inteiro, preço de meia e vigência, com lote promocional, virada automática e preço da porta definido à parte. |
| RF08 | Verificação e abertura das vendas | Verifica data confirmada, contrato, montagem, cotas, lotes e convidados, lista as pendências ao dono e, sem pendências, abre as vendas e gera o link da página do show. |
| RF09 | Página pública de vendas | Disponibiliza sem login a página de cada show à venda, acessada pelo link do Instagram, e a agenda pública da casa, com lotes esgotados marcados como indisponíveis. |
| RF10 | Carrinho com reserva temporária | Permite selecionar sessão, tipo e quantidade respeitando o limite por CPF, reservando os ingressos na cota online por quinze minutos. |
| RF11 | Pagamento online com confirmação automática | Permite pagar por Pix ou cartão, com confirmação enviada pelo provedor, sem depender de comprovante encaminhado pelo cliente. Não armazena dados completos do cartão. |
| RF12 | Emissão de ingresso com QR Code | Gera para cada ingresso de qualquer canal um código único com QR Code assinado, enviado por e-mail em PDF que pode ser salvo no aparelho. |
| RF13 | Meia-entrada e comprovante | Permite comprar meia-entrada dentro da cota por sessão, com categoria e comprovante. O ingresso é nominal e a portaria só libera após conferir o documento. |
| RF14 | Cupons de desconto | Permite criar cupons com código, tipo de desconto, quantidade de usos, validade e restrição por show, aplicados no pagamento online. |
| RF15 | Cancelamento e reembolso | Permite pedir cancelamento, aplica a política do show, encaminha exceções ao dono e ao sócio e devolve o valor pelo canal de origem, sempre ao comprador identificado por CPF. |
| RF16 | Transferência e nominação | Permite nomear o portador de cada ingresso e transferi-lo por CPF, invalidando o código anterior e emitindo um novo. |
| RF17 | Check-in e validação de acesso | Permite à portaria ler o QR Code ou buscar por CPF e obter em até dois segundos a resposta liberado, negado com motivo ou verificação de documento, registrando cada entrada. |
| RF18 | Operação offline da portaria | Permite baixar ingressos e lista de convidados antes da abertura e validar sem internet, sincronizando ao reconectar e tratando duplicidade entre aparelhos. |
| RF19 | Escala da equipe com confirmação | Permite montar a escala por função, enviar convite com data, horário e valor, receber a confirmação de cada pessoa e registrar a presença, gerando a despesa correspondente. |
| RF20 | Atrações, fornecedores e contratos | Permite registrar cachê, sinal, fornecedores e aluguéis, anexar contrato ou a mensagem de confirmação e acompanhar a situação de cada compromisso. |
| RF21 | Cronograma de produção | Permite montar a linha do tempo do dia, da montagem à desmontagem, alertando divergência com o horário anunciado e liberando a portaria após a passagem de som. |
| RF22 | Resultado financeiro e fechamento | Apresenta receitas por canal, descontos, reembolsos, comissão do parceiro, despesas e resultado, com resultado prévio logo após o show e fechamento definitivo após o acerto do parceiro. |
| RF23 | Relatórios e exportação | Disponibiliza relatórios de vendas por canal, comparecimento, uso da lista de convidados, ocorrências e resultado por show, com exportação em planilha e PDF. |
| RF24 | Notificações e comunicação | Envia por e-mail e mensagem confirmações de compra, avisos de pagamento, reembolso, remarcação, convites de escala e liberação de cota, e comunicados aos compradores. |
| RF25 | Auditoria das operações críticas | Registra em trilha somente leitura alterações de preço e cota, convidados acima da cota, reembolsos, sangrias, despesas e fechamentos, retida por cinco anos. |
| RF26 | Agenda de datas da casa | Apresenta calendário por local com datas livres, pré-reservadas e confirmadas, impedindo dois shows na mesma data e liberando pré-reservas vencidas ou descartadas. |
| RF27 | Distribuição de ingressos por canal | Divide a capacidade em cotas para online, loja parceira, porta e convidados, com estoque único consolidado em tempo real e remanejamento de saldo entre canais. |
| RF28 | Lista de convidados com cotas | Define quem pode indicar convidados e quantos, cadastra cada nome com CPF, exige aprovação do dono acima da cota e permite uma única entrada por convite. |
| RF29 | Venda pela loja parceira e acerto | Permite à loja registrar cada venda na hora, com nome e CPF, baixando da própria cota, e calcula o acerto com a comissão combinada após o show. |
| RF30 | Venda e caixa da bilheteria | Permite abrir e fechar o caixa da noite, vender na porta por dinheiro, Pix ou cartão e registrar sangrias com motivo, apontando diferenças no fechamento. |
| RF31 | Remarcação e cancelamento de show | Permite remarcar ou cancelar a sessão, avisando os compradores e abrindo prazo de reembolso automático, e sinaliza compromissos para renegociação. |
| RF32 | Controle de lotação em tempo real | Conta as pessoas dentro da casa a partir das entradas, alerta aos noventa por cento e bloqueia a venda na porta ao atingir a capacidade da montagem. |
| RF33 | Lançamento de despesas e pagamentos | Permite lançar cada despesa com valor, quem recebeu, origem do dinheiro e foto do recibo, pelo celular durante a noite, alimentando o resultado do show. |

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
