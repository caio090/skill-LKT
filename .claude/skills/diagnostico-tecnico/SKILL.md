---
name: diagnostico-tecnico
description: >
  Diagnostica a situação técnica de um sistema/projeto existente: stack,
  débito técnico, riscos de segurança básicos, performance percebida e
  o que trava a evolução. Use quando o usuário pedir "faz um diagnóstico
  técnico desse sistema", "por que esse sistema está lento/travando".
---

# diagnostico-tecnico — Diagnóstico técnico

## Quando usar

Início de trabalho técnico num sistema já existente, ou quando algo
está dando problema sem causa clara.

## Quando não usar

Sistema novo do zero → `app-e-sistema` (planejamento), não diagnóstico.

## Entradas

Acesso ao código/repositório (leitura), descrição do problema
percebido.

## Dependências

`auditar-repositorio` (detalhe técnico), `revisar-codigo`.

## Contexto que deve ser carregado

`07-tecnologia/` do projeto ativo, se já existir documentação.

---

## Workflow

1. Stack atual (linguagem, framework, banco, hospedagem).
2. Débito técnico visível (código duplicado, sem teste, sem
   documentação).
3. Riscos de segurança básicos (segredo exposto, dependência
   desatualizada crítica — ver `qa`, modo segurança).
4. Performance percebida vs. real (se houver como medir).
5. O que trava a evolução (dependência de uma pessoa só, falta de
   ambiente de teste, deploy manual arriscado).
6. Salvar em `<pasta-do-projeto-ativo>/07-tecnologia/diagnostico-tecnico.md`.

## Saídas

Diagnóstico técnico com riscos e recomendações priorizadas.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/07-tecnologia/`.

## Regras

- Nunca afirmar vulnerabilidade sem verificar (não especular sobre
  segurança sem evidência).
- Recomendação sempre com prioridade e esforço estimado.

## Critérios de qualidade

Cada risco apontado tem evidência (arquivo, linha, comportamento
observado).

## Critérios de validação

Recomendações são executáveis (têm próximo passo claro).

## Limitações

Não corrige nada sozinho — diagnostica; correção é
`revisar-codigo`/`depurar-erro`/decisão do responsável técnico.

## Contrato de handoff

Encaminha pra `arquitetura-de-software` (se o problema for estrutural)
ou `depurar-erro` (se for um bug específico).

## Exemplos de gatilhos positivos

- "Faz um diagnóstico técnico desse sistema"
- "Por que esse sistema está lento"

## Exemplos de gatilhos negativos

- "Planeja um sistema novo do zero" (é `app-e-sistema`)
