---
name: relatorio-executivo
description: >
  Consolida financeiro, marketing, comercial e operação de um
  cliente/projeto num único relatório executivo de alto nível (visão de
  dono/board, não detalhe técnico de cada área). Use quando o usuário
  pedir "relatório executivo completo desse cliente", "resume tudo pro
  board".
---

# relatorio-executivo — Relatório executivo cross-área

## Quando usar

Reporte de alto nível que cruza mais de uma área (não é só financeiro
nem só marketing).

## Quando não usar

Relatório de uma área específica → `relatorio-financeiro` ou
`relatorio-de-marketing` isolados.

## Entradas

Saídas de `relatorio-financeiro`, `relatorio-de-marketing`,
`funil-de-vendas`, `gestao-de-negocio` (as que existirem pro período).

## Dependências

As skills de relatório de cada área.

## Contexto que deve ser carregado

`PROJETO.md` (objetivo, indicador de sucesso do projeto).

---

## Workflow

1. Reunir os relatórios de área já existentes pro período (não
   recalcular).
2. Resumo executivo (3-5 frases): o que mais importa, cruzando todas as
   áreas.
3. Seção curta por área (financeiro, marketing, comercial, operação) —
   só o essencial, sem repetir o detalhe técnico de cada relatório de
   origem.
4. Comparar com o indicador de sucesso definido em `PROJETO.md`.
5. 3-5 recomendações priorizadas, cruzando áreas se necessário.
6. Encaminhar pra `texto-natural-pt-br`.
7. Salvar em `<pasta-do-projeto-ativo>/09-relatorios/executivo-<periodo>.md`.

## Saídas

Relatório único, de leitura rápida (2-3 minutos).

## Caminho de salvamento

`<pasta-do-projeto-ativo>/09-relatorios/`.

## Regras

- Não recalcular o que os relatórios de área já calcularam.
- Foco em decisão, não em detalhe técnico — se o leitor quiser
  detalhe, aponta pro relatório de área específico.

## Critérios de qualidade

Leitura em poucos minutos entrega visão completa do projeto.

## Critérios de validação

Todo número citado é rastreável ao relatório de área de origem.

## Limitações

Depende dos relatórios de área terem rodado no período.

## Contrato de handoff

`texto-natural-pt-br`, `anti-chat` (quality gate final), `plano-estrategico`
(se recomendação exigir replanejamento).

## Exemplos de gatilhos positivos

- "Relatório executivo completo desse cliente esse trimestre"
- "Resume tudo pro board"

## Exemplos de gatilhos negativos

- "Só o relatório financeiro" (é `relatorio-financeiro`)
