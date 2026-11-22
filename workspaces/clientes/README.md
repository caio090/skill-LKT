# Clientes

Cada cliente atendido (modo de uso: agência/consultoria/prestador) vive
em `workspaces/clientes/<slug-do-cliente>/`, com contexto e entregas
isolados dos demais clientes e da memória geral da instalação.

## Estrutura de cada cliente

```
workspaces/clientes/<slug-do-cliente>/
  WORKSPACE.txt         — quem é o cliente, contato, escopo (texto simples)
  INDICE.txt            — lista dos arquivos principais do workspace
  _memoria.json          — memória estruturada (schemas/workspace.schema.json)
  00-contexto/
    entrada/              — arquivos recebidos desse cliente, ainda não processados
    resumo/                — resumo do que já foi entendido
    fontes/                  — pesquisas e referências usadas
  projetos/
    <slug-do-projeto>/        — ver estrutura de projeto abaixo
```

## Estrutura de cada projeto de cliente

```
workspaces/clientes/<slug-do-cliente>/projetos/<slug-do-projeto>/
  PROJETO.md      — objetivo, responsável por papel, prazo, orçamento, indicador, estado
  00-contexto/
  01-diagnostico/
  02-modelagem/
  03-planejamento/
  04-comercial/
  05-operacao/
  06-financeiro-e-projecoes/
  07-entregaveis/
  08-medicao/
  09-relatorios/
  _fontes/          — pesquisas, referências e fontes usadas no projeto
  _historico/        — versões anteriores e decisões do projeto
```

Nem todo projeto usa todas as pastas — a skill `novo-projeto` cria só as
pertinentes ao tipo de projeto (ver `docs/METODO_DE_TRABALHO.md`).

## Regras

- Nunca misturar informação de um cliente com a memória geral da
  instalação (`_memoria/` na raiz) ou com a de outro cliente.
- `arquivos/` na raiz do sistema é só a central geral — arquivos e
  entregas específicas de cliente ficam aqui dentro, não lá.
- A skill `novo-projeto` cria essa estrutura automaticamente, sempre
  confirmando antes de criar um cliente novo.

Nenhum cliente cadastrado ainda.
