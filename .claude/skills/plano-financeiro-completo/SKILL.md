---
name: plano-financeiro-completo
description: >
  Orquestra a análise financeira completa de um cliente/projeto: leitura
  de planilha, auditoria, fluxo de caixa, DRE, CMV, precificação, CAC/LTV,
  projeções e recomendações — encadeando as skills financeiras menores.
  Use quando o usuário pedir "faz a análise financeira completa", "quero
  entender a saúde financeira desse negócio do zero".
---

# plano-financeiro-completo — Orquestrador financeiro

## Quando usar

Primeira análise financeira profunda de um cliente/projeto, ou revisão
completa periódica.

## Quando não usar

Pedido de uma métrica isolada — chamar a skill específica direto.

## Entradas

Planilhas/dados financeiros do cliente/projeto.

## Dependências

`processar-arquivo`, `ler-planilha`, `auditar-planilha`,
`fluxo-de-caixa`, `dre`, `calcular-cmv`, `precificacao`, `cac-e-ltv`,
`projecao-financeira`, `relatorio-financeiro`.

## Contexto que deve ser carregado

Projeto/cliente ativo.

---

## Workflow

1. `processar-arquivo` — se a planilha ainda não passou pela central de
   arquivos.
2. `ler-planilha` — normalizar dados.
3. `auditar-planilha` — reportar erros/inconsistências (parar e
   perguntar antes de seguir se houver erro que distorça o resultado).
4. `fluxo-de-caixa` — situação de caixa e capital de giro.
5. `dre` — resultado por competência.
6. `calcular-cmv` — custo real, margem de contribuição, ponto de
   equilíbrio.
7. `precificacao` — validar se preços praticados são viáveis.
8. `cac-e-ltv` — se houver dado de aquisição de cliente.
9. `projecao-financeira` — cenários futuros com base no que foi
   encontrado.
10. `relatorio-financeiro` — consolidar tudo em entrega única.

Mostrar resumo curto ao final de cada etapa antes de seguir pra próxima.

## Saídas

Todos os arquivos de `03-financeiro/` preenchidos + relatório final em
`09-relatorios/`.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/03-financeiro/` e `09-relatorios/`.

## Regras

- Nunca pular a auditoria quando houver planilha com erro conhecido.
- Nunca apresentar projeção como certeza.
- Nunca alterar planilha original em nenhuma etapa.

## Critérios de qualidade

Relatório final consolida achados de todas as etapas aplicáveis, sem
contradição entre elas.

## Critérios de validação

Cada etapa aplicável foi executada ou descartada com motivo registrado.

## Limitações

Depende da qualidade do dado de entrada — se a planilha for
incompleta/inconsistente, isso limita a profundidade da análise.

## Contrato de handoff

`anti-chat` (quality gate contra faixa genérica de mercado sem contexto)
antes de entregar; encaminha pra `plano-estrategico` (decisões
priorizadas com base na saúde financeira encontrada).

## Exemplos de gatilhos positivos

- "Faz a análise financeira completa desse cliente"
- "Quero entender a saúde financeira desse negócio do zero"

## Exemplos de gatilhos negativos

- "Só quero saber meu CAC" (é `cac-e-ltv` isolado)
