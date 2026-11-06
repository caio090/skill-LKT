---
name: publicar-tema
description: >
  Orquestra a criação completa de uma peça de conteúdo SEO + redes sociais a partir de um tema.
  Pega um tema (manual ou da estratégia de conteúdo do SEO), escreve o artigo de blog completo,
  gera o carrossel resumo via skill /carrossel, e produz as legendas pra Instagram, Facebook e
  LinkedIn — tudo amarrado, com o carrossel apontando pro blog.
  Use quando o usuário pedir "publicar tema", "gera o conteúdo do tema X", "transforma esse tema
  em post", "cria o conteúdo completo", ou /publicar-tema.
---

# /publicar-tema — Pipeline de conteúdo SEO + redes sociais

Skill orquestradora. Pega um tema → entrega artigo no blog + carrossel + 3 legendas (Insta, FB, LinkedIn), tudo conectado.

## Dependências

- **Estratégia de conteúdo:** `<pasta-do-projeto-ativo>/04-marketing/seo/05-estrategia-conteudo.md` (lista mestra de temas, criada pelo `seo`)
- **Outras pesquisas SEO:** `<pasta-do-projeto-ativo>/04-marketing/seo/01-pesquisa-demanda.md`, `02-analise-concorrencia.md`, `08-geo-otimizacao-ia.md`
- **Skill carrossel:** `.claude/skills/carrossel/SKILL.md` — usar pra fase do carrossel
- **Site (blog):** o site do cliente/negócio é um projeto externo ao LKT System (repositório próprio, não faz parte desta estrutura) — perguntar o caminho real na primeira vez e registrar em `workspaces/clientes/<cliente>/CLIENTE.md`. Estruturas comuns: Astro (`.../src/content/blog/`), WordPress, ou outro. Se ainda não tiver site, perguntar antes de seguir
- **Tom de voz:** `_memoria/preferencias.md`
- **Contexto:** `_memoria/empresa.md`, `_memoria/marca.md`

---

## Workflow

### Passo 0 — Escolher o tema

Se o usuário passou um tema explícito → usar.

Se não passou nada → ler `<pasta-do-projeto-ativo>/04-marketing/seo/05-estrategia-conteudo.md`, listar os artigos satélite + a página pilar, e perguntar:

> "Qual tema da estratégia? (lista de opções)"

Marcar mentalmente quais já viraram blog (checar pasta do blog) pra não duplicar.

### Passo 1 — Pesquisa rápida

Antes de escrever, ler o que tem nas pesquisas SEO sobre esse tema:
- Keyword principal e variações (`01-pesquisa-demanda.md`)
- Como concorrentes tratam (`02-analise-concorrencia.md`) — pra fugir do óbvio
- Ângulo GEO se aplicável (`08-geo-otimizacao-ia.md`) — perguntas que IAs respondem

### Passo 2 — Escrever o blog post

**Destino:** depende do stack do site. Padrões comuns:
- Astro: `site/astro-site/src/content/blog/<slug>.md`
- WordPress: gerar markdown que o usuário cola no editor
- Outro: confirmar com o usuário

**Slug:** kebab-case curto, sem stopwords. Ex: "Como conservar carne salgada no restaurante" → `conservar-carne-salgada`.

**Frontmatter (se o stack usa markdown com frontmatter):**

```yaml
---
title: "Título atrativo, próximo da keyword"
description: "Meta description 150-160 caracteres, com keyword e benefício pro leitor"
publishedAt: YYYY-MM-DD
author: "<nome configurado em _memoria/empresa.md>"
keywords:
  - keyword principal
  - variação 1
  - variação 2
draft: true
---
```

**Sempre começar com `draft: true`.** O usuário revisa e flipa pra `false` quando aprovar.

**Estrutura do artigo (800-1500 palavras):**

1. **Lead (1-2 parágrafos):** problema concreto do público, sem enrolação
2. **H2 explicativo:** o quê e por quê
3. **H2 prático:** como fazer / o que olhar
4. **H2 comparativo ou de detalhe técnico** (opcional)
5. **H2 onde a empresa se encaixa:** conexão natural com o produto, sem ser propaganda
6. **CTA final:** link WhatsApp / formulário / contato configurado

**Regras de escrita** (seguir `_memoria/preferencias.md` estritamente):
- Sem jargão de marketing/inglês quando o público não usa
- Frases curtas, parágrafos de 2-4 linhas
- Concreto: números, certificações, datas, valores quando souber
- Markdown limpo: `##` pra H2, `###` pra H3, listas com `-`, links em `[texto](url)`

### Passo 3 — Carrossel resumo

**Sem perguntar, partir direto pra criação do carrossel** chamando `.claude/skills/carrossel/SKILL.md` (tipo 1: carrossel texto puro).

**Pasta:** `<pasta-do-projeto-ativo>/04-marketing/<slug-do-blog>-<YYYY-MM-DD>/`

Estrutura de slides do resumo:
- **Slide 1 — capa:** mesmo título do blog (ou variação enxuta)
- **Slides 2-6:** os pontos-chave do blog (1 ideia por slide, frase natural, não bullet seco)
- **Slide final — CTA pro blog:** "Texto completo no nosso blog" + URL `<dominio>/blog/<slug>`

**Capa:** seguir sequência alternada do feed (claro → foto/escuro → cor principal → repete) — checar `<pasta-do-projeto-ativo>/04-marketing/` mais recente.

### Passo 4 — Legendas (3 versões)

Salvar todas em `<pasta-do-projeto-ativo>/04-marketing/<pasta-do-carrossel>/`:

**`legenda.md`** (Instagram + Facebook — mesmo texto):
- Hook na primeira linha
- 2-3 parágrafos de contexto (frases naturais, sem corporativês)
- CTA pro carrossel ("Arraste pro lado") + CTA pro blog ("Texto completo no link da bio" ou URL direta)
- Bloco oferta da empresa (diferenciais, contato)
- 10-15 hashtags (público + nicho + local)

**`legenda-linkedin.md`** (LinkedIn — mais formal, sem hashtags):
- Hook (pode ser provocativo, profissional)
- 3-5 parágrafos analíticos — LinkedIn aceita texto longo
- Sem "arraste pro lado" (público diferente, comportamento diferente)
- CTA: link direto pro blog
- Sem bloco de oferta agressivo — fechar com 1 linha de quem é a empresa
- Máx 3 hashtags no final, do nicho profissional

### Passo 5 — Resumo de entrega

No fim, mostrar pro usuário uma lista clara:

```
✓ Blog post: <caminho>/<slug>.md (draft)
✓ Carrossel: <pasta-do-projeto-ativo>/04-marketing/<pasta>/
  - carrossel.html + render.js
  - PNGs em instagram/
✓ Legendas:
  - legenda.md (Insta + FB)
  - legenda-linkedin.md

Pra publicar:
1. Revisar o blog → flipar draft: false
2. Rebuild do site (se Astro/Hugo/etc) ou copiar pro CMS
3. Renderizar PNGs do carrossel: cd <pasta-do-projeto-ativo>/04-marketing/<pasta> && node render.js
4. Postar carrossel no Insta + FB com legenda.md (ou usar /aprovar-post)
5. Postar texto + link no LinkedIn com legenda-linkedin.md
```

---

## Quando usar

- Tema (manual ou da estratégia de conteúdo do SEO) pronto pra virar
  artigo de blog + carrossel + legendas conectados.

## Quando não usar

- Pedido de carrossel avulso (sem blog) → usar `carrossel` direto
- Atualização de artigo existente → editar direto o .md
- Post único, frase de impacto → `carrossel`

## Entradas

Tema (explícito ou da estratégia de conteúdo já levantada por `seo`).

## Contexto que deve ser carregado

`_memoria/empresa.md`, `preferencias.md`, `marca.md`, pesquisas de SEO
do projeto ativo se existirem.

## Saídas

Artigo de blog (draft), carrossel resumo e 3 legendas (Instagram/
Facebook, LinkedIn), todos conectados entre si.

## Caminho de salvamento

Blog na estrutura do site do cliente (fora do LKT System); carrossel e
legendas em `<pasta-do-projeto-ativo>/04-marketing/`.

## Critérios de qualidade

- Blog é sempre a peça-mãe — carrossel e legendas derivam dele.
- Nunca publicado automaticamente — sempre `draft: true` até revisão.

## Critérios de validação

- Carrossel referencia o blog e vice-versa (link/CTA cruzado).

## Limitações

- Depende do site do cliente existir e ter stack conhecida (Astro,
  WordPress, etc.) — se não houver site, perguntar antes de seguir.

## Contrato de handoff

`carrossel` (Passo 3), `aprovar-post` (publicação final, nunca
automática).

## Regras

1. **Blog é a peça-mãe.** Carrossel e legendas são derivados dele, não o contrário.
2. **Tudo conectado.** Cada peça referencia a outra (carrossel linka pro blog, blog tem CTA pro contato).
3. **Draft sempre.** Nunca publicar automaticamente — usuário revisa antes (ou usa `aprovar-post`).
4. **Linguagem do público real.** Sem corporativês. Sempre.

## Exemplos de gatilhos positivos

- "Publicar tema"
- "Gera o conteúdo do tema X"
- "Transforma esse tema em post completo"

## Exemplos de gatilhos negativos

- "Cria só um carrossel avulso, sem blog" (é `carrossel` direto)
- "Publica o que já foi criado" (conteúdo já pronto — é `aprovar-post`)
