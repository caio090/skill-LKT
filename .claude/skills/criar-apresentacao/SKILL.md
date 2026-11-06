---
name: criar-apresentacao
description: >
  Cria uma apresentação (slides) para reunião, proposta, palestra ou
  relatório de um projeto, coerente com a marca. Usa template quando
  existir, valida o resultado e registra no índice. Use quando o usuário
  pedir "cria uma apresentação de X", "monta os slides pra reunião com o
  cliente", "preciso de uma palestra sobre Y".
---

# criar-apresentacao — Slides para reunião/proposta/palestra

## Quando usar

- Entrega que será apresentada oralmente ou lida como slides (reunião de
  alinhamento, proposta comercial, palestra, relatório visual).

## Quando não usar

- Documento pra leitura corrida → `criar-documento`.
- Conteúdo social (carrossel de Instagram) → `carrossel` (formato e
  objetivo diferentes, mesmo que ambos sejam "slides").

## Entradas

- Objetivo da apresentação, público, conteúdo-base (diagnóstico,
  proposta, relatório já existente).

## Dependências

- Template em `templates/documentos/` se existir um modelo de
  apresentação.
- `_memoria/marca.md` / `workspaces/clientes/<cliente>/_memoria/marca.md` —
  identidade visual.
- `design-front-end` para calibrar direção visual se a apresentação for
  visualmente elaborada (não só texto).

## Contexto que deve ser carregado

Projeto/cliente ativo, memória de marca.

---

## Workflow

### Passo 1 — Objetivo e público

Definir o que a apresentação precisa convencer/comunicar e pra quem —
isso decide quanto de dado técnico vs. narrativa entra.

### Passo 2 — Estrutura

Definir a sequência de slides (ex.: contexto → problema → proposta →
próximos passos). Um objetivo por slide — não empilhar informação.

### Passo 3 — Conteúdo

Escrever o texto de cada slide: curto, direto, sem parágrafo denso —
apresentação não é documento. Encaminhar pra `texto-natural-pt-br` no
texto de cada slide antes de finalizar.

### Passo 4 — Visual

Aplicar identidade de `marca.md`. Se precisar de decisão visual mais
elaborada, encaminhar pra `design-front-end`.

### Passo 5 — Validar

Conferir: nenhum slide com texto genérico/placeholder, dados batem com a
fonte real (nada inventado), narrativa flui na ordem certa.

### Passo 6 — Salvar e registrar

Salvar em `<pasta-do-projeto-ativo>/08-entregas/` e registrar no índice.

---

## Saídas

Apresentação (slides) pronta pra reunião, proposta, palestra ou
relatório visual.

## Regras

- Um objetivo por slide.
- Nunca dado inventado — todo número vem de fonte rastreável (diagnóstico,
  planilha, pesquisa já feita no projeto).
- Texto de slide é sempre mais curto que texto de documento — se está
  denso demais, é sinal de que devia ser `criar-documento`, não slide.

## Critérios de qualidade

- Cada slide tem uma mensagem central identificável.
- Identidade visual da marca aplicada de forma consistente entre slides.

## Critérios de validação

- Nenhum placeholder remanescente.
- Registrado no índice do projeto.

## Limitações

- Não decide a narrativa estratégica sozinha — isso vem do diagnóstico/
  estratégia do projeto; a skill organiza e apresenta.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/08-entregas/`.

## Contrato de handoff

`texto-natural-pt-br` (texto de cada slide), `design-front-end` (se
precisar de direção visual elaborada), `anti-chat` (quality gate final).

## Exemplos de gatilhos positivos

- "Monta os slides pra reunião com o cliente X"
- "Cria uma apresentação da proposta"

## Exemplos de gatilhos negativos

- "Cria um carrossel pro Instagram" (é `carrossel`)
- "Escreve o relatório completo em texto" (é `criar-documento`)
