---
name: revisar-nivel
description: >
  Revisa uma classificação de nível existente quando houver novo
  diagnóstico, mudança de projeto, marco concluído, dependência
  resolvida, mudança de orçamento/escopo, métrica relevante alterada ou
  fim de fase. Registra a transição (avanço/recuo) sem alterar
  retroativamente avaliações antigas. Use quando o usuário disser
  "revisa o nível", "isso mudou, reclassifica", ou nos gatilhos listados.
---

# revisar-nivel — Revisão que preserva o histórico

Revisa uma classificação existente e registra a transição — nunca
apaga ou reescreve a avaliação anterior. Ver
`schemas/level-transition.schema.json`.

## Quando usar

Novo diagnóstico; projeto mudou; marco concluído; dependência
resolvida; orçamento mudou; escopo mudou; métrica relevante mudou;
fase terminou; ou pedido explícito do usuário.

## Quando não usar

- Para a primeira classificação (é `classificar-nivel`).
- Quando nada relevante mudou desde a última avaliação — nesse caso,
  só confirmar que continua válida (sem gerar nova entrada).

## Entradas

- `level-assessment` anterior.
- O que mudou (gatilho da revisão).

## Dependências

- `schemas/level-transition.schema.json`,
  `schemas/level-assessment.schema.json`
- `.claude/skills/classificar-nivel` (reaplica a classificação com o
  novo contexto)

## Contexto que deve ser carregado

- Todas as avaliações anteriores da dimensão (histórico completo, não
  só a mais recente).

---

## Workflow

### Passo 1 — Identificar o gatilho (ver `perguntas.txt`)

Confirmar qual dos gatilhos de revisão se aplica.

### Passo 2 — Reclassificar com o contexto novo

Rodar a lógica de `classificar-nivel` com a evidência atualizada.

### Passo 3 — Comparar com a avaliação anterior

Se o nível mudou: registrar `level-transition` (avanço, recuo ou
revisão humana), com motivo e evidências. Se não mudou: registrar só
que foi revisado e confirmado (sem nova transição).

### Passo 4 — Nunca alterar avaliação antiga

A avaliação anterior permanece intacta, com a `versao_da_regra` que a
gerou. A nova avaliação é um registro novo, referenciando a anterior
via `level-transition`.

### Passo 5 — Avisar sobre efeito em recomendação/proposta

Se havia uma `level-recommendation` ou proposta baseada no nível
anterior, avisar que pode precisar de atualização (encaminhar para
`recomendar-nivel` de novo, se fizer sentido).

---

## Saídas

`level-transition` (quando houve mudança) + novo `level-assessment`.
Avaliação anterior preservada, intocada.

## Regras

- Nunca editar ou apagar uma avaliação anterior.
- Toda transição registra motivo e evidência.
- Revisão humana que diverge da regra automática é sempre registrada
  como tal, nunca silenciosamente sobrescrita.

## Critérios de qualidade

- Toda transição tem `de_nivel`, `para_nivel`, motivo e data.

## Critérios de validação

- `level-transition` válido contra
  `schemas/level-transition.schema.json`.
- Avaliação anterior permanece recuperável no histórico.

## Limitações

- Não decide sozinha revisar — precisa de um gatilho real (não roda
  em loop nem por iniciativa própria sem gatilho).

## Caminho de salvamento

`workspaces/<tipo>/<slug>/[projetos/<projeto>/]01-diagnostico/NIVEL-<dimensao>.json`
(nova entrada) + `_historico/` (referência à avaliação anterior).

## Contrato de handoff

Recebe gatilho de qualquer skill (`diagnostico-empresarial`,
`proposta-e-precificacao`, `mapear-processo`, etc.). Encaminha para
`recomendar-nivel` quando a recomendação precisar ser refeita.

## Exemplos de gatilhos positivos

- "Revisa o nível de maturidade comercial, o CRM já foi implantado"
- "Isso mudou, reclassifica"

## Exemplos de gatilhos negativos

- "Classifica pela primeira vez" (é `classificar-nivel`)

Arquivos de apoio: `perguntas.txt`, `fluxo.md`, `saidas.md`,
`validacao.md`, `exemplos.md`.
