---
name: criar-sop
description: >
  Documenta um processo operacional recorrente em SOP (procedimento
  padrão): passo a passo, responsável, ferramenta, tempo estimado,
  critério de qualidade. Use quando o usuário pedir "documenta esse
  processo", "cria o passo a passo padrão pra isso".
---

# criar-sop — Procedimento operacional padrão

## Quando usar

Processo que se repete e ainda não está documentado, ou que muda de
responsável com frequência (risco de conhecimento se perder).

## Quando não usar

Tarefa única, sem repetição — não vale o esforço de documentar.

## Entradas

Descrição do processo (mesmo que informal/na cabeça de alguém).

## Dependências

`_memoria/processos.md` (ou do cliente) — registrar referência lá.

## Contexto que deve ser carregado

Processos já documentados, pra não duplicar.

---

## Workflow

1. Nomear o processo especificamente (não "atendimento" genérico —
   "responder pedido de orçamento por WhatsApp em até 2h").
2. Passo a passo numerado, cada passo com responsável.
3. Ferramentas usadas em cada passo.
4. Tempo estimado total e por passo.
5. Critério de qualidade (como saber que foi bem feito).
6. O que fazer quando algo sai do padrão (exceção comum).
7. Salvar em `_memoria/processos.md` (referência) e arquivo próprio em
   `<pasta-do-projeto-ativo>/00-contexto/sops/<processo>.md` (ou geral,
   se não for específico de projeto).

## Saídas

SOP documentado, pronto pra treinar qualquer pessoa nova no processo.

## Caminho de salvamento

`_memoria/processos.md` + `sops/<processo>.md`.

## Regras

- Processo nomeado especificamente, nunca genérico.
- Sempre inclui o que fazer na exceção, não só o caminho feliz.

## Critérios de qualidade

Uma pessoa nova consegue seguir o SOP sem perguntar nada além do que
está escrito.

## Critérios de validação

Todo passo tem responsável e ferramenta definidos.

## Limitações

Não substitui treinamento prático — é o material de referência.

## Contrato de handoff

Referenciado por `organizar-projeto` e `onboarding-de-cliente` quando
aplicável.

## Exemplos de gatilhos positivos

- "Documenta esse processo de atendimento"
- "Cria o passo a passo padrão pra fechar o mês financeiro"

## Exemplos de gatilhos negativos

- "Faz isso uma vez só, não precisa documentar" (tarefa pontual, não
  SOP)
