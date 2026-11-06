---
name: processar-arquivo
description: >
  Processa um arquivo novo recebido em arquivos/entrada/ (ou
  workspaces/clientes/<cliente>/arquivos/entrada/): preserva o original, calcula
  hash, extrai conteúdo útil, classifica, move pra processados/ ou
  biblioteca/, e atualiza o índice. Use quando o usuário disser "processa
  esse arquivo", "chegou uma planilha nova", "joguei um PDF em entrada",
  "organiza esse documento", ou quando um arquivo novo aparecer em
  qualquer pasta entrada/ do sistema.
---

# processar-arquivo — Central de arquivos (entrada → processados/biblioteca)

Operacionaliza a regra de central de arquivos que já está descrita no
`CLAUDE.md`: todo arquivo recebido é preservado no original, registrado,
processado e indexado — nunca alterado na origem, nunca com dado
inventado.

## Quando usar

- Um arquivo novo foi colocado em `arquivos/entrada/` (geral) ou em
  `workspaces/clientes/<cliente>/arquivos/entrada/`.
- O usuário pede explicitamente pra processar/organizar um documento,
  planilha, PDF, manual de marca, etc.

## Quando não usar

- Arquivo que já foi processado (já tem entrada equivalente no índice) —
  nesse caso, perguntar se é uma nova versão (reprocessar) ou duplicata.
- Análise de dados como fim em si (gerar insights de uma planilha) — isso
  é `analisar-dados`; `processar-arquivo` cuida só da entrada na central
  de arquivos. As duas podem ser usadas em sequência.

## Entradas

- Caminho do arquivo em alguma pasta `entrada/`.

## Dependências

- `arquivos/INDICE.md` (geral) ou `workspaces/clientes/<cliente>/arquivos/INDICE.md`
  (equivalente por cliente, criar se ainda não existir).
- Ferramentas de leitura conforme o formato (planilha, PDF, imagem,
  texto).

## Contexto que deve ser carregado

- `_memoria/empresa.md` (ou memória do cliente, se o arquivo for
  específico dele) — pra saber classificar o conteúdo com contexto.

---

## Workflow

### Passo 1 — Confirmar escopo

Identificar se o arquivo é geral (negócio) ou de um cliente/projeto
específico — isso determina se o destino é `arquivos/` da raiz ou
`workspaces/clientes/<cliente>/arquivos/`.

### Passo 2 — Preservar e registrar

1. Nunca mover o original antes de registrar — copiar os metadados
   primeiro:
   - Nome original, formato, tamanho, data
   - Hash (SHA-256, se houver ferramenta disponível; senão, registrar
     "hash não calculado — ferramenta indisponível")
   - Origem (quem enviou, de onde veio)
2. Criar uma entrada correspondente antes de mexer no arquivo.

### Passo 3 — Extrair conteúdo útil

- Ler o arquivo com a ferramenta adequada ao formato.
- Se fizer sentido, gerar uma versão em Markdown do conteúdo relevante
  (resumo, texto extraído, estrutura de abas de uma planilha, etc.) —
  guardar ao lado do processamento, não substituir o original.
- Se o arquivo for uma planilha, **não alterar fórmulas ou dados
  originais** — só ler e descrever.

### Passo 4 — Classificar

Decidir a categoria (marca, pesquisa, comercial, financeiro, conteudo,
dados, referencias, legal, audiovisual, codigo — mesmas categorias de
`arquivos/biblioteca/`) e se o material é:
- **Fato** (dado concreto, verificável)
- **Estimativa** (projeção, aproximação)
- **Interpretação** (leitura/opinião sobre o material)

Registrar essa distinção — nunca deixar estimativa parecer fato.

### Passo 5 — Mover pra destino final

- Material de uso pontual (já extraído o que interessava) →
  `arquivos/processados/<slug>-<data>/` (ou equivalente do cliente).
- Material de referência permanente (manual de marca, planilha financeira
  ativa, contrato) → `arquivos/biblioteca/<categoria>/` (ou equivalente
  do cliente).

O arquivo original nunca é editado — só copiado/movido de pasta, com
metadados preservados.

### Passo 6 — Atualizar índice

Atualizar `arquivos/INDICE.md` (ou o do cliente) com uma linha nova:
nome original, formato, origem, data, categoria, destino, resumo curto.
Não reformatar a tabela inteira.

### Passo 7 — Indicar o que entra na memória

Ao final, apontar explicitamente: "isso deveria atualizar
`_memoria/<arquivo>.md`" (ou o equivalente do cliente) — sem gravar
sozinho na memória sem confirmar, a menos que seja óbvio e de baixo
risco (seguindo a mesma régua de "Aprender com correções" do
`CLAUDE.md`).

---

## Saídas

Arquivo preservado no original, registrado no índice, classificado e movido pra processados/biblioteca.

## Regras

- Nunca alterar o arquivo original.
- Nunca inventar conteúdo ausente ou ilegível — registrar como limitação.
- Nunca pular o registro de metadados (nome, formato, origem, data) antes
  de mover o arquivo.
- Distinguir sempre fato / estimativa / interpretação no que for
  extraído.

## Critérios de qualidade

- Toda entrada no índice é rastreável até o arquivo original preservado.
- Nenhum dado extraído aparece na memória sem passar por essa
  classificação.

## Critérios de validação

- `arquivos/INDICE.md` (ou o do cliente) sempre reflete todo arquivo que
  passou por esta skill.
- O arquivo original continua acessível e inalterado depois do
  processamento.

## Limitações

- Não decide sozinho gravar em memória — só indica e, se ambíguo,
  pergunta antes.
- Não substitui uma auditoria financeira completa (ver módulo
  `financeiro`) — só faz a entrada do arquivo na central.

## Caminho de salvamento

`arquivos/processados/` ou `arquivos/biblioteca/<categoria>/` (raiz), ou
os equivalentes dentro de `workspaces/clientes/<cliente>/arquivos/`.

## Contrato de handoff

Se o arquivo for de dados/planilha e o usuário quiser insights, encaminha
pra `analisar-dados`. Se for financeiro (planilha de custos, precificação),
encaminha pro módulo `financeiro` quando as skills financeiras existirem.

## Exemplos de gatilhos positivos

- "Processa esse arquivo"
- "Chegou uma planilha nova"
- "Joguei um PDF em entrada"

## Exemplos de gatilhos negativos

- "O que esses dados mostram" (arquivo já processado — é
  `analisar-dados`)
