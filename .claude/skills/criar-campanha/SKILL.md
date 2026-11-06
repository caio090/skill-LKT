---
name: criar-campanha
description: >
  Gera uma campanha completa — briefing, objetivo, público, oferta,
  canais, cronograma, ativos, página, conteúdos, orçamento, funil
  associado, eventos de conversão, metas, plano de medição, riscos,
  aprovação e relatório. Use quando o usuário disser "cria uma
  campanha pra X", "quero lançar Y", "preciso organizar essa ação de
  marketing/evento".
---

# criar-campanha — Ação coordenada com objetivo, prazo e orçamento

Estrutura uma campanha como conjunto coordenado de ativos, canais e
métricas — distinta de processo (sem prazo definido) e de pipeline de
campanhas (que acompanha várias campanhas em andamento, não o conteúdo
de uma). Ver `knowledge/projetos/ONTOLOGIA_PROCESSOS_FUNIS_PIPELINES.md`.

## Quando usar

- Ação com objetivo específico, prazo definido, canais e orçamento
  (lançamento, evento, promoção, campanha de tráfego).

## Quando não usar

- Para operação contínua sem prazo (isso é processo/módulo).

## Entradas

- Objetivo, público, oferta.
- Canais, período, orçamento.
- Ativos e conteúdos previstos.
- Página associada (se houver — ver `estruturar-pagina-de-oferta`).
- Funil associado (se houver — ver `desenhar-funil`).

## Dependências

- `schemas/campanha.schema.json`, `schemas/funil.schema.json`,
  `schemas/evento-conversao.schema.json`
- `templates/campanha/CAMPANHA.txt`
- `.claude/skills/desenhar-funil`, `.claude/skills/estruturar-pagina-de-oferta`,
  `.claude/skills/projecoes`

## Contexto que deve ser carregado

- `_memoria/sistema/marca.md` (identidade visual/tom).
- Campanhas anteriores do workspace (para não repetir aprendizado já
  registrado).

---

## Workflow

### Passo 1 — Briefing (ver `perguntas.txt`)

Objetivo, público, oferta, canais, período, orçamento, ativos,
conteúdos, página, CTA.

### Passo 2 — Estruturar (ver `fluxo.md`)

Cronograma, funil associado (uma campanha pode gerar vários funis — ver
ontologia), eventos de conversão, plano de medição, responsáveis por
papel, dependências, riscos.

### Passo 3 — Projeções (opcional, quando fizer sentido)

Encaminhar para `.claude/skills/projecoes` (tipo marketing) para
investimento, alcance, leads, custo por lead esperado.

### Passo 4 — Aprovação e geração de saída (ver `saidas.md`)

Documento de campanha + checklist de aprovação antes de considerar
ativa.

### Passo 5 — Validar (ver `validacao.md`)

Regra de atribuição declarada (evita dupla contagem — ver
`schemas/evento-conversao.schema.json`).

---

## Saídas

Campanha estruturada (`schemas/campanha.schema.json`), com funil
associado quando houver, plano de medição e checklist de aprovação.

## Regras

- Nunca ativar campanha sem objetivo, público, período e orçamento
  definidos (mesmo que "a definir" temporariamente, registrado como
  pendência).
- Sempre declarar regra de atribuição quando houver mais de uma origem
  possível.

## Critérios de qualidade

- Toda campanha tem objetivo, público, período, orçamento, funil ou
  evento de conversão associado, e plano de medição.

## Critérios de validação

- Documento válido contra `schemas/campanha.schema.json`.

## Limitações

- Não publica nem dispara a campanha — isso exige confirmação explícita
  (nível 3 de autonomia, ver `docs/SEGURANCA_E_PERMISSOES.md`).

## Caminho de salvamento

`workspaces/<tipo>/<slug>/[projetos/<projeto>/]04-comercial/CAMPANHA.md`

## Contrato de handoff

Recebe de `novo-projeto` (quando o tipo de projeto for campanha).
Encaminha para `desenhar-funil`, `estruturar-pagina-de-oferta` e
`analisar-conversao` (medição pós-lançamento).

## Exemplos de gatilhos positivos

- "Cria uma campanha pra esse lançamento"
- "Preciso organizar essa ação de marketing"

## Exemplos de gatilhos negativos

- "Publica esse post" (execução pontual, não criação de campanha)

Arquivos de apoio desta skill: `perguntas.txt`, `fluxo.md`, `saidas.md`,
`validacao.md`, `exemplos.md`.
