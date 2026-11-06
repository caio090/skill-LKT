---
name: produto-e-engenharia-de-cardapio
description: >
  Orquestra o ciclo completo de produto e cardápio de um negócio de food
  service: contexto, cardápio atual, fichas técnicas, rendimento/perdas,
  custo e preço, cruzamento com vendas/margem, engenharia de cardápio,
  combos/adicionais, descontos/cupons, estoque, projeção de impacto,
  plano de teste e indicadores. Use quando o usuário pedir "quero refazer
  o cardápio", "revisão completa do cardápio e produtos".
---

# produto-e-engenharia-de-cardapio — Orquestrador de produto/cardápio

## Quando usar

Revisão completa de cardápio/produto — não uma etapa isolada.

## Quando não usar

Pedido específico (só ficha técnica, só engenharia de cardápio) →
chamar a skill direto.

## Entradas

Cardápio atual, fichas técnicas existentes (se houver), dados de venda.

## Dependências

`dna-do-negocio`, `ficha-tecnica`, `rendimento-e-desperdicio`,
`calcular-cmv`/`cmv-real-e-teorico`, `precificacao-food-service`,
`engenharia-de-cardapio`, `aumento-de-ticket`,
`analisar-promocao-cupom`, `estoque-food-service`,
`projecao-financeira`.

## Contexto que deve ser carregado

`.lkt-system/estado/contexto-ativo.json` para o projeto ativo.

---

## Workflow

1. Carregar contexto (`dna-do-negocio`, se existir; senão, levantar o
   mínimo antes de seguir).
2. Identificar negócio e canal (balcão, delivery próprio, marketplace).
3. Ler cardápio atual (via `cardapio-digital` se for digital, ou
   levantamento manual se físico).
4. Cadastrar produtos que ainda não têm ficha técnica.
5. Validar fichas técnicas existentes (`ficha-tecnica`) — datas,
   versões, insumos atualizados.
6. Revisar rendimento e perdas (`rendimento-e-desperdicio`).
7. Calcular custo e preço (`calcular-cmv` / `precificacao-food-service`).
8. Cruzar vendas e margem (`engenharia-de-cardapio`).
9. Executar a classificação da engenharia de cardápio e recomendações.
10. Analisar combos e adicionais (`aumento-de-ticket`).
11. Analisar descontos e cupons ativos (`analisar-promocao-cupom`).
12. Analisar estoque relacionado (`estoque-food-service`).
13. Projetar impacto das mudanças propostas (`projecao-financeira`,
    3 cenários).
14. Criar plano de teste para mudanças significativas (template
    `TESTE-DE-PRODUTO.md`).
15. Definir indicadores de acompanhamento.
16. Registrar decisão final em `_memoria/decisoes.md` (ou do cliente) e
    `PROJETO.md`.

Mostrar resumo curto ao final de cada etapa antes de seguir.

## Saídas

Cardápio revisado com fichas técnicas, preços, classificação de
engenharia de cardápio, plano de teste e indicadores.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/04-marketing/` e `03-financeiro/`.

## Regras

- Nunca pular direto pra "tirar produto X" sem passar pela análise
  completa.
- Toda mudança de preço/cardápio significativa passa por plano de teste
  antes de virar definitiva, quando possível.

## Critérios de qualidade

Cada etapa aplicável foi executada ou descartada com motivo.

## Critérios de validação

Recomendações finais são rastreáveis às etapas anteriores (ficha
técnica → custo → preço → engenharia de cardápio → recomendação).

## Limitações

Ciclo completo depende de dado de venda por produto — sem isso, algumas
etapas ficam qualitativas.

## Contrato de handoff

Encaminha pra `gestao-de-negocio` (próxima ação consolidada) e
`projecao-financeira` (cenários de médio prazo).

## Exemplos de gatilhos positivos

- "Quero refazer o cardápio inteiro"
- "Revisão completa dos produtos e preços"

## Exemplos de gatilhos negativos

- "Só ajusta o preço desse item" (é `precificacao-food-service` isolado)
