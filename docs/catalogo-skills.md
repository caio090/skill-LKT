# Catálogo de skills

Lista de todas as skills ativas em `.claude/skills/`. Atualizar sempre que
uma skill for criada, migrada ou removida — ver regra de validação em
[`../CLAUDE.md`](../CLAUDE.md).

Total: 163 skills — 127 do núcleo Sistema LKT (v1.0.0), 2 do LKT Plus e
34 de terceiros. Origem e licença de cada skill de terceiros em
[`skills-terceiros.md`](skills-terceiros.md). Skills do Codex (OpenAI)
ficam à parte, em [`../terceiros/codex/`](../terceiros/codex/README.md).

| Skill | Descrição | Origem |
|---|---|---|
| `abrir` | Abre uma sessão de trabalho carregando a memória do negócio (empresa, preferências, estratégia, marca) e devolve um resumo curto pro usuário. | Sistema LKT |
| `accessibility-review` | Run a WCAG 2.1 AA accessibility audit on a design or page. | Terceiros: anthropics/knowledge-work-plugins (design) · Apache-2.0 |
| `analisar-concorrentes` | Mapeia concorrentes reais de um cliente/projeto (via WebSearch/WebFetch): quem são, o que oferecem, pontos fortes/fracos, gaps e oportunidades. | Sistema LKT |
| `analisar-conversao` | Calcula e explica volume, taxa, perda, tendência e gargalo de um funil ou pipeline, com hipótese, recomendação e nível de confiança — sinalizando quando faltar dado suficiente. | Sistema LKT |
| `analisar-dados` | Analisa um arquivo de dados (CSV, Excel, TXT, JSON) e gera um resumo executivo com os principais insights, tendências e recomendações. | Sistema LKT |
| `analisar-promocao-cupom` | Analisa se uma promoção/cupom vale a pena: quem paga o desconto (loja, plataforma ou compartilhado), margem antes e depois, volume necessário pra compensar, novos clientes vs. | Sistema LKT |
| `analisar-publico` | Aprofunda quem é o público real de um cliente/projeto: perfil, dor, processo de decisão de compra, objeções, onde ele está. | Sistema LKT |
| `analisar-video` | Analisa um vídeo já existente (próprio ou de referência/concorrente): estrutura, ritmo, gancho, retenção estimada, pontos fortes e fracos. | Sistema LKT |
| `analyzing-financial-statements` | This skill calculates key financial ratios and metrics from financial statement data for investment analysis | Terceiros: anthropics/claude-cookbooks · MIT |
| `animation-vocabulary` | Reverse-lookup glossary that turns a vague description of a web animation or motion effect into its exact term ("the bouncy thing when a popover opens" → Pop in; "the iOS rubber... | Terceiros: emilkowalski/skills · MIT |
| `anti-chat` | Quality gate transversal contra aparência e linguagem genérica de IA: design de template, gradiente/glassmorphism gratuito, cards demais, tipografia preguiçosa, texto motivacion... | Sistema LKT |
| `anuncio-google` | Cria estrutura completa de campanha do Google Ads a partir de um briefing ou da pesquisa SEO. | Sistema LKT |
| `anuncio-meta` | Monta estrutura de campanha do Meta Ads (Instagram/Facebook) a partir de briefing/estratégia: campanha, conjuntos de anúncio, públicos, criativos e copy — pronta pra configurar ... | Sistema LKT |
| `app-e-sistema` | Coordena escopo, usuários, fluxos, permissões, dados, integrações, interface, backlog, arquitetura, QA e documentação de um aplicativo ou sistema de um projeto de cliente ou int... | Sistema LKT |
| `applying-brand-guidelines` | This skill applies consistent corporate branding and styling to all generated documents including colors, fonts, layouts, and messaging | Terceiros: anthropics/claude-cookbooks · MIT |
| `aprovar-post` | Prepara um conteúdo já aprovado (blog + carrossel + legendas, criado por publicar-tema ou carrossel) para publicação, montando um pacote local pronto pra postar. | Sistema LKT |
| `arquitetura-de-software` | Define a arquitetura técnica de um sistema/app: componentes, stack, integrações, estratégia de deploy, versionamento e plano de migração quando aplicável. | Sistema LKT |
| `atendimento` | Responde dúvidas/solicitações de clientes já ativos, e cobre retenção (identificar risco de cancelamento e agir) e análise de churn (por que clientes saem). | Sistema LKT |
| `atualizar` | Varre o projeto e atualiza os arquivos de contexto (`_memoria/empresa.md`, `preferencias.md`, `estrategia.md`, `CLAUDE.md`, `identidade/design-guide.md`) que ficaram desatualiza... | LKT Plus |
| `atualizar-memoria` | Varre o projeto e compara com os 13 arquivos de _memoria/ (empresa, preferências, estratégia, marca, produtos-e-servicos, processos, ferramentas, equipe, métricas, decisões, apr... | Sistema LKT |
| `auditar-planilha` | Audita uma planilha financeira já lida (ler-planilha): mapeia fórmulas com erro, referências quebradas, abas ocultas, inconsistências de status/categoria, e explica o que descob... | Sistema LKT |
| `auditar-repositorio` | Audita um repositório de código: estrutura, dependências desatualizadas/vulneráveis, segredos expostos, cobertura de teste, documentação e convenções — sem corrigir nada sozinha. | Sistema LKT |
| `auditoria-completa` | Orquestra uma auditoria completa de um cliente/projeto: financeiro (planilhas), técnico (repositório/sistema) e operacional, consolidando achados num relatório único. | Sistema LKT |
| `aumento-de-ticket` | Analisa ticket médio e mapeia oportunidades reais de aumento (combo, adicional, tamanho, sobremesa, bebida, oferta de volume, sugestão de atendimento, posição no cardápio, pós-c... | Sistema LKT |
| `automacao-fluxos` | Planeja e documenta automações de fluxo (n8n ou equivalente) e de WhatsApp Business: gatilho, passos, integrações envolvidas, tratamento de erro. | Sistema LKT |
| `automatizar-fluxo` | Transforma uma etapa de processo/funil/pipeline em regra de automação, sempre distinguindo sugestão, execução assistida, execução com confirmação e execução automática — nunca c... | Sistema LKT |
| `brand-review` | Review content against your brand voice, style guide, and messaging pillars, flagging deviations by severity with specific before/after fixes. | Terceiros: anthropics/knowledge-work-plugins (marketing) · Apache-2.0 |
| `briefing-audiovisual` | Coleta o briefing de uma produção audiovisual: objetivo, mensagem, público, formato, duração, referências, orçamento e prazo. | Sistema LKT |
| `briefing-completo` | Coleta e organiza o briefing completo de um projeto ou entrega específica (o que precisa, pra quem, prazo, restrições, referências). | Sistema LKT |
| `briefing-de-edicao` | Prepara o briefing para o editor: seleção de melhores tomadas, ritmo, trilha, cor, legendas, versões por formato/plataforma e critério de aprovação final. | Sistema LKT |
| `cac-e-ltv` | Calcula e explica CAC, LTV, relação LTV/CAC, payback, ROI e ROAS — as métricas de retorno sobre investimento em aquisição/retenção de cliente. | Sistema LKT |
| `calcular-cmv` | Calcula CMV (custo de mercadoria/serviço vendido), custo interno, margem de contribuição, estoque e desperdício de um negócio, a partir de ficha técnica ou dado de compra/consumo. | Sistema LKT |
| `calendario-de-conteudo` | Monta o calendário editorial recorrente (não de campanha específica): temas, formato, canal e frequência, coerente com a estratégia de marketing. | Sistema LKT |
| `campaign-plan` | Generate a full campaign brief with objectives, audience, messaging, channel strategy, content calendar, and success metrics. | Terceiros: anthropics/knowledge-work-plugins (marketing) · Apache-2.0 |
| `campanha-completa` | Orquestra uma campanha de marketing do zero: contexto, objetivo, público, oferta, canais, conceito, peças, mídia, calendário e relatório — encadeando as skills de estratégia, co... | Sistema LKT |
| `canvas-design` | Create beautiful visual art in .png and .pdf documents using design philosophy. | Terceiros: anthropics/skills · Apache-2.0 |
| `cardapio-digital` | Audita o cardápio digital (categorias, produtos, adicionais, combos, fotos, descrições, disponibilidade, horários, taxas, retirada, entrega, pagamento, cupons) e cruza com produ... | Sistema LKT |
| `carrossel` | Cria carrosséis e posts visuais pra Instagram, TikTok, LinkedIn com a identidade visual da marca. | Sistema LKT |
| `classificar-nivel` | Classifica um workspace/projeto numa dimensão de maturidade (ex.: maturidade digital, financeira, comercial) com base em evidência real — nunca por impressão vaga. | Sistema LKT |
| `cmv-real-e-teorico` | Especialização food service de calcular-cmv: compara CMV real (a partir de estoque) com CMV teórico (a partir de vendas × ficha técnica), localiza a lacuna e investiga causas pr... | Sistema LKT |
| `competitive-brief` | Research competitors and generate a positioning and messaging comparison with content gaps, opportunities, and threats. | Terceiros: anthropics/knowledge-work-plugins (marketing) · Apache-2.0 |
| `configurar-pipeline` | Configura um pipeline — visualização de onde cada item (oportunidade, candidato, chamado) está agora. | Sistema LKT |
| `construir-produto-digital` | Orquestra a construção de um produto digital do zero: escopo, especificação, arquitetura, banco de dados, integrações, interface, QA e documentação — encadeando as skills do mód... | Sistema LKT |
| `content-creation` | Draft marketing content across channels — blog posts, social media, email newsletters, landing pages, press releases, and case studies. | Terceiros: anthropics/knowledge-work-plugins (marketing) · Apache-2.0 |
| `continuar-projeto` | Lê a memória, as decisões, as pendências e os arquivos recentes de um workspace ou projeto, e informa o próximo passo — sem repetir perguntas já respondidas. | Sistema LKT |
| `cowork-plugin-customizer` | Customize a Claude Code plugin for a specific organization's tools and workflows. | Terceiros: anthropics/knowledge-work-plugins (cowork-plugin-management) · Apache-2.0 |
| `create-cowork-plugin` | Guide users through creating a new plugin from scratch in a cowork session. | Terceiros: anthropics/knowledge-work-plugins (cowork-plugin-management) · Apache-2.0 |
| `creating-financial-models` | This skill provides an advanced financial modeling suite with DCF analysis, sensitivity testing, Monte Carlo simulations, and scenario planning for investment decisions | Terceiros: anthropics/claude-cookbooks · MIT |
| `criar-apresentacao` | Cria uma apresentação (slides) para reunião, proposta, palestra ou relatório de um projeto, coerente com a marca. | Sistema LKT |
| `criar-campanha` | Gera uma campanha completa — briefing, objetivo, público, oferta, canais, cronograma, ativos, página, conteúdos, orçamento, funil associado, eventos de conversão, metas, plano d... | Sistema LKT |
| `criar-documento` | Cria ou edita um documento de texto (Word/Markdown/rich text) para um projeto — proposta, relatório, briefing, contrato, manual. | Sistema LKT |
| `criar-pdf` | Converte um documento, relatório ou apresentação já finalizado em PDF para entrega, preservando o arquivo-fonte original. | Sistema LKT |
| `criar-planilha` | Cria ou edita uma planilha (custos, fluxo de caixa, orçamento, cronograma, controle) para um projeto. | Sistema LKT |
| `criar-produto-e-oferta` | Estrutura ou refina um produto/serviço e sua oferta comercial (o que inclui, preço, condição, garantia) com base no diagnóstico, público e posicionamento do cliente/projeto. | Sistema LKT |
| `criar-sop` | Documenta um processo operacional recorrente em SOP (procedimento padrão): passo a passo, responsável, ferramenta, tempo estimado, critério de qualidade. | Sistema LKT |
| `depurar-erro` | Investiga e corrige um erro/bug específico: reproduz, localiza causa raiz, corrige, e confirma que não quebrou outra coisa. | Sistema LKT |
| `desenhar-funil` | Desenha um funil de conversão — quantidade e taxa de passagem de uma entidade (visitante, lead, candidato) entre etapas até um resultado final. | Sistema LKT |
| `design-critique` | Get structured design feedback on usability, hierarchy, and consistency. | Terceiros: anthropics/knowledge-work-plugins (design) · Apache-2.0 |
| `design-front-end` | Orienta direção visual, tipografia, paleta, hierarquia, grid, layout, responsividade, acessibilidade, componentes, estados vazios/erro e experiência mobile para qualquer interfa... | Sistema LKT |
| `design-handoff` | Generate developer handoff specs from a design. | Terceiros: anthropics/knowledge-work-plugins (design) · Apache-2.0 |
| `design-system` | Audit, document, or extend your design system. | Terceiros: anthropics/knowledge-work-plugins (design) · Apache-2.0 |
| `diagnostico-completo` | Orquestra o diagnóstico completo de um cliente/projeto novo, do contexto ao plano de ação, encadeando as skills menores do módulo de diagnóstico e estratégia. | Sistema LKT |
| `diagnostico-empresarial` | Analisa os pilares aplicáveis de um workspace ou projeto (negócio, oferta, público, marca, marketing, presença digital, conteúdo, comercial, atendimento, financeiro, operação, l... | Sistema LKT |
| `diagnostico-negocio` | Diagnostica a situação atual de um negócio/cliente: modelo, operação, finanças macro, marketing, comercial, o que funciona e o que trava. | Sistema LKT |
| `diagnostico-tecnico` | Diagnostica a situação técnica de um sistema/projeto existente: stack, débito técnico, riscos de segurança básicos, performance percebida e o que trava a evolução. | Sistema LKT |
| `direcao-de-cena` | Orienta a execução no dia de gravação: o que checar antes de cada cena, direção de talento/depoimento, continuidade em tempo real e critério de "cena aprovada, pode seguir". | Sistema LKT |
| `dna-do-negocio` | Registra o DNA do negócio — história, propósito, posicionamento, público, personalidade, produtos principais, diferenciais, operação, canais, limites, concorrentes e objetivos. | Sistema LKT |
| `documentar-sistema` | Documenta um sistema/projeto técnico: visão geral, arquitetura, como rodar localmente, como fazer deploy, decisões técnicas importantes. | Sistema LKT |
| `draft-content` | Draft blog posts, social media, email newsletters, landing pages, press releases, and case studies with channel-specific formatting and SEO recommendations. | Terceiros: anthropics/knowledge-work-plugins (marketing) · Apache-2.0 |
| `dre` | Monta e explica o DRE (Demonstrativo de Resultado) de um período: receita, deduções, CMV/custo de serviço, margem bruta, despesas, resultado operacional e líquido — e compara pr... | Sistema LKT |
| `email-profissional` | Rascunha um email profissional a partir de um contexto livre. | Sistema LKT |
| `email-sequence` | Design and draft multi-email sequences with full copy, timing, branching logic, exit conditions, and performance benchmarks. | Terceiros: anthropics/knowledge-work-plugins (marketing) · Apache-2.0 |
| `emil-design-eng` | This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that make software feel great. | Terceiros: emilkowalski/skills · MIT |
| `engenharia-de-cardapio` | Analisa popularidade, margem de contribuição, faturamento, quantidade vendida e posição no cardápio (físico e digital) de cada produto, separando o que vende muito, dá margem, é... | Sistema LKT |
| `especificacao-de-produto` | Escreve especificação de produto digital: problema, solução, backlog priorizado e roadmap por fase. | Sistema LKT |
| `estoque-food-service` | Controla estoque central e de cozinha separadamente: compras, entradas, transferências, consumo, perdas, validade, cortesia, refeição de equipe, correções, devoluções e ajustes. | Sistema LKT |
| `estrategia-de-marketing` | Define a estratégia de marketing de um cliente/projeto: objetivos, canais prioritários, mensagem (a partir do posicionamento), verba e cronograma macro — antes de qualquer peça ... | Sistema LKT |
| `estruturar-crm` | Estrutura o CRM de um cliente/projeto: etapas do funil, campos por lead/cliente, critérios de qualificação e regras de movimentação entre etapas — não é um CRM web, é a estrutur... | Sistema LKT |
| `estruturar-pagina-de-oferta` | Estrutura uma página de oferta/venda — headline, promessa, público, dor, oferta, prova, demonstração, expert (quando existir), CTA, FAQ, garantia, checkout e evento de conversão... | Sistema LKT |
| `fechar-sessao` | Encerra o foco no cliente/projeto atual de forma segura: atualiza .lkt-system/estado/contexto-ativo.json (limpa cliente/projeto ativo ou troca pra outro), sem apagar histórico. | Sistema LKT |
| `ficha-tecnica` | Cria, revisa e atualiza a ficha técnica de um produto de food service: ingredientes, quantidades, unidades, peso bruto/líquido/final, rendimento, porção, embalagem, mão de obra ... | Sistema LKT |
| `find-skills` | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in extendin... | Terceiros: vercel-labs/skills · MIT |
| `fluxo-de-caixa` | Organiza entradas e saídas por período, calcula saldo projetado e de capital de giro, e explica em linguagem simples o que o fluxo de caixa significa pra decisão do dono. | Sistema LKT |
| `frontend-design` | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. | Terceiros: anthropics/claude-plugins-official · Apache-2.0 |
| `funil-de-vendas` | Acompanha e analisa o funil de vendas já estruturado: quantos leads em cada etapa, taxa de conversão entre etapas, tempo médio, gargalos, e documenta o playbook comercial (o que... | Sistema LKT |
| `gerar-escopo-por-nivel` | Monta o escopo interno completo de um projeto a partir de um nível recomendado e seu perfil de entrega, separando obrigatório, recomendado, opcional, futuro e não incluso. | Sistema LKT |
| `gerar-plano-de-avanco` | Transforma a lacuna entre nível atual e recomendado (recomendar-nivel) em ações concretas — entregas, tarefas, responsáveis por papel, dependências, prazo, custo, validação, ris... | Sistema LKT |
| `gerar-proposta-a-partir-do-nivel` | Traduz a inteligência interna dos níveis (escopo, plano de avanço, recomendação) para a camada comercial — só o que o cliente precisa entender para decidir. | Sistema LKT |
| `gestao-de-negocio` | Consolida vendas, custos, despesas, caixa, produtos, clientes, campanhas, estoque e decisões de um negócio (com especialização em food service, adaptável a outros segmentos) e i... | Sistema LKT |
| `humanizer` | Rewrite AI-sounding text so it reads like the writer without changing what it says. | Terceiros: blader/humanizer · MIT |
| `humanizer-pt-br` | Remove traços de escrita gerada por IA de textos em português brasileiro, tornando-os mais naturais, humanos e com personalidade real. | Terceiros: mackswendhell/humanizer-pt-br · MIT |
| `image-edit` | Edit images on RunComfy — this skill is a smart router that matches the user's intent to the right edit model in the RunComfy catalog. | Terceiros: agentspace-so/runcomfy-agent-skills · MIT |
| `instalar` | Instala o Sistema LKT no negócio ou projeto onde a pasta foi copiada. | Sistema LKT |
| `integrar-api` | Planeja e documenta a integração com uma API externa (pagamento, WhatsApp, CRM, cardápio digital, etc.): autenticação, endpoints usados, tratamento de erro, e adaptador de dados... | Sistema LKT |
| `ler-planilha` | Lê uma planilha financeira (Excel/CSV) e normaliza o conteúdo para o schema de transação/produto do LKT System, sem alterar o arquivo original. | Sistema LKT |
| `lista-de-planos` | Gera a shot list (lista de planos) técnica a partir do storyboard, pronta pra equipe de câmera usar no set — ordem de captura, tipo de plano, lente sugerida, movimento de câmera. | Sistema LKT |
| `mapear-processo` | Mapeia um processo interno (o que a empresa faz, em que ordem, com qual regra) — início, fim, entradas, etapas, decisões, responsáveis por papel, ferramentas, arquivos gerados, ... | Sistema LKT |
| `mapear-rotinas` | Mapeia tarefas repetitivas que o usuário faz no dia a dia e gera skills personalizadas pra automatizá-las. | Sistema LKT |
| `mensagem-whatsapp` | Escreve mensagens de WhatsApp (atendimento, follow-up, campanha, confirmação) no tom certo pro canal — curtas, diretas, sem formalidade de email. | Sistema LKT |
| `nano-banana-2` | Generate images with Google Nano Banana 2 (Gemini-family flash-tier text-to-image) on RunComfy — bundled with the model's documented prompting patterns so the skill gets sharper... | Terceiros: agentspace-so/runcomfy-agent-skills · MIT |
| `notebook-lm` | Gera um dossiê Word (DOCX real, não Markdown renomeado) consolidando as informações de uma empresa ou de um projeto — memória, diagnóstico, proposta, projeções, roadmap, campanh... | Sistema LKT |
| `novo-projeto` | Cria um workspace novo (cliente, empresa ou projeto interno, conforme o modo de uso da instalação) ou um projeto dentro de um workspace já existente, com a estrutura padronizada... | Sistema LKT |
| `onboarding-de-cliente` | Estrutura o onboarding de um cliente novo fechado: o que precisa ser coletado, comunicado e configurado nos primeiros dias, com checklist e responsáveis. | Sistema LKT |
| `organizar-arquivos` | Analisa um arquivo anexado (documento, planilha, print, áudio, link) e indica exatamente em qual pasta ele deve ficar — geral (`arquivos/`) ou de um workspace/projeto específico. | Sistema LKT |
| `organizar-projeto` | Organiza a operação de um projeto/equipe: prioriza demandas, distribui responsáveis, planeja sprint/ciclo de trabalho, acompanha pendências e audita a operação em busca de gargalo. | Sistema LKT |
| `pagina-e-site` | Coordena a criação de uma página, landing page ou site (de um projeto de cliente ou interno) do contexto até o QA: objetivo, arquitetura de informação, conteúdo, estrutura de pá... | Sistema LKT |
| `pauta-de-conteudo` | Detalha uma entrada do calendário de conteúdo em pauta pronta pra produção: ângulo, mensagem-chave, referência, formato específico. | Sistema LKT |
| `performance-report` | Build a marketing performance report with key metrics, trend analysis, wins and misses, and prioritized optimization recommendations. | Terceiros: anthropics/knowledge-work-plugins (marketing) · Apache-2.0 |
| `pesquisa-mercado` | Pesquisa real (via WebSearch/WebFetch) sobre tamanho de mercado, tendências, comportamento do público e contexto do setor de um cliente/projeto — sempre com fonte registrada. | Sistema LKT |
| `planejar-banco-de-dados` | Modela o banco de dados de um sistema: entidades, relacionamentos, campos, índices — incluindo modo específico para Supabase (Postgres + auth + storage). | Sistema LKT |
| `plano-de-campanha` | Planeja uma campanha específica (lançamento, sazonal, promocional): objetivo, público, oferta, mensagem, canais, orçamento, cronograma, peças necessárias, responsáveis, métricas... | Sistema LKT |
| `plano-de-captacao` | Planeja a logística de gravação a partir do storyboard: cronograma de produção, lista de equipamentos, locação, equipe necessária, plano de áudio, continuidade e orçamento audio... | Sistema LKT |
| `plano-de-distribuicao` | Define onde, quando e como o vídeo finalizado é publicado (plataforma, formato, legenda, campanha associada), e consolida o relatório de desempenho depois de publicado. | Sistema LKT |
| `plano-estrategico` | Transforma diagnóstico, público, posicionamento e oferta já definidos num plano de ação priorizado: o que fazer, por quê, quem, custo, prazo, indicador, risco. | Sistema LKT |
| `plano-financeiro-completo` | Orquestra a análise financeira completa de um cliente/projeto: leitura de planilha, auditoria, fluxo de caixa, DRE, CMV, precificação, CAC/LTV, projeções e recomendações — encad... | Sistema LKT |
| `posicionamento` | Define posicionamento e mensagem central de um cliente/projeto: o que o diferencia de verdade, pra quem, e como isso se traduz em comunicação. | Sistema LKT |
| `precificacao` | Define preço de venda a partir do custo real (calcular-cmv), markup ou margem desejada, impostos e taxas — para qualquer segmento. | Sistema LKT |
| `precificacao-food-service` | Especialização de precificacao para food service: forma preço a partir da ficha técnica, considerando embalagem, taxas de cartão/delivery/ marketplace, comissão, descontos e per... | Sistema LKT |
| `preflight-ambiente` | Levanta o estado real do ambiente técnico antes de um projeto técnico ou ao entrar num repositório desconhecido: Git, branch, remote, framework, Node, extensões do editor, e qua... | Sistema LKT |
| `processar-arquivo` | Processa um arquivo novo recebido em arquivos/entrada/ (ou workspaces/clientes/<cliente>/arquivos/entrada/): preserva o original, calcula hash, extrai conteúdo útil, classifica,... | Sistema LKT |
| `producao-audiovisual-completa` | Orquestra a produção audiovisual completa: briefing, conceito, roteiro, storyboard, lista de planos, plano de captação, direção de cena, briefing de edição e distribuição — enca... | Sistema LKT |
| `produto-e-engenharia-de-cardapio` | Orquestra o ciclo completo de produto e cardápio de um negócio de food service: contexto, cardápio atual, fichas técnicas, rendimento/perdas, custo e preço, cruzamento com venda... | Sistema LKT |
| `projecao-financeira` | Projeta cenários financeiros futuros (conservador, provável, otimista) para decisões de investimento, novo produto, reajuste de preço, contratação, expansão — sempre com premiss... | Sistema LKT |
| `projecoes` | Gera cenários financeiros, comerciais, de marketing, operacionais, logísticos ou de projeto, sempre declarando dados usados, hipóteses, limitações e nível de confiança — nunca a... | Sistema LKT |
| `proposta-comercial` | Monta a proposta comercial para um lead/cliente específico: escopo, prazo, investimento e condições, a partir da oferta e do diagnóstico daquele lead — e aciona criar-documento ... | Sistema LKT |
| `proposta-completa` | Orquestra o caminho completo até uma proposta comercial: diagnóstico rápido, posicionamento, oferta, precificação e documento final — encadeando as skills de diagnóstico, produt... | Sistema LKT |
| `proposta-e-precificacao` | Gera escopo, entregáveis, responsabilidades por papel, dependências, custos externos, preço, condições e limites de um projeto, a partir do diagnóstico (quando existir). | Sistema LKT |
| `prospeccao` | Planeja abordagem de prospecção ativa (outbound): lista de alvos reais, canal de abordagem, mensagem inicial. | Sistema LKT |
| `publicar-tema` | Orquestra a criação completa de uma peça de conteúdo SEO + redes sociais a partir de um tema. | Sistema LKT |
| `qa` | Define e executa critério de qualidade antes de considerar uma entrega técnica pronta: testes funcionais, checklist de segurança básica, e plano mínimo de observabilidade (o que... | Sistema LKT |
| `qualificar-lead` | Avalia se um lead específico é qualificado, com base nos critérios definidos em estruturar-crm, e sugere a próxima ação. | Sistema LKT |
| `recomendar-nivel` | A partir de uma classificação de nível atual (classificar-nivel), recomenda o nível adequado e executável para o objetivo do projeto — nunca o nível mais alto por padrão. | Sistema LKT |
| `referencia-site` | Analisa referências visuais e de interação de sites (link, print, vídeo) para identificar exatamente o que o usuário quer aproveitar — scroll, hero, tipografia, paleta, grid, mo... | Sistema LKT |
| `registrar-prompt` | Gera o próximo ID sequencial de prompt (P0001, P0002...), cria o arquivo em prompts/arquivo/ a partir do template, atualiza prompts/REGISTRO.md e registra o resultado/handoff ao... | Sistema LKT |
| `relatorio-ads` | Gera relatório semanal de performance de anúncios pagos (Google Ads + Meta Ads). | Sistema LKT |
| `relatorio-de-marketing` | Consolida desempenho de marketing do período (conteúdo, SEO, ads, campanhas) num relatório executivo único, cruzando com objetivo da estratégia. | Sistema LKT |
| `relatorio-executivo` | Consolida financeiro, marketing, comercial e operação de um cliente/projeto num único relatório executivo de alto nível (visão de dono/board, não detalhe técnico de cada área). | Sistema LKT |
| `relatorio-financeiro` | Consolida DRE, fluxo de caixa, CMV, CAC/LTV e projeções num relatório executivo único, em linguagem simples, pro dono do negócio entender sem precisar ser contador. | Sistema LKT |
| `rendimento-e-desperdicio` | Calcula rendimento de insumo/preparo/porcionamento e mede perdas (limpeza, corte, cocção, validade, erro, sobra, porção acima do padrão), explicando o impacto financeiro e regis... | Sistema LKT |
| `research-synthesis` | Synthesize user research into themes, insights, and recommendations. | Terceiros: anthropics/knowledge-work-plugins (design) · Apache-2.0 |
| `responder-avaliacoes` | Escreve respostas curtas e humanas pras avaliações do Google Meu Negócio. | Sistema LKT |
| `reuniao-e-ata` | Prepara pauta de reunião e/ou documenta ata com decisões e próximos passos. | Sistema LKT |
| `reverse-engineer-anything` | Reverse engineer native, managed, Electron/JavaScript, packaged, firmware, and browser targets with REA. | Terceiros: morluto/rea · MIT |
| `review-animations` | Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering philosophy. | Terceiros: emilkowalski/skills · MIT |
| `revisar-codigo` | Revisa uma mudança de código específica: correção, simplificação, segurança, aderência ao padrão do projeto. | Sistema LKT |
| `revisar-nivel` | Revisa uma classificação de nível existente quando houver novo diagnóstico, mudança de projeto, marco concluído, dependência resolvida, mudança de orçamento/escopo, métrica rele... | Sistema LKT |
| `rotear-ambiente` | Decide ONDE continuar uma tarefa técnica — ambiente local/agente de código, chat do editor, Codex Web/GitHub, ou deploy — a partir do tipo de mudança, do escopo de arquivos e do... | Sistema LKT |
| `rotear-tarefa` | Decide qual módulo e qual skill (ou cadeia de skills) atende um pedido, consultando docs/roteamento.md e docs/catalogo-skills.md, quando não é óbvio de cara qual skill usar ou q... | Sistema LKT |
| `roteiro` | Escreve roteiro curto para vídeo de rede social (reels, stories, vídeo curto) a partir de uma pauta — gancho, desenvolvimento, CTA, indicação de corte/plano simples. | Sistema LKT |
| `roteiro-audiovisual` | Escreve roteiro completo de produção audiovisual: cena, diálogo, ação, duração e transição, a partir do briefing. | Sistema LKT |
| `salvar` | Salva o trabalho do LKT PLUS no GitHub (commit + push). | LKT Plus |
| `salvar-local` | Fecha uma sessão de trabalho: atualiza memória, decisões e pendências, atualiza índices e catálogo, registra o que foi criado/modificado, gera um resumo da sessão, roda o valida... | Sistema LKT |
| `script-comercial` | Escreve script/roteiro de abordagem comercial (ligação, reunião, mensagem) e trata objeções comuns, incluindo follow-up quando não há resposta. | Sistema LKT |
| `seo` | Fluxo completo de SEO, GEO e Google Ads em 8 passos: pesquisa de demanda, análise de concorrência, Google Meu Negócio, otimização on-page, estratégia de conteúdo, Google Ads, ch... | Sistema LKT |
| `seo-audit` | Run a comprehensive SEO audit — keyword research, on-page analysis, content gaps, technical checks, and competitor comparison. | Terceiros: anthropics/knowledge-work-plugins (marketing) · Apache-2.0 |
| `skill-creator` | Create new skills, modify and improve existing skills, and measure skill performance. | Terceiros: anthropics/skills · Apache-2.0 |
| `storyboard` | Detalha cada cena do roteiro em plano visual: cena, plano, enquadramento, ação, diálogo, áudio, duração, transição, referência visual e necessidade de produção. | Sistema LKT |
| `texto-natural-pt-br` | Acabamento final de qualquer texto voltado a público, cliente ou usuário final — legendas, roteiros, sites, landing pages, propostas, relatórios, e-mails, apresentações, anúncio... | Sistema LKT |
| `theme-factory` | Toolkit for styling artifacts with a theme. | Terceiros: anthropics/skills · Apache-2.0 |
| `user-research` | Plan, conduct, and synthesize user research. | Terceiros: anthropics/knowledge-work-plugins (design) · Apache-2.0 |
| `ux-copy` | Write or review UX copy — microcopy, error messages, empty states, CTAs. | Terceiros: anthropics/knowledge-work-plugins (design) · Apache-2.0 |
| `validar-sistema` | Roda a validação estrutural do sistema (tools/validar.js) e traduz o resultado em linguagem de conversa: o que está certo, o que é problema real, o que é aviso, e o que fazer a ... | Sistema LKT |
| `web-artifacts-builder` | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). | Terceiros: anthropics/skills · Apache-2.0 |

## Skills obrigatórias em cadeia

Para páginas, sites, landing pages, dashboards, portais ou interfaces:

1. `pagina-e-site`
2. `design-front-end`
3. `texto-natural-pt-br`

Para qualquer texto voltado ao público final, aplicar `texto-natural-pt-br`
ao final do fluxo, independente da skill principal usada.
