---
name: dre
description: >
  Monta e explica o DRE (Demonstrativo de Resultado) de um período:
  receita, deduções, CMV/custo de serviço, margem bruta, despesas,
  resultado operacional e líquido — e compara previsto versus realizado.
  Use quando o usuário pedir "monta o DRE", "qual foi meu lucro esse
  mês", "previsto versus realizado".
---

# dre — Demonstrativo de Resultado

## Quando usar

Fechamento de período (mês, trimestre) pra entender lucro real, não só
caixa.

## Quando não usar

Análise de caixa/capital de giro (regime de caixa) → `fluxo-de-caixa`.

## Entradas

Transações normalizadas por competência.

## Dependências

`calcular-cmv` (custo do período), `schemas/financeiro/transacao.schema.json`.

## Contexto que deve ser carregado

DRE de períodos anteriores, se existirem, para comparação.

---

## Workflow

1. Agrupar por competência (regime de competência, não caixa).
2. Estrutura mínima: receita bruta → deduções/impostos → receita
   líquida → CMV/custo de serviço → margem bruta → despesas operacionais
   → resultado operacional → outras receitas/despesas → resultado
   líquido.
3. **Previsto vs. realizado:** se houver meta/orçamento do período
   (`_memoria/metricas.md` ou `PROJETO.md`), comparar e explicar o
   desvio — nunca só mostrar os dois números lado a lado sem
   interpretar.
4. Comparar com o período anterior (evolução do próprio negócio, não
   benchmark externo sem fonte).
5. Explicar em linguagem simples: margem melhorou/piorou, por quê,
   o que isso significa pra próxima decisão.
6. Salvar em `<pasta-do-projeto-ativo>/03-financeiro/dre-<periodo>.md`.

## Saídas

DRE estruturado + comparação previsto/realizado + comparação com período
anterior + leitura em linguagem simples.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/03-financeiro/`.

## Regras

- Regime de competência, não confundir com caixa.
- Toda meta usada na comparação previsto/realizado é citada com a fonte
  (onde foi definida).
- Nunca comparar com "média de mercado" sem fonte, segmento, região e
  data.

## Critérios de qualidade

DRE fecha matematicamente (receita líquida − CMV = margem bruta, etc.)
e todo desvio relevante é explicado, não só apontado.

## Critérios de validação

Resultado líquido do DRE bate com a soma das transações de origem do
período.

## Limitações

Depende de `calcular-cmv` estar correto para a linha de CMV ser
confiável.

## Contrato de handoff

Encaminha pra `projecao-financeira` (próximos períodos) e
`relatorio-financeiro` (versão executiva pro cliente).

## Exemplos de gatilhos positivos

- "Monta o DRE de julho"
- "Qual foi meu lucro esse trimestre comparado com o mês passado"

## Exemplos de gatilhos negativos

- "Vou ter caixa pra pagar isso semana que vem" (é `fluxo-de-caixa`)
