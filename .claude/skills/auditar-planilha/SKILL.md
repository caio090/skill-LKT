---
name: auditar-planilha
description: >
  Audita uma planilha financeira já lida (ler-planilha): mapeia fórmulas
  com erro, referências quebradas, abas ocultas, inconsistências de
  status/categoria, e explica o que descobriu — sem corrigir nada
  sozinha. Use quando o usuário pedir "audita essa planilha", "por que
  esse número está estranho", "essa aba oculta tem erro".
---

# auditar-planilha — Auditoria de erros e inconsistências

## Quando usar

Depois de `ler-planilha`, quando houver fórmula com erro, aba oculta
suspeita, ou número que não bate com o esperado.

## Quando não usar

Planilha nova ainda não lida — rodar `ler-planilha` primeiro.

## Entradas

Dado normalizado de `ler-planilha` + acesso à planilha original (só
leitura).

## Dependências

`ler-planilha`, `schemas/financeiro/*`.

## Contexto que deve ser carregado

Mapeamento de colunas já feito por `ler-planilha`.

---

## Workflow

1. Listar toda fórmula com erro (`#REF!`, `#DIV/0!`, `#N/A`) — quantas,
   em qual aba, e (se possível) a que fórmula/aba elas deveriam
   referenciar originalmente.
2. **Não corrigir no escuro.** Antes de propor correção, descobrir qual
   era o mapeamento esperado (ex.: uma aba oculta com `VLOOKUP` quebrado
   provavelmente apontava pra uma aba/tabela que mudou de nome ou
   estrutura — investigar isso antes de sugerir fórmula nova).
3. Checar se o erro afeta resultados visíveis (dashboard, total) ou fica
   isolado numa aba de apoio.
4. Checar inconsistência de texto usada em fórmula (`SE(status="Concluído"...)`
   vs. variações de caixa/acento) — isso pode fazer linha ser contada no
   mês/ano errado.
5. Verificar padrões tipo `VLOOKUP(...,Tabela1[...],...)` — confirmar se
   a tabela nomeada ainda existe e se a referência é válida no Excel
   real (não só no texto da fórmula).
6. Registrar tudo num relatório: quantidade de erros, localização,
   causa provável, impacto, e uma proposta de correção **para
   aprovação** — nunca aplicar sozinha.

## Saídas

`<pasta-do-projeto-ativo>/03-financeiro/auditoria-planilha-<nome>.md`
com lista de problemas, causa provável, impacto e proposta de correção.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/03-financeiro/`.

## Regras

- Nunca corrigir a planilha original.
- Nunca corrigir fórmula sem antes explicar a causa provável e pedir
  aprovação.
- Nunca tratar estimativa/suposição como se fosse a causa confirmada do
  erro — marcar como hipótese até confirmar.

## Critérios de qualidade

Todo erro relatado tem localização exata (aba, célula/fórmula) e causa
provável justificada.

## Critérios de validação

Nenhuma correção aplicada sem aprovação explícita registrada.

## Limitações

Não tem acesso a rodar a planilha no Excel real — análise é sobre o
texto/estrutura extraída; recomendar conferência manual quando a dúvida
não puder ser resolvida só pela leitura.

## Contrato de handoff

Encaminha pra `calculo-cmv`/`precificacao`/`dre` só depois que os erros
relevantes estiverem esclarecidos (ou explicitamente aceitos como
limitação conhecida).

## Exemplos de gatilhos positivos

- "Audita essa planilha de precificação"
- "Por que essa aba oculta tem erro de referência"

## Exemplos de gatilhos negativos

- "Cria uma planilha nova" (é `criar-planilha`)
