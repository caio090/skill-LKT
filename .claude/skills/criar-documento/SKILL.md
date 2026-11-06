---
name: criar-documento
description: >
  Cria ou edita um documento de texto (Word/Markdown/rich text) para um
  projeto — proposta, relatório, briefing, contrato, manual. Preserva
  originais recebidos, usa cópia de trabalho, valida o resultado e
  registra no índice. Use quando o usuário pedir "cria o documento de X",
  "escreve a proposta em Word", "gera esse relatório em documento".
---

# criar-documento — Documento de texto para entrega

## Quando usar

- Entrega que faz mais sentido como documento de texto corrido
  (proposta, relatório narrativo, contrato, manual, briefing formal) do
  que como planilha, apresentação ou PDF puro.

## Quando não usar

- Dado tabular/numérico → `criar-planilha`.
- Apresentação com slides → `criar-apresentacao`.
- Documento já finalizado que só precisa virar PDF → `criar-pdf`.

## Entradas

- Conteúdo do documento (ou os arquivos-fonte de onde extrair).
- Formato de saída desejado (`.md`, `.docx`, outro).

## Dependências

- Template relevante em `templates/documentos/` (checar antes de criar
  do zero).
- `_memoria/marca.md` (para cabeçalho/identidade, se o documento for
  formal e for pra cliente).
- Se partir de arquivo recebido: passar antes por `processar-arquivo`.

## Contexto que deve ser carregado

Projeto/cliente ativo (`.lkt-system/estado/contexto-ativo.json`), memória de
preferências para o tom do texto.

---

## Workflow

### Passo 1 — Verificar template

Checar `templates/documentos/` por um modelo compatível com o tipo de
documento pedido. Usar como base se existir; se não, propor estrutura e
seguir.

### Passo 2 — Cópia de trabalho

Se o documento parte de um arquivo já existente, nunca editar o
original — trabalhar numa cópia dentro de
`<pasta-do-projeto-ativo>/08-entregas/` (ou `_historico/` se for
revisão de algo já entregue antes).

### Passo 3 — Escrever o conteúdo

Escrever o conteúdo real (não lorem ipsum). Encaminhar texto voltado a
cliente/público para `texto-natural-pt-br` antes de finalizar.

### Passo 4 — Definir formato de saída

Confirmar formato (`.md` é o padrão mais simples e versionável; `.docx`
quando o cliente precisar editar em Word). Gerar nesse formato.

### Passo 5 — Validar

Conferir: nenhum campo placeholder esquecido, formatação consistente,
nome de cliente/projeto correto ao longo do texto (não copiado de outro
cliente por engano).

### Passo 6 — Salvar e registrar

Salvar em `<pasta-do-projeto-ativo>/08-entregas/` e registrar no índice
do projeto (ou `arquivos/INDICE.md` se for documento geral, não de
projeto específico).

---

## Saídas

Documento final (proposta, relatório, contrato, manual) no formato
definido, sem placeholder remanescente.

## Regras

- Nunca alterar arquivo original recebido — sempre cópia de trabalho.
- Nunca deixar placeholder ("[nome do cliente]", "lorem ipsum") no
  documento final.
- Texto voltado a público/cliente sempre passa por `texto-natural-pt-br`.

## Critérios de qualidade

- Documento final não tem nenhum campo genérico não preenchido.
- Formato de saída bate com o pedido (ou foi confirmado com o usuário).

## Critérios de validação

- Arquivo final abre/renderiza sem erro no formato escolhido.
- Registrado no índice correto.

## Limitações

- Não decide o conteúdo estratégico do documento sozinha — isso vem do
  diagnóstico/projeto; esta skill escreve e formata.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/08-entregas/`.

## Contrato de handoff

`texto-natural-pt-br` para qualquer texto voltado a público antes de
finalizar, e `anti-chat` (quality gate final) na sequência.

## Exemplos de gatilhos positivos

- "Cria a proposta comercial em documento"
- "Escreve esse relatório em Word"

## Exemplos de gatilhos negativos

- "Cria uma planilha de custos" (é `criar-planilha`)
- "Transforma isso em slides" (é `criar-apresentacao`)
