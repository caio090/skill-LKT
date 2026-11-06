---
name: proposta-e-precificacao
description: >
  Gera escopo, entregáveis, responsabilidades por papel, dependências,
  custos externos, preço, condições e limites de um projeto, a partir
  do diagnóstico (quando existir). Separa implantação, recorrência,
  manutenção e serviço avulso, e nunca apresenta desconto ou preço sem
  explicar a composição. Use quando o usuário disser "monta uma
  proposta", "quanto isso custa", "precifica isso", "manda um
  orçamento".
---

# proposta-e-precificacao — Escopo, preço e condições, com composição visível

Gera a proposta comercial e a precificação de um projeto, sempre
mostrando como o preço foi composto e o que não está incluído. Nunca
apresenta um valor "no chute" sem explicar a base de cálculo.

## Quando usar

- Depois do diagnóstico, quando o projeto já tem escopo claro o
  suficiente para orçar.
- Quando o usuário pede preço, orçamento ou proposta diretamente,
  mesmo sem diagnóstico formal (nesse caso, avisar que o preço é uma
  estimativa até o escopo ser confirmado).

## Quando não usar

- Para simplesmente informar um preço de tabela já fixado em
  `catalogo/servicos/` — nesse caso é só consulta, não precisa gerar
  proposta nova.

## Entradas

- Escopo do projeto (`PROJETO.md`, diagnóstico se existir).
- Entregáveis previstos.
- Prazo e forma de entrega.
- Custos externos conhecidos (ferramenta, mídia, terceiro, hospedagem,
  domínio, licença, deslocamento).
- Desconto ou contrapartida, se houver (sempre com aprovação
  registrada).

## Dependências

- `templates/proposta/PROPOSTA-COMERCIAL.md`
- `templates/documentos/README.md` (para apresentação/relatório
  correlatos)
- `schemas/proposta.schema.json`
- `catalogo/servicos/`, `catalogo/entregaveis/`
- `.claude/skills/diagnostico-empresarial` (entrada, quando existir)

## Contexto que deve ser carregado

- `PROJETO.md` e diagnóstico do projeto ativo, se existirem.
- `_memoria/sistema/produtos-e-servicos.md`.

---

## Workflow

### Passo 1 — Montar a composição do preço

```
Preço recomendado =
  estratégia
  + produção
  + tecnologia
  + operação
  + gestão
  + risco
  + margem
  + despesas externas
  - desconto aprovado
```

Separar sempre, quando aplicável: implantação, recorrência, manutenção,
serviço avulso, ferramenta, custo de terceiro, mídia, deslocamento,
hospedagem, domínio, licença, imposto estimado, contingência, desconto,
contrapartida.

### Passo 2 — Montar o escopo

O que será feito, por que será feito, o que será entregue, formato da
entrega, prazo, responsabilidades por papel, limites, dependências,
itens não incluídos, próximos passos, condições de continuidade
(nova fase ou novo contrato — nunca presumir suporte permanente por
padrão, ver `docs/METODO_DE_TRABALHO.md`).

### Passo 3 — Gerar o documento

Formato conforme o destino (ver `docs/PADRAO_DE_ARQUIVOS.md`):
Markdown/TXT para uso interno, DOCX quando for editável pelo cliente,
PDF para a versão final assinável, PPTX se for apresentação comercial.

### Passo 4 — Salvar e registrar

Salvar em `.../04-comercial/`. Atualizar `PROJETO.md` (orçamento,
entregas previstas) e registrar a decisão de preço em
`_memoria/decisoes/decisoes.md` se envolver desconto ou condição fora
do padrão.

---

## Saídas

Proposta com escopo e composição de preço explícita, salva no formato
certo para o destino, com o que não está incluído sempre visível.

## Regras

- Nunca apresentar preço sem mostrar (ao menos internamente) a
  composição.
- Nunca aplicar desconto sem registrar quem aprovou.
- Nunca prometer continuidade/manutenção que não esteja explicitamente
  no escopo.
- Responsável sempre por papel, nunca só nome solto.

## Critérios de qualidade

- Toda proposta lista: o que é, por que, o que entrega, prazo,
  responsabilidades, limites, dependências, o que não está incluído,
  condições de continuidade.

## Critérios de validação

- Preço final bate com a soma dos componentes declarados.
- Documento gerado no formato certo para o uso (ver
  `docs/PADRAO_DE_ARQUIVOS.md`).

## Limitações

- Não decide o preço sozinha quando não há dado de custo — nesse caso,
  apresenta a composição com os campos que faltam como pendência.
- Não envia nem publica a proposta — só gera o documento.

## Caminho de salvamento

`workspaces/<tipo>/<slug>/projetos/<projeto>/04-comercial/`

## Contrato de handoff

Recebe de `diagnostico-empresarial`. Encaminha para execução do módulo
correspondente depois de a proposta ser aprovada.

## Exemplos de gatilhos positivos

- "Monta uma proposta pra esse projeto"
- "Quanto isso custa?"

## Exemplos de gatilhos negativos

- "Qual o preço da tabela de [serviço]?" quando já existe preço fixo em
  `catalogo/servicos/` (é consulta direta, não gera proposta nova)
