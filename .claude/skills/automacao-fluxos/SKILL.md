---
name: automacao-fluxos
description: >
  Planeja e documenta automações de fluxo (n8n ou equivalente) e de
  WhatsApp Business: gatilho, passos, integrações envolvidas, tratamento
  de erro. Use quando o usuário pedir "automatiza esse fluxo", "monta
  uma automação no n8n", "configura resposta automática no WhatsApp".
---

# automacao-fluxos — Automação de processos (n8n, WhatsApp)

## Quando usar

Processo repetitivo que pode virar automação (não uma skill do Claude —
uma automação real rodando fora, tipo n8n).

## Quando não usar

Processo que precisa de julgamento humano a cada execução — automatizar
isso esconde erro em vez de resolver.

## Entradas

Descrição do processo, ferramentas disponíveis (n8n, WhatsApp Business
API, outras).

## Dependências

`criar-sop` (se o processo já estiver documentado), `integrar-api`.

## Contexto que deve ser carregado

Ferramentas já usadas pelo negócio (`_memoria/ferramentas.md`).

---

## Workflow

1. Definir o gatilho (o que inicia a automação).
2. Passo a passo do fluxo (cada nó/ação do n8n, ou cada regra do
   WhatsApp).
3. Integrações envolvidas (`integrar-api` se houver serviço externo).
4. Tratamento de erro: o que acontece se um passo falhar — nunca deixar
   falha silenciosa numa automação que roda sem supervisão.
5. Definir quando a automação precisa de intervenção humana (não
   automatizar decisão que deveria ser humana).
6. Salvar em `<pasta-do-projeto-ativo>/07-tecnologia/automacao-<nome>.md`.

## Saídas

Fluxo de automação documentado, pronto pra implementar na ferramenta
real.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/07-tecnologia/`.

## Regras

- Toda automação tem tratamento de erro explícito, nunca falha
  silenciosa.
- Não automatizar decisão que exige julgamento humano caso a caso.
- Credenciais de integração nunca em texto no documento — referenciar
  onde ficam guardadas com segurança.

## Critérios de qualidade

Fluxo documentado é implementável direto na ferramenta sem
reinterpretação.

## Critérios de validação

Todo passo tem tratamento de erro definido.

## Limitações

Não implementa a automação na ferramenta real (isso é feito
diretamente na plataforma, ex.: n8n) — documenta o desenho.

## Contrato de handoff

Encaminha pra `integrar-api` (integrações) e `qa` (teste do fluxo).

## Exemplos de gatilhos positivos

- "Automatiza esse fluxo de resposta de lead"
- "Monta uma automação no n8n pra isso"

## Exemplos de gatilhos negativos

- "Isso precisa de julgamento humano toda vez" (não automatizar,
  documentar como processo manual via `criar-sop`)
