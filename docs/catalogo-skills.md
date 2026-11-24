# Catálogo de skills

Lista de todas as skills ativas em `.claude/skills/`. Atualizar sempre que
uma skill for criada, migrada ou removida — ver regra de validação em
[`../CLAUDE.md`](../CLAUDE.md).

| Skill | Descrição | Módulo relacionado | Origem |
|---|---|---|---|
| `vidigal-png` | Processo visual V22 R12: briefing, integridade de ativos, pesquisa visual adaptativa 3x1, direção de arte, tipografia, Brand Scale Lock, Anti-Chat e Quality Control | `modules/conteudo` / design visual | Prompt consolidado Vidigal PNG V22 R12 fornecido pelo usuário |

| `promptificacao-programacao-lkt` | Prompts de programação numerados, contexto, execução, validação e relatório por evidências | `modules/operacional` | Padrão definido pelo usuário |

## Skills obrigatórias em cadeia

Para páginas, sites, landing pages, dashboards, portais ou interfaces:

1. `pagina-e-site`
2. `design-front-end`
3. `texto-natural-pt-br`

Para qualquer texto voltado ao público final, aplicar `texto-natural-pt-br`
ao final do fluxo, independente da skill principal usada.
