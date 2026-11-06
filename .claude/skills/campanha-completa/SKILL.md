---
name: campanha-completa
description: >
  Orquestra uma campanha de marketing do zero: contexto, objetivo,
  público, oferta, canais, conceito, peças, mídia, calendário e
  relatório — encadeando as skills de estratégia, conteúdo e ads. Use
  quando o usuário pedir "quero uma campanha completa pro lançamento de
  X", "monta tudo pra essa campanha do zero".
---

# campanha-completa — Orquestrador de campanha

## Quando usar

Campanha nova que precisa de todo o ciclo, não uma peça isolada.

## Quando não usar

Peça avulda sem campanha → skill de produção direto.

## Entradas

Motivo/objetivo da campanha.

## Dependências

`plano-de-campanha`, `carrossel`, `publicar-tema`, `roteiro`,
`anuncio-google`, `anuncio-meta`, `analisar-promocao-cupom`,
`aprovar-post`, `relatorio-de-marketing`.

## Contexto que deve ser carregado

Estratégia de marketing e posicionamento do projeto ativo.

---

## Workflow

1. `plano-de-campanha` — objetivo, público, oferta, mensagem, canais,
   orçamento, cronograma, responsáveis, métricas, riscos.
2. Conceito criativo (linha visual e narrativa da campanha).
3. Peças: `carrossel`/`publicar-tema` (conteúdo orgânico), `roteiro`
   (vídeo curto), conforme o cronograma.
4. Mídia: `anuncio-google` e/ou `anuncio-meta` conforme os canais pagos
   definidos.
5. Se houver desconto/cupom: `analisar-promocao-cupom` antes de aprovar.
6. Calendário de publicação das peças.
7. Aprovação e publicação: `aprovar-post` (nunca push/publicação
   automática).
8. Ao final do período: `relatorio-de-marketing` consolidando resultado
   e aprendizados.
9. Registrar aprendizados em `_memoria/aprendizados.md` (ou do cliente).

## Saídas

Campanha completa documentada + peças + relatório final.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/04-marketing/campanhas/<nome>/`.

## Regras

- Toda campanha registra objetivo, público, oferta, mensagem, canais,
  orçamento, cronograma, peças, responsáveis, métricas, riscos e
  aprendizados — nunca menos que isso.
- `aprovar-post` continua sem push nem publicação automática mesmo
  dentro deste orquestrador.

## Critérios de qualidade

Toda peça é rastreável ao plano de campanha que a originou.

## Critérios de validação

Relatório final compara resultado com métricas definidas no Passo 1.

## Limitações

Não substitui o julgamento criativo humano na aprovação final das
peças — sempre passa por confirmação antes de publicar.

## Contrato de handoff

`anti-chat` (quality gate final das peças) e `relatorio-de-marketing` ao
final; `plano-estrategico` se o resultado exigir replanejamento maior.

## Exemplos de gatilhos positivos

- "Quero uma campanha completa pro lançamento desse produto"
- "Monta tudo pra campanha de fim de ano, do zero"

## Exemplos de gatilhos negativos

- "Só cria um carrossel avulso" (é `carrossel` direto)
