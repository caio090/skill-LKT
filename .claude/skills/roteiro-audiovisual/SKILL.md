---
name: roteiro-audiovisual
description: >
  Escreve roteiro completo de produção audiovisual: cena, diálogo,
  ação, duração e transição, a partir do briefing. Use quando o usuário
  pedir "escreve o roteiro do comercial", "roteiriza esse institucional".
---

# roteiro-audiovisual — Roteiro de produção

## Quando usar

Depois de `briefing-audiovisual`, produção com mais de um plano/cena.

## Quando não usar

Vídeo curto de rede social sem produção formal → `roteiro` (módulo de
conteúdo).

## Entradas

`briefing-audiovisual` já preenchido.

## Dependências

`briefing-audiovisual`, `_memoria/preferencias.md`.

## Contexto que deve ser carregado

Briefing audiovisual do projeto ativo.

---

## Workflow

1. Estrutura narrativa (abertura, desenvolvimento, fechamento) alinhada
   à mensagem central do briefing.
2. Pra cada cena: ação, diálogo/narração, duração estimada, transição
   pra próxima cena.
3. Marcar onde precisa de depoimento real, produto em uso, ou
   demonstração.
4. Encaminhar pra `texto-natural-pt-br` (diálogo/narração).
5. Salvar em `<pasta-do-projeto-ativo>/06-audiovisual/roteiro.md`.

## Saídas

Roteiro cena a cena.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/06-audiovisual/`.

## Regras

- Toda cena serve à mensagem central do briefing — cortar cena que só
  "fica bonita" sem função narrativa.
- Duração total bate com o formato definido no briefing.

## Critérios de qualidade

Roteiro lido em voz alta bate com a duração estimada do formato.

## Critérios de validação

Toda cena tem ação, diálogo/narração e duração definidos.

## Limitações

Não define enquadramento/plano técnico — isso é `storyboard`/
`lista-de-planos`.

## Contrato de handoff

Encaminha pra `storyboard` e `lista-de-planos`.

## Exemplos de gatilhos positivos

- "Escreve o roteiro do comercial de 30 segundos"
- "Roteiriza esse institucional"

## Exemplos de gatilhos negativos

- "Roteiriza um reels rápido" (é `roteiro`)
