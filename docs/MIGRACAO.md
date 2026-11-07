# Migração: REC OS → LKT System

## Genealogia

1. **MazyOS** e **LKT Plus**: instalações anteriores do mesmo tipo de
   sistema (pastas `MazyOS/` e `lkt-plus/`, fora deste repositório).
2. **REC OS**: substituiu as duas; documentação original preservada em
   [`manifesto.md`](manifesto.md) e no histórico Git.
3. **LKT System 1.0.0**: núcleo de 127 skills instalado na Tayannara em
   2026-08-03 e importado para este repositório no PR #1.
4. **LKT System (biblioteca central)**: esta revisão. Nome canônico
   **LKT System**; REC OS fica como nome histórico.

## O que mudou para quem usa

| Antes | Agora | Ação |
|---|---|---|
| `docs/catalogo-skills.md` editado à mão | Gerado de `registry/skills.json` | Editar `registry/fontes.json` e rodar `tools/registro.py build` + `catalogo` |
| Instalador lia `.claude/skills`, `vendor/tayannara-skills` e `vendor/superpowers` | Lê só skills `aprovada` do registro | Skills do superpowers não são mais instaladas por este instalador (não passaram pela verificação de licença do registro; MIT, podem ser propostas como candidatas) |
| Perfis `base`, `web`, `marketing`, `automacao` no código | 10 perfis em `registry/perfis.json` | Os 4 nomes antigos continuam existindo |
| `--apply` copiava; pasta existente era sempre preservada | Igual, mais manifesto `.lkt/instalacao.json`, `--check`, `--update`, `--rollback`, `--uninstall` | Projetos instalados pela versão antiga não têm manifesto: suas pastas aparecem como `EXISTENTE_NAO_GERENCIADA` e são preservadas. Para passar a gerenciar, remova a pasta manualmente e reinstale |
| `salvar`, `atualizar` (LKT Plus) instaláveis | `aposentada` | Usar `salvar-local` e `atualizar-memoria` |
| Validador apontava 56 "links quebrados" | 0 no conteúdo LKT; links de terceiros viram aviso | — |

## Pendências conhecidas da migração

- `CLAUDE.md` e `AGENTS.md` ainda descrevem `modules/` e `templates/`, que
  não existem neste repositório (herança do REC OS). As regras de operação
  continuam válidas; a estrutura de módulos deve ser criada ou removida da
  documentação numa próxima revisão.
- Raiz sem `LICENSE` (decisão do dono, ver [`licencas.md`](licencas.md)).
