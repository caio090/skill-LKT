---
name: roteiro
description: >
  Escreve roteiro curto para vídeo de rede social (reels, stories,
  vídeo curto) a partir de uma pauta — gancho, desenvolvimento, CTA,
  indicação de corte/plano simples. Use quando o usuário pedir "escreve
  o roteiro desse reels", "roteiriza esse vídeo curto".
---

# roteiro — Roteiro curto para vídeo social

## Quando usar

Vídeo curto de rede social (reels, TikTok, stories, short) a partir de
uma pauta já definida.

## Quando não usar

Produção audiovisual maior (comercial, institucional, com equipe de
filmagem) → `roteiro-audiovisual` (mais completo, com cena/plano/
enquadramento/áudio).

## Entradas

Pauta (`pauta-de-conteudo`), duração alvo.

## Dependências

`pauta-de-conteudo`, `_memoria/preferencias.md`.

## Contexto que deve ser carregado

Tom de voz e posicionamento do projeto ativo.

---

## Workflow

1. Gancho (primeiros 2-3 segundos — motivo de não passar o vídeo).
2. Desenvolvimento (1 ideia central, não várias).
3. CTA final.
4. Indicação simples de corte/plano (quando muda o plano, texto na
   tela, se houver).
5. Duração estimada.
6. Encaminhar pra `texto-natural-pt-br` antes de finalizar.
7. Salvar em `<pasta-do-projeto-ativo>/04-marketing/roteiros/<tema>.md`.

## Saídas

Roteiro pronto pra gravação simples (sem equipe de produção completa).

## Caminho de salvamento

`<pasta-do-projeto-ativo>/04-marketing/roteiros/`.

## Regras

- Gancho é sempre a primeira coisa escrita, não deixar pro final.
- Uma ideia central por vídeo curto — não amontoar.

## Critérios de qualidade

Roteiro cabe na duração alvo sem parecer apressado ou vazio.

## Critérios de validação

Gancho, desenvolvimento e CTA presentes e na ordem certa.

## Limitações

Não cobre produção audiovisual complexa (isso é `roteiro-audiovisual`).

## Contrato de handoff

`texto-natural-pt-br` (acabamento). Se a gravação precisar de equipe/
equipamento, encaminhar pro módulo audiovisual.

## Exemplos de gatilhos positivos

- "Escreve o roteiro desse reels"
- "Roteiriza esse vídeo curto pro TikTok"

## Exemplos de gatilhos negativos

- "Roteiriza o comercial institucional" (é `roteiro-audiovisual`)
