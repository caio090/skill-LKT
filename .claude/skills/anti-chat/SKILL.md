---
name: anti-chat
description: >
  Quality gate transversal contra aparência e linguagem genérica de IA:
  design de template, gradiente/glassmorphism gratuito, cards demais,
  tipografia preguiçosa, texto motivacional, jargão de marketing sem
  base, estratégia genérica, conta financeira sem contexto e código
  desnecessariamente complexo. Use ao final de qualquer entrega visual,
  textual, estratégica, financeira ou de código antes de considerá-la
  pronta — nunca como etapa isolada a pedido direto do usuário.
---

# anti-chat — Quality gate contra padrão genérico de IA

## Quando usar

Como última etapa (handoff, não execução isolada) de qualquer skill que
produza: site, app, dashboard, apresentação, documento, copy,
estratégia, plano de gestão, relatório financeiro, peça audiovisual ou
código. A pergunta central que orienta a revisão:

> Isso nasceu do contexto real deste projeto ou foi uma resposta padrão
> porque era fácil?

Se for padrão, revisar antes de entregar.

## Quando não usar

- Rascunho interno explicitamente marcado como rascunho, ainda em
  discussão com o usuário.
- Dado bruto (planilha lida, transcrição, ficha técnica numérica) sem
  componente de texto, design ou estratégia — não há o que revisar.
- Não usar como skill isolada a pedido solto ("roda o anti-chat aqui") —
  ela é sempre acoplada à entrega de outra skill.

## Entradas

O material já produzido pela skill principal (texto, design, código,
plano ou análise), antes da entrega final ao usuário.

## Dependências

`texto-natural-pt-br` (linguagem), `design-front-end` (quando houver
UI), `docs/ANTI-CHAT.md` (lista completa de padrões proibidos e
critério de poda).

## Contexto que deve ser carregado

`_memoria/sistema/marca.md` e `_memoria/sistema/preferencias.md` (ou
equivalente do workspace) — o que é genérico só se define em relação ao
negócio real.

---

## Workflow

### Passo 1 — Identificar o tipo de entrega

Design/UI, texto, estratégia/gestão, financeiro ou código — cada um tem
sua lista própria de padrões proibidos (ver `docs/ANTI-CHAT.md`).

### Passo 2 — Aplicar a pergunta central

Para cada elemento (parágrafo, componente visual, recomendação, linha de
código): nasceu do contexto real ou é resposta padrão? Marcar os que
falharem.

### Passo 3 — Checar padrões proibidos específicos

**Texto:** frase motivacional, frase de efeito sem informação,
introdução inútil, adjetivo em excesso, jargão, promessa sem base,
repetição, título genérico, tom de IA, travessão longo, aspas
decorativas, enumeração artificial (lista de três forçada).

**Design/UI:** gradiente sem função, glassmorphism gratuito, blobs,
brilho aleatório, linha/traço decorativo, onda genérica, card atrás de
card, borda em tudo, radius exagerado, sombra em tudo, ícone em toda
linha, três cards porque existem três itens, número gigante sem função,
selo genérico, mockup gratuito, fundo abstrato de IA, hero genérico
(badge + headline + texto + dois botões + cards flutuantes), dashboard
cheio de widget que não responde pergunta real, tipografia padrão do
framework sem justificativa (ver `templates/design/PESQUISA-TIPOGRAFICA.md`).

**Estratégia/gestão:** SWOT por obrigação, persona inventada, funil
padrão sem evidência, "poste mais", "invista em tráfego" sem conta,
benchmark sem fonte, KPI sem decisão associada, meta sem base,
framework escolhido antes do problema.

**Financeiro:** faixa genérica de mercado como verdade universal (ex.:
"CMV acima de X é ruim") sem segmento, região, fonte e data; média de
mercado inventada; projeção sem premissas.

**Código:** abstração antes da necessidade, arquitetura complexa para
problema simples, dependência nova sem necessidade, wrapper sem função,
comentário que repete o código, configuração duplicada,
future-proofing inventado, código morto, feature parcial apresentada
como pronta.

### Passo 4 — Aplicar a pergunta de poda (design)

Se remover o elemento, a compreensão ou a marca pioram? Se não, propor a
remoção.

### Passo 5 — Corrigir ou justificar exceção

Cada padrão proibido encontrado: corrigir, ou registrar por que essa
entrega específica justifica a exceção (ex.: gradiente que é parte da
identidade visual já definida na marca).

## Saídas

A mesma entrega, revisada, com a lista de padrões corrigidos e as
exceções justificadas (quando houver).

## Caminho de salvamento

Não gera arquivo próprio — a revisão se aplica no local onde a entrega
original já está sendo salva pela skill principal.

## Regras

- Nunca aplicar rótulo de "proibido" sem alternativa concreta — sempre
  indicar o que fazer no lugar.
- Nunca aceitar exceção sem justificativa registrada.
- Fazer handoff, nunca copiar esta skill inteira para dentro de outra.

## Critérios de qualidade

Cada elemento da entrega final é rastreável a uma decisão de contexto
real (negócio, marca, dado) — não a um padrão genérico reaproveitado.

## Critérios de validação

Reler a entrega perguntando "isso poderia ter sido gerado sem saber nada
sobre este negócio específico?" — se a resposta for sim, a revisão ainda
não terminou.

## Limitações

Julgamento de skill, não motor de regras automatizado — decisões de
gosto/estilo ficam registradas como recomendação, o usuário decide em
caso de divergência.

## Contrato de handoff

Skills que devem chamar `anti-chat` como etapa final: `pagina-e-site`,
`design-front-end`, `app-e-sistema`, `criar-apresentacao`,
`criar-documento`, `criar-pdf`, `proposta-comercial`,
`relatorio-executivo`, `diagnostico-completo`, `plano-financeiro-completo`,
`campanha-completa`, `producao-audiovisual-completa`,
`construir-produto-digital`.

## Exemplos de gatilhos positivos

- Entrega final de site, apresentação ou proposta, antes de mostrar ao
  usuário.
- "Isso não ficou meio genérico?"

## Exemplos de gatilhos negativos

- "Roda o anti-chat" isolado, sem entrega associada — pedir qual entrega
  revisar.
- Planilha ou dado bruto sem texto/design/estratégia associado.
