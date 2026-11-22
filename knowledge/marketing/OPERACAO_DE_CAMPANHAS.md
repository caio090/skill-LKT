# Operação de campanhas — rascunho, revisão, publicação e veiculação

Regra geral para qualquer skill que estruture campanha Meta ou Google
(`anuncio-meta`, `anuncio-google`, `criar-campanha`, `plano-de-campanha`,
`campanha-completa`). Conhecimento geral; sem dados de cliente.

## Fluxo obrigatório

1. **Rascunho** — a skill monta a estrutura (campanha, conjuntos, anúncios,
   criativos, públicos, orçamento, evento de conversão, UTMs). Nada vai
   para a plataforma.
2. **Revisão** — alguém da equipe revisa e envia para aprovação.
3. **Aprovação** — só admin/super_admin aprova. Editar orçamento, datas,
   nome ou objetivo de algo aprovado devolve para rascunho.
4. **Publicação** — feita pelo servidor, só do que foi aprovado, e o objeto
   nasce **PAUSADO** na plataforma. Publicar não gera gasto.
5. **Veiculação** — ativar (gasto real) exige autorização específica,
   registrada (quem e quando) e confirmada na execução. Nunca automática,
   nunca "por padrão", nunca dentro de uma skill.

Uma skill pode entregar o rascunho e o checklist. Nunca ativa anúncio,
nunca aumenta orçamento e nunca cria gasto sem autorização explícita do
responsável pela conta.

## Ligação com funil e CRM

Toda campanha aponta para: cliente → funil → etapa do funil (o que ela
alimenta) → evento de conversão esperado. O lead que chega registra origem
(canal, UTMs, campanha/anúncio do primeiro toque). Oportunidade e venda
ficam no CRM do cliente, ligadas ao lead. Assim o resultado é lido por
etapa, do anúncio à venda.

No LOKAT OS isso corresponde às tabelas `mkt_funnels`, `mkt_funnel_stages`,
`mkt_campaigns`, `mkt_ad_sets`, `mkt_ads`, `mkt_creatives`, `mkt_leads`,
`mkt_opportunities`, `mkt_conversion_events` e `mkt_performance_daily`
(migração 105 do repositório lokat-os).

## Meta: o que verificar antes de ler ou publicar

- Versão da API explícita e atual (v26.0 em 2026-11; conferir a
  documentação oficial antes de mudar).
- Permissões: `ads_read` para relatórios; `ads_management` para criar e
  editar. Contas de terceiros pedem Advanced Access (Revisão do App).
- Token: de longa duração, com validade e escopos registrados; renovar ou
  reconectar quando expirar; revogar quando o cliente sair.
- Pixel e API de Conversões: mesmo `event_id` nos dois para deduplicar.
- Leitura de Insights: paginação por cursor, limites de requisição com
  nova tentativa e espera, datas no fuso da conta, valores na moeda da
  conta, configuração de atribuição registrada.

## Google Ads

Mesmo fluxo. A estrutura pode ser entregue como planilhas para o Google
Ads Editor (ver `anuncio-google`), importadas com a campanha **pausada**;
ativação segue a mesma regra de autorização.
