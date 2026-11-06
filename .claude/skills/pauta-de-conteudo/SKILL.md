---
name: pauta-de-conteudo
description: >
  Detalha uma entrada do calendário de conteúdo em pauta pronta pra
  produção: ângulo, mensagem-chave, referência, formato específico. Use
  quando o usuário pedir "detalha essa pauta", "qual o ângulo desse
  tema".
---

# pauta-de-conteudo — Pauta detalhada

## Quando usar

Antes de produzir a peça (carrossel, artigo, roteiro) de uma entrada do
calendário.

## Quando não usar

Tema ainda não está no calendário → `calendario-de-conteudo` primeiro.

## Entradas

Tema do calendário.

## Dependências

`calendario-de-conteudo`, `posicionamento` (mensagem-chave deriva dele).

## Contexto que deve ser carregado

Posicionamento e preferências de tom do projeto ativo.

---

## Workflow

1. Ângulo específico do tema (não "fala sobre X", e sim "mostra como X
   resolve Y pro público Z").
2. Mensagem-chave (uma frase).
3. Referência (exemplo, dado, história que ilustra).
4. Formato final (carrossel, artigo, vídeo, story).
5. Salvar em `<pasta-do-projeto-ativo>/04-marketing/pautas/<tema>.md`.

## Saídas

Pauta pronta pra virar peça.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/04-marketing/pautas/`.

## Regras

- Ângulo específico, nunca genérico ("fala sobre o produto" não é
  ângulo).

## Critérios de qualidade

Pauta é suficiente pra outra pessoa produzir a peça sem perguntar mais
nada.

## Critérios de validação

Ângulo, mensagem-chave, referência e formato preenchidos.

## Limitações

Não produz a peça final — encaminha pra skill de produção certa.

## Contrato de handoff

Encaminha pra `carrossel`, `publicar-tema` ou `roteiro` conforme o
formato.

## Exemplos de gatilhos positivos

- "Detalha a pauta desse tema da semana"
- "Qual o ângulo pra esse post"

## Exemplos de gatilhos negativos

- "Monta o calendário do mês inteiro" (é `calendario-de-conteudo`)
