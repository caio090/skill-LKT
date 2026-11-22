# Projetos internos

Iniciativas da própria instalação (não são entregas para cliente
externo, nem uma empresa/cliente com workspace próprio) vivem em
`workspaces/projetos-internos/<slug-do-projeto>/`, direto — sem
workspace por cima, porque não há cliente externo nem empresa associada.

Em modo grupo, esta pasta guarda projetos compartilhados entre as
empresas do grupo (não pertencem a uma única empresa).

```
workspaces/projetos-internos/<slug-do-projeto>/
  PROJETO.md
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
  _fontes/
  _historico/
```

Nem todo projeto usa todas as pastas — a skill `novo-projeto` cria só as
pertinentes ao tipo de projeto (ver `docs/METODO_DE_TRABALHO.md`).

A skill `novo-projeto` cria essa estrutura quando o projeto é
identificado como iniciativa interna (não cliente, não empresa).

Nenhum projeto interno cadastrado ainda.
