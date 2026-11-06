---
name: atendimento
description: >
  Responde dúvidas/solicitações de clientes já ativos, e cobre retenção
  (identificar risco de cancelamento e agir) e análise de churn (por que
  clientes saem). Use quando o usuário pedir "responde essa dúvida do
  cliente", "esse cliente parece insatisfeito", "por que estamos
  perdendo clientes".
---

# atendimento — Atendimento, retenção e churn

## Quando usar

Cliente já ativo com dúvida/solicitação, sinal de insatisfação, ou
análise de por que clientes cancelam.

## Quando não usar

Cliente novo em processo de fechamento → `script-comercial`/
`onboarding-de-cliente`.

## Entradas

Dúvida/mensagem do cliente, ou dados de cancelamento (para churn).

## Dependências

`_memoria/preferencias.md`, `CLIENTE.md`.

## Contexto que deve ser carregado

Histórico do cliente (`CLIENTE.md`, decisões anteriores).

---

## Workflow

### Modo: Atendimento

1. Entender a dúvida/solicitação real (não responder genérico).
2. Responder no tom da marca, resolvendo ou encaminhando pra quem
   resolve.
3. Registrar se for algo recorrente (candidato a `criar-sop` ou FAQ).

### Modo: Retenção

1. Identificar sinal de risco (queda de uso, reclamação, silêncio
   incomum).
2. Agir proativamente — contato antes do cancelamento, não depois.
3. Entender a causa raiz antes de oferecer solução genérica (desconto
   não resolve problema de produto/atendimento).

### Modo: Análise de churn

1. Levantar clientes que cancelaram no período e o motivo declarado
   (ou inferido com evidência).
2. Agrupar por causa (preço, atendimento, produto, concorrência, uso).
3. Recomendar ação pra reduzir a causa mais frequente.
4. Salvar em `<pasta-do-projeto-ativo>/09-relatorios/churn-<periodo>.md`.

## Saídas

Resposta ao cliente, plano de retenção, ou análise de churn com causas e
recomendação.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/09-relatorios/` (churn) ou direto na conversa
(atendimento pontual).

## Regras

- Atendimento nunca genérico — resolve ou encaminha de verdade.
- Causa de churn baseada em evidência (motivo declarado ou padrão
  observável), não suposição.

## Critérios de qualidade

Toda causa de churn agrupada tem pelo menos um caso real que a
sustenta.

## Critérios de validação

Recomendação de retenção ataca a causa raiz, não sintoma.

## Limitações

Não substitui contato humano direto em casos delicados — prepara a
resposta, decisão final de tom é do responsável.

## Contrato de handoff

Encaminha pra `criar-sop` (se virar processo recorrente) e
`plano-estrategico` (se o churn apontar problema estrutural).

## Exemplos de gatilhos positivos

- "Responde essa dúvida do cliente"
- "Por que estamos perdendo clientes esse trimestre"

## Exemplos de gatilhos negativos

- "Fecha o onboarding desse cliente novo" (é `onboarding-de-cliente`)
