---
name: auditoria-completa
description: >
  Orquestra uma auditoria completa de um cliente/projeto: financeiro
  (planilhas), técnico (repositório/sistema) e operacional, consolidando
  achados num relatório único. Use quando o usuário pedir "faz uma
  auditoria completa desse negócio/sistema", "quero um raio-x geral
  antes de assumir esse cliente".
---

# auditoria-completa — Orquestrador de auditoria cross-área

## Quando usar

Início de trabalho com um cliente/sistema desconhecido, quando é preciso
entender riscos antes de agir (financeiro, técnico e operacional
juntos).

## Quando não usar

Auditoria de uma área só → `auditar-planilha` ou `auditar-repositorio`
isolados.

## Entradas

Acesso aos materiais do cliente/projeto (planilhas, repositório,
processos).

## Dependências

`auditar-planilha`, `diagnostico-tecnico`, `auditar-repositorio`,
`organizar-projeto` (modo auditoria operacional).

## Contexto que deve ser carregado

Tudo que já existir do cliente/projeto ativo.

---

## Workflow

1. Se houver planilha financeira: `ler-planilha` → `auditar-planilha`.
2. Se houver sistema/repositório: `diagnostico-tecnico` →
   `auditar-repositorio`.
3. Auditoria operacional: `organizar-projeto` (modo auditoria) —
   gargalo de processo, equipe, pendência.
4. Consolidar achados por severidade (crítico, importante, observação),
   cruzando as três áreas quando fizer sentido (ex.: erro de planilha
   que também é sintoma de processo mal desenhado).
5. Recomendações priorizadas, com responsável e prazo.
6. Salvar em `<pasta-do-projeto-ativo>/09-relatorios/auditoria-completa-<data>.md`.

## Saídas

Relatório único consolidando os 3 eixos de auditoria.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/09-relatorios/`.

## Regras

- Nenhum eixo (financeiro/técnico/operacional) é auditado sem os
  materiais correspondentes existirem — não inventar achado.
- Achado crítico (segredo exposto, erro financeiro grave) sempre no
  topo, independente da área.

## Critérios de qualidade

Todo achado é rastreável à skill de origem que o identificou.

## Critérios de validação

Cada eixo aplicável foi auditado ou explicitamente descartado (por
falta de material) com motivo registrado.

## Limitações

Profundidade de cada eixo depende da qualidade/completude do material
disponível.

## Contrato de handoff

Encaminha pra `plano-estrategico` (achados que exigem decisão de
negócio) e `organizar-projeto` (achados operacionais a corrigir).

## Exemplos de gatilhos positivos

- "Faz uma auditoria completa desse negócio antes de eu assumir"
- "Quero um raio-x geral desse cliente novo"

## Exemplos de gatilhos negativos

- "Só audita essa planilha" (é `auditar-planilha` isolado)
