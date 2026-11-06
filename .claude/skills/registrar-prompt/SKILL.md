---
name: registrar-prompt
description: >
  Gera o próximo ID sequencial de prompt (P0001, P0002...), cria o
  arquivo em prompts/arquivo/ a partir do template, atualiza
  prompts/REGISTRO.md e registra o resultado/handoff ao final da
  execução. Use para todo prompt operacional relevante — não para
  conversa banal ou pergunta simples.
---

# registrar-prompt — Registro numerado de prompts operacionais

## Quando usar

Prompt que inicia ou avança um trabalho operacional relevante: mudança
estrutural, projeto novo, decisão registrada, entrega de cliente,
atualização do template mestre.

## Quando não usar

- Pergunta simples ou conversa que não gera trabalho rastreável.
- Continuação imediata do mesmo prompt já numerado (usar o mesmo ID,
  atualizar o resultado, não criar um novo).

## Entradas

Objetivo do prompt, projeto/cliente, tipo de tarefa, ambiente de
execução.

## Dependências

`prompts/REGISTRO.md`, `prompts/TEMPLATE.md`.

## Contexto que deve ser carregado

`prompts/REGISTRO.md` (último ID usado, pra nunca reutilizar nem
renumerar).

---

## Workflow

### Passo 1 — Determinar o próximo ID

Ler o último ID em `prompts/REGISTRO.md` e incrementar
(`P0001` → `P0002` ...). Nunca reutilizar ou renumerar um ID existente,
mesmo que o prompt anterior tenha sido cancelado ou tenha falhado.

### Passo 2 — Criar o arquivo

`prompts/arquivo/P####-nome-curto.md`, a partir de `prompts/TEMPLATE.md`,
com frontmatter:

```
---
id: P####
data:
projeto:
cliente:
tipo:
ambiente:
status:
---
```

Preencher: objetivo, contexto, instrução, skills, ambiente recomendado,
arquivos, resultado esperado, critérios de conclusão, restrições.

### Passo 3 — Executar e registrar o resultado

Ao final da execução, completar no mesmo arquivo: resultado real,
arquivos alterados, commit/PR/deploy (se houver), próximo prompt
relacionado (se já souber).

### Passo 4 — Atualizar o índice

Adicionar uma linha em `prompts/REGISTRO.md`:

```
ID | Data | Projeto | Tipo | Ambiente | Status | Resultado
```

## Saídas

Arquivo `prompts/arquivo/P####-nome-curto.md` completo e linha
correspondente em `prompts/REGISTRO.md`.

## Caminho de salvamento

`prompts/arquivo/` (arquivo individual), `prompts/REGISTRO.md` (índice).

## Regras

- Nunca renumerar nem reutilizar um ID, mesmo de prompt cancelado.
- Nunca registrar conversa banal como prompt.
- Todo prompt registrado tem status atualizado ao final (não fica
  pendente sem necessidade).

## Critérios de qualidade

Qualquer prompt registrado é encontrável só pelo ID, com contexto
suficiente pra retomar sem reler a conversa original.

## Critérios de validação

`prompts/REGISTRO.md` não tem ID duplicado nem lacuna inexplicada na
sequência.

## Limitações

Registro manual por skill, não automático a cada mensagem — depende do
critério de "prompt relevante" (ver Quando usar).

## Contrato de handoff

Recebe de `rotear-ambiente` (quando a tarefa envolve troca de ambiente,
o handoff entra no mesmo arquivo do prompt).

## Exemplos de gatilhos positivos

- Início de uma atualização estrutural no template mestre.
- "Registra esse prompt" / "qual foi o número desse prompt mesmo".

## Exemplos de gatilhos negativos

- "Oi, tudo bem?" ou pergunta sem trabalho associado.
- Segunda mensagem do mesmo prompt já em andamento.
