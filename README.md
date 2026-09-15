# Análise de Sistemas — Sistema "Palco"

Análise de um sistema de gestão de shows para a **Cena Livre**, casa de shows de cerca de quatrocentos lugares, feita para a disciplina de Análise de Sistemas do 3º semestre de ADS do IFBA Irecê, com o professor Wild Barreto.

Este repositório contém a **análise**, não a implementação. A entrega pedida é o Documento de Visão com os requisitos e os diagramas BPMN do processo, anexados ao final, mantendo coerência entre a modelagem e os requisitos mapeados.

Os requisitos e os processos foram levantados numa entrevista com o dono do negócio, registrada em [`docs/entrevista.md`](docs/entrevista.md).

## O que tem aqui

| Caminho | Conteúdo |
|---|---|
| [`docs/entrevista.md`](docs/entrevista.md) | Transcrição da entrevista com o dono da Cena Livre e síntese dos problemas relatados. |
| [`docs/documento-de-visao.md`](docs/documento-de-visao.md) | Documento de Visão completo, na estrutura do modelo entregue pelo professor. |
| [`docs/requisitos/requisitos-funcionais.md`](docs/requisitos/requisitos-funcionais.md) | 32 requisitos funcionais ativos detalhados, acima do mínimo de 15 exigido, com a origem de cada um na entrevista. |
| [`docs/requisitos/requisitos-nao-funcionais.md`](docs/requisitos/requisitos-nao-funcionais.md) | 26 requisitos não funcionais, por categoria. |
| [`docs/processos/`](docs/processos/) | Um documento por processo, com atividades, requisitos atendidos e fluxo. |
| [`docs/rastreabilidade.md`](docs/rastreabilidade.md) | Matriz que liga cada requisito às atividades dos diagramas. |
| [`bpmn/`](bpmn/) | Arquivos `.bpmn` dos seis processos, prontos para abrir no Bizagi ou no bpmn.io. |
| [`bpmn/png/`](bpmn/png/) | Imagens dos diagramas, para colar no documento entregue em Word ou PDF. |
| [`tools/`](tools/) | Scripts que geram os diagramas e a documentação a partir de uma única definição. |

## Os seis processos modelados

| Processo | Nome | Assunto |
|---|---|---|
| P1 | Planejamento do show e abertura de vendas | Da proposta da banda à venda aberta, com agenda, contrato, cotas por canal e convidados. |
| P2 | Venda de ingressos nos canais | Página de vendas com pagamento confirmado e venda registrada pela loja parceira. |
| P3 | Cancelamento, remarcação e reembolso | Desistência do cliente, remarcação do show e devolução pelo canal de origem. |
| P4 | Entrada do público no dia do show | Portaria offline, lista de convidados, venda na porta e controle de lotação. |
| P5 | Produção do show | Escala com confirmação, cronograma do dia e pagamentos da noite. |
| P6 | Fechamento financeiro do show | Caixa da porta, resultado prévio, conferência de despesas e acerto do parceiro. |

## Como os arquivos são gerados

A definição dos processos, com raias, atividades, desvios e requisitos atendidos, vive num único lugar, em `tools/gen_bpmn.py`. Os diagramas e a documentação saem dela. Isso é o que impede a modelagem e os requisitos de divergirem ao longo do semestre.

```bash
python tools/gen_bpmn.py     # escreve os .bpmn em bpmn/
python tools/gen_docs.py     # escreve docs/processos/ e docs/rastreabilidade.md
python tools/render_html.py  # escreve build/, paginas para conferir o desenho
```

Para conferir o desenho no navegador, sirva a pasta `build` e abra qualquer página:

```bash
python tools/render_html.py
python -m http.server 8899 --directory build
```

Os arquivos `.bpmn` são BPMN 2.0 com coordenadas embutidas, então abrem já desenhados no [bpmn.io](https://demo.bpmn.io/), no Camunda Modeler e no Bizagi Modeler.

## Acompanhamento do trabalho

Os requisitos e os processos também estão num quadro Trello, usado para acompanhar o andamento da análise durante o semestre. O link fica em [`docs/plataforma.md`](docs/plataforma.md), junto com a justificativa da escolha da ferramenta.
