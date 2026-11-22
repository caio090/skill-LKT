# Catálogo de níveis

Conjuntos de níveis (`schemas/level-set.schema.json`) e definições de
nível (`schemas/level-definition.schema.json`) configuráveis da
instalação. Ver `knowledge/niveis/COMO_FUNCIONAM_OS_NIVEIS.md` e
`knowledge/niveis/NIVEIS_E_DIMENSOES.md` para o conceito completo.

## Arquivo de exemplo

`maturidade-digital.exemplo.json` é um **rascunho de referência** — um
conjunto de níveis completo e funcional, mas marcado explicitamente
como exemplo, não como regra oficial da instalação. Copie e adapte
para criar o primeiro conjunto real (remova `"rascunho_de_referencia":
true` quando a regra for validada com uso real).

## Como adicionar um conjunto de níveis novo

1. Definir a dimensão (ver lista sugerida em `NIVEIS_E_DIMENSOES.md` —
   não é obrigatório usar uma dessas, pode ser uma dimensão nova).
2. Criar `<slug-da-dimensao>.json` aqui, com um `level-set` e seus
   `level-definition` (2 a 5 níveis costuma ser o suficiente — evitar
   granularidade excessiva).
3. Validar contra os schemas (`node tools/validar.js` cobre isso).
4. Registrar regras de classificação relacionadas em
   `classification-rule.schema.json` (podem viver no mesmo arquivo ou
   em `regras/<slug>.json`, conforme a complexidade).

Nenhum conjunto de níveis é obrigatório em toda instalação — o
diagnóstico decide quais dimensões fazem sentido para cada
workspace/projeto.
