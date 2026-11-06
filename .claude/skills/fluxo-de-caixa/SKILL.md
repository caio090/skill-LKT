---
name: fluxo-de-caixa
description: >
  Organiza entradas e saídas por período, calcula saldo projetado e de
  capital de giro, e explica em linguagem simples o que o fluxo de caixa
  significa pra decisão do dono. Use quando o usuário pedir "como está
  meu fluxo de caixa", "vou ter caixa pra pagar isso mês que vem",
  "preciso de capital de giro".
---

# fluxo-de-caixa — Fluxo de caixa e capital de giro

## Quando usar

Análise de entrada/saída por período (diário, semanal, mensal) e
decisão sobre capacidade de pagamento.

## Quando não usar

Análise de lucro/prejuízo por competência (isso é `dre`, regime
diferente do caixa).

## Entradas

Transações normalizadas (`ler-planilha`) ou lançamentos informados
diretamente.

## Dependências

`schemas/financeiro/transacao.schema.json`.

## Contexto que deve ser carregado

Histórico financeiro do cliente/projeto ativo, se existir.

---

## Workflow

1. Agrupar transações por data de pagamento/recebimento (regime de
   caixa, não competência).
2. Calcular saldo inicial, entradas, saídas, saldo final por período.
3. **Capital de giro:** calcular quanto o negócio precisa ter disponível
   pra cobrir a operação entre o pagamento de despesas e o recebimento
   de vendas — explicar isso em linguagem simples ("você paga
   fornecedor em 30 dias mas recebe em 60 — precisa de X pra cobrir
   esse intervalo").
4. Projetar saldo futuro com base em contas já previstas (a
   pagar/receber) — marcar isso como projeção, nunca certeza.
5. Sinalizar risco: algum período com saldo projetado negativo.
6. Explicar o que o número significa — nunca só a tabela, sempre com
   leitura ("esse mês o caixa aperta por causa de X").
7. Salvar em `<pasta-do-projeto-ativo>/03-financeiro/fluxo-de-caixa.md`.

## Saídas

Tabela de fluxo por período + explicação + alerta de saldo negativo
projetado + estimativa de capital de giro necessário.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/03-financeiro/`.

## Regras

- Regime de caixa (data de pagamento/recebimento real), nunca confundir
  com competência.
- Projeção sempre marcada como projeção, com premissas explícitas.
- Nunca esconder um saldo negativo projetado — alertar mesmo que
  ninguém pergunte.

## Critérios de qualidade

Toda leitura de número vem acompanhada de explicação do que significa
pra decisão do dono.

## Critérios de validação

Soma de entradas/saídas por período bate com o total das transações de
origem.

## Limitações

Depende da qualidade/completude do dado de entrada — se faltar
transação, o fluxo fica incompleto e isso deve ser dito.

## Contrato de handoff

Encaminha pra `projecao-financeira` (cenários futuros) e `dre` (visão de
lucro por competência).

## Exemplos de gatilhos positivos

- "Como está meu fluxo de caixa esse mês"
- "Vou ter caixa pra pagar o fornecedor semana que vem"

## Exemplos de gatilhos negativos

- "Qual foi meu lucro esse mês" (é `dre`)
