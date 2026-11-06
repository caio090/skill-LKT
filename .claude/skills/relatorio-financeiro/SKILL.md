---
name: relatorio-financeiro
description: >
  Consolida DRE, fluxo de caixa, CMV, CAC/LTV e projeções num relatório
  executivo único, em linguagem simples, pro dono do negócio entender
  sem precisar ser contador. Use quando o usuário pedir "relatório
  financeiro do mês", "resume a situação financeira pro cliente".
---

# relatorio-financeiro — Relatório executivo financeiro

## Quando usar

Fechamento periódico (mensal/trimestral) ou entrega formal ao cliente
sobre a situação financeira.

## Quando não usar

Análise técnica detalhada isolada (isso são as skills individuais —
`dre`, `fluxo-de-caixa`, etc.). Esta skill consolida, não substitui.

## Entradas

Saídas de `dre`, `fluxo-de-caixa`, `calcular-cmv`, `cac-e-ltv`,
`projecao-financeira` (as que existirem para o período).

## Dependências

As skills financeiras acima já executadas para o período.

## Contexto que deve ser carregado

Preferências de tom (`_memoria/preferencias.md`) e metas registradas
(`PROJETO.md`/`_memoria/metricas.md`).

---

## Workflow

1. Reunir os resultados já calculados do período (não recalcular do
   zero se já existir).
2. Resumo executivo (3-5 frases): o que mais importa esse período.
3. Seção por indicador (receita, custo, margem, caixa, CAC/LTV se
   aplicável) — cada uma com número + explicação, nunca só a tabela.
4. Comparação com período anterior e com meta (se houver).
5. Alertas (o que preocupa) e oportunidades (o que está indo bem).
6. Recomendações concretas (3-5 itens, com prioridade).
7. Encaminhar pra `texto-natural-pt-br` antes de entregar ao cliente.
8. Salvar em `<pasta-do-projeto-ativo>/09-relatorios/`.

## Saídas

Relatório único em `09-relatorios/relatorio-financeiro-<periodo>.md`.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/09-relatorios/`.

## Regras

- Nunca recalcular métricas que outra skill já calculou — consolidar,
  não duplicar cálculo.
- Diferenciar sempre receita, faturamento, lucro, margem.
- Nunca apresentar projeção como fato consumado.

## Critérios de qualidade

Dono do negócio (não contador) consegue entender o relatório sem
precisar de tradução adicional.

## Critérios de validação

Todo número do relatório é rastreável à skill que o calculou
originalmente.

## Limitações

Depende das skills financeiras individuais já terem rodado para o
período — não é fonte primária de cálculo.

## Contrato de handoff

`texto-natural-pt-br` (acabamento) antes de entregar. Pode encadear com
`criar-pdf`/`criar-apresentacao` se o formato final não for markdown.

## Exemplos de gatilhos positivos

- "Monta o relatório financeiro do mês pro cliente"
- "Resume a situação financeira desse trimestre"

## Exemplos de gatilhos negativos

- "Calcula meu CMV" (é a skill individual `calcular-cmv`)
