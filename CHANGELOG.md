# Changelog

## [não lançado] — 2026-11-06, branch `feat/importar-skills-lkt-completas`

Versão estável **não** declarada: há itens bloqueados e pendentes (ver
`docs/auditorias/COBERTURA-E-FECHAMENTO-LKT-2026-11-06.md`).

### Adicionado
- Registro canônico: `registry/fontes.json` (curadoria), `registry/skills.json`
  (gerado, com hash do `SKILL.md` e da pasta), `registry/skills.schema.json`,
  `tools/registro.py` (`build`, `check`, `catalogo`).
- Skills: `apple-design` (emilkowalski/skills, MIT),
  `supabase-postgres-best-practices` (supabase/agent-skills, MIT),
  `n8n-workflow-check` (smrht/samautomation-workflows, MIT, promovida de
  `terceiros/codex`).
- Skills autorais: `ecommerce-loja`, `qa-e2e-playwright`, com exemplos e testes.
- Perfis `app`, `ecommerce`, `audiovisual`, `operacao`, `dados`, `cliente-local`.
- Instalador: `--list`, `--exclude`, `--runtime`, `--check`, `--update`,
  `--uninstall`, `--rollback`, `--json`, manifesto `.lkt/instalacao.json`.
- Testes: `tests/test_instalador.py` (18), `tests/links.test.js` (9),
  `tests/link-whatsapp.test.js` (5); CI `.github/workflows/validar.yml`.
- Docs: `licencas.md`, `compatibilidade.md`, `sandbox.md`, `MIGRACAO.md`,
  reconciliação de inventários.
- `terceiros/codex/plugins/vercel/LICENSE` (Apache-2.0 do upstream).

### Alterado
- Nome canônico: LKT System (README, validador).
- `docs/catalogo-skills.md` passa a ser gerado.
- `docs/roteamento.md`: precedência, sobreposições e cenários A–J.
- `tools/validar.js`: parser de links ignora código e esquemas não-arquivo;
  links de terceiros viram aviso; confere registro e catálogo.
- Instalador lê só o registro (ver `docs/MIGRACAO.md`).

### Marcado (sem apagar)
- `salvar`, `atualizar`: aposentadas.
- `terceiros/codex/plugins/remotion`: bloqueada por conflito de licença.
- Plugins Codex `supabase`, `google-drive`, `documents`, `pdf`,
  `presentations`, `spreadsheets`: licença pendente.
