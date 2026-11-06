---
name: gerar-escopo-por-nivel
description: >
  Monta o escopo interno completo de um projeto a partir de um nível
  recomendado e seu perfil de entrega, separando obrigatório,
  recomendado, opcional, futuro e não incluso. Uso interno — a versão
  para o cliente é gerada por gerar-proposta-a-partir-do-nivel. Use
  quando o usuário disser "monta o escopo completo pra esse nível",
  ou depois de gerar-plano-de-avanco.
---

# gerar-escopo-por-nivel — Escopo interno completo, por camada

Monta o escopo interno (uso da equipe, não do cliente) a partir de um
`deliverable-profile` ligado ao nível recomendado. Ver
`schemas/deliverable-profile.schema.json` e
`knowledge/niveis/NIVEIS_E_PROPOSTAS.md`.

## Quando usar

- Depois de `recomendar-nivel`/`gerar-plano-de-avanco`, para formalizar
  o escopo interno completo antes de traduzir pra proposta comercial.

## Quando não usar

- Para gerar o material que vai para o cliente (isso é
  `gerar-proposta-a-partir-do-nivel`, que consome a saída desta skill).

## Entradas

- `level-recommendation` e/ou `level-definition` do nível-alvo.
- `deliverable-profile` correspondente (`catalogo/perfis-de-entrega/`),
  se já existir — senão, montar um novo a partir da
  `level-definition` (entregáveis mínimos/opcionais/não inclusos).

## Dependências

- `schemas/deliverable-profile.schema.json`
- `catalogo/perfis-de-entrega/`
- `.claude/skills/recomendar-nivel`, `.claude/skills/gerar-plano-de-avanco`

## Contexto que deve ser carregado

- `level-recommendation` de origem.
- Plano de avanço, se já gerado.

---

## Workflow

### Passo 1 — Localizar ou montar o perfil de entrega

Checar `catalogo/perfis-de-entrega/` por um perfil já ligado a esse
`level_definition_id`. Se não existir, montar um novo a partir de
`entregaveis_minimos`/`entregaveis_opcionais`/`itens_nao_inclusos` da
`level-definition`.

### Passo 2 — Separar em camadas

- **Obrigatório** — sem isso o nível não é atingido.
- **Recomendado** — reforça o resultado, não é bloqueante.
- **Opcional** — nice-to-have, decisão do cliente/prioridade.
- **Futuro** — pertence a um nível seguinte, registrado mas fora do
  escopo atual.
- **Não incluso** — explicitamente fora, evita expectativa errada.

### Passo 3 — Cruzar com o plano de avanço

Confirmar que toda ação do plano (`gerar-plano-de-avanco`) aparece em
alguma camada do escopo — nada solto fora do escopo formal.

### Passo 4 — Registrar

Salvar o `deliverable-profile` (novo ou atualizado) em
`catalogo/perfis-de-entrega/` quando for reutilizável, e o escopo
aplicado ao projeto em `02-modelagem/`.

---

## Saídas

Escopo interno completo (obrigatório/recomendado/opcional/futuro/não
incluso), rastreável ao nível e ao plano de avanço.

## Regras

- Toda camada do perfil precisa estar presente, mesmo que vazia
  (declarar "nenhum item opcional neste caso", por exemplo — não
  omitir a camada).
- "Não incluso" é sempre explícito — nunca implícito.

## Critérios de qualidade

- Todo item do plano de avanço aparece em exatamente uma camada do
  escopo.

## Critérios de validação

- `deliverable-profile` válido contra
  `schemas/deliverable-profile.schema.json`.

## Limitações

- Não decide preço — isso é `proposta-e-precificacao`.
- Não é a versão para o cliente — isso é
  `gerar-proposta-a-partir-do-nivel`.

## Caminho de salvamento

`workspaces/<tipo>/<slug>/[projetos/<projeto>/]02-modelagem/ESCOPO-POR-NIVEL-<dimensao>.md`
+ `catalogo/perfis-de-entrega/<slug>.json` (quando reutilizável).

## Contrato de handoff

Recebe de `recomendar-nivel`/`gerar-plano-de-avanco`. Encaminha para
`gerar-proposta-a-partir-do-nivel` (tradução comercial) e
`proposta-e-precificacao` (preço final).

## Exemplos de gatilhos positivos

- "Monta o escopo completo pra esse nível"
- "Separa o que é obrigatório do que é opcional nesse projeto"

## Exemplos de gatilhos negativos

- "Gera a proposta pro cliente" (é `gerar-proposta-a-partir-do-nivel`,
  consome a saída desta skill)

Arquivos de apoio: `perguntas.txt`, `fluxo.md`, `saidas.md`,
`validacao.md`, `exemplos.md`.
