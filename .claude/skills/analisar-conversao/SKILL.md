---
name: analisar-conversao
description: >
  Calcula e explica volume, taxa, perda, tendência e gargalo de um
  funil ou pipeline, com hipótese, recomendação e nível de confiança —
  sinalizando quando faltar dado suficiente. Use quando o usuário
  disser "por que a conversão caiu", "onde está o gargalo", "analisa
  esse funil/pipeline".
---

# analisar-conversao — Gargalo com hipótese, não só o número

Analisa um funil ou pipeline já estruturado e explica onde está a perda,
com hipótese e recomendação — nunca só o número frio.

## Quando usar

- Depois que um funil (`desenhar-funil`) ou pipeline
  (`configurar-pipeline`) já tem dado registrado.
- Quando o usuário pergunta por que a conversão caiu ou onde está o
  gargalo.

## Quando não usar

- Para estruturar um funil/pipeline do zero (isso é `desenhar-funil`/
  `configurar-pipeline`).

## Entradas

- Funil ou pipeline a analisar.
- Período de comparação (se houver).

## Dependências

- `schemas/funil.schema.json`, `schemas/pipeline.schema.json`
- `.claude/skills/projecoes` (quando a análise precisar de projeção)

## Contexto que deve ser carregado

- Dado histórico do funil/pipeline, quando existir.

---

## Workflow

### Passo 1 — Calcular (ver `fluxo.md`)

Volume por etapa, taxa por etapa, taxa total, tendência (comparado a
período anterior, se houver dado).

### Passo 2 — Identificar o gargalo

Etapa com maior perda relativa — não confundir maior perda absoluta
(pode ser natural, ex.: topo de funil) com maior perda proporcional.

### Passo 3 — Levantar hipótese

Hipótese sobre a causa (nunca apresentada como fato) — ex.: "a queda
entre proposta e fechamento pode estar ligada ao prazo de resposta,
mas isso precisa ser confirmado com mais dado".

### Passo 4 — Recomendar (ver `saidas.md`)

Recomendação de ação, com nível de confiança declarado e o que faltaria
para aumentar a confiança.

### Passo 5 — Validar (ver `validacao.md`)

Se não houver dado suficiente, dizer isso explicitamente em vez de
forçar uma conclusão.

---

## Saídas

Análise com volume, taxa, perda, gargalo identificado, hipótese,
recomendação e nível de confiança.

## Regras

- Nunca apresentar hipótese como fato.
- Sempre dizer quando o dado disponível é insuficiente para conclusão
  confiável.

## Critérios de qualidade

- Toda recomendação vem acompanhada do porquê e do nível de confiança.

## Critérios de validação

- Cálculo bate com o dado bruto do funil/pipeline analisado.

## Limitações

- Não corrige o funil/pipeline sozinha — recomenda, quem decide é o
  responsável pelo papel.

## Caminho de salvamento

`workspaces/<tipo>/<slug>/[projetos/<projeto>/]08-medicao/ANALISE-DE-CONVERSAO.md`

## Contrato de handoff

Recebe de `desenhar-funil`/`configurar-pipeline`. Encaminha para
`projecoes` quando a recomendação precisar de cenário futuro.

## Exemplos de gatilhos positivos

- "Por que a conversão caiu esse mês?"
- "Onde está o gargalo desse funil?"

## Exemplos de gatilhos negativos

- "Monta um funil novo" (é `desenhar-funil`)

Arquivos de apoio desta skill: `perguntas.txt`, `fluxo.md`, `saidas.md`,
`validacao.md`, `exemplos.md`.
