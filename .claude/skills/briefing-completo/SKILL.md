---
name: briefing-completo
description: >
  Coleta e organiza o briefing completo de um projeto ou entrega
  específica (o que precisa, pra quem, prazo, restrições, referências).
  Use quando o usuário pedir "faz o briefing desse projeto", "preciso
  organizar as informações antes de começar".
---

# briefing-completo — Briefing organizado de projeto/entrega

## Quando usar

Início de uma entrega específica dentro de um projeto já existente,
quando as informações ainda estão soltas/incompletas.

## Quando não usar

- Diagnóstico geral do negócio (isso é `diagnostico-negocio`) — briefing
  é sobre uma entrega específica, não o negócio inteiro.

## Entradas

Respostas do cliente/usuário às perguntas abaixo.

## Dependências

`<pasta-do-projeto-ativo>/00-contexto/`, `01-diagnostico/` (se já
existir, reaproveitar em vez de perguntar de novo).

## Contexto que deve ser carregado

Diagnóstico do projeto ativo, se existir.

---

## Workflow

1. **O quê:** o que precisa ser entregue, especificamente.
2. **Pra quem:** público/destinatário dessa entrega.
3. **Por quê:** objetivo que essa entrega serve.
4. **Prazo:** quando precisa estar pronto.
5. **Restrições:** orçamento, ferramentas obrigatórias, o que não pode.
6. **Referências:** exemplos do que o cliente gosta/não gosta.
7. **Critério de aprovação:** como saber que ficou bom.
8. Registrar tudo em `00-contexto/briefing-<entrega>.md`.

## Saídas

`00-contexto/briefing-<entrega>.md`.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/00-contexto/`.

## Regras

- Não inventar restrição ou preferência que não foi dita.
- Se o cliente não souber responder algo, registrar como "a definir",
  não como resposta padrão genérica.

## Critérios de qualidade

As 7 perguntas têm resposta real ou estão marcadas como pendentes.

## Critérios de validação

Briefing revisado com o solicitante antes de iniciar produção baseada
nele.

## Limitações

Não substitui diagnóstico de negócio quando o projeto ainda não tem
contexto nenhum — nesse caso, rodar `diagnostico-negocio` antes.

## Contrato de handoff

Encaminha pro módulo/skill da entrega específica (conteúdo, financeiro,
audiovisual, tecnologia).

## Exemplos de gatilhos positivos

- "Faz o briefing desse vídeo antes de gravar"
- "Organiza as informações desse projeto"

## Exemplos de gatilhos negativos

- "Entende esse negócio do zero" (é `diagnostico-negocio`)
