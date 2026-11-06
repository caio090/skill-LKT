---
name: fechar-sessao
description: >
  Encerra o foco no cliente/projeto atual de forma segura: atualiza
  .lkt-system/estado/contexto-ativo.json (limpa cliente/projeto ativo ou troca
  pra outro), sem apagar histórico. Use quando o usuário disser "encerra
  esse projeto por hoje", "muda o foco pro cliente Y", "limpa o contexto
  ativo".
---

# fechar-sessao — Encerramento seguro de contexto ativo

Complementa `salvar-local` (que registra o que foi feito) cuidando
especificamente de `.lkt-system/estado/contexto-ativo.json` — o que
`salvar-local` não faz sozinho.

## Quando usar

Fim de foco num cliente/projeto (não necessariamente fim da sessão de
trabalho inteira), ou troca explícita de contexto.

## Quando não usar

Só quer registrar progresso sem mudar o foco atual → `salvar-local`
sozinho já basta.

## Entradas

Nenhuma obrigatória — ou o próximo cliente/projeto, se for troca.

## Dependências

`.lkt-system/estado/contexto-ativo.json`, `.lkt-system/schemas/contexto-ativo.schema.json`.

## Contexto que deve ser carregado

Estado atual de `contexto-ativo.json`.

---

## Workflow

1. Confirmar se é encerramento (limpar `cliente_ativo`/`projeto_ativo`/
   `projeto_interno_ativo` pra `null`) ou troca (definir o próximo).
2. Se houver pendência não registrada no projeto que está saindo de
   foco, sugerir rodar `salvar-local` antes de trocar.
3. Atualizar `contexto-ativo.json` conforme o schema — nunca gravar
   segredo.
4. Confirmar a mudança:
   > "Contexto ativo agora: [novo cliente/projeto, ou 'nenhum']."

## Saídas

`.lkt-system/estado/contexto-ativo.json` atualizado.

## Caminho de salvamento

`.lkt-system/estado/contexto-ativo.json`.

## Regras

- Nunca apagar `_memoria/`, `decisoes.md` ou qualquer histórico — só
  atualiza o ponteiro de foco atual.
- Nunca gravar segredo/token em `contexto-ativo.json`.
- Sempre sugerir `salvar-local` antes de trocar de foco, se houver
  trabalho não registrado.

## Critérios de qualidade

`contexto-ativo.json` sempre válido contra o schema depois da operação.

## Critérios de validação

Nenhum dado de `_memoria/` é apagado por esta skill.

## Limitações

Não decide sozinha se há trabalho pendente não registrado — pergunta
ao usuário quando não tem certeza.

## Contrato de handoff

`salvar-local` (se houver pendência de registro antes de trocar) e
`abrir` (na próxima sessão, lê o novo contexto).

## Exemplos de gatilhos positivos

- "Encerra o foco nesse projeto por hoje"
- "Muda o contexto ativo pro cliente Y"

## Exemplos de gatilhos negativos

- "Salva o progresso mas continua no mesmo projeto" (é `salvar-local`
  sozinho)
