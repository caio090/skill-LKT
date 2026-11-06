---
name: pagina-e-site
description: >
  Coordena a criação de uma página, landing page ou site (de um projeto
  de cliente ou interno) do contexto até o QA: objetivo, arquitetura de
  informação, conteúdo, estrutura de páginas, copy, implementação,
  responsividade, SEO técnico e QA. Sempre encadeia com design-front-end
  e texto-natural-pt-br. Use quando o usuário pedir "cria um site",
  "preciso de uma landing page", "monta a página de X".
---

# pagina-e-site — Orquestradora de site/landing page

Skill orquestradora: coordena a criação de um site/página **de um
projeto** (cliente ou interno) — nunca cria site para o próprio LKT
System, que não é e não deve virar um site.

## Quando usar

- Início de qualquer página, landing page ou site novo dentro de um
  projeto já existente (`workspaces/clientes/<cliente>/projetos/<projeto>/` ou
  `workspaces/projetos-internos/<projeto>/`).

## Quando não usar

- Sem projeto ativo definido — rodar `novo-projeto` primeiro.
- Para ajuste pontual num site já implementado (corrigir um texto, trocar
  uma cor) — isso é edição direta, não precisa reabrir o fluxo inteiro.

## Entradas

- Objetivo do site/página, público, oferta (do diagnóstico do projeto,
  se já existir).

## Dependências

- `referencia-site` (Passo 0, quando houver referência visual).
- `<pasta-do-projeto-ativo>/01-diagnostico/`, `02-estrategia/` (se
  existirem — usar como base; se não existirem, fazer as perguntas
  mínimas aqui mesmo).
- Skill `design-front-end` (direção visual) — obrigatória antes de
  implementar.
- Skill `texto-natural-pt-br` (acabamento de todo copy) — obrigatória ao
  final.
- `_memoria/marca.md` / `workspaces/clientes/<cliente>/_memoria/marca.md`.

## Contexto que deve ser carregado

Diagnóstico e estratégia do projeto ativo, memória de marca.

---

## Workflow

### Passo 0 — Referência (via `referencia-site`)

Se nenhuma referência tiver sido fornecida ainda, perguntar "Você tem
alguma referência de site que quer usar?" — não perguntar se o usuário
já mandou link, print, vídeo ou descrição suficiente. Havendo
referência, `referencia-site` decompõe o que aproveitar antes de seguir
pro Passo 1. Ver `docs/REFERENCIAS-WEB.md`.

### Passo 1 — Contexto e objetivo

Se não vier do diagnóstico do projeto: perguntar objetivo (venda,
captura de lead, institucional, portfólio), público, e o que a página
precisa provar/comunicar.

### Passo 2 — Arquitetura de informação

Definir: quantas páginas/seções, ordem, o que cada uma precisa conter
pra cumprir o objetivo. Não adicionar seção "porque sites geralmente
têm" — cada seção existe porque atende ao objetivo do Passo 1.

### Passo 3 — Conteúdo e copy

Escrever o conteúdo de cada seção (headline, corpo, CTA). Encaminhar
para `texto-natural-pt-br` ao final desta etapa, antes de implementar
visualmente — corrigir o texto primeiro é mais barato que depois de
implementado.

### Passo 4 — Direção visual

Encaminhar pra `design-front-end` com a arquitetura e conteúdo já
definidos. Não implementar nada antes dessa direção estar clara.

### Passo 5 — Estrutura de páginas / implementação

Implementar conforme a stack do projeto (definida em
`07-tecnologia/` se o projeto já tiver uma, ou perguntar: HTML estático,
framework específico, CMS). Seguir a direção visual do Passo 4
literalmente — não improvisar layout diferente na hora de implementar.

### Passo 6 — Responsividade

Testar/descrever comportamento em mobile, tablet, desktop conforme
definido em `design-front-end`.

### Passo 7 — SEO técnico

Meta title, meta description, headings hierárquicos (H1 único por
página), alt text de imagem, URLs amigáveis, sitemap/robots se aplicável.
Se o projeto já rodou a skill `seo`, reaproveitar os termos/estratégia de
lá em vez de redefinir do zero.

### Passo 8 — QA

Checklist mínimo antes de considerar pronto: links funcionam, formulário
(se houver) envia pra onde deveria, imagens carregam, responsivo nas
larguras principais, sem texto genérico esquecido ("lorem ipsum",
placeholder). Se o projeto tiver a skill `qa`, usar ela para esse passo.

### Passo 9 — Entrega

Salvar em `<pasta-do-projeto-ativo>/08-entregas/` e registrar em
`09-relatorios/` um resumo do que foi entregue.

---

## Saídas

Página/site implementado, com direção visual aplicada, copy revisado e QA executado.

## Regras

- Nunca pular `design-front-end` antes de implementar visualmente.
- Nunca entregar copy sem passar por `texto-natural-pt-br`.
- Nunca criar site para o próprio LKT System — esta skill é sempre sobre
  um projeto de cliente ou interno.
- Nunca usar aparência de template genérico.

## Critérios de qualidade

- Toda página entregue tem objetivo único e claro.
- SEO técnico básico presente (title, description, H1) em toda página.

## Critérios de validação

- QA do Passo 8 rodado antes de considerar entregue.
- Nenhum texto placeholder remanescente na entrega final.

## Limitações

- Não decide arquitetura de backend/dados complexa — isso é
  `app-e-sistema` quando o projeto for além de site institucional/landing.
- Não hospeda nem faz deploy — implementação e deploy real são passos
  manuais do responsável técnico do projeto.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/08-entregas/` (site/página final) e
`<pasta-do-projeto-ativo>/07-tecnologia/` (decisões técnicas).

## Contrato de handoff

`referencia-site` (Passo 0, se houver referência) → `design-front-end`
(Passo 4) → `texto-natural-pt-br` (Passo 3 e revisão final) →
`anti-chat` (quality gate final) → `qa` (Passo 8, se existir).

## Exemplos de gatilhos positivos

- "Cria uma landing page pro lançamento de X"
- "Preciso do site institucional do cliente Y"
- "Monta a página de captura pra esse produto"

## Exemplos de gatilhos negativos

- "Muda o texto do botão do site" (edição pontual, direto no arquivo)
- Pedido sem projeto/cliente associado (perguntar ou rodar `novo-projeto`
  antes)
