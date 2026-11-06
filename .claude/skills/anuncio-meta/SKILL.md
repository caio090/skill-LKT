---
name: anuncio-meta
description: >
  Monta estrutura de campanha do Meta Ads (Instagram/Facebook) a partir
  de briefing/estratégia: campanha, conjuntos de anúncio, públicos,
  criativos e copy — pronta pra configurar no Gerenciador de Anúncios.
  Use quando o usuário pedir "cria uma campanha de Instagram Ads",
  "monta o anúncio pro Facebook".
---

# anuncio-meta — Estrutura de campanha Meta Ads

## Quando usar

Campanha paga em Instagram/Facebook a partir de estratégia/briefing já
definido.

## Quando não usar

Google Ads → `anuncio-google`.

## Entradas

Objetivo, público, orçamento, criativos disponíveis (ou a produzir via
`carrossel`).

## Dependências

`estrategia-de-marketing` ou `plano-de-campanha`, `_memoria/empresa.md`,
`_memoria/preferencias.md`.

## Contexto que deve ser carregado

Estratégia/campanha do projeto ativo.

---

## Workflow

1. Objetivo da campanha (reconhecimento, tráfego, conversão, mensagens).
2. Público: segmentação com base em `analisar-publico` — nunca persona
   genérica.
3. Estrutura: campanha → conjuntos de anúncio (1 por público/
   objetivo) → anúncios (2-3 variações de criativo por conjunto).
4. Criativos: se ainda não existirem, encaminhar pra `carrossel` (peça
   estática) — vídeo curto encaminha pra `roteiro`.
5. Copy: seguir `_memoria/preferencias.md`, CTA específico.
6. Orçamento e programação por conjunto.
7. Checklist de conversões configuradas (pixel/evento) antes de ativar.
8. Salvar em `<pasta-do-projeto-ativo>/04-marketing/campanhas/meta-ads-<data>/`.

## Saídas

Estrutura de campanha pronta (documento, não CSV — Meta Ads não tem
importação CSV padrão como Google Ads).

## Caminho de salvamento

`<pasta-do-projeto-ativo>/04-marketing/campanhas/`.

## Regras

- Nunca inventar CPM/CPC esperado — se perguntado, dizer que depende de
  leilão real e dar faixa via pesquisa, não afirmar número fixo.
- Sempre começar campanha pausada — ativação é decisão do cliente.
- Conversão/pixel configurado antes de ativar — sem isso, alertar que o
  Meta não otimiza direito.

## Critérios de qualidade

Cada conjunto de anúncio tem público específico, não um público genérico
repetido em todos.

## Critérios de validação

Checklist de conversão conferido antes de considerar pronto pra ativar.

## Limitações

Não ativa a campanha de verdade — monta a estrutura pra configuração
manual ou futura integração via API.

## Contrato de handoff

`carrossel`/`roteiro` (criativos), `relatorio-de-marketing` (depois de
rodar).

## Exemplos de gatilhos positivos

- "Cria uma campanha de Instagram Ads pra esse produto"
- "Monta o anúncio pro Facebook"

## Exemplos de gatilhos negativos

- "Cria a campanha no Google Ads" (é `anuncio-google`)
