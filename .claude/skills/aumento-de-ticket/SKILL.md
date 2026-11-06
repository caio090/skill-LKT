---
name: aumento-de-ticket
description: >
  Analisa ticket médio e mapeia oportunidades reais de aumento (combo,
  adicional, tamanho, sobremesa, bebida, oferta de volume, sugestão de
  atendimento, posição no cardápio, pós-compra, recompra), calculando
  impacto e risco de canibalização — não só sugerindo ideias. Use quando
  o usuário pedir "como aumentar meu ticket médio", "vale a pena um
  combo novo".
---

# aumento-de-ticket — Aumento de ticket médio

## Quando usar

Depois de `engenharia-de-cardapio` apontar oportunidade, ou quando o
dono quiser aumentar receita sem necessariamente trazer cliente novo.

## Quando não usar

Aquisição de cliente novo (isso é marketing/tráfego pago, não ticket).

## Entradas

Ticket médio atual, pedidos por período, produtos candidatos a
complemento/combo.

## Dependências

`engenharia-de-cardapio`, `ficha-tecnica` (custo dos itens do combo).

## Contexto que deve ser carregado

Dados de venda do período.

---

## Workflow

1. Calcular ticket médio atual:
   ```
   ticket médio = faturamento ÷ número de pedidos
   ```
2. Mapear oportunidades reais: complemento natural (o que combina com o
   produto-herói), combo, adicional, tamanho maior, sobremesa, bebida,
   oferta de volume, sugestão no atendimento, reposicionamento no
   cardápio, pós-compra (recompra).
3. Pra cada oportunidade, calcular impacto:
   ```
   incremento de ticket = ticket projetado − ticket atual
   receita incremental = incremento de ticket × número projetado de pedidos
   ```
4. Avaliar **risco de canibalização** — o combo/adicional pode reduzir a
   venda de outro item já rentável? Declarar isso explicitamente, não
   ignorar.
5. Priorizar as oportunidades com maior impacto e menor risco.
6. Salvar em `<pasta-do-projeto-ativo>/04-marketing/aumento-ticket.md`.

## Saídas

Ticket médio atual, oportunidades priorizadas com impacto calculado e
risco de canibalização declarado.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/04-marketing/`.

## Regras

- Toda sugestão vem com cálculo de impacto — nunca só ideia solta.
- Risco de canibalização sempre avaliado e declarado, nunca omitido.
- Premissas de projeção explícitas (quantos pedidos aceitariam a
  oferta, de onde veio essa suposição).

## Critérios de qualidade

Cada oportunidade prioriza tem impacto financeiro estimado e
comparável entre si.

## Critérios de validação

Receita incremental projetada é recalculável a partir do incremento de
ticket e volume projetado informados.

## Limitações

Projeção depende de premissa de adesão à oferta — sem teste real, é
estimativa (ver `teste-de-produto`, no workflow
`produto-e-engenharia-de-cardapio`).

## Contrato de handoff

Encaminha pra `analisar-promocao-cupom` (se a oferta envolver desconto)
e `projecao-financeira` (impacto de médio prazo).

## Exemplos de gatilhos positivos

- "Como aumentar meu ticket médio"
- "Vale a pena criar um combo novo"

## Exemplos de gatilhos negativos

- "Como trazer mais clientes novos" (é marketing/aquisição, não ticket)
