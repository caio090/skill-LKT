---
name: plano-de-captacao
description: >
  Planeja a logística de gravação a partir do storyboard: cronograma de
  produção, lista de equipamentos, locação, equipe necessária, plano de
  áudio, continuidade e orçamento audiovisual. Use quando o usuário
  pedir "planeja a gravação", "o que precisamos levar pra filmagem".
---

# plano-de-captacao — Logística de gravação

## Quando usar

Depois de `storyboard`, antes do dia de gravação.

## Quando não usar

Storyboard ainda não existe → fazer isso primeiro.

## Entradas

Storyboard com necessidade de produção por cena.

## Dependências

`storyboard`.

## Contexto que deve ser carregado

Storyboard e briefing do projeto ativo.

---

## Workflow

1. **Cronograma de produção:** ordem de gravação das cenas (não
   necessariamente a ordem do roteiro — agrupar por locação/
   equipamento pra otimizar o dia).
2. **Lista de equipamentos:** câmera, lente, luz, áudio, tripé,
   estabilizador — o que cada cena exige.
3. **Locação:** onde gravar cada bloco de cenas.
4. **Equipe necessária:** quem precisa estar (direção, câmera, áudio,
   produção, talentos/atores).
5. **Plano de áudio:** captação direta vs. dublagem/narração posterior,
   microfone necessário por cena.
6. **Continuidade:** o que precisa se manter igual entre cenas
   (figurino, posição de objetos, luz) pra não quebrar a edição.
7. **Orçamento audiovisual:** equipamento (aluguel ou próprio),
   locação, equipe, pós-produção.
8. Salvar em `<pasta-do-projeto-ativo>/06-audiovisual/plano-captacao.md`.

## Saídas

Cronograma, lista de equipamentos, plano de áudio, continuidade e
orçamento.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/06-audiovisual/`.

## Regras

- Cronograma otimizado por locação/equipamento, não pela ordem do
  roteiro.
- Continuidade documentada antes de gravar, não descoberta na edição.

## Critérios de qualidade

Equipe sabe exatamente o que levar e quando, sem perguntar no dia.

## Critérios de validação

Toda necessidade de produção do storyboard está coberta no plano.

## Limitações

Não executa a gravação — planeja.

## Contrato de handoff

Encaminha pra `direcao-de-cena` (execução no dia) e
`briefing-de-edicao` (pós-produção).

## Exemplos de gatilhos positivos

- "Planeja a gravação desse comercial"
- "O que precisamos levar pra filmagem"

## Exemplos de gatilhos negativos

- "Monta o storyboard" (é `storyboard`, passo anterior)
