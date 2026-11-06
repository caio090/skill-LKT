---
name: gestao-de-negocio
description: >
  Consolida vendas, custos, despesas, caixa, produtos, clientes,
  campanhas, estoque e decisões de um negócio (com especialização em
  food service, adaptável a outros segmentos) e indica a próxima ação
  concreta: problema principal, evidência, causa provável, informação
  faltante, ação imediata, de 30 e de 90 dias, responsável, custo, prazo,
  indicador, risco e prioridade. Use quando o usuário pedir "analisa meu
  negócio", "o que está acontecendo com a empresa", "qual é o próximo
  passo", "onde estou perdendo dinheiro", "como melhorar o resultado",
  "monta um plano para a empresa".
---

# gestao-de-negocio — Consolidação e próxima ação

Skill principal do módulo `gestao-de-negocio` (`catalogo/modulos/gestao-de-negocio/`,
especialização `food-service/`). Entende primeiro o negócio, depois
calcula — nunca começa pela conta.

## Quando usar

Visão geral e decisão de prioridade — quando o dono não sabe por onde
começar ou quer entender a saúde geral do negócio.

## Quando não usar

Pergunta específica já direcionada (CMV, cardápio, ticket) → chamar a
skill específica direto; esta é pra consolidar, não pra métrica isolada.

## Entradas

Tudo que já existir: `dna-do-negocio`, `03-financeiro/` (DRE, fluxo de
caixa, CMV), `04-marketing/` (engenharia de cardápio, ticket, promoções),
estoque, decisões anteriores.

## Dependências

`dna-do-negocio`, `dre`, `fluxo-de-caixa`, `cmv-real-e-teorico` (ou
`calcular-cmv`), `engenharia-de-cardapio`, `aumento-de-ticket`,
`estoque-food-service`, `analisar-promocao-cupom`, `plano-estrategico`.

## Contexto que deve ser carregado

Todo o histórico financeiro e de produto do cliente/projeto ativo.

---

## Workflow

### Passo 1 — Entender antes de calcular

Antes de qualquer número, confirmar: segmento, cidade/região, público,
posicionamento, canais, operação, capacidade produtiva, horários,
equipe, fornecedores, embalagens, taxas, histórico de desperdício,
promoções ativas, histórico de venda, objetivo financeiro, limitações
reais. Reaproveitar `dna-do-negocio` se já existir, só perguntar o que
faltar.

### Passo 2 — Consolidar o que já existe

Reunir (sem recalcular o que outra skill já calculou): resultado
financeiro (`dre`), caixa (`fluxo-de-caixa`), CMV real/teórico, situação
de estoque, desempenho de cardápio/produto, ticket médio, promoções
ativas, decisões anteriores registradas.

### Passo 3 — Comparar evolução do próprio negócio

Nunca usar faixa universal de "CMV bom/ruim" ou média de mercado sem
fonte, segmento, região e data. Priorizar:
- período atual vs. anterior;
- produto vs. produto;
- previsto vs. realizado;
- CMV teórico vs. CMV real;
- margem antes vs. depois;
- ticket antes vs. depois.

### Passo 4 — Identificar gargalo real

O problema principal precisa de evidência concreta, não impressão vaga.

### Passo 5 — Próxima ação

Fechar sempre com:

```
Problema principal: <descrição concreta>
Evidência: <o que comprova>
Causa provável: <hipótese, marcada como hipótese se não confirmada>
Informação faltante: <o que ajudaria a confirmar>
Ação imediata: <o que fazer agora>
Ação de 30 dias: <...>
Ação de 90 dias: <...>
Responsável: <quem>
Custo: <estimativa ou "a definir">
Prazo: <data>
Indicador: <métrica de sucesso>
Risco: <o que pode dar errado>
Prioridade: <alta/média/baixa>
```

Escrever isso em linguagem que o dono entende, não jargão de contador/
analista.

### Passo 6 — Registrar

Salvar em `<pasta-do-projeto-ativo>/09-relatorios/gestao-negocio-<data>.md`
e atualizar `_memoria/pendencias.md`/`PROJETO.md` com a ação priorizada.

## Saídas

Diagnóstico consolidado + próxima ação nos 12 campos do Passo 5.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/09-relatorios/`.

## Regras

- Nunca calcular antes de entender o contexto do Passo 1.
- Nunca usar benchmark de mercado sem fonte, segmento, região e data.
- Sempre comparar a evolução do próprio negócio antes de qualquer
  comparação externa.
- Toda ação recomendada tem os 12 campos do Passo 5 — nunca uma
  recomendação solta.

## Critérios de qualidade

A resposta final é compreensível para o dono do negócio, sem jargão não
explicado.

## Critérios de validação

Problema principal apontado tem evidência concreta citada, não
suposição.

## Limitações

Depende da qualidade e completude dos dados consolidados de cada skill
individual — se algo estiver incompleto, isso deve aparecer em
"informação faltante", não ser ignorado.

## Contrato de handoff

Encaminha pra `plano-estrategico` (formalizar em plano completo) e pras
skills específicas do gargalo identificado (`cmv-real-e-teorico`,
`engenharia-de-cardapio`, `aumento-de-ticket`, etc.).

## Exemplos de gatilhos positivos

- "Analisa meu negócio e me diz o que fazer"
- "Onde estou perdendo dinheiro"
- "Qual é o próximo passo da empresa"

## Exemplos de gatilhos negativos

- "Calcula só meu CMV desse mês" (é a skill específica, direto)
