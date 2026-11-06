---
name: precificacao-food-service
description: >
  Especialização de precificacao para food service: forma preço a partir
  da ficha técnica, considerando embalagem, taxas de cartão/delivery/
  marketplace, comissão, descontos e perdas, comparando preço de balcão,
  retirada, delivery próprio e marketplace, e calculando preço mínimo
  sustentável. Use quando o usuário pedir "quanto cobrar nesse
  delivery", "meu preço no marketplace é viável", "calcula o preço desse
  combo".
---

# precificacao-food-service — Precificação por canal (food service)

Estende `precificacao` (base geral) com as taxas e canais específicos de
alimentação.

## Quando usar

Produto de food service vendido em mais de um canal (balcão, delivery
próprio, marketplace) com taxas diferentes por canal.

## Quando não usar

Precificação simples sem canal com taxa diferenciada → `precificacao`
(base) já resolve.

## Entradas

Ficha técnica (`ficha-tecnica`), taxas de cada canal, markup/margem
desejada.

## Dependências

`ficha-tecnica`, `precificacao`, `schemas/financeiro/produto-precificacao.schema.json`.

## Contexto que deve ser carregado

DNA do negócio (canais usados).

---

## Workflow

1. Partir do custo variável unitário:
   ```
   custo variável unitário = ingredientes + embalagem + taxas variáveis + comissão + outros custos variáveis
   ```
2. Calcular margem de contribuição por canal:
   ```
   margem de contribuição unitária = preço líquido de venda − custo variável unitário
   margem de contribuição percentual = margem de contribuição unitária ÷ preço líquido de venda × 100
   ```
3. Calcular preço líquido considerando desconto/cupom:
   ```
   preço líquido = preço anunciado − descontos − cupons assumidos pela loja
   ```
4. Calcular preço mínimo sustentável:
   ```
   preço mínimo sustentável = custo variável unitário ÷ (1 − percentual necessário para despesas, impostos e margem)
   ```
   Exigir que esse "percentual necessário" seja uma premissa explícita,
   nunca um número assumido sem declarar.
5. Comparar preço final entre balcão, retirada, delivery próprio e
   marketplace — mostrando onde a margem aperta mais.
6. Simular combo: soma dos custos variáveis dos itens do combo vs. preço
   do combo, calculando a margem resultante (nunca assumir que combo
   "sempre compensa").
7. Salvar em `<pasta-do-projeto-ativo>/03-financeiro/precificacao-canais.md`.

## Saídas

Preço por canal, margem de contribuição por canal, preço mínimo
sustentável, simulação de combo.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/03-financeiro/`.

## Regras

- Toda fórmula de preço mínimo exige premissa explícita do percentual
  necessário — nunca aplicar número "padrão de mercado" sem fonte.
- Comparação entre canais sempre mostra a taxa específica de cada um,
  não um número médio genérico.

## Critérios de qualidade

Preço de cada canal é rastreável às taxas específicas daquele canal.

## Critérios de validação

Recalcular o preço líquido a partir dos componentes reproduz o valor
apresentado.

## Limitações

Depende de taxas reais informadas por canal — sem isso, fica estimativa
marcada como tal.

## Contrato de handoff

Encaminha pra `engenharia-de-cardapio` (posição no cardápio) e
`dre`/`relatorio-financeiro` (impacto no resultado).

## Exemplos de gatilhos positivos

- "Quanto cobrar nesse marketplace considerando a comissão"
- "Calcula o preço desse combo"

## Exemplos de gatilhos negativos

- "Quanto custa produzir esse item" (é `ficha-tecnica`)
