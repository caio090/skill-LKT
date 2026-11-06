---
name: app-e-sistema
description: >
  Coordena escopo, usuários, fluxos, permissões, dados, integrações,
  interface, backlog, arquitetura, QA e documentação de um aplicativo ou
  sistema de um projeto de cliente ou interno. Não implementa produto
  real nesta fase — ensina a coordenar o processo para quando o projeto
  for construído. Use quando o usuário pedir "preciso de um app pra X",
  "vamos criar um sistema", "planeja esse produto digital".
---

# app-e-sistema — Orquestradora de aplicativo/sistema

Coordena o planejamento de um app/sistema de um projeto específico — não
constrói o LKT System como aplicativo (ele não é isso).

## Quando usar

- Início de planejamento de um app, sistema interno ou produto digital
  dentro de um projeto já existente.

## Quando não usar

- Ajuste pontual de um sistema já em produção — isso é `revisar-codigo`
  ou `depurar-erro` diretamente.
- Antes de ter um projeto/cliente associado — rodar `novo-projeto`
  primeiro.

## Entradas

- Objetivo do sistema, quem usa, problema que resolve.

## Dependências

- `referencia-site` (quando houver referência visual de interface a
  aproveitar — mesmo princípio de `pagina-e-site`, aplicado à UI do
  app).
- `<pasta-do-projeto-ativo>/01-diagnostico/`, `02-estrategia/`.
- Skills `arquitetura-de-software`, `planejar-banco-de-dados`,
  `design-front-end`, `qa` (quando existirem/forem chamadas).

## Contexto que deve ser carregado

Diagnóstico e estratégia do projeto ativo.

---

## Workflow

### Passo 1 — Escopo e usuários

Definir: quem usa o sistema (perfis de usuário), o que cada perfil
precisa fazer, o que fica fora de escopo nesta fase.

### Passo 2 — Fluxos principais

Mapear os 3-5 fluxos mais importantes (ex.: cadastro, ação principal,
consulta de resultado) em passos simples, sem ainda decidir tela.

### Passo 3 — Permissões

Definir o que cada perfil pode ver/fazer/editar — mesmo em sistema
simples, deixar isso explícito evita retrabalho depois.

### Passo 4 — Dados

Listar as entidades principais (o que o sistema precisa guardar) em
linguagem simples — a modelagem técnica detalhada é
`planejar-banco-de-dados`, aqui é só o levantamento.

### Passo 5 — Integrações

Listar o que precisa conversar com fora (WhatsApp, planilha, API de
terceiro, pagamento) — sem configurar nada agora, só mapear.

### Passo 6 — Interface

Encaminhar pra `design-front-end` com os fluxos do Passo 2 definidos.

### Passo 7 — Arquitetura

Encaminhar pra `arquitetura-de-software` com escopo, dados e integrações
já levantados.

### Passo 8 — Backlog

Transformar os fluxos em lista priorizada de itens de trabalho — o que é
essencial pro primeiro uso real (MVP) vs. o que pode esperar.

### Passo 9 — QA e documentação

Definir critério mínimo de pronto (o que precisa funcionar antes de
considerar entregue) e encaminhar pra `qa` e `documentar-sistema` quando
essas skills existirem/forem chamadas.

---

## Saídas

Documento de planejamento com escopo, usuários, fluxos, permissões,
dados, integrações e backlog priorizado.

## Regras

- Não implementar código nesta skill — ela planeja, não constrói.
- Não inventar requisito que o usuário não mencionou nem confirmou.
- Sempre separar "essencial pro primeiro uso" do resto — evita escopo
  inchado antes de validar a ideia.

## Critérios de qualidade

- Todo perfil de usuário tem permissões explícitas, não implícitas.
- Backlog prioriza o essencial antes do desejável.

## Critérios de validação

- Escopo, fluxos, permissões e dados documentados antes de qualquer
  arquitetura técnica ser definida.

## Limitações

- Não decide stack técnica sozinha — isso é `arquitetura-de-software`.
- Não substitui teste real com usuário — só organiza o planejamento.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/07-tecnologia/`.

## Contrato de handoff

`design-front-end` (Passo 6), `arquitetura-de-software` (Passo 7),
`planejar-banco-de-dados` (Passo 4/7), `qa`, `anti-chat` (quality gate
final) e `documentar-sistema` (Passo 9).

## Exemplos de gatilhos positivos

- "Preciso de um app pra gestão de pedidos do cliente X"
- "Vamos criar um sistema interno pra isso"

## Exemplos de gatilhos negativos

- "Corrige esse bug no sistema" (é `depurar-erro`)
- "Revisa esse código" (é `revisar-codigo`)
