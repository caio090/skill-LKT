---
name: script-comercial
description: >
  Escreve script/roteiro de abordagem comercial (ligação, reunião,
  mensagem) e trata objeções comuns, incluindo follow-up quando não há
  resposta. Use quando o usuário pedir "escreve o script de vendas",
  "como eu respondo essa objeção de preço", "monta o follow-up".
---

# script-comercial — Script de abordagem e objeções

## Quando usar

Preparação de abordagem comercial (ligação, reunião, mensagem) ou
resposta a objeção.

## Quando não usar

Mensagem de atendimento pós-venda → `atendimento`.

## Entradas

Etapa do funil, perfil do lead, objeção específica (se houver).

## Dependências

`posicionamento`, `criar-produto-e-oferta`, `_memoria/preferencias.md`.

## Contexto que deve ser carregado

Posicionamento e oferta do projeto ativo.

---

## Workflow

### Modo: Script de abordagem

1. Abertura (contexto, sem enrolar).
2. Perguntas de descoberta (entender a dor real do lead).
3. Apresentação da oferta conectada à dor identificada.
4. Próximo passo claro (não terminar sem next step definido).

### Modo: Tratamento de objeção

1. Identificar a objeção real por trás da frase (preço pode significar
   "não vi valor", não literalmente "caro").
2. Responder reconhecendo, não se defendendo.
3. Reconectar com o valor/diferencial já definido no posicionamento.

### Modo: Follow-up

1. Se não houver resposta em X dias, mensagem de follow-up curta,
   trazendo novo valor (não só "oi, tudo bem, viu minha mensagem?").
2. Definir quantas tentativas antes de considerar o lead frio.

## Saídas

Script de abordagem, resposta de objeção, ou mensagem de follow-up.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/05-comercial/scripts/`.

## Regras

- Objeção respondida com reconhecimento, nunca defensiva.
- Follow-up sempre agrega algo novo, não é só "lembrete".
- Seguir `_memoria/preferencias.md` — sem jargão de vendas genérico
  ("oportunidade única", "não perca").

## Critérios de qualidade

Script termina sempre com próximo passo claro.

## Critérios de validação

Objeção tratada reconecta com o posicionamento/diferencial real.

## Limitações

Não substitui treinamento de equipe comercial — é material de apoio.

## Contrato de handoff

`texto-natural-pt-br` (acabamento), `funil-de-vendas` (registro).

## Exemplos de gatilhos positivos

- "Escreve o script de abordagem pra ligação"
- "Como eu respondo objeção de preço"
- "Monta o follow-up pra esse lead que sumiu"

## Exemplos de gatilhos negativos

- "Escreve uma mensagem de suporte pro cliente já ativo" (é `atendimento`)
