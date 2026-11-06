---
name: proposta-completa
description: >
  Orquestra o caminho completo até uma proposta comercial: diagnóstico
  rápido, posicionamento, oferta, precificação e documento final —
  encadeando as skills de diagnóstico, produto e comercial. Use quando o
  usuário pedir "monta uma proposta completa pra esse lead do zero",
  "preciso de diagnóstico e proposta juntos pra esse prospect".
---

# proposta-completa — Orquestrador de diagnóstico até proposta

## Quando usar

Lead qualificado que precisa de proposta bem fundamentada, não só um
documento com preço solto.

## Quando não usar

Cliente já com oferta e preço definidos, só precisando do documento →
`proposta-comercial` direto.

## Entradas

Lead qualificado, informações levantadas até agora.

## Dependências

`diagnostico-negocio` (versão enxuta), `posicionamento`,
`criar-produto-e-oferta`, `precificacao`, `proposta-comercial`.

## Contexto que deve ser carregado

Memória do lead/cliente, se já existir.

---

## Workflow

1. Diagnóstico rápido do lead (contexto, dor, urgência) — versão
   enxuta de `diagnostico-negocio`, não o pacote completo de projeto.
2. Confirmar posicionamento/oferta aplicável (reaproveitar se já
   existir para esse segmento).
3. `precificacao` — validar viabilidade do preço antes de propor.
4. `proposta-comercial` — montar a proposta final.
5. Encaminhar pra `texto-natural-pt-br`.

## Saídas

Proposta comercial fundamentada em diagnóstico real, não em preço
solto.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/05-comercial/propostas/` (ou
`workspaces/clientes/<cliente>/arquivos/` se ainda não houver projeto formal).

## Regras

- Preço da proposta sempre passa por `precificacao` antes de ser
  enviado.
- Diagnóstico rápido não substitui `diagnostico-completo` se o lead
  virar cliente — nesse caso, `novo-projeto` + `diagnostico-completo`
  rodam depois, à parte.

## Critérios de qualidade

Proposta reflete a dor/contexto real do lead, não um template genérico.

## Critérios de validação

Preço da proposta é rastreável à precificação validada.

## Limitações

Diagnóstico aqui é enxuto — não substitui o diagnóstico completo do
projeto se o lead fechar.

## Contrato de handoff

Se o lead fechar, encaminha pra `novo-projeto` e `onboarding-de-cliente`.

## Exemplos de gatilhos positivos

- "Monta uma proposta completa pra esse lead do zero"
- "Preciso de diagnóstico e proposta juntos pra esse prospect"

## Exemplos de gatilhos negativos

- "Só formata a proposta, já sei o preço" (é `proposta-comercial`
  direto)
