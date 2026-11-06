---
name: design-front-end
description: >
  Orienta direção visual, tipografia, paleta, hierarquia, grid, layout,
  responsividade, acessibilidade, componentes, estados vazios/erro e
  experiência mobile para qualquer interface (site, app, dashboard,
  apresentação visual) de um projeto de cliente ou interno — sempre com
  coerência com a marca real, nunca aparência genérica de template. Use
  como segunda etapa obrigatória depois de pagina-e-site ou app-e-sistema,
  ou quando o usuário pedir "define a direção visual", "como deveria
  ficar essa tela", "revisa o design disso".
---

# design-front-end — Direção visual e experiência de interface

Esta skill **ensina como decidir e aplicar direção visual** em projetos
de site/app/dashboard — ela não constrói um site para o próprio LKT
System. Toda decisão de design é sempre no contexto de um projeto
específico (cliente ou interno), nunca do LKT System em si.

## Quando usar

- Depois de `pagina-e-site` ou `app-e-sistema` já terem definido escopo e
  conteúdo, antes de implementar qualquer tela.
- Quando o usuário pedir revisão de uma interface já existente.

## Quando não usar

- Antes de existir um objetivo/conteúdo definido (isso é
  `pagina-e-site`/`app-e-sistema` primeiro).
- Para decidir arquitetura de dados ou backend — isso é
  `arquitetura-de-software`/`planejar-banco-de-dados`.

## Entradas

- Contexto do projeto (`PROJETO.md`, `00-contexto/`).
- Telas/páginas que precisam de direção visual.

## Dependências

- `_memoria/marca.md` ou `workspaces/clientes/<cliente>/_memoria/marca.md` —
  identidade visual existente (cores, tipografia, logo, referências).
  **Ler antes de propor qualquer coisa.**
- `_memoria/preferencias.md` — tom, que também influencia o "tom visual".

## Contexto que deve ser carregado

Memória de marca do cliente/projeto ativo (via
`.lkt-system/estado/contexto-ativo.json`), ou geral se for projeto interno.

---

## Workflow

### Passo 1 — Ler a marca antes de propor qualquer coisa

Se `marca.md` já tiver paleta/tipografia definidas, usar isso como
restrição, não sugestão. Se estiver vazio, propor uma direção e pedir
validação antes de aplicar em qualquer tela — nunca usar template
genérico "porque sim".

### Passo 2 — Definir a direção

Decidir e documentar (em `<pasta-do-projeto-ativo>/04-marketing/` ou
`07-tecnologia/`, conforme o tipo de entrega):

- **Tipografia:** família, pesos usados, escala de tamanhos, tratamento
  de títulos vs. corpo.
- **Paleta:** cor base, cor de destaque (evitar mais de uma cor de
  destaque competindo), uso em estados (sucesso, erro, alerta).
- **Hierarquia:** o que o olho deve ver primeiro, segundo, terceiro em
  cada tela.
- **Grid e layout:** colunas, espaçamento base, breakpoints.
- **Componentes:** botões, campos, cards — com estado normal, hover,
  desabilitado.
- **Estados vazios:** o que aparece quando não há dado ainda (nunca tela
  em branco sem explicação).
- **Estados de erro:** mensagem específica, não genérica ("algo deu
  errado" não é aceitável — dizer o que houve e o que fazer).
- **Responsividade/mobile:** o que muda de layout, o que
  esconde/reorganiza em telas pequenas.
- **Acessibilidade:** contraste mínimo, tamanho de toque, texto
  alternativo, navegação por teclado quando aplicável.

### Passo 3 — Validar coerência com o negócio real

Antes de finalizar, checar: essa direção faz sentido pro público real
desse negócio? Evitar decisão só porque "fica bonito" sem ligar com quem
vai usar.

### Passo 4 — Entregar

Documentar a direção (não implementar código aqui — isso é
`pagina-e-site`/`app-e-sistema` na fase de implementação) e encaminhar.

---

## Saídas

Direção visual documentada (tipografia, paleta, hierarquia, grid, componentes, estados) pronta pra implementação.

## Regras

- Nunca aparência genérica de template.
- Nunca gradiente, card, número gigante ou efeito visual só pra enfeitar
  — cada elemento tem função.
- Nunca mais de uma cor de destaque competindo por atenção.
- Sempre prever estado vazio e estado de erro — nunca assumir que os
  dados sempre existem.
- Mobile é considerado desde o início, não como ajuste depois.

## Critérios de qualidade

- Toda tela proposta tem hierarquia clara (o que ver primeiro é óbvio).
- Toda decisão de cor/tipografia é rastreável até `marca.md` ou até uma
  justificativa registrada, se `marca.md` estava vazio.

## Critérios de validação

- Nenhuma tela final ignora estado vazio ou estado de erro.
- Direção visual documentada antes de qualquer implementação.

## Limitações

- Não decide conteúdo/copy (isso é `pagina-e-site` + `texto-natural-pt-br`).
- Não implementa código — orienta a decisão que `pagina-e-site` ou
  `app-e-sistema` vão implementar.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/04-marketing/direcao-visual.md` (sites/peças de
marketing) ou `<pasta-do-projeto-ativo>/07-tecnologia/direcao-visual.md`
(apps/sistemas).

## Contrato de handoff

Depois da direção definida, encaminha pra `pagina-e-site` ou
`app-e-sistema` implementarem, e ao final pra `texto-natural-pt-br`
revisar qualquer texto de interface e pra `anti-chat` (quality gate
final).

## Exemplos de gatilhos positivos

- "Define a direção visual desse site"
- "Como deveria ficar essa tela de cadastro"
- "Revisa o design dessa página"

## Exemplos de gatilhos negativos

- "Cria o site" sem direção visual ainda definida (rodar
  `pagina-e-site` primeiro para escopo/conteúdo)
- "Muda a cor do botão" isolado, numa tela já com direção definida (é
  edição pontual, não precisa reabrir a skill inteira)
