---
name: rotear-ambiente
description: >
  Decide ONDE continuar uma tarefa técnica — ambiente local/agente de
  código, chat do editor, Codex Web/GitHub, ou deploy — a partir do
  tipo de mudança, do escopo de arquivos e do estado do repositório.
  Use quando o trabalho for técnico e não for óbvio se deve continuar
  no editor, num agente local ou remoto, e gere um handoff sempre que
  recomendar troca de ambiente.
---

# rotear-ambiente — Roteamento de tarefa técnica para ambiente de trabalho

`rotear-tarefa` decide qual skill usar; `rotear-ambiente` decide **onde**
executar — nenhuma ferramenta é o ambiente único, o trabalho é híbrido.

## Quando usar

Tarefa técnica cujo melhor lugar de execução não é óbvio: refatoração
grande, revisão de PR, migração de banco de dados, ajuste pontual num
arquivo aberto, ou qualquer momento em que o usuário pergunte "onde eu
continuo isso".

## Quando não usar

- Ajuste pequeno e óbvio no arquivo já aberto no editor — só fazer,
  sem rotear.
- Tarefa não técnica (estratégia, conteúdo, financeiro) — não se
  aplica.

## Entradas

Descrição da tarefa técnica e o estado atual do repositório (via
`preflight-ambiente`, se ainda não tiver rodado nesta sessão).

## Dependências

`preflight-ambiente` (estado do ambiente), `templates/operacao/HANDOFF.md`.

## Contexto que deve ser carregado

Nenhuma memória de negócio — decisão puramente técnica/operacional.

---

## Workflow

### Passo 1 — Classificar a tarefa

- Alteração ligada aos arquivos já abertos, incremental, correção
  pontual, teste local → **chat/agente do VS Code**.
- Leitura ampla do repositório, alteração em muitos arquivos, script,
  migration, auditoria, uso de MCP local → **ambiente local/agente de
  código**.
- Revisão de PR, auditoria remota, continuação de código já publicado no
  GitHub → **Codex Web/GitHub**.
- Projeto web pronto pra ir ao ar → sequência **local → Git → repositório
  remoto → deploy**.

### Passo 2 — Verificar pré-condição

Antes de recomendar GitHub ou deploy, confirmar (via
`preflight-ambiente`) que existe remote configurado e autenticação
válida — nunca supor que existe.

### Passo 3 — Decidir e explicar

Registrar tarefa, ambiente recomendado, motivo, skills envolvidas,
arquivos afetados, estado do Git e integrações necessárias.

### Passo 4 — Gerar handoff quando trocar de ambiente

Se a recomendação muda o ambiente em relação a onde a sessão está
rodando agora, preencher `templates/operacao/HANDOFF.md` antes de
encerrar, pra continuidade sem repetir contexto.

## Saídas

```
tarefa:
ambiente_recomendado:
motivo:
skills:
arquivos:
estado_git:
integracoes_necessarias:
handoff:
```

## Caminho de salvamento

Handoff gerado em `prompts/arquivo/` junto ao registro de prompt
correspondente (ver `registrar-prompt`), quando a tarefa fizer parte da
numeração de prompts.

## Regras

- Nunca recomendar GitHub ou deploy sem remote/autenticação confirmados
  nesta sessão.
- Sempre gerar handoff explícito ao recomendar troca de ambiente — nunca
  assumir que o próximo ambiente "vai saber" o contexto.

## Critérios de qualidade

A recomendação de ambiente é justificada pelo tipo real da tarefa, não
por preferência genérica de ferramenta.

## Critérios de validação

Seguir a recomendação e o handoff gerado permite continuar a tarefa sem
precisar repetir perguntas já respondidas nesta sessão.

## Limitações

Depende do `preflight-ambiente` estar atualizado — se o ambiente mudou
desde o último preflight, rodar de novo antes de rotear.

## Contrato de handoff

Recebe de `preflight-ambiente`; entrega pra `registrar-prompt` (quando a
tarefa vira prompt numerado) e para a skill técnica escolhida.

## Exemplos de gatilhos positivos

- "Onde eu continuo isso, aqui ou no Codex Web?"
- Início de uma refatoração grande que cruza dezenas de arquivos.

## Exemplos de gatilhos negativos

- Correção de uma linha no arquivo já aberto — só fazer.
- Tarefa não técnica.
