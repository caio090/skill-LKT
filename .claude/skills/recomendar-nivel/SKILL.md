---
name: recomendar-nivel
description: >
  A partir de uma classificação de nível atual (classificar-nivel),
  recomenda o nível adequado e executável para o objetivo do projeto —
  nunca o nível mais alto por padrão. Considera prazo, orçamento,
  capacidade e risco. Gera a lacuna entre atual e recomendado. Use
  quando o usuário disser "qual nível a gente deveria buscar", "o que
  falta pra chegar no próximo nível", ou depois de classificar-nivel.
---

# recomendar-nivel — Nível adequado, não o mais alto por padrão

Recomenda o nível certo para o objetivo real do projeto, considerando
capacidade de execução — não empurra sempre o nível máximo. Ver
`knowledge/niveis/COMO_FUNCIONAM_OS_NIVEIS.md`.

## Quando usar

- Depois de `classificar-nivel`, para decidir até onde faz sentido
  avançar agora.

## Quando não usar

- Sem uma classificação de nível atual já feita (rodar
  `classificar-nivel` primeiro).

## Entradas

- `level-assessment` atual (nível atual, confiança).
- Objetivo do projeto, prazo, orçamento, capacidade de operação
  (própria e do cliente), risco aceitável.

## Dependências

- `schemas/level-recommendation.schema.json`
- `catalogo/niveis/`, `catalogo/perfis-de-entrega/`
- `.claude/skills/classificar-nivel` (entrada)
- `.claude/skills/projecoes` (faixas de prazo/custo viram cenário)

## Contexto que deve ser carregado

- `level-assessment` mais recente da dimensão.
- `PROJETO.md` (objetivo, prazo, orçamento).

---

## Workflow

### Passo 1 — Ler o nível atual e o objetivo

Carregar `level-assessment` e o objetivo declarado do projeto.

### Passo 2 — Considerar viabilidade, não só ambição

Avaliar prazo, orçamento, capacidade (própria e do cliente), risco e
dependências antes de sugerir um nível-alvo. **Nunca recomendar o
nível mais alto do conjunto por padrão** — recomendar o nível seguinte
que seja realista de executar com os recursos declarados, a não ser
que o usuário explicitamente peça o mais avançado e aceite os
riscos/custos envolvidos.

### Passo 3 — Calcular a lacuna

Comparar `level-definition` do nível atual com a do recomendado:
diferença em critérios, entregáveis, dependências, papéis, prazo,
custo.

### Passo 4 — Gerar `level-recommendation`

Preencher todos os campos do schema — lacunas, prioridades,
entregáveis, tarefas, dependências, papéis, prazo/custo projetado
(conservador/base/agressivo), riscos, critérios de aceite, próxima
revisão.

### Passo 5 — Explicar a diferença

Em linguagem simples: o que muda entre o nível atual e o recomendado,
e por que essa é a recomendação (não a mais alta possível).

---

## Saídas

`level-recommendation` salvo, com lacuna, prioridades e faixa de
prazo/custo — nunca preço final (isso é
`proposta-e-precificacao`/`gerar-proposta-a-partir-do-nivel`).

## Regras

- Nunca recomendar o nível mais alto por padrão.
- Nunca tratar faixa de prazo/custo como preço fechado.
- Sempre explicar a diferença entre atual e recomendado em linguagem
  simples.

## Critérios de qualidade

- Toda recomendação considera capacidade real de execução, não só
  ambição do objetivo.

## Critérios de validação

- `level-recommendation` válido contra
  `schemas/level-recommendation.schema.json`.

## Limitações

- Não decide sozinha quando o cliente insiste em pular etapas — nesse
  caso, apresenta os riscos e segue com o que for decidido, registrando
  a decisão.

## Caminho de salvamento

`workspaces/<tipo>/<slug>/[projetos/<projeto>/]02-modelagem/RECOMENDACAO-NIVEL-<dimensao>.json`

## Contrato de handoff

Recebe de `classificar-nivel`. Encaminha para `gerar-plano-de-avanco`
(transformar lacuna em ações) e `gerar-escopo-por-nivel`.

## Exemplos de gatilhos positivos

- "Qual nível a gente deveria buscar em financeiro?"
- "O que falta pra chegar no próximo nível de maturidade digital?"

## Exemplos de gatilhos negativos

- "Classifica o nível atual" (é `classificar-nivel`, entrada desta
  skill)

Arquivos de apoio: `perguntas.txt`, `fluxo.md`, `saidas.md`,
`validacao.md`, `exemplos.md`.
