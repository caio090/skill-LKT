# LKT System

Biblioteca central de skills da Lokat para Claude Code e Codex: estratégia,
marketing, conteúdo, páginas e lojas, tecnologia, automação, financeiro,
food service e audiovisual. Cada projeto instala **só o que precisa**; esta
biblioteca é a fonte de atualização e auditoria.

- **Biblioteca central** (este repositório): skills, registro de origem e
  licença, instalador, testes.
- **Projeto consumidor** (site, loja, app, cliente): recebe uma seleção de
  skills em `.claude/skills/` (ou `.agents/skills/` no Codex), com o
  manifesto `.lkt/instalacao.json`. Identidade, regras, contexto e segredos
  do projeto ficam no projeto.

## Começar em 5 minutos

```bash
git clone https://github.com/caio090/skill-LKT.git && cd skill-LKT

# 1. Ver perfis e skills disponíveis
python3 tools/instalar_lkt.py --list

# 2. Simular a instalação num projeto (não escreve nada)
python3 tools/instalar_lkt.py --project ../meu-projeto --profile web

# 3. Aplicar
python3 tools/instalar_lkt.py --project ../meu-projeto --profile web --apply

# 4. Depois, no projeto: commitar .claude/skills/ e .lkt/instalacao.json
```

Perfis: `base`, `web`, `app`, `ecommerce`, `marketing`, `audiovisual`,
`automacao`, `operacao`, `dados`, `cliente-local` ([`registry/perfis.json`](registry/perfis.json)).
Somar ou tirar skills: `--include nome` / `--exclude nome`. Codex: `--runtime codex`.

## Atualizar, verificar e reverter

```bash
python3 tools/instalar_lkt.py --project ../meu-projeto --check            # o que mudou, sem escrever
python3 tools/instalar_lkt.py --project ../meu-projeto --update --apply   # atualiza o que não foi editado
python3 tools/instalar_lkt.py --project ../meu-projeto --rollback --apply # desfaz a última operação
python3 tools/instalar_lkt.py --project ../meu-projeto --uninstall seo --apply
```

O instalador nunca sobrescreve uma skill editada no projeto nem uma pasta
que ele não instalou: reporta `CONFLITO` ou `EXISTENTE_NAO_GERENCIADA`.

## Descobrir uma skill

- [`docs/catalogo-skills.md`](docs/catalogo-skills.md): catálogo por
  categoria, gerado do registro.
- [`registry/skills.json`](registry/skills.json): origem, licença, versão,
  hash, estado, dependências e ambientes de cada skill.
- [`docs/roteamento.md`](docs/roteamento.md): qual skill usar e precedência
  quando duas se sobrepõem.

Estados: `aprovada` (instalável) · `pendente` · `bloqueada` · `referencia`
· `aposentada`. Só `aprovada` é instalada.

## Adicionar uma skill

**Autoral:** criar `.claude/skills/<nome-em-kebab-case>/SKILL.md` com
`name` e `description`; incluir o nome numa categoria de
[`registry/fontes.json`](registry/fontes.json); rodar:

```bash
python3 tools/registro.py build && python3 tools/registro.py catalogo
node tools/validar.js
```

**De terceiros:** seguir [`docs/licencas.md`](docs/licencas.md) (licença
conferida no repositório oficial, arquivo LICENSE junto, origem e commit
em `registry/fontes.json`). Sem licença redistribuível, a skill fica como
referência externa.

Não commitar `.env`, dados de clientes, tabelas de preço internas,
históricos de sessão ou dumps. Ver [`docs/sandbox.md`](docs/sandbox.md).

## Testes

```bash
node tools/validar.js                       # estrutura, links, registro e catálogo
python3 -m unittest discover -s tests -v    # instalador (projetos descartáveis, sem rede)
node --test tests/*.test.js                 # parser de links e exemplo de e-commerce
```

O modelo de CI ([`docs/ci/validar.yml`](docs/ci/validar.yml)) roda
os três em cada PR. Não faz deploy nem merge. Para ativar, copie o arquivo
para `.github/workflows/validar.yml` pela interface do GitHub ou com uma
credencial que tenha o escopo `workflow`.

## Ambientes

Claude Code e Codex recebem skills por cópia controlada. ChatGPT não
instala skills locais. Detalhes em [`docs/compatibilidade.md`](docs/compatibilidade.md).

## Estrutura

| Pasta | Conteúdo |
|---|---|
| `.claude/skills/` | Skills aprovadas (e as aposentadas/pendentes, marcadas no registro) |
| `registry/` | `fontes.json` (curadoria), `skills.json` (gerado), schema, perfis |
| `terceiros/codex/` | Plugins e skills do Codex como referência; não instalados pelo instalador |
| `vendor/` | Submódulos de referência (superpowers, kursku/skills, Dify); não copiados |
| `tools/` | `instalar_lkt.py`, `registro.py`, `validar.js` |
| `tests/` | Testes do instalador, do parser de links e dos exemplos |
| `docs/` | Licenças, compatibilidade, roteamento, sandbox, auditorias |
| `_memoria/`, `arquivos/` | Modelos vazios de memória e central de arquivos (sem dados reais) |

Regras de operação do agente: [`CLAUDE.md`](CLAUDE.md) (resumo em [`AGENTS.md`](AGENTS.md)).

## FAQ

- **`ERRO: projeto inexistente`**: o caminho de `--project` precisa existir.
- **`informe um projeto existente fora da biblioteca`**: não instale dentro
  do próprio `skill-LKT`.
- **`AUSENTE`**: nome errado, skill só de referência, ou submódulo não
  baixado (`git submodule update --init` se precisar consultar `vendor/`).
- **`BLOQUEADA`**: estado não aprovado no registro; a mensagem indica a
  substituta quando existe.
- **`CONFLITO`**: a skill foi editada no projeto. Revise à mão; o
  instalador não sobrescreve.
- **Permissão negada**: rode como o usuário dono do projeto. O instalador
  não pede elevação de privilégio.

## Histórico do nome

Este sistema já se chamou **REC OS** e teve duas instalações anteriores,
**LKT Plus** e **MazyOS**. O nome canônico é **LKT System**. A genealogia e
as mudanças de comportamento estão em [`docs/MIGRACAO.md`](docs/MIGRACAO.md)
e [`CHANGELOG.md`](CHANGELOG.md).
