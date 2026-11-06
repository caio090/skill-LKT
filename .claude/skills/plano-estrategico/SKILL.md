---
name: plano-estrategico
description: >
  Transforma diagnóstico, público, posicionamento e oferta já definidos
  num plano de ação priorizado: o que fazer, por quê, quem, custo, prazo,
  indicador, risco. Use quando o usuário pedir "monta o plano de ação",
  "o que fazemos primeiro", "estratégia pros próximos meses".
---

# plano-estrategico — Plano de ação priorizado

## Quando usar

Depois de diagnóstico + posicionamento (+ oferta, se aplicável) — nunca
como primeiro passo de um projeto novo.

## Quando não usar

Sem diagnóstico ainda — rodar `diagnostico-negocio` primeiro.

## Entradas

Tudo já registrado em `01-diagnostico/` e `02-estrategia/`.

## Dependências

`diagnostico-negocio`, `posicionamento`, `criar-produto-e-oferta` (os
que existirem).

## Contexto que deve ser carregado

Todo o conteúdo de `01-diagnostico/` e `02-estrategia/` do projeto ativo.

---

## Workflow

1. Listar as ações possíveis a partir dos gargalos do diagnóstico.
2. Pra cada ação, registrar: o que fazer, por que fazer, responsável,
   custo estimado, prazo, indicador de sucesso, risco, prioridade
   (alta/média/baixa).
3. Ordenar por prioridade — o que ataca o gargalo mais crítico primeiro,
   não o que é mais fácil de fazer.
4. Marcar claramente o que é estimativa (custo, prazo) vs. compromisso
   confirmado.
5. Salvar em `<pasta-do-projeto-ativo>/02-estrategia/plano-de-acao.md`.
6. Atualizar `PROJETO.md` (estado passa de "em diagnóstico" pra "em
   execução" quando o plano for aprovado).

## Saídas

`02-estrategia/plano-de-acao.md`.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/02-estrategia/`.

## Regras

- Toda ação tem os 8 campos (o quê, por quê, quem, custo, prazo,
  indicador, risco, prioridade) — nunca uma lista solta sem isso.
- Nunca apresentar estimativa de custo/prazo como compromisso fechado.
- Não incluir ação que não ataca nenhum gargalo do diagnóstico.

## Critérios de qualidade

Toda ação do plano é rastreável a um gargalo específico do diagnóstico.

## Critérios de validação

As 8 informações obrigatórias estão presentes em cada ação do plano.

## Limitações

Não substitui aprovação de orçamento real — os valores aqui são
planejamento, a confirmação financeira é do módulo financeiro/cliente.

## Contrato de handoff

Encaminha pros módulos de execução (`conteudo`, `financeiro`,
`comercial`, `audiovisual`, `tecnologia`) conforme o tipo de cada ação.

## Exemplos de gatilhos positivos

- "Monta o plano de ação pra esse cliente"
- "O que a gente faz primeiro nos próximos 3 meses"

## Exemplos de gatilhos negativos

- "Já sei o plano, só executa" (ainda assim, checar se o plano existe
  registrado — se não, perguntar antes de produzir sem rastreio)
