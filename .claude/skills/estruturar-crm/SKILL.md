---
name: estruturar-crm
description: >
  Estrutura o CRM de um cliente/projeto: etapas do funil, campos por
  lead/cliente, critérios de qualificação e regras de movimentação entre
  etapas — não é um CRM web, é a estrutura/regra pra usar em qualquer
  ferramenta (planilha, CRM real, ou o próprio LKT System). Use quando o
  usuário pedir "estrutura meu CRM", "organiza meu funil de vendas".
---

# estruturar-crm — Estrutura de CRM

## Quando usar

Negócio sem processo comercial estruturado, ou que quer organizar antes
de escolher/usar uma ferramenta.

## Quando não usar

Ferramenta de CRM já madura precisando só de ajuste pontual — editar
direto.

## Entradas

Processo comercial atual (mesmo informal), diagnóstico do negócio.

## Dependências

`diagnostico-negocio`, `analisar-publico`.

## Contexto que deve ser carregado

Diagnóstico e oferta do projeto ativo.

---

## Workflow

1. Definir etapas do funil (ex.: novo lead → qualificado → proposta →
   negociação → fechado/perdido) — específicas do negócio, não um
   template genérico de 20 etapas que ninguém usa.
2. Definir campos mínimos por lead/cliente (nome, contato, origem,
   interesse, valor estimado, responsável, última interação).
3. Definir critério de qualificação (o que torna um lead "qualificado" —
   ver `qualificar-lead`).
4. Definir regra de movimentação entre etapas (o que precisa acontecer
   pra avançar).
5. Definir o que salvar em `_memoria/pendencias.md`/`PROJETO.md` vs. o
   que vive só na ferramenta de CRM em si.
6. Salvar em `<pasta-do-projeto-ativo>/05-comercial/estrutura-crm.md`.

## Saídas

Estrutura de funil com etapas, campos e regras de movimentação.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/05-comercial/`.

## Regras

- Etapas específicas do negócio real, não template genérico.
- Não recomendar ferramenta específica de CRM sem o cliente pedir —
  a estrutura funciona em qualquer ferramenta.

## Critérios de qualidade

Cada etapa tem critério objetivo de quando um lead avança pra ela.

## Critérios de validação

Estrutura é usável tanto em planilha simples quanto em CRM formal.

## Limitações

Não implementa integração com ferramenta de CRM real — isso é
`integrar-api` (módulo de tecnologia), quando necessário.

## Contrato de handoff

Encaminha pra `funil-de-vendas` (operação do funil no dia a dia) e
`qualificar-lead`.

## Exemplos de gatilhos positivos

- "Estrutura meu CRM do zero"
- "Organiza meu funil de vendas"

## Exemplos de gatilhos negativos

- "Qualifica esse lead específico" (é `qualificar-lead`)
