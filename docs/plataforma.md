# Plataforma de acompanhamento

## Escolha

**Trello**, quadro [Análise de Sistemas — Sistema Palco (IFBA)](https://trello.com/b/BCEWi4vI).

O critério de escolha foi um só: precisa existir um servidor MCP funcionando, para que o quadro possa ser lido e alterado por conversa com o Claude Code, sem abrir o navegador. O Trello foi a única ferramenta de gestão que atendeu esse critério neste ambiente, com o servidor já conectado e autenticado.

## O que o quadro tem

| Lista | Conteúdo |
|---|---|
| Backlog de requisitos | Vazia. Recebe requisito novo que aparecer na revisão com o professor. |
| Em detalhamento | RF01, RF02 e RF25, funcionalidades de apoio sem passo próprio no BPMN. |
| Modelado no BPMN | Os 22 requisitos que já aparecem em alguma atividade dos diagramas. |
| Concluído | Vazia. Recebe o que for validado na apresentação. |
| Processos BPMN | Os seis processos, com raias, requisitos cobertos e o arquivo correspondente. |
| Entrega e referências | As três exigências do professor e os links da turma e do repositório. |

Etiquetas de prioridade: Essencial em vermelho, Importante em amarelo, Desejável em azul. Processo BPMN em roxo.

## O que dá para fazer por conversa

Com o servidor MCP conectado, dá para pedir em linguagem natural e o quadro é alterado na hora. Alguns exemplos do que já está disponível:

- Mover um requisito de lista quando ele for detalhado ou modelado.
- Criar requisito novo com descrição, prioridade e processo.
- Adicionar checklist de critérios de aceitação a um card.
- Comentar num card e ler os comentários.
- Listar o que está em cada lista, para conferir o andamento antes de uma entrega.

## Alternativas consideradas

**GitHub Projects e Issues.** Ficam no mesmo lugar do repositório e são controláveis pela linha de comando com `gh`, que já está autenticado nesta máquina. Foi a segunda opção. Perde para o Trello na visualização de quadro, que é mais direta para acompanhar requisito por requisito, e exigiria manter dois modelos mentais, o de issue e o de card.

**Notion.** Tem servidor MCP oficial e seria uma boa base de documentação e quadro no mesmo lugar. Foi descartado porque exigiria instalar e autenticar um servidor novo antes de qualquer trabalho útil, e o ganho não compensaria o atraso.

**Jira.** Bom para rastreabilidade de requisito, que é justamente o ponto cobrado pelo professor, mas pesado demais para um trabalho de disciplina de um semestre.

## Pendência de sincronização

Depois da entrevista com o dono da Cena Livre, os requisitos passaram a ser RF01 a RF33, com o RF03 retirado, e os seis processos foram remodelados. O quadro ainda reflete a versão anterior, de 25 requisitos, e precisa ser atualizado: arquivar o card do RF03, criar os cards de RF26 a RF33 e renomear os cards dos processos.

## Observação sobre a fonte da verdade

O quadro serve para **acompanhar** o andamento. A fonte da verdade dos requisitos e dos processos continua sendo o repositório, em particular `tools/gen_bpmn.py`, de onde saem os diagramas e a matriz de rastreabilidade. Se o quadro e o repositório divergirem, vale o repositório.
