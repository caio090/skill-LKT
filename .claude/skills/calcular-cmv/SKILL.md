---
name: calcular-cmv
description: >
  Calcula CMV (custo de mercadoria/serviço vendido), custo interno,
  margem de contribuição, estoque e desperdício de um negócio, a partir
  de ficha técnica ou dado de compra/consumo. Tem modo geral (qualquer
  segmento) e é a base que a especialização food-service
  (cmv-real-e-teorico, estoque-food-service) estende. Use quando o
  usuário pedir "calcula meu CMV", "qual minha margem de contribuição",
  "quanto custa esse produto/serviço de verdade".
---

# calcular-cmv — CMV, custo interno, margem de contribuição, estoque e desperdício

Skill principal do custo direto — cobre os conceitos gerais; segmentos
com necessidade mais profunda (ex.: alimentação) usam a especialização
em `catalogo/modulos/gestao-de-negocio/food-service/` sem duplicar esta lógica
base.

## Quando usar

Precificação, DRE, ou qualquer decisão que dependa de saber o custo real
de produzir/entregar o que o negócio vende.

## Quando não usar

Negócio de alimentação com ficha técnica detalhada, rendimento de
insumo e comparação CMV real vs. teórico → usar a especialização
`cmv-real-e-teorico` (que reaproveita esta skill como base, não a
substitui).

## Entradas

Ficha técnica ou lista de insumos/custos diretos do produto/serviço.

## Dependências

`schemas/financeiro/produto-precificacao.schema.json`.

## Contexto que deve ser carregado

Custos fixos do negócio (`_memoria/empresa.md` ou financeiro do
cliente), se for calcular rateio.

---

## Workflow (modos)

### Modo: CMV simples

```
CMV = custo direto do que foi vendido no período
```
Usar quando não há estoque formal — custo direto por venda.

### Modo: Custo interno / custo de serviço

Para negócios de serviço: mão de obra direta, materiais consumidos,
deslocamento — o equivalente ao CMV pra quem não vende produto físico.

### Modo: Margem de contribuição

```
margem de contribuição unitária = preço de venda − custo variável unitário
margem de contribuição percentual = margem de contribuição unitária ÷ preço de venda × 100
```
Explicar: essa é a margem que sobra pra pagar custo fixo e gerar lucro —
não confundir com margem bruta do DRE (que é sobre o total, não por
unidade).

### Modo: Ponto de equilíbrio

```
ponto de equilíbrio (unidades) = custo fixo total ÷ margem de contribuição unitária
ponto de equilíbrio (receita) = custo fixo total ÷ (margem de contribuição percentual ÷ 100)
```

### Modo: Estoque e desperdício (visão geral)

Perda = diferença entre o que devia ter sido consumido (teórico) e o que
foi de fato consumido/perdido. Pedir dado real de perda antes de estimar
— nunca inventar percentual de desperdício sem fonte.

## Saídas

`<pasta-do-projeto-ativo>/03-financeiro/cmv.md` com o(s) modo(s) usados,
valores e explicação em linguagem simples.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/03-financeiro/`.

## Regras

- Nunca inventar custo/perda sem dado real — marcar como estimativa e
  pedir confirmação.
- Diferenciar sempre margem de contribuição de margem bruta/líquida.
- Rateio de custo fixo explicado (como foi dividido entre produtos),
  nunca aplicado silenciosamente.

## Critérios de qualidade

Toda margem calculada explica o que a diferencia de outras margens
(bruta, líquida, contribuição) pra não confundir o dono do negócio.

## Critérios de validação

Ponto de equilíbrio recalculado bate com margem de contribuição e custo
fixo informados.

## Limitações

Modo geral — não cobre rendimento de insumo, peso bruto/líquido nem
comparação real vs. teórico em profundidade (isso é a especialização
food-service).

## Contrato de handoff

Encaminha pra `precificacao` (definir preço final) e `dre` (linha de
CMV do resultado). Em food-service, a especialização
`cmv-real-e-teorico` chama esta skill como base.

## Exemplos de gatilhos positivos

- "Calcula meu CMV desse mês"
- "Qual a margem de contribuição desse produto"
- "Qual meu ponto de equilíbrio"

## Exemplos de gatilhos negativos

- "Quanto devo cobrar por esse produto" (é `precificacao`, que usa o CMV
  como insumo)
