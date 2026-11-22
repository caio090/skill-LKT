# Funis, lançamentos e métricas — referência geral

Referência de planejamento usada por `escada-de-valor-e-funil`,
`planejar-lancamento`, `desenhar-funil`, `analisar-conversao`,
`plano-de-campanha` e `relatorio-ads`. Contém só conhecimento geral: nada
de cliente, preço interno ou dado privado. O contexto de cada cliente fica
na memória e no workspace do projeto consumidor.

Espelho executável no LOKAT OS: `src/lib/marketing-ops/frameworks.ts`,
`metrics.ts` e `funnel-analysis.ts`.

## Regra de honestidade

- Metodologia é referência de planejamento, não garantia de resultado.
- Nenhum número deste arquivo é meta. Meta ou benchmark só existe por
  cliente, com fonte declarada (histórico do próprio cliente, estudo
  citável, combinado em contrato).
- Sem dado, dizer "sem dado". Sem histórico ou benchmark, dizer "sem
  referência", nunca preencher com uma taxa "de mercado".

## De onde vêm as ideias

| Conceito | Origem | Como usar |
|---|---|---|
| Escada de valor (isca → entrada → principal → premium → continuidade) | Russell Brunson, *DotCom Secrets* (2015) | Organizar as ofertas do cliente e o caminho entre elas. |
| Tipos de funil (captura, oferta de entrada, webinar, aplicação) | Brunson, *DotCom Secrets* e *Expert Secrets* (2017) | Escolher o formato pela oferta, ticket e ciclo de venda. |
| Gancho, história e oferta | Brunson, *DotCom Secrets* | Estruturar anúncio e página. |
| Tráfego que você controla, conquista e possui | Brunson, *Traffic Secrets* (2020) | Equilibrar mídia paga, parcerias e audiência própria (lista, WhatsApp). |
| Fórmula de Lançamento (pré-pré, pré com conteúdos/CPLs, carrinho aberto, encerramento) | Érico Rocha, adaptação brasileira do *Product Launch Formula* de Jeff Walker | Planejar lançamentos semente, interno, em parceria e perpétuo. |

Adaptar sempre: negócio local que vende pelo WhatsApp raramente precisa de
webinar; serviço de alto valor raramente fecha sem conversa.

## Escolha do funil

| Situação do cliente | Formato a considerar | Evitar quando |
|---|---|---|
| Público não conhece a marca; venda pede confiança | Captura (isca) → nutrição → oferta | Compra é imediata e barata |
| Negócio local / serviço que fecha na conversa | Anúncio → WhatsApp → orçamento → venda | Não há quem responda rápido |
| Ticket médio/alto que precisa de explicação | Webinar / aula | Ninguém apresenta bem; produto simples |
| Serviço caro, consultivo, poucas vagas | Aplicação → reunião → fechamento | Ticket baixo (reunião não se paga) |
| Existe produto barato que leva ao principal | Oferta de entrada → oferta seguinte | Não existe oferta seguinte |

Cada etapa precisa de um **evento que comprove a entrada** (ex.: `lead`,
`messaging_conversation_started`, `purchase`) e de uma fonte para esse
evento (Pixel, API de Conversões, CRM, planilha). Etapa sem evento não é
medida; não inventar número para ela.

## Lançamentos (Érico Rocha / Jeff Walker)

| Modelo | Quando considerar | Cuidados |
|---|---|---|
| Semente | Validar oferta com público pequeno | Vender só o que dá para entregar no prazo |
| Interno | Já existe audiência própria aquecida | Prazo e escassez verdadeiros (CDC, regras da Meta) |
| Parceria | Parceiros com audiência compatível | UTM/cupom por parceiro, senão a atribuição se perde |
| Perpétuo | Oferta validada, tráfego contínuo | Prazo individual real, sem contador falso |

Fases do interno: pré-pré-lançamento (aquecer, pesquisar) → pré-lançamento
(sequência de conteúdos) → carrinho aberto (período curto) → encerramento →
pós-lançamento (entrega e análise por etapa). Não prometer ganho financeiro
nem resultado garantido em nenhum material.

## Métricas: fórmula, período, fonte e limitações

| Métrica | Fórmula | Período | Fonte | Limitações |
|---|---|---|---|---|
| CPM | investimento ÷ impressões × 1000 | mesmo intervalo | plataforma | moeda da conta; varia por leilão |
| CTR de link | cliques no link ÷ impressões | mesmo intervalo | plataforma | clique ≠ visita |
| CPC de link | investimento ÷ cliques no link | mesmo intervalo | plataforma | moeda da conta |
| Frequência | impressões ÷ alcance | intervalo fechado | plataforma | alcance não soma dia a dia |
| Custo por lead | investimento ÷ leads | mesmo intervalo; dizer se lead é da plataforma ou do CRM | plataforma ou CRM | janela de atribuição; lead da plataforma pode não chegar ao CRM |
| Conversão entre etapas | entradas etapa N+1 ÷ entradas etapa N | coorte ou fluxo (declarar) | eventos / CRM | por fluxo, o período corrente sai subestimado |
| Taxa de fechamento | ganhas ÷ (ganhas + perdidas) | oportunidades encerradas no período | CRM | abertas ficam fora |
| CAC | (mídia + custos declarados) ÷ novos clientes | mesmo intervalo | plataforma + financeiro + CRM | dizer o que entra; ciclo longo desloca vendas |
| ROAS | receita atribuída ÷ investimento em mídia | mesma janela de atribuição | plataforma ou CRM | receita não é lucro |
| Ticket médio | receita ÷ vendas | mesmo intervalo | CRM / financeiro | poucas vendas distorcem |
| LTV simples | ticket médio × compras no horizonte | horizonte explícito | CRM / financeiro | sem histórico é projeção |

### Cuidados que valem para todas

- **Atribuição:** números da Meta seguem a janela de atribuição de cada
  conjunto (configuração unificada). Não somar com o CRM nem comparar
  períodos com janelas diferentes. Registrar a configuração junto do dado.
- **Fuso:** dias da plataforma seguem o fuso da conta de anúncios, que pode
  diferir do CRM.
- **Moeda:** valores na moeda da conta; converter antes de comparar contas.
- **Amostra:** com menos de ~30 entradas na etapa de origem, a taxa é
  leitura fraca; dizer isso em vez de concluir.
- **Gargalo:** é a passagem que mais piorou contra o histórico do próprio
  cliente (ou benchmark do cliente com fonte). Sem referência, não apontar.
