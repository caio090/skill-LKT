# Food service — especialização de gestão de negócio

Skills: `dna-do-negocio`, `ficha-tecnica`, `rendimento-e-desperdicio`,
`engenharia-de-cardapio`, `precificacao-food-service`,
`cmv-real-e-teorico`, `estoque-food-service`, `aumento-de-ticket`,
`analisar-promocao-cupom`, `cardapio-digital`, e o orquestrador
`produto-e-engenharia-de-cardapio`.

Templates em `templates/gestao-de-negocio/food-service/`. Schemas em
`schemas/gestao-de-negocio/`.

O sistema entende o negócio antes de calcular: segmento, cidade/região,
público, posicionamento, canais, operação, capacidade produtiva,
horários, equipe, fornecedores, embalagens, taxas, desperdícios,
promoções, histórico de venda, objetivo financeiro e limitações reais —
nunca começa a análise de cardápio ou preço só pelo valor de venda.

Comparações priorizam a evolução do próprio negócio (período vs.
período, produto vs. produto, previsto vs. realizado, CMV teórico vs.
real) — nunca faixa universal de "CMV bom/ruim" ou média de mercado sem
fonte, segmento, região e data.

Aplicável no futuro a outros segmentos (varejo, serviços, clínica,
agência, escritório, indústria) adaptando os mesmos princípios, sem
duplicar a arquitetura.
