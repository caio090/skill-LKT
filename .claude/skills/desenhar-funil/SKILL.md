---
name: desenhar-funil
description: >
  Desenha um funil de conversão — quantidade e taxa de passagem de uma
  entidade (visitante, lead, candidato) entre etapas até um resultado
  final. Pergunta resultado final, entidade contada, período, etapas,
  evento que comprova cada avanço, dados existentes, metas, fonte,
  campanha associada, taxa atual e taxa projetada. Use quando o usuário
  disser "monta um funil", "quero medir conversão de X até Y", "onde
  estamos perdendo gente".
---

# desenhar-funil — Quantidade e taxa de passagem entre etapas

Estrutura um funil de conversão com etapas, evento que comprova cada
avanço, e taxa por etapa — nunca confundir com pipeline (itens
individuais) ou processo (sem entidade contável). Ver
`knowledge/projetos/ONTOLOGIA_PROCESSOS_FUNIS_PIPELINES.md`.

## Quando usar

- Existe uma sequência com perda mensurável de pessoas/entidades entre
  etapas até um resultado.

## Quando não usar

- Para acompanhar oportunidades individuais (é `configurar-pipeline`).
- Para fluxo financeiro sem motivo analítico de passagem/perda real.

## Entradas

- Resultado final desejado.
- Entidade que será contada.
- Período de análise.
- Etapas do funil.
- Evento que comprova cada avanço.
- Dados/fonte disponíveis.
- Metas (se houver).
- Campanha associada (se houver).

## Dependências

- `schemas/funil.schema.json`, `schemas/etapa.schema.json`,
  `schemas/evento-conversao.schema.json`
- `templates/funil/FUNIL.txt`
- `.claude/skills/analisar-conversao` (cálculo de taxa/perda)

## Contexto que deve ser carregado

- Campanha ativa e funis já existentes do workspace (evitar duplicar).

---

## Workflow

### Passo 1 — Perguntar (ver `perguntas.txt`)

Qual resultado final, qual entidade será contada, qual período, quais
etapas, qual evento comprova cada avanço, quais dados existem, quais
metas, qual fonte, qual campanha, qual taxa atual, qual taxa projetada.

### Passo 2 — Estruturar (ver `fluxo.md`)

Etapas em ordem, evento de avanço por etapa, origem do dado.

### Passo 3 — Calcular (ver `saidas.md`)

Quantidade e taxa por etapa, taxa total, maior ponto de perda —
encaminhar cálculo detalhado para `analisar-conversao` quando precisar
de hipótese e recomendação.

### Passo 4 — Validar (ver `validacao.md`)

Cada etapa tem evento de avanço definido; sem etapa "furada" sem dado.

---

## Saídas

Funil estruturado com etapas, quantidade/taxa por etapa e taxa total,
salvo no workspace/projeto e, se houver campanha associada, referenciado
nela (`campanha.funil_id`).

## Regras

- Nunca renomear fluxo financeiro como funil sem motivo analítico real.
- Nunca apresentar taxa sem declarar o período e a fonte do dado.

## Critérios de qualidade

- Toda etapa tem evento de avanço e (quando houver dado) quantidade.

## Critérios de validação

- Documento válido contra `schemas/funil.schema.json`.

## Limitações

- Não coleta dado automaticamente de ferramenta externa nesta versão —
  usa o que o usuário fornecer ou já estiver registrado.

## Caminho de salvamento

`workspaces/<tipo>/<slug>/[projetos/<projeto>/]02-modelagem/FUNIL.md`

## Contrato de handoff

Encaminha para `analisar-conversao` (cálculo de gargalo/hipótese) e
para `criar-campanha` quando o funil precisar de uma campanha para
gerar tráfego.

## Exemplos de gatilhos positivos

- "Monta um funil de vendas"
- "Onde estamos perdendo gente entre o anúncio e a compra?"

## Exemplos de gatilhos negativos

- "Em que fase está a proposta do cliente X?" (é `configurar-pipeline`)

Arquivos de apoio desta skill: `perguntas.txt`, `fluxo.md`, `saidas.md`,
`validacao.md`, `exemplos.md`.
