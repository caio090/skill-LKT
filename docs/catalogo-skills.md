# Catálogo de skills

> Arquivo GERADO por `python3 tools/registro.py catalogo` a partir de
> [`registry/skills.json`](../registry/skills.json). Não editar à mão: altere
> [`registry/fontes.json`](../registry/fontes.json) ou a skill e gere de novo.

Em `.claude/skills/`: **168** skills — 129 do núcleo LKT System, 2 do LKT Plus (aposentadas, mantidas só como histórico) e 37 de terceiros.
Em `terceiros/codex/`: **80** skills de referência para o Codex (não instaladas pelo instalador).

Estados: **aprovada** (pode ser instalada) · **pendente** (falta verificar origem/licença) ·
**bloqueada** (licença impede redistribuição) · **referência** (instalar pela fonte oficial) ·
**aposentada** (substituída; não instalar).

Origem e licença detalhadas: [`skills-terceiros.md`](skills-terceiros.md) e [`licencas.md`](licencas.md).

## audiovisual

| Skill | Descrição | Origem | Estado |
|---|---|---|---|
| `analisar-video` | Analisa um vídeo já existente (próprio ou de referência/concorrente): estrutura, ritmo, gancho, retenção estimada, pontos fortes e fracos. | LKT System | aprovada |
| `briefing-audiovisual` | Coleta o briefing de uma produção audiovisual: objetivo, mensagem, público, formato, duração, referências, orçamento e prazo. | LKT System | aprovada |
| `briefing-de-edicao` | Prepara o briefing para o editor: seleção de melhores tomadas, ritmo, trilha, cor, legendas, versões por formato/plataforma e critério de aprovação final. | LKT System | aprovada |
| `direcao-de-cena` | Orienta a execução no dia de gravação: o que checar antes de cada cena, direção de talento/depoimento, continuidade em tempo real e critério de "cena aprovada, pode seguir". | LKT System | aprovada |
| `lista-de-planos` | Gera a shot list (lista de planos) técnica a partir do storyboard, pronta pra equipe de câmera usar no set — ordem de captura, tipo de plano, lente sugerida, movimento de câmera. | LKT System | aprovada |
| `plano-de-captacao` | Planeja a logística de gravação a partir do storyboard: cronograma de produção, lista de equipamentos, locação, equipe necessária, plano de áudio, continuidade e orçamento audio... | LKT System | aprovada |
| `plano-de-distribuicao` | Define onde, quando e como o vídeo finalizado é publicado (plataforma, formato, legenda, campanha associada), e consolida o relatório de desempenho depois de publicado. | LKT System | aprovada |
| `producao-audiovisual-completa` | Orquestra a produção audiovisual completa: briefing, conceito, roteiro, storyboard, lista de planos, plano de captação, direção de cena, briefing de edição e distribuição — enca... | LKT System | aprovada |
| `roteiro` | Escreve roteiro curto para vídeo de rede social (reels, stories, vídeo curto) a partir de uma pauta — gancho, desenvolvimento, CTA, indicação de corte/plano simples. | LKT System | aprovada |
| `roteiro-audiovisual` | Escreve roteiro completo de produção audiovisual: cena, diálogo, ação, duração e transição, a partir do briefing. | LKT System | aprovada |
| `storyboard` | Detalha cada cena do roteiro em plano visual: cena, plano, enquadramento, ação, diálogo, áudio, duração, transição, referência visual e necessidade de produção. | LKT System | aprovada |

## automacao

| Skill | Descrição | Origem | Estado |
|---|---|---|---|
| `automacao-fluxos` | Planeja e documenta automações de fluxo (n8n ou equivalente) e de WhatsApp Business: gatilho, passos, integrações envolvidas, tratamento de erro. | LKT System | aprovada |
| `automatizar-fluxo` | Transforma uma etapa de processo/funil/pipeline em regra de automação, sempre distinguindo sugestão, execução assistida, execução com confirmação e execução automática — nunca c... | LKT System | aprovada |
| `n8n-workflow-check` | Build, repair or review importable n8n workflow JSON, with a reproducible test for valid input, invalid input and duplicate events. | smrht/samautomation-workflows · MIT | aprovada |

## comercial-crm

| Skill | Descrição | Origem | Estado |
|---|---|---|---|
| `analisar-conversao` | Calcula e explica volume, taxa, perda, tendência e gargalo de um funil ou pipeline, com hipótese, recomendação e nível de confiança — sinalizando quando faltar dado suficiente. | LKT System | aprovada |
| `atendimento` | Responde dúvidas/solicitações de clientes já ativos, e cobre retenção (identificar risco de cancelamento e agir) e análise de churn (por que clientes saem). | LKT System | aprovada |
| `configurar-pipeline` | Configura um pipeline — visualização de onde cada item (oportunidade, candidato, chamado) está agora. | LKT System | aprovada |
| `criar-produto-e-oferta` | Estrutura ou refina um produto/serviço e sua oferta comercial (o que inclui, preço, condição, garantia) com base no diagnóstico, público e posicionamento do cliente/projeto. | LKT System | aprovada |
| `desenhar-funil` | Desenha um funil de conversão — quantidade e taxa de passagem de uma entidade (visitante, lead, candidato) entre etapas até um resultado final. | LKT System | aprovada |
| `email-profissional` | Rascunha um email profissional a partir de um contexto livre. | LKT System | aprovada |
| `estruturar-crm` | Estrutura o CRM de um cliente/projeto: etapas do funil, campos por lead/cliente, critérios de qualificação e regras de movimentação entre etapas — não é um CRM web, é a estrutur... | LKT System | aprovada |
| `funil-de-vendas` | Acompanha e analisa o funil de vendas já estruturado: quantos leads em cada etapa, taxa de conversão entre etapas, tempo médio, gargalos, e documenta o playbook comercial (o que... | LKT System | aprovada |
| `gerar-proposta-a-partir-do-nivel` | Traduz a inteligência interna dos níveis (escopo, plano de avanço, recomendação) para a camada comercial — só o que o cliente precisa entender para decidir. | LKT System | aprovada |
| `mensagem-whatsapp` | Escreve mensagens de WhatsApp (atendimento, follow-up, campanha, confirmação) no tom certo pro canal — curtas, diretas, sem formalidade de email. | LKT System | aprovada |
| `onboarding-de-cliente` | Estrutura o onboarding de um cliente novo fechado: o que precisa ser coletado, comunicado e configurado nos primeiros dias, com checklist e responsáveis. | LKT System | aprovada |
| `proposta-comercial` | Monta a proposta comercial para um lead/cliente específico: escopo, prazo, investimento e condições, a partir da oferta e do diagnóstico daquele lead — e aciona criar-documento... | LKT System | aprovada |
| `proposta-completa` | Orquestra o caminho completo até uma proposta comercial: diagnóstico rápido, posicionamento, oferta, precificação e documento final — encadeando as skills de diagnóstico, produt... | LKT System | aprovada |
| `proposta-e-precificacao` | Gera escopo, entregáveis, responsabilidades por papel, dependências, custos externos, preço, condições e limites de um projeto, a partir do diagnóstico (quando existir). | LKT System | aprovada |
| `prospeccao` | Planeja abordagem de prospecção ativa (outbound): lista de alvos reais, canal de abordagem, mensagem inicial. | LKT System | aprovada |
| `qualificar-lead` | Avalia se um lead específico é qualificado, com base nos critérios definidos em estruturar-crm, e sugere a próxima ação. | LKT System | aprovada |
| `script-comercial` | Escreve script/roteiro de abordagem comercial (ligação, reunião, mensagem) e trata objeções comuns, incluindo follow-up quando não há resposta. | LKT System | aprovada |

## diagnostico-estrategia

| Skill | Descrição | Origem | Estado |
|---|---|---|---|
| `analisar-concorrentes` | Mapeia concorrentes reais de um cliente/projeto (via WebSearch/WebFetch): quem são, o que oferecem, pontos fortes/fracos, gaps e oportunidades. | LKT System | aprovada |
| `analisar-publico` | Aprofunda quem é o público real de um cliente/projeto: perfil, dor, processo de decisão de compra, objeções, onde ele está. | LKT System | aprovada |
| `auditoria-completa` | Orquestra uma auditoria completa de um cliente/projeto: financeiro (planilhas), técnico (repositório/sistema) e operacional, consolidando achados num relatório único. | LKT System | aprovada |
| `briefing-completo` | Coleta e organiza o briefing completo de um projeto ou entrega específica (o que precisa, pra quem, prazo, restrições, referências). | LKT System | aprovada |
| `classificar-nivel` | Classifica um workspace/projeto numa dimensão de maturidade (ex.: maturidade digital, financeira, comercial) com base em evidência real — nunca por impressão vaga. | LKT System | aprovada |
| `competitive-brief` | Research competitors and generate a positioning and messaging comparison with content gaps, opportunities, and threats. | anthropics/knowledge-work-plugins · Apache-2.0 | aprovada |
| `diagnostico-completo` | Orquestra o diagnóstico completo de um cliente/projeto novo, do contexto ao plano de ação, encadeando as skills menores do módulo de diagnóstico e estratégia. | LKT System | aprovada |
| `diagnostico-empresarial` | Analisa os pilares aplicáveis de um workspace ou projeto (negócio, oferta, público, marca, marketing, presença digital, conteúdo, comercial, atendimento, financeiro, operação, l... | LKT System | aprovada |
| `diagnostico-negocio` | Diagnostica a situação atual de um negócio/cliente: modelo, operação, finanças macro, marketing, comercial, o que funciona e o que trava. | LKT System | aprovada |
| `dna-do-negocio` | Registra o DNA do negócio — história, propósito, posicionamento, público, personalidade, produtos principais, diferenciais, operação, canais, limites, concorrentes e objetivos. | LKT System | aprovada |
| `gerar-escopo-por-nivel` | Monta o escopo interno completo de um projeto a partir de um nível recomendado e seu perfil de entrega, separando obrigatório, recomendado, opcional, futuro e não incluso. | LKT System | aprovada |
| `gerar-plano-de-avanco` | Transforma a lacuna entre nível atual e recomendado (recomendar-nivel) em ações concretas — entregas, tarefas, responsáveis por papel, dependências, prazo, custo, validação, ris... | LKT System | aprovada |
| `pesquisa-mercado` | Pesquisa real (via WebSearch/WebFetch) sobre tamanho de mercado, tendências, comportamento do público e contexto do setor de um cliente/projeto — sempre com fonte registrada. | LKT System | aprovada |
| `plano-estrategico` | Transforma diagnóstico, público, posicionamento e oferta já definidos num plano de ação priorizado: o que fazer, por quê, quem, custo, prazo, indicador, risco. | LKT System | aprovada |
| `posicionamento` | Define posicionamento e mensagem central de um cliente/projeto: o que o diferencia de verdade, pra quem, e como isso se traduz em comunicação. | LKT System | aprovada |
| `recomendar-nivel` | A partir de uma classificação de nível atual (classificar-nivel), recomenda o nível adequado e executável para o objetivo do projeto — nunca o nível mais alto por padrão. | LKT System | aprovada |
| `research-synthesis` | Synthesize user research into themes, insights, and recommendations. | anthropics/knowledge-work-plugins · Apache-2.0 | aprovada |
| `revisar-nivel` | Revisa uma classificação de nível existente quando houver novo diagnóstico, mudança de projeto, marco concluído, dependência resolvida, mudança de orçamento/escopo, métrica rele... | LKT System | aprovada |
| `user-research` | Plan, conduct, and synthesize user research. | anthropics/knowledge-work-plugins · Apache-2.0 | aprovada |

## documentos-processos

| Skill | Descrição | Origem | Estado |
|---|---|---|---|
| `analisar-dados` | Analisa um arquivo de dados (CSV, Excel, TXT, JSON) e gera um resumo executivo com os principais insights, tendências e recomendações. | LKT System | aprovada |
| `criar-apresentacao` | Cria uma apresentação (slides) para reunião, proposta, palestra ou relatório de um projeto, coerente com a marca. | LKT System | aprovada |
| `criar-documento` | Cria ou edita um documento de texto (Word/Markdown/rich text) para um projeto — proposta, relatório, briefing, contrato, manual. | LKT System | aprovada |
| `criar-pdf` | Converte um documento, relatório ou apresentação já finalizado em PDF para entrega, preservando o arquivo-fonte original. | LKT System | aprovada |
| `criar-planilha` | Cria ou edita uma planilha (custos, fluxo de caixa, orçamento, cronograma, controle) para um projeto. | LKT System | aprovada |
| `criar-sop` | Documenta um processo operacional recorrente em SOP (procedimento padrão): passo a passo, responsável, ferramenta, tempo estimado, critério de qualidade. | LKT System | aprovada |
| `mapear-processo` | Mapeia um processo interno (o que a empresa faz, em que ordem, com qual regra) — início, fim, entradas, etapas, decisões, responsáveis por papel, ferramentas, arquivos gerados,... | LKT System | aprovada |
| `organizar-projeto` | Organiza a operação de um projeto/equipe: prioriza demandas, distribui responsáveis, planeja sprint/ciclo de trabalho, acompanha pendências e audita a operação em busca de gargalo. | LKT System | aprovada |
| `reuniao-e-ata` | Prepara pauta de reunião e/ou documenta ata com decisões e próximos passos. | LKT System | aprovada |

## financeiro

| Skill | Descrição | Origem | Estado |
|---|---|---|---|
| `analyzing-financial-statements` | This skill calculates key financial ratios and metrics from financial statement data for investment analysis | anthropics/claude-cookbooks · MIT | aprovada |
| `auditar-planilha` | Audita uma planilha financeira já lida (ler-planilha): mapeia fórmulas com erro, referências quebradas, abas ocultas, inconsistências de status/categoria, e explica o que descob... | LKT System | aprovada |
| `cac-e-ltv` | Calcula e explica CAC, LTV, relação LTV/CAC, payback, ROI e ROAS — as métricas de retorno sobre investimento em aquisição/retenção de cliente. | LKT System | aprovada |
| `calcular-cmv` | Calcula CMV (custo de mercadoria/serviço vendido), custo interno, margem de contribuição, estoque e desperdício de um negócio, a partir de ficha técnica ou dado de compra/consumo. | LKT System | aprovada |
| `cmv-real-e-teorico` | Especialização food service de calcular-cmv: compara CMV real (a partir de estoque) com CMV teórico (a partir de vendas × ficha técnica), localiza a lacuna e investiga causas pr... | LKT System | aprovada |
| `creating-financial-models` | This skill provides an advanced financial modeling suite with DCF analysis, sensitivity testing, Monte Carlo simulations, and scenario planning for investment decisions | anthropics/claude-cookbooks · MIT | aprovada |
| `dre` | Monta e explica o DRE (Demonstrativo de Resultado) de um período: receita, deduções, CMV/custo de serviço, margem bruta, despesas, resultado operacional e líquido — e compara pr... | LKT System | aprovada |
| `fluxo-de-caixa` | Organiza entradas e saídas por período, calcula saldo projetado e de capital de giro, e explica em linguagem simples o que o fluxo de caixa significa pra decisão do dono. | LKT System | aprovada |
| `gestao-de-negocio` | Consolida vendas, custos, despesas, caixa, produtos, clientes, campanhas, estoque e decisões de um negócio (com especialização em food service, adaptável a outros segmentos) e i... | LKT System | aprovada |
| `ler-planilha` | Lê uma planilha financeira (Excel/CSV) e normaliza o conteúdo para o schema de transação/produto do LKT System, sem alterar o arquivo original. | LKT System | aprovada |
| `plano-financeiro-completo` | Orquestra a análise financeira completa de um cliente/projeto: leitura de planilha, auditoria, fluxo de caixa, DRE, CMV, precificação, CAC/LTV, projeções e recomendações — encad... | LKT System | aprovada |
| `precificacao` | Define preço de venda a partir do custo real (calcular-cmv), markup ou margem desejada, impostos e taxas — para qualquer segmento. | LKT System | aprovada |
| `precificacao-food-service` | Especialização de precificacao para food service: forma preço a partir da ficha técnica, considerando embalagem, taxas de cartão/delivery/ marketplace, comissão, descontos e per... | LKT System | aprovada |
| `projecao-financeira` | Projeta cenários financeiros futuros (conservador, provável, otimista) para decisões de investimento, novo produto, reajuste de preço, contratação, expansão — sempre com premiss... | LKT System | aprovada |
| `projecoes` | Gera cenários financeiros, comerciais, de marketing, operacionais, logísticos ou de projeto, sempre declarando dados usados, hipóteses, limitações e nível de confiança — nunca a... | LKT System | aprovada |
| `relatorio-executivo` | Consolida financeiro, marketing, comercial e operação de um cliente/projeto num único relatório executivo de alto nível (visão de dono/board, não detalhe técnico de cada área). | LKT System | aprovada |
| `relatorio-financeiro` | Consolida DRE, fluxo de caixa, CMV, CAC/LTV e projeções num relatório executivo único, em linguagem simples, pro dono do negócio entender sem precisar ser contador. | LKT System | aprovada |

## food-service

| Skill | Descrição | Origem | Estado |
|---|---|---|---|
| `analisar-promocao-cupom` | Analisa se uma promoção/cupom vale a pena: quem paga o desconto (loja, plataforma ou compartilhado), margem antes e depois, volume necessário pra compensar, novos clientes vs. | LKT System | aprovada |
| `aumento-de-ticket` | Analisa ticket médio e mapeia oportunidades reais de aumento (combo, adicional, tamanho, sobremesa, bebida, oferta de volume, sugestão de atendimento, posição no cardápio, pós-c... | LKT System | aprovada |
| `cardapio-digital` | Audita o cardápio digital (categorias, produtos, adicionais, combos, fotos, descrições, disponibilidade, horários, taxas, retirada, entrega, pagamento, cupons) e cruza com produ... | LKT System | aprovada |
| `engenharia-de-cardapio` | Analisa popularidade, margem de contribuição, faturamento, quantidade vendida e posição no cardápio (físico e digital) de cada produto, separando o que vende muito, dá margem, é... | LKT System | aprovada |
| `estoque-food-service` | Controla estoque central e de cozinha separadamente: compras, entradas, transferências, consumo, perdas, validade, cortesia, refeição de equipe, correções, devoluções e ajustes. | LKT System | aprovada |
| `ficha-tecnica` | Cria, revisa e atualiza a ficha técnica de um produto de food service: ingredientes, quantidades, unidades, peso bruto/líquido/final, rendimento, porção, embalagem, mão de obra... | LKT System | aprovada |
| `produto-e-engenharia-de-cardapio` | Orquestra o ciclo completo de produto e cardápio de um negócio de food service: contexto, cardápio atual, fichas técnicas, rendimento/perdas, custo e preço, cruzamento com venda... | LKT System | aprovada |
| `rendimento-e-desperdicio` | Calcula rendimento de insumo/preparo/porcionamento e mede perdas (limpeza, corte, cocção, validade, erro, sobra, porção acima do padrão), explicando o impacto financeiro e regis... | LKT System | aprovada |

## imagem-motion

| Skill | Descrição | Origem | Estado |
|---|---|---|---|
| `animation-vocabulary` | Reverse-lookup glossary that turns a vague description of a web animation or motion effect into its exact term ("the bouncy thing when a popover opens" → Pop in; "the iOS rubber... | emilkowalski/skills · MIT | aprovada |
| `apple-design` | Apple's approach to interface design and fluid, physical motion, translated for the web. | emilkowalski/skills · MIT | aprovada |
| `canvas-design` | Create beautiful visual art in .png and .pdf documents using design philosophy. | anthropics/skills · Apache-2.0 | aprovada |
| `image-edit` | Edit images on RunComfy — this skill is a smart router that matches the user's intent to the right edit model in the RunComfy catalog. | prime-skills/runcomfy-agent-skills · MIT | aprovada |
| `nano-banana-2` | Generate images with Google Nano Banana 2 (Gemini-family flash-tier text-to-image) on RunComfy — bundled with the model's documented prompting patterns so the skill gets sharper... | prime-skills/runcomfy-agent-skills · MIT | aprovada |
| `review-animations` | Reviews animation and motion code against a high craft bar derived from Emil Kowalski's design engineering philosophy. | emilkowalski/skills · MIT | aprovada |

## marketing-conteudo

| Skill | Descrição | Origem | Estado |
|---|---|---|---|
| `anuncio-google` | Cria estrutura completa de campanha do Google Ads a partir de um briefing ou da pesquisa SEO. | LKT System | aprovada |
| `anuncio-meta` | Monta estrutura de campanha do Meta Ads (Instagram/Facebook) a partir de briefing/estratégia: campanha, conjuntos de anúncio, públicos, criativos e copy — pronta pra configurar... | LKT System | aprovada |
| `applying-brand-guidelines` | This skill applies consistent corporate branding and styling to all generated documents including colors, fonts, layouts, and messaging | anthropics/claude-cookbooks · MIT | aprovada |
| `aprovar-post` | Prepara um conteúdo já aprovado (blog + carrossel + legendas, criado por publicar-tema ou carrossel) para publicação, montando um pacote local pronto pra postar. | LKT System | aprovada |
| `brand-review` | Review content against your brand voice, style guide, and messaging pillars, flagging deviations by severity with specific before/after fixes. | anthropics/knowledge-work-plugins · Apache-2.0 | aprovada |
| `calendario-de-conteudo` | Monta o calendário editorial recorrente (não de campanha específica): temas, formato, canal e frequência, coerente com a estratégia de marketing. | LKT System | aprovada |
| `campaign-plan` | Generate a full campaign brief with objectives, audience, messaging, channel strategy, content calendar, and success metrics. | anthropics/knowledge-work-plugins · Apache-2.0 | aprovada |
| `campanha-completa` | Orquestra uma campanha de marketing do zero: contexto, objetivo, público, oferta, canais, conceito, peças, mídia, calendário e relatório — encadeando as skills de estratégia, co... | LKT System | aprovada |
| `carrossel` | Cria carrosséis e posts visuais pra Instagram, TikTok, LinkedIn com a identidade visual da marca. | LKT System | aprovada |
| `content-creation` | Draft marketing content across channels — blog posts, social media, email newsletters, landing pages, press releases, and case studies. | anthropics/knowledge-work-plugins · Apache-2.0 | aprovada |
| `criar-campanha` | Gera uma campanha completa — briefing, objetivo, público, oferta, canais, cronograma, ativos, página, conteúdos, orçamento, funil associado, eventos de conversão, metas, plano d... | LKT System | aprovada |
| `draft-content` | Draft blog posts, social media, email newsletters, landing pages, press releases, and case studies with channel-specific formatting and SEO recommendations. | anthropics/knowledge-work-plugins · Apache-2.0 | aprovada |
| `email-sequence` | Design and draft multi-email sequences with full copy, timing, branching logic, exit conditions, and performance benchmarks. | anthropics/knowledge-work-plugins · Apache-2.0 | aprovada |
| `estrategia-de-marketing` | Define a estratégia de marketing de um cliente/projeto: objetivos, canais prioritários, mensagem (a partir do posicionamento), verba e cronograma macro — antes de qualquer peça... | LKT System | aprovada |
| `pauta-de-conteudo` | Detalha uma entrada do calendário de conteúdo em pauta pronta pra produção: ângulo, mensagem-chave, referência, formato específico. | LKT System | aprovada |
| `performance-report` | Build a marketing performance report with key metrics, trend analysis, wins and misses, and prioritized optimization recommendations. | anthropics/knowledge-work-plugins · Apache-2.0 | aprovada |
| `plano-de-campanha` | Planeja uma campanha específica (lançamento, sazonal, promocional): objetivo, público, oferta, mensagem, canais, orçamento, cronograma, peças necessárias, responsáveis, métricas... | LKT System | aprovada |
| `publicar-tema` | Orquestra a criação completa de uma peça de conteúdo SEO + redes sociais a partir de um tema. | LKT System | aprovada |
| `relatorio-ads` | Gera relatório semanal de performance de anúncios pagos (Google Ads + Meta Ads). | LKT System | aprovada |
| `relatorio-de-marketing` | Consolida desempenho de marketing do período (conteúdo, SEO, ads, campanhas) num relatório executivo único, cruzando com objetivo da estratégia. | LKT System | aprovada |
| `responder-avaliacoes` | Escreve respostas curtas e humanas pras avaliações do Google Meu Negócio. | LKT System | aprovada |
| `seo` | Fluxo completo de SEO, GEO e Google Ads em 8 passos: pesquisa de demanda, análise de concorrência, Google Meu Negócio, otimização on-page, estratégia de conteúdo, Google Ads, ch... | LKT System | aprovada |
| `seo-audit` | Run a comprehensive SEO audit — keyword research, on-page analysis, content gaps, technical checks, and competitor comparison. | anthropics/knowledge-work-plugins · Apache-2.0 | aprovada |

## nucleo-operacao

| Skill | Descrição | Origem | Estado |
|---|---|---|---|
| `abrir` | Abre uma sessão de trabalho carregando a memória do negócio (empresa, preferências, estratégia, marca) e devolve um resumo curto pro usuário. | LKT System | aprovada |
| `atualizar` | Varre o projeto e atualiza os arquivos de contexto (`_memoria/empresa.md`, `preferencias.md`, `estrategia.md`, `CLAUDE.md`, `identidade/design-guide.md`) que ficaram desatualiza... | LKT Plus | aposentada → `atualizar-memoria` |
| `atualizar-memoria` | Varre o projeto e compara com os 13 arquivos de _memoria/ (empresa, preferências, estratégia, marca, produtos-e-servicos, processos, ferramentas, equipe, métricas, decisões, apr... | LKT System | aprovada |
| `continuar-projeto` | Lê a memória, as decisões, as pendências e os arquivos recentes de um workspace ou projeto, e informa o próximo passo — sem repetir perguntas já respondidas. | LKT System | aprovada |
| `cowork-plugin-customizer` | Customize a Claude Code plugin for a specific organization's tools and workflows. | anthropics/knowledge-work-plugins · Apache-2.0 | aprovada |
| `create-cowork-plugin` | Guide users through creating a new plugin from scratch in a cowork session. | anthropics/knowledge-work-plugins · Apache-2.0 | aprovada |
| `fechar-sessao` | Encerra o foco no cliente/projeto atual de forma segura: atualiza .lkt-system/estado/contexto-ativo.json (limpa cliente/projeto ativo ou troca pra outro), sem apagar histórico. | LKT System | aprovada |
| `find-skills` | Helps users discover and install agent skills when they ask questions like "how do I do X", "find a skill for X", "is there a skill that can...", or express interest in extendin... | vercel-labs/skills · MIT | aprovada |
| `instalar` | Instala o Sistema LKT no negócio ou projeto onde a pasta foi copiada. | LKT System | aprovada |
| `mapear-rotinas` | Mapeia tarefas repetitivas que o usuário faz no dia a dia e gera skills personalizadas pra automatizá-las. | LKT System | aprovada |
| `notebook-lm` | Gera um dossiê Word (DOCX real, não Markdown renomeado) consolidando as informações de uma empresa ou de um projeto — memória, diagnóstico, proposta, projeções, roadmap, campanh... | LKT System | aprovada |
| `novo-projeto` | Cria um workspace novo (cliente, empresa ou projeto interno, conforme o modo de uso da instalação) ou um projeto dentro de um workspace já existente, com a estrutura padronizada... | LKT System | aprovada |
| `organizar-arquivos` | Analisa um arquivo anexado (documento, planilha, print, áudio, link) e indica exatamente em qual pasta ele deve ficar — geral (`arquivos/`) ou de um workspace/projeto específico. | LKT System | aprovada |
| `preflight-ambiente` | Levanta o estado real do ambiente técnico antes de um projeto técnico ou ao entrar num repositório desconhecido: Git, branch, remote, framework, Node, extensões do editor, e qua... | LKT System | aprovada |
| `processar-arquivo` | Processa um arquivo novo recebido em arquivos/entrada/ (ou workspaces/clientes/<cliente>/arquivos/entrada/): preserva o original, calcula hash, extrai conteúdo útil, classifica,... | LKT System | aprovada |
| `registrar-prompt` | Gera o próximo ID sequencial de prompt (P0001, P0002...), cria o arquivo em prompts/arquivo/ a partir do template, atualiza prompts/REGISTRO.md e registra o resultado/handoff ao... | LKT System | aprovada |
| `rotear-ambiente` | Decide ONDE continuar uma tarefa técnica — ambiente local/agente de código, chat do editor, Codex Web/GitHub, ou deploy — a partir do tipo de mudança, do escopo de arquivos e do... | LKT System | aprovada |
| `rotear-tarefa` | Decide qual módulo e qual skill (ou cadeia de skills) atende um pedido, consultando docs/roteamento.md e docs/catalogo-skills.md, quando não é óbvio de cara qual skill usar ou q... | LKT System | aprovada |
| `salvar` | Salva o trabalho do LKT PLUS no GitHub (commit + push). | LKT Plus | aposentada → `salvar-local` |
| `salvar-local` | Fecha uma sessão de trabalho: atualiza memória, decisões e pendências, atualiza índices e catálogo, registra o que foi criado/modificado, gera um resumo da sessão, roda o valida... | LKT System | aprovada |
| `skill-creator` | Create new skills, modify and improve existing skills, and measure skill performance. | anthropics/skills · Apache-2.0 | aprovada |
| `validar-sistema` | Roda a validação estrutural do sistema (tools/validar.js) e traduz o resultado em linguagem de conversa: o que está certo, o que é problema real, o que é aviso, e o que fazer a... | LKT System | aprovada |

## qualidade-testes

| Skill | Descrição | Origem | Estado |
|---|---|---|---|
| `qa` | Define e executa critério de qualidade antes de considerar uma entrega técnica pronta: testes funcionais, checklist de segurança básica, e plano mínimo de observabilidade (o que... | LKT System | aprovada |
| `qa-e2e-playwright` | Cria e executa testes ponta a ponta com Playwright em ambiente isolado: navegação, formulários, filtros, estados vazios e de erro, mobile e desktop, acessibilidade básica por te... | LKT System | aprovada |

## tecnologia

| Skill | Descrição | Origem | Estado |
|---|---|---|---|
| `app-e-sistema` | Coordena escopo, usuários, fluxos, permissões, dados, integrações, interface, backlog, arquitetura, QA e documentação de um aplicativo ou sistema de um projeto de cliente ou int... | LKT System | aprovada |
| `arquitetura-de-software` | Define a arquitetura técnica de um sistema/app: componentes, stack, integrações, estratégia de deploy, versionamento e plano de migração quando aplicável. | LKT System | aprovada |
| `auditar-repositorio` | Audita um repositório de código: estrutura, dependências desatualizadas/vulneráveis, segredos expostos, cobertura de teste, documentação e convenções — sem corrigir nada sozinha. | LKT System | aprovada |
| `construir-produto-digital` | Orquestra a construção de um produto digital do zero: escopo, especificação, arquitetura, banco de dados, integrações, interface, QA e documentação — encadeando as skills do mód... | LKT System | aprovada |
| `depurar-erro` | Investiga e corrige um erro/bug específico: reproduz, localiza causa raiz, corrige, e confirma que não quebrou outra coisa. | LKT System | aprovada |
| `diagnostico-tecnico` | Diagnostica a situação técnica de um sistema/projeto existente: stack, débito técnico, riscos de segurança básicos, performance percebida e o que trava a evolução. | LKT System | aprovada |
| `documentar-sistema` | Documenta um sistema/projeto técnico: visão geral, arquitetura, como rodar localmente, como fazer deploy, decisões técnicas importantes. | LKT System | aprovada |
| `especificacao-de-produto` | Escreve especificação de produto digital: problema, solução, backlog priorizado e roadmap por fase. | LKT System | aprovada |
| `integrar-api` | Planeja e documenta a integração com uma API externa (pagamento, WhatsApp, CRM, cardápio digital, etc.): autenticação, endpoints usados, tratamento de erro, e adaptador de dados... | LKT System | aprovada |
| `planejar-banco-de-dados` | Modela o banco de dados de um sistema: entidades, relacionamentos, campos, índices — incluindo modo específico para Supabase (Postgres + auth + storage). | LKT System | aprovada |
| `reverse-engineer-anything` | Reverse engineer native, managed, Electron/JavaScript, packaged, firmware, and browser targets with REA. | morluto/rea · MIT | aprovada |
| `revisar-codigo` | Revisa uma mudança de código específica: correção, simplificação, segurança, aderência ao padrão do projeto. | LKT System | aprovada |
| `supabase-postgres-best-practices` | Postgres best practices maintained by Supabase, for Postgres running anywhere. | supabase/agent-skills · MIT | aprovada |

## texto

| Skill | Descrição | Origem | Estado |
|---|---|---|---|
| `humanizer` | Rewrite AI-sounding text so it reads like the writer without changing what it says. | blader/humanizer · MIT | aprovada |
| `humanizer-pt-br` | Remove traços de escrita gerada por IA de textos em português brasileiro, tornando-os mais naturais, humanos e com personalidade real. | mackswendhell/humanizer-pt-br · MIT | aprovada |
| `texto-natural-pt-br` | Acabamento final de qualquer texto voltado a público, cliente ou usuário final — legendas, roteiros, sites, landing pages, propostas, relatórios, e-mails, apresentações, anúncio... | LKT System | aprovada |

## web-design

| Skill | Descrição | Origem | Estado |
|---|---|---|---|
| `accessibility-review` | Run a WCAG 2.1 AA accessibility audit on a design or page. | anthropics/knowledge-work-plugins · Apache-2.0 | aprovada |
| `anti-chat` | Quality gate transversal contra aparência e linguagem genérica de IA: design de template, gradiente/glassmorphism gratuito, cards demais, tipografia preguiçosa, texto motivacion... | LKT System | aprovada |
| `design-critique` | Get structured design feedback on usability, hierarchy, and consistency. | anthropics/knowledge-work-plugins · Apache-2.0 | aprovada |
| `design-front-end` | Orienta direção visual, tipografia, paleta, hierarquia, grid, layout, responsividade, acessibilidade, componentes, estados vazios/erro e experiência mobile para qualquer interfa... | LKT System | aprovada |
| `design-handoff` | Generate developer handoff specs from a design. | anthropics/knowledge-work-plugins · Apache-2.0 | aprovada |
| `design-system` | Audit, document, or extend your design system. | anthropics/knowledge-work-plugins · Apache-2.0 | aprovada |
| `ecommerce-loja` | Planeja, audita e especifica uma loja virtual (plataforma pronta, stack própria ou catálogo simples com pedido pelo WhatsApp): produtos, variantes e SKUs, estoque, coleções e fi... | LKT System | aprovada |
| `emil-design-eng` | This skill encodes Emil Kowalski's philosophy on UI polish, component design, animation decisions, and the invisible details that make software feel great. | emilkowalski/skills · MIT | aprovada |
| `estruturar-pagina-de-oferta` | Estrutura uma página de oferta/venda — headline, promessa, público, dor, oferta, prova, demonstração, expert (quando existir), CTA, FAQ, garantia, checkout e evento de conversão... | LKT System | aprovada |
| `frontend-design` | Guidance for distinctive, intentional visual design when building new UI or reshaping an existing one. | anthropics/claude-plugins-official · Apache-2.0 | aprovada |
| `pagina-e-site` | Coordena a criação de uma página, landing page ou site (de um projeto de cliente ou interno) do contexto até o QA: objetivo, arquitetura de informação, conteúdo, estrutura de pá... | LKT System | aprovada |
| `referencia-site` | Analisa referências visuais e de interação de sites (link, print, vídeo) para identificar exatamente o que o usuário quer aproveitar — scroll, hero, tipografia, paleta, grid, mo... | LKT System | aprovada |
| `theme-factory` | Toolkit for styling artifacts with a theme. | anthropics/skills · Apache-2.0 | aprovada |
| `ux-copy` | Write or review UX copy — microcopy, error messages, empty states, CTAs. | anthropics/knowledge-work-plugins · Apache-2.0 | aprovada |
| `web-artifacts-builder` | Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). | anthropics/skills · Apache-2.0 | aprovada |

## Referência Codex (`terceiros/codex/`)

| ID | Fonte | Licença | Estado |
|---|---|---|---|
| `codex.documents/documents` | openai/openai-runtime | nao_verificado | pendente |
| `codex.google-drive/google-docs` | openai/plugins | nao_verificado | pendente |
| `codex.google-drive/google-drive` | openai/plugins | nao_verificado | pendente |
| `codex.google-drive/google-drive-comments` | openai/plugins | nao_verificado | pendente |
| `codex.google-drive/google-sheets` | openai/plugins | nao_verificado | pendente |
| `codex.google-drive/google-slides` | openai/plugins | nao_verificado | pendente |
| `codex.pdf/pdf` | openai/openai-runtime | nao_verificado | pendente |
| `codex.presentations/presentations` | openai/openai-runtime | nao_verificado | pendente |
| `codex.remotion/remotion-best-practices` | remotion-dev/remotion | nao_verificado | bloqueada |
| `codex.remotion/remotion-captions` | remotion-dev/remotion | nao_verificado | bloqueada |
| `codex.remotion/remotion-create` | remotion-dev/remotion | nao_verificado | bloqueada |
| `codex.remotion/remotion-docs` | remotion-dev/remotion | nao_verificado | bloqueada |
| `codex.remotion/remotion-interactivity` | remotion-dev/remotion | nao_verificado | bloqueada |
| `codex.remotion/remotion-maps` | remotion-dev/remotion | nao_verificado | bloqueada |
| `codex.remotion/remotion-markup` | remotion-dev/remotion | nao_verificado | bloqueada |
| `codex.remotion/remotion-multimedia` | remotion-dev/remotion | nao_verificado | bloqueada |
| `codex.remotion/remotion-render` | remotion-dev/remotion | nao_verificado | bloqueada |
| `codex.remotion/remotion-saas` | remotion-dev/remotion | nao_verificado | bloqueada |
| `codex.remotion/remotion-studio` | remotion-dev/remotion | nao_verificado | bloqueada |
| `codex.remotion/remotion-upgrade` | remotion-dev/remotion | nao_verificado | bloqueada |
| `codex.samautomation-workflows/n8n-workflow-check` | smrht/samautomation-workflows | MIT | referência |
| `codex.spreadsheets/excel-live-control` | openai/openai-runtime | nao_verificado | pendente |
| `codex.spreadsheets/spreadsheets` | openai/openai-runtime | nao_verificado | pendente |
| `codex.supabase/supabase` | supabase-community/supabase-plugin | nao_verificado | pendente |
| `codex.supabase/supabase-postgres-best-practices` | supabase-community/supabase-plugin | nao_verificado | pendente |
| `codex.vercel/access-protected-vercel-deployment` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/ai-gateway` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/ai-sdk` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/auth` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/bootstrap` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/build-agents` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/cdn-caching` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/chat-sdk` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/create-a-backend` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/custom-metrics` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/deployments-cicd` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/domains` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/env-vars` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/eve` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/flags-sdk` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/is-agentic` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/knowledge-update` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/marketplace` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/microfrontends` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/queues` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/react-best-practices` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/routing-middleware` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/runtime-cache` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/vercel-agent` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/vercel-cli` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/vercel-connect` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/vercel-firewall` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/vercel-functions` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/vercel-sandbox` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/vercel-services` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/vercel-storage` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/verification` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex.vercel/workflow` | vercel/vercel-plugin | Apache-2.0 | referência |
| `codex/chatgpt-apps` | openai/skills | Apache-2.0 | referência |
| `codex/cli-creator` | openai/skills | Apache-2.0 | referência |
| `codex/cloudflare-deploy` | openai/skills | Apache-2.0 | referência |
| `codex/define-goal` | openai/skills | Apache-2.0 | referência |
| `codex/gh-fix-ci` | openai/skills | Apache-2.0 | referência |
| `codex/hatch-pet` | openai/skills | Apache-2.0 | referência |
| `codex/jupyter-notebook` | openai/skills | Apache-2.0 | referência |
| `codex/netlify-deploy` | openai/skills | Apache-2.0 | referência |
| `codex/openai-docs` | openai/skills | Apache-2.0 | referência |
| `codex/pdf` | openai/skills | Apache-2.0 | referência |
| `codex/playwright` | openai/skills | Apache-2.0 | referência |
| `codex/playwright-interactive` | openai/skills | Apache-2.0 | referência |
| `codex/render-deploy` | openai/skills | Apache-2.0 | referência |
| `codex/screenshot` | openai/skills | Apache-2.0 | referência |
| `codex/security-best-practices` | openai/skills | Apache-2.0 | referência |
| `codex/security-ownership-map` | openai/skills | Apache-2.0 | referência |
| `codex/security-threat-model` | openai/skills | Apache-2.0 | referência |
| `codex/sentry` | openai/skills | Apache-2.0 | referência |
| `codex/speech` | openai/skills | Apache-2.0 | referência |
| `codex/transcribe` | openai/skills | Apache-2.0 | referência |
| `codex/vercel-deploy` | openai/skills | Apache-2.0 | referência |
| `codex/yeet` | openai/skills | Apache-2.0 | referência |

## Skills obrigatórias em cadeia

Para páginas, sites, landing pages, dashboards, portais ou interfaces:

1. `pagina-e-site`
2. `design-front-end`
3. `texto-natural-pt-br`

Para qualquer texto voltado ao público final, aplicar `texto-natural-pt-br`
ao final do fluxo, independente da skill principal usada. Regras de
precedência completas em [`roteamento.md`](roteamento.md).
