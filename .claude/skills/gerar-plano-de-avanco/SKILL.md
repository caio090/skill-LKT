---
name: gerar-plano-de-avanco
description: >
  Transforma a lacuna entre nível atual e recomendado
  (recomendar-nivel) em ações concretas — entregas, tarefas,
  responsáveis por papel, dependências, prazo, custo, validação, risco
  e ordem recomendada. Use quando o usuário disser "como a gente chega
  no próximo nível", "monta o plano pra evoluir isso", ou depois de
  recomendar-nivel.
---

# gerar-plano-de-avanco — Da lacuna à ação concreta

Converte a lacuna registrada em `level-recommendation` num plano
executável — sem inventar prazo/custo sem base.

## Quando usar

- Depois de `recomendar-nivel`, quando o usuário decide seguir com o
  avanço.

## Quando não usar

- Sem uma `level-recommendation` já gerada.

## Entradas

- `level-recommendation` (lacunas, entregáveis, tarefas já listadas
  em alto nível).
- Prazo e orçamento disponíveis (para ordenar prioridade real).

## Dependências

- `schemas/level-recommendation.schema.json`
- `schemas/projeto.schema.json` (roadmap/entregas do projeto)
- `.claude/skills/projecoes` (custo/prazo projetado)

## Contexto que deve ser carregado

- `level-recommendation` de origem.
- `PROJETO.md` (para encaixar o plano no roadmap já existente, sem
  duplicar).

---

## Workflow

### Passo 1 — Listar as lacunas (ver `perguntas.txt` se precisar confirmar prioridade)

Uma linha por lacuna, vinda de `level-recommendation.lacunas`.

### Passo 2 — Transformar cada lacuna em ação

Para cada lacuna: ação, entrega associada, tarefa(s), responsável por
papel, dependência, prazo, custo, critério de validação, risco.

### Passo 3 — Ordenar

Ordem recomendada considerando dependência (o que bloqueia o quê) e
impacto — não necessariamente a ordem em que as lacunas foram listadas.

### Passo 4 — Consolidar prazo/custo total

Somar por fase (não só por ação isolada), e encaminhar para
`projecoes` se o usuário quiser cenário conservador/base/agressivo do
plano inteiro.

### Passo 5 — Registrar no roadmap do projeto

Atualizar `PROJETO.md`/roadmap com as fases do plano, sem duplicar o
que já estava lá.

---

## Saídas

Plano de avanço: lista ordenada de ações com entrega, tarefa,
responsável, dependência, prazo, custo, critério de validação e risco.

## Regras

- Nunca inventar prazo/custo sem base na faixa do nível ou em dado
  real do projeto.
- Ordem sempre justificada por dependência/impacto, não arbitrária.

## Critérios de qualidade

- Toda ação do plano rastreia de volta a uma lacuna específica.

## Critérios de validação

- Toda ação tem responsável por papel e critério de validação.

## Limitações

- Não executa as ações — só planeja. Execução é dos módulos/skills
  correspondentes a cada entrega.

## Caminho de salvamento

`workspaces/<tipo>/<slug>/[projetos/<projeto>/]03-planejamento/PLANO-DE-AVANCO-<dimensao>.md`

## Contrato de handoff

Recebe de `recomendar-nivel`. Encaminha para `gerar-escopo-por-nivel`
(separar obrigatório/opcional/futuro) e para os módulos de execução
correspondentes a cada entrega do plano.

## Exemplos de gatilhos positivos

- "Como a gente chega no próximo nível de maturidade financeira?"
- "Monta o plano pra evoluir a operação"

## Exemplos de gatilhos negativos

- "Qual nível a gente deveria buscar?" (é `recomendar-nivel`, entrada
  desta skill)

Arquivos de apoio: `perguntas.txt`, `fluxo.md`, `saidas.md`,
`validacao.md`, `exemplos.md`.
