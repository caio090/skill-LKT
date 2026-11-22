# Empresas

Usada nos modos de uso "empresa única" (uma organização) e "grupo/
holding" (várias empresas relacionadas). Cada empresa vive em
`workspaces/empresas/<slug-da-empresa>/`, com contexto e entregas
isolados das demais empresas e da memória geral da instalação.

Em modo empresa única, normalmente existe apenas um workspace aqui
(a própria organização). Em modo grupo, existe um por empresa do grupo,
com `workspaces/projetos-internos/` guardando o que for compartilhado
entre elas.

## Estrutura de cada empresa

```
workspaces/empresas/<slug-da-empresa>/
  WORKSPACE.txt         — identidade, contato, escopo (texto simples)
  INDICE.txt            — lista dos arquivos principais do workspace
  _memoria.json          — memória estruturada (schemas/workspace.schema.json)
  00-contexto/
    entrada/              — arquivos recebidos, ainda não processados
    resumo/                — resumo do que já foi entendido
    fontes/                  — pesquisas e referências usadas
  projetos/
    <slug-do-projeto>/        — ver estrutura de projeto em workspaces/clientes/README.md
```

## Regras

- Nunca misturar informação de uma empresa com a memória geral da
  instalação (`_memoria/` na raiz) ou com a de outra empresa do grupo.
- A skill `novo-projeto` cria essa estrutura automaticamente, sempre
  confirmando antes de criar uma empresa nova.

Nenhuma empresa cadastrada ainda.
