---
name: arquitetura-de-software
description: >
  Define a arquitetura técnica de um sistema/app: componentes, stack,
  integrações, estratégia de deploy, versionamento e plano de migração
  quando aplicável. Use quando o usuário pedir "define a arquitetura
  desse sistema", "qual stack usar", "como estruturar o deploy".
---

# arquitetura-de-software — Arquitetura técnica

## Quando usar

Depois de `app-e-sistema` levantar escopo/dados/integrações, antes de
implementar.

## Quando não usar

Sistema já implementado só precisando de ajuste pontual → editar
direto ou `revisar-codigo`.

## Entradas

Escopo, dados e integrações de `app-e-sistema`.

## Dependências

`app-e-sistema`, `planejar-banco-de-dados`.

## Contexto que deve ser carregado

Escopo técnico do projeto ativo.

---

## Workflow

1. Escolher stack (linguagem, framework) coerente com a equipe/
   manutenibilidade — não a mais nova por ser nova, a que a equipe
   consegue manter.
2. Definir componentes principais (frontend, backend, banco,
   integrações externas) e como conversam entre si.
3. **Deploy:** ambiente (produção, staging), como o deploy acontece
   (manual ou CI/CD), sem nunca configurar deploy automático que dependa
   de push sem revisão humana.
4. **Versionamento:** estratégia de branch, convenção de commit.
5. **Migração** (se for sistema legado): plano de transição sem
   quebrar o que já funciona, com etapas reversíveis.
6. Salvar em `<pasta-do-projeto-ativo>/07-tecnologia/arquitetura.md`.

## Saídas

Arquitetura documentada (stack, componentes, deploy, versionamento,
migração se aplicável).

## Caminho de salvamento

`<pasta-do-projeto-ativo>/07-tecnologia/`.

## Regras

- Stack escolhida pela capacidade real de manutenção, não modismo.
- Deploy sempre com revisão humana antes de ir pra produção — nunca
  100% automático sem esse gate.
- Migração sempre com etapas reversíveis.

## Critérios de qualidade

Arquitetura é compreensível por outro desenvolvedor sem precisar
perguntar ao autor original.

## Critérios de validação

Toda integração externa listada em `app-e-sistema` está coberta na
arquitetura.

## Limitações

Não implementa o código — define a estrutura que `revisar-codigo`/
implementação seguem.

## Contrato de handoff

Encaminha pra `planejar-banco-de-dados`, `integrar-api`, `qa`.

## Exemplos de gatilhos positivos

- "Define a arquitetura desse sistema novo"
- "Qual stack usar pra esse projeto"

## Exemplos de gatilhos negativos

- "Corrige esse bug" (é `depurar-erro`)
