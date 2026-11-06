---
name: pesquisa-mercado
description: >
  Pesquisa real (via WebSearch/WebFetch) sobre tamanho de mercado,
  tendências, comportamento do público e contexto do setor de um
  cliente/projeto — sempre com fonte registrada. Use quando o usuário
  pedir "pesquisa o mercado de X", "quero entender esse setor antes de
  decidir", "tem demanda pra isso?".
---

# pesquisa-mercado — Pesquisa de mercado com fonte

## Quando usar

Diagnóstico ou plano estratégico que precisa de dado externo real (não
suposição) sobre o mercado do cliente.

## Quando não usar

- Pesquisa de concorrente específico → `analisar-concorrentes`.
- Pesquisa de palavra-chave/SEO → `seo` (mais específico pra isso).

## Entradas

Setor, região, tipo de negócio do cliente/projeto.

## Dependências

WebSearch, WebFetch. `<pasta-do-projeto-ativo>/_fontes/` para cache de
pesquisas já feitas.

## Contexto que deve ser carregado

Diagnóstico do projeto ativo (setor, região, público já levantados).

---

## Workflow

1. Checar `_fontes/` por pesquisa recente (< 30 dias) sobre o mesmo
   tema antes de buscar de novo.
2. Definir as perguntas reais que a pesquisa precisa responder (tamanho
   do mercado, crescimento, sazonalidade, comportamento de compra).
3. Rodar WebSearch/WebFetch, registrando fonte e data de cada dado.
4. Separar fato (fonte verificável) de estimativa (inferência a partir
   de dado parcial) — nunca apresentar estimativa como fato.
5. Salvar em `<pasta-do-projeto-ativo>/01-diagnostico/pesquisa-mercado.md`
   e uma cópia das fontes em `_fontes/`.

## Saídas

`01-diagnostico/pesquisa-mercado.md` com dados, fontes e nível de
confiança de cada afirmação.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/01-diagnostico/` e `_fontes/`.

## Regras

- Toda afirmação de mercado tem fonte e data.
- Nunca inventar número de tamanho de mercado sem fonte real.
- Marcar explicitamente o que é estimativa própria vs. dado de terceiro.

## Critérios de qualidade

Cada dado citado é rastreável até uma fonte real registrada em
`_fontes/`.

## Critérios de validação

Nenhuma afirmação sem fonte ou marcação de estimativa.

## Limitações

Não substitui pesquisa paga/formal (painel, survey) — é pesquisa
aberta via busca.

## Contrato de handoff

Encaminha pra `diagnostico-negocio` ou `plano-estrategico` com os dados
levantados.

## Exemplos de gatilhos positivos

- "Pesquisa o mercado de estética facial na minha região"
- "Tem demanda real pra esse produto?"

## Exemplos de gatilhos negativos

- "Analisa esse concorrente específico" (é `analisar-concorrentes`)
