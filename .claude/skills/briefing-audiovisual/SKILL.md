---
name: briefing-audiovisual
description: >
  Coleta o briefing de uma produção audiovisual: objetivo, mensagem,
  público, formato, duração, referências, orçamento e prazo. Base de
  todo roteiro/storyboard. Use quando o usuário pedir "vamos gravar um
  vídeo pra X", "briefing pra esse comercial".
---

# briefing-audiovisual — Briefing de produção audiovisual

## Quando usar

Início de qualquer produção audiovisual (comercial, institucional,
conteúdo de redes, depoimento).

## Quando não usar

Vídeo curto simples de rede social sem produção formal → `roteiro`
(módulo de conteúdo) já resolve sozinho.

## Entradas

Respostas do cliente às perguntas abaixo.

## Dependências

`briefing-completo` (estrutura geral), `posicionamento`.

## Contexto que deve ser carregado

Posicionamento e DNA do negócio do projeto ativo.

---

## Workflow

1. Objetivo do vídeo (o que deve fazer o espectador sentir/fazer
   depois).
2. Mensagem central (uma só).
3. Público específico.
4. Formato e duração (comercial 30s, institucional 2min, depoimento,
   etc.).
5. Referências visuais/de estilo (o que o cliente gosta).
6. Orçamento e prazo.
7. Critério de aprovação (o que faz o cliente aprovar a entrega).
8. Salvar em `<pasta-do-projeto-ativo>/06-audiovisual/briefing.md`.

## Saídas

Briefing completo (8 itens).

## Caminho de salvamento

`<pasta-do-projeto-ativo>/06-audiovisual/`.

## Regras

- Objetivo e mensagem central sempre confirmados antes de qualquer
  roteiro.
- Critério de aprovação definido antes de gravar, não depois.

## Critérios de qualidade

Os 8 itens preenchidos ou explicitamente marcados como pendentes.

## Critérios de validação

Mensagem central é uma frase só, não um parágrafo.

## Limitações

Não decide o roteiro em si — isso é `roteiro-audiovisual`.

## Contrato de handoff

Encaminha pra `roteiro-audiovisual`.

## Exemplos de gatilhos positivos

- "Vamos gravar um vídeo institucional, faz o briefing"
- "Briefing pra esse comercial novo"

## Exemplos de gatilhos negativos

- "Escreve o roteiro de um reels rápido" (é `roteiro`, módulo de
  conteúdo, sem produção formal)
