---
name: construir-produto-digital
description: >
  Orquestra a construção de um produto digital do zero: escopo,
  especificação, arquitetura, banco de dados, integrações, interface,
  QA e documentação — encadeando as skills do módulo de tecnologia. Não
  desenvolve o produto real nesta fase — organiza o processo pra quando
  o desenvolvimento acontecer. Use quando o usuário pedir "quero
  construir esse produto digital do zero", "pacote completo de
  desenvolvimento desse app".
---

# construir-produto-digital — Orquestrador de produto digital

## Quando usar

Produto digital novo que precisa do ciclo completo de planejamento
técnico.

## Quando não usar

Ajuste pontual em sistema já existente → skills técnicas isoladas
(`revisar-codigo`, `depurar-erro`).

## Entradas

Objetivo do produto.

## Dependências

`app-e-sistema`, `especificacao-de-produto`, `arquitetura-de-software`,
`planejar-banco-de-dados`, `integrar-api`, `design-front-end`, `qa`,
`documentar-sistema`.

## Contexto que deve ser carregado

`.lkt-system/estado/contexto-ativo.json` para o projeto ativo.

---

## Workflow

1. `app-e-sistema` — escopo, usuários, fluxos, permissões, dados,
   integrações, backlog inicial.
2. `especificacao-de-produto` — especificação, backlog priorizado,
   roadmap.
3. `arquitetura-de-software` — stack, componentes, deploy,
   versionamento.
4. `planejar-banco-de-dados` — modelo de dados.
5. `integrar-api` — cada integração externa necessária.
6. `design-front-end` — direção visual e experiência.
7. Desenvolvimento em si (fora do escopo desta skill — é execução
   humana/de outra ferramenta, não geração de produto real nesta fase).
8. `qa` — teste funcional, segurança básica, observabilidade.
9. `documentar-sistema` — documentação final.

Mostrar resumo curto ao final de cada etapa antes de seguir.

## Saídas

Todo o planejamento técnico documentado em `07-tecnologia/`, pronto pra
implementação.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/07-tecnologia/`.

## Regras

- Não implementa/gera o produto real nesta fase — cria a estrutura de
  planejamento.
- Nunca pula etapa (mesmo produto simples passa por escopo antes de
  arquitetura).

## Critérios de qualidade

Cada etapa aplicável executada ou descartada com motivo.

## Critérios de validação

Backlog final é rastreável à especificação e ao escopo original.

## Limitações

Não substitui a equipe de desenvolvimento real — organiza o
planejamento e a documentação.

## Contrato de handoff

Ao final, o backlog e a arquitetura ficam prontos pra
implementação real, coordenada via `organizar-projeto`, com `anti-chat`
como quality gate antes de qualquer entrega visual.

## Exemplos de gatilhos positivos

- "Quero construir esse produto digital do zero"
- "Pacote completo de planejamento desse app novo"

## Exemplos de gatilhos negativos

- "Corrige esse bug no sistema que já existe" (é `depurar-erro`)
