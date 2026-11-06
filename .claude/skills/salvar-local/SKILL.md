---
name: salvar-local
description: >
  Fecha uma sessão de trabalho: atualiza memória, decisões e pendências,
  atualiza índices e catálogo, registra o que foi criado/modificado, gera
  um resumo da sessão, roda o validador e sugere (mas nunca executa
  sozinha) um commit local. Nunca faz push, nunca configura remoto, nunca
  publica nada. Use quando o usuário disser "salvar", "salva o progresso",
  "fecha a sessão", "/salvar-local", ou pedir pra registrar o que foi
  feito antes de parar.
---

# salvar-local — Fechamento de sessão (sempre local)

Substitui a antiga skill `salvar`, que fazia commit + push automático
pro GitHub. **Essa skill nunca toca em remoto.** Push, configuração de
remoto e publicação são sempre decisão manual do usuário, fora desta
skill.

## Quando usar

- Fim de uma sessão de trabalho, ou quando o usuário pedir explicitamente
  pra "salvar"/"registrar o progresso".

## Quando não usar

- Para publicar conteúdo (site, redes sociais) → isso é `aprovar-post`,
  que também nunca dá push sozinha.
- Para dar push de verdade → o usuário faz isso manualmente (`git push`),
  fora de qualquer skill. Esta skill no máximo sugere a mensagem de
  commit local.

## Entradas

Nenhuma obrigatória — opera sobre o estado atual do workspace e da
conversa.

## Dependências

- `tools/validar.js`
- `_memoria/decisoes.md`, `_memoria/pendencias.md`, `_memoria/aprendizados.md`
- `docs/catalogo-skills.md`, `docs/roteamento.md`, `arquivos/INDICE.md`
- Memória do cliente/projeto ativo, se a sessão foi sobre um deles

## Contexto que deve ser carregado

- Estado atual de `_memoria/pendencias.md` e `_memoria/decisoes.md`
- `git status` (se houver repositório Git local)

---

## Workflow

### Passo 1 — Levantar o que mudou na sessão

Revisar o que foi feito na conversa: arquivos criados, arquivos
modificados, decisões tomadas, pendências abertas ou resolvidas.

### Passo 2 — Atualizar memória

- Se alguma correção ou preferência permanente surgiu na sessão e ainda
  não foi salva, perguntar se deve ser registrada agora (seguindo a regra
  de "Aprender com correções" do `CLAUDE.md`).
- Atualizar `_memoria/decisoes.md` com decisões novas (uma linha clara
  por decisão, sem reformatar o arquivo inteiro).
- Atualizar `_memoria/pendencias.md`: marcar o que foi resolvido, adicionar
  o que ficou em aberto.
- Se algo reaproveitável foi descoberto, registrar em
  `_memoria/aprendizados.md`.

### Passo 3 — Atualizar índices e catálogo

- Se algum arquivo novo entrou em `arquivos/entrada/` ou foi processado,
  conferir que `arquivos/INDICE.md` está atualizado (ou o equivalente
  dentro de `workspaces/clientes/<cliente>/arquivos/` se for por cliente).
- Se alguma skill foi criada, adaptada ou removida na sessão, conferir
  que `docs/catalogo-skills.md` e `docs/roteamento.md` refletem isso.

### Passo 4 — Rodar o validador

Rodar `node tools/validar.js` e reportar o resultado (problemas e
avisos), sem corrigir nada automaticamente além do que já foi decidido
na sessão.

### Passo 5 — Registrar contexto ativo

Atualizar `.lkt-system/estado/contexto-ativo.json`:
- `ultima_sessao`: data/hora atual (ISO 8601).
- `arquivos_recentes`: adicionar os arquivos criados/modificados desta
  sessão no topo da lista (mais recente primeiro), mantendo no máximo
  ~20 entradas.
- `decisoes_recentes`: adicionar um resumo de uma linha por decisão nova
  registrada no Passo 2, no topo da lista, mantendo no máximo ~20
  entradas.

Não alterar `cliente_ativo`/`projeto_ativo`/`projeto_interno_ativo` aqui
— isso é responsabilidade de `novo-projeto` (ou de uma futura
`fechar-sessao`, se for criada).

### Passo 6 — Resumo da sessão

Mostrar, sem esconder nada:

```
Resumo da sessão

Arquivos criados: [lista]
Arquivos modificados: [lista]
Decisões registradas: [lista ou "nenhuma"]
Pendências abertas: [lista ou "nenhuma"]
Validação: [N problemas, N avisos]
```

### Passo 7 — Git (se houver repositório local)

Rodar `git status`. Se não houver mudanças, informar e parar — nada a
salvar.

Se houver mudanças, mostrar o `git status` resumido e **sugerir** uma
mensagem de commit (baseada no resumo do Passo 6). Perguntar:

> "Quer que eu faça o commit local dessas mudanças com essa mensagem?
> (isso não dá push nem mexe em remoto — fica só no seu histórico local)"

Só rodar `git add` + `git commit` se o usuário confirmar explicitamente
nesta pergunta. Nunca configurar `git remote`, nunca rodar `git push`,
nunca sugerir publicar em lugar nenhum.

Se o usuário perguntar sobre push ou GitHub, responder que isso é uma
ação manual dele — a skill não faz e não configura isso.

---

## Saídas

Resumo da sessão, memória/índices atualizados, contexto ativo registrado, e commit local (se autorizado) — nunca push.

## Critérios de qualidade

- Resumo da sessão nunca omite o que foi feito, mesmo que pouco.
- Commit só acontece com confirmação explícita nesta execução.

## Regras

- **Nunca fazer push.**
- **Nunca configurar remoto** (`git remote add`, `gh repo create`, etc.).
- **Nunca publicar nada** (site, post, deploy).
- **Nunca fazer commit sem confirmação explícita** do usuário nesta
  execução — mesmo que o usuário tenha autorizado commit numa sessão
  anterior, perguntar de novo.
- **Nunca enviar dados para serviço externo** sem autorização explícita.
- Não reformatar arquivos de memória inteiros — só adicionar/editar a
  linha relevante.
- Se não houver nada para salvar, dizer isso diretamente, sem inventar
  resumo.

## Critérios de validação

- Nenhum comando de rede (`push`, `remote add`, chamada a API externa) é
  executado por esta skill em nenhuma circunstância.
- Commit local só acontece após confirmação explícita no Passo 7.
- `docs/catalogo-skills.md` e `docs/roteamento.md` nunca ficam
  desatualizados em relação às skills existentes após esta skill rodar.

## Limitações

- Não decide sozinha o que é uma "decisão permanente" vs. contexto
  pontual — na dúvida, pergunta.
- Não substitui `aprovar-post` para publicação de conteúdo.

## Caminho de salvamento

Edita arquivos existentes em `_memoria/`, `docs/`, `arquivos/INDICE.md`
(ou equivalentes dentro de `workspaces/clientes/<cliente>/`) — não cria pasta nova
própria.

## Contrato de handoff

Encerra a sessão. Não encadeia automaticamente com nenhuma outra skill.

## Exemplos de gatilhos positivos

- "Salvar"
- "Salva o progresso"
- "Fecha a sessão"

## Exemplos de gatilhos negativos

- "Publica esse post" (é `aprovar-post`, que também nunca dá push)
- "Dá push no GitHub" (esta skill nunca dá push — só comita local com
  confirmação explícita)
