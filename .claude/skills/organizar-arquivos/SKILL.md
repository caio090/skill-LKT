---
name: organizar-arquivos
description: >
  Analisa um arquivo anexado (documento, planilha, print, áudio, link) e
  indica exatamente em qual pasta ele deve ficar — geral (`arquivos/`)
  ou de um workspace/projeto específico. Preserva sempre o original,
  extrai o conteúdo útil, gera um resumo em TXT quando fizer sentido, e
  atualiza o `INDICE.txt`/`INDICE.md` correspondente. Use quando o
  usuário anexar algo ou perguntar "onde eu coloco isso".
---

# organizar-arquivos — Cada arquivo no lugar certo, sem alterar o original

Recebe um arquivo (ou a descrição de um) e decide onde ele deve ficar,
seguindo `docs/PADRAO_DE_ARQUIVOS.md`. Nunca altera o arquivo original.

## Quando usar

- Usuário anexa um documento, planilha, print, áudio, foto, vídeo ou
  link e pergunta onde colocar ou pede pra já processar.
- Início de um workspace, quando há material histórico pra organizar
  de uma vez.

## Quando não usar

- Para gerar um documento novo (isso é a skill específica do tipo de
  entrega, não esta).

## Entradas

- O arquivo (ou a descrição/local dele).
- Contexto: geral da instalação ou de um workspace/projeto específico.
- Se já existe um workspace ativo (ver `.lkt-system/estado/contexto-ativo.json`).

## Dependências

- `arquivos/INDICE.md` (central geral)
- `workspaces/<tipo>/<slug>/INDICE.txt` (por workspace)
- `docs/PADRAO_DE_ARQUIVOS.md`

## Contexto que deve ser carregado

- Workspace/projeto ativo, se houver.
- Categoria de biblioteca já existente (`marca`, `pesquisa`, `comercial`,
  `financeiro`, `conteudo`, `dados`, `referencias`, `legal`,
  `audiovisual`, `codigo`).

---

## Workflow

### Passo 1 — Identificar o destino

- Sem workspace ativo ou material claramente geral da instalação →
  `arquivos/entrada/`.
- Com workspace ativo → `workspaces/<tipo>/<slug>/00-contexto/entrada/`.

Informar o caminho exato antes de qualquer ação:

> "Coloque o arquivo original em: <caminho completo>"

### Passo 2 — Processar (quando o conteúdo já estiver acessível)

1. Preservar o original, sem alterar.
2. Registrar nome, formato, origem e data.
3. Extrair o conteúdo útil.
4. Criar versão em Markdown ou TXT quando fizer sentido (resumo
   legível).
5. Classificar o material (categoria de biblioteca ou pasta do
   workspace).
6. Mover a versão processada para `arquivos/processados/` (geral) ou
   `00-contexto/resumo/` (workspace).
7. Indicar quais informações devem entrar em `_memoria/sistema/` ou em
   `_memoria.json` do workspace — perguntar antes de gravar.
8. Não inventar informação ausente no arquivo.

### Passo 3 — Atualizar o índice

Atualizar `arquivos/INDICE.md` ou `INDICE.txt` do workspace com: nome,
formato, categoria, data, resumo de uma linha.

---

## Saídas

Arquivo original preservado no lugar certo, versão processada (quando
aplicável) e índice atualizado.

## Regras

- Nunca alterar o arquivo original recebido.
- Nunca colocar entrega ou material de workspace em
  `arquivos/biblioteca/` da raiz.
- Nunca inventar conteúdo que não está no arquivo.

## Critérios de qualidade

- Todo arquivo processado aparece no índice correspondente com data e
  categoria.

## Critérios de validação

- Original intacto (checagem de que não foi sobrescrito).
- Índice atualizado sem duplicar entrada já existente.

## Limitações

- Não decide sozinha se um dado deve virar memória permanente — sempre
  pergunta antes de gravar em `_memoria/`.
- Não converte formato de arquivo (ex.: não transcreve áudio) além do
  que a ferramenta disponível permitir — se não conseguir processar,
  registra o arquivo como pendente de processamento manual.

## Caminho de salvamento

`arquivos/entrada/` ou `processados/` (geral); `workspaces/<tipo>/<slug>/00-contexto/entrada/`
ou `resumo/` (workspace).

## Contrato de handoff

Encaminha para `diagnostico-empresarial` quando o material processado
mudar o entendimento do negócio, ou para o módulo correspondente ao
tipo de conteúdo.

## Exemplos de gatilhos positivos

- "Onde eu coloco esse arquivo?"
- Usuário anexa um documento sem instrução explícita

## Exemplos de gatilhos negativos

- "Cria um relatório novo" (gera documento, não organiza um existente)
