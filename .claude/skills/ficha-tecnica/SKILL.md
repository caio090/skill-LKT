---
name: ficha-tecnica
description: >
  Cria, revisa e atualiza a ficha técnica de um produto de food service:
  ingredientes, quantidades, unidades, peso bruto/líquido/final,
  rendimento, porção, embalagem, mão de obra direta quando aplicável, e
  custo total e por unidade, com controle de versão e data. Use quando o
  usuário pedir "preencher ficha técnica", "calcular custo do lanche",
  "quanto custa produzir", "montar ficha do produto".
---

# ficha-tecnica — Ficha técnica de produto (food service)

## Quando usar

Todo produto de cardápio que precisa de custo confiável — base pra
`precificacao-food-service`, `cmv-real-e-teorico` e
`engenharia-de-cardapio`.

## Quando não usar

Produto sem componente físico/receita (ex.: serviço puro) →
`calcular-cmv` (modo custo interno) no lugar.

## Entradas

Receita/ingredientes do produto, pesos, rendimento, embalagem.

## Dependências

`schemas/gestao-de-negocio/ficha-tecnica.schema.json`,
`schemas/gestao-de-negocio/ingrediente.schema.json`.

## Contexto que deve ser carregado

`dna-do-negocio` (produto-herói, produtos principais).

---

## Workflow

1. Identificar o produto e a que categoria pertence (herói, entrada,
   margem, sazonal — conforme `dna-do-negocio`).
2. Listar ingredientes com quantidade e unidade — nunca misturar
   unidades sem conversão explícita (g, ml, unidade).
3. Registrar **peso bruto** (como comprado), **peso líquido** (após
   limpeza/corte) e **peso final** (após cocção/preparo) separadamente —
   nunca tratar como o mesmo número.
4. Calcular rendimento:
   ```
   rendimento aproveitável = peso líquido ÷ peso bruto
   perda no pré-preparo = peso bruto − peso líquido
   percentual de perda = perda ÷ peso bruto × 100
   rendimento de cocção = peso final preparado ÷ peso líquido antes da cocção
   ```
5. Calcular custo líquido do insumo:
   ```
   custo líquido do insumo = custo de compra ÷ quantidade aproveitável
   ```
6. Definir porcionamento:
   ```
   número de porções = rendimento total ÷ peso padrão da porção
   custo por porção = custo total da receita ÷ número de porções
   ```
7. Somar embalagem e mão de obra direta (quando aplicável) ao custo por
   porção/unidade.
8. Registrar versão e data — toda atualização de preço de insumo ou
   receita gera nova versão, não sobrescreve sem histórico.
9. Tratar divisão por zero e dado ausente explicitamente (nunca deixar
   erro silencioso — reportar "rendimento não pode ser calculado, peso
   líquido ausente").
10. Salvar em `workspaces/clientes/<cliente>/03-financeiro/fichas-tecnicas/<produto>.md`
    (ou `.json` seguindo o schema).

## Saídas

Ficha técnica completa com custo por porção/unidade, versionada.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/03-financeiro/fichas-tecnicas/`.

## Regras

- Nunca confundir peso bruto, líquido e final.
- Nunca dividir por zero silenciosamente — sempre reportar o dado
  ausente.
- Toda ficha tem versão e data — histórico preservado, nunca
  sobrescrito sem registro anterior.

## Critérios de qualidade

Custo por porção é rastreável a cada insumo e seu rendimento
individual.

## Critérios de validação

Recalcular o custo total a partir dos insumos individuais reproduz o
valor da ficha.

## Limitações

Depende de dado real de compra/rendimento — sem isso, fica estimativa
marcada como tal.

## Contrato de handoff

Encaminha pra `rendimento-e-desperdicio` (perdas), `cmv-real-e-teorico`
(comparação), `precificacao-food-service` (preço final).

## Exemplos de gatilhos positivos

- "Monta a ficha técnica desse lanche"
- "Quanto custa produzir esse prato"

## Exemplos de gatilhos negativos

- "Qual o preço final de venda" (é `precificacao-food-service`, que usa
  esta ficha como insumo)
