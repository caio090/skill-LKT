---
name: diagnostico-negocio
description: >
  Diagnostica a situação atual de um negócio/cliente: modelo, operação,
  finanças macro, marketing, comercial, o que funciona e o que trava.
  Base de qualquer projeto novo, antes de qualquer plano ou produção. Use
  quando o usuário pedir "faz um diagnóstico de X", "entende esse
  negócio antes de a gente planejar", ou como primeiro passo de
  `novo-projeto`.
---

# diagnostico-negocio — Diagnóstico do negócio/cliente

## Quando usar

Primeiro passo real de qualquer projeto novo, depois da estrutura criada
por `novo-projeto` — nunca pular direto pra plano ou produção.

## Quando não usar

- Ajuste pontual num projeto já diagnosticado — reaproveitar o
  diagnóstico existente em `01-diagnostico/`, não refazer do zero.

## Entradas

- O que já existe em `CLIENTE.md`/`00-contexto/`.
- Respostas do cliente às perguntas de diagnóstico (abaixo).

## Dependências

- `_memoria/empresa.md` (se for projeto interno) ou
  `workspaces/clientes/<cliente>/CLIENTE.md` e `_memoria/` do cliente.
- Encaminha para `pesquisa-mercado`, `analisar-concorrentes`,
  `analisar-publico` quando precisar de dado externo.

## Contexto que deve ser carregado

Memória do cliente/projeto ativo (`.lkt-system/estado/contexto-ativo.json`).

---

## Workflow

1. **Contexto:** o que o negócio faz, há quanto tempo, tamanho da equipe.
2. **Problema real:** por que esse projeto começou agora — o que
   incomoda ou trava.
3. **Situação atual:** o que já é feito hoje em marketing, comercial,
   financeiro, operação (nível macro, sem entrar em números detalhados
   ainda — isso é `03-financeiro` com as skills financeiras).
4. **Público:** quem compra hoje, de fato (encaminhar pra
   `analisar-publico` se precisar de profundidade).
5. **Oferta:** o que vende, pra quem, por quanto.
6. **Concorrência:** quem mais atende esse público (encaminhar pra
   `analisar-concorrentes` se precisar de pesquisa real).
7. **O que funciona:** o que já dá resultado e não deve ser mexido sem
   necessidade.
8. **O que trava:** gargalos concretos, não genéricos ("falta
   marketing" não é diagnóstico — "não tem ninguém respondendo lead em
   menos de 3 dias" é).
9. **Registrar** tudo em `<pasta-do-projeto-ativo>/01-diagnostico/`.

## Saídas

`01-diagnostico/diagnostico.md` com as 8 seções acima.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/01-diagnostico/diagnostico.md`.

## Regras

- Nunca pular direto pra plano de ação sem diagnóstico.
- Gargalo tem que ser concreto e verificável, não uma impressão vaga.
- Se faltar dado, registrar como lacuna — não inventar.

## Critérios de qualidade

- Todo gargalo citado é específico e rastreável a uma evidência (o que o
  cliente disse, o que foi observado).

## Critérios de validação

- As 8 seções do workflow estão preenchidas ou explicitamente marcadas
  como pendentes.

## Limitações

- Não substitui auditoria financeira detalhada (isso é módulo
  financeiro) nem pesquisa de mercado formal (isso é `pesquisa-mercado`).

## Contrato de handoff

Encaminha pra `posicionamento`, `criar-produto-e-oferta` ou
`plano-estrategico`, conforme o que o diagnóstico apontar como
prioridade. Pode encadear com `pesquisa-mercado`,
`analisar-concorrentes`, `analisar-publico` antes de fechar.

## Exemplos de gatilhos positivos

- "Faz um diagnóstico desse negócio"
- "Antes de planejar, entende a situação atual do cliente"

## Exemplos de gatilhos negativos

- "Já sei o problema, só quero o plano" (ainda assim, registrar o
  diagnóstico mínimo — mas se o usuário insistir em pular, seguir e
  registrar a lacuna)
