---
name: automatizar-fluxo
description: >
  Transforma uma etapa de processo/funil/pipeline em regra de
  automação, sempre distinguindo sugestão, execução assistida, execução
  com confirmação e execução automática — nunca concede autonomia total
  por padrão. Use quando o usuário disser "automatiza isso", "quero
  que o sistema faça isso sozinho", "cria uma regra pra enviar X quando
  Y acontecer".
---

# automatizar-fluxo — Automação com nível de autonomia explícito

Cria uma regra de automação a partir de um gatilho e uma ação, sempre
declarando o nível de autonomia (0 a 5, ver
`docs/SEGURANCA_E_PERMISSOES.md`) e nunca assumindo o nível mais alto
por padrão.

## Quando usar

- Uma etapa de processo, funil ou pipeline é repetitiva e seguiria uma
  regra clara e segura de automatizar.

## Quando não usar

- Para uma ação única, não recorrente (isso é execução direta, não
  automação).
- Para ação crítica sem que o usuário tenha pedido automação
  explicitamente (excluir, enviar em massa, publicar, mover valor —
  ver lista completa em `docs/SEGURANCA_E_PERMISSOES.md`).

## Entradas

- Gatilho (o que dispara a automação).
- Condição (quando ela deve ou não rodar).
- Ação (o que ela faz).
- Nível de autonomia desejado (perguntar se não for claro — nunca
  assumir o mais alto).

## Dependências

- `schemas/regra-automacao.schema.json`
- `templates/automacao/AUTOMACAO.txt`
- `docs/SEGURANCA_E_PERMISSOES.md`

## Contexto que deve ser carregado

- Automações já existentes no workspace (evitar duplicar ou
  conflitar).

---

## Workflow

### Passo 1 — Classificar o nível de execução (ver `perguntas.txt`)

- **Sugestão** — o agente recomenda, não executa.
- **Execução assistida** — o agente prepara (rascunho, tarefa), não
  publica nem envia.
- **Execução com confirmação** — o agente apresenta a ação específica e
  espera aprovação a cada execução.
- **Execução automática** — roda sozinha, dentro de limite e janela
  definidos, só depois de autorização explícita e registrada.

Nunca conceder autonomia total (execução automática irrestrita) por
padrão — a pergunta inicial sempre assume o nível mais baixo possível
que ainda resolve o problema do usuário.

### Passo 2 — Declarar os campos obrigatórios (ver `fluxo.md`)

Gatilho, condição, ação, nível de autonomia, limite de execução, janela
de tempo, idempotência, tentativas, tratamento de erro, log,
responsável por papel, possibilidade de desativar.

### Passo 3 — Checar se a ação é sempre crítica

Se a ação estiver na lista de ações sempre críticas
(`docs/SEGURANCA_E_PERMISSOES.md`), forçar `requer_confirmacao: true`
mesmo em nível 4, salvo política explícita registrada em contrário.

### Passo 4 — Gerar e salvar (ver `saidas.md`)

Regra salva conforme `schemas/regra-automacao.schema.json`, com log
inicial vazio e status `pausada` até confirmação final de ativação.

### Passo 5 — Validar (ver `validacao.md`)

Nunca ativar automação nova direto em nível 4/5 sem essa confirmação
explícita separada da criação da regra.

---

## Saídas

Regra de automação estruturada e salva, com nível de autonomia
explícito e status inicial `pausada` até ativação confirmada.

## Regras

- Nunca conceder autonomia total por padrão.
- Ações sempre críticas nunca pulam confirmação, mesmo automatizadas.
- Toda automação é desativável e tem log.

## Critérios de qualidade

- Toda regra declara: gatilho, condição, ação, nível, limite, log,
  responsável, tratamento de erro.

## Critérios de validação

- Documento válido contra `schemas/regra-automacao.schema.json`.
- Status inicial é `pausada`, nunca `ativa` direto na criação.

## Limitações

- Não executa a automação nesta skill — só a estrutura e registra;
  ativação é um passo separado, explícito.

## Caminho de salvamento

`workspaces/<tipo>/<slug>/[projetos/<projeto>/]05-operacao/AUTOMACOES/`

## Contrato de handoff

Recebe de `mapear-processo`, `desenhar-funil` ou `configurar-pipeline`
(quando identificam etapa candidata a automação).

## Exemplos de gatilhos positivos

- "Automatiza esse fluxo"
- "Quero que o sistema envie isso sozinho quando X acontecer"

## Exemplos de gatilhos negativos

- "Manda essa mensagem agora" (ação única, execução direta)

Arquivos de apoio desta skill: `perguntas.txt`, `fluxo.md`, `saidas.md`,
`validacao.md`, `exemplos.md`.
