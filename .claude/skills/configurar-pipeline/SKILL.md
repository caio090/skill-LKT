---
name: configurar-pipeline
description: >
  Configura um pipeline — visualização de onde cada item (oportunidade,
  candidato, chamado) está agora. Pergunta o que será acompanhado,
  etapas, critérios de entrada e saída de cada etapa, responsável,
  próxima ação, prazo, prioridade, valor, probabilidade e automações
  permitidas. Use quando o usuário disser "monta um pipeline", "quero
  ver onde está cada oportunidade", "organiza minhas negociações".
---

# configurar-pipeline — Onde cada item está agora

Estrutura um pipeline com etapas e itens individuais rastreados — nunca
confundir com funil (taxa agregada) nem processo (sem item
individualizado). Ver
`knowledge/projetos/ONTOLOGIA_PROCESSOS_FUNIS_PIPELINES.md`.

## Quando usar

- Existe um conjunto de itens (oportunidades, candidatos, chamados,
  campanhas em produção) que precisam de acompanhamento individual.

## Quando não usar

- Para medir taxa agregada de conversão (é `desenhar-funil`).

## Entradas

- O que será acompanhado (tipo de item).
- Etapas.
- Critérios de entrada e saída de cada etapa.
- Responsável por papel.
- Automações permitidas (nível de autonomia, ver
  `docs/SEGURANCA_E_PERMISSOES.md`).

## Dependências

- `schemas/pipeline.schema.json`, `schemas/etapa.schema.json`
- `templates/pipeline/PIPELINE.txt`
- `.claude/skills/automatizar-fluxo` (quando houver automação)

## Contexto que deve ser carregado

- Pipelines já existentes do workspace (evitar duplicar).

---

## Workflow

### Passo 1 — Perguntar (ver `perguntas.txt`)

O que será acompanhado, quais etapas, critérios de entrada, critérios
de saída, responsável, próxima ação, prazo, prioridade, valor,
probabilidade, automações permitidas.

### Passo 2 — Estruturar (ver `fluxo.md`)

Etapas com critério de entrada/saída; cada item novo entra com etapa
atual, data de entrada, responsável e próxima ação — nunca sem próxima
ação definida.

### Passo 3 — Gerar saída (ver `saidas.md`)

Pipeline salvo conforme `schemas/pipeline.schema.json`.

### Passo 4 — Validar (ver `validacao.md`)

Nenhum item sem próxima ação; nenhum item parado além do SLA sem
sinalização.

---

## Saídas

Pipeline estruturado com etapas e itens rastreados, salvo no
workspace/projeto.

## Regras

- Todo item tem responsável por papel, próxima ação e (quando fizer
  sentido) prazo.
- Automação de nível 4/5 nunca é o padrão — ver
  `docs/SEGURANCA_E_PERMISSOES.md`.

## Critérios de qualidade

- Nenhum item "morto" (sem próxima ação, sem prazo, sem atualização há
  muito tempo) sem estar sinalizado como risco.

## Critérios de validação

- Documento válido contra `schemas/pipeline.schema.json`.

## Limitações

- Não decide sozinha quando mover um item de etapa — segue o critério
  de saída definido, ou pergunta quando não estiver claro.

## Caminho de salvamento

`workspaces/<tipo>/<slug>/[projetos/<projeto>/]04-comercial/PIPELINE.md`
(ou `05-operacao/` quando o pipeline não for comercial)

## Contrato de handoff

Encaminha para `automatizar-fluxo` quando alguma transição de etapa for
candidata a automação.

## Exemplos de gatilhos positivos

- "Monta um pipeline de vendas"
- "Onde está cada oportunidade agora?"

## Exemplos de gatilhos negativos

- "Quantas pessoas converteram esse mês?" (é `desenhar-funil` /
  `analisar-conversao`)

Arquivos de apoio desta skill: `perguntas.txt`, `fluxo.md`, `saidas.md`,
`validacao.md`, `exemplos.md`.
