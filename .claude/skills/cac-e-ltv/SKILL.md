---
name: cac-e-ltv
description: >
  Calcula e explica CAC, LTV, relação LTV/CAC, payback, ROI e ROAS —
  as métricas de retorno sobre investimento em aquisição/retenção de
  cliente. Use quando o usuário pedir "qual meu CAC", "vale a pena esse
  investimento em ads", "meu LTV compensa o CAC", "qual o ROI dessa
  campanha".
---

# cac-e-ltv — Economia do cliente e retorno de investimento

## Quando usar

Avaliar se o custo de conseguir/manter cliente compensa o valor que ele
gera, ou se um investimento (ads, campanha, expansão) se pagou.

## Quando não usar

Análise de custo de produto/serviço em si → `calcular-cmv`/`precificacao`.

## Entradas

Investimento em aquisição (período), número de clientes novos, receita
por cliente ao longo do tempo, custo variável associado a atender esse
cliente.

## Dependências

`fluxo-de-caixa`/`dre` (para dados reais de receita e investimento).

## Contexto que deve ser carregado

Histórico de CAC/LTV anterior, se existir, para comparação de evolução.

---

## Workflow

1. **CAC:**
   ```
   CAC = investimento total em aquisição ÷ número de clientes novos no período
   ```
2. **LTV:**
   ```
   LTV = ticket médio × frequência de compra × tempo médio de relacionamento × margem de contribuição %
   ```
   Deixar claro que LTV é projeção, baseada em comportamento passado —
   nunca apresentar como garantia futura.
3. **Relação LTV/CAC:** calcular e explicar o que o número significa (
   relação abaixo de 3x costuma indicar aquisição cara demais pro valor
   gerado — mas isso é referência, não regra fixa; comparar com o
   histórico do próprio negócio quando possível).
4. **Payback:** em quanto tempo o CAC se paga com a margem gerada pelo
   cliente.
5. **ROI:**
   ```
   ROI = (retorno − investimento) ÷ investimento × 100
   ```
6. **ROAS:**
   ```
   ROAS = receita gerada ÷ valor investido em mídia
   ```
   Diferenciar de ROI (ROAS é receita bruta gerada por mídia; ROI
   considera custo/lucro real).
7. Salvar em `<pasta-do-projeto-ativo>/03-financeiro/cac-ltv.md`.

## Saídas

CAC, LTV, relação LTV/CAC, payback, ROI, ROAS — cada um com explicação
em linguagem simples do que significa pra decisão.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/03-financeiro/`.

## Regras

- LTV é sempre projeção — nunca apresentar como número garantido.
- Não usar limiar universal ("LTV/CAC bom é 3x") como regra fixa sem
  contextualizar pro segmento/negócio específico.
- ROI e ROAS nunca confundidos — são cálculos diferentes.

## Critérios de qualidade

Toda métrica vem com a fórmula explícita usada e as premissas de
cálculo (período, o que entrou como custo/receita).

## Critérios de validação

CAC e LTV recalculados a partir dos dados brutos batem com o valor
apresentado.

## Limitações

Qualidade do resultado depende da qualidade do dado de entrada
(investimento real, clientes novos reais) — se o dado for incompleto,
dizer isso.

## Contrato de handoff

Encaminha pra `relatorio-financeiro` (versão executiva) e
`plano-estrategico` (decisão de continuar/ajustar investimento).

## Exemplos de gatilhos positivos

- "Qual meu CAC esse mês"
- "Esse investimento em ads valeu a pena"

## Exemplos de gatilhos negativos

- "Quanto custa produzir esse item" (é `calcular-cmv`)
