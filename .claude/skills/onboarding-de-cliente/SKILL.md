---
name: onboarding-de-cliente
description: >
  Estrutura o onboarding de um cliente novo fechado: o que precisa ser
  coletado, comunicado e configurado nos primeiros dias, com checklist e
  responsáveis. Use quando o usuário pedir "fecha o onboarding desse
  cliente novo", "o que preciso fazer agora que o cliente assinou".
---

# onboarding-de-cliente — Onboarding pós-fechamento

## Quando usar

Logo depois que uma proposta é aceita/contrato assinado.

## Quando não usar

Cliente já em operação há tempo → isso é `atendimento`/operação normal.

## Entradas

Escopo fechado (`proposta-comercial`), dados de contato do cliente.

## Dependências

`novo-projeto` (se ainda não criou a estrutura do cliente/projeto),
`proposta-comercial`.

## Contexto que deve ser carregado

Escopo fechado do projeto ativo.

---

## Workflow

1. Confirmar que `novo-projeto` já rodou (estrutura de cliente/projeto
   criada) — se não, rodar antes.
2. Checklist de onboarding: dados de acesso necessários, materiais que o
   cliente precisa enviar (arquivos → `processar-arquivo`), reunião de
   kickoff, expectativas alinhadas (prazo, comunicação, entregas).
3. Comunicar ao cliente o que esperar (canal de comunicação, cadência de
   report).
4. Registrar responsável por cada item do checklist.
5. Atualizar `PROJETO.md` (estado passa pra "em execução").
6. Salvar checklist em `<pasta-do-projeto-ativo>/00-contexto/onboarding.md`.

## Saídas

Checklist de onboarding com responsáveis e prazos.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/00-contexto/`.

## Regras

- Onboarding nunca pula direto pra produção sem alinhar expectativas.
- Todo item do checklist tem responsável.

## Critérios de qualidade

Cliente sai do onboarding sabendo exatamente o que esperar e quando.

## Critérios de validação

`PROJETO.md` atualizado com estado correto ao final.

## Limitações

Não substitui o diagnóstico completo (`diagnostico-completo`) se o
projeto ainda não tiver passado por ele.

## Contrato de handoff

Encaminha pra `diagnostico-completo` (se ainda não rodou) ou direto pro
módulo de execução do escopo fechado.

## Exemplos de gatilhos positivos

- "Fecha o onboarding desse cliente novo"
- "O que preciso fazer agora que o cliente assinou"

## Exemplos de gatilhos negativos

- "Atende essa dúvida do cliente que já é nosso há 1 ano" (é
  `atendimento`)
