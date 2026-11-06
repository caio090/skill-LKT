# Skills do Codex (OpenAI)

Biblioteca de skills e plugins do Codex com licença aberta, copiados do
computador de trabalho em 2026-11-06. Ficam fora de `.claude/skills/` de
propósito: foram escritos para o Codex e o Claude Code não carrega esta
pasta sozinho. Para usar uma delas num projeto, copiar a pasta da skill
para `.claude/skills/` (Claude Code) ou `.agents/skills/` (Codex) e revisar
as referências a ferramentas próprias do Codex.

## `plugins/` (plugin inteiro, estrutura preservada)

| Plugin | Versão | Skills | Licença | Área no LKT |
|---|---|---|---|---|
| `remotion` | 4.0.534 | 12 | MIT (arquivo `LICENSE`) | Vídeo programático, social |
| `vercel` | 0.54.1 | 33 | Apache-2.0 (declarada no `plugin.json`) | Publicar sites e landing pages |
| `supabase` | 1.0.0 | 2 | MIT (arquivo `LICENSE`) | Banco de dados de apps |
| `google-drive` | 0.1.22 | 5 | MIT (declarada no `plugin.json`) | Docs, planilhas, slides no Drive |
| `documents` | 26.818.11542 | 1 | MIT (declarada no `plugin.json`) | Documentos Word |
| `presentations` | 26.818.11542 | 1 | MIT (declarada no `plugin.json`) | Apresentações |
| `spreadsheets` | 26.818.11542 | 2 | MIT (declarada no `plugin.json`) | Planilhas |
| `pdf` | 26.818.11542 | 1 | MIT (declarada no `plugin.json`) | PDF |
| `samautomation-workflows` | 1.0.0 | 1 | MIT (arquivo `LICENSE`) | Revisão de fluxos n8n |

`documents`, `presentations`, `spreadsheets` e `pdf` são a alternativa de
licença aberta às skills `docx`/`pptx`/`xlsx`/`pdf` da Anthropic, que são
proprietárias e não podem ir para este repositório.

## `skills/` (skills avulsas do catálogo padrão openai/skills)

Todas com arquivo de licença na pasta (Apache-2.0; `vercel-deploy` é MIT):

`chatgpt-apps` · `cli-creator` · `cloudflare-deploy` · `define-goal` ·
`gh-fix-ci` · `hatch-pet` · `jupyter-notebook` · `netlify-deploy` ·
`openai-docs` · `pdf` · `playwright` · `playwright-interactive` ·
`render-deploy` · `screenshot` · `security-best-practices` ·
`security-ownership-map` · `security-threat-model` · `sentry` · `speech` ·
`transcribe` · `vercel-deploy` · `yeet`

O que ficou de fora e por quê está em
[`../../docs/skills-terceiros.md`](../../docs/skills-terceiros.md).
