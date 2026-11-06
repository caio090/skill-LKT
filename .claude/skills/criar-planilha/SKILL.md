---
name: criar-planilha
description: >
  Cria ou edita uma planilha (custos, fluxo de caixa, orçamento,
  cronograma, controle) para um projeto. Preserva planilhas originais
  recebidas, trabalha em cópia, valida fórmulas e resultado, e registra
  no índice. Use quando o usuário pedir "cria uma planilha de X", "monta
  o controle de orçamento em planilha", "organiza isso numa tabela".
---

# criar-planilha — Planilha para controle/entrega

## Quando usar

- Dado tabular/numérico que precisa de cálculo, controle contínuo ou
  organização em linhas/colunas (custos, cronograma, orçamento,
  checklist com status).

## Quando não usar

- Planilha financeira já existente do cliente que só precisa ser lida —
  isso é `ler-planilha`/`auditar-planilha`, não recriar do zero.
- Documento narrativo → `criar-documento`.

## Entradas

- Dados a organizar, ou objetivo do controle (ex.: "orçamento de
  campanha").

## Dependências

- Template relevante em `templates/financeiro/` ou
  `templates/documentos/` (checar antes de criar do zero).
- Se partir de planilha recebida: nunca editar o original — usar
  `processar-arquivo` primeiro pra registrar e criar cópia de trabalho.
- Schema de referência em `schemas/` quando o tipo de dado já tiver um
  (ex.: transação financeira).

## Contexto que deve ser carregado

Projeto/cliente ativo. Se for planilha financeira, ver também as regras
financeiras do módulo `financeiro`.

---

## Workflow

### Passo 1 — Verificar template e schema

Checar `templates/financeiro/` (ou pasta equivalente) e `schemas/` por
modelo/formato já validado antes de estruturar colunas do zero.

### Passo 2 — Cópia de trabalho

Se a planilha parte de um arquivo recebido, nunca alterar o original.
Trabalhar em cópia salva em `<pasta-do-projeto-ativo>/03-financeiro/`
(se financeiro) ou `08-entregas/` (outro tipo de controle).

### Passo 3 — Estruturar

Definir colunas/abas com nomes claros (nunca "Coluna1", "tipo2" — nomear
pelo que representam de fato). Fórmulas devem ser conferíveis (não
"caixa preta" sem explicação de como o valor é calculado).

### Passo 4 — Preencher

Preencher com dado real fornecido. Nunca inventar número — se faltar
dado, deixar célula vazia ou marcada como "a confirmar", nunca um valor
estimado disfarçado de real.

### Passo 5 — Validar

Conferir: fórmulas calculam o esperado (testar com 1-2 casos manuais),
nenhuma referência quebrada, nenhuma aba oculta com erro sem explicação.

### Passo 6 — Salvar e registrar

Salvar na pasta correta do projeto e registrar no índice
(`arquivos/INDICE.md` ou o do cliente/projeto).

---

## Saídas

Planilha de controle/entrega, com fórmulas testadas e sem dado inventado.

## Regras

- Nunca alterar planilha original recebida.
- Nunca inventar dado numérico ausente — marcar como pendente.
- Nomear colunas/abas de forma clara, nunca genérica.
- Toda projeção/estimativa marcada explicitamente como tal, nunca
  misturada com dado real sem diferenciação visual.

## Critérios de qualidade

- Fórmulas testadas antes de entregar.
- Nenhuma célula com valor inventado disfarçado de dado real.

## Critérios de validação

- Arquivo abre sem erro de fórmula.
- Está registrado no índice correto.

## Limitações

- Não faz auditoria de planilha financeira complexa já existente — isso
  é `auditar-planilha` (módulo financeiro).
- Não decide política financeira (markup, precificação) — só organiza o
  que foi decidido em outro lugar, a menos que a skill financeira
  específica seja chamada em conjunto.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/03-financeiro/` (financeiro) ou
`08-entregas/` (outro controle).

## Contrato de handoff

Se for planilha financeira de verdade (custos, DRE, fluxo de caixa),
encaminhar pras skills do módulo financeiro assim que existirem.

## Exemplos de gatilhos positivos

- "Cria uma planilha de orçamento de campanha"
- "Monta um controle de cronograma em planilha"

## Exemplos de gatilhos negativos

- "Analisa essa planilha que o cliente mandou" (é `ler-planilha`/`auditar-planilha`)
- "Escreve o relatório final" (é `criar-documento`)
