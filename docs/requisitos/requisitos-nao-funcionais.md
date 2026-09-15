# Requisitos Não Funcionais — Sistema Palco

As categorias seguem o modelo de Documento de Visão da disciplina: Usabilidade, Segurança, Performance e Portabilidade. Foram acrescentadas duas categorias complementares, Confiabilidade e Conformidade legal, por serem determinantes num sistema de bilheteria. Os valores foram calibrados para a Cena Livre, casa de cerca de quatrocentos lugares que também realiza shows maiores em espaços alugados, conforme a [entrevista com o dono](../entrevista.md).

## Usabilidade

| Código | Aplicação | Descrição |
|---|---|---|
| RNF01 | Portal público | A compra de um ingresso deve ser concluída em no máximo cinco telas contadas da página do evento até a confirmação, sem exigir cadastro prévio do comprador. |
| RNF02 | Portal público | Os preços devem ser exibidos com a taxa de serviço destacada em separado do valor do ingresso, em todas as etapas da compra. |
| RNF03 | Aplicativo de portaria | A tela de leitura de QR Code deve indicar o resultado por cor e por texto, verde para liberado e vermelho para negado, legível sob luz forte e à distância de um braço. |
| RNF04 | Todo o sistema | A interface deve seguir as diretrizes WCAG 2.1 nível AA, com contraste mínimo, navegação por teclado e textos alternativos nas imagens. |
| RNF05 | Painel do dono | O dono, que declarou usar apenas o celular e não ter familiaridade com computador, deve conseguir cadastrar um show simples e abrir as vendas pelo celular em menos de dez minutos, sem treinamento formal. |

## Segurança

| Código | Aplicação | Descrição |
|---|---|---|
| RNF06 | Todo o sistema | As senhas devem ser armazenadas com função de hash de sentido único com sal, nunca em texto claro nem com criptografia reversível. |
| RNF07 | Todo o sistema | Todo o tráfego deve ocorrer sobre HTTPS com TLS 1.2 ou superior, e o acesso por HTTP deve ser redirecionado. |
| RNF08 | Bilheteria | O sistema não deve armazenar número completo do cartão, código de segurança nem data de validade, delegando a captura ao provedor de pagamento certificado pelo padrão PCI DSS. |
| RNF09 | Ingresso digital | O QR Code deve conter assinatura digital verificável offline, de modo que uma cópia forjada seja rejeitada mesmo sem conexão com o servidor. |
| RNF10 | Painel financeiro | O acesso aos perfis Dono e Sócio, que enxergam os valores financeiros, deve exigir segundo fator de autenticação. |
| RNF11 | Todo o sistema | O controle de acesso deve ser aplicado no servidor a cada requisição, e não apenas pela ocultação de itens na interface. |

## Performance

| Código | Aplicação | Descrição |
|---|---|---|
| RNF12 | Portal público | A página do evento deve carregar em até dois segundos no percentil 95, considerando conexão móvel de quatro megabits. |
| RNF13 | Bilheteria | O sistema deve suportar quinhentas compras simultâneas na abertura de vendas de um show em espaço alugado, somando todos os canais, sem venda acima da capacidade da montagem. |
| RNF14 | Aplicativo de portaria | A validação de um ingresso deve responder em até dois segundos, e cada celular de portaria deve sustentar a entrada de seiscentas pessoas por hora, permitindo encher a casa em cerca de vinte minutos com duas pessoas lendo ingressos. |
| RNF15 | Relatórios | Os relatórios gerenciais devem ser gerados em até dez segundos para uma janela de doze meses, com processamento assíncrono e aviso ao usuário quando esse tempo for excedido. |

## Portabilidade

| Código | Aplicação | Descrição |
|---|---|---|
| RNF16 | Portal público | A interface deve ser responsiva e funcionar em telas a partir de trezentos e vinte pixels de largura, nas versões atuais e na anterior de Chrome, Firefox, Safari e Edge. |
| RNF17 | Aplicativo de portaria | O aplicativo deve rodar em Android 9 ou superior e iOS 14 ou superior, em dispositivos de entrada com câmera traseira. |
| RNF18 | Servidor | A aplicação deve ser distribuída em contêineres, de modo a ser instalável em qualquer provedor compatível com Docker, sem dependência de serviço proprietário de um único fornecedor. |
| RNF19 | Dados | O sistema deve permitir exportação completa dos dados da casa em formato aberto, CSV e JSON, para uso do contador e garantindo a portabilidade prevista na legislação. |

## Confiabilidade e disponibilidade

| Código | Aplicação | Descrição |
|---|---|---|
| RNF20 | Bilheteria | A disponibilidade mensal deve ser de no mínimo noventa e nove vírgula cinco por cento, excluídas janelas de manutenção comunicadas com quarenta e oito horas de antecedência. |
| RNF21 | Aplicativo de portaria | A portaria e a venda na porta devem continuar operando por no mínimo seis horas sem conexão de rede, sincronizando ao restabelecer o acesso. |
| RNF22 | Banco de dados | Deve haver cópia de segurança diária com retenção de trinta dias e teste de restauração trimestral documentado. |

## Conformidade legal

| Código | Aplicação | Descrição |
|---|---|---|
| RNF23 | Todo o sistema | O tratamento de dados pessoais deve seguir a Lei Geral de Proteção de Dados, com base legal registrada, consentimento para uso promocional e atendimento a pedidos de exclusão em até quinze dias. |
| RNF24 | Bilheteria | A cota de meia-entrada deve respeitar o limite de quarenta por cento do total de ingressos por sessão, conforme a Lei 12.933 de 2013. |
| RNF25 | Bilheteria | A política de cancelamento deve respeitar o direito de arrependimento de sete dias previsto no Código de Defesa do Consumidor para compras fora do estabelecimento. |
| RNF26 | Auditoria | Os registros de auditoria, os comprovantes de despesas e os fechamentos de caixa devem ser retidos por cinco anos. |
