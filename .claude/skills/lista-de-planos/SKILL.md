---
name: lista-de-planos
description: >
  Gera a shot list (lista de planos) técnica a partir do storyboard,
  pronta pra equipe de câmera usar no set — ordem de captura, tipo de
  plano, lente sugerida, movimento de câmera. Use quando o usuário pedir
  "monta a shot list", "lista de planos pra gravação".
---

# lista-de-planos — Shot list

## Quando usar

Dia de gravação, complementando `plano-de-captacao` com o detalhe
técnico de câmera.

## Quando não usar

Antes do storyboard existir.

## Entradas

Storyboard.

## Dependências

`storyboard`, `plano-de-captacao` (ordem de gravação).

## Contexto que deve ser carregado

Storyboard e cronograma de produção.

---

## Workflow

1. Pra cada plano do storyboard: tipo (geral/médio/close/detalhe),
   movimento de câmera (fixo, pan, travelling), lente sugerida (se a
   equipe usar isso).
2. Ordenar pela sequência de gravação real (`plano-de-captacao`), não
   pela ordem do roteiro.
3. Marcar planos de segurança (cobertura extra, caso o principal não
   funcione na edição).
4. Salvar em `<pasta-do-projeto-ativo>/06-audiovisual/shot-list.md`.

## Saídas

Shot list ordenada pra gravação.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/06-audiovisual/`.

## Regras

- Ordem de captura, não ordem do roteiro final.
- Sempre incluir pelo menos um plano de segurança por cena crítica.

## Critérios de qualidade

Equipe de câmera executa sem precisar reconsultar o storyboard
constantemente.

## Critérios de validação

Toda cena do storyboard aparece na shot list.

## Limitações

Não substitui o storyboard — é o detalhamento técnico complementar.

## Contrato de handoff

Encaminha pra `direcao-de-cena` (execução).

## Exemplos de gatilhos positivos

- "Monta a shot list pra gravação de amanhã"
- "Lista de planos técnica pra equipe de câmera"

## Exemplos de gatilhos negativos

- "Detalha o storyboard" (é `storyboard`)
