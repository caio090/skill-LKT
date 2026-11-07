# Skills do Codex (OpenAI)

Biblioteca de skills e plugins do Codex com licença declarada como aberta (ver estado de cada um abaixo), copiados do
computador de trabalho em 2026-11-06. Ficam fora de `.claude/skills/` de
propósito: foram escritos para o Codex e o Claude Code não carrega esta
pasta sozinho. No Codex, instale o plugin pelo marketplace oficial. Copiar
uma skill daqui para um projeto só é permitido quando o estado dela em
`registry/skills.json` não for `bloqueada` ou `pendente`; nesse caso,
revisar as referências a ferramentas próprias do Codex.

## `plugins/` (plugin inteiro, estrutura preservada)

| Plugin | Versão | Skills | Licença (verificação de 2026-11-06) | Estado no registro | Área no LKT |
|---|---|---|---|---|---|
| `remotion` | 4.0.534 | 12 | Cópia traz LICENSE MIT, mas o upstream `remotion-dev/remotion` usa a Remotion License e `packages/codex-plugin` não tem LICENSE | **bloqueada** | Vídeo programático, social |
| `vercel` | 0.54.1 | 33 | Apache-2.0 conferido em `vercel/vercel-plugin`; `LICENSE` adicionado | referência | Publicar sites e landing pages |
| `supabase` | 1.0.0 | 2 | Cópia traz LICENSE MIT; upstream `supabase-community/supabase-plugin` sem LICENSE | pendente | Banco de dados de apps |
| `google-drive` | 0.1.22 | 5 | MIT só no `plugin.json`; `openai/plugins` sem LICENSE | pendente | Docs, planilhas, slides no Drive |
| `documents` | 26.818.11542 | 1 | MIT no `plugin.json` + LICENSE.txt; origem privada | pendente | Documentos Word |
| `presentations` | 26.818.11542 | 1 | MIT só no `plugin.json`; origem privada | pendente | Apresentações |
| `spreadsheets` | 26.818.11542 | 2 | MIT só no `plugin.json`; origem privada | pendente | Planilhas |
| `pdf` | 26.818.11542 | 1 | MIT só no `plugin.json`; origem privada | pendente | PDF |
| `samautomation-workflows` | 1.0.0 | 1 | MIT conferido em `smrht/samautomation-workflows` | referência (cópia aprovada em `.claude/skills/n8n-workflow-check`) | Revisão de fluxos n8n |

O instalador não copia nada desta pasta. Detalhes em
[`../../docs/licencas.md`](../../docs/licencas.md).

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
