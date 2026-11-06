---
name: analisar-promocao-cupom
description: >
  Analisa se uma promoção/cupom vale a pena: quem paga o desconto (loja,
  plataforma ou compartilhado), margem antes e depois, volume necessário
  pra compensar, novos clientes vs. recompra vs. CAC. Recomenda manter,
  limitar, alterar ou encerrar. Use quando o usuário pedir "esse cupom
  vale a pena", "devo continuar com esse desconto da plataforma".
---

# analisar-promocao-cupom — Viabilidade de promoção/cupom

## Quando usar

Antes de lançar uma promoção/cupom, ou para revisar uma já ativa.

## Quando não usar

Análise de ticket médio sem desconto envolvido → `aumento-de-ticket`.

## Entradas

Preço cheio, desconto, quem assume (loja/plataforma/compartilhado),
volume de vendas com e sem a promoção.

## Dependências

`cac-e-ltv` (CAC de clientes trazidos pela promoção),
`precificacao-food-service` (margem por canal).

## Contexto que deve ser carregado

Margem de contribuição dos produtos envolvidos na promoção.

---

## Workflow

1. Separar componentes: preço cheio, desconto, preço líquido, custo do
   produto, taxa do canal, comissão, cupom, subsídio (quem de fato
   arca com o desconto — a loja, a plataforma, ou os dois).
2. Calcular margem final:
   ```
   margem final = preço líquido − custo do produto − taxa do canal − comissão
   ```
3. Calcular volume necessário pra compensar o desconto (quantas vendas
   extras a promoção precisa gerar pra empatar com a margem sem
   promoção).
4. Medir (com dado real, se disponível): quantos clientes novos a
   promoção trouxe, quantos são recompra, impacto no ticket médio,
   impacto no caixa.
5. Cruzar com CAC — se a promoção está sendo usada como aquisição,
   comparar custo do desconto com CAC de outros canais.
6. Recomendar: manter, limitar (só pra cliente novo, só em horário
   específico), alterar (mudar percentual/condição) ou encerrar — com
   justificativa numérica.
7. Salvar em `<pasta-do-projeto-ativo>/04-marketing/promocao-<nome>.md`.

## Saídas

Análise de margem antes/depois, volume necessário, recomendação
justificada.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/04-marketing/`.

## Regras

- Sempre identificar quem paga o desconto de fato — nunca tratar
  "desconto" como um bloco único sem separar loja vs. plataforma.
- Recomendação sempre justificada com número, nunca só opinião.

## Critérios de qualidade

Margem final calculada reflete todos os componentes (taxa, comissão,
desconto) do canal específico.

## Critérios de validação

Volume necessário pra compensar é recalculável a partir da margem
antes/depois informada.

## Limitações

Depende de dado real de volume com/sem promoção — sem isso, a
recomendação é qualitativa e deve dizer isso.

## Contrato de handoff

Encaminha pra `cac-e-ltv` (comparação de aquisição) e
`plano-estrategico` (decisão final).

## Exemplos de gatilhos positivos

- "Esse cupom da plataforma vale a pena"
- "Devo continuar com esse desconto de terça-feira"

## Exemplos de gatilhos negativos

- "Como aumentar meu ticket sem desconto" (é `aumento-de-ticket`)
