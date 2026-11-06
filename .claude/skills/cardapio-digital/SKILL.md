---
name: cardapio-digital
description: >
  Audita o cardápio digital (categorias, produtos, adicionais, combos,
  fotos, descrições, disponibilidade, horários, taxas, retirada, entrega,
  pagamento, cupons) e cruza com produtos parados/mais vendidos, ticket,
  horário de pico, abandono e recompra. Prepara integração futura via
  adaptador genérico (não exige nenhuma plataforma específica). Use
  quando o usuário pedir "revisa meu cardápio digital", "meu app de
  delivery está bem configurado".
---

# cardapio-digital — Auditoria e contrato de dados do cardápio digital

## Quando usar

Cardápio já publicado numa plataforma (própria ou de terceiro) que
precisa de revisão ou análise de desempenho.

## Quando não usar

Definir o que vai no cardápio (isso é `engenharia-de-cardapio`) — esta
skill audita a apresentação/dados de um cardápio já existente.

## Entradas

Export ou acesso de leitura ao cardápio digital atual (nome de
plataforma não importa — ver contrato de dados abaixo).

## Dependências

`schemas/gestao-de-negocio/pedido.schema.json` e schemas relacionados
(item_pedido, produto, categoria, adicional, combo, cliente, cupom,
pagamento, canal, loja, horario, status).

## Contexto que deve ser carregado

`engenharia-de-cardapio` (se já existir análise de produtos).

---

## Workflow

1. Auditar estrutura: categorias fazem sentido, produtos com foto e
   descrição completas, adicionais/combos configurados corretamente,
   disponibilidade e horário batem com a operação real.
2. Checar taxas, opções de retirada/entrega e formas de pagamento
   configuradas.
3. Cruzar com desempenho: produtos parados, produtos mais vendidos,
   ticket médio, horário de pico, taxa de abandono de carrinho (se
   disponível), recompra.
4. Identificar atrito: cardápio com escolha confusa, produto sem foto,
   descrição vaga, categoria mal ordenada.
5. Recomendar ajustes concretos (reordenar categoria, completar foto,
   simplificar adicional confuso).
6. Salvar em `<pasta-do-projeto-ativo>/04-marketing/cardapio-digital.md`.

## Contrato de dados (adaptador genérico)

Esta skill não depende de nenhuma plataforma específica (não exige
OlaClick nem qualquer outra). Qualquer integração futura deve traduzir
os dados da plataforma real para este contrato genérico antes de a
skill processar:

`pedido`, `item_pedido`, `produto`, `categoria`, `adicional`, `combo`,
`cliente`, `cupom`, `pagamento`, `canal`, `loja`, `horario`, `status`.

Ver `schemas/gestao-de-negocio/` para o formato de cada entidade. Uma
integração nova = um adaptador novo que popula esse contrato — a skill
em si nunca muda para se adaptar a uma plataforma específica.

## Saídas

Auditoria estrutural + cruzamento com desempenho + recomendações.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/04-marketing/`.

## Regras

- Nunca exigir uma plataforma específica — sempre passar pelo contrato
  de dados genérico.
- Recomendação sempre concreta (o que mudar, onde), nunca genérica
  ("melhore as fotos").

## Critérios de qualidade

Toda recomendação aponta o item/categoria específico afetado.

## Critérios de validação

Dados cruzados (produto parado, horário de pico) são rastreáveis ao
export/fonte original.

## Limitações

Não implementa a mudança na plataforma real — só audita e recomenda; a
aplicação é manual ou via integração futura (`integrar-api`).

## Contrato de handoff

Encaminha pra `engenharia-de-cardapio` (decisão de produto) e
`integrar-api` (quando a integração automática for implementada).

## Exemplos de gatilhos positivos

- "Revisa meu cardápio no aplicativo de delivery"
- "Meu cardápio digital está bem configurado?"

## Exemplos de gatilhos negativos

- "Quais produtos devo tirar" (é `engenharia-de-cardapio`, decisão de
  conteúdo, não de apresentação digital)
