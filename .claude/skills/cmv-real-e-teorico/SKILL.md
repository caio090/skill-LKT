---
name: cmv-real-e-teorico
description: >
  Especialização food service de calcular-cmv: compara CMV real (a partir
  de estoque) com CMV teórico (a partir de vendas × ficha técnica),
  localiza a lacuna e investiga causas prováveis sem acusar sem
  evidência. Use quando o usuário pedir "meu CMV aumentou", "por que meu
  CMV real não bate com o teórico", "compara CMV real e teórico".
---

# cmv-real-e-teorico — CMV real vs. teórico (food service)

Estende `calcular-cmv` (base geral) com a comparação específica de
alimentação, que depende de estoque e ficha técnica.

## Quando usar

Negócio de alimentação com estoque controlado e fichas técnicas
existentes, quando o CMV parece alto ou inconsistente.

## Quando não usar

Sem ficha técnica ou estoque controlado ainda — rodar `ficha-tecnica` e
`estoque-food-service` primeiro.

## Entradas

Estoque inicial/final, compras do período, vendas por produto, fichas
técnicas.

## Dependências

`calcular-cmv`, `ficha-tecnica`, `estoque-food-service`.

## Contexto que deve ser carregado

Fichas técnicas e movimentos de estoque do período.

---

## Workflow

1. **CMV real:**
   ```
   CMV real = estoque inicial + compras − estoque final
   ```
2. **CMV teórico:**
   ```
   CMV teórico = quantidade vendida × custo padrão da ficha técnica
   ```
3. **Lacuna:**
   ```
   lacuna de CMV = CMV real − CMV teórico
   ```
4. Investigar causas possíveis, sem acusar sem evidência: ficha
   desatualizada, porção acima do padrão, perda, vencimento, cortesia,
   consumo interno, erro de compra, erro de contagem, transferência não
   registrada, baixa incorreta, desvio, venda não registrada, unidade de
   medida errada.
5. Pra cada causa possível, indicar que evidência confirmaria ou
   descartaria ela (ex.: "conferir se a ficha do produto X foi
   atualizada depois do último reajuste de preço do fornecedor").
6. Registrar plano de investigação — não uma conclusão definitiva sem
   checagem.
7. Salvar em `<pasta-do-projeto-ativo>/03-financeiro/cmv-real-teorico-<periodo>.md`.

## Saídas

CMV real, CMV teórico, lacuna, lista de causas possíveis com plano de
investigação.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/03-financeiro/`.

## Regras

- Nunca acusar fraude ou desvio sem evidência concreta.
- Lacuna sempre acompanhada de plano de investigação, nunca só
  reportada como número solto.
- Comparação é sempre do próprio negócio ao longo do tempo — nunca
  contra "CMV bom/ruim" de mercado sem fonte.

## Critérios de qualidade

Toda causa possível listada tem uma evidência sugerida pra confirmar ou
descartar.

## Critérios de validação

CMV real recalculado bate com estoque inicial + compras − estoque
final informados.

## Limitações

Depende de estoque e vendas por produto confiáveis — sem isso, a
lacuna calculada pode refletir erro de dado, não de operação.

## Contrato de handoff

Encaminha pra `estoque-food-service` (se a causa for de estoque) ou
`rendimento-e-desperdicio` (se for de perda/porção).

## Exemplos de gatilhos positivos

- "Meu CMV aumentou, por quê"
- "Compara meu CMV real com o teórico desse mês"

## Exemplos de gatilhos negativos

- "Calcula o CMV desse produto novo" (é `ficha-tecnica`/`calcular-cmv`)
