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

## Casos de uso

Os diagramas de casos de uso em UML seguem a mesma regra dos processos: a definição vive **num único lugar**, a lista `PACOTES` em `tools/gen_casos_de_uso.py`, com os atores, os casos de uso, as associações e os relacionamentos `include` e `extend` de cada pacote. Cada caso carrega o campo `refs` com os requisitos que ele atende, e as coordenadas são escritas à mão, como no `gen_bpmn.py`.

A partir dela são gerados:

- `casos-de-uso/*.drawio`, XML do mxGraph sem compressão, que o draw.io abre com as formas editáveis
- `build/*.svg`, prévia descartável para conferir o desenho sem abrir o draw.io

```bash
python tools/gen_casos_de_uso.py
```

O texto de apoio, esse sim escrito à mão, está em `docs/casos-de-uso/`: `atores.md` traz os oito atores primários, os três secundários e o ator Tempo, com a justificativa de por que "Sistema" não é ator; `casos-de-uso.md` agrupa os 32 requisitos ativos em 43 casos de uso distribuídos em sete pacotes, um por processo de P1 a P6 mais o pacote de apoio Acesso e administração, e fecha com a tabela de cobertura de requisito para caso de uso.

Requisito e caso de uso não são a mesma coisa: um requisito extenso vira vários casos, como o RF15, e um caso pode atender mais de um requisito, como o UC11. Ao mexer num caso de uso, mantenha alinhados o pacote em `casos-de-uso.md`, a tabela de cobertura no fim do mesmo arquivo e a entrada em `PACOTES`.

## Convenções

- Texto em **português do Brasil**, com acentuação, inclusive dentro dos rótulos dos diagramas.
- Código de requisito é estável: `RF01` a `RF33` e `RNF01` a `RNF26`. O `RF03` foi retirado. Nunca reaproveite um código de requisito removido. Ao criar um RF novo, atualize também `ULTIMO_RF` em `tools/gen_docs.py`.
- Processos são `P1` a `P6`, e o nome do arquivo `.bpmn` começa pelo código.
- Código de caso de uso é estável: `UC01` a `UC43`. Nunca reaproveite um código retirado. O pacote de um diagrama usa o código do processo correspondente, e o nome do arquivo `.drawio` começa por ele.
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
