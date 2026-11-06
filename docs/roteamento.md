# Roteamento

Como uma solicitação é direcionada dentro do REC OS: módulo responsável,
skill(s) usada(s) e memória consultada.

| Tipo de pedido | Módulo | Skill(s) | Memória consultada |
|---|---|---|---|
| Diagnóstico de negócio/marca | `modules/diagnostico` | _a definir na migração_ | empresa, cliente, produtos-e-servicos |
| Briefing de projeto | `modules/briefing` | _a definir na migração_ | cliente, projeto |
| Plano estratégico | `modules/estrategia` | _a definir na migração_ | estrategia, metricas |
| Posicionamento e comunicação | `modules/posicionamento` | _a definir na migração_ | marca, cliente |
| Produtos, ofertas e modelo de negócio | `modules/produtos-e-ofertas` | _a definir na migração_ | produtos-e-servicos |
| Páginas, sites, landing pages, portais | `modules/paginas-e-sites` | `pagina-e-site` → `design-front-end` → `texto-natural-pt-br` | marca, cliente |
| Conteúdo, roteiros, campanhas, calendário | `modules/conteudo` | _a definir na migração_ | marca, preferencias, cliente |
| Tráfego pago | `modules/trafego-pago` | _a definir na migração_ | metricas, cliente |
| CRM, leads, vendas, atendimento | `modules/crm` | _a definir na migração_ | cliente |
| Financeiro (CAC, LTV, ROI, ROAS, margem) | `modules/financeiro` | _a definir na migração_ | metricas |
| Operação e processos internos | `modules/operacional` | _a definir na migração_ | processos, equipe |
| Automações e WhatsApp | `modules/automacoes` | _a definir na migração_ | ferramentas, processos |
| Análise de dados e relatórios | `modules/dados-e-relatorios` | _a definir na migração_ | metricas |

As linhas "_a definir na migração_" serão preenchidas conforme skills forem
migradas de `lkt-plus/`/`MazyOS/` ou criadas do zero — ver
[`manifesto.md`](manifesto.md) e [`catalogo-skills.md`](catalogo-skills.md).
