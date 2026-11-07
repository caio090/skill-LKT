---
name: ecommerce-loja
description: >
  Planeja, audita e especifica uma loja virtual (plataforma pronta, stack
  própria ou catálogo simples com pedido pelo WhatsApp): produtos,
  variantes e SKUs, estoque, coleções e filtros, página de produto,
  carrinho, checkout, pagamento, frete e retirada, trocas, SEO técnico,
  analytics, acessibilidade e mobile, com roteiro de teste sem compra
  real. Use quando o usuário pedir "monta uma loja virtual", "audita
  minha loja", "catálogo com pedido no WhatsApp", "estrutura de produtos
  e variantes", "checkout da loja".
---

# ecommerce-loja — Loja virtual do catálogo ao pós-venda

## Quando usar

- Planejar uma loja nova (Shopify, Nuvemshop, WooCommerce, VTEX, stack
  própria em Next.js ou catálogo estático com consulta pelo WhatsApp).
- Auditar uma loja existente: catálogo, conversão, checkout, frete,
  políticas, SEO, performance e mobile.
- Especificar integração de estoque e pedidos com sistema já usado pelo
  cliente.

## Quando não usar

- Cardápio de delivery de food service → `cardapio-digital`.
- Página institucional ou landing page sem venda de produto →
  `pagina-e-site`.
- Só a campanha de mídia da loja → `plano-de-campanha` / `anuncio-meta`.
- Execução dos testes ponta a ponta → `qa-e2e-playwright` (esta skill
  só define os roteiros).

## Modo de atuação (declarar no início da resposta)

| Modo | O que a skill faz | O que NÃO faz |
|---|---|---|
| Planejar | Estrutura, especificação, backlog, critérios de aceite | Não cria nada na plataforma |
| Auditar | Lê a loja (navegação pública, exportação de catálogo, prints) e aponta problemas | Não altera preço, estoque, produto ou campanha |
| Executar com aprovação | Gera arquivos (CSV de importação, código, textos) para o responsável aplicar | Não publica, não ativa pagamento, não importa em produção sem aprovação explícita por escrito |

Alterar preço real, estoque, cupom, campanha, meio de pagamento ou
configuração de frete em produção exige autorização específica do
responsável para aquela alteração. Pedido de diagnóstico nunca vira
alteração.

## Entradas

- Segmento, região de atendimento, ticket médio, volume de pedidos.
- Plataforma atual (ou "nenhuma") e sistemas conectados (ERP, PDV,
  planilha de estoque, gateway).
- Exportação do catálogo ou lista de produtos.
- Políticas atuais: troca, devolução, prazo, frete, retirada.
- Identidade visual oficial (logo e arquivos originais; nunca redesenhar
  logo por inferência — pedir o arquivo se não estiver no projeto).

## Dependências

`design-front-end` (interface), `texto-natural-pt-br` (todo texto
público), `seo` (estratégia de busca), `integrar-api` (estoque/pedidos),
`planejar-banco-de-dados` (stack própria), `qa-e2e-playwright` (testes).

---

## Workflow

### 1. Catálogo

1. Modelo de produto: título, descrição, marca, categoria, atributos
   (tamanho, cor, material, numeração), variantes e SKU único por
   variante. Regra de SKU documentada (ex.: `MODELO-COR-TAM`).
2. Coleções e categorias com no máximo 2 níveis; filtros só por
   atributo que existe de fato nos produtos.
3. Imagens: proporção única por loja, fundo consistente, peso ≤ 200 KB
   na listagem, texto alternativo descrevendo o produto.
4. Descrição: o que é, para quem, medidas/tabela de tamanhos, cuidados,
   o que vem na caixa. Sem promessa que o produto não cumpre.

### 2. Estoque e disponibilidade

1. Fonte de verdade do estoque (plataforma, ERP ou planilha) — uma só.
2. Reserva no carrinho ou só na confirmação do pagamento (decidir e
   documentar).
3. Ruptura: esconder, mostrar "esgotado" ou "avise-me". Variante
   esgotada nunca selecionável como disponível.
4. Divergência de preço ou estoque entre canais: regra de qual vale e
   alerta para o responsável.

### 3. Carrinho e checkout

1. Etapas mínimas; frete calculável antes do login.
2. Pagamentos: Pix, cartão (parcelamento), boleto se fizer sentido.
   Antifraude e conciliação descritos em nível conceitual (quem
   confere, quando, com que relatório).
3. Abandono de carrinho: gatilho, intervalo, canal, opção de descadastro.
4. Mensagens de erro específicas (CEP inválido, cartão recusado,
   estoque acabou durante a compra).

### 4. Entrega, retirada e políticas

1. Tabela de frete por região/peso, frete grátis com regra clara,
   retirada na loja com horário, restrições geográficas.
2. Trocas e devoluções conforme o Código de Defesa do Consumidor
   (arrependimento em 7 dias para compra a distância) — indicar revisão
   jurídica para o texto final.

### 5. Loja sem checkout (consulta pelo WhatsApp)

1. Cada produto tem botão "Consultar disponibilidade" que abre o
   WhatsApp com mensagem pronta contendo produto, variante e SKU.
2. Link no formato `https://wa.me/<DDI+DDD+número>?text=<mensagem
   codificada>`. Exemplo de geração e teste em
   `exemplos/link-whatsapp.js`.
3. Nunca automatizar envio de mensagem. O cliente clica e envia.

### 6. SEO técnico, dados e performance

1. URL legível por produto, canonical nas variantes, sitemap, robots.
2. Dados estruturados `Product` + `Offer` (preço, moeda, disponibilidade)
   coerentes com a página.
3. Core Web Vitals medidos (LCP da página de produto e da listagem).
4. Analytics: eventos `view_item`, `add_to_cart`, `begin_checkout`,
   `purchase` (ou `contact` no modo WhatsApp), com consentimento de
   cookies conforme a LGPD.

### 7. Acessibilidade e mobile

Seleção de variante por teclado, contraste, foco visível, alvos de toque
≥ 44 px, estados de carregamento e vazio, sem rolagem horizontal.

### 8. Roteiros de teste (sem compra real)

Gerar a lista de cenários para `qa-e2e-playwright`: navegação por
categoria, filtro, variante esgotada, carrinho, cupom, frete por CEP,
checkout em **sandbox** do gateway, erro de pagamento simulado, link do
WhatsApp. Dados sempre fictícios (ver `exemplos/catalogo-ficticio.json`).

---

## Saídas

Documento com: modo de atuação, mapa do catálogo (atributos, variantes,
SKU), regras de estoque, fluxo de checkout, tabela de frete/retirada,
políticas, plano de SEO e eventos, checklist mobile/acessibilidade,
roteiros de teste e checklist de aceite.

## Checklist de aceite

**Comercial:** preço e condições conferidos pelo responsável; políticas
publicadas; frete validado em 3 CEPs reais de teste (sem pedido).
**Operacional:** fonte de estoque definida; responsável por pedido,
troca e atendimento nomeado por papel.
**Técnico:** testes de `qa-e2e-playwright` aprovados em sandbox; dados
estruturados válidos; nenhum segredo de gateway no código; eventos de
analytics disparando em ambiente de teste.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/07-tecnologia/ecommerce-<entrega>.md`.

## Regras

- Nunca criar pedido real, cobrar cartão real ou disparar mensagem real
  em teste.
- Nunca copiar segredos (chave de gateway, token de plataforma) para o
  documento, exemplo ou repositório.
- Dados de cliente real nunca entram em fixture ou exemplo.
- Recomendação comercial sem dado do cliente é marcada como estimativa.
- A sigla LKT não aparece em nenhuma peça entregue ao cliente.
