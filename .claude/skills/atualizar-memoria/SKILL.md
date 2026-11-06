---
name: atualizar-memoria
description: >
  Varre o projeto e compara com os 13 arquivos de _memoria/ (empresa,
  preferências, estratégia, marca, produtos-e-servicos, processos,
  ferramentas, equipe, métricas, decisões, aprendizados, pendências) e com
  docs/catalogo-skills.md e docs/roteamento.md, propondo atualizações
  quando algo ficou desatualizado em relação ao estado real do workspace.
  Use quando o usuário disser "atualiza a memória", "varre o projeto",
  "atualiza o catálogo", ou pedir uma reconciliação geral.
---

# atualizar-memoria — Varredura e atualização de contexto

Substitui a antiga skill `atualizar` (que só cobria 3 arquivos de
memória). Compara o que está registrado com o estado real do workspace e
propõe atualizações — nunca aplica sem aprovação.

## Quando usar

- Periodicamente, ou quando o usuário desconfiar que a memória está
  desatualizada.
- Depois de criar/adaptar/remover skills (pra manter catálogo e
  roteamento coerentes).
- Depois de fechar um cliente ou projeto novo (pra conferir se a memória
  geral reflete isso, sem duplicar o que já está em
  `workspaces/clientes/<cliente>/`).

## Quando não usar

- Para registrar uma correção pontual que acabou de acontecer na
  conversa — isso é feito na hora, direto no arquivo relevante (regra de
  "Aprender com correções" do `CLAUDE.md`), sem precisar rodar essa
  varredura inteira.

## Entradas

Nenhuma — opera sobre o estado atual do workspace.

## Dependências

- Os 13 arquivos de `_memoria/`.
- `docs/catalogo-skills.md`, `docs/roteamento.md`.
- `.claude/skills/` (lista real de skills existentes).
- `workspaces/clientes/`, `workspaces/projetos-internos/` (pra conferir se há cliente/projeto
  não refletido em lugar nenhum).

## Contexto que deve ser carregado

Todos os arquivos de `_memoria/` listados acima.

---

## Workflow

### Passo 1 — Levantamento

Listar:
- Skills reais em `.claude/skills/` (nome de cada pasta).
- Clientes reais em `workspaces/clientes/` e projetos internos em
  `workspaces/projetos-internos/`.
- Arquivos recentes (últimos 30 dias) em `arquivos/processados/`,
  `arquivos/biblioteca/`, e nas pastas de projeto ativas.

### Passo 2 — Comparação

Pra cada arquivo de `_memoria/`, checar se ainda bate com a realidade:

- **`empresa.md`:** serviços, ferramentas, equipe — batem com o que
  apareceu no workspace?
- **`estrategia.md`:** foco atual, prazos — ainda fazem sentido pela
  data de hoje?
- **`marca.md`:** coerente com o que foi gerado nas últimas peças
  visuais?
- **`produtos-e-servicos.md`, `processos.md`, `ferramentas.md`,
  `equipe.md`, `metricas.md`:** cada um reflete o que já foi mencionado
  em sessões recentes?
- **`decisoes.md`, `aprendizados.md`, `pendencias.md`:** alguma pendência
  já foi resolvida e não foi marcada? Alguma decisão recente ainda não
  foi registrada?
- **`docs/catalogo-skills.md`:** lista todas as skills que existem de
  fato em `.claude/skills/`? Alguma skill removida ainda aparece lá?
- **`docs/roteamento.md`:** as skills citadas em cada linha ainda
  existem com esse nome?

### Passo 3 — Proposta de mudanças

Apresentar uma lista curta:

```
Encontrei [N] coisas pra atualizar:

1. _memoria/empresa.md — falta o cliente "Acme" (vi pasta
   workspaces/clientes/acme/ criada em [data])
2. docs/catalogo-skills.md — lista a skill "salvar", que não existe
   mais (foi substituída por "salvar-local")
3. _memoria/estrategia.md — fala em "fechar 1º cliente em fevereiro",
   já é [data atual] e tem [N] clientes ativos

Quer que eu aplique essas mudanças? Posso aplicar todas, escolher
algumas, ou nenhuma.
```

### Passo 4 — Aplicação

Se aprovado, editar com cirurgia — só a linha relevante, sem reformatar o
documento inteiro. Mostrar o diff de cada mudança aplicada.

---

## Saídas

Arquivos de _memoria/ e docs/catalogo-skills.md/roteamento.md atualizados, com diff mostrado antes de aplicar.

## Critérios de qualidade

- Toda mudança proposta é aprovada explicitamente antes de ser aplicada.
- Nenhuma edição reformata um arquivo inteiro — só adiciona/corrige a linha relevante.

## Regras

- Não inventar fatos — só registrar o que tem evidência no workspace.
- Se a evidência for ambígua, perguntar antes de adicionar.
- Não apagar conteúdo dos arquivos de contexto — só atualizar e
  adicionar (remoção explícita só se o usuário confirmar que algo não
  existe mais).
- Se nenhuma mudança for necessária, responder "Tá tudo coerente, nada
  pra atualizar".
- Nunca misturar memória de um cliente específico dentro dos arquivos
  gerais de `_memoria/` — se encontrar isso, sinalizar como problema a
  corrigir, não como atualização normal.

## Critérios de validação

- Depois de rodar, `docs/catalogo-skills.md` lista exatamente as skills
  que existem em `.claude/skills/` — nem mais, nem menos.
- Nenhuma edição aplicada sem aprovação explícita do usuário.

## Limitações

- Não decide sozinha se uma informação é "geral da empresa" ou
  "específica de cliente" quando ambíguo — pergunta.
- Não roda validação estrutural completa (YAML, links) — isso é
  `validar-sistema`; as duas podem ser usadas em sequência.

## Caminho de salvamento

Edita os arquivos existentes em `_memoria/` e `docs/` — não cria arquivo
novo.

## Contrato de handoff

Depois de atualizar, pode encadear com `validar-sistema` pra confirmar
que nada ficou quebrado, ou com `salvar-local` pra fechar a sessão.

## Exemplos de gatilhos positivos

- "Atualiza a memória"
- "Varre o projeto"
- "Atualiza o catálogo de skills"

## Exemplos de gatilhos negativos

- Correção pontual de uma frase específica na conversa (aplicar direto,
  sem rodar a varredura inteira)
- "Valida o sistema" (é `validar-sistema`)
