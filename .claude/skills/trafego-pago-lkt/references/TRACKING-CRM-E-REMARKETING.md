# Tracking, CRM e remarketing

## Objetivo

Fechar o ciclo entre anúncio e resultado comercial.

Sem tracking e retorno do comercial, o gerenciador mostra apenas uma parte do negócio.

## Meta Pixel

Pixel envia eventos do navegador para a Meta.

Usos:
- medir ações no site;
- criar públicos;
- otimizar campanhas;
- atribuir conversões.

Eventos comuns:
- PageView;
- ViewContent;
- Lead;
- Contact;
- InitiateCheckout;
- Purchase.

Usar o evento que representa a ação real do negócio.

## Conversions API

CAPI envia eventos via servidor/API.

Pode complementar o Pixel.

Quando browser e servidor enviam o mesmo evento:
- configurar deduplicação;
- preservar event_id quando aplicável.

Não afirmar que CAPI está ativa apenas porque existe Pixel.

Fonte:
https://developers.facebook.com/docs/facebook-business-extension/fbe/get-started/pixel-capi-onboarding/

## Google tag e GA4

Usar para:
- page views;
- eventos;
- conversões;
- origem;
- UTMs;
- importação para Google Ads quando apropriado.

A ação usada para otimização deve representar valor real.

## UTMs

Padrão recomendado:

utm_source = plataforma
utm_medium = paid_social / cpc
utm_campaign = campanha
utm_content = anúncio/criativo
utm_term = palavra-chave ou audiência quando aplicável

Manter nomenclatura consistente.

## CRM

Lead deve registrar, quando disponível:
- data;
- nome;
- telefone;
- cidade;
- produto/interesse;
- campanha;
- conjunto/grupo;
- anúncio;
- origem;
- status;
- responsável;
- última ação;
- próxima ação;
- venda;
- valor.

## Status de funil

Exemplo:
Novo → Contatado → Respondeu → Qualificado → Negociação → Visita/Reunião → Venda

Saídas:
- Perdido;
- Sem resposta;
- Follow-up;
- Reativar depois.

## Feedback para tráfego

O comercial deve devolver:
- quantidade de leads válidos;
- interesse real;
- motivos de perda;
- visitas;
- propostas;
- vendas;
- ticket;
- margem quando possível.

Sem isso, não existe leitura completa de qualidade.

## Remarketing

Fontes possíveis:
- visualizadores de vídeo;
- engajamento Instagram/Facebook;
- visitantes de site;
- visitantes de página específica;
- abertura de formulário;
- lead;
- lista de clientes;
- carrinho;
- checkout;
- compradores.

## Exclusões

Quando fizer sentido:
- excluir compradores da aquisição;
- excluir leads já convertidos;
- excluir equipe;
- excluir público irrelevante.

## Sequência conceitual

Descoberta → Engajamento/visita → Lead → Qualificação → Negociação → Venda → Pós-venda

A campanha de remarketing deve responder à próxima objeção ou ação, não apenas repetir o anúncio anterior.

## Exemplo genérico

Pessoa viu 50% de vídeo:
- remarketing com case/prova.

Pessoa abriu formulário e não enviou:
- remarketing com benefício, objeção ou urgência.

Lead enviado:
- CRM + atendimento;
- remarketing apenas se não conflitar com abordagem comercial.

Comprador:
- excluir aquisição e mover para retenção/upsell quando aplicável.

## Limitações

Se a conversão ocorre em WhatsApp comum sem integração:
- parte da atribuição pode ficar incompleta;
- registrar origem no CRM;
- usar mensagem pré-preenchida quando útil;
- pedir retorno do comercial.

Se a pessoa vê anúncio e chama depois por outro caminho:
- pode haver influência da mídia sem atribuição direta;
- não afirmar causalidade sem evidência.
