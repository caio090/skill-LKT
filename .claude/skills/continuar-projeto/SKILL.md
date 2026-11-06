---
name: continuar-projeto
description: >
  Lê a memória, as decisões, as pendências e os arquivos recentes de um
  workspace ou projeto, e informa o próximo passo — sem repetir
  perguntas já respondidas. Use no início de uma sessão quando o
  usuário disser "continua o projeto X", "retoma de onde parei", "cadê
  a gente", ou ao reabrir um workspace já existente.
---

# continuar-projeto — Retomar sem perguntar tudo de novo

Lê o estado salvo de um workspace/projeto e resume onde ele parou, o
que já foi decidido, o que está pendente, e qual é o próximo passo —
para o usuário não precisar recontar o contexto.

## Quando usar

- Início de sessão em um workspace/projeto que já existe.
- Usuário pede explicitamente para retomar ou continuar.

## Quando não usar

- Para criar um workspace/projeto novo (isso é `novo-projeto`).
- Quando o contexto já está claro na conversa atual (não precisa
  relatório formal a cada mensagem).

## Entradas

- Nome ou slug do workspace/projeto (se ambíguo, perguntar qual).

## Dependências

- `.lkt-system/estado/contexto-ativo.json`
- `_memoria.json` e `WORKSPACE.txt` do workspace
- `PROJETO.md` do projeto
- `_memoria/decisoes/decisoes.md`, `_memoria/aprendizados/aprendizados.md`
- `INDICE.txt`/`INDICE.md` do workspace

## Contexto que deve ser carregado

- Tudo listado em Dependências, mais `_memoria/sistema/` geral.

---

## Workflow

### Passo 1 — Localizar o workspace/projeto

Se não vier explícito, usar `workspace_ativo`/`projeto_ativo` de
`.lkt-system/estado/contexto-ativo.json`. Se não houver nenhum ativo e o
usuário não especificar, perguntar qual.

### Passo 2 — Ler o estado

- `WORKSPACE.txt` / `PROJETO.md` — objetivo, responsável, prazo,
  indicador, estado atual.
- `_memoria.json` — decisões, hipóteses, pendências, riscos recentes.
- `_memoria/decisoes/decisoes.md` e `_memoria/aprendizados/aprendizados.md`
  — o que foi decidido e aprendido que afeta este workspace.
- Arquivos recentes em `arquivos_recentes` do contexto ativo.
- `INDICE.txt`/`INDICE.md` — o que já foi entregue.

### Passo 3 — Resumir

```
<Nome do workspace/projeto> — estado: <estado atual>

O que já foi feito:
- ...

Decisões recentes:
- ...

Pendências:
- ...

Próximo passo recomendado: <com base no estado e no que falta>
```

### Passo 4 — Atualizar contexto ativo

Atualizar `workspace_ativo`/`projeto_ativo` em
`.lkt-system/estado/contexto-ativo.json` se mudou desde a última sessão.

---

## Saídas

Resumo do estado atual do workspace/projeto e recomendação de próximo
passo, sem repetir perguntas já respondidas em sessões anteriores.

## Regras

- Nunca perguntar de novo algo que já está registrado em memória —
  usar o que existe.
- Nunca inventar progresso que não está registrado.

## Critérios de qualidade

- Resumo cobre: estado, feito, decisões recentes, pendências, próximo
  passo.

## Critérios de validação

- Contexto ativo atualizado ao final, se mudou.

## Limitações

- Não executa nenhuma ação por conta própria — só informa e recomenda.
- Se a memória estiver vazia ou incompleta, avisa explicitamente em vez
  de preencher lacuna com suposição.

## Caminho de salvamento

Não gera arquivo novo por padrão (só lê e resume). Se o usuário pedir
para registrar o resumo, salvar em
`workspaces/<tipo>/<slug>/[projetos/<projeto>/]09-relatorios/`.

## Contrato de handoff

Encaminha para a skill do próximo passo recomendado (diagnóstico,
proposta, produção do módulo correspondente, etc.).

## Exemplos de gatilhos positivos

- "Continua o projeto X"
- "Retoma de onde parei"
- "Cadê a gente com o cliente Y?"

## Exemplos de gatilhos negativos

- "Cria um projeto novo pra Z" (é `novo-projeto`, não continuação)
