---
name: mapear-processo
description: >
  Mapeia um processo interno (o que a empresa faz, em que ordem, com
  qual regra) — início, fim, entradas, etapas, decisões, responsáveis
  por papel, ferramentas, arquivos gerados, tempo, gargalos, riscos e
  indicadores. Não confundir com funil (não mede conversão de pessoas)
  nem com pipeline (não acompanha item individual). Use quando o
  usuário disser "mapeia esse processo", "como funciona o atendimento
  hoje", "documenta como a gente faz X".
---

# mapear-processo — O que a empresa faz, em que ordem, com qual regra

Documenta um processo existente (ou desenhado do zero) como sequência de
etapas com responsável, ferramenta e saída — sem tratar isso como funil
ou pipeline. Ver `knowledge/projetos/ONTOLOGIA_PROCESSOS_FUNIS_PIPELINES.md`.

## Quando usar

- Documentar como uma operação já funciona hoje.
- Desenhar um processo novo antes de transformar em fluxo de trabalho
  ou automação.

## Quando não usar

- Quando o objetivo é medir conversão de pessoas entre etapas (é
  `desenhar-funil`).
- Quando o objetivo é acompanhar item individual em andamento (é
  `configurar-pipeline`).

## Entradas

- Nome e área do processo.
- Descrição de como funciona hoje (ou intenção, se for novo).

## Dependências

- `schemas/processo.schema.json`, `schemas/etapa.schema.json`
- `templates/processo/PROCESSO.txt`
- `knowledge/projetos/ONTOLOGIA_PROCESSOS_FUNIS_PIPELINES.md`

## Contexto que deve ser carregado

- `_memoria.json` do workspace (processos já mapeados, para não
  duplicar).

---

## Workflow

### Passo 1 — Perguntar (ver `perguntas.txt`)

Início, fim, entradas, etapas, decisões, responsáveis, ferramentas,
arquivos gerados, tempo, gargalos, riscos, indicadores.

### Passo 2 — Estruturar (ver `fluxo.md`)

Organizar etapas em ordem, com responsável por papel e regra de
decisão/transição entre elas (`schemas/transicao.schema.json`).

### Passo 3 — Gerar saída (ver `saidas.md`)

Documento do processo em `templates/processo/PROCESSO.txt` e/ou
`_memoria.json` estruturado conforme `schemas/processo.schema.json`.

### Passo 4 — Validar (ver `validacao.md`)

Conferir que toda etapa tem responsável e que não há etapa sem entrada
nem saída definida.

---

## Saídas

Processo documentado (etapas, responsáveis, regras, indicadores) salvo
no workspace/projeto ativo.

## Regras

- Nunca chamar de "funil" um processo sem entidade contável passando
  por etapas.
- Toda etapa tem responsável por papel, não nome solto.

## Critérios de qualidade

- Início e fim claros; nenhuma etapa órfã (sem entrada ou sem saída).

## Critérios de validação

- Documento válido contra `schemas/processo.schema.json`.

## Limitações

- Não mede desempenho histórico — isso é `analisar-conversao` (quando
  aplicável) ou medição do módulo correspondente.

## Caminho de salvamento

`workspaces/<tipo>/<slug>/[projetos/<projeto>/]02-modelagem/PROCESSO.md`

## Contrato de handoff

Encaminha para `automatizar-fluxo` quando alguma etapa for candidata a
automação.

## Exemplos de gatilhos positivos

- "Mapeia esse processo"
- "Como funciona o atendimento hoje"

## Exemplos de gatilhos negativos

- "Quero saber quantas pessoas viram o anúncio e compraram" (é
  `desenhar-funil`)

Arquivos de apoio desta skill: `perguntas.txt`, `fluxo.md`, `saidas.md`,
`validacao.md`, `exemplos.md`.
