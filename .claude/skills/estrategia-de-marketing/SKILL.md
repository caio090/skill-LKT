---
name: estrategia-de-marketing
description: >
  Define a estratégia de marketing de um cliente/projeto: objetivos,
  canais prioritários, mensagem (a partir do posicionamento), verba e
  cronograma macro — antes de qualquer peça ser produzida. Use quando o
  usuário pedir "monta a estratégia de marketing", "por onde começar no
  marketing desse cliente".
---

# estrategia-de-marketing — Estratégia de marketing

## Quando usar

Depois de `diagnostico-negocio` + `posicionamento`, antes de
`plano-de-campanha` ou produção de conteúdo.

## Quando não usar

Produção de peça isolada sem estratégia definida — isso é sintoma de
pular etapa; voltar aqui primeiro.

## Entradas

Diagnóstico, público, posicionamento já definidos.

## Dependências

`posicionamento`, `analisar-publico`, `criar-produto-e-oferta`.

## Contexto que deve ser carregado

`02-estrategia/` do projeto ativo.

---

## Workflow

1. Objetivo de marketing (não confundir com objetivo de negócio — ex.:
   "gerar 50 leads qualificados/mês" é objetivo de marketing).
2. Canais prioritários, com base em onde o público real está
   (`analisar-publico`), não em achismo.
3. Mensagem principal por canal, derivada do `posicionamento` — nunca
   uma mensagem nova desconectada.
4. Verba disponível e como se distribui entre canais.
5. Cronograma macro (o que roda em que mês/trimestre).
6. Salvar em `<pasta-do-projeto-ativo>/04-marketing/estrategia.md`.

## Saídas

`04-marketing/estrategia.md`.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/04-marketing/`.

## Regras

- Mensagem de cada canal deriva do posicionamento já definido, não
  reinventa.
- Canal escolhido tem que ser onde o público real está, não onde é mais
  fácil produzir.

## Critérios de qualidade

Todo canal escolhido é justificado com dado de público, não suposição.

## Critérios de validação

Objetivo de marketing é mensurável (número, prazo).

## Limitações

Não produz peça — define a direção que as skills de produção seguem.

## Contrato de handoff

Encaminha pra `plano-de-campanha`, `calendario-de-conteudo`.

## Exemplos de gatilhos positivos

- "Monta a estratégia de marketing desse cliente"
- "Por onde eu começo no marketing desse negócio"

## Exemplos de gatilhos negativos

- "Cria um post pra hoje" (é `carrossel`/conteúdo direto, se a
  estratégia já existir)
