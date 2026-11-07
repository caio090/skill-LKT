# Roteamento e precedência

Como uma solicitação vira um conjunto **mínimo** de skills. O agente não lê
todos os `SKILL.md`: consulta o registro (`registry/skills.json`: id,
categoria, descrição, estado) e só abre as skills escolhidas.

## Ordem de decisão

1. **Classificar a intenção**: criar, auditar, revisar, publicar ou executar.
   Diagnóstico nunca vira execução em produção (ver [`sandbox.md`](sandbox.md)).
2. **Reconhecer o contexto**: empresa, cliente, projeto, entrega e ambiente
   (Claude Code, Codex, ChatGPT — ver [`compatibilidade.md`](compatibilidade.md)).
3. **Aplicar regras transversais** (sempre): privacidade e dados de cliente,
   autoria/licença, padrão de qualidade LKT, `texto-natural-pt-br` em texto
   público, `anti-chat` antes de considerar a entrega pronta.
4. **Escolher o conjunto mínimo** pela tabela abaixo. Só skills com estado
   `aprovada` e instaladas no projeto.
5. **Resolver sobreposição** pela precedência.
6. **Fallback**: se a skill não estiver instalada, seguir orientação geral e
   dizer que a skill não foi usada. Nunca alegar ferramenta indisponível.
7. Quando útil, informar ao final quais skills foram usadas.

## Precedência

1. Skill autoral LKT especializada > skill autoral genérica > skill externa.
2. Skill externa só entra se a licença e o ambiente permitirem e se cobrir
   algo que a autoral não cobre.
3. Orquestradora (`*-completa`, `construir-produto-digital`) só quando o
   pedido for o pacote inteiro; senão, a skill pontual.

| Sobreposição | Usar | Complementar com | Não usar para |
|---|---|---|---|
| Página/site | `pagina-e-site` → `design-front-end` → `texto-natural-pt-br` | `referencia-site`, `frontend-design`, `accessibility-review` | — |
| Loja virtual | `ecommerce-loja` | cadeia de página/site; `qa-e2e-playwright` | `cardapio-digital` (é food service) |
| SEO | `seo` | `seo-audit` (auditoria técnica pontual) | — |
| Campanha | `plano-de-campanha` / `campanha-completa` | `campaign-plan` só se pedido em inglês ou formato do plugin | — |
| Conteúdo social | `carrossel`, `publicar-tema` | `content-creation` | — |
| Crítica de design | `design-front-end` (modo revisão) | `design-critique`, `accessibility-review` | — |
| Texto natural | `texto-natural-pt-br` | `humanizer-pt-br` (português), `humanizer` (inglês) | — |
| Qualidade técnica | `qa` (checklist) | `qa-e2e-playwright` (execução de testes) | `qa` como prova de teste executado |
| Automação n8n | `automacao-fluxos` (plano) | `n8n-workflow-check` (JSON verificável) | `automacao-fluxos` como prova de que o fluxo funciona |
| Banco Supabase | `planejar-banco-de-dados` | `supabase-postgres-best-practices` | aplicar migração em produção |
| Visual estático | `canvas-design` | `theme-factory` | substituir código editável de interface |
| Animação de interface | `apple-design`, `emil-design-eng` | `animation-vocabulary`, `review-animations` | vídeo (usar `producao-audiovisual-completa`; Remotion está bloqueado) |
| Imagem gerada | `nano-banana-2`, `image-edit` (exigem conta RunComfy) | — | logo: nunca redesenhar; pedir o arquivo original |
| Copy de interface | `texto-natural-pt-br` | `ux-copy` | deploy de aplicação |

## Cenários de referência

| # | Cenário | Skills esperadas | Não ativar | Saída mínima verificável |
|---|---|---|---|---|
| A | Landing page simples, sem banco | pagina-e-site, design-front-end, texto-natural-pt-br, anti-chat | planejar-banco-de-dados, ecommerce-loja | Estrutura + página + checklist mobile |
| B | App Next.js com banco de teste | app-e-sistema, arquitetura-de-software, planejar-banco-de-dados, supabase-postgres-best-practices, qa-e2e-playwright | migração em produção | SQL revisável + testes rodando contra banco local |
| C | Loja de tênis com consulta de numeração no WhatsApp | ecommerce-loja, pagina-e-site, design-front-end, qa-e2e-playwright | checkout real, disparo de WhatsApp | Link wa.me testado (`tests/link-whatsapp.test.js`) + spec E2E |
| D | Cardápio digital fictício | cardapio-digital, design-front-end | ecommerce-loja | Auditoria com dados fictícios |
| E | Campanha Meta Ads sem publicação | plano-de-campanha, anuncio-meta, texto-natural-pt-br | publicação | Estrutura de campanha documentada |
| F | Automação n8n com dados sintéticos | automacao-fluxos, n8n-workflow-check | webhook real, envio real | JSON com `active: false` + saída do `check_workflow.py` |
| G | Vídeo Remotion | — (bloqueado por licença) | Remotion | Registrar bloqueio; usar skills de roteiro/briefing |
| H | Planilha fictícia | ler-planilha, analisar-dados | — | Resumo com números rastreáveis |
| I | Auditoria visual mobile | design-front-end, accessibility-review, qa-e2e-playwright | — | Lista de achados + screenshots de dados fictícios |
| J | Perfil base em projeto vazio | instalador | — | `.lkt/instalacao.json` + reexecução idempotente (testado em `tests/test_instalador.py`) |

Execução desta revisão: J (instalador real em projeto vazio) e o exemplo de
C (Playwright 8/8 e link WhatsApp 5/5) foram executados. Os demais estão
definidos, não executados.

## Histórico

A versão anterior desta página (REC OS) organizava o roteamento por
`modules/`, que nunca foram criados neste repositório. O roteamento passou a
ser por categoria do registro.
