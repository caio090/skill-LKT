---
name: especificacao-de-produto
description: >
  Escreve especificação de produto digital: problema, solução, backlog
  priorizado e roadmap por fase. Use quando o usuário pedir
  "especifica esse produto", "monta o backlog", "qual o roadmap desse
  app".
---

# especificacao-de-produto — Especificação, backlog e roadmap

## Quando usar

Produto digital em planejamento, precisando de documento de referência
pra guiar desenvolvimento.

## Quando não usar

Sistema já em produção estável sem produto novo em jogo → ajustes vão
direto em `organizar-projeto` (backlog operacional do dia a dia).

## Entradas

Escopo de `app-e-sistema`, objetivo de negócio.

## Dependências

`app-e-sistema`, `criar-produto-e-oferta`.

## Contexto que deve ser carregado

Escopo técnico e objetivo de negócio do projeto ativo.

---

## Workflow

### Modo: Especificação

1. Problema que o produto resolve (específico, não genérico).
2. Solução proposta em linguagem simples.
3. Critérios de sucesso (como saber que o produto funciona).

### Modo: Backlog

1. Transformar o escopo em itens de trabalho.
2. Priorizar por valor/esforço — essencial (MVP) primeiro.

### Modo: Roadmap

1. Organizar o backlog em fases/marcos temporais.
2. Marcar dependências entre fases.

Salvar em `<pasta-do-projeto-ativo>/07-tecnologia/especificacao.md`.

## Saídas

Especificação + backlog priorizado + roadmap por fase.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/07-tecnologia/`.

## Regras

- Backlog sempre separa essencial (MVP) de desejável.
- Roadmap não promete data sem considerar capacidade real da equipe.

## Critérios de qualidade

Todo item do backlog é rastreável ao problema definido na
especificação.

## Critérios de validação

Roadmap reflete dependências reais entre itens (não paraleliza o que
depende sequencialmente de outra coisa).

## Limitações

Não decide a arquitetura técnica (isso é `arquitetura-de-software`) —
especifica o produto, não a implementação.

## Contrato de handoff

Encaminha pra `arquitetura-de-software` e `organizar-projeto`
(execução do backlog no dia a dia).

## Exemplos de gatilhos positivos

- "Especifica esse produto novo"
- "Monta o backlog e o roadmap desse app"

## Exemplos de gatilhos negativos

- "Organiza as tarefas dessa semana" (é `organizar-projeto`)
