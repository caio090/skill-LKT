---
name: proposta-comercial
description: >
  Monta a proposta comercial para um lead/cliente específico: escopo,
  prazo, investimento e condições, a partir da oferta e do diagnóstico
  daquele lead — e aciona criar-documento para formatar a entrega final.
  Use quando o usuário pedir "monta a proposta pro cliente X", "prepara
  o orçamento pra esse lead".
---

# proposta-comercial — Proposta para lead/cliente específico

## Quando usar

Lead qualificado, pronto para receber proposta formal.

## Quando não usar

Definição geral de produto/oferta (isso é `criar-produto-e-oferta`) —
esta skill aplica a oferta já definida a um caso específico.

## Entradas

Lead qualificado, escopo específico solicitado, oferta/precificação já
definida.

## Dependências

`criar-produto-e-oferta`, `precificacao`, `criar-documento`
(formatação final).

## Contexto que deve ser carregado

Oferta e posicionamento do projeto ativo.

---

## Workflow

1. Confirmar escopo específico pra esse lead (pode variar da oferta
   padrão).
2. Confirmar preço com base em `precificacao`/`criar-produto-e-oferta` —
   nunca dar desconto sem calcular impacto na margem.
3. Definir prazo e condições de pagamento.
4. Montar a proposta usando `templates/proposta/PROPOSTA-COMERCIAL.md`
   como base, via `criar-documento`.
5. Encaminhar pra `texto-natural-pt-br`.
6. Registrar no CRM (`funil-de-vendas`) que a proposta foi enviada.

## Saídas

Proposta comercial formatada, pronta pra envio.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/05-comercial/propostas/`.

## Regras

- Nunca propor desconto sem checar impacto na margem
  (`calcular-cmv`/`precificacao`).
- Escopo da proposta é específico, nunca vago.

## Critérios de qualidade

Preço da proposta é rastreável à precificação validada, não um número
negociado no improviso.

## Critérios de validação

Proposta tem escopo, prazo, investimento e condições — as 4 partes
mínimas.

## Limitações

Não decide a política comercial geral (isso é `criar-produto-e-oferta`)
— aplica a um caso.

## Contrato de handoff

`anti-chat` (quality gate final), `criar-documento` (formatação),
`criar-pdf` (se precisar exportar), `funil-de-vendas` (registro).

## Exemplos de gatilhos positivos

- "Monta a proposta pro cliente X"
- "Prepara o orçamento pra esse lead"

## Exemplos de gatilhos negativos

- "Define a oferta geral do produto" (é `criar-produto-e-oferta`)
