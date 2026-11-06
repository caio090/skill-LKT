---
name: gerar-proposta-a-partir-do-nivel
description: >
  Traduz a inteligência interna dos níveis (escopo, plano de avanço,
  recomendação) para a camada comercial — só o que o cliente precisa
  entender para decidir. Nunca expõe raciocínio interno, notas
  internas, custo interno, margem, caso confidencial de outro cliente
  ou regra técnica desnecessária. Use quando o usuário disser "traduz
  isso pra proposta", "gera a proposta a partir desse nível", ou depois
  de gerar-escopo-por-nivel.
---

# gerar-proposta-a-partir-do-nivel — Só a camada comercial

Produz a versão comercial do escopo por nível — contexto, solução,
entregas, prazo, investimento, condições, próximos passos. Ver
`knowledge/niveis/NIVEIS_E_PROPOSTAS.md` e
`docs/NIVEIS_NA_PROPOSTA_COMERCIAL.md`.

## Quando usar

- Depois de `gerar-escopo-por-nivel`, quando o próximo passo é
  apresentar ao cliente.

## Quando não usar

- Para uso interno da equipe (isso é `gerar-escopo-por-nivel`).
- Quando não há classificação/recomendação de nível envolvida — nesse
  caso, usar `proposta-e-precificacao` diretamente.

## Entradas

- `deliverable-profile` (escopo por camada).
- `level-recommendation` (prazo/custo projetado).
- Fase comercial desejada (estrutura inicial, implantação, evolução,
  escala futura).

## Dependências

- `templates/proposta/PROPOSTA_POR_NIVEL.txt`,
  `templates/proposta/PROPOSTA_POR_NIVEL.json`
- `.claude/skills/gerar-escopo-por-nivel` (entrada)
- `.claude/skills/proposta-e-precificacao` (fecha preço final)

## Contexto que deve ser carregado

- `deliverable-profile` e `level-recommendation` de origem.
- `_memoria/sistema/preferencias.md` (tom de voz comercial).

---

## Workflow

### Passo 1 — Selecionar o que entra na proposta

Da camada "obrigatório" + "recomendado" do escopo (via
`gerar-escopo-por-nivel`) — "opcional" e "futuro" aparecem como
possibilidade, não como compromisso; "não incluso" aparece
explicitamente como fora do escopo.

### Passo 2 — Traduzir termos técnicos

Reescrever qualquer termo técnico/interno em linguagem que o cliente
entenda. O nome do nível interno (ex.: "maturidade digital:
estruturada") só aparece se ajudar — senão, usar a fase comercial
(estrutura inicial / implantação / evolução / escala futura).

### Passo 3 — Remover o que nunca vai para o cliente

Tarefa interna detalhada, risco interno, margem, custo por
colaborador, nota confidencial, pontuação técnica completa, caso de
outro cliente, raciocínio privado. Ver checklist completo em
`docs/NIVEIS_NA_PROPOSTA_COMERCIAL.md`.

### Passo 4 — Montar a proposta

Contexto, solução, entregas selecionadas, prazo, investimento (faixa
vira número fechado só depois de passar por
`proposta-e-precificacao`), condições, próximos passos. Usar
`templates/proposta/PROPOSTA_POR_NIVEL.txt`.

### Passo 5 — Encaminhar para fechamento de preço

Se o preço ainda não foi fechado, encaminhar para
`proposta-e-precificacao` antes de considerar a proposta pronta para
envio.

---

## Saídas

Documento comercial (formato conforme `docs/PADRAO_DE_ARQUIVOS.md`),
sem nenhum dado interno vazado, pronto para revisão final em
`proposta-e-precificacao`.

## Regras

- Nunca expor raciocínio interno completo, nota interna, custo
  interno, margem, caso confidencial de outro cliente, ou dado que não
  ajuda a decisão do cliente.
- Nunca citar o nível interno quando isso não ajudar o cliente a
  entender.

## Critérios de qualidade

- Toda entrega da proposta é rastreável ao escopo "obrigatório" ou
  "recomendado" do perfil de entrega.

## Critérios de validação

- Nenhum campo de `deliverable-profile` marcado como interno (custo,
  margem, tarefa técnica) aparece no texto final.

## Limitações

- Não fecha o preço final sozinha — sempre passa por
  `proposta-e-precificacao`.

## Caminho de salvamento

`workspaces/<tipo>/<slug>/projetos/<projeto>/04-comercial/PROPOSTA-POR-NIVEL.md`

## Contrato de handoff

Recebe de `gerar-escopo-por-nivel`. Encaminha para
`proposta-e-precificacao` (composição final de preço) e, quando pronta,
para `notebook-lm` (consolidação no dossiê).

## Exemplos de gatilhos positivos

- "Traduz isso pra proposta"
- "Gera a proposta a partir desse nível"

## Exemplos de gatilhos negativos

- "Monta o escopo interno completo" (é `gerar-escopo-por-nivel`,
  entrada desta skill)

Arquivos de apoio: `perguntas.txt`, `fluxo.md`, `saidas.md`,
`validacao.md`, `exemplos.md`.
