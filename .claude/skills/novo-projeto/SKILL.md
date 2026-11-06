---
name: novo-projeto
description: >
  Cria um workspace novo (cliente, empresa ou projeto interno, conforme
  o modo de uso da instalação) ou um projeto dentro de um workspace já
  existente, com a estrutura padronizada e um PROJETO.md registrando
  objetivo, responsável por papel, prazo, orçamento, indicador e estado.
  Classifica o tipo de projeto (empresa, cliente, campanha, site,
  landing page, evento, produto, serviço, infoproduto, financeiro,
  comercial, conteúdo, implantação de sistema, logístico, interno) e
  cria só as pastas pertinentes a esse tipo — nunca a estrutura inteira
  por padrão. Verifica se o workspace já existe antes de criar pasta
  nova, e nunca começa direto pela produção de conteúdo. Use quando o
  usuário disser "novo projeto", "novo cliente", "nova empresa",
  "começar projeto pra X", "preciso estruturar um trabalho novo", ou
  similar.
---

# novo-projeto — Workspace e projeto novos, com estrutura padronizada

Cria a estrutura de pastas de um workspace (cliente, empresa ou
iniciativa interna, conforme o modo de uso — ver `docs/MODOS_DE_USO.md`)
e/ou de um projeto dentro dele, junto com o `PROJETO.md` que registra o
essencial pra acompanhar o trabalho. Nunca cria conteúdo (posts,
roteiros, campanhas) nesta skill — isso vem depois, através do
diagnóstico e do módulo correto.

## Quando usar

- Início de um workspace novo (cliente, empresa ou projeto interno).
- Início de um projeto novo dentro de um workspace já existente.

## Quando não usar

- Para adicionar uma entrega dentro de um projeto que já existe — usar a
  pasta do projeto existente direto (ex.: `04-comercial/`), sem recriar
  estrutura.
- Para começar a produzir conteúdo sem contexto — mesmo que o usuário
  peça direto ("faz um carrossel pro cliente novo X"), se o workspace/
  projeto ainda não existir, passar primeiro por esta skill antes de
  produzir qualquer peça.

## Entradas

- Nome do workspace (cliente, empresa) ou do projeto.
- Modo de uso da instalação (`.lkt-system/estado/contexto-ativo.json`,
  campo `modo_de_uso`) — decide se o workspace vai para
  `workspaces/clientes/`, `workspaces/empresas/` ou
  `workspaces/projetos-internos/`.
- Se é workspace novo, workspace existente, ou projeto interno.
- Objetivo principal.
- Classificação do projeto: empresa, cliente, campanha, site, landing
  page, evento, produto, serviço, infoproduto, projeto financeiro,
  comercial, de conteúdo, implantação de sistema, logístico, ou
  interno.
- Se o projeto precisa de processo, fluxo de trabalho, funil, pipeline,
  campanha, jornada, automação, página de oferta e/ou projeção (ver
  `knowledge/projetos/ONTOLOGIA_PROCESSOS_FUNIS_PIPELINES.md`) — isso
  decide quais pastas e skills entram em cena depois do diagnóstico.
- Responsável por papel, prazo e orçamento (se já souber).

## Dependências

- `workspaces/clientes/`, `workspaces/empresas/`, `workspaces/projetos-internos/`
  (raízes) e seus respectivos `README.md`
- `templates/workspace/` e `templates/projeto/PROJETO.md` (modelos-base
  — os blocos abaixo já são cópia deles; se os templates mudarem,
  atualizar aqui também)
- `_memoria/sistema/empresa.md`, `_memoria/sistema/preferencias.md`
  (memória geral)
- `.lkt-system/estado/contexto-ativo.json` (atualizado no Passo 7)
- `catalogo/modulos/diagnostico` e `.claude/skills/diagnostico-empresarial`
  (próximo passo depois da estrutura criada)
- `schemas/workspace.schema.json` e `schemas/projeto.schema.json`
  (contrato de dados de `_memoria.json` e `PROJETO.md`)

## Contexto que deve ser carregado

- Memória geral (`_memoria/sistema/empresa.md`, `preferencias.md`,
  `estrategia.md`)
- Se o workspace já existir: `WORKSPACE.txt` e `_memoria.json` dele

---

## Workflow

### Passo 1 — Entrevista inicial

Perguntar, uma coisa por vez:

1. "Qual o nome do cliente, empresa ou projeto?"
2. "É um workspace novo, um workspace que já existe, ou um projeto
   interno da instalação?"
3. "Qual o objetivo principal? (uma frase)"
4. "Que tipo de projeto é esse — empresa, cliente, campanha, site,
   landing page, evento, produto, serviço, infoproduto, financeiro,
   comercial, de conteúdo, implantação de sistema, logístico, ou
   interno?" (pode ser mais de um tipo)
5. "Quem é o responsável por papel, qual o prazo e (se já souber) o
   orçamento?"

Se alguma resposta não vier ainda, seguir sem ela e registrar como
pendente no `PROJETO.md` (não travar a criação por falta de orçamento ou
prazo definido).

### Passo 2 — Verificar se o workspace já existe

Checar a raiz certa conforme o modo de uso: `workspaces/clientes/<slug>/`
(agência), `workspaces/empresas/<slug>/` (empresa única ou grupo) ou
`workspaces/projetos-internos/<slug>/` (iniciativa própria da
instalação, sem cliente externo associado). Gerar o slug (minúsculas,
sem acento, espaço vira hífen).

- **Se já existir:** carregar `WORKSPACE.txt` e `_memoria.json` dele —
  não recriar nada, só adicionar o projeto novo dentro de `projetos/`.
- **Se não existir e for workspace novo:** **perguntar antes de criar**:
  > "Não encontrei '<nome>' ainda. Confirma que é pra criar a pasta
  > `workspaces/<raiz>/<slug>/` agora?"
  Só criar depois de confirmação explícita.
- **Se for projeto interno da instalação:** vai direto em
  `workspaces/projetos-internos/<slug-do-projeto>/`, sem workspace
  separado por cima.

### Passo 3 — Criar o workspace (só se novo e confirmado)

```
workspaces/<raiz>/<slug>/
  WORKSPACE.txt
  INDICE.txt
  _memoria.json
  00-contexto/
    entrada/
    resumo/
    fontes/
  projetos/
```

`WORKSPACE.txt` (texto simples, legível por quem não é técnico):

```
<Nome do workspace>

Criado em: <data>
Tipo: <cliente | empresa | grupo>

SOBRE
[o que o workspace faz, em 1-2 frases — preencher no diagnóstico se
ainda não souber]

CONTATO
[nome do papel, canal de contato — preencher quando souber]

ESCOPO GERAL
[o que a instalação atende aqui, em termos amplos]

PROJETOS
- <slug-do-projeto> — criado em <data>
```

`_memoria.json` (schema completo em `schemas/workspace.schema.json`):

```json
{
  "id": "<slug>",
  "tipo": "cliente | empresa | grupo",
  "criado_em": "<data ISO>",
  "identidade": {},
  "objetivos": [],
  "publicos": [],
  "produtos": [],
  "servicos": [],
  "canais": [],
  "papeis": [],
  "projetos": [],
  "decisoes": [],
  "hipoteses": [],
  "pendencias": [],
  "riscos": [],
  "entregaveis": [],
  "metricas": [],
  "fontes": [],
  "ultima_atualizacao": "<data ISO>"
}
```

`INDICE.txt`: lista vazia inicialmente, atualizada pela skill
`organizar-arquivos` conforme material chega.

### Passo 4 — Classificar o projeto e escolher só as pastas pertinentes

Local: `workspaces/<raiz>/<slug>/projetos/<slug-do-projeto>/` (workspace
com projetos) ou `workspaces/projetos-internos/<slug-do-projeto>/`
(interno, direto).

Estrutura completa de referência (nunca criar tudo por padrão — só o
pertinente à classificação do Passo 1):

```
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

Guia de seleção por tipo (ponto de partida — ajustar ao caso real):

- **Site, landing page, evento, campanha:** contexto, diagnóstico,
  modelagem, planejamento, comercial, operação, entregáveis, medição,
  relatórios.
- **Financeiro:** contexto, diagnóstico, planejamento,
  financeiro-e-projecoes, medição, relatórios (sem comercial/operação
  se não fizer parte do escopo).
- **Logístico:** contexto, diagnóstico, planejamento, operação,
  financeiro-e-projecoes (se houver custo), entregáveis, medição,
  relatórios.
- **Produto, serviço, infoproduto:** contexto, diagnóstico, modelagem,
  planejamento, comercial, financeiro-e-projecoes, entregáveis,
  medição, relatórios.
- **Empresa/cliente (diagnóstico geral, sem projeto específico ainda):**
  contexto, diagnóstico, modelagem, planejamento.
- **Implantação de sistema:** contexto, diagnóstico, planejamento,
  operação, entregáveis, medição, relatórios.

`_fontes/` e `_historico/` são sempre criadas (pesquisas/referências
usadas e histórico de decisões do projeto).

`PROJETO.md`:

```markdown
# <Nome do projeto>

> Criado em <data>. Workspace: <nome> (`workspaces/<raiz>/<slug>/`) |
> Tipo de projeto: <classificação do Passo 1>

## Objetivo

<resposta da pergunta 3>

## Entregas previstas

- <entrega 1>
- <entrega 2>
- ...

## Responsável por papel

<papel: nome ou "a definir" — nunca só um nome sem o papel>

## Prazo

<data, ou "a definir">

## Orçamento

<valor, ou "a definir">

## Indicador de sucesso

<métrica que vai dizer se o projeto deu certo — perguntar se não veio
na entrevista: "como vamos saber que esse projeto funcionou?">

## Modelo aplicável

<processo | fluxo de trabalho | funil | pipeline | campanha | jornada |
nenhum ainda — ver knowledge/projetos/ONTOLOGIA_PROCESSOS_FUNIS_PIPELINES.md>

## Estado

`em contexto` — projeto criado, diagnóstico ainda não rodou.

## Histórico de estado

- <data> — criado, estado inicial: em contexto
```

Estados possíveis pra usar em `## Estado` ao longo do projeto: `em
contexto` → `em diagnóstico` → `em execução` → `em entrega` →
`concluído` / `pausado` / `cancelado`. Atualizar essa linha (e adicionar
uma entrada no histórico) sempre que o estado mudar de verdade — não a
cada sessão.

### Passo 5 — Próximo passo (nunca começar por conteúdo)

Depois de criar a estrutura, o próximo passo é sempre o diagnóstico
(`.claude/skills/diagnostico-empresarial` e/ou
`catalogo/modulos/diagnostico`), nunca produção direta de
conteúdo/campanha/peça — mesmo que o pedido original do usuário já
mencionasse uma entrega específica. Se o usuário insistir em pular
direto pra produção, avisar uma vez:

> "Posso já ir direto pra [entrega pedida], mas sem diagnóstico o
> trabalho corre risco de não bater com o contexto real do
> negócio/cliente. Prefere seguir assim mesmo, ou faz sentido rodar o
> diagnóstico primeiro?"

Seguir com o que o usuário decidir.

### Passo 6 — Detectar necessidade de processo/funil/pipeline/campanha

Perguntar (ou inferir do objetivo, confirmando antes de assumir):

- Existe uma sequência de tarefas internas repetível? → considerar
  `.claude/skills/mapear-processo`.
- Existe conversão de pessoas entre etapas com perda mensurável? →
  considerar `.claude/skills/desenhar-funil`.
- Existem oportunidades em andamento que precisam de acompanhamento? →
  considerar `.claude/skills/configurar-pipeline`.
- É uma ação coordenada com prazo, canais e orçamento? → considerar
  `.claude/skills/criar-campanha`.
- Vai existir uma página de oferta/venda? → considerar
  `.claude/skills/estruturar-pagina-de-oferta`.

Registrar a resposta em `## Modelo aplicável` no `PROJETO.md`. Não
forçar nenhum desses modelos quando não fizer sentido para o projeto.

### Passo 6b — Avaliar necessidade de classificação por nível

Perguntar: "Existe alguma dimensão que precisa ser classificada aqui —
maturidade digital, financeira, comercial, operacional, ou outra?" (ver
`knowledge/niveis/NIVEIS_E_DIMENSOES.md`). Se sim: qual resultado o
projeto busca, e (se já for possível saber) qual o nível atual, qual o
recomendado, qual a lacuna, qual o plano de avanço e qual o escopo
mínimo.

Não obrigar classificação quando isso não agregar valor — uma tarefa
simples de correção de arquivo normalmente não precisa; uma
estruturação empresarial, financeira, digital, comercial ou
operacional provavelmente precisa. Se sim, encaminhar para
`.claude/skills/classificar-nivel` depois do diagnóstico.

### Passo 7 — Atualizar contexto ativo

Atualizar `.lkt-system/estado/contexto-ativo.json`:
- `workspace_ativo`: `{ "tipo": "clientes|empresas|projetos-internos", "slug": "<slug>" }`
- `projeto_ativo`: slug do projeto (ou `null`)
- Adicionar uma linha em `decisoes_recentes` registrando a criação.

Não sobrescrever `ultima_sessao` aqui — isso é responsabilidade de
`salvar-local`.

### Passo 8 — Resumo

```
✓ Workspace: workspaces/<raiz>/<slug>/ [criado agora | já existia]
✓ Projeto: .../projetos/<slug-do-projeto>/ (ou workspaces/projetos-internos/<slug>/)
  - PROJETO.md
  - Estrutura criada: <lista só das pastas pertinentes>

Objetivo: <objetivo>
Responsável: <papel: nome ou "a definir">
Prazo: <prazo ou "a definir">
Indicador: <indicador>
Modelo aplicável: <processo/funil/pipeline/campanha/jornada/nenhum>

Próximo passo recomendado: diagnóstico (diagnostico-empresarial).
```

---

## Saídas

Workspace (se novo) e projeto criados com estrutura padronizada
(só as pastas pertinentes), `PROJETO.md` preenchido e contexto ativo
atualizado.

## Regras

- Nunca criar workspace novo sem confirmação explícita do usuário.
- Nunca começar por produção de conteúdo — o fluxo padrão é contexto →
  diagnóstico → ... → produção.
- Nome de pasta: slug a partir do nome real (minúsculas, sem acento,
  espaço vira hífen) — não usar nome genérico tipo "cliente-novo".
- Se o workspace/projeto já existir com esse nome, avisar e perguntar
  se é pra adicionar um projeto novo dentro dele ou se é outro
  workspace/projeto homônimo (nesse caso, sufixo no slug).
- Nunca criar todas as 8 subpastas de projeto por padrão — só as
  pertinentes à classificação (Passo 4).
- Responsável sempre registrado como papel + (nome ou "a definir"),
  nunca só um nome solto.

## Critérios de qualidade

- `WORKSPACE.txt` sempre tem nome, tipo e data — mesmo que o resto
  esteja "a definir".
- `PROJETO.md` sempre tem objetivo, entregas previstas, indicador de
  sucesso, modelo aplicável e estado — mesmo que responsável/prazo/
  orçamento ainda estejam "a definir".
- Estrutura de pastas consistente entre workspaces do mesmo tipo (só
  muda a raiz: `workspaces/clientes/`, `workspaces/empresas/`,
  `workspaces/projetos-internos/`).

## Critérios de validação

- Todo workspace criado tem `WORKSPACE.txt`, `INDICE.txt` e
  `_memoria.json` válido contra `schemas/workspace.schema.json`.
- Todo projeto criado tem `PROJETO.md` com as 7 seções obrigatórias
  (objetivo, entregas previstas, responsável, prazo, orçamento,
  indicador, modelo aplicável) mais o estado.

## Limitações

- Não faz diagnóstico nem preenche o conteúdo de `01-diagnostico/` em
  diante — só cria a estrutura vazia.
- Não decide sozinha se um workspace "parecido" é o mesmo ou outro —
  pergunta quando houver ambiguidade de nome.

## Caminho de salvamento

`workspaces/<raiz>/<slug>/` (workspace novo) e/ou
`workspaces/<raiz>/<slug>/projetos/<slug-do-projeto>/` ou
`workspaces/projetos-internos/<slug-do-projeto>/`.

## Contrato de handoff

Encaminha para `.claude/skills/diagnostico-empresarial` como próximo
passo padrão. Se o usuário decidir pular o diagnóstico, encaminha
direto pro módulo da entrega pedida (`catalogo/modulos/conteudo`,
`catalogo/modulos/financeiro`, etc.), ou para
`mapear-processo`/`desenhar-funil`/`configurar-pipeline`/`criar-campanha`
quando o Passo 6 identificar essa necessidade.

## Exemplos de gatilhos positivos

- "Novo projeto"
- "Novo cliente"
- "Nova empresa"
- "Começar projeto pra [nome]"

## Exemplos de gatilhos negativos

- "Cria um carrossel pro projeto Y" quando o projeto Y já existe (é
  direto na skill de conteúdo, sem passar por aqui)
