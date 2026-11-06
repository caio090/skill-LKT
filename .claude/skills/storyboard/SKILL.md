---
name: storyboard
description: >
  Detalha cada cena do roteiro em plano visual: cena, plano,
  enquadramento, ação, diálogo, áudio, duração, transição, referência
  visual e necessidade de produção. Use quando o usuário pedir "monta o
  storyboard desse roteiro", "detalha os planos dessa cena".
---

# storyboard — Storyboard cena a cena

## Quando usar

Depois de `roteiro-audiovisual`, antes da gravação.

## Quando não usar

Roteiro ainda não existe → `roteiro-audiovisual` primeiro.

## Entradas

Roteiro já escrito.

## Dependências

`roteiro-audiovisual`.

## Contexto que deve ser carregado

Roteiro do projeto ativo.

---

## Workflow

Pra cada cena do roteiro, detalhar:

1. **Cena** — número e resumo.
2. **Plano** — geral, médio, close, etc.
3. **Enquadramento** — o que entra no quadro.
4. **Ação** — o que acontece.
5. **Diálogo** — texto falado, se houver.
6. **Áudio** — trilha, efeito, silêncio proposital.
7. **Duração** — estimativa em segundos.
8. **Transição** — corte seco, fade, etc.
9. **Referência visual** — imagem/vídeo de referência do estilo
   pretendido.
10. **Necessidade de produção** — equipamento, locação, figurino,
    pessoas envolvidas nessa cena específica.

Salvar em `<pasta-do-projeto-ativo>/06-audiovisual/storyboard.md`.

## Saídas

Storyboard com os 10 campos por cena.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/06-audiovisual/`.

## Regras

- Todo campo preenchido por cena — nunca deixar "a definir" sem
  necessidade.
- Necessidade de produção de cada cena alimenta `plano-de-captacao`.

## Critérios de qualidade

Quem vai gravar consegue executar só lendo o storyboard, sem perguntar
mais nada.

## Critérios de validação

Soma das durações por cena bate com a duração total do formato.

## Limitações

Não define o cronograma de gravação em si — isso é `plano-de-captacao`.

## Contrato de handoff

Encaminha pra `lista-de-planos` e `plano-de-captacao`.

## Exemplos de gatilhos positivos

- "Monta o storyboard desse roteiro"
- "Detalha os planos de cada cena"

## Exemplos de gatilhos negativos

- "Escreve o roteiro" (é `roteiro-audiovisual`, passo anterior)
