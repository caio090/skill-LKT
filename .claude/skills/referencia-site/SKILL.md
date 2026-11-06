---
name: referencia-site
description: >
  Analisa referências visuais e de interação de sites (link, print,
  vídeo) para identificar exatamente o que o usuário quer aproveitar —
  scroll, hero, tipografia, paleta, grid, motion, seção específica ou
  experiência completa — e transforma isso em especificação própria
  para o projeto atual, nunca em cópia literal. Use quando o usuário
  mencionar uma referência de site ("tenho uma referência", "quero
  parecido com esse site", "pega esse scroll", "gostei desse hero") ou
  no início de `pagina-e-site` quando nenhuma referência tiver sido
  dada.
---

# referencia-site — Decomposição de referência visual em especificação própria

## Quando usar

Sempre que existir uma referência externa de site (link, print, vídeo,
repositório) e o usuário quiser aproveitar algo dela. Também
automaticamente no início de `pagina-e-site`, quando o projeto for site
ou landing page novo e nenhuma referência tiver sido fornecida ainda.

## Quando não usar

- Site sem nenhuma referência desejada e o usuário já confirmou que não
  quer usar nenhuma — seguir direto com `design-front-end`.
- Referência já virou ficha (`REF-###`) e a tarefa agora é só
  implementar — usar `pagina-e-site`/`design-front-end` direto.

## Entradas

Link, print, vídeo ou descrição da referência; o que o usuário já
disse que quer aproveitar (se disse).

## Dependências

`templates/design/REFERENCIA-SITE.md`, `templates/design/MOTION-SPEC.md`,
`templates/design/MOTION-DECISION.md`, `docs/GSAP.md`,
`docs/REFERENCIAS-WEB.md`, `preflight-ambiente`, `rotear-ambiente`,
`registrar-prompt`.

## Contexto que deve ser carregado

`_memoria/sistema/marca.md` (ou do workspace) — toda adaptação é em
relação à identidade real do projeto, nunca em relação ao vácuo.

---

## Workflow

### Passo 1 — Perguntar por referência (só quando faltar)

No início de um site/landing page novo, sem referência fornecida:

> "Você tem alguma referência de site que quer usar?"

Não perguntar se o usuário já mandou link, print, vídeo, repositório ou
descrição suficiente.

### Passo 2 — Perguntar o escopo da referência

Nunca assumir que o usuário quer copiar tudo:

> "O que você quer aproveitar dessa referência?"

Aceitar múltiplos itens: scroll, movimento/animações, hero, menu,
tipografia, paleta, composição, grid, espaçamento, seção específica,
transições, cards, fotografia, comportamento mobile, experiência geral,
estrutura completa, ou "ainda não sei, analisa e me mostra o que vale
aproveitar".

### Passo 3 — Decidir onde analisar (operação híbrida)

Rodar `preflight-ambiente` antes de assumir qualquer capacidade. Se o
ambiente atual conseguir analisar a referência adequadamente, continuar
aqui. Senão, usar `rotear-ambiente` — preferência pra referência de
site: Codex Web (quando houver acesso à referência e ao repositório),
ambiente local com browser/Playwright real e configurado, VS Code pra
implementação depois, ou screenshots/gravações fornecidas pelo usuário.
Nunca afirmar que Playwright, Codex Web ou outro recurso está disponível
sem checar `.lkt-system/capabilities.json`.

Se a análise for melhor no Codex Web, gerar prompt numerado via
`registrar-prompt` (ex.: `P####-analisar-referencia-site.md`) contendo:
projeto, cliente, URL, objetivo, aspectos pedidos, stack atual, arquivos
importantes, identidade visual existente, tipografia atual, restrições
do Anti-Chat, e a instrução:

> "Analise esta referência sem reproduzi-la literalmente. Identifique os
> princípios de arquitetura da página, grid, ritmo, espaçamento,
> tipografia, cores, tratamento de imagem, hierarquia, navegação,
> comportamento responsivo, animações, transições, scroll e
> microinterações. Separe: (1) o que existe na referência, (2) o que
> vale aproveitar, (3) o que não combina com o projeto, (4) como
> adaptar, (5) o que precisa de GSAP, (6) o que não precisa. Não copie
> textos, imagens, identidade ou composição pixel a pixel."

Gerar handoff de volta pro ambiente de implementação ao final.

### Passo 4 — Decompor a referência em princípio, nunca em molde

Regra obrigatória: a referência é matéria-prima, não molde. Nunca copiar
automaticamente logo, texto, imagem, ilustração, identidade, código
proprietário ou composição pixel perfect. Identificar o princípio.

Errado: "Copie este hero."
Certo: "A referência usa assimetria, contraste tipográfico grande,
personagem à direita e entrada escalonada — reinterpretar esses
princípios pra identidade deste projeto."

### Passo 5 — Registrar a ficha de referência

Uma ficha por referência, a partir de `templates/design/REFERENCIA-SITE.md`,
em `referencias/sites/REF-###-<slug>.md` (ou caminho equivalente dentro
do cliente/projeto ativo). Nunca guardar só o link — a referência vira
conhecimento utilizável.

### Passo 6 — Múltiplas referências

Se houver mais de uma, criar `REFERENCIAS-MESTRE.md` com tabela
`Referência | Elemento aproveitado | Como será adaptado` — evita
procurar um único site que resolva tudo.

### Passo 7 — Usuário sem referência mas quer pesquisar

Se não houver referência e o usuário quiser ajuda, pesquisar com base em
segmento, posicionamento, público, época, tipo de página/interação,
tipografia, estética e stack — nunca só "melhores sites de X". Preferir
buscas específicas (ex.: "editorial accounting website typography",
"premium restaurant website gsap scroll"). Registrar URLs analisadas.

### Passo 8 — Se houver motion, criar mapa de movimento

`templates/design/MOTION-SPEC.md` por comportamento relevante, e
`templates/design/MOTION-DECISION.md` pra decidir CSS vs. GSAP vs.
Lenis/Locomotive — ver `docs/GSAP.md`.

### Passo 9 — Encaminhar pra implementação

`pagina-e-site` → `design-front-end` → skill(s) de GSAP quando
necessário (`docs/referencias/GSAP-SKILLS.md`) → `texto-natural-pt-br`
→ `anti-chat` → `qa`.

## Saídas

Ficha(s) de referência, `REFERENCIAS-MESTRE.md` (se houver mais de
uma), `MOTION-SPEC.md`/`MOTION-DECISION.md` (se houver motion), e a
especificação pronta pra `pagina-e-site`/`design-front-end`
implementarem.

## Caminho de salvamento

`referencias/sites/` (ou caminho equivalente do workspace/projeto
ativo).

## Regras

- Nunca copiar automaticamente logo, texto, imagem, identidade ou
  composição pixel perfect de uma referência.
- Nunca afirmar disponibilidade de Playwright/Codex Web/MCP sem
  `preflight-ambiente` confirmar.
- Nunca assumir que o usuário quer a experiência completa — sempre
  perguntar o escopo.
- Toda referência analisada vira ficha, nunca só um link solto.

## Critérios de qualidade

O resultado final é rastreável a princípios extraídos da referência
(tipografia, ritmo, hierarquia), nunca a uma reprodução reconhecível da
peça original.

## Critérios de validação

Comparar a entrega final com a referência: elementos literais (texto,
imagem, identidade) não devem coincidir; princípios estruturais
(ritmo, grid, hierarquia) podem coincidir de forma reinterpretada.

## Limitações

Depende do que o ambiente disponível consegue efetivamente acessar da
referência (link acessível, print, vídeo) — sem isso, a análise fica
limitada ao que o usuário descrever.

## Contrato de handoff

Recebe de `pagina-e-site` (início do projeto). Encaminha pra
`design-front-end`, skills de GSAP (`docs/referencias/GSAP-SKILLS.md`)
quando houver motion, e `anti-chat` (que verifica especialmente
reprodução óbvia da referência) como quality gate final.

## Exemplos de gatilhos positivos

- "Tenho uma referência, quero um site parecido com esse scroll"
- "Gostei desse hero, dá pra usar como base?"

## Exemplos de gatilhos negativos

- "Quero um site" sem nenhuma referência e sem interesse em ter uma —
  seguir com `design-front-end` a partir da marca.
- Referência já virou ficha e a tarefa agora é só implementar.
