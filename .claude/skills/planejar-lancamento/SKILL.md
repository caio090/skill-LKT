---
name: planejar-lancamento
description: >
  Planeja um lançamento de produto ou serviço para um cliente/projeto
  (semente, interno, em parceria ou perpétuo), usando a Fórmula de
  Lançamento de Érico Rocha (adaptação do Product Launch Formula de Jeff
  Walker) como referência: fases, conteúdos, funil, eventos de conversão,
  campanhas, cronograma, riscos e métricas por etapa, sem prometer
  resultado. Use quando o usuário pedir "planeja o lançamento", "quero
  lançar esse curso/serviço", "monta o cronograma do lançamento".
---

# planejar-lancamento — Lançamento com fases, funil e métricas por etapa

Transforma a intenção de lançar em um plano executável e mensurável,
adaptado ao cliente. A metodologia é referência de planejamento; o plano
nunca promete faturamento.

## Quando usar

- Há uma oferta (nova ou existente) para vender num período definido ou de
  forma perpétua, e o cliente quer estruturar o lançamento.

## Quando não usar

- Campanha sazonal ou promoção sem fases de aquecimento → `plano-de-campanha`.
- A oferta ainda não existe ou não está clara → `criar-produto-e-oferta` antes.
- Só medir um funil que já roda → `desenhar-funil` / `analisar-conversao`.

## Entradas

- Cliente/projeto e oferta (o que é, preço, entrega, garantia).
- Público e audiência própria disponível (lista, seguidores, WhatsApp).
- Recursos: equipe, verba de mídia, prazo, quem apresenta o conteúdo.
- Histórico de lançamentos anteriores, se houver (números com fonte).
- Restrições: datas, capacidade de entrega, regras do setor.

## Dependências

- `knowledge/marketing/FUNIS_LANCAMENTOS_E_METRICAS.md` (origem das ideias,
  modelos de lançamento, métricas com fórmula/período/fonte/limitações)
- `knowledge/marketing/OPERACAO_DE_CAMPANHAS.md` (rascunho → revisão →
  publicação pausada → veiculação autorizada)
- `.claude/skills/desenhar-funil` (etapas e eventos)
- `.claude/skills/plano-de-campanha` (campanhas de cada fase)
- `.claude/skills/texto-natural-pt-br` (todo texto público)

## Contexto que deve ser carregado

- `_memoria/empresa.md`, `_memoria/estrategia.md`, `_memoria/preferencias.md`
- Memória e workspace do cliente (`_memoria/clientes/<cliente>.md`).
- Funis e campanhas já existentes do cliente (evitar duplicar).

---

## Workflow

### Passo 1 — Perguntar o que falta (ver `perguntas.txt`)

Só o que não estiver na memória do cliente. Uma pergunta por vez quando a
informação for decisiva (modelo, audiência, capacidade de entrega).

### Passo 2 — Escolher o modelo

Semente, interno, parceria ou perpétuo, pela tabela da referência. Dizer
por que o modelo serve **para este cliente** e o que faria escolher outro.

### Passo 3 — Montar as fases

Para cada fase: objetivo, datas (com fuso), conteúdos/peças, canal,
evento que comprova o avanço e responsável. Escassez e prazo só se forem
verdadeiros.

### Passo 4 — Ligar ao funil e às campanhas

Uma etapa do funil por passagem mensurável (ex.: anúncio → inscrição →
presença no conteúdo → carrinho → compra). Cada campanha aponta para a
etapa que alimenta. Campanhas saem como **rascunho**; publicação nasce
pausada; veiculação exige autorização registrada.

### Passo 5 — Métricas e leitura

Para cada etapa: métrica, fórmula, período, fonte e limitação (copiar da
referência). Meta numérica só se o cliente tiver histórico ou benchmark
com fonte; senão, a primeira rodada é linha de base.

### Passo 6 — Riscos e plano B

Capacidade de entrega, página fora do ar, verba acabando antes do
carrinho, rastreamento quebrado (Pixel/CAPI/UTM), reprovação de anúncio,
promessas que violem regras de anúncio ou o CDC.

## Saídas

- `PLANO_DE_LANCAMENTO.md` no projeto do cliente: modelo e justificativa,
  fases com datas, funil com eventos, lista de campanhas (rascunho),
  conteúdos, métricas por etapa, riscos, responsáveis e checklist.
- Quando o projeto for o LOKAT OS: correspondência com `mkt_launches`
  (fases), `mkt_funnels`/`mkt_funnel_stages` e `mkt_campaigns`.

## Regras

- Citar a origem (Érico Rocha / Jeff Walker) como referência; nunca como
  garantia.
- Nenhuma meta universal; nenhum "lançamento de seis dígitos".
- Nunca ativar anúncio, aumentar verba ou publicar sem o fluxo de
  autorização.
- Não copiar dados privados do cliente para repositório público.

## Critérios de qualidade

- Cada fase tem objetivo, data, peça, canal, evento e responsável.
- Cada etapa do funil tem evento e fonte de dado.

## Critérios de validação

- O plano funciona com a capacidade de entrega informada.
- Toda métrica tem fórmula, período, fonte e limitação.
- Nenhum texto promete resultado financeiro.

## Limitações

- Não estima faturamento sem histórico; quando pedido, faz cenário com
  premissas explícitas e marca como estimativa.
- Não substitui revisão jurídica de oferta, garantia ou sorteio.

## Caminho de salvamento

`workspaces/clientes/<cliente>/projetos/<projeto>/04-marketing/PLANO_DE_LANCAMENTO.md`

## Contrato de handoff

Entrega o plano e a lista de campanhas em rascunho. Para estruturar cada
campanha, seguir com `plano-de-campanha` → `anuncio-meta`/`anuncio-google`.
Textos passam por `texto-natural-pt-br`.

## Exemplos de gatilhos positivos

- "Planeja o lançamento do curso em março"
- "Quero fazer um lançamento semente pra validar esse serviço"
- "Monta o cronograma de pré-lançamento"

## Exemplos de gatilhos negativos

- "Faz a campanha de Black Friday" (sazonal → `plano-de-campanha`)
- "Por que a conversão do lançamento caiu?" (→ `analisar-conversao`)
