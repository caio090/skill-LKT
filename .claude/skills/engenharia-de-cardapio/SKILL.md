---
name: engenharia-de-cardapio
description: >
  Analisa popularidade, margem de contribuição, faturamento, quantidade
  vendida e posição no cardápio (físico e digital) de cada produto,
  separando o que vende muito, dá margem, é produto de entrada/imagem/
  combo, ou está parado — e recomenda manter, destacar, reposicionar,
  reajustar, combinar, simplificar, testar ou retirar. Use quando o
  usuário pedir "quais produtos devo tirar do cardápio", "meu cardápio
  está funcionando bem", "reorganiza meu menu".
---

# engenharia-de-cardapio — Engenharia de cardápio

## Quando usar

Revisão periódica de cardápio, ou quando o dono suspeitar que produtos
parados/de baixa margem estão ocupando espaço que deveria ir pra
produtos melhores.

## Quando não usar

Cálculo de custo/preço de um produto isolado → `ficha-tecnica`/
`precificacao-food-service` primeiro (esta skill precisa desses dados
prontos pra cruzar com venda).

## Entradas

Vendas por produto (quantidade, faturamento), margem de contribuição de
cada produto (`calcular-cmv`/`ficha-tecnica`), estrutura atual do
cardápio (ordem, destaque, fotos, descrições).

## Dependências

`ficha-tecnica`, `calcular-cmv`, `cardapio-digital` (se o cardápio for
digital).

## Contexto que deve ser carregado

`dna-do-negocio` (produto-herói, produtos de entrada/margem/sazonais já
mapeados).

---

## Workflow

1. Reunir, por produto: quantidade vendida, faturamento, margem de
   contribuição, posição atual no cardápio.
2. Classificar na matriz mínima:
   - **Alta popularidade + alta margem** — proteger e destacar.
   - **Alta popularidade + baixa margem** — repensar preço/custo sem
     perder o produto (costuma ser produto de entrada/imagem).
   - **Baixa popularidade + alta margem** — reposicionar, testar
     destaque, treinar equipe pra sugerir.
   - **Baixa popularidade + baixa margem** — candidato a simplificar ou
     retirar.
3. **Não usar o rótulo como sentença automática** — cruzar com a função
   estratégica do produto (`dna-do-negocio`): um produto de entrada pode
   ter margem baixa de propósito, um produto sazonal pode ter baixa
   venda só porque é fora de época.
4. Analisar estrutura do cardápio: ordem das categorias, destaque
   visual, nomes, descrição, foto, preço, adicionais, combos, atrito de
   escolha (cardápio confuso reduz conversão).
5. Recomendar, por produto: manter, destacar, reposicionar, reajustar,
   combinar, simplificar, testar ou retirar — com justificativa
   específica, não genérica.
6. Salvar em `<pasta-do-projeto-ativo>/04-marketing/engenharia-cardapio-<data>.md`.

## Saídas

Matriz de classificação + recomendação por produto + análise de
estrutura do cardápio.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/04-marketing/`.

## Regras

- Rótulo da matriz nunca é decisão automática — sempre cruzado com
  função estratégica do produto.
- Recomendação de retirar um produto exige checar se ele tem função
  não-financeira (imagem, entrada, fidelização) antes de confirmar.

## Critérios de qualidade

Toda recomendação é específica ao produto, com dado de venda/margem
citado, não genérica.

## Critérios de validação

Classificação de cada produto é rastreável aos números de venda e
margem usados.

## Limitações

Depende de dado de venda por produto confiável — sem isso, a análise
fica qualitativa e deve ser marcada como tal.

## Contrato de handoff

Encaminha pra `aumento-de-ticket` (combos/adicionais), `precificacao-food-service`
(reajuste), `produto-e-engenharia-de-cardapio` (workflow completo).

## Exemplos de gatilhos positivos

- "Quais produtos devo tirar do cardápio"
- "Meu cardápio está funcionando bem"

## Exemplos de gatilhos negativos

- "Quanto custa esse produto" (é `ficha-tecnica`)
