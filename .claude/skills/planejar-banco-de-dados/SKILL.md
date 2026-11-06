---
name: planejar-banco-de-dados
description: >
  Modela o banco de dados de um sistema: entidades, relacionamentos,
  campos, índices — incluindo modo específico para Supabase (Postgres +
  auth + storage). Use quando o usuário pedir "modela o banco de dados
  desse sistema", "estrutura as tabelas no Supabase".
---

# planejar-banco-de-dados — Modelagem de dados

## Quando usar

Depois de `app-e-sistema` levantar as entidades em linguagem simples,
antes de implementar.

## Quando não usar

Banco já modelado, só precisando de query pontual → direto no código.

## Entradas

Entidades e relacionamentos levantados em `app-e-sistema`.

## Dependências

`app-e-sistema`, `arquitetura-de-software`.

## Contexto que deve ser carregado

Escopo de dados do projeto ativo.

---

## Workflow

1. Transformar entidades em tabelas: campos, tipos, obrigatoriedade.
2. Definir relacionamentos (um-pra-muitos, muitos-pra-muitos) e chaves
   estrangeiras.
3. Definir índices necessários (campos de busca/filtro frequente).
4. **Modo Supabase (quando aplicável):** considerar Row Level Security
   (RLS) desde o desenho — nunca modelar tabela sensível sem já pensar
   na política de acesso; usar Auth do Supabase pra usuário/permissão em
   vez de reinventar; Storage pra arquivo, não guardar binário na
   tabela.
5. Salvar em `<pasta-do-projeto-ativo>/07-tecnologia/banco-de-dados.md`.

## Saídas

Modelo de dados (tabelas, campos, relacionamentos, índices) + política
de acesso quando aplicável.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/07-tecnologia/`.

## Regras

- Toda tabela com dado sensível já nasce com política de acesso
  pensada (RLS ou equivalente), não como adição posterior.
- Não modelar campo especulativo ("pode ser que precise no futuro")
  sem necessidade concreta atual.

## Critérios de qualidade

Todo relacionamento do modelo reflete uma necessidade real do escopo
(`app-e-sistema`), não suposição.

## Critérios de validação

Modelo cobre todas as entidades listadas em `app-e-sistema`.

## Limitações

Não executa migração real no banco — modela; execução é
`arquitetura-de-software`/implementação.

## Contrato de handoff

Encaminha pra `arquitetura-de-software` e `integrar-api`.

## Exemplos de gatilhos positivos

- "Modela o banco de dados desse sistema novo"
- "Estrutura as tabelas no Supabase com RLS"

## Exemplos de gatilhos negativos

- "Corrige essa query lenta" (é `depurar-erro`/`revisar-codigo`)
