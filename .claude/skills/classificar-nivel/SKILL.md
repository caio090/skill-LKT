---
name: classificar-nivel
description: >
  Classifica um workspace/projeto numa dimensão de maturidade (ex.:
  maturidade digital, financeira, comercial) com base em evidência real
  — nunca por impressão vaga. Mostra o nível atual, a confiança, a
  justificativa em linguagem simples e as lacunas de informação. Marca
  como provisório quando faltar evidência, nunca inventa. Use quando o
  usuário disser "em que nível estamos em X", "classifica a maturidade
  digital dessa empresa", ou comando `/classificar-nivel`.
---

# classificar-nivel — Classificação explicável, nunca por impressão

Classifica um workspace/projeto numa dimensão usando as regras de
`catalogo/niveis/` e `schemas/classification-rule.schema.json`. Ver
`knowledge/niveis/REGRAS_DE_CLASSIFICACAO.md`.

## Quando usar

- Depois (ou durante) um diagnóstico, quando uma dimensão de maturidade
  precisar de classificação formal para orientar prioridade, plano de
  avanço ou proposta.

## Quando não usar

- Para tarefa simples e pontual, sem relação com maturidade/estrutura
  (ex.: corrigir um arquivo) — classificar nível aqui não agrega valor.
- Quando já existe uma avaliação recente e nada mudou — usar
  `continuar-projeto`/`revisar-nivel` em vez de reclassificar do zero.

## Entradas

- Workspace/projeto e dimensão a classificar (perguntar se ambíguo —
  ver `perguntas.txt`).
- Evidências disponíveis (diagnóstico, dado financeiro, ferramenta
  ativa, documento, etc.).

## Dependências

- `catalogo/niveis/` (conjuntos de níveis configurados)
- `schemas/classification-rule.schema.json`,
  `schemas/level-assessment.schema.json`
- `knowledge/niveis/REGRAS_DE_CLASSIFICACAO.md`
- `.claude/skills/diagnostico-empresarial` (fonte comum de evidência)

## Contexto que deve ser carregado

- Diagnóstico existente do workspace/projeto, se houver.
- Avaliações anteriores da mesma dimensão (`_memoria.json` ou
  histórico de `level-assessment`) — nunca reclassificar ignorando o
  que já foi registrado.

---

## Workflow

### Passo 1 — Identificar dimensão (ver `perguntas.txt`)

Se o usuário não especificar, sugerir com base no tipo de
projeto/diagnóstico (ver `knowledge/niveis/NIVEIS_E_DIMENSOES.md`) e
confirmar antes de seguir.

### Passo 2 — Coletar evidências

Reunir o que já existe (diagnóstico, arquivo, ferramenta ativa, dado
financeiro, resposta do usuário). Nunca inventar evidência ausente.

### Passo 3 — Aplicar regras

Comparar evidências com os critérios de cada `level-definition` do
conjunto (`catalogo/niveis/<dimensao>.json`), do nível mais baixo para
o mais alto, parando no último nível cujos critérios foram
confirmados.

### Passo 4 — Determinar confiança

`confirmado` / `provável` / `parcial` / `incerto` / `sem dados` — ver
critério em `REGRAS_DE_CLASSIFICACAO.md`. Se `incerto` ou `sem dados`,
marcar o nível como **provisório** e listar o que falta.

### Passo 5 — Explicar em linguagem simples

Nunca mostrar só o código do nível. Sempre no formato:

> "[Dimensão] está no nível [nome] porque [evidência confirmada], mas
> ainda não [o que falta para o próximo nível]. A recomendação é
> [avançar para X / manter, se for o caso]."

### Passo 6 — Salvar e oferecer validação humana

Salvar `level-assessment` (schema correspondente). Perguntar: "Essa
classificação faz sentido pra você, ou quer ajustar/registrar como
exceção?" — registrar a resposta em `revisao_humana`.

---

## Saídas

`level-assessment` salvo, com nível atual, confiança, justificativa em
linguagem simples, evidências, lacunas e (se houver) revisão humana.

## Regras

- Nunca classificar por impressão vaga — sempre evidência declarada.
- Nunca inventar evidência ausente — marcar provisório.
- Nunca reclassificar ignorando avaliação anterior sem explicar a
  mudança.
- Sempre oferecer a opção de exceção quando a regra padrão não
  representar bem o caso.

## Critérios de qualidade

- Toda classificação tem justificativa em linguagem simples, não só
  código do nível.
- Toda classificação provisória lista o que falta para confirmar.

## Critérios de validação

- `level-assessment` válido contra
  `schemas/level-assessment.schema.json`.

## Limitações

- Não decide sozinha quando há conflito de evidência — sinaliza e
  pede revisão humana.
- Não cria conjunto de níveis novo — usa o que já está em
  `catalogo/niveis/` (criar conjunto novo é uma decisão de quem
  administra o catálogo, não desta skill).

## Caminho de salvamento

`workspaces/<tipo>/<slug>/[projetos/<projeto>/]01-diagnostico/NIVEL-<dimensao>.json`

## Contrato de handoff

Encaminha para `recomendar-nivel` (nível recomendado + lacuna) e,
quando houver revisão humana divergente, para `revisar-nivel`.

## Exemplos de gatilhos positivos

- "Em que nível estamos em marketing digital?"
- "Classifica a maturidade financeira dessa empresa"
- "/classificar-nivel"

## Exemplos de gatilhos negativos

- "Corrige esse arquivo" (tarefa pontual, sem relação com nível)

Arquivos de apoio: `perguntas.txt`, `fluxo.md`, `saidas.md`,
`validacao.md`, `exemplos.md`.
