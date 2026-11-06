---
name: validar-sistema
description: >
  Roda a validação estrutural do sistema (tools/validar.js) e traduz o
  resultado em linguagem de conversa: o que está certo, o que é problema
  real, o que é aviso, e o que fazer a respeito. Use quando o usuário
  pedir "valida o sistema", "checa se tá tudo certo", "roda o validador",
  "/validar-sistema", ou depois de qualquer alteração estrutural
  (skill nova, pasta renomeada, migração).
---

# validar-sistema — Validação estrutural traduzida

Skill fina: roda `tools/validar.js` e apresenta o resultado de um jeito
que não exige o usuário entender a saída bruta do script.

## Quando usar

- Depois de criar, adaptar ou remover uma skill.
- Depois de qualquer alteração estrutural (renomear pasta, mover
  arquivo, migrar conteúdo de `lkt-plus`/`MazyOS`).
- Quando o usuário só quiser um check-up geral.

## Quando não usar

- Para corrigir os problemas encontrados — esta skill só reporta, nunca
  corrige sozinha. Correção é uma ação separada, decidida com o usuário.

## Entradas

Nenhuma — roda sobre o estado atual do repositório.

## Dependências

- `tools/validar.js`

## Contexto que deve ser carregado

Nenhum arquivo de memória é necessário para esta skill.

---

## Workflow

### Passo 1 — Rodar o validador

```bash
node tools/validar.js
```

Capturar a saída completa (resumo, problemas, avisos).

### Passo 2 — Traduzir o resultado

Não colar a saída bruta sem contexto. Organizar assim:

```
Validação do sistema

Resumo: [N pastas em catalogo/modulos/, N skills válidas, N arquivos lidos]

Problemas (precisam de ação):
- [cada problema, em uma frase, com o caminho do arquivo]
[ou "Nenhum problema encontrado."]

Avisos (vale olhar, não é urgente):
- [cada aviso, em uma frase]
[ou "Nenhum aviso."]
```

Se algum problema for um falso positivo conhecido (ex.: link de exemplo
`[texto](url)` num texto explicativo, ou um padrão de detecção de nome de
pasta intencional dentro de uma skill), sinalizar isso explicitamente em
vez de tratar como problema real:

> "O validador aponta X como link quebrado, mas é só um exemplo de
> markdown no texto — não precisa de correção."

### Passo 3 — Recomendação

Terminar com uma linha de recomendação:

- Se zero problemas: "Sistema validado, nada pra corrigir agora."
- Se houver problemas: listar prioridade (o que resolver primeiro) e
  perguntar se o usuário quer que a correção seja feita agora ou depois.

---

## Saídas

Relatório traduzido do resultado de tools/validar.js, com recomendação de prioridade.

## Critérios de qualidade

- Nenhum problema real é escondido ou minimizado no relatório.
- Falso positivo conhecido é sinalizado como tal, não tratado como problema real.

## Regras

- Nunca editar arquivos para "corrigir" um problema sem o usuário pedir
  explicitamente — esta skill só diagnostica.
- Nunca esconder um problema real pra deixar o resultado bonito.
- Diferenciar claramente problema (bloqueia/quebra algo) de aviso
  (informativo, não urgente).

## Critérios de validação

- A saída sempre reflete exatamente o que `tools/validar.js` reportou —
  nenhum número inventado ou arredondado.

## Limitações

- Só valida o que `tools/validar.js` cobre hoje (YAML, kebab-case, links,
  referências residuais, catálogo desatualizado). Não substitui revisão
  de conteúdo ou de lógica de uma skill.

## Caminho de salvamento

Não gera arquivo novo — é só relatório de conversa. Se o usuário pedir
pra registrar o resultado, isso é `salvar-local`.

## Contrato de handoff

Se houver problemas que o usuário quer corrigir, encaminhar pra edição
direta do arquivo apontado (ou pra skill relacionada, se for uma skill
inteira que precisa de ajuste — ver `docs/catalogo-skills.md`).

## Exemplos de gatilhos positivos

- "Valida o sistema"
- "Checa se tá tudo certo"
- "Roda o validador"

## Exemplos de gatilhos negativos

- "Corrige os problemas que achou" (esta skill só diagnostica, nunca
  corrige sozinha)
