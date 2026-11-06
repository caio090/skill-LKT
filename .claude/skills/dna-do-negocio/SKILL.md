---
name: dna-do-negocio
description: >
  Registra o DNA do negócio — história, propósito, posicionamento,
  público, personalidade, produtos principais, diferenciais, operação,
  canais, limites, concorrentes e objetivos. Vai além de identidade
  visual: orienta cardápio/produto, conteúdo, atendimento, oferta, preço,
  expansão e investimento. Use quando o usuário pedir "registra o DNA do
  negócio", "quem é essa marca de verdade", ou como parte inicial de
  `novo-projeto`/`diagnostico-negocio` para negócios de produto físico
  (food service e afins).
---

# dna-do-negocio — DNA do negócio (além da identidade visual)

## Quando usar

Início de projeto de um negócio com produto físico/cardápio (mas
aplicável a qualquer segmento) — antes de qualquer decisão de cardápio,
oferta, preço ou expansão.

## Quando não usar

- Só identidade visual (cor, tipografia) → `_memoria/marca.md` /
  `design-front-end` — o DNA é mais amplo que isso, mas não substitui o
  arquivo de marca visual, complementa.

## Entradas

Respostas do dono/responsável às perguntas abaixo, e o que já existir em
`CLIENTE.md`/`01-diagnostico/`.

## Dependências

`diagnostico-negocio`, `analisar-publico`, `posicionamento` (reaproveitar
se já existirem).

## Contexto que deve ser carregado

Diagnóstico do cliente/projeto ativo.

---

## Workflow

Registrar, um bloco por vez:

1. **História e origem** — como começou, de verdade.
2. **Propósito prático** — o que o negócio resolve, sem discurso vazio.
3. **Proposta e posicionamento** — o que oferece e como se posiciona.
4. **Público e região** — quem compra, onde.
5. **Personalidade e linguagem** — como fala, o que nunca diria.
6. **Produtos principais, produto-herói, produtos de entrada, produtos
   de margem, produtos sazonais** — mapear cada categoria, não só listar
   o cardápio.
7. **Diferenciais reais** (não genéricos tipo "qualidade").
8. **Experiência prometida** — o que o cliente deve sentir/viver.
9. **Operação** — capacidade real, equipe, horários, limites.
10. **Canais** — onde vende (balcão, delivery próprio, marketplace).
11. **Concorrentes** — quem disputa o mesmo público.
12. **Provas** — o que sustenta a credibilidade (tempo de mercado,
    prêmios, avaliações).
13. **Riscos e objetivos** — o que preocupa, aonde quer chegar.

Salvar em `workspaces/clientes/<cliente>/_memoria/dna-do-negocio.md` (ou
`_memoria/dna-do-negocio.md` se for projeto interno).

## Saídas

`dna-do-negocio.md` com as 13 seções.

## Caminho de salvamento

`workspaces/clientes/<cliente>/_memoria/dna-do-negocio.md`.

## Regras

- Não inventar diferencial ou produto-herói — perguntar se não estiver
  claro.
- Personalidade/linguagem alimenta `_memoria/preferencias.md` do
  cliente, sem duplicar — referenciar, não copiar tudo de novo.

## Critérios de qualidade

Toda seção reflete o negócio real, não um template genérico preenchido
por preencher.

## Critérios de validação

`ficha-tecnica`, `engenharia-de-cardapio` e `criar-produto-e-oferta`
conseguem citar o DNA como referência ao tomar decisão.

## Limitações

Não substitui pesquisa de mercado formal — é a síntese do que o próprio
negócio já sabe sobre si.

## Contrato de handoff

Encaminha pra `ficha-tecnica`, `engenharia-de-cardapio`,
`criar-produto-e-oferta`, `posicionamento`.

## Exemplos de gatilhos positivos

- "Registra o DNA desse negócio antes de mexermos no cardápio"
- "Quem é essa marca de verdade"

## Exemplos de gatilhos negativos

- "Define só a paleta de cores" (é `_memoria/marca.md`/`design-front-end`)
