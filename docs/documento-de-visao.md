# Documento de Visão: Sistema "Palco"

**Disciplina:** Análise de Sistemas — 3º Semestre ADS — IFBA Irecê
**Professor:** Wild Barreto
**Data:** ___/___/______  **Versão:** 0.1
**Autor(es):** Eduardo de Souza Silva e demais integrantes do grupo

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

Este documento apresenta uma visão geral do sistema "Palco", uma plataforma de gestão de eventos e shows que cobre desde a criação do evento pelo produtor até o fechamento financeiro depois da realização. O texto descreve o problema observado no mercado de produção de eventos de pequeno e médio porte, os usuários envolvidos, as funções que o sistema deve oferecer e as condições sob as quais deve funcionar.

### 1.1 Objetivos deste documento

Descrever e especificar as necessidades de um software capaz de apoiar produtoras de eventos na venda de ingressos, no controle de acesso e no controle financeiro dos shows, necessidades que devem ser atendidas pelo produto "Palco", bem como definir para os desenvolvedores o produto a ser feito.

Público-alvo: cliente, usuários e desenvolvedores do projeto "Palco".

### 1.2 Escopo do produto

O produto a ser desenvolvido é o sistema "Palco".

A missão do sistema é proporcionar apoio informatizado a produtoras de eventos e casas de show na venda de ingressos, no controle de acesso do público e na apuração do resultado financeiro de cada evento.

Estão no escopo:

- Cadastro de produtoras, locais, setores, eventos, sessões e lotes de ingressos.
- Fluxo de aprovação e publicação de eventos na vitrine pública.
- Venda de ingressos pela internet, com reserva temporária, cupons, cortesias e meia-entrada.
- Emissão de ingresso digital com QR Code assinado.
- Cancelamento de compra e reembolso, inclusive por cancelamento do evento inteiro.
- Check-in do público na portaria, com operação offline e sincronização posterior.
- Gestão de equipe, atrações, fornecedores e cronograma de produção.
- Fechamento financeiro por sessão, repasse ao produtor e relatórios gerenciais.

Estão fora do escopo desta versão:

- Emissão de nota fiscal e integração com sistemas contábeis.
- Venda de alimentos e bebidas dentro do evento, incluindo cashless.
- Aplicativo nativo para o público comprador, atendido pelo portal responsivo.
- Marketplace de fornecedores e contratação de serviços dentro da plataforma.
- Transmissão ao vivo e venda de ingressos para eventos online.

### 1.3 Definições, acrônimos e abreviações

| Nº | Sigla ou termo | Definição |
|---|---|---|
| 1 | Evento | Espetáculo comercializado na plataforma, por exemplo um show de uma banda. |
| 2 | Sessão | Ocorrência datada de um evento. Um show em três noites é um evento com três sessões. |
| 3 | Setor | Divisão física do local com capacidade e preço próprios, por exemplo Pista e Camarote. |
| 4 | Lote | Faixa de venda de um setor, com quantidade, preço e vigência definidos. |
| 5 | Cortesia | Ingresso de valor zero destinado a convidados, imprensa ou permuta. |
| 6 | Meia-entrada | Ingresso com desconto legal de cinquenta por cento, sujeito a cota e comprovação. |
| 7 | Check-in | Validação do ingresso na portaria, que libera a entrada do portador. |
| 8 | QR Code | Código de barras bidimensional impresso no ingresso, lido pela portaria. |
| 9 | PSP | Provedor de serviços de pagamento, responsável por processar cobranças e estornos. |
| 10 | Repasse | Transferência ao produtor do valor apurado no fechamento, descontada a comissão. |
| 11 | BPMN | Business Process Model and Notation, notação de modelagem de processos de negócio. |
| 12 | LGPD | Lei Geral de Proteção de Dados, Lei 13.709 de 2018. |
| 13 | PCI DSS | Norma de segurança para o tratamento de dados de cartão de pagamento. |
| 14 | RF | Requisito funcional. |
| 15 | RNF | Requisito não funcional. |

---

## 2. Contexto

### 2.1 Declaração do problema

Produtoras de pequeno e médio porte organizam shows controlando tudo por planilhas, grupos de mensagens e cadernos. A venda de ingressos acontece em canais soltos, um lote pelo Instagram, outro na loja de um parceiro, outro na porta no dia do evento. O resultado é um conjunto de problemas que se repetem a cada show.

O produtor não sabe em tempo real quantos ingressos foram vendidos, então descobre que vendeu acima da capacidade apenas quando a fila trava na portaria. A entrada é conferida em lista impressa, o que gera fila, atrasa a abertura da casa e não impede que o mesmo comprovante entre duas vezes. Ingressos são falsificados com facilidade, porque o comprovante é uma imagem encaminhada por aplicativo de mensagens. A cota legal de meia-entrada não é controlada, o que expõe a produtora a autuação.

No dia seguinte ao show, ninguém sabe dizer se houve lucro. As receitas estão espalhadas entre transferências, dinheiro em espécie e vendas de parceiros, e os custos de cachê, som, luz, segurança e equipe estão em recibos avulsos. O pedido de reembolso de um cliente vira uma negociação manual, sem política clara nem registro, e o cancelamento de um evento inteiro se transforma numa operação de risco reputacional.

O problema afeta o produtor, que perde margem e tempo, a equipe de portaria, que trabalha sem ferramenta adequada, e o público, que enfrenta fila, insegurança na compra e dificuldade para cancelar. Uma solução adequada precisa concentrar venda, acesso e dinheiro num mesmo registro, funcionar no celular da equipe, aguentar o pico de vendas na abertura de um lote e continuar validando ingressos quando a internet cair no meio do show.

### 2.2 Descrição dos usuários

| Nº | Usuário | Descrição |
|---|---|---|
| 1 | Cliente | Público comprador. Pesquisa eventos, compra ingressos, recebe o ingresso digital, transfere ingressos, solicita cancelamento e acompanha suas compras. Não precisa de cadastro para pesquisar, apenas para comprar. |
| 2 | Produtor | Responsável pela produtora. Cadastra locais, eventos, sessões e lotes, define preços e políticas, emite cortesias e cupons, monta equipe e cronograma, acompanha vendas e recebe o repasse. |
| 3 | Portaria | Operador que trabalha na entrada do evento. Lê o QR Code dos ingressos, confere documento quando exigido e registra o acesso, inclusive sem conexão de rede. |
| 4 | Financeiro | Usuário da plataforma que analisa reembolsos fora da política automática, confere o demonstrativo de cada sessão, fecha o período e libera o repasse ao produtor. |
| 5 | Administrador | Usuário da plataforma que aprova o cadastro das produtoras, analisa e publica eventos, gerencia usuários e perfis e consulta a trilha de auditoria. |
| 6 | Provedor de pagamento | Ator externo. Processa cobranças de cartão, Pix e boleto e executa os estornos solicitados pelo sistema. |

---

## 3. Requisitos específicos

### 3.1 Requisitos funcionais

O detalhamento completo, com regras de cada funcionalidade, está em [requisitos/requisitos-funcionais.md](requisitos/requisitos-funcionais.md). O quadro abaixo é o resumo exigido pelo Documento de Visão. São 25 requisitos funcionais, acima do mínimo de 15 pedido na entrega.

| Código | Nome | Descrição |
|---|---|---|
| RF01 | Gestão de usuários e perfis | Permite ao administrador cadastrar, editar, inativar e listar usuários, atribuindo os perfis Administrador, Produtor, Financeiro, Portaria e Cliente. Usuários com operações registradas não podem ser excluídos, apenas inativados. |
| RF02 | Autenticação e recuperação de senha | Permite o acesso por e-mail e senha ou conta Google, com bloqueio após cinco tentativas, recuperação por link de uso único válido por trinta minutos e segundo fator para perfis administrativos. |
| RF03 | Cadastro de produtor e dados de recebimento | Permite cadastrar a produtora com dados cadastrais, responsável legal, documentos e dados bancários de repasse. A submissão de eventos depende da aprovação do cadastro, e a alteração dos dados bancários exige nova aprovação. |
| RF04 | Cadastro de locais e setores | Permite cadastrar locais com endereço, capacidade, coordenadas e acessibilidade, divididos em setores com capacidade própria. A soma das capacidades dos setores não pode ultrapassar a do local. |
| RF05 | Cadastro de evento | Permite cadastrar evento com nome, descrição, categoria, classificação indicativa, local, imagem, política de meia-entrada e de cancelamento. O evento nasce como rascunho e pode ser editado, duplicado, pesquisado e listado. |
| RF06 | Gestão de sessões | Permite cadastrar uma ou mais sessões por evento, com data, abertura dos portões, início e término previsto, cada uma com estoque próprio. O sistema impede sessões sobrepostas no mesmo local. |
| RF07 | Gestão de lotes e preços | Permite definir por setor e sessão os lotes com quantidade, preço inteiro, preço de meia, taxa de serviço e vigência. A virada de lote ocorre por esgotamento ou por data, e o histórico de preços é preservado. |
| RF08 | Submissão, aprovação e publicação | Permite ao produtor submeter o evento e ao administrador aprovar, reprovar com justificativa ou solicitar ajustes. Aprovado, o evento é publicado na vitrine na data de início de vendas. |
| RF09 | Vitrine pública e busca | Permite ao público consultar eventos publicados sem login, com busca por texto, filtros de cidade, categoria, preço e período, e página de evento com sessões, setores, preços e políticas. |
| RF10 | Carrinho com reserva temporária | Permite selecionar sessão, setor, tipo e quantidade respeitando o limite por CPF, criando reserva que retira o ingresso do estoque por quinze minutos e o devolve automaticamente se a compra não for concluída. |
| RF11 | Checkout e pagamento | Permite concluir a compra por cartão, Pix ou boleto, mantendo o pedido aguardando confirmação do provedor. Aprovado, emite os ingressos; recusado ou expirado, libera o estoque. Não armazena dados completos do cartão. |
| RF12 | Emissão de ingresso com QR Code | Gera para cada ingresso um código único com QR Code assinado digitalmente, contendo evento, sessão, setor, tipo e portador, disponível na área do cliente e enviado por e-mail em PDF. |
| RF13 | Meia-entrada e comprovante | Permite comprar meia-entrada dentro da cota legal por sessão, informando a categoria do benefício e anexando comprovante quando exigido. O ingresso é nominal e sinalizado para conferência na portaria. |
| RF14 | Cupons e cortesias | Permite criar cupons com código, tipo de desconto, quantidade de usos, validade e restrição de aplicação, e emitir cortesias com cota separada do estoque de venda. |
| RF15 | Cancelamento e reembolso | Permite ao cliente solicitar cancelamento e ao financeiro processar o reembolso conforme a política do evento, invalidando os ingressos, devolvendo o estoque e solicitando o estorno ao provedor. |
| RF16 | Transferência e nominação | Permite nomear o portador de cada ingresso e transferir ingressos não utilizados por e-mail, invalidando o código anterior e emitindo um novo. |
| RF17 | Check-in e validação de acesso | Permite à portaria ler o QR Code e obter em até dois segundos a resposta de acesso liberado, acesso negado com o motivo ou verificação manual do documento, registrando data, hora, operador e portão. |
| RF18 | Operação offline da portaria | Permite baixar a lista de ingressos da sessão e validar acessos sem rede, enfileirando os registros e sincronizando ao reconectar, com tratamento de duplicidade entre dispositivos. |
| RF19 | Gestão de equipe e escala | Permite montar a escala por função com horários e diárias, alertar sobrescala de uma mesma pessoa e registrar a presença efetiva, alimentando o custo de pessoal do evento. |
| RF20 | Atrações, fornecedores e contratos | Permite cadastrar atrações com cachê e requisitos técnicos e fornecedores com valores contratados, anexar contratos e acompanhar a situação de cada compromisso. |
| RF21 | Cronograma de produção | Permite montar a linha do tempo do dia da sessão, com responsável e horário por etapa, marcar etapas concluídas e recalcular as seguintes quando houver atraso. |
| RF22 | Painel financeiro e fechamento | Apresenta receita, taxas, descontos, reembolsos, custos e resultado por evento e sessão, permite fechar a sessão congelando valores e gerar o repasse ao produtor após o fim da janela de reembolso. |
| RF23 | Relatórios e exportação | Disponibiliza relatórios de vendas, curva de vendas, taxa de comparecimento, ocorrências de portaria e demonstrativo de resultado, com filtros e exportação em CSV e PDF. |
| RF24 | Notificações e comunicação | Envia confirmação de compra, avisos de pagamento, cancelamento e reembolso, lembrete da sessão e avisos de alteração, e permite ao produtor comunicar todos os compradores de uma sessão. |
| RF25 | Auditoria das operações críticas | Registra em trilha somente leitura as operações sensíveis, com usuário, data, origem, valor anterior e valor novo, consultável pelo administrador e retida por cinco anos. |

### 3.2 Requisitos não funcionais

O detalhamento está em [requisitos/requisitos-nao-funcionais.md](requisitos/requisitos-nao-funcionais.md).

#### Usabilidade

| Código | RNF / Aplicação | Descrição |
|---|---|---|
| RNF01 | Portal público | A compra deve ser concluída em no máximo cinco telas, sem exigir cadastro prévio do comprador. |
| RNF02 | Portal público | Os preços devem exibir a taxa de serviço destacada do valor do ingresso em todas as etapas. |
| RNF03 | Aplicativo de portaria | O resultado da leitura deve ser indicado por cor e por texto, legível sob luz forte e à distância de um braço. |
| RNF04 | Todo o sistema | A interface deve seguir a WCAG 2.1 nível AA, com contraste, navegação por teclado e textos alternativos. |
| RNF05 | Painel do produtor | Publicar um evento simples deve levar menos de dez minutos, sem treinamento formal. |

#### Segurança

| Código | RNF / Aplicação | Descrição |
|---|---|---|
| RNF06 | Todo o sistema | Senhas armazenadas com hash de sentido único com sal, nunca em texto claro. |
| RNF07 | Todo o sistema | Todo o tráfego sobre HTTPS com TLS 1.2 ou superior. |
| RNF08 | Bilheteria | Não armazenar número completo, código de segurança nem validade do cartão, delegando a captura ao provedor certificado PCI DSS. |
| RNF09 | Ingresso digital | O QR Code deve conter assinatura digital verificável offline, rejeitando cópias forjadas sem consultar o servidor. |
| RNF10 | Painel administrativo | Perfis Administrador e Financeiro exigem segundo fator de autenticação. |
| RNF11 | Todo o sistema | O controle de acesso deve ser aplicado no servidor a cada requisição, não apenas na interface. |

#### Performance

| Código | RNF / Aplicação | Descrição |
|---|---|---|
| RNF12 | Portal público | A página do evento deve carregar em até dois segundos no percentil 95 em conexão móvel de quatro megabits. |
| RNF13 | Bilheteria | Suportar mil compras simultâneas na abertura de vendas sem vender acima da capacidade do setor. |
| RNF14 | Aplicativo de portaria | Validar um ingresso em até dois segundos e sustentar mil e duzentas entradas por hora por portão. |
| RNF15 | Relatórios | Gerar relatórios de doze meses em até dez segundos, com processamento assíncrono acima desse tempo. |

#### Portabilidade

| Código | RNF / Aplicação | Descrição |
|---|---|---|
| RNF16 | Portal público | Interface responsiva a partir de trezentos e vinte pixels, nas versões atual e anterior de Chrome, Firefox, Safari e Edge. |
| RNF17 | Aplicativo de portaria | Rodar em Android 9 ou superior e iOS 14 ou superior, em aparelhos de entrada com câmera traseira. |
| RNF18 | Servidor | Distribuição em contêineres, instalável em qualquer provedor compatível com Docker. |
| RNF19 | Dados | Exportação completa dos dados do produtor em CSV e JSON. |

#### Confiabilidade e conformidade legal

| Código | RNF / Aplicação | Descrição |
|---|---|---|
| RNF20 | Bilheteria | Disponibilidade mensal mínima de noventa e nove vírgula cinco por cento. |
| RNF21 | Aplicativo de portaria | Operar no mínimo seis horas sem conexão, sincronizando ao reconectar. |
| RNF22 | Banco de dados | Cópia de segurança diária com retenção de trinta dias e teste de restauração trimestral. |
| RNF23 | Todo o sistema | Tratamento de dados pessoais conforme a LGPD, com base legal registrada e exclusão atendida em até quinze dias. |
| RNF24 | Bilheteria | Cota de meia-entrada limitada a quarenta por cento dos ingressos por sessão, conforme a Lei 12.933 de 2013. |
| RNF25 | Bilheteria | Direito de arrependimento de sete dias respeitado na política de cancelamento. |
| RNF26 | Auditoria | Retenção de registros de auditoria e documentos fiscais por cinco anos. |

---

## 4. Lista de riscos

| Nº | Risco | Probabilidade | Impacto | Resposta |
|---|---|---|---|---|
| R01 | Venda acima da capacidade por concorrência no pico de abertura de um lote | Média | Alto | Reserva com bloqueio de estoque em transação, teste de carga antes da estreia e limite por CPF (RF10, RNF13). |
| R02 | Queda de internet no local do evento durante a entrada do público | Alta | Alto | Portaria offline com lista pré-carregada e sincronização posterior (RF18, RNF21). |
| R03 | Indisponibilidade ou lentidão do provedor de pagamento | Média | Alto | Mais de um provedor habilitado, fila de reprocessamento e mensagem clara ao comprador (RF11). |
| R04 | Fraude por duplicação de ingresso | Média | Alto | QR Code assinado, código não sequencial, invalidação na transferência e detecção de duplicidade (RF12, RF16, RF18, RNF09). |
| R05 | Autuação por descumprimento da cota de meia-entrada | Baixa | Alto | Controle automático de cota por sessão e retenção do comprovante (RF13, RNF24). |
| R06 | Cancelamento de evento de grande porte com reembolso em massa | Baixa | Alto | Rotina de reembolso em lote, comunicação automática e retenção do repasse até o fim da janela (RF15, RF22, RF24). |
| R07 | Vazamento de dados pessoais dos compradores | Baixa | Muito alto | Criptografia em trânsito, mínimo de dados coletados, controle de acesso no servidor e trilha de auditoria (RNF06, RNF07, RNF11, RF25). |
| R08 | Produtor lançar dados bancários incorretos e receber repasse indevido | Média | Médio | Aprovação obrigatória de alteração bancária e histórico de mudanças (RF03). |
| R09 | Equipe de portaria sem preparo para operar o aplicativo no dia | Alta | Médio | Interface de resultado único por leitura, modo de treinamento e busca por CPF como alternativa (RF17, RNF03). |
| R10 | Escopo crescer durante o semestre e inviabilizar a entrega | Alta | Médio | Escopo negativo declarado na seção 1.2 e priorização por Essencial, Importante e Desejável. |

---

## 5. Lista de restrições

### 5.1 De hardware

| Nº | Nome | Descrição |
|---|---|---|
| 1 | Dispositivo da portaria | A portaria opera com celulares de entrada fornecidos pela produtora, com câmera traseira e Android 9 ou superior, sem leitor laser dedicado. |
| 2 | Conectividade no local | Casas de show e áreas abertas têm sinal instável, portanto o aplicativo de portaria não pode depender de conexão contínua. |
| 3 | Servidor de aplicação | A hospedagem inicial é uma instância única com dois núcleos e quatro gigabytes de memória, o que limita o processamento síncrono de relatórios. |
| 4 | Impressão | Não haverá impressora térmica na portaria nesta versão. O ingresso é digital e a conferência é feita na tela do dispositivo. |

### 5.2 De software

| Nº | Nome | Descrição |
|---|---|---|
| 1 | Provedor de pagamento | A captura de dados de cartão é feita pela interface do provedor contratado, e o sistema recebe apenas o retorno da transação. |
| 2 | Navegadores suportados | O portal atende as versões atual e anterior de Chrome, Firefox, Safari e Edge. Não há suporte a Internet Explorer. |
| 3 | Plataforma móvel | O aplicativo de portaria atende Android 9 ou superior e iOS 14 ou superior. |
| 4 | Licenciamento | Devem ser usadas apenas bibliotecas com licença livre compatível com uso comercial, por restrição de orçamento da produtora. |
| 5 | Idioma e moeda | A versão inicial atende apenas português do Brasil e real, sem internacionalização. |
| 6 | Integração fiscal | Não há integração com emissor de nota fiscal nesta versão, conforme o escopo negativo. |

---

## 6. Anexos: diagramas BPMN

Os diagramas do processo estão em [processos/](processos/) na forma de arquivos `.bpmn` abríveis no Bizagi Modeler e no bpmn.io, acompanhados da descrição textual de cada processo. A coerência entre a modelagem e os requisitos é demonstrada na [matriz de rastreabilidade](rastreabilidade.md), que liga cada atividade dos diagramas ao requisito funcional correspondente.

| Processo | Nome | Requisitos cobertos |
|---|---|---|
| P1 | Criação e publicação de evento | RF03, RF04, RF05, RF06, RF07, RF08, RF09, RF24 |
| P2 | Venda de ingresso online | RF09, RF10, RF11, RF12, RF13, RF14, RF24 |
| P3 | Cancelamento e reembolso | RF12, RF15, RF22, RF24 |
| P4 | Check-in e controle de acesso | RF12, RF13, RF16, RF17, RF18 |
| P5 | Produção e realização do evento | RF19, RF20, RF21, RF23, RF24 |
| P6 | Fechamento financeiro e repasse | RF03, RF19, RF20, RF22, RF23, RF24 |
