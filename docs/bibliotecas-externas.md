# Bibliotecas externas, fonte integral

As bibliotecas abaixo sao vinculadas por submodulos Git, e nao reescritas. Isso preserva arquivos auxiliares, historico de origem, licencas e atualizacoes independentes. Nao confundir vinculo com instalacao automatica das skills no Claude Code.

| Biblioteca | Fonte | Ref fixada | Tipo |
| --- | --- | --- | --- |
| kursku/skills | https://github.com/kursku/skills | `346c313fd2ec241a088c68274da26c538422568b` (`master`) | Colecao de skills e materiais auxiliares. A origem possui licencas variadas por pasta; verificar individualmente antes de redistribuir. |
| obra/superpowers | https://github.com/obra/superpowers | `22f0b463e7a5e579904dd6211a520321035526f7` (`main`) | Skills de desenvolvimento, licenca MIT. |

## Clonar a biblioteca completa

```bash
git clone --recurse-submodules https://github.com/caio090/skill-LKT.git
# Apos realizar o merge desta branch na principal:
cd skill-LKT
git submodule update --init --recursive
```

Enquanto a migracao estiver so na branch `feat/importar-skills-lkt-completas`, use `git clone --branch feat/importar-skills-lkt-completas --recurse-submodules https://github.com/caio090/skill-LKT.git`.

**Importante:** bibliotecas ficam em `vendor/` e **nao sao skills ativas automaticamente**. O instalador futuro deve selecionar quais copiar/instalar em `.claude/skills/` por projeto e preservar cada licenca. Nao instalar indiscriminadamente milhares de skills.
