---
name: organizar-projeto
description: >
  Organiza a operação de um projeto/equipe: prioriza demandas, distribui
  responsáveis, planeja sprint/ciclo de trabalho, acompanha pendências e
  audita a operação em busca de gargalo. Use quando o usuário pedir
  "organiza as demandas dessa semana", "quem fica responsável por cada
  coisa", "planeja o próximo ciclo", "por que a operação está travando".
---

# organizar-projeto — Organização operacional

## Quando usar

Gestão do dia a dia de um projeto/equipe: o que fazer, quem faz, em que
ordem, e onde a operação está travando.

## Quando não usar

Planejamento estratégico de negócio (isso é `plano-estrategico`) — esta
skill organiza a execução, não decide a estratégia.

## Entradas

Lista de demandas/tarefas, equipe disponível, prazos.

## Dependências

`_memoria/equipe.md`, `_memoria/pendencias.md`, `PROJETO.md`.

## Contexto que deve ser carregado

Pendências e equipe do projeto ativo.

---

## Workflow

### Modo: Priorizar demandas

1. Listar demandas com impacto e urgência.
2. Priorizar por impacto no objetivo do projeto (`PROJETO.md`), não por
   "quem pediu primeiro" ou "o que é mais fácil".

### Modo: Distribuir responsáveis

1. Cruzar demanda com capacidade/habilidade de cada pessoa
   (`_memoria/equipe.md`).
2. Não sobrecarregar uma pessoa só porque é a mais rápida — considerar
   capacidade real disponível.

### Modo: Planejar sprint/ciclo

1. Definir o que entra no ciclo (baseado na priorização).
2. Definir critério de "pronto" pra cada item.
3. Definir data de revisão do ciclo.

### Modo: Acompanhar pendências

1. Revisar `_memoria/pendencias.md`/`PROJETO.md`: o que venceu, o que
   está travado, o que foi resolvido sem registrar.
2. Atualizar status.

### Modo: Auditoria operacional

1. Identificar gargalo recorrente (mesma tarefa sempre atrasa, mesma
   pessoa sempre sobrecarregada).
2. Recomendar ajuste de processo (`criar-sop` se for processo mal
   documentado).

## Saídas

Lista priorizada, distribuição de responsáveis, plano de ciclo, ou
relatório de auditoria operacional.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/00-contexto/` ou `PROJETO.md` diretamente.

## Regras

- Priorização por impacto real, não por ordem de chegada.
- Nunca distribuir responsabilidade sem considerar capacidade real.

## Critérios de qualidade

Toda demanda priorizada tem impacto e urgência declarados.

## Critérios de validação

Pendências de `_memoria/pendencias.md` refletem o estado real depois do
acompanhamento.

## Limitações

Não decide prioridade estratégica de negócio — só organiza a execução
do que já foi decidido.

## Contrato de handoff

Encaminha pra `criar-sop` (gargalo de processo) e `plano-estrategico`
(se o gargalo for estratégico, não operacional).

## Exemplos de gatilhos positivos

- "Organiza as demandas dessa semana"
- "Por que a operação está travando"

## Exemplos de gatilhos negativos

- "Qual a estratégia geral do negócio" (é `plano-estrategico`)
