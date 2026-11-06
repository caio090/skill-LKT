---
name: plano-de-campanha
description: >
  Planeja uma campanha específica (lançamento, sazonal, promocional):
  objetivo, público, oferta, mensagem, canais, orçamento, cronograma,
  peças necessárias, responsáveis, métricas e riscos. Use quando o
  usuário pedir "planeja essa campanha de lançamento", "monta a campanha
  do dia das mães".
---

# plano-de-campanha — Planejamento de campanha

## Quando usar

Antes de produzir peças de uma campanha específica (não o marketing
contínuo — isso é `estrategia-de-marketing`/`calendario-de-conteudo`).

## Quando não usar

Conteúdo recorrente sem campanha específica associada.

## Entradas

Motivo da campanha (lançamento, data sazonal, promoção), estratégia de
marketing já definida.

## Dependências

`estrategia-de-marketing`, `criar-produto-e-oferta` (se houver oferta
específica), `analisar-promocao-cupom` (se houver desconto).

## Contexto que deve ser carregado

Estratégia de marketing e posicionamento do projeto ativo.

---

## Workflow

1. Objetivo específico da campanha.
2. Público (pode ser subconjunto do público geral).
3. Oferta da campanha (se houver desconto/condição especial, encaminhar
   pra `analisar-promocao-cupom` pra validar viabilidade).
4. Mensagem central da campanha (derivada do posicionamento).
5. Canais e formato de cada peça.
6. Orçamento (mídia + produção).
7. Cronograma (datas de cada peça/publicação).
8. Responsáveis por cada entrega.
9. Métricas de sucesso.
10. Riscos (o que pode fazer a campanha não performar).
11. Salvar em `<pasta-do-projeto-ativo>/04-marketing/campanha-<nome>.md`.

## Saídas

Plano de campanha completo (11 itens do workflow).

## Caminho de salvamento

`<pasta-do-projeto-ativo>/04-marketing/`.

## Regras

- Toda campanha com desconto passa por `analisar-promocao-cupom` antes
  de ser aprovada.
- Cronograma sempre com datas específicas, não "ao longo do mês".

## Critérios de qualidade

Toda peça do cronograma tem responsável e prazo.

## Critérios de validação

Métricas de sucesso são mensuráveis e ligadas ao objetivo do item 1.

## Limitações

Não produz as peças — aciona `carrossel`, `publicar-tema`, `roteiro`,
`anuncio-meta`, `anuncio-google` conforme o formato definido.

## Contrato de handoff

Encaminha pras skills de produção conforme cada peça do cronograma, e
pra `campanha-completa` se for um pacote completo do zero.

## Exemplos de gatilhos positivos

- "Planeja a campanha de lançamento desse produto"
- "Monta a campanha do dia das mães"

## Exemplos de gatilhos negativos

- "Cria só um post avulso" (sem campanha, é conteúdo direto)
