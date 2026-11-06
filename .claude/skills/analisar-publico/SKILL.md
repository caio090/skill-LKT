---
name: analisar-publico
description: >
  Aprofunda quem é o público real de um cliente/projeto: perfil, dor,
  processo de decisão de compra, objeções, onde ele está. Baseado em
  dado real do negócio (clientes existentes), não em persona genérica.
  Use quando o usuário pedir "quem é meu público de verdade", "entende
  melhor meu cliente ideal".
---

# analisar-publico — Perfil real de público

## Quando usar

Diagnóstico, posicionamento ou plano de marketing que precisa de
clareza sobre quem realmente compra — não uma persona genérica de
template.

## Quando não usar

Pesquisa de mercado ampla (tamanho, tendência) → `pesquisa-mercado`.

## Entradas

Dados reais do negócio: quem já compra, perguntas frequentes, objeções
ouvidas de verdade.

## Dependências

`_memoria/produtos-e-servicos.md` ou o do cliente. Se houver CRM/dados de
clientes já processados, usar `analisar-dados` neles primeiro.

## Contexto que deve ser carregado

Diagnóstico e oferta do projeto ativo.

---

## Workflow

1. Perguntar (ou extrair do diagnóstico): quem já compra hoje, de
   verdade — não quem "gostaria" de vender pra.
2. Levantar a dor real que motiva a compra (não a dor genérica de
   template de marketing).
3. Mapear o processo de decisão: como esse público decide, o que
   pesquisa antes, quem mais influencia a decisão.
4. Levantar objeções reais já ouvidas (preço, confiança, tempo).
5. Mapear onde esse público está (canal, horário, tipo de conteúdo que
   consome).
6. Salvar em `<pasta-do-projeto-ativo>/01-diagnostico/publico.md`.

## Saídas

`01-diagnostico/publico.md`.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/01-diagnostico/`.

## Regras

- Basear em cliente real, não em persona fictícia de template ("Maria,
  32 anos, gosta de yoga" sem lastro real é proibido).
- Se não houver dado real ainda, registrar isso como lacuna e sugerir
  como levantar (entrevista com clientes atuais, por exemplo).

## Critérios de qualidade

Perfil descrito é rastreável a clientes/comportamento real, não
inventado.

## Critérios de validação

Objeções e dores citadas têm exemplo concreto de onde vieram.

## Limitações

Não substitui pesquisa quantitativa formal quando o negócio precisar de
uma amostra estatística real.

## Contrato de handoff

Encaminha pra `posicionamento`, `estrategia-de-marketing`,
`criar-produto-e-oferta`.

## Exemplos de gatilhos positivos

- "Quem é meu cliente de verdade"
- "Quais objeções meu público mais tem"

## Exemplos de gatilhos negativos

- "Qual o tamanho desse mercado" (é `pesquisa-mercado`)
