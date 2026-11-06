---
name: qa
description: >
  Define e executa critério de qualidade antes de considerar uma entrega
  técnica pronta: testes funcionais, checklist de segurança básica, e
  plano mínimo de observabilidade (o que monitorar depois de no ar). Use
  quando o usuário pedir "isso está pronto pra produção", "faz o QA
  desse sistema", "checklist de segurança".
---

# qa — Qualidade, segurança básica e observabilidade

## Quando usar

Antes de considerar uma entrega técnica (site, app, integração) pronta
pra produção.

## Quando não usar

Revisão de código isolada sem contexto de entrega → `revisar-codigo`.

## Entradas

Sistema/página/integração a validar.

## Dependências

`pagina-e-site`, `app-e-sistema`, `integrar-api` (o que estiver sendo
validado).

## Contexto que deve ser carregado

Critério de aprovação definido no briefing/escopo original.

---

## Workflow

### Modo: Teste funcional

1. Fluxos principais funcionam de ponta a ponta.
2. Estados de erro/vazio tratados (não só o caminho feliz).
3. Responsivo nas larguras principais (se for interface).

### Modo: Segurança básica

1. Nenhum segredo/token exposto no código ou resposta de API.
2. Input de usuário validado (sem injeção óbvia).
3. Permissões/RLS conferidas (quem pode ver/editar o quê).
4. HTTPS em produção, nunca dado sensível em texto plano.

### Modo: Observabilidade mínima

1. O que precisa ser monitorado depois de no ar (erro, tempo de
   resposta, uso).
2. Onde os logs ficam acessíveis pra quem for investigar problema.
3. Alerta mínimo pra quando algo crítico falhar.

## Saídas

Checklist de QA com status (feito/pendente) por item.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/07-tecnologia/qa-<entrega>.md`.

## Regras

- Nenhuma entrega considerada "pronta" com item de segurança básica
  pendente sem aviso explícito ao responsável.
- Checklist sempre específico à entrega, não genérico copiado.

## Critérios de qualidade

Todo item do checklist tem status claro (feito, pendente, não
aplicável com motivo).

## Critérios de validação

Nenhum "pronto" declarado com item de segurança crítico pendente sem
essa pendência estar visível.

## Limitações

Não substitui teste automatizado real (unitário/integração) quando o
projeto já tiver suíte própria — complementa.

## Contrato de handoff

Encaminha pra `depurar-erro` (se achar problema) e `documentar-sistema`
(registro final).

## Exemplos de gatilhos positivos

- "Isso está pronto pra produção?"
- "Faz o checklist de segurança desse sistema"

## Exemplos de gatilhos negativos

- "Revisa esse código específico" (é `revisar-codigo`)
