# Compatibilidade por ambiente

O que cada ambiente consegue fazer com a biblioteca LKT. "Formato válido"
significa que a skill tem `SKILL.md` com `name` e `description` no formato
que o runtime lê; não significa que cada skill foi executada naquele
ambiente.

| Ambiente | Como recebe as skills | O que funciona | Limites |
|---|---|---|---|
| **Claude Code** (CLI, desktop, IDE, web) | `tools/instalar_lkt.py --runtime claude` copia para `<projeto>/.claude/skills/`; versionar a pasta no Git do projeto | Carrega `SKILL.md` do projeto; skills aparecem para seleção automática e via `/nome` | Skills em `~/.claude/skills` da máquina **não** vão para Codespaces/nuvem: só o que está commitado no projeto. Skills que pedem ferramentas (Playwright, Python, CLI REA, conta RunComfy) dependem do ambiente ter essas ferramentas |
| **Codex** (CLI/app) | `tools/instalar_lkt.py --runtime codex` copia para `<projeto>/.agents/skills/` | Mesmo formato `SKILL.md` | Não testado skill a skill nesta revisão. Skills que citam ferramentas do Claude (ex.: `WebSearch`, `Skill`) precisam ser lidas como instrução geral. Plugins de `terceiros/codex/` devem ser instalados pelo marketplace do Codex, não copiados |
| **ChatGPT** (web/app) | **Não há instalação local.** Não lê `.claude/skills/` nem `.agents/skills/` | Colar o conteúdo de uma skill como instrução de um projeto/GPT; usar conectores próprios do ChatGPT | Scripts das skills não rodam; nenhuma garantia de comportamento. Não prometer "instalação automática" no ChatGPT |
| **claude.ai** (chat) | Skills da conta e plugins sincronizados pela Anthropic | Skills proprietárias (`docx`, `pptx`, `xlsx`, `pdf`) vêm da conta | Não lê a biblioteca LKT sozinho |

## Dependências e autenticação por skill

Registradas no campo `dependencias` de `registry/skills.json`. As que exigem
algo do usuário:

| Skill | Exige |
|---|---|
| `image-edit`, `nano-banana-2` | Conta RunComfy (autenticação do usuário) |
| `reverse-engineer-anything` | CLI REA |
| `n8n-workflow-check` | Python 3 |
| `web-artifacts-builder` | Node.js |
| `carrossel` | Playwright (render PNG) |
| `qa-e2e-playwright` | `@playwright/test` no projeto (Apache-2.0) |

## Fallback quando a ferramenta não existe

A skill deve dizer que não executou e entregar o artefato como "não
executado" (ex.: testes escritos mas não rodados). Nunca afirmar que
carregou ferramenta ou rodou comando indisponível.

## Caminhos por sistema operacional

O instalador usa `pathlib` e cópia controlada (sem links simbólicos), então
funciona em macOS, Linux e Windows. Testado nesta revisão: macOS (Python
3.9, Node 24). Linux: na CI (`.github/workflows/validar.yml`). Windows: não
testado.
