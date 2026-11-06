---
name: projecao-financeira
description: >
  Projeta cenários financeiros futuros (conservador, provável, otimista)
  para decisões de investimento, novo produto, reajuste de preço,
  contratação, expansão — sempre com premissas explícitas, fonte e
  incerteza declarada. Use quando o usuário pedir "projeta meu
  faturamento", "vale a pena investir nisso", "simula esse cenário".
---

# projecao-financeira — Cenários e viabilidade

## Quando usar

Qualquer decisão financeira que dependa de estimar o futuro: novo
produto, reajuste, contratação, expansão, novo canal.

## Quando não usar

Análise do que já aconteceu (isso é `dre`/`fluxo-de-caixa`).

## Entradas

Premissa da simulação (o que está mudando), dados históricos reais como
base (`dre`, `fluxo-de-caixa`).

## Dependências

`dre`, `fluxo-de-caixa`, `cac-e-ltv`, `calcular-cmv` (conforme o tipo de
projeção).

## Contexto que deve ser carregado

Histórico financeiro real do projeto/cliente ativo.

---

## Workflow

1. Definir claramente o que está sendo simulado (reajuste de preço,
   novo produto, aumento de ticket, redução de custo, nova unidade,
   contratação, marketing, expansão, etc.).
2. Levantar premissas explícitas — nunca simular sem declarar o que está
   sendo assumido (ex.: "assumindo que o volume de vendas se mantém").
3. Construir 3 cenários obrigatórios:
   - **Conservador:** premissas mais cautelosas.
   - **Provável:** premissas mais realistas dado o histórico.
   - **Otimista:** premissas mais favoráveis, mas ainda plausíveis.
4. Escolher horizonte(s) relevante(s) ao pedido: 30 dias, 90 dias, 6
   meses, 12 meses, 24 meses quando fizer sentido.
5. Mostrar o impacto em receita, custo e resultado em cada cenário.
6. Listar riscos e incertezas explicitamente — o que pode fazer a
   projeção não se confirmar.
7. **Nunca tratar a projeção como promessa ou garantia.**
8. Salvar em `<pasta-do-projeto-ativo>/03-financeiro/projecao-<tema>.md`.

## Saídas

3 cenários com premissas, resultado projetado, riscos e incertezas.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/03-financeiro/`.

## Regras

- Sempre 3 cenários (conservador, provável, otimista) — nunca um número
  único apresentado como "a" projeção.
- Toda premissa é explícita e rastreável à fonte (histórico real ou
  suposição declarada como tal).
- Nunca apresentar projeção como certeza.

## Critérios de qualidade

Cada cenário é internamente consistente (as premissas batem com o
resultado calculado).

## Critérios de validação

Cenário provável é ancorado em dado histórico real do próprio negócio,
não em benchmark externo sem fonte.

## Limitações

Qualidade da projeção depende da qualidade do histórico disponível —
negócio sem histórico tem projeção mais incerta, e isso deve ser dito.

## Contrato de handoff

Encaminha pra `plano-estrategico` (decisão) e `relatorio-financeiro`
(comunicação ao cliente).

## Exemplos de gatilhos positivos

- "Projeta meu faturamento pros próximos 6 meses"
- "Vale a pena contratar mais uma pessoa"

## Exemplos de gatilhos negativos

- "Qual foi meu resultado esse mês" (é `dre`, fato passado, não projeção)
