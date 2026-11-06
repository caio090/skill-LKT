---
name: criar-produto-e-oferta
description: >
  Estrutura ou refina um produto/serviço e sua oferta comercial (o que
  inclui, preço, condição, garantia) com base no diagnóstico, público e
  posicionamento do cliente/projeto. Use quando o usuário pedir "estrutura
  essa oferta", "monta um novo produto/serviço", "como devo empacotar
  isso".
---

# criar-produto-e-oferta — Produto e oferta comercial

## Quando usar

Quando o diagnóstico apontar que a oferta atual não está clara, não
converte, ou quando o cliente quer lançar algo novo.

## Quando não usar

- Definir preço a partir de custos reais (CMV, margem) → módulo
  financeiro (`precificacao`, `calcular-cmv`) — esta skill define o
  pacote/proposta de valor, não o cálculo de custo.

## Entradas

Diagnóstico, público, posicionamento já levantados.

## Dependências

`posicionamento`, `analisar-publico`. Módulo financeiro pra validar
viabilidade de preço quando existir.

## Contexto que deve ser carregado

Diagnóstico e posicionamento do projeto ativo.

---

## Workflow

1. O que o produto/serviço resolve, de verdade, pro público já mapeado.
2. O que inclui (escopo) e o que não inclui.
3. Como se compara com a concorrência mapeada — diferencial claro.
4. Faixa de preço proposta (marcado como proposta, não fechado, até
   passar pela validação financeira).
5. Condições (garantia, forma de pagamento, prazo de entrega).
6. Salvar em `<pasta-do-projeto-ativo>/02-estrategia/oferta.md`.
7. Se houver dúvida sobre viabilidade financeira do preço proposto,
   encaminhar pro módulo financeiro antes de considerar fechado.

## Saídas

`02-estrategia/oferta.md`.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/02-estrategia/`.

## Regras

- Preço proposto aqui é sempre marcado como proposta até validação
  financeira confirmar viabilidade (margem, ponto de equilíbrio).
- Escopo da oferta tem que ser específico — "consultoria completa" sem
  detalhar o que inclui não é oferta, é vago.

## Critérios de qualidade

Oferta tem escopo, preço proposto e diferencial claros e específicos.

## Critérios de validação

Preço proposto foi confrontado com custo real (quando módulo financeiro
disponível) antes de virar oferta final.

## Limitações

Não substitui o cálculo financeiro de viabilidade — só propõe o pacote
comercial.

## Contrato de handoff

Encaminha pro módulo financeiro (viabilidade de preço) e pra
`plano-estrategico`/`estrategia-de-marketing` (como comunicar a oferta).

## Exemplos de gatilhos positivos

- "Estrutura essa oferta de assinatura"
- "Como devo empacotar esse serviço novo"

## Exemplos de gatilhos negativos

- "Calcula o preço com base no meu custo" (é `precificacao`, financeiro)
