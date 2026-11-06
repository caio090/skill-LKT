# AGENTS.md

Instruções de operação do REC OS, no formato padrão `AGENTS.md` para
ferramentas de agente que não leem `CLAUDE.md`. Este arquivo é um resumo
equivalente — a fonte completa e mais detalhada é [`CLAUDE.md`](CLAUDE.md).

## Regras essenciais

- Ler `_memoria/empresa.md`, `_memoria/preferencias.md` e
  `_memoria/estrategia.md` antes de qualquer resposta ou decisão.
- Antes de qualquer tarefa, checar se existe skill relevante em
  `.claude/skills/` e segui-la.
- Para páginas, sites, landing pages, dashboards ou interfaces, encadear
  obrigatoriamente `pagina-e-site` → `design-front-end` →
  `texto-natural-pt-br`.
- Para qualquer texto voltado ao público final, aplicar
  `texto-natural-pt-br` ao final.
- Nunca alterar arquivos originais recebidos em `arquivos/entrada/`.
- Nunca misturar contexto de um cliente com a memória geral da empresa.
- Nunca copiar `lkt-plus/` ou `MazyOS/` para dentro do REC OS sem antes
  explicar origem, função, destino, conflitos e dependências.
- Depois de qualquer alteração estrutural, rodar `tools/validar.js`.

## Estrutura de referência

`modules/` (áreas de atuação) · `templates/` (ponto de partida por tipo de
negócio) · `.claude/skills/` (skills do sistema) · `arquivos/` (central de
arquivos: entrada, processados, biblioteca) · `_memoria/` (memória do
sistema) · `docs/` (manifesto, catálogo de skills, roteamento) · `tools/`
(scripts de validação).

Ver [`CLAUDE.md`](CLAUDE.md) para o detalhamento completo de cada regra.
