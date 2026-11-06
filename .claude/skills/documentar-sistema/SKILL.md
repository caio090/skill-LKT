---
name: documentar-sistema
description: >
  Documenta um sistema/projeto técnico: visão geral, arquitetura,
  como rodar localmente, como fazer deploy, decisões técnicas
  importantes. Use quando o usuário pedir "documenta esse sistema",
  "escreve o README técnico".
---

# documentar-sistema — Documentação técnica

## Quando usar

Sistema implementado (ou em implementação) sem documentação adequada.

## Quando não usar

Documentação de negócio/processo não técnico → `criar-sop`.

## Entradas

Código/arquitetura do sistema.

## Dependências

`arquitetura-de-software`, `planejar-banco-de-dados`.

## Contexto que deve ser carregado

Arquitetura documentada do projeto ativo, se existir.

---

## Workflow

1. Visão geral (o que o sistema faz, em linguagem simples).
2. Arquitetura (componentes, stack) — reaproveitar de
   `arquitetura-de-software` se já existir.
3. Como rodar localmente (passo a passo, sem assumir conhecimento
   prévio).
4. Como fazer deploy (processo real usado no projeto).
5. Decisões técnicas importantes e por quê (evita que alguém desfaça
   uma decisão por não saber o motivo original).
6. Salvar em `<pasta-do-projeto-ativo>/07-tecnologia/README.md` (ou
   `08-entregas/` se for parte da entrega ao cliente).

## Saídas

Documentação técnica completa.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/07-tecnologia/`.

## Regras

- Instruções de "como rodar" testáveis por alguém que nunca viu o
  projeto.
- Decisão técnica documentada com o motivo, não só o "o quê".

## Critérios de qualidade

Pessoa nova consegue rodar o projeto localmente só seguindo a
documentação.

## Critérios de validação

Todas as decisões técnicas relevantes de `arquitetura-de-software`
aparecem documentadas com motivo.

## Limitações

Não substitui comentário de código específico quando necessário — é a
documentação de nível de projeto, não de linha.

## Contrato de handoff

Referenciado por `qa` e `onboarding` de novos membros da equipe técnica.

## Exemplos de gatilhos positivos

- "Documenta esse sistema pro próximo desenvolvedor"
- "Escreve o README técnico"

## Exemplos de gatilhos negativos

- "Documenta esse processo de atendimento" (é `criar-sop`)
