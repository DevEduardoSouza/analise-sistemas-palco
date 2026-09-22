# Atores do sistema Palco

Este documento identifica os atores usados nos diagramas de casos de uso do sistema Palco, desenvolvido para a casa de shows Cena Livre. Os atores foram extraídos do campo **Ator** dos requisitos funcionais detalhados em [../requisitos/requisitos-funcionais.md](../requisitos/requisitos-funcionais.md) e dos papéis relatados na [entrevista](../entrevista.md) com o dono da casa.

Ator é quem está fora da fronteira do sistema e interage com ele. Atores **primários** iniciam os casos de uso para atingir um objetivo próprio; atores **secundários** são acionados pelo sistema durante a execução de um caso de uso.

## 1. Atores primários

| Ator | Quem é na Cena Livre | Principal interesse | Requisitos |
|---|---|---|---|
| Dono | Proprietário da casa, que negocia as atrações e decide a agenda | Montar o show, abrir as vendas e decidir as exceções | RF01, RF04, RF05, RF06, RF08, RF15, RF19, RF20, RF22, RF23, RF26, RF27, RF28, RF31 |
| Sócio | Sócio responsável pelo dinheiro e pela produção | Definir preços, acompanhar o resultado e fechar as contas do show | RF07, RF14, RF15, RF19, RF20, RF21, RF22, RF23, RF26, RF29, RF31, RF33 |
| Administrativo | Funcionário que cuida de contratos, notas e pagamentos | Registrar despesas e documentos sem depender do sócio | RF23, RF33 |
| Bilheteria | Quem atende o público na bilheteria e no caixa da noite | Vender na porta e prestar contas do caixa | RF15, RF30, RF32 |
| Portaria | Quem fica na entrada conferindo ingressos | Liberar a entrada rápido, mesmo sem internet | RF13, RF17, RF18, RF28, RF32 |
| Loja parceira | Loja que vende ingressos por cota e acerta depois do show | Vender a própria cota e receber a comissão | RF29 |
| Cliente | Público que compra o ingresso | Comprar, receber e usar o ingresso sem transtorno | RF09, RF10, RF11, RF13, RF15, RF16 |
| Equipe | Segurança, som, luz, bar e limpeza escalados para a noite | Receber o convite da escala e confirmar presença | RF19 |

Todos os atores primários, exceto o Cliente não cadastrado que apenas consulta a página pública, autenticam-se pelo RF02.

Um mesmo funcionário pode acumular papéis — na Cena Livre a mesma pessoa trabalha na bilheteria e na portaria —, o que no diagrama é representado por atores distintos, e não por generalização, porque os objetivos são diferentes.

## 2. Atores secundários

| Ator | O que faz | Requisitos |
|---|---|---|
| Provedor de pagamento | Processa Pix e cartão e devolve a confirmação ao sistema, sem comprovante enviado pelo cliente | RF11, RF15 |
| Serviço de e-mail e mensagem | Entrega ingressos em PDF, confirmações, avisos de remarcação e convites de escala | RF12, RF24 |
| Conta Google | Autentica o cliente que opta por entrar com a conta Google | RF02 |

## 3. Tempo

O ator **Tempo** representa os disparos automáticos por prazo, e não uma pessoa. É ele quem inicia a expiração da reserva de quinze minutos do carrinho (RF10), o encerramento do prazo do Pix (RF11), a virada de lote por data (RF07) e a liberação de pré-reservas de data vencidas (RF26).

## 4. Por que "Sistema" não é ator

O campo **Ator** dos requisitos RF08, RF12, RF24 e RF25 traz "Sistema", indicando comportamento automático da aplicação. Em um diagrama de casos de uso, porém, o sistema é a própria fronteira: ele não pode ser ator de si mesmo. Esses comportamentos aparecem como:

- **Emissão do ingresso (RF12)** — incluída pelo caso de uso que conclui a venda, em qualquer canal, por relacionamento `<<include>>`.
- **Verificação de pendências (RF08)** — incluída pelo caso de uso de abertura das vendas, iniciado pelo Dono.
- **Notificações (RF24)** — executadas pelo sistema com o ator secundário Serviço de e-mail e mensagem.
- **Trilha de auditoria (RF25)** — registro automático das operações críticas, sem caso de uso próprio, citado como regra nos casos de uso que ela audita.
