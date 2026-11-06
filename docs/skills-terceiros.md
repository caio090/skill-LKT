# Skills de terceiros

Registro de origem e licença de toda skill que não foi escrita pela Lokat.
Cada pasta de skill de terceiros carrega o arquivo `LICENSE` (ou
`LICENSE.txt`) original. Levantamento feito em 2026-11-06 a partir das
skills instaladas no computador de trabalho.

Regra: este repositório é público. Só entra skill com licença que permite
redistribuição (MIT, Apache-2.0). Skill sem licença ou com licença
proprietária fica fora e aparece na última seção, com o jeito certo de
instalar.

## Em `.claude/skills/` (carregadas pelo Claude Code)

| Skill | Repositório de origem | Licença | Área no LKT |
|---|---|---|---|
| `frontend-design` | anthropics/claude-plugins-official | Apache-2.0 | Design, site, landing page |
| `canvas-design` | anthropics/skills | Apache-2.0 | Peças visuais estáticas |
| `theme-factory` | anthropics/skills | Apache-2.0 | Temas visuais |
| `web-artifacts-builder` | anthropics/skills | Apache-2.0 | Páginas e protótipos |
| `skill-creator` | anthropics/skills | Apache-2.0 | Criar e testar skills |
| `emil-design-eng` | emilkowalski/skills | MIT | Design de interface |
| `animation-vocabulary` | emilkowalski/skills | MIT | Animação de interface |
| `review-animations` | emilkowalski/skills | MIT | Revisão de animação |
| `accessibility-review`, `design-critique`, `design-handoff`, `design-system`, `research-synthesis`, `user-research`, `ux-copy` | anthropics/knowledge-work-plugins (plugin `design`) | Apache-2.0 | Padrão de design, pesquisa, UX |
| `brand-review`, `campaign-plan`, `competitive-brief`, `content-creation`, `draft-content`, `email-sequence`, `performance-report`, `seo-audit` | anthropics/knowledge-work-plugins (plugin `marketing`) | Apache-2.0 | Social, digital, estratégia |
| `cowork-plugin-customizer`, `create-cowork-plugin` | anthropics/knowledge-work-plugins (plugin `cowork-plugin-management`) | Apache-2.0 | Meta: plugins |
| `applying-brand-guidelines` | anthropics/claude-cookbooks | MIT | Padrão de marca |
| `creating-financial-models` | anthropics/claude-cookbooks | MIT | Planejamento financeiro |
| `analyzing-financial-statements` | anthropics/claude-cookbooks | MIT | Planejamento financeiro |
| `humanizer` | blader/humanizer (v3.1.0) | MIT | Texto natural (inglês) |
| `humanizer-pt-br` | mackswendhell/humanizer-pt-br | MIT | Texto natural (português) |
| `image-edit` | agentspace-so/runcomfy-agent-skills | MIT | Edição de imagem (exige conta RunComfy) |
| `nano-banana-2` | agentspace-so/runcomfy-agent-skills | MIT | Geração de imagem (exige conta RunComfy) |
| `find-skills` | vercel-labs/skills | MIT | Meta: achar skills novas |
| `reverse-engineer-anything` | morluto/rea | MIT | Engenharia reversa de software |

As skills dos plugins `marketing` e `design` usam marcadores de conector
(`~~categoria`); o mapeamento está no `CONNECTORS.md` dentro de cada pasta.
Única alteração feita nelas: o link `../../CONNECTORS.md` (raiz do plugin
original) virou `CONNECTORS.md`, porque o arquivo foi copiado para dentro
da pasta de cada skill.

## Em `terceiros/codex/` (biblioteca do Codex, não carregada sozinha)

Ver [`../terceiros/codex/README.md`](../terceiros/codex/README.md).

## Fora do repositório (licença não permite publicar)

| Skill | Origem | Motivo | Como instalar |
|---|---|---|---|
| `docx`, `pptx`, `xlsx`, `pdf` | Anthropic | Proprietária | Já vêm com a conta Claude |
| `deep-research`, `docs`, `google-workspace`, `morning`, `import-memory`, `built-in-browser`, `chrome-browser`, `computer-use` | Anthropic (app) | Sem licença; dependem de ferramentas do app | Já vêm com a conta Claude |
| `instagram-carousel` | marcolang/Marketing-Skills | Repositório sem licença | `npx skills add marcolang/Marketing-Skills` |
| `browser-automation` | extensão CodeGPT | Sem licença | Vem com a extensão |
| `figma-*` (8 skills) | openai/skills | Termos próprios da Figma | Codex: catálogo padrão |
| `notion-*` (4 skills) | openai/skills | Copyright Notion Labs | Codex: catálogo padrão |
| `aspnet-core`, `gh-address-comments`, `linear`, `migrate-to-codex`, `winui-app` | openai/skills | Sem licença | Codex: catálogo padrão |
| Plugins `product-design`, `sites`, `openai-templates`, `template-creator`, `browser`, `chrome`, `work-pets`, `openai-developers`, `plugin-management` | OpenAI (Codex) | Proprietária | Codex: marketplace |

## Deixadas de fora por escolha

| Skill | Motivo |
|---|---|
| `rea-analysis-optimization`, `rea-changelog-update`, `rea-ci-tests-audit`, `rea-tool-design` | Manutenção interna do repositório morluto/rea; não servem fora dele |
| `cookbook-audit`, `managed_agents/*` | Exemplos do claude-cookbooks, não são skills de uso |
| `diagnostico-lokat`, `novo-cliente` (LKT Plus) | Contêm tabela de preços interna da Lokat; o núcleo já cobre com `onboarding-de-cliente` e `diagnostico-completo` |
