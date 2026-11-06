---
name: diagnostico-empresarial
description: >
  Analisa os pilares aplicáveis de um workspace ou projeto (negócio,
  oferta, público, marca, marketing, presença digital, conteúdo,
  comercial, atendimento, financeiro, operação, logística, equipe por
  papéis, tecnologia, dados, riscos), usando só os pilares pertinentes
  ao caso. Também identifica como contatos chegam, avançam e se perdem,
  para escolher entre processo, fluxo de trabalho, funil, pipeline ou
  campanha antes de recomendar qualquer ferramenta. Pode atribuir nota
  de 0 a 5 por pilar, sempre explicando critério e evidência. Use
  depois que um workspace/projeto foi criado por `novo-projeto`, antes
  de qualquer produção.
---

# diagnostico-empresarial — Diagnóstico por pilares, sem receita fixa

Analisa o estado atual de um workspace ou projeto pilar por pilar,
usando só os pilares pertinentes, e produz um diagnóstico que serve de
base para planejamento, proposta e execução. Nunca aplica a mesma
receita para negócios diferentes — cada pilar só entra se fizer sentido
para o caso.

## Quando usar

- Depois que `novo-projeto` cria a estrutura de um workspace ou projeto,
  antes de qualquer produção de conteúdo ou entrega.
- Quando o usuário pede "diagnóstico", "avaliação", "onde estamos",
  "por que as vendas caíram", "o que está faltando".
- Antes de montar uma proposta (`proposta-e-precificacao` depende do
  diagnóstico para justificar escopo e preço).

## Quando não usar

- Para ajustar um ponto pontual já conhecido (ex.: "revisa esse texto")
  — isso não precisa de diagnóstico completo.
- Repetidamente na mesma sessão sem novo dado — diagnóstico é um
  retrato, não é recalculado a cada pergunta.

## Entradas

- Workspace/projeto ativo (`.lkt-system/estado/contexto-ativo.json`).
- Memória do workspace (`_memoria.json`, `WORKSPACE.txt`).
- Material disponível em `00-contexto/entrada/` e
  `00-contexto/fontes/`.
- Pilares que o usuário já sabe que quer avaliar (opcional — se não
  informar, avaliar os pertinentes ao tipo de projeto).

## Dependências

- `catalogo/modulos/diagnostico`
- `templates/diagnostico/`
- `schemas/diagnostico.schema.json`
- `knowledge/projetos/ONTOLOGIA_PROCESSOS_FUNIS_PIPELINES.md`
- `knowledge/niveis/`, `catalogo/niveis/` (quando a dimensão tiver
  conjunto de níveis formal)
- `docs/GLOSSARIO-GESTAO-DE-NEGOCIO.md`

## Contexto que deve ser carregado

- `_memoria/sistema/empresa.md`, `estrategia.md`
- `_memoria.json` do workspace
- `PROJETO.md` do projeto, se houver um ativo

---

## Workflow

### Passo 1 — Selecionar os pilares pertinentes

Pilares possíveis: negócio, oferta, público, marca, marketing, presença
digital, conteúdo, comercial, atendimento, financeiro, operação,
logística, equipe por papéis, tecnologia, dados, riscos.

Selecionar conforme o tipo de projeto/workspace e o que o usuário
descreveu — nunca avaliar os 16 por padrão. Perguntar se não estiver
claro: "Pra esse diagnóstico, faz sentido olhar [lista sugerida] — tem
algum desses que não se aplica, ou algum que falta?"

### Passo 2 — Avaliar cada pilar selecionado

Para cada pilar: o que existe hoje, o que falta, evidência (de onde vem
essa informação), e opcionalmente uma nota de 0 a 5 — só atribuir nota
se conseguir explicar o critério usado. Nunca inventar informação sem
fonte; o que não foi respondido vira pendência, não vira suposição.

Quando existir um conjunto de níveis formal para a dimensão do pilar em
`catalogo/niveis/` (ver `knowledge/niveis/COMO_FUNCIONAM_OS_NIVEIS.md`),
encaminhar para `.claude/skills/classificar-nivel` em vez de (ou além
de) uma nota solta 0-5 — o resultado é mais explicável. Nunca apresentar
só o código do nível:

> "Marketing está no nível Base porque a empresa já possui canais
> ativos, mas ainda não possui calendário, métricas consolidadas nem
> processo de aprovação. A recomendação é avançar para Estrutura
> Organizada antes de implantar automações." (nunca "Marketing: nível
> 2.")

### Passo 3 — Mapear como contatos/pessoas avançam (quando pertinente)

Perguntar (só quando o pilar comercial, marketing ou atendimento
estiver em avaliação):

- Como os contatos chegam?
- Como são atendidos?
- Como avançam de uma etapa pra outra?
- Onde são registrados hoje?
- Quais etapas existem?
- Onde há perda?
- Quem responde por cada etapa?
- Qual a próxima ação em cada caso parado?
- Quais métricas já existem?
- Quais automações já existem, e quais são seguras de manter?
- Qual a maturidade comercial real (volume, recorrência, equipe,
  complexidade, histórico de perda, capacidade de operação)?

A partir disso, classificar o que existe usando
`knowledge/projetos/ONTOLOGIA_PROCESSOS_FUNIS_PIPELINES.md`: é um
processo, um fluxo de trabalho, um funil, um pipeline, uma campanha ou
uma jornada? **Não recomendar CRM só porque não existe CRM** — primeiro
avaliar volume, recorrência, equipe, complexidade, perda, histórico e
capacidade real de operação (ver `docs/MODULOS.md`).

### Passo 4 — Consolidar

Gerar o diagnóstico com: pilares avaliados, pilares fora de escopo (e
por quê), o que existe, o que falta, prioridade agora vs. depois,
modelo de processo/funil/pipeline identificado (se aplicável), e
próximo passo recomendado.

### Passo 5 — Salvar

Salvar em `.../01-diagnostico/` do workspace/projeto ativo, em Markdown
(documentação técnica) com um resumo em TXT quando o destinatário for
leigo. Atualizar `PROJETO.md` (`## Estado` → `em diagnóstico` ou
`em execução`, conforme o resultado) e `_memoria.json` do workspace.

---

## Saídas

Diagnóstico salvo em `.../01-diagnostico/DIAGNOSTICO.md` (+ resumo TXT
opcional), com pilares avaliados, evidências, notas (se aplicável),
modelo de processo/funil/pipeline identificado, e prioridades.

## Regras

- Nunca avaliar todos os 16 pilares por padrão.
- Nunca atribuir nota sem explicar o critério e a evidência.
- Nunca inventar dado ausente — registrar como pendência.
- Nunca recomendar CRM automaticamente por ausência de CRM.
- Nunca chamar um fluxo de trabalho interno de "funil".

## Critérios de qualidade

- Todo pilar avaliado tem pelo menos: o que existe, o que falta,
  evidência.
- Toda recomendação indica prioridade (agora/depois) e por quê.

## Critérios de validação

- Diagnóstico salvo no caminho certo do workspace/projeto ativo.
- `PROJETO.md` e `_memoria.json` atualizados com o resultado.

## Limitações

- Não cria proposta nem preço — isso é `proposta-e-precificacao`.
- Não executa nenhuma automação — só recomenda.

## Caminho de salvamento

`workspaces/<tipo>/<slug>/[projetos/<projeto>/]01-diagnostico/DIAGNOSTICO.md`

## Contrato de handoff

Encaminha para `proposta-e-precificacao` (quando o próximo passo for
comercial) ou direto para o módulo correspondente em
`catalogo/modulos/` (quando o diagnóstico já apontar a entrega certa).
Se identificar necessidade de funil/pipeline/campanha, encaminha para
`desenhar-funil`, `configurar-pipeline` ou `criar-campanha`. Se algum
pilar tiver conjunto de níveis formal, encaminha para
`classificar-nivel`.

## Exemplos de gatilhos positivos

- "Faz um diagnóstico"
- "Onde a gente está hoje?"
- "Por que as vendas caíram esse mês?"

## Exemplos de gatilhos negativos

- "Ajusta esse texto aqui" (edição pontual, não diagnóstico)
