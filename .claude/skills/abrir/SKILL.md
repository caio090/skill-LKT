---
name: abrir
description: >
  Abre uma sessão de trabalho carregando a memória do negócio (empresa,
  preferências, estratégia, marca) e devolve um resumo curto pro usuário.
  Se a sessão for sobre um cliente ou projeto específico, carrega também
  a memória dele. Use quando o usuário disser "abrir", "começar o dia",
  "abrir sessão" ou no primeiro turno depois de rodar "instalar".
---

# abrir — Abertura de sessão

Curto e direto. O objetivo é carregar contexto e devolver uma síntese de
uma frase pra o usuário começar a trabalhar.

## Workflow

1. Ler `.lkt-system/estado/contexto-ativo.json` (se existir) para saber cliente/
   projeto ativo, última sessão e decisões recentes.

2. Ler, em ordem:
   - `_memoria/empresa.md`
   - `_memoria/preferencias.md`
   - `_memoria/estrategia.md`
   - `_memoria/marca.md` (só pra saber se está preenchida ou em branco)

3. Se o pedido do usuário (ou o `contexto-ativo.json`) já indicar um
   cliente ou projeto específico, ler também:
   - `workspaces/clientes/<cliente>/CLIENTE.md` e o que houver em
     `workspaces/clientes/<cliente>/_memoria/`
   - `workspaces/clientes/<cliente>/projetos/<projeto>/PROJETO.md` (ou
     `workspaces/projetos-internos/<projeto>/PROJETO.md`)

4. Se algum dos três primeiros (empresa, preferências, estratégia)
   estiver em branco (placeholder), responder:
   > "Vi que `_memoria/<arquivo>.md` ainda não foi preenchido. Quer rodar
   > a instalação agora?"
   E parar.

5. Se tudo estiver preenchido, devolver UMA mensagem curta no formato:

```
[Nome do negócio] — [o que faz em 5-8 palavras]
Foco atual: [prioridade da estratégia, em uma frase]
Tom: [resumo de 3-4 palavras do tom de voz]
[Se contexto-ativo.json tiver cliente/projeto: Cliente/projeto: [nome] — [estado do PROJETO.md]]

Pronto. O que vamos fazer?
```

6. Não listar quais arquivos foram lidos. Não confirmar leitura. Só usar
   o contexto.

## Quando usar

- Início de sessão de trabalho, ou primeiro turno depois de `instalar`.

## Quando não usar

- No meio de uma sessão já com contexto carregado — rodar de novo é
  redundante.

## Entradas

Nenhuma — lê o estado atual de `_memoria/` e do contexto ativo.

## Dependências

`_memoria/empresa.md`, `preferencias.md`, `estrategia.md`, `marca.md`,
`.lkt-system/estado/contexto-ativo.json`.

## Contexto que deve ser carregado

Memória geral e, se houver cliente/projeto ativo, a memória dele.

## Saídas

Resumo curto (poucas linhas) do negócio, foco atual e tom — ou aviso de
memória em branco pedindo instalação.

## Caminho de salvamento

Não gera arquivo — só carrega contexto pra conversa.

## Critérios de qualidade

- Resposta cabe em poucas linhas, nunca um despejo de tudo que foi lido.

## Critérios de validação

- Memória em branco é detectada e comunicada, nunca ignorada
  silenciosamente.

## Limitações

- Não decide o que fazer na sessão — só carrega contexto pra decisão
  humana.

## Contrato de handoff

Encaminha pra qualquer skill que o pedido do usuário indicar em
seguida.

## Regras

- Resposta tem que caber em poucas linhas no terminal.
- Não fazer perguntas além de "o que vamos fazer?" (exceto o caso de
  memória em branco do passo 3).
- Se `_memoria/marca.md` estiver em branco, não mencionar — só vira
  problema quando alguma skill visual for chamada.

## Exemplos de gatilhos positivos

- "Abrir"
- "Começar o dia"
- Primeiro turno de uma sessão nova, depois de "instalar" já ter rodado

## Exemplos de gatilhos negativos

- Pedido de trabalho específico já no primeiro turno, sem carregar
  contexto (rodar `abrir` antes, não em vez de)
