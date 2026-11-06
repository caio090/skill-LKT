---
name: precificacao
description: >
  Define preço de venda a partir do custo real (calcular-cmv), markup ou
  margem desejada, impostos e taxas — para qualquer segmento. Tem modo
  geral e é a base que a especialização food-service
  (precificacao-food-service) estende com taxas de delivery/marketplace.
  Use quando o usuário pedir "quanto devo cobrar por isso", "calcula meu
  markup", "esse preço é viável".
---

# precificacao — Formação de preço

## Quando usar

Definir ou revisar preço de venda com base em custo real, não em
"achismo" ou cópia de concorrente.

## Quando não usar

- Delivery/marketplace com taxas específicas de food-service → usar
  `precificacao-food-service` (estende esta skill).
- Apenas propor pacote/oferta comercial sem calcular custo →
  `criar-produto-e-oferta` (a decisão final de preço ainda passa por
  aqui pra validar viabilidade).

## Entradas

Custo total do produto/serviço (`calcular-cmv`), markup ou margem
desejada, impostos e taxas aplicáveis.

## Dependências

`calcular-cmv`, `schemas/financeiro/produto-precificacao.schema.json`.

## Contexto que deve ser carregado

Posicionamento do projeto (preço tem que ser coerente com o
posicionamento definido, não só com o custo).

---

## Workflow

1. Confirmar custo total (via `calcular-cmv` se ainda não calculado).
2. Definir markup desejado ou margem de contribuição desejada — os dois
   são formas diferentes de calcular, nunca confundir:
   ```
   preço com markup = custo total × (1 + markup desejado)
   preço com margem desejada = custo total ÷ (1 − margem desejada)
   ```
3. Somar impostos e taxas de cartão/plataforma aplicáveis.
4. Calcular preço sugerido e comparar com preço praticado (se houver).
5. Validar coerência com posicionamento (preço muito abaixo do
   posicionamento premium é inconsistente, e vice-versa).
6. Calcular ponto de equilíbrio com o preço proposto (via `calcular-cmv`).
7. Salvar em `<pasta-do-projeto-ativo>/03-financeiro/precificacao.md`.

## Saídas

Preço sugerido, markup aplicado, margem resultante, ponto de equilíbrio,
comparação com preço praticado (se houver).

## Caminho de salvamento

`<pasta-do-projeto-ativo>/03-financeiro/`.

## Regras

- Nunca precificar sem custo real confirmado — se não houver, calcular
  via `calcular-cmv` antes.
- Diferenciar sempre markup de margem — são cálculos diferentes.
- Nunca apresentar preço sugerido como definitivo sem o dono validar
  viabilidade operacional/comercial.

## Critérios de qualidade

Preço sugerido é rastreável ao custo real + markup/margem aplicados,
nunca um número solto.

## Critérios de validação

Recalcular o preço a partir dos componentes (custo, markup, impostos,
taxas) reproduz o valor sugerido.

## Limitações

Modo geral — taxas específicas de delivery/marketplace/combo são da
especialização food-service.

## Contrato de handoff

Encaminha pra `dre` (impacto no resultado) e `criar-produto-e-oferta`
(comunicação da oferta).

## Exemplos de gatilhos positivos

- "Quanto devo cobrar por essa consultoria"
- "Calcula o markup ideal desse produto"

## Exemplos de gatilhos negativos

- "Calcula o CMV desse produto" (é `calcular-cmv`, insumo desta skill)
