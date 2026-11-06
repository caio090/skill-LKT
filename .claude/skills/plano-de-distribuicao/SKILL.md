---
name: plano-de-distribuicao
description: >
  Define onde, quando e como o vídeo finalizado é publicado
  (plataforma, formato, legenda, campanha associada), e consolida o
  relatório de desempenho depois de publicado. Use quando o usuário
  pedir "onde a gente publica esse vídeo", "como foi o desempenho desse
  vídeo".
---

# plano-de-distribuicao — Distribuição e resultado

## Quando usar

Vídeo editado e pronto, ou já publicado precisando de relatório de
desempenho.

## Quando não usar

Vídeo ainda em produção → skills anteriores do módulo audiovisual.

## Entradas

Vídeo finalizado (várias versões de formato), estratégia de marketing.

## Dependências

`briefing-de-edicao`, `estrategia-de-marketing`, `aprovar-post` (se for
publicar em redes sociais).

## Contexto que deve ser carregado

Estratégia de marketing e calendário do projeto ativo.

---

## Workflow

### Modo: Plano de distribuição

1. Definir plataformas (Instagram, YouTube, site, WhatsApp) e qual
   versão de formato vai em cada uma.
2. Definir data/hora de publicação, coerente com o calendário de
   conteúdo.
3. Legenda/copy de acompanhamento por plataforma (`texto-natural-pt-br`).
4. Se fizer parte de campanha paga, associar à `campanha-completa`/
   `anuncio-meta`.
5. Publicação em si passa por `aprovar-post` — nunca automática.

### Modo: Relatório de desempenho

1. Reunir métricas por plataforma (visualizações, retenção, cliques,
   conversão — o que estiver disponível).
2. Comparar com objetivo definido no `briefing-audiovisual`.
3. Recomendações pra próxima produção.
4. Salvar em `<pasta-do-projeto-ativo>/09-relatorios/audiovisual-<data>.md`.

## Saídas

Plano de distribuição, ou relatório de desempenho.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/06-audiovisual/` (plano) e `09-relatorios/`
(desempenho).

## Regras

- Publicação sempre via `aprovar-post` — nunca automática.
- Relatório de desempenho sempre compara com o objetivo original do
  briefing, não só lista número solto.

## Critérios de qualidade

Cada plataforma recebe a versão de formato correta (vertical/quadrado/
horizontal).

## Critérios de validação

Relatório de desempenho é rastreável ao objetivo do
`briefing-audiovisual`.

## Limitações

Não publica sozinha — sempre via `aprovar-post`, com confirmação.

## Contrato de handoff

`aprovar-post` (publicação), `relatorio-de-marketing` (se entrar no
consolidado de marketing).

## Exemplos de gatilhos positivos

- "Onde a gente publica esse vídeo institucional"
- "Como foi o desempenho desse vídeo depois de publicado"

## Exemplos de gatilhos negativos

- "Edita esse vídeo" (é `briefing-de-edicao`, passo anterior)
