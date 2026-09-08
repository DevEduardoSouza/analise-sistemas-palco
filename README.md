# Análise de Sistemas — Sistema "Palco"

Análise de um sistema de gestão de eventos e shows, feita para a disciplina de Análise de Sistemas do 3º semestre de ADS do IFBA Irecê, com o professor Wild Barreto.

Este repositório contém a **análise**, não a implementação. A entrega pedida é o Documento de Visão com os requisitos e os diagramas BPMN do processo, anexados ao final, mantendo coerência entre a modelagem e os requisitos mapeados.

## O que tem aqui

| Caminho | Conteúdo |
|---|---|
| [`docs/documento-de-visao.md`](docs/documento-de-visao.md) | Documento de Visão completo, na estrutura do modelo entregue pelo professor. |
| [`docs/requisitos/requisitos-funcionais.md`](docs/requisitos/requisitos-funcionais.md) | 25 requisitos funcionais detalhados, acima do mínimo de 15 exigido. |
| [`docs/requisitos/requisitos-nao-funcionais.md`](docs/requisitos/requisitos-nao-funcionais.md) | 26 requisitos não funcionais, por categoria. |
| [`docs/processos/`](docs/processos/) | Um documento por processo, com atividades, requisitos atendidos e fluxo. |
| [`docs/rastreabilidade.md`](docs/rastreabilidade.md) | Matriz que liga cada requisito às atividades dos diagramas. |
| [`bpmn/`](bpmn/) | Arquivos `.bpmn` dos seis processos, prontos para abrir no Bizagi ou no bpmn.io. |
| [`bpmn/png/`](bpmn/png/) | Imagens dos diagramas, para colar no documento entregue em Word ou PDF. |
| [`tools/`](tools/) | Scripts que geram os diagramas e a documentação a partir de uma única definição. |

## Os seis processos modelados

| Processo | Nome | Assunto |
|---|---|---|
| P1 | Criação e publicação de evento | Da chegada da produtora ao evento no ar, com duas aprovações. |
| P2 | Venda de ingresso online | Vitrine, reserva temporária, pagamento e emissão do ingresso. |
| P3 | Cancelamento e reembolso | Política automática, análise manual, invalidação e estorno. |
| P4 | Check-in e controle de acesso | Portaria com leitura de QR Code e operação offline. |
| P5 | Produção e realização do evento | Atrações, fornecedores, escala e cronograma do dia. |
| P6 | Fechamento financeiro e repasse | Consolidação, conferência, fechamento e repasse ao produtor. |

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
