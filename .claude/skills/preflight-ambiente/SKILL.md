---
name: preflight-ambiente
description: >
  Levanta o estado real do ambiente técnico antes de um projeto técnico
  ou ao entrar num repositório desconhecido: Git, branch, remote,
  framework, Node, extensões do editor, e quais MCPs estão de fato
  configurados (nunca por suposição). Use no início de um projeto
  técnico, ao abrir um repositório pela primeira vez, ou quando o
  usuário perguntar "o que já está configurado aqui".
---

# preflight-ambiente — Levantamento real do ambiente técnico

## Quando usar

Início de projeto técnico (site, app, sistema, integração) ou primeira
sessão num repositório ainda não mapeado. Também quando o usuário pedir
diretamente "verifica o ambiente" ou "o que tá instalado aqui".

## Quando não usar

- Projeto não técnico (estratégia, conteúdo, financeiro puro) — não
  forçar Git, deploy ou MCP onde não faz sentido.
- Sessão já mapeada na mesma pasta, sem mudança de ambiente — não repetir
  o levantamento completo, só o que for relevante pra tarefa atual.

## Entradas

Caminho do repositório/pasta de trabalho ativo.

## Dependências

`docs/PREFLIGHT.md` (lista completa do que verificar e como classificar),
`.lkt-system/capabilities.json` (matriz de capacidades a atualizar com o
resultado).

## Contexto que deve ser carregado

Nenhuma memória de negócio — este levantamento é técnico, não depende de
marca ou estratégia.

---

## Workflow

### Passo 1 — Ambiente do sistema

Sistema operacional, shell, Node/npm (ou gerenciador equivalente), Git
instalado.

### Passo 2 — Estado do repositório

`.git` existe? Branch atual, alterações pendentes, remote configurado
(nome e URL, nunca assumir GitHub por padrão), `.gitignore`, `README`,
`package.json`, lockfile, framework detectado (ler `package.json`/config,
nunca advinhar pelo nome da pasta), banco de dados declarado, deploy
declarado, variáveis de ambiente esperadas (nomes, nunca valores).

### Passo 3 — Editor (VS Code ou equivalente)

Ler `.vscode/extensions.json`, `.vscode/settings.json`,
`.vscode/tasks.json`, `.vscode/launch.json` quando existirem. Se
`code --list-extensions` estiver disponível no ambiente, usar como fonte
adicional.

**Nunca confundir extensão de editor com MCP.** Registrar como extensão
de editor, não MCP: temas de ícone, pacote de idioma, Live Server, Live
Preview, dashboards do editor, extensão do Codex, extensão do GitHub.

### Passo 4 — MCP realmente configurado

Um MCP só é registrado como configurado por evidência real (arquivo de
configuração do MCP, comando oficial de listagem retornando o servidor,
ou chamada de ferramenta bem-sucedida) — nunca por o usuário ter
mencionado o nome antes. Playwright, por exemplo, pode existir como
biblioteca de projeto, extensão de editor ou MCP — verificar qual dos
três está de fato presente, sem assumir.

### Passo 5 — Integrações externas

Para cada integração citada pelo usuário ou encontrada em configuração
(deploy, CRM, WhatsApp Business, pagamento, cardápio digital):
classificar segundo `.lkt-system/capabilities.json` — nunca marcar
`REAL` sem teste ou evidência concreta nesta sessão.

### Passo 6 — Consolidar e atualizar a matriz

Escrever/atualizar `.lkt-system/capabilities.json` com o que foi
confirmado, incluindo `last_verified` com a data desta checagem.

## Saídas

Relatório do ambiente (Git, editor, MCPs, integrações) e
`.lkt-system/capabilities.json` atualizado.

## Caminho de salvamento

`.lkt-system/capabilities.json` (matriz), relatório apresentado
diretamente ao usuário (não gera arquivo de relatório separado por
padrão).

## Regras

- Nunca marcar uma integração como funcionando sem teste real na sessão
  atual.
- Nunca tratar extensão de editor como MCP, nem o inverso.
- Nunca presumir GitHub, Vercel ou qualquer provedor específico — usar o
  que estiver de fato configurado no repositório.

## Critérios de qualidade

Todo item da matriz de capacidades tem `last_verified` e estado
(`REAL`/`PARTIAL`/`DEMO`/`COMING_SOON`/`NOT_IMPLEMENTED`/`UNAVAILABLE`)
condizente com a evidência encontrada nesta sessão.

## Critérios de validação

Repetir a checagem de uma integração marcada `REAL` deveria reproduzir o
mesmo resultado (mesma credencial, mesmo teste).

## Limitações

Detecção depende do que o ambiente expõe nesta sessão — MCP configurado
fora do escopo acessível pode não aparecer; reportar como não
confirmado, nunca como ausente com certeza.

## Contrato de handoff

Alimenta `rotear-ambiente` (decide onde continuar) e qualquer skill
técnica que dependa de Git/deploy/integração
(`arquitetura-de-software`, `integrar-api`, `qa`).

## Exemplos de gatilhos positivos

- Primeira sessão num repositório novo, antes de codificar.
- "O que já está configurado nesse projeto?"

## Exemplos de gatilhos negativos

- Projeto de estratégia ou conteúdo sem componente técnico.
- Segunda tarefa técnica na mesma sessão, ambiente já mapeado e sem
  mudança relevante.
