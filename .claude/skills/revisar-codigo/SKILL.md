---
name: revisar-codigo
description: >
  Revisa uma mudança de código específica: correção, simplificação,
  segurança, aderência ao padrão do projeto. Use quando o usuário pedir
  "revisa esse código", "esse PR está bom pra mergear".
---

# revisar-codigo — Revisão de código

## Quando usar

Mudança de código específica (arquivo, função, PR) pronta pra revisão.

## Quando não usar

Auditoria ampla do repositório inteiro → `auditar-repositorio`.

## Entradas

Código/diff a revisar.

## Dependências

Convenções do projeto (se documentadas em `arquitetura-de-software`).

## Contexto que deve ser carregado

Padrões de arquitetura do projeto ativo, se existirem.

---

## Workflow

1. Correção: o código faz o que deveria, sem efeito colateral óbvio.
2. Simplificação: existe jeito mais simples de resolver o mesmo
   problema, sem abstração desnecessária.
3. Segurança: input de usuário validado nas bordas, sem injeção óbvia.
4. Aderência ao padrão do projeto (nomenclatura, estrutura).
5. Reportar achados por severidade (crítico, importante, sugestão).

## Saídas

Lista de achados priorizados, sem aplicar correção sozinha (a menos que
o usuário peça explicitamente pra corrigir).

## Caminho de salvamento

Não gera arquivo — resposta em conversa, ou registrado no PR/commit se
o fluxo do projeto exigir.

## Regras

- Não aplicar mudança sem o usuário pedir explicitamente.
- Achado de segurança sempre reportado, mesmo que pequeno.

## Critérios de qualidade

Todo achado tem localização exata e explicação do porquê é um problema.

## Critérios de validação

Nenhuma sugestão de simplificação muda o comportamento do código sem
avisar isso explicitamente.

## Limitações

Não roda o código nem tem certeza absoluta de comportamento em runtime
sem executar — reportar quando a análise é só estática.

## Contrato de handoff

Encaminha pra `qa` (testes) e `depurar-erro` (se identificar bug ativo).

## Exemplos de gatilhos positivos

- "Revisa esse código antes de eu mergear"
- "Esse PR está bom?"

## Exemplos de gatilhos negativos

- "Audita o repositório inteiro" (é `auditar-repositorio`)
