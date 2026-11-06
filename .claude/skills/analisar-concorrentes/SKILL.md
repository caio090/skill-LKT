---
name: analisar-concorrentes
description: >
  Mapeia concorrentes reais de um cliente/projeto (via WebSearch/WebFetch):
  quem são, o que oferecem, pontos fortes/fracos, gaps e oportunidades.
  Use quando o usuário pedir "analisa meus concorrentes", "quem mais
  atende esse público", "onde eu posso me diferenciar".
---

# analisar-concorrentes — Mapeamento de concorrência

## Quando usar

Diagnóstico ou posicionamento que precisa saber quem mais disputa o
mesmo público do cliente.

## Quando não usar

Análise de SEO/ranking de busca especificamente → `seo` (Passo 2 já
cobre isso nesse contexto).

## Entradas

Nicho, região, produto/serviço do cliente.

## Dependências

WebSearch, WebFetch. `_fontes/` para registro.

## Contexto que deve ser carregado

Diagnóstico e oferta do projeto ativo.

---

## Workflow

1. Identificar 3-8 concorrentes reais (buscar, não supor).
2. Pra cada um: o que oferecem, preço (se público), diferencial
   declarado, pontos fracos observáveis (reviews, reclamações públicas).
3. Mapear gaps: o que nenhum concorrente faz bem, onde há espaço.
4. Registrar fonte de cada observação.
5. Salvar em `<pasta-do-projeto-ativo>/01-diagnostico/concorrencia.md`.

## Saídas

`01-diagnostico/concorrencia.md` — tabela de concorrentes + gaps/
oportunidades.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/01-diagnostico/`.

## Regras

- Concorrente tem que ser real e verificável, não hipotético.
- Nunca inventar preço ou dado que não está público — se não achar,
  marcar como "não disponível".

## Critérios de qualidade

Cada concorrente citado é rastreável (site, perfil, fonte real).

## Critérios de validação

Gaps/oportunidades derivam de observação real, não de suposição.

## Limitações

Só cobre o que é público — não acessa dados internos do concorrente.

## Contrato de handoff

Encaminha pra `posicionamento` e `plano-estrategico`.

## Exemplos de gatilhos positivos

- "Quem são meus concorrentes reais nessa região"
- "Onde dá pra me diferenciar desses concorrentes"

## Exemplos de gatilhos negativos

- "Qual palavra-chave meu concorrente rankeia" (é `seo`)
