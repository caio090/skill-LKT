---
name: integrar-api
description: >
  Planeja e documenta a integração com uma API externa (pagamento,
  WhatsApp, CRM, cardápio digital, etc.): autenticação, endpoints
  usados, tratamento de erro, e adaptador de dados quando a integração
  alimenta um contrato genérico (ex.: cardapio-digital). Use quando o
  usuário pedir "integra com a API de X", "conecta esse sistema no
  WhatsApp Business".
---

# integrar-api — Integração com API externa

## Quando usar

Sistema que precisa conversar com serviço externo via API.

## Quando não usar

Sem credencial/acesso à API real disponível — documentar o plano, mas
não implementar a chamada real sem a credencial (nunca pedir a
credencial diretamente ao usuário fora de canal seguro do próprio
serviço).

## Entradas

Documentação da API externa, objetivo da integração.

## Dependências

`arquitetura-de-software`, `cardapio-digital` (se for adaptador de
contrato de dados).

## Contexto que deve ser carregado

Arquitetura do projeto ativo.

---

## Workflow

1. Definir objetivo da integração (o que precisa entrar/sair).
2. Mapear autenticação exigida pela API (token, OAuth) — nunca
   armazenar credencial em texto no repositório; sempre `.env` ou
   equivalente seguro.
3. Mapear endpoints necessários e formato de dado de cada um.
4. Tratamento de erro: o que fazer se a API estiver fora do ar, retornar
   erro, ou mudar formato.
5. Se a integração alimenta um contrato de dados genérico já existente
   (ex.: `pedido`/`item-pedido` de `cardapio-digital`), documentar o
   adaptador: como o dado da API real vira o formato do schema
   genérico.
6. Salvar em `<pasta-do-projeto-ativo>/07-tecnologia/integracao-<nome>.md`.

## Saídas

Plano de integração documentado (ou implementação, se credencial já
estiver disponível e autorizada).

## Caminho de salvamento

`<pasta-do-projeto-ativo>/07-tecnologia/`.

## Regras

- Nunca gravar segredo/token/senha em arquivo versionado.
- Nunca implementar chamada real sem credencial já configurada e
  autorização explícita do usuário pra essa integração específica.
- Erro de API externa sempre tratado explicitamente, nunca ignorado
  silenciosamente.

## Critérios de qualidade

Todo endpoint documentado tem tratamento de erro definido.

## Critérios de validação

Nenhuma credencial aparece em texto no plano/código.

## Limitações

Não cria conta/credencial no serviço externo — usa o que já existir.

## Contrato de handoff

Encaminha pra `qa` (teste da integração) e `documentar-sistema`.

## Exemplos de gatilhos positivos

- "Integra esse sistema com a API de pagamento"
- "Conecta no WhatsApp Business API"

## Exemplos de gatilhos negativos

- "Me dá a chave de API de tal serviço" (a skill não gera nem solicita
  credencial de terceiro fora do canal oficial do serviço)
