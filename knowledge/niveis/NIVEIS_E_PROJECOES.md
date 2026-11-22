# Níveis e projeções

As faixas de prazo e custo de um nível (`schemas/level-definition.schema.json`,
campos `prazo_minimo`/`prazo_maximo`/`custo_minimo`/`custo_maximo`)
alimentam projeções — nunca são tratadas como preço final automático.

## O que a projeção considera

Nível atual, nível recomendado, quantidade de lacunas, complexidade,
dependências, disponibilidade, custos externos, risco, urgência,
capacidade do cliente, capacidade do prestador.

## O que a projeção gera

Cenário conservador, cenário base, cenário ampliado — cada um com
hipótese, fonte, confiança e gatilho de revisão explícitos, seguindo o
mesmo padrão de `docs/PROJECOES.md` e `schemas/projecao.schema.json`.

## Como isso se conecta

```
classificar-nivel → nível atual + nível recomendado + lacunas
  → gerar-plano-de-avanco → ações, entregáveis, dependências, prazo, custo
    → projecoes (skill existente) → cenários conservador/base/ampliado
```

A skill `projecoes` (já existente) recebe a faixa do nível como uma das
entradas possíveis — não é um novo motor de projeção, é mais uma fonte
de dado para o motor que já existe.

## Regra

Nunca apresentar a faixa de custo/prazo de um nível como cotação
fechada. Toda vez que uma faixa de nível virar número específico numa
proposta, isso passa por `proposta-e-precificacao` ou
`gerar-proposta-a-partir-do-nivel`, que aplicam a composição completa
de preço (ver `docs/PADRAO_DE_ARQUIVOS.md` e
`knowledge/niveis/NIVEIS_E_PROPOSTAS.md`).
