---
name: direcao-de-cena
description: >
  Orienta a execução no dia de gravação: o que checar antes de cada
  cena, direção de talento/depoimento, continuidade em tempo real e
  critério de "cena aprovada, pode seguir". Use quando o usuário pedir
  "como dirigir essa cena", "o que preciso checar antes de gravar".
---

# direcao-de-cena — Direção durante a gravação

## Quando usar

No dia da gravação, antes/durante cada cena.

## Quando não usar

Planejamento prévio (isso é `plano-de-captacao`/`storyboard`).

## Entradas

Storyboard, shot list, plano de captação.

## Dependências

`storyboard`, `lista-de-planos`, `plano-de-captacao`.

## Contexto que deve ser carregado

Storyboard e plano de captação do projeto ativo.

---

## Workflow

1. Antes de cada cena: conferir continuidade (figurino, posição,
   iluminação) contra a cena anterior da mesma sequência.
2. Direção de talento/depoimento: orientar tom, ritmo, o que evitar
   (jargão que não combina com o tom da marca).
3. Conferir áudio captado (sem ruído indesejado, volume adequado).
4. Critério de "cena aprovada": bate com o objetivo da cena no
   storyboard — se não bater, regravar antes de seguir pra próxima.
5. Registrar o que foi gravado vs. o que ficou pendente.

## Saídas

Registro de cenas aprovadas/pendentes no dia.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/06-audiovisual/registro-captacao-<data>.md`.

## Regras

- Nunca aprovar cena com problema de continuidade óbvio.
- Critério de aprovação vem do storyboard, não de "achei que ficou
  legal".

## Critérios de qualidade

Toda cena aprovada atende ao objetivo definido no storyboard.

## Critérios de validação

Registro final lista claramente o que foi gravado e o que falta.

## Limitações

Não substitui o julgamento do diretor/produtor no set — orienta o
critério, a decisão final é humana.

## Contrato de handoff

Encaminha pra `briefing-de-edicao` com o material gravado.

## Exemplos de gatilhos positivos

- "Como dirigir essa cena de depoimento"
- "O que preciso checar antes de gravar essa cena"

## Exemplos de gatilhos negativos

- "Planeja a logística da gravação" (é `plano-de-captacao`)
