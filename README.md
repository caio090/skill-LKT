# REC OS

Sistema operacional interno da Lokat: diagnóstico, briefing, estratégia,
posicionamento, produtos e ofertas, páginas e sites, conteúdo, tráfego
pago, CRM, financeiro, operação, automações e dados — tudo rodando dentro
do Claude Code, com memória própria por empresa/cliente/projeto.

## Estrutura

- `modules/` — uma pasta por área de atuação (diagnóstico, briefing,
  estratégia, posicionamento, produtos-e-ofertas, páginas-e-sites,
  conteúdo, tráfego pago, CRM, financeiro, operacional, automações,
  dados-e-relatórios).
- `templates/` — ponto de partida por tipo de negócio: `nova-marca`,
  `negocio-local`, `produto-digital`, `cliente-modelo`.
- `.claude/skills/` — skills do sistema (uma pasta por skill, com
  `SKILL.md`).
- `arquivos/` — central de arquivos: `entrada/` (não processados),
  `processados/` (resultado da análise), `biblioteca/` (material
  permanente, por categoria).
- `_memoria/` — memória do sistema: empresa, preferências, estratégia,
  marca, clientes, produtos e serviços, projetos, processos, ferramentas,
  equipe, métricas, decisões, aprendizados, pendências.
- `docs/` — manifesto de arquivos, catálogo de skills e roteamento.
- `tools/` — scripts de validação e manutenção.

## Como operar

Regras completas em [`CLAUDE.md`](CLAUDE.md) (e resumo em
[`AGENTS.md`](AGENTS.md)). Em resumo: o Claude lê a memória antes de
responder, procura skill relevante antes de executar qualquer tarefa, e
mantém contexto de empresa, cliente e projeto sempre separados.

## Origem

O REC OS nasceu para substituir duas instalações anteriores do mesmo tipo
de sistema — `lkt-plus/` e `MazyOS/`, pastas irmãs preservadas apenas como
fonte de consulta e migração (não fazem parte do REC OS e não devem ser
alteradas). O processo de migração é registrado em
[`docs/manifesto.md`](docs/manifesto.md).

## Validação

```
node tools/validar.js
```

Verifica frontmatter das skills, nomenclatura de pastas, links quebrados e
referências remanescentes a MazyOS/LKT Plus.
