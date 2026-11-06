---
name: producao-audiovisual-completa
description: >
  Orquestra a produção audiovisual completa: briefing, conceito,
  roteiro, storyboard, lista de planos, plano de captação, direção de
  cena, briefing de edição e distribuição — encadeando as skills
  menores do módulo audiovisual. Use quando o usuário pedir "quero
  produzir um vídeo do zero", "pacote completo de produção audiovisual".
---

# producao-audiovisual-completa — Orquestrador audiovisual

## Quando usar

Produção nova que precisa do ciclo completo, não uma etapa isolada.

## Quando não usar

Vídeo curto de rede social simples → `roteiro` (módulo de conteúdo)
sozinho já resolve.

## Entradas

Motivo/objetivo da produção.

## Dependências

`briefing-audiovisual`, `roteiro-audiovisual`, `storyboard`,
`lista-de-planos`, `plano-de-captacao`, `direcao-de-cena`,
`briefing-de-edicao`, `plano-de-distribuicao`.

## Contexto que deve ser carregado

`.lkt-system/estado/contexto-ativo.json` para o projeto ativo.

---

## Workflow

1. `briefing-audiovisual` — objetivo, mensagem, público, formato,
   orçamento, prazo, critério de aprovação.
2. Conceito criativo (linha visual/narrativa).
3. `roteiro-audiovisual`.
4. `storyboard`.
5. `lista-de-planos`.
6. `plano-de-captacao` (cronograma, equipamento, equipe, áudio,
   continuidade, orçamento).
7. `direcao-de-cena` (execução no dia).
8. `briefing-de-edicao` (pós-produção, versões por formato).
9. `plano-de-distribuicao` (onde/quando publicar + relatório de
   desempenho depois).

Mostrar resumo curto ao final de cada etapa antes de seguir.

## Saídas

Produção completa documentada, do briefing à distribuição.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/06-audiovisual/`.

## Regras

- Nunca pular etapa — mesmo produção simples passa pelo briefing antes
  do roteiro.
- Publicação sempre via `aprovar-post`, nunca automática.

## Critérios de qualidade

Cada etapa aplicável executada ou descartada com motivo.

## Critérios de validação

Critério de aprovação do briefing original é o que valida a entrega
final.

## Limitações

Não substitui equipe de produção real — organiza e documenta o
processo.

## Contrato de handoff

`anti-chat` (quality gate final antes da distribuição),
`plano-de-distribuicao` (publicação) e `relatorio-de-marketing` (se
entrar no consolidado).

## Exemplos de gatilhos positivos

- "Quero produzir um vídeo institucional do zero"
- "Pacote completo de produção audiovisual pro lançamento"

## Exemplos de gatilhos negativos

- "Só escreve um roteiro de reels" (é `roteiro`, módulo de conteúdo)
