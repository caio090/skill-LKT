# Licenças e proveniência

Este repositório é **público**. Cada diretório tem um regime de licença
próprio; não existe licença global que valha para tudo.

| Diretório | Conteúdo | Licença |
|---|---|---|
| `.claude/skills/<skill>` com `origem_tipo: autoral` | Skills escritas pela Lokat (LKT System, LKT Plus) | **Não definida.** O repositório não tem `LICENSE` na raiz. Até o dono decidir, o conteúdo autoral é "todos os direitos reservados" por padrão, mesmo estando público. |
| `.claude/skills/<skill>` com `origem_tipo: externa` | Skills de terceiros | A do autor original, com o arquivo `LICENSE`/`LICENSE.txt` dentro da pasta da skill |
| `terceiros/codex/` | Plugins e skills do Codex guardados como referência | A de cada plugin/skill; ver estado em `registry/skills.json` |
| `vendor/` | Submódulos Git (não copiados) | A de cada projeto de origem: `obra/superpowers` MIT; `kursku/skills` **sem licença**; `langgenius/dify` licença própria (Dify Open Source License). Só são lidos como referência; o instalador não copia nada daqui. |
| `tools/`, `tests/`, `registry/`, `docs/` | Ferramentas e documentação da Lokat | Mesmo regime do conteúdo autoral |

## Regras para admitir skill de terceiros

1. Licença conferida **no repositório oficial**, na versão copiada (arquivo
   `LICENSE` do projeto ou da pasta da skill). Declaração em
   `plugin.json` sem texto de licença não basta para estado `aprovada`.
2. Só entram licenças que permitem redistribuição (MIT, Apache-2.0, BSD,
   ISC). Sem licença = sem cópia: fica como referência externa.
3. O arquivo de licença original vai junto, dentro da pasta da skill.
   Créditos, cabeçalhos e `NOTICE` (Apache-2.0) são preservados.
4. A origem (repositório + commit ou versão) é registrada em
   `registry/fontes.json`. Adaptações locais também (ex.: link
   `../../CONNECTORS.md` → `CONNECTORS.md` nos plugins Anthropic).
5. Licença da skill **não** autoriza o uso comercial do software que ela
   opera. Ex.: as instruções de Remotion podem ser MIT e o framework
   Remotion exigir licença de empresa.
6. Conteúdo proprietário (skills `docx`/`pptx`/`xlsx`/`pdf` da Anthropic,
   plugins `Proprietary` da OpenAI) nunca é copiado.
7. Nenhuma skill externa é reescrita como autoria LKT.

## Estado das pendências de licença (2026-11-06)

| Item | Situação | Estado no registro | O que falta |
|---|---|---|---|
| `terceiros/codex/plugins/remotion` (12) | Cópia traz LICENSE MIT; upstream `remotion-dev/remotion` usa a *Remotion License*; `packages/codex-plugin` sem LICENSE; `remotion-dev/skills` sem licença | **bloqueada** | Confirmação escrita da Remotion sobre a licença das skills; decisão humana se a pasta continua no repositório público. Uso comercial do framework exige avaliação separada pela licença vigente. |
| `terceiros/codex/plugins/supabase` (2) | Cópia traz LICENSE MIT; upstream `supabase-community/supabase-plugin` sem LICENSE | pendente | Confirmar com a Supabase. A skill `supabase-postgres-best-practices` aprovada em `.claude/skills` vem de outro repositório (`supabase/agent-skills`, MIT). |
| `terceiros/codex/plugins/google-drive` (5) | `plugin.json` declara MIT; `openai/plugins` sem LICENSE | pendente | Texto de licença oficial |
| `terceiros/codex/plugins/{documents,pdf,presentations,spreadsheets}` (5) | `plugin.json` declara MIT; origem privada (`openai/openai`) | pendente | Impossível conferir fonte; decidir se ficam |
| `terceiros/codex/plugins/vercel` (33) | Apache-2.0 conferido no upstream `vercel/vercel-plugin`; LICENSE adicionado nesta revisão | referência | — |
| `react-best-practices` | Vem de `vercel/vercel-plugin` (Apache-2.0). A cópia é versão anterior ao upstream atual. Não foi copiada para `.claude/skills` | referência | Se for promovida, copiar do upstream atual com LICENSE |
| Raiz do repositório | Sem `LICENSE` | — | **Decisão do dono**: escolher licença para o conteúdo autoral (ou manter fechado e tornar o repositório privado) |

Esta página não é parecer jurídico. Casos de dúvida vão para revisão
humana antes de qualquer redistribuição.

## Como auditar

```
python3 tools/registro.py check      # estado, licença e arquivo LICENSE por skill
node tools/validar.js                # estrutura, links e registro
```

Skill externa `aprovada` sem arquivo de licença na pasta, ou com licença
`nao_verificado`, reprova o `check`.
