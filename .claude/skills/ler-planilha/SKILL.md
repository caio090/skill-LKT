---
name: ler-planilha
description: >
  Lê uma planilha financeira (Excel/CSV) e normaliza o conteúdo para o
  schema de transação/produto do LKT System, sem alterar o arquivo
  original. Primeiro passo antes de qualquer análise financeira mais
  profunda. Use quando o usuário pedir "lê essa planilha", "o que tem
  nesse Excel", "importa esses dados financeiros".
---

# ler-planilha — Leitura e normalização de planilha financeira

## Quando usar

Primeira vez que uma planilha financeira entra no projeto, antes de
`auditar-planilha`, `fluxo-de-caixa`, `dre`, `calcular-cmv` ou
`precificacao` rodarem sobre ela.

## Quando não usar

- Planilha não financeira (briefing, cronograma) → `analisar-dados`.
- Planilha já lida e normalizada nesta sessão → reaproveitar o resultado
  em vez de reler.

## Entradas

Arquivo de planilha (`.xlsx`, `.csv`).

## Dependências

- `processar-arquivo` (a planilha deve passar pela central de arquivos
  primeiro — hash, preservação do original, registro no índice).
- `schemas/financeiro/transacao.schema.json`,
  `schemas/financeiro/produto-precificacao.schema.json`.

## Contexto que deve ser carregado

Nenhuma memória de negócio é necessária pra ler — só o schema de
destino.

---

## Workflow

1. Confirmar que o arquivo já passou por `processar-arquivo` (hash,
   original preservado). Se não, rodar isso primeiro.
2. Ler todas as abas/planilhas, listando nomes de aba e tamanho de cada
   uma antes de processar (evita ignorar aba oculta com dado relevante,
   como aconteceu na planilha `PRECIFICACAO_LUCRATIVA` com a aba oculta
   `BDUNI`).
3. Identificar colunas e mapear pro schema mais próximo (transação ou
   produto/precificação) — registrar o mapeamento coluna-original →
   campo-schema explicitamente, não silenciosamente.
4. **Normalizar status/categoria de texto** (ex.: "Concluído",
   "cONCLUÍDO", "concluído" → todos viram o mesmo valor normalizado) —
   nunca deixar variação de caixa/acento quebrar agrupamento por status.
5. Identificar nomes de coluna genéricos (`Coluna1`, `tipo2`, `ind`) e
   documentar o que representam, sem renomear a planilha original.
6. Identificar fórmulas com erro (`#REF!`, `#DIV/0!`) e **não corrigir
   sozinha** — reportar quantas, onde, e perguntar antes de qualquer
   correção (isso é `auditar-planilha`).
7. Salvar a versão normalizada (JSON ou Markdown) em
   `<pasta-do-projeto-ativo>/03-financeiro/`, mantendo o vínculo com o
   arquivo original via hash.

## Saídas

Dado normalizado em `03-financeiro/` + relatório de mapeamento de
colunas e problemas encontrados (não corrigidos).

## Caminho de salvamento

`<pasta-do-projeto-ativo>/03-financeiro/`.

## Regras

- Nunca alterar a planilha original.
- Nunca inventar valor pra célula vazia ou ilegível.
- Sempre reportar abas ocultas e fórmulas com erro, mesmo que ninguém
  pergunte.

## Critérios de qualidade

Todo campo do schema de destino está mapeado a uma coluna real, ou
marcado como ausente.

## Critérios de validação

Nenhuma transformação de dado sem registro do mapeamento aplicado.

## Limitações

Não corrige erro de fórmula — só relata (isso é `auditar-planilha`).

## Contrato de handoff

Encaminha pra `auditar-planilha` (se houver erro/fórmula suspeita),
`fluxo-de-caixa`, `dre`, `calcular-cmv` ou `precificacao` conforme o tipo
de dado.

## Exemplos de gatilhos positivos

- "Lê essa planilha financeira que o cliente mandou"
- "O que tem nesse Excel de custos"

## Exemplos de gatilhos negativos

- "Analisa esse cronograma" (é `analisar-dados`, não financeiro)
