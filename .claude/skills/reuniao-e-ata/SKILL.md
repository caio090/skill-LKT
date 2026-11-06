---
name: reuniao-e-ata
description: >
  Prepara pauta de reunião e/ou documenta ata com decisões e próximos
  passos. Use quando o usuário pedir "prepara a pauta dessa reunião",
  "escreve a ata com o que decidimos".
---

# reuniao-e-ata — Pauta e ata de reunião

## Quando usar

Antes de uma reunião (pauta) ou logo depois (ata).

## Quando não usar

Registro de decisão isolada fora de reunião → direto em
`_memoria/decisoes.md` (via `salvar-local`).

## Entradas

Objetivo da reunião, participantes, ou notas da reunião já realizada.

## Dependências

`_memoria/decisoes.md`, `PROJETO.md`.

## Contexto que deve ser carregado

Pendências e decisões recentes do projeto ativo.

---

## Workflow

### Modo: Pauta

1. Objetivo da reunião.
2. Itens a discutir, com tempo estimado cada.
3. O que cada participante precisa levar preparado.

### Modo: Ata

1. Participantes e data.
2. Decisões tomadas (registrar também em `_memoria/decisoes.md`).
3. Próximos passos com responsável e prazo.
4. Pendências que ficaram em aberto.
5. Salvar em `<pasta-do-projeto-ativo>/00-contexto/atas/<data>.md`.

## Saídas

Pauta ou ata estruturada.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/00-contexto/atas/`.

## Regras

- Decisão de reunião sempre também registrada em `_memoria/decisoes.md`
  (ou do cliente), não só na ata isolada.
- Todo próximo passo tem responsável e prazo.

## Critérios de qualidade

Ata é suficiente pra quem faltou entender o que foi decidido.

## Critérios de validação

Toda decisão da ata está espelhada em `_memoria/decisoes.md`.

## Limitações

Não substitui gravação/transcrição real da reunião — é o resumo
estruturado.

## Contrato de handoff

`organizar-projeto` (próximos passos viram demanda).

## Exemplos de gatilhos positivos

- "Prepara a pauta da reunião de amanhã"
- "Escreve a ata com o que decidimos"

## Exemplos de gatilhos negativos

- "Registra essa decisão que tomamos agora na conversa" (é
  `salvar-local`/direto em `_memoria/decisoes.md`, sem precisar de ata)
