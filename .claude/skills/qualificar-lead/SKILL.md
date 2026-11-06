---
name: qualificar-lead
description: >
  Avalia se um lead específico é qualificado, com base nos critérios
  definidos em estruturar-crm, e sugere a próxima ação. Use quando o
  usuário pedir "esse lead é bom", "vale a pena investir tempo nesse
  contato".
---

# qualificar-lead — Qualificação de lead

## Quando usar

Avaliação de um lead específico antes de investir tempo comercial nele.

## Quando não usar

Análise agregada do funil → `funil-de-vendas`.

## Entradas

Informações do lead (origem, interesse, orçamento, urgência, fit com o
público-alvo).

## Dependências

`estruturar-crm` (critérios de qualificação já definidos).

## Contexto que deve ser carregado

Público-alvo e oferta do projeto ativo.

---

## Workflow

1. Comparar o lead com o critério de qualificação definido em
   `estruturar-crm` (fit de público, orçamento, urgência).
2. Classificar: qualificado, a nutrir (não está pronto ainda), ou fora
   do perfil.
3. Sugerir próxima ação: avançar pra proposta, nutrir com conteúdo,
   ou descartar educadamente.
4. Registrar no CRM/planilha do projeto.

## Saídas

Classificação do lead + próxima ação recomendada.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/05-comercial/` (registro de lead).

## Regras

- Critério de qualificação vem de `estruturar-crm`, não inventado ad hoc.
- "Fora do perfil" é uma classificação válida — não forçar todo lead a
  parecer qualificado.

## Critérios de qualidade

Classificação é rastreável ao critério definido, não intuição.

## Critérios de validação

Próxima ação é coerente com a classificação.

## Limitações

Depende de critérios de qualificação já definidos — sem isso, roda
`estruturar-crm` primeiro.

## Contrato de handoff

Encaminha pra `script-comercial` (se qualificado, próxima abordagem) ou
`funil-de-vendas` (registro no funil).

## Exemplos de gatilhos positivos

- "Esse lead vale a pena?"
- "Qualifica esse contato que chegou"

## Exemplos de gatilhos negativos

- "Como está meu funil no geral" (é `funil-de-vendas`)
