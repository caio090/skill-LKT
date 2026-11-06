---
name: analisar-video
description: >
  Analisa um vídeo já existente (próprio ou de referência/concorrente):
  estrutura, ritmo, gancho, retenção estimada, pontos fortes e fracos.
  Use quando o usuário pedir "analisa esse vídeo", "por que esse vídeo
  do concorrente performa bem".
---

# analisar-video — Análise de vídeo existente

## Quando usar

Vídeo já pronto (próprio, de referência ou de concorrente) que precisa
de leitura crítica.

## Quando não usar

Vídeo ainda não existe → skills de produção (`roteiro-audiovisual` em
diante).

## Entradas

Vídeo ou link/descrição do vídeo a analisar.

## Dependências

Nenhuma obrigatória — pode ser standalone.

## Contexto que deve ser carregado

DNA do negócio/posicionamento, se a análise for comparativa.

---

## Workflow

1. Estrutura: como o vídeo abre, desenvolve e fecha.
2. Gancho: o que prende atenção nos primeiros segundos (ou não prende).
3. Ritmo: corte rápido ou contemplativo, coerente com o objetivo.
4. Pontos fortes e fracos, específicos (não "é bom"/"é ruim" genérico).
5. Se for concorrente: o que dá pra aprender sem copiar.
6. Salvar em `<pasta-do-projeto-ativo>/06-audiovisual/analise-video-<nome>.md`.

## Saídas

Análise estruturada com pontos fortes/fracos específicos.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/06-audiovisual/`.

## Regras

- Análise específica, nunca genérica ("bom ritmo" sem dizer por quê).
- Aprender com concorrente é sobre técnica, nunca copiar conteúdo.

## Critérios de qualidade

Cada ponto forte/fraco aponta um momento específico do vídeo.

## Critérios de validação

Análise não inventa dado de performance que não foi fornecido (views,
retenção) — só analisa o que é observável no próprio vídeo.

## Limitações

Sem acesso a métricas reais (views, retenção), a análise é qualitativa
e deve dizer isso.

## Contrato de handoff

Encaminha pra `roteiro-audiovisual` (aprendizado aplicado em produção
futura).

## Exemplos de gatilhos positivos

- "Analisa esse vídeo que fizemos"
- "Por que esse vídeo do concorrente performa bem"

## Exemplos de gatilhos negativos

- "Escreve o roteiro de um vídeo novo" (é `roteiro-audiovisual`)
