---
name: escada-de-valor-e-funil
description: >
  Organiza as ofertas de um cliente numa escada de valor (isca, entrada,
  principal, premium, continuidade) e escolhe ou revisa o tipo de funil
  para cada uma (captura, WhatsApp local, webinar, aplicação, oferta de
  entrada), usando Russell Brunson como referência e adaptando ao ticket,
  ciclo de venda e operação do cliente. Use quando o usuário pedir "qual
  funil usar", "revisa a oferta e o funil", "monta a escada de valor",
  "como levar o cliente do primeiro contato até a compra maior".
---

# escada-de-valor-e-funil — Ofertas em sequência e o funil certo para cada uma

Decide **qual caminho** o cliente final percorre entre as ofertas e **qual
formato de funil** serve a cada uma. Medir o funil depois é
`desenhar-funil`; analisar gargalo é `analisar-conversao`.

## Quando usar

- O cliente tem (ou vai ter) mais de uma oferta e precisa organizar a
  sequência, ou quer saber qual formato de funil combina com uma oferta.
- Revisão de oferta/funil que não está vendendo, antes de mexer em anúncio.

## Quando não usar

- Criar ou precificar a oferta em si → `criar-produto-e-oferta` / `precificacao`.
- Só medir taxas entre etapas → `desenhar-funil`.
- Planejar um lançamento com fases → `planejar-lancamento`.

## Entradas

- Ofertas atuais e planejadas (o que entregam, preço, recorrência).
- Público, ticket, ciclo de venda e como a venda fecha hoje (site,
  WhatsApp, reunião, loja).
- Capacidade de atendimento e recursos de conteúdo.
- Dados existentes por etapa (com fonte), se houver.

## Dependências

- `knowledge/marketing/FUNIS_LANCAMENTOS_E_METRICAS.md` (escada de valor,
  tipos de funil, quando evitar cada um, métricas)
- `knowledge/projetos/ONTOLOGIA_PROCESSOS_FUNIS_PIPELINES.md` (funil ≠
  pipeline ≠ processo)
- `.claude/skills/desenhar-funil`, `.claude/skills/criar-produto-e-oferta`

## Contexto que deve ser carregado

- `_memoria/empresa.md`, `_memoria/produtos-e-servicos.md`, `_memoria/estrategia.md`
- Diagnóstico e memória do cliente; funis já registrados.

---

## Workflow

### Passo 1 — Mapear as ofertas na escada

Posicionar cada oferta (isca, entrada, principal, premium, continuidade).
Apontar degraus vazios e saltos grandes demais (ex.: da isca direto para
o premium) sem inventar produto: sugerir, marcar como sugestão.

### Passo 2 — Escolher o formato por oferta

Pela tabela "Escolha do funil" da referência: dizer o formato, por que
serve a este cliente, e quando seria melhor outro. Negócio local que fecha
no WhatsApp não precisa de webinar.

### Passo 3 — Gancho, história e oferta

Para a oferta prioritária: gancho (o que faz parar), história (por que
acreditar), oferta (o que leva, condição, garantia real). Sem promessa de
resultado, sem escassez falsa.

### Passo 4 — Etapas e eventos

Listar etapas com o evento que comprova cada entrada e a fonte do dado.
Passar para `desenhar-funil` quando for hora de medir.

### Passo 5 — Revisão (quando já existe funil)

Comparar o funil atual com o formato indicado; apontar desalinhamentos
(oferta cara num funil sem conversa, isca que não leva a nenhuma oferta,
etapa sem evento). Se houver dados, chamar `analisar-conversao`.

## Saídas

- `ESCADA_DE_VALOR_E_FUNIS.md` no projeto: escada com degraus, funil
  escolhido por oferta e justificativa, gancho/história/oferta da
  prioritária, etapas com eventos, pontos de revisão.
- No LOKAT OS: `mkt_funnels` (framework, tipo, posição na escada) e
  `mkt_funnel_stages` (etapas e evento de entrada).

## Regras

- Citar Russell Brunson como referência, nunca como garantia.
- Nenhuma taxa de conversão "padrão de mercado" como meta.
- Sugestão de nova oferta fica marcada como sugestão.

## Critérios de qualidade

- Cada formato escolhido tem "por que serve" e "quando evitar".
- Cada etapa tem evento e fonte.

## Critérios de validação

- A escada não depende de oferta que o cliente não consegue entregar.
- O funil escolhido bate com o jeito que a venda fecha hoje.

## Limitações

- Não valida demanda sozinho; quando houver dúvida, recomenda teste
  pequeno (semente) antes de investir.

## Caminho de salvamento

`workspaces/clientes/<cliente>/projetos/<projeto>/04-marketing/ESCADA_DE_VALOR_E_FUNIS.md`

## Contrato de handoff

Entrega escada e funis. Medição → `desenhar-funil`; campanhas →
`plano-de-campanha`; lançamento → `planejar-lancamento`.

## Exemplos de gatilhos positivos

- "Qual funil faz sentido pra esse consultório?"
- "Revisa a oferta e o funil do curso, não está vendendo"
- "Monta a escada de valor da Lokat"

## Exemplos de gatilhos negativos

- "Quanto devo cobrar?" (→ `precificacao`)
- "Calcula a conversão de cada etapa" (→ `desenhar-funil` / `analisar-conversao`)
