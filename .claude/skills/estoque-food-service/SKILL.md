---
name: estoque-food-service
description: >
  Controla estoque central e de cozinha separadamente: compras,
  entradas, transferências, consumo, perdas, validade, cortesia, refeição
  de equipe, correções, devoluções e ajustes. Calcula cobertura, ponto de
  reposição, itens críticos/parados e divergência de inventário. Use
  quando o usuário pedir "controla meu estoque", "quando devo comprar de
  novo", "meu inventário não bate".
---

# estoque-food-service — Estoque e inventário

## Quando usar

Controle de estoque de negócio de alimentação com mais de um local
(central + cozinha) ou necessidade de saber quando reabastecer.

## Quando não usar

Cálculo de custo de receita isolado → `ficha-tecnica`.

## Entradas

Movimentos de estoque (compra, transferência, consumo, perda, etc.).

## Dependências

`schemas/gestao-de-negocio/estoque.schema.json`,
`schemas/gestao-de-negocio/movimento.schema.json`.

## Contexto que deve ser carregado

Fichas técnicas (consumo esperado por venda).

---

## Workflow

1. Separar sempre **estoque central** de **estoque de cozinha** — nunca
   somar como se fossem um único local sem necessidade.
2. Registrar movimentos mínimos: compra, transferência de entrada,
   transferência de saída, consumo de produção, desperdício, vencimento,
   refeição de equipe, cortesia, correção, devolução ao fornecedor,
   ajuste manual.
3. **Transferência nunca cria saldo negativo silenciosamente** — se a
   transferência de saída for maior que o disponível, travar e reportar,
   não deixar passar.
4. Calcular:
   ```
   ponto de reposição = consumo médio diário × prazo de entrega + estoque de segurança
   cobertura em dias = estoque disponível ÷ consumo médio diário
   divergência = estoque físico − estoque esperado
   valor da divergência = divergência × custo unitário
   ```
5. Apontar item crítico (abaixo do ponto de reposição), item parado
   (sem movimento recente) e divergência relevante.
6. Medir precisão de estoque (quanto o físico bate com o esperado ao
   longo do tempo).
7. Salvar em `<pasta-do-projeto-ativo>/03-financeiro/estoque-<periodo>.md`.

## Saídas

Posição de estoque por local, itens críticos/parados, divergências,
cobertura e ponto de reposição por item.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/03-financeiro/`.

## Regras

- Estoque central e de cozinha sempre tratados separadamente.
- Transferência que criaria saldo negativo é bloqueada e reportada, não
  silenciada.
- Divergência sempre calculada com valor financeiro, não só quantidade.

## Critérios de qualidade

Todo item crítico/parado tem cálculo (ponto de reposição / última
movimentação) que sustenta a classificação.

## Critérios de validação

Soma dos movimentos do período reproduz a variação de estoque
observada (inicial + entradas − saídas = final).

## Limitações

Depende de registro consistente dos movimentos — sem isso, a
divergência pode refletir falha de registro, não perda real.

## Contrato de handoff

Encaminha pra `cmv-real-e-teorico` (lacuna de CMV) e
`rendimento-e-desperdicio` (causas de perda).

## Exemplos de gatilhos positivos

- "Quando devo comprar mais desse insumo"
- "Meu inventário físico não bate com o sistema"

## Exemplos de gatilhos negativos

- "Qual o custo dessa receita" (é `ficha-tecnica`)
