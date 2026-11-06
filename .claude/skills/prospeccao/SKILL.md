---
name: prospeccao
description: >
  Planeja abordagem de prospecção ativa (outbound): lista de alvos
  reais, canal de abordagem, mensagem inicial. Use quando o usuário
  pedir "quero prospectar clientes novos", "monta uma lista de
  prospecção".
---

# prospeccao — Prospecção ativa

## Quando usar

Negócio que precisa buscar cliente ativamente (outbound), não só
esperar lead chegar (inbound).

## Quando não usar

Lead que já chegou por conta própria → `qualificar-lead`.

## Entradas

Perfil de cliente-alvo (`analisar-publico`), canal disponível
(WebSearch, LinkedIn, indicação).

## Dependências

`analisar-publico`, `pesquisa-mercado`.

## Contexto que deve ser carregado

Perfil de público-alvo do projeto ativo.

---

## Workflow

1. Definir perfil de alvo específico (não "qualquer empresa").
2. Levantar lista real de alvos (via WebSearch quando aplicável) — nunca
   inventar nome de empresa/contato.
3. Definir canal de abordagem (email, WhatsApp, LinkedIn, telefone).
4. Escrever mensagem inicial (`script-comercial` ou
   `email-profissional`/`mensagem-whatsapp` conforme o canal).
5. Registrar cada alvo no CRM como novo lead.

## Saídas

Lista de alvos + mensagem inicial + registro no CRM.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/05-comercial/prospeccao-<data>.md`.

## Regras

- Nunca inventar contato/empresa — só listar o que foi encontrado de
  verdade.
- Mensagem inicial específica ao perfil do alvo, não genérica em massa.

## Critérios de qualidade

Cada alvo da lista é verificável (fonte real).

## Critérios de validação

Lista de alvos bate com o perfil definido no Passo 1.

## Limitações

Não substitui ferramenta de prospecção em escala (LinkedIn Sales
Navigator, etc.) — organiza a abordagem manual/pequena escala.

## Contrato de handoff

Encaminha pra `script-comercial`, `email-profissional` ou
`mensagem-whatsapp` conforme canal, e `qualificar-lead` na resposta.

## Exemplos de gatilhos positivos

- "Quero prospectar clientes novos nesse nicho"
- "Monta uma lista de empresas pra abordar"

## Exemplos de gatilhos negativos

- "Qualifica esse lead que já respondeu" (é `qualificar-lead`)
