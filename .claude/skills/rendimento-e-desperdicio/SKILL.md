---
name: rendimento-e-desperdicio
description: >
  Calcula rendimento de insumo/preparo/porcionamento e mede perdas
  (limpeza, corte, cocção, validade, erro, sobra, porção acima do
  padrão), explicando o impacto financeiro e registrando causas e plano
  de redução. Use quando o usuário pedir "quanto eu perco de insumo",
  "meu desperdício está alto", "calcula o rendimento desse ingrediente".
---

# rendimento-e-desperdicio — Rendimento e perdas

## Quando usar

Quando a ficha técnica indicar rendimento baixo, ou quando o dono achar
que está perdendo dinheiro com desperdício sem saber onde.

## Quando não usar

Cálculo isolado de custo de receita já com rendimento definido → esse é
o papel de `ficha-tecnica`; esta skill foca na origem/redução da perda.

## Entradas

Dados de compra, uso e descarte de insumos.

## Dependências

`ficha-tecnica`, `schemas/gestao-de-negocio/perda.schema.json`.

## Contexto que deve ser carregado

Fichas técnicas existentes dos produtos afetados.

---

## Workflow

1. Calcular (reaproveitando fórmulas de `ficha-tecnica` quando
   aplicável):
   ```
   rendimento aproveitável = peso líquido ÷ peso bruto
   percentual de perda = (peso bruto − peso líquido) ÷ peso bruto × 100
   ```
2. Classificar a perda por causa: limpeza, corte, cocção, validade,
   erro, sobra, porção acima do padrão.
3. Para cada causa, calcular impacto financeiro:
   ```
   valor da perda = quantidade perdida × custo unitário do insumo
   ```
4. Registrar causas prováveis com base em evidência (não acusar sem
   dado — "porção 20% acima do padrão em 3 conferências" é evidência;
   "acho que estão exagerando" não é).
5. Propor plano de redução (padronizar porcionamento, treinar equipe,
   ajustar compra, revisar fornecedor) com responsável e prazo.
6. Salvar em `<pasta-do-projeto-ativo>/03-financeiro/perdas-<periodo>.md`.

## Saídas

Relatório de perdas por causa, impacto financeiro, plano de redução.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/03-financeiro/`.

## Regras

- Nunca estimar percentual de desperdício sem dado real — pedir
  contagem/registro antes de afirmar número.
- Toda causa apontada precisa de evidência, não suposição.

## Critérios de qualidade

Cada causa de perda tem impacto financeiro calculado, não só descrito.

## Critérios de validação

Soma das perdas por causa bate com a perda total observada no período.

## Limitações

Depende de registro real de perda — sem isso, só estima a partir da
diferença entre CMV teórico e real (ver `cmv-real-e-teorico`).

## Contrato de handoff

Encaminha pra `cmv-real-e-teorico` (comparação agregada) e
`estoque-food-service` (se a perda for por vencimento/estoque parado).

## Exemplos de gatilhos positivos

- "Quanto estou perdendo de insumo por mês"
- "Meu desperdício de carne está alto, por quê"

## Exemplos de gatilhos negativos

- "Qual o custo dessa receita" (é `ficha-tecnica`)
