---
name: relatorio-de-marketing
description: >
  Consolida desempenho de marketing do período (conteúdo, SEO, ads,
  campanhas) num relatório executivo único, cruzando com objetivo da
  estratégia. Use quando o usuário pedir "relatório de marketing do
  mês", "como está indo o marketing desse cliente".
---

# relatorio-de-marketing — Relatório executivo de marketing

## Quando usar

Fechamento periódico consolidando conteúdo + ads + SEO, não só um canal.

## Quando não usar

Relatório de um canal isolado → `relatorio-ads` (só ads).

## Entradas

Saídas de `relatorio-ads`, `seo` (checklist de monitoramento),
desempenho de conteúdo (alcance, engajamento, se disponível).

## Dependências

`relatorio-ads`, `estrategia-de-marketing` (pra comparar com objetivo).

## Contexto que deve ser carregado

Estratégia de marketing e metas do período.

---

## Workflow

1. Reunir resultados já calculados (não recalcular).
2. Resumo executivo: o que mais importa esse período.
3. Por canal: o que foi feito, resultado, comparação com período
   anterior e com meta.
4. Cruzar com objetivo da `estrategia-de-marketing` — está no caminho
   ou não.
5. Recomendações pra próximo período.
6. Encaminhar pra `texto-natural-pt-br` antes de entregar.
7. Salvar em `<pasta-do-projeto-ativo>/09-relatorios/marketing-<periodo>.md`.

## Saídas

Relatório consolidado.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/09-relatorios/`.

## Regras

- Não recalcular o que outra skill já calculou — consolidar.
- Toda comparação usa dado real do próprio histórico, não benchmark
  externo sem fonte.

## Critérios de qualidade

Relatório conecta resultado com objetivo estratégico, não só lista
número.

## Critérios de validação

Todo número é rastreável à skill/fonte que o gerou.

## Limitações

Depende das skills de canal terem rodado no período.

## Contrato de handoff

`texto-natural-pt-br`, `plano-estrategico` (se recomendação exigir
replanejar).

## Exemplos de gatilhos positivos

- "Relatório de marketing do mês pro cliente"
- "Como está indo o marketing desse negócio"

## Exemplos de gatilhos negativos

- "Só o relatório de ads" (é `relatorio-ads`)
