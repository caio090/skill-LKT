---
name: projecoes
description: >
  Gera cenários financeiros, comerciais, de marketing, operacionais,
  logísticos ou de projeto, sempre declarando dados usados, hipóteses,
  limitações e nível de confiança — nunca apresenta projeção como
  garantia. Produz cenário conservador, base e agressivo quando fizer
  sentido. Use quando o usuário disser "projeta isso", "quanto eu vou
  faturar", "quanto tempo vai levar", "e se eu aumentar o investimento".
---

# projecoes — Cenários com hipótese explícita, nunca garantia

Gera projeções para os seis tipos definidos em `docs/PROJECOES.md`
(financeira, comercial, marketing, operacional, logística, projeto),
sempre separando fato de hipótese.

## Quando usar

- Quando o usuário pede uma estimativa de futuro (faturamento, prazo,
  capacidade, retorno de investimento, ponto de equilíbrio).
- Ao planejar um projeto novo (`novo-projeto` pode encaminhar aqui
  quando o tipo de projeto tiver componente financeiro/comercial).

## Quando não usar

- Para reportar um número que já é fato (ex.: faturamento já realizado)
  — isso é relatório, não projeção.

## Entradas

- Tipo de projeção (financeira, comercial, marketing, operacional,
  logística, projeto).
- Dados históricos disponíveis (de onde vêm, período).
- Hipóteses que o usuário quer testar (ex.: "e se eu dobrar o
  investimento em tráfego").
- Faixa de prazo/custo de um nível recomendado (`recomendar-nivel`),
  quando a projeção vier de um plano de avanço — sempre tratada como
  ponto de partida, nunca como preço fechado.
- Meta ou pergunta que a projeção precisa responder.

## Dependências

- `schemas/projecao.schema.json`
- `templates/projecao/`
- `docs/PROJECOES.md`
- `.claude/skills/analisar-conversao` (quando a projeção depender de
  taxa de conversão de funil)
- `.claude/skills/recomendar-nivel` (quando a projeção partir de faixa
  de prazo/custo de um nível — ver `knowledge/niveis/NIVEIS_E_PROJECOES.md`)

## Contexto que deve ser carregado

- `_memoria.json` do workspace (histórico financeiro/comercial já
  registrado).
- `PROJETO.md` do projeto ativo, se houver.

---

## Workflow

### Passo 1 — Declarar a base

Registrar: dados utilizados, origem dos dados, período coberto. Se não
houver dado histórico suficiente, avisar explicitamente e reduzir o
nível de confiança, nunca inventar número.

### Passo 2 — Declarar hipóteses e variáveis

Listar toda hipótese assumida (ex.: "taxa de conversão mantém a média
dos últimos 3 meses") e toda variável que pode mudar o resultado.

### Passo 3 — Calcular os cenários

Gerar cenário conservador, cenário base e cenário agressivo, quando
fizer sentido para o tipo de projeção. Mostrar o cálculo, não só o
resultado.

### Passo 4 — Declarar limitações, riscos e gatilho de revisão

O que pode invalidar a projeção, e em que condição ela deve ser
refeita (ex.: "revisar se o CAC subir mais de 20%").

### Passo 5 — Separar fato de recomendação

Sempre no documento final: fato (o que já aconteceu) → hipótese (o que
está sendo assumido) → cálculo (como se chegou no número) →
recomendação (o que fazer com isso) → decisão (o que foi decidido, se
já houver).

### Passo 6 — Salvar

Salvar em `.../06-financeiro-e-projecoes/`, com data da última
atualização visível no documento.

---

## Saídas

Projeção salva com dados, hipóteses, limitações, nível de confiança,
cenários (quando aplicável), riscos e gatilho de revisão.

## Regras

- Nunca apresentar projeção como garantia.
- Nunca omitir a origem dos dados usados.
- Sempre separar fato, hipótese, cálculo, recomendação e decisão.

## Critérios de qualidade

- Todo número projetado tem hipótese e origem de dado declaradas.
- Nível de confiança é justificado (quantidade e qualidade do dado
  histórico disponível).

## Critérios de validação

- Documento contra `schemas/projecao.schema.json`: todos os campos
  obrigatórios presentes.

## Limitações

- Não decide a ação a partir da projeção — recomenda, mas a decisão é
  do usuário (ou de quem tem o papel de responsável estratégico).
- Não substitui uma projeção financeira contábil formal quando o caso
  exigir parecer profissional (ex.: para fins fiscais/societários).

## Caminho de salvamento

`workspaces/<tipo>/<slug>/projetos/<projeto>/06-financeiro-e-projecoes/`

## Contrato de handoff

Pode receber de `diagnostico-empresarial`, `analisar-conversao` ou
`criar-campanha` (quando a campanha precisar de meta projetada).
Encaminha para `proposta-e-precificacao` quando a projeção embasar
preço.

## Exemplos de gatilhos positivos

- "Quanto eu vou faturar se..."
- "Projeta os próximos 3 meses"
- "Qual o ponto de equilíbrio desse produto?"

## Exemplos de gatilhos negativos

- "Quanto faturei mês passado?" (fato já realizado, é relatório)
