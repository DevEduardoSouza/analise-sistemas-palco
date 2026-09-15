# Contexto do projeto

## O que é

Trabalho da disciplina **Análise de Sistemas**, 3º semestre de ADS, IFBA Irecê, professor **Wild Barreto**, turma "26.2 ANÁLISE DE SISTEMAS". Aluno: Eduardo de Souza Silva.

Este repositório é **análise, não implementação**. Não crie código de aplicação, banco de dados nem telas aqui. O produto do trabalho é documentação: Documento de Visão, requisitos e diagramas BPMN.

O trabalho é individual. O tema escolhido é um **sistema de gestão de shows**, chamado "Palco" no documento, feito para o cliente **Cena Livre**, uma casa de shows. Os requisitos e processos saem da entrevista simulada com o dono, em `docs/entrevista.md`; cada requisito cita o problema relatado (A01 a A16) que o originou.

## O que o professor pediu

Do mural do Google Classroom, aviso de 3 de setembro de 2026:

- O Documento de Visão deve contemplar **no mínimo 15 requisitos funcionais devidamente detalhados**. Aqui há 32 ativos.
- Os **diagramas BPMN** do processo devem ser incluídos **como anexo ao final do documento**.
- Deve haver **coerência entre a modelagem dos processos (BPMN) e os requisitos mapeados**. É o que `docs/rastreabilidade.md` demonstra, e é o ponto mais provável de perda de nota se algo for editado pela metade.

Materiais de apoio da turma: modelo "Documento de Visão.docx", slides de Engenharia de Requisitos, apostilas de BPMN, tutorial do Bizagi Modeler e o livro de UML 2 do Guedes. Ferramentas sugeridas pelo professor: Bizagi Modeler, bpmn.io, draw.io e o plugin Yaoqiang.

A estrutura de seções do Documento de Visão segue o modelo `.docx` do professor e não deve ser reorganizada: Introdução, Objetivos deste documento, Escopo do produto, Definições, Contexto, Declaração do Problema, Requisitos específicos com funcionais e não funcionais divididos em Usabilidade, Segurança, Performance e Portabilidade, Lista de Riscos e Lista de Restrições de hardware e de software.

## Regra central de manutenção

A definição dos processos vive **num único lugar**: a lista `PROCESSES` em `tools/gen_bpmn.py`. Cada atividade carrega o campo `refs` com os requisitos que ela atende.

A partir dela são gerados:

- `bpmn/*.bpmn` por `tools/gen_bpmn.py`
- `docs/processos/*.md` e `docs/rastreabilidade.md` por `tools/gen_docs.py`
- `build/*.html` por `tools/render_html.py`, apenas para conferência visual

**Nunca edite os arquivos gerados à mão.** Para mudar um processo, altere `PROCESSES` e rode de novo:

```bash
python tools/gen_bpmn.py && python tools/gen_docs.py
```

Ao acrescentar ou renomear um requisito funcional, atualize os três lugares que o citam: o detalhamento em `docs/requisitos/requisitos-funcionais.md`, o quadro resumo na seção 3.1 do Documento de Visão e o campo `refs` da atividade correspondente em `tools/gen_bpmn.py`.

## Convenções

- Texto em **português do Brasil**, com acentuação, inclusive dentro dos rótulos dos diagramas.
- Código de requisito é estável: `RF01` a `RF33` e `RNF01` a `RNF26`. O `RF03` foi retirado. Nunca reaproveite um código de requisito removido. Ao criar um RF novo, atualize também `ULTIMO_RF` em `tools/gen_docs.py`.
- Processos são `P1` a `P6`, e o nome do arquivo `.bpmn` começa pelo código.
- Comentários e docstrings nos scripts em português, sem acentuação, para evitar problema de codificação no Windows.
- `build/` é descartável e não entra no controle de versão.

## Como conferir o desenho

```bash
python tools/render_html.py
python -m http.server 8899 --directory build
# abrir http://127.0.0.1:8899/P1-planejamento-e-abertura-de-vendas.html
```

As imagens em `bpmn/png/` foram capturadas dessas páginas e são o que se cola no documento final em Word.

## Entrega

O documento entregue ao professor sai de `docs/documento-de-visao.md`, convertido para Word ou PDF, com as imagens de `bpmn/png/` anexadas ao final, na ordem de P1 a P6.
