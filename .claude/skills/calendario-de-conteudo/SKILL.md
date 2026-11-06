---
name: calendario-de-conteudo
description: >
  Monta o calendário editorial recorrente (não de campanha específica):
  temas, formato, canal e frequência, coerente com a estratégia de
  marketing. Use quando o usuário pedir "monta o calendário de conteúdo
  do mês", "o que a gente posta essa semana".
---

# calendario-de-conteudo — Calendário editorial

## Quando usar

Planejamento recorrente de conteúdo (semanal/mensal), fora do escopo de
uma campanha específica.

## Quando não usar

Campanha específica com cronograma próprio → `plano-de-campanha`.

## Entradas

Estratégia de marketing, temas relevantes ao negócio/público.

## Dependências

`estrategia-de-marketing`, `pauta-de-conteudo` (detalhamento de cada
tema).

## Contexto que deve ser carregado

Estratégia de marketing do projeto ativo.

---

## Workflow

1. Definir frequência por canal (ex.: 3 posts/semana Instagram, 1
   artigo/semana blog).
2. Distribuir temas ao longo do período — variar formato (educativo,
   institucional, prova social, bastidor) sem repetir o mesmo tipo
   seguido.
3. Marcar datas relevantes (sazonalidade, datas comemorativas do
   nicho).
4. Pra cada entrada do calendário, indicar: tema, formato, canal, data.
5. Salvar em `<pasta-do-projeto-ativo>/04-marketing/calendario-<periodo>.md`.

## Saídas

Calendário com tema/formato/canal/data por entrada.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/04-marketing/`.

## Regras

- Não repetir o mesmo formato em publicações seguidas.
- Todo tema do calendário é coerente com a estratégia/posicionamento.

## Critérios de qualidade

Frequência é sustentável pra capacidade real de produção do
cliente/equipe (não criar calendário que ninguém consegue cumprir).

## Critérios de validação

Cada entrada tem tema, formato, canal e data definidos.

## Limitações

Não escreve o conteúdo em si — isso é `pauta-de-conteudo` +
`carrossel`/`publicar-tema`/`roteiro`.

## Contrato de handoff

Encaminha pra `pauta-de-conteudo` (detalhar cada entrada).

## Exemplos de gatilhos positivos

- "Monta o calendário de conteúdo do mês"
- "O que a gente posta essa semana"

## Exemplos de gatilhos negativos

- "Planeja a campanha de black friday" (é `plano-de-campanha`)
