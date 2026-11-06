---
name: depurar-erro
description: >
  Investiga e corrige um erro/bug específico: reproduz, localiza causa
  raiz, corrige, e confirma que não quebrou outra coisa. Use quando o
  usuário pedir "corrige esse bug", "por que isso está dando erro".
---

# depurar-erro — Depuração de bug

## Quando usar

Erro/comportamento específico reportado, com ou sem mensagem de erro.

## Quando não usar

Diagnóstico amplo sem bug específico → `diagnostico-tecnico`.

## Entradas

Descrição do erro, mensagem de erro/stack trace se houver, passos pra
reproduzir.

## Dependências

Nenhuma obrigatória.

## Contexto que deve ser carregado

Arquitetura do sistema, se documentada.

---

## Workflow

1. Reproduzir o erro (ou entender exatamente quando ele acontece, se
   não for reproduzível diretamente).
2. Localizar a causa raiz — não parar no primeiro sintoma.
3. Avaliar o impacto de corrigir (o que mais usa esse código).
4. Corrigir a causa raiz, não só o sintoma.
5. Confirmar que a correção não quebrou outro comportamento (rodar
   testes existentes, se houver).
6. Documentar a causa e a correção, se for um bug não óbvio (ajuda
   quem encontrar de novo).

## Saídas

Correção aplicada + explicação da causa raiz.

## Caminho de salvamento

Direto no código do projeto. Se for bug recorrente/não óbvio, registrar
em `<pasta-do-projeto-ativo>/07-tecnologia/bugs-conhecidos.md`.

## Regras

- Corrigir causa raiz, nunca só o sintoma.
- Nunca aplicar correção sem entender por que o bug acontecia.

## Critérios de qualidade

Explicação da causa é verificável (aponta o código exato responsável).

## Critérios de validação

Erro não se reproduz mais depois da correção.

## Limitações

Sem ambiente de execução real, a depuração pode ficar limitada à
análise estática do código — reportar essa limitação quando aplicável.

## Contrato de handoff

Encaminha pra `qa` (teste de regressão) e `revisar-codigo` (revisão da
correção).

## Exemplos de gatilhos positivos

- "Corrige esse bug que está dando erro 500"
- "Por que essa função está retornando valor errado"

## Exemplos de gatilhos negativos

- "Faz um diagnóstico geral do sistema" (é `diagnostico-tecnico`)
