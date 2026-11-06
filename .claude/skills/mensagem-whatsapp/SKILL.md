---
name: mensagem-whatsapp
description: >
  Escreve mensagens de WhatsApp (atendimento, follow-up, campanha,
  confirmação) no tom certo pro canal — curtas, diretas, sem formalidade
  de email. Use quando o usuário pedir "escreve essa mensagem de
  WhatsApp", "manda um follow-up pelo whats".
---

# mensagem-whatsapp — Mensagem de WhatsApp

## Quando usar

Qualquer texto que vai sair por WhatsApp — atendimento, follow-up
comercial, aviso, campanha.

## Quando não usar

Email formal → `email-profissional` (tom e estrutura diferentes).

## Entradas

Contexto (pra quem, objetivo da mensagem).

## Dependências

`_memoria/preferencias.md`.

## Contexto que deve ser carregado

Tom de voz do projeto/cliente ativo.

---

## Workflow

1. Objetivo da mensagem (uma ação só pedida por vez).
2. Escrever curto — WhatsApp não é email, frases longas cansam.
3. Sem formalidade excessiva ("Prezado", "Vimos por meio desta") nem
   informalidade fora do tom da marca.
4. Emoji só se o tom de voz da marca já usa.
5. Encaminhar pra `texto-natural-pt-br` antes de entregar.

## Saídas

Mensagem pronta pra enviar.

## Caminho de salvamento

Não gera arquivo — devolve o texto. Se for parte de campanha, registrar
em `<pasta-do-projeto-ativo>/04-marketing/`.

## Regras

- Uma ação pedida por mensagem.
- Nunca soar como email colado no WhatsApp.

## Critérios de qualidade

Mensagem lida em poucos segundos, sem parecer robótica.

## Critérios de validação

Nenhuma linguagem formal de email presente.

## Limitações

Não substitui automação de WhatsApp Business (isso é
`whatsapp-automacao`, módulo de tecnologia).

## Contrato de handoff

`texto-natural-pt-br` (acabamento).

## Exemplos de gatilhos positivos

- "Escreve essa mensagem de follow-up pro WhatsApp"
- "Manda um aviso pro cliente pelo whats"

## Exemplos de gatilhos negativos

- "Escreve um email formal pro fornecedor" (é `email-profissional`)
