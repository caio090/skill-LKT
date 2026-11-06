---
name: funil-de-vendas
description: >
  Acompanha e analisa o funil de vendas já estruturado: quantos leads em
  cada etapa, taxa de conversão entre etapas, tempo médio, gargalos, e
  documenta o playbook comercial (o que fazer em cada etapa). Use quando
  o usuário pedir "como está meu funil", "onde estou perdendo vendas",
  "documenta o playbook comercial".
---

# funil-de-vendas — Acompanhamento e playbook do funil

## Quando usar

Funil já estruturado (`estruturar-crm`) que precisa de análise de
desempenho ou documentação do processo.

## Quando não usar

Funil ainda não existe → `estruturar-crm` primeiro.

## Entradas

Dados de leads/clientes por etapa (quantidade, tempo, conversão).

## Dependências

`estruturar-crm`.

## Contexto que deve ser carregado

Estrutura de CRM do projeto ativo.

---

## Workflow

### Modo: Análise de funil

1. Quantos leads em cada etapa.
2. Taxa de conversão entre etapas consecutivas.
3. Tempo médio em cada etapa.
4. Identificar gargalo (etapa com maior perda ou maior tempo parado).
5. Recomendações concretas pro gargalo identificado.

### Modo: Playbook comercial

Documentar, por etapa: o que fazer, quem faz, script/material de apoio
(`script-comercial`), critério pra avançar/perder o lead.

Salvar em `<pasta-do-projeto-ativo>/05-comercial/funil-<periodo>.md` ou
`playbook-comercial.md`.

## Saídas

Análise de funil com gargalo identificado, ou playbook documentado.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/05-comercial/`.

## Regras

- Gargalo apontado com dado (taxa de conversão, tempo), não impressão.
- Playbook reflete o processo real, não um ideal nunca praticado.

## Critérios de qualidade

Toda etapa do playbook tem ação e critério de avanço claros.

## Critérios de validação

Taxas de conversão somadas/calculadas batem com os dados de entrada.

## Limitações

Depende de dado real de movimentação de lead — sem isso, a análise fica
qualitativa.

## Contrato de handoff

Encaminha pra `qualificar-lead`, `script-comercial`,
`plano-estrategico` (se o gargalo exigir replanejamento maior).

## Exemplos de gatilhos positivos

- "Como está meu funil de vendas esse mês"
- "Documenta o playbook comercial"

## Exemplos de gatilhos negativos

- "Estrutura meu funil do zero" (é `estruturar-crm`)
