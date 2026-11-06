---
name: rotear-tarefa
description: >
  Decide qual módulo e qual skill (ou cadeia de skills) atende um pedido,
  consultando docs/roteamento.md e docs/catalogo-skills.md, quando não é
  óbvio de cara qual skill usar ou quando mais de uma poderia se aplicar.
  Use quando o usuário fizer um pedido ambíguo ou amplo ("me ajuda com
  marketing dessa marca", "preciso organizar isso"), quando duas skills
  parecerem cobrir a mesma coisa, ou quando pedir explicitamente "qual
  skill eu uso pra X".
---

# rotear-tarefa — Roteamento de pedido para módulo/skill

Esta skill não executa a tarefa em si — ela decide **por onde começar**.
Para pedidos claros (ex.: "cria um carrossel sobre X"), não é necessário
invocar esta skill: vai direto na skill óbvia. Ela existe pros casos
ambíguos, amplos, ou que cruzam mais de um módulo.

## Quando usar

- O pedido é amplo demais pra mapear direto numa skill ("preciso de
  ajuda com o negócio", "organiza minha operação").
- O pedido parece precisar de mais de uma skill em sequência, e não está
  claro qual vem primeiro.
- Existe mais de uma skill candidata e não é óbvio qual encaixa melhor.
- O usuário pergunta diretamente qual skill/módulo usar.

## Quando não usar

- Pedido específico que já aponta claramente pra uma skill (ex.: "escreve
  um email pra..." → `email-profissional` direto, sem passar por aqui).
- Não usar como camada obrigatória em toda tarefa — isso deixaria o
  sistema lento e burocrático. É um recurso pontual pra ambiguidade real.

## Entradas

- O pedido do usuário, como veio.

## Dependências

- `docs/roteamento.md` — tabela de tipo de pedido → módulo → skill(s) →
  memória consultada.
- `docs/catalogo-skills.md` — lista de skills existentes com descrição.

## Contexto que deve ser carregado

Nenhuma memória de negócio é necessária pra decidir o roteamento em si —
só os dois documentos de roteamento/catálogo acima. A skill escolhida no
final é que vai carregar a memória relevante.

---

## Workflow

### Passo 1 — Entender o pedido

Identificar: qual é o objetivo real por trás do pedido, e se ele cruza
mais de um domínio (ex.: "quero vender mais" cruza estratégia,
marketing, comercial e possivelmente financeiro).

### Passo 2 — Consultar roteamento e catálogo

Ler `docs/roteamento.md` pra ver se o tipo de pedido já tem uma linha
mapeada. Ler `docs/catalogo-skills.md` pra conferir se a skill sugerida
ainda existe e está com o `status` atual (ativa, precisa adaptação, etc).

### Passo 3 — Decidir e explicar

Se o pedido mapeia limpo pra uma skill: dizer qual e seguir com ela.

Se o pedido cruza vários módulos: propor a ordem de encadeamento
(ex.: diagnóstico → estratégia → conteúdo), sem executar tudo de uma vez
sem alinhar com o usuário — perguntar se ele quer o pacote completo ou só
o primeiro passo.

Se nenhuma skill existente cobre bem o pedido: dizer isso explicitamente
e perguntar se vale criar uma skill nova (seguindo a regra de criação de
skills do `CLAUDE.md`) ou se é uma tarefa pontual que não precisa virar
skill.

### Passo 4 — Encaminhar

Passar a mão pra skill (ou sequência de skills) decidida, com o contexto
já entendido — não repetir perguntas que o usuário já respondeu aqui.

---

## Saídas

Pedido encaminhado pra skill (ou sequência de skills) certa, com a ordem de encadeamento explicada quando cruzar módulos.

## Critérios de qualidade

- A skill final sugerida é sempre uma que existe de fato.
- Pedidos que cruzam módulos recebem ordem explícita, não lista solta.

## Regras

- Nunca inventar uma skill que não existe em `.claude/skills/` — só
  encaminhar pra skills reais, ou propor criar uma nova explicitamente.
- Não forçar um pedido simples a passar por esta skill — isso é
  sobrecarga desnecessária.
- Se `docs/roteamento.md` estiver desatualizado em relação às skills
  reais, sinalizar isso (é um caso pra `validar-sistema` ou
  `salvar-local` corrigir o catálogo).

## Critérios de validação

- A skill final sugerida existe de fato em `.claude/skills/<nome>/SKILL.md`.
- Pedidos que cruzam módulos recebem uma ordem de encadeamento explícita,
  não uma lista solta de skills sem sequência.

## Limitações

- Não substitui o bom senso de ir direto na skill óbvia quando o pedido
  já é claro — existe só pra reduzir ambiguidade real.

## Caminho de salvamento

Não gera arquivo — é uma decisão de fluxo, tomada em conversa.

## Contrato de handoff

Entrega o pedido já roteado pra skill (ou primeira skill da cadeia)
decidida no Passo 3, com o contexto do Passo 1 já entendido.

## Exemplos de gatilhos positivos

- "Qual skill eu uso pra X"
- "Me ajuda a vender mais" (pedido amplo, cruza módulos)

## Exemplos de gatilhos negativos

- "Escreve um email pra fulano" (pedido óbvio — vai direto em
  `email-profissional`, sem passar por aqui)
