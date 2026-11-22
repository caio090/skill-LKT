---
name: trafego-pago-lkt
description: Sistema LKT para planejar, estruturar, analisar e otimizar tráfego pago em Meta Ads e Google Ads, conectando funil, orçamento, criativos, tracking, CRM e resultado comercial.
---

# Tráfego Pago LKT

Esta skill transforma pedidos de tráfego pago em uma operação completa: contexto do negócio, estágio do funil, campanha, conjunto/grupo, anúncio, criativo, rastreamento, leitura de métricas, qualificação comercial e próxima decisão.

Não tratar tráfego como preenchimento de campos no gerenciador. O trabalho começa no objetivo de negócio e termina no resultado comercial medido.

## Quando usar

Ativar quando houver qualquer pedido sobre:

- Meta Ads, Facebook Ads, Instagram Ads ou Google Ads;
- criação, revisão ou duplicação de campanha;
- estrutura de campanha, conjunto/grupo e anúncio;
- orçamento, duração, distribuição de verba ou campanhas paralelas;
- topo, meio e fundo de funil;
- lançamento, captação, remarketing ou venda;
- análise de print do Gerenciador de Anúncios ou Google Ads;
- análise de vídeo, arte, copy, gancho, CTA ou retenção para mídia paga;
- Pixel da Meta, Conversions API, Google tag, GA4 ou tracking;
- leads, formulários, WhatsApp, landing page, CRM, CAC, CPA, ROAS;
- relatório de campanha e decisão de otimização.

Se o usuário anexar uma imagem ou vídeo, analisar o ativo antes de sugerir a estrutura.

## Princípios não negociáveis

1. Objetivo de negócio antes do objetivo da plataforma.
2. Funil é comportamento do cliente, não obrigação de criar três campanhas.
3. Campanha representa uma intenção principal; conjunto/grupo organiza público, orçamento, localização, agenda e otimização; anúncio contém criativo, mensagem, destino e CTA.
4. Orçamento pequeno exige simplificação. Não pulverizar verba entre campanhas, conjuntos ou criativos sem hipótese clara.
5. Orçamento maior permite ampliar testes, cobertura de funil e remarketing, mas não justifica complexidade sem evidência.
6. Nenhuma verba é "pequena demais" para pensar estrategicamente, mas verba menor reduz velocidade, alcance e quantidade de testes. Nunca prometer o mesmo resultado independentemente do investimento.
7. O objetivo é extrair o máximo de aprendizado e resultado possível dentro do orçamento real, preservando prioridade comercial.
8. Não usar benchmarks fixos de CTR, CPC, CPM, CPL ou CPA como lei. Comparar com histórico da conta, objetivo, nicho, região, estágio do funil, criativo, ticket e resultado comercial.
9. Não alterar várias variáveis ao mesmo tempo quando o objetivo for aprender. Identificar a hipótese do teste.
10. Não desligar estrutura vencedora apenas porque o plano previa um segundo teste. Preservar o que funciona enquanto houver resultado e margem para escalar.
11. Não confundir lead com venda. Lead entra no funil; comercial qualifica, conduz e registra avanço.
12. Não avaliar campanha apenas por curtida, clique ou mensagem. Conectar mídia a lead qualificado, oportunidade, venda, receita, margem, CAC e ROAS quando os dados existirem.
13. Não usar nomenclatura antiga se a interface atual mostra outra opção. Quando houver print, seguir os campos visíveis na tela.
14. Nunca publicar campanha, aumentar orçamento, gastar mídia ou alterar conta sem autorização explícita.
15. Quando a resposta depender da interface atual da Meta ou Google, verificar documentação atual ou usar os campos visíveis fornecidos pelo usuário.

## Leitura obrigatória

Antes de estruturar uma operação relevante, consultar:

- references/FUNIL-E-ORCAMENTO.md
- references/META-ADS.md quando Meta for usada
- references/GOOGLE-ADS.md quando Google for usado
- references/CRIATIVOS-E-METRICAS.md para análise de criativo e diagnóstico
- references/TRACKING-CRM-E-REMARKETING.md para rastreamento, leads e fechamento
- references/FRAMEWORKS-DE-FUNIL.md quando houver lançamento, escada de valor ou arquitetura de funil

## Processo operacional

### 1. Contexto

Identificar antes de montar a campanha:

- negócio e oferta;
- produto/serviço e ticket;
- região atendida;
- objetivo comercial;
- destino da conversão;
- orçamento de mídia disponível;
- prazo;
- ativos existentes;
- histórico de campanhas;
- capacidade de atendimento/comercial;
- tracking disponível;
- restrições do cliente.

Se o usuário já forneceu esses dados, não perguntar novamente.

### 2. Diagnóstico de funil

Classificar a intenção principal:

- **Topo:** descoberta, alcance, lembrança, visualização e primeiro contato.
- **Meio:** consideração, prova, comparação, conteúdo, case, demonstração e intenção crescente.
- **Fundo:** lead, conversa, orçamento, cadastro, agendamento, pedido, compra ou outra ação comercial.
- **Pós-conversão:** remarketing, recuperação, recompra, upsell, cross-sell, indicação e reativação.

Não transformar automaticamente cada estágio em uma campanha separada.

### 3. Arquitetura de orçamento

Calcular:

- verba total de mídia;
- dias ativos;
- verba média diária;
- quantidade real de campanhas e conjuntos que o orçamento comporta;
- prioridade do funil;
- verba reservada para testes quando fizer sentido.

Regra principal: quanto menor o orçamento, maior a concentração.

Exemplo conceitual:

- orçamento enxuto + objetivo de venda agora: priorizar fundo e usar criativos com prova/oferta;
- orçamento enxuto + marca nova sem dados: uma estrutura simples de descoberta ou lead, conforme objetivo real;
- orçamento suficiente + histórico: campanha principal + remarketing + teste controlado, se houver volume.

Não criar duas ou três campanhas apenas para "ter topo, meio e fundo". Criar múltiplas campanhas somente quando houver verba, público, objetivo ou etapa distinta que justifique a separação.

### 4. Escolha de plataforma

**Meta Ads:** forte para descoberta, demanda latente, criativo visual, leads, mensagens, remarketing e venda por oferta.

**Google Ads:** forte para demanda existente, intenção de busca, descoberta via YouTube/Demand Gen, remarketing e conversões rastreadas.

Pode usar as duas plataformas no mesmo sistema, mas cada uma deve receber função clara no funil.

### 5. Estrutura da campanha

Ao montar Meta Ads, entregar sempre:

1. **Campanha**
   - nome;
   - objetivo atual da Meta;
   - por que esse objetivo;
   - orçamento na campanha ou conjunto, se aplicável.

2. **Conjunto de anúncios**
   - nome;
   - local da conversão;
   - meta de desempenho;
   - público;
   - localização;
   - idade/gênero quando fizer sentido;
   - Advantage+ ou expansão, quando aplicável;
   - posicionamentos;
   - orçamento;
   - período;
   - hipótese do conjunto.

3. **Anúncio**
   - nome;
   - formato;
   - criativo;
   - Texto principal;
   - Título;
   - Descrição;
   - Chamada para ação;
   - destino.

4. **Formulário ou Mensagens**, quando existirem
   - apresentação;
   - título;
   - descrição;
   - perguntas;
   - informações de contato;
   - explicação de uso dos dados;
   - política de privacidade;
   - encerramento;
   - ação adicional;
   - saudação;
   - perguntas rápidas;
   - mensagem de conversão.

5. **Rastreamento**
   - Pixel;
   - Conversions API;
   - UTMs;
   - evento principal;
   - evento secundário;
   - CRM/planilha;
   - como atribuir venda ao lead.

Ao montar Google Ads, seguir o padrão específico em references/GOOGLE-ADS.md.

### 6. Leitura de criativo

Se receber vídeo:

- identificar os primeiros 1 a 3 segundos;
- qual é o gancho;
- quando aparece produto/oferta;
- se a promessa é cumprida;
- onde entra prova;
- onde entra CTA;
- se há excesso de introdução;
- se o formato combina com o posicionamento;
- sugerir hipóteses de queda de retenção, sem fingir possuir dados de retenção que não foram fornecidos.

Se receber imagem:

- identificar hierarquia;
- legibilidade;
- proposta;
- benefício;
- oferta;
- urgência;
- prova;
- CTA;
- adequação a Feed, Stories, Reels e demais posicionamentos.

Quando o problema exigir nova peça visual, encadear com **vidigal-png**.

### 7. Leitura de métricas

Ler o funil em ordem:

1. entrega: alcance, impressões, CPM, frequência;
2. atenção: retenção, visualizações, hook rate quando disponível;
3. interesse: CTR, cliques, CPC;
4. conversão: visualizações da página, formulário, conversa, lead, CPL/CPA;
5. qualidade: lead qualificado, contato, reunião, visita, proposta;
6. negócio: venda, receita, margem, CAC, ROAS, LTV.

Nunca concluir "criativo ruim" apenas por CPC alto. Cruzar as métricas.

Exemplos de diagnóstico:

- CPM saudável + CTR fraco: olhar criativo, oferta e mensagem antes de culpar distribuição;
- CTR forte + pouca conversão: olhar página, formulário, WhatsApp, proposta e tracking;
- clique barato + lead ruim: qualificação, oferta ou público podem estar atraindo curiosos;
- frequência crescente + resultado piorando: investigar fadiga;
- leads bons + poucas vendas: investigar atendimento, timing, preço e follow-up;
- venda com CPA aceitável apesar de CPC alto: campanha pode estar saudável.

### 8. Tracking antes de escalar

Quando existe site, landing page ou checkout, verificar possibilidade de:

- Meta Pixel;
- Conversions API;
- Google tag;
- GA4;
- UTMs;
- eventos de ViewContent, Lead, Contact, Purchase ou equivalentes;
- deduplicação quando browser e servidor enviam o mesmo evento;
- identificação de origem no CRM.

Se não houver tracking completo, declarar claramente o limite da análise.

### 9. CRM e ciclo comercial

Todo lead deve poder avançar por estados como:

**Novo → Contatado → Respondeu → Qualificado → Negociação → Visita/Reunião → Venda → Perdido/Follow-up**

Adaptar à operação.

Criar remarketing com base em comportamento quando houver volume e base suficiente:

- assistiu vídeo;
- engajou;
- visitou página;
- abriu formulário e não enviou;
- enviou lead;
- conversou;
- comprou.

Excluir compradores ou leads já convertidos quando o objetivo exigir aquisição nova.

### 10. Otimização

Antes de mudar algo, responder:

- qual métrica está fora do esperado?
- em qual etapa do funil está o gargalo?
- qual hipótese explica isso?
- qual variável será alterada?
- por quanto tempo ou volume será observada?
- qual resultado confirma ou rejeita a hipótese?

Evitar "otimização por ansiedade".

## Padrão de orçamento LKT

O orçamento define a largura do teste, não a qualidade do raciocínio.

Com verba enxuta:

- concentrar no objetivo comercial prioritário;
- reduzir número de campanhas/conjuntos;
- usar poucos criativos com ângulos realmente diferentes;
- aproveitar estruturas validadas;
- testar uma variável por vez;
- prolongar janela de coleta quando necessário;
- não prometer volume que a verba não comporta.

Com verba intermediária:

- manter campanha principal;
- reservar parcela para teste;
- ativar remarketing se houver público;
- ampliar criativos e ofertas sem fragmentar demais.

Com verba maior e volume:

- separar etapas quando houver razão;
- testar geografia, oferta, público, posicionamento e criativo;
- usar campanhas de retenção/remarketing;
- trabalhar valor de conversão quando tracking permitir.

Nunca definir orçamento mínimo universal em reais. A plataforma pode impor mínimos diferentes por objetivo, moeda, evento de cobrança e conta.

## Modelos de funil

A skill pode combinar:

- topo, meio, fundo e pós-conversão;
- escada de valor;
- descoberta → consideração → conversão → retenção;
- lançamento com pré-aquecimento, captação, evento/oferta, fechamento e remarketing;
- Hook → Story → Offer como lente criativa;
- Problema → prova → oferta → ação;
- PAS, AIDA, BAB, QUEST, PPP e storyboard.

Framework é ferramenta, não dogma. A escolha depende do cliente, oferta, prazo, orçamento e estágio de consciência.

## Exemplo genérico: negócio local de ticket alto

1. **Campanha de descoberta/posicionamento**
   - vídeo ou prova;
   - objetivo coerente com alcance/engajamento;
   - coleta de audiência.

2. **Campanha de captação**
   - Leads;
   - formulário ou mensagens;
   - perguntas suficientes para separar interesse real de curiosidade;
   - CRM.

3. **Remarketing**
   - pessoas que viram, engajaram, visitaram ou abriram formulário;
   - case, estoque/oferta, objeções, urgência ou condição;
   - destino comercial.

4. **Comercial**
   - contato;
   - qualificação;
   - follow-up;
   - venda;
   - feedback de qualidade para mídia.

Essa sequência não obriga três campanhas simultâneas. O orçamento e o volume definem se as etapas rodam juntas ou em sequência.

## Segurança operacional

- Não pedir senha pessoal quando acesso por permissões empresariais resolver.
- Preservar propriedade dos ativos no cliente.
- Não criar Pixel, CAPI, tag, público, campanha, formulário ou integração sem autorização quando isso alterar conta externa.
- Não publicar ou aumentar gasto sem autorização.
- Não afirmar que tracking está funcionando sem validar eventos.
- Não usar dados sensíveis em públicos ou relatórios fora das regras da plataforma e da legislação aplicável.

## Fontes oficiais de referência

Revisado em 2026-11-22.

- Meta Marketing API, estrutura Campaign → Ad Set → Ad e objetivos ODAX:
  https://developers.facebook.com/docs/marketing-api/reference/v27.0
- Meta Blueprint, Performance 5:
  https://www.facebookblueprint.com/student/path/253157-performance-5
- Meta Pixel e Conversions API:
  https://developers.facebook.com/docs/facebook-business-extension/fbe/get-started/pixel-capi-onboarding/
- Google Ads, objetivos de campanha:
  https://support.google.com/google-ads/answer/7450050
- Google Ads, Smart Bidding:
  https://support.google.com/google-ads/answer/7065882
- Google Ads, escolha de estratégia de lances:
  https://support.google.com/google-ads/answer/2472725
