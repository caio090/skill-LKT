# Reconciliação dos inventários 103, 163 e 244

Data: 2026-11-06. Evidência: [`RECONCILIACAO-2026-11-06.csv`](RECONCILIACAO-2026-11-06.csv)
(uma linha por skill do inventário local, cruzada com `registry/skills.json`).

Os três números medem **universos diferentes** e não podem ser somados.

| Universo | Fonte | Contagem | O que conta |
|---|---|---|---|
| LKT da Tayannara | `~/tayannara-contadora/.claude/skills` (sistema de arquivos local) | 103 | Instalação LKT System em um projeto de cliente |
| Instaladas no computador | Varredura local de `SKILL.md` (Claude Code, claude.ai, Codex, projetos) | 244 nomes distintos | Inclui as 103 + 141 de plataformas e terceiros |
| Árvore Git, PR #1 (antes desta revisão) | `git ls-files` na branch `feat/importar-skills-lkt-completas` @ `1631070` | 163 em `.claude/skills` + 80 em `terceiros/codex` | Biblioteca versionada |
| Árvore Git, depois desta revisão | `registry/skills.json` | 168 em `.claude/skills` + 80 em `terceiros/codex` = 248 | +3 candidatas importadas, +2 autorais novas |

## 103 dentro das 163 (comparação por hash do `SKILL.md`)

- **103/103** presentes no repositório com o mesmo nome.
- **67** idênticas byte a byte.
- **36** variantes de versão: o repositório traz o núcleo LKT System 1.0.0 com
  127 skills (as 103 + 24 novas), e 36 dessas 103 foram reescritas nessa
  versão. Nenhuma skill da Tayannara está ausente.
- As 163 = 127 núcleo + 2 LKT Plus (`atualizar`, `salvar`) + 34 de terceiros.

## 141 de fora do LKT dentro do repositório

| Classificação no inventário local | No repositório | Fora |
|---|---|---|
| Candidata (6) | 6 (3 já estavam; 3 importadas nesta revisão) | 0 |
| Pendente (30) | 28 | 2 (`premiere-pro-mcp`, `edit-premiere-project`: Codex-only, terceiro hetpatel-11; não incorporadas) |
| Não incorporar (105) | 47 | 58 |

As 47 "não incorporar" presentes são, quase todas, plugins Codex guardados
como **referência** em `terceiros/codex/` (32 Vercel, 10 OpenAI runtime /
Google Drive, 1 Supabase), que o instalador não copia; mais 2 do plugin
`cowork-plugin-management` (Apache-2.0, aprovadas pelo PR) e homônimos
(`skill-creator`, `pdf`: mesmo nome, conteúdo e autor diferentes, separados
por namespace `codex/...`).

## Divergências relevantes e motivo

| Divergência | Motivo | Tratamento |
|---|---|---|
| `salvar` e `atualizar` reintroduzidas pelo PR | Foram aposentadas no LKT da Tayannara em 2026-07-26 (push automático; escopo parcial) | Estado `aposentada` no registro; o instalador bloqueia e indica a substituta. Arquivos preservados como histórico |
| Remotion: 12 skills em `terceiros/codex` | Cópia MIT diverge da licença do upstream | Estado `bloqueada` (ver [`../licencas.md`](../licencas.md)) |
| Remotion local (`~/.agents/skills`) ≠ cópia Codex | Duas versões; ambas desatualizadas em relação ao upstream (hashes de pasta diferentes; upstream adicionou `remotion-license`) | Não importadas; decisão aguarda licença |
| 18 skills de terceiros "diferentes" do upstream | Versões anteriores ao HEAD do upstream e adaptação documentada de link `CONNECTORS.md` | Registrado em `estado_upstream: versao_anterior`; atualização é tarefa separada |
| `qa` fora do catálogo antigo da Tayannara | Omissão documental | Resolvido: o catálogo agora é gerado do registro |

## Uso comprovado

Somente evidências acessíveis no histórico local (15 sessões Claude Code, 5
Codex): `design-front-end`, `pagina-e-site` (Claude Code, 2026-09-22);
`remotion-best-practices`, `remotion-create`, `remotion-markup`,
`remotion-render`, `react-best-practices`, `google-drive` (Codex,
2026-10-27); `documents`, `pdf`, `plugin-management` (Codex, até
2026-11-06). Ausência de registro não prova que uma skill não foi usada.
