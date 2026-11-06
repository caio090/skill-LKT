---
name: posicionamento
description: >
  Define posicionamento e mensagem central de um cliente/projeto: o que
  o diferencia de verdade, pra quem, e como isso se traduz em
  comunicação. Baseado em diagnóstico, público e concorrência já
  levantados. Use quando o usuário pedir "define o posicionamento",
  "qual nossa mensagem principal", "como a gente se diferencia".
---

# posicionamento — Posicionamento e mensagem central

## Quando usar

Depois de diagnóstico + análise de público/concorrência, antes de
qualquer plano de comunicação ou conteúdo.

## Quando não usar

- Sem diagnóstico ainda feito — rodar `diagnostico-negocio` primeiro.

## Entradas

`01-diagnostico/` completo (diagnóstico, público, concorrência).

## Dependências

`analisar-publico`, `analisar-concorrentes` (reaproveitar se já
existirem).

## Contexto que deve ser carregado

Diagnóstico completo do projeto ativo.

---

## Workflow

1. Ler diagnóstico, público e concorrência já levantados.
2. Identificar o diferencial real (não genérico — "qualidade" e
   "atendimento" não são diferencial se todo concorrente diz o mesmo).
3. Definir pra quem esse diferencial importa de verdade (cruzar com
   `publico.md`).
4. Escrever a mensagem central em uma frase testável — se ela também
   servisse pra qualquer concorrente, não é posicionamento de verdade.
5. Traduzir em 2-3 mensagens de apoio (o que sustenta a mensagem
   central).
6. Salvar em `<pasta-do-projeto-ativo>/02-estrategia/posicionamento.md`.

## Saídas

`02-estrategia/posicionamento.md`.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/02-estrategia/`.

## Regras

- Posicionamento genérico (que serviria pra qualquer concorrente) é
  rejeitado — voltar e refinar.
- Baseado em diferencial real, não aspiracional sem lastro.

## Critérios de qualidade

A mensagem central passa no teste: "um concorrente direto poderia dizer
a mesma coisa?" — se sim, não está pronta.

## Critérios de validação

Posicionamento é coerente com diagnóstico, público e concorrência já
levantados (não contradiz nenhum).

## Limitações

Não cria peças de comunicação — define a mensagem que as peças (feitas
por `conteudo`, `carrossel`, `pagina-e-site`) vão seguir.

## Contrato de handoff

Encaminha pra `plano-estrategico`, `estrategia-de-marketing`,
`criar-produto-e-oferta`.

## Exemplos de gatilhos positivos

- "Define o posicionamento desse cliente"
- "Qual nossa mensagem central"

## Exemplos de gatilhos negativos

- "Escreve o post de hoje" (isso é conteúdo, que deveria seguir o
  posicionamento já definido, não redefini-lo)
