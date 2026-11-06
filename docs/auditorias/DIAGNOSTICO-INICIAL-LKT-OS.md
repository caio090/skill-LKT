# Diagnóstico inicial — LKT OS (repositório REC-OS)

> Executado nas Fases 0 e 1 do prompt mestre de refinamento do LKT OS.
> Somente leitura — nenhuma alteração estrutural, migração ou correção foi
> feita nesta rodada. Data: 2026-07-26.

---

## Fase 0 — Ambiente

- **Diretório confirmado:** `C:\Users\Trabalho\Desktop\Novo Sistema REC OS\REC-OS`
- **Pasta pai contém:** `REC-OS/` (repositório principal), `lkt-plus/` e
  `MazyOS/` (pastas antigas, intactas, não tocadas).
- **Git:** `REC-OS` **não é um repositório Git** (`git status` retorna
  "not a git repository"). Não há risco de commit/push acidental porque não
  há Git para começar. `MazyOS` tem `.git` próprio; `lkt-plus` não tem.
- **Node.js:** v24.16.0 — **npm:** 11.13.0 — disponíveis.
- **Python:** não instalado (alias da Microsoft Store, sem binário real).
  Qualquer script financeiro/de automação previsto no prompt mestre em
  Python **não pode rodar** neste ambiente até Python ser instalado, ou
  precisa ser escrito em Node.
- **Arquivos `.env`:** nenhum encontrado em `REC-OS`. Nenhum segredo
  exposto observado.
- Nenhum comando destrutivo, commit, push ou alteração foi executado.

---

## Fase 1 — Estrutura encontrada em REC-OS

```
REC-OS/
  CLAUDE.md            (223 linhas — enxuto, dentro do espírito pedido)
  README.md
  AGENTS.md
  .claude/skills/      → VAZIO (nenhuma subpasta)
  _memoria/            → 13 arquivos-modelo + clientes/ e projetos/ vazios
  docs/                → catalogo-skills.md, manifesto.md, roteamento.md
  modules/             → 13 pastas, TODAS vazias (sem nenhum arquivo)
  templates/           → 4 pastas, TODAS vazias (sem nenhum arquivo)
  tools/               → validar.js (validador Node, funcional)
  arquivos/
    entrada/           → VAZIO
    processados/       → VAZIO
    biblioteca/        → 10 subpastas, TODAS vazias
    INDICE.md          → tabela vazia ("nenhum arquivo processado ainda")
```

### Leitura de `CLAUDE.md`, `README.md`, `AGENTS.md`

Já existe uma base coerente e enxuta, criada em 2026-07-20, que já segue boa
parte dos princípios do prompt mestre:

- Memória modular (empresa, preferências, estratégia, marca, clientes,
  projetos, processos, ferramentas, equipe, métricas, decisões,
  aprendizados, pendências) — já separada corretamente por tipo.
- Já define a cadeia obrigatória `pagina-e-site → design-front-end →
  texto-natural-pt-br` e a regra de aplicar `texto-natural-pt-br` a todo
  texto voltado a público externo.
- Já define central de arquivos (`entrada/processados/biblioteca`) com
  regra de nunca alterar o original.
- Já orienta ordem de ativação de cliente/projeto (contexto → diagnóstico →
  objetivos → ... → ajustes), igual ao pedido no prompt mestre.
- Já tem regra de migração de `lkt-plus`/`MazyOS` exigindo registro prévio
  no manifesto antes de copiar qualquer coisa.
- `AGENTS.md` é um resumo derivado do `CLAUDE.md`, não duplica tudo.

**Conclusão:** o núcleo (Fase 2 do roadmap do prompt mestre) já foi
parcialmente construído numa sessão anterior. Não é um projeto do zero —
é um esqueleto correto, mas **vazio de conteúdo real**: zero skills, zero
memória preenchida, zero clientes, zero arquivos processados.

---

## Skills

- **Skills válidas em `.claude/skills/`: 0**
- **Skills inválidas: 0** (porque não há nenhuma — pasta completamente
  vazia)
- `docs/catalogo-skills.md` já reflete isso corretamente: "Nenhuma skill
  instalada ainda."
- `docs/roteamento.md` tem a tabela de módulos → skill pronta, mas todas as
  células de skill dizem `_a definir na migração_`.
- Rodei o validador existente (`node tools/validar.js`):

```
Pastas em modules/: 13
Pastas em templates/: 4
Skills válidas: 0
Arquivos Markdown lidos: 19
Problemas: 0
Avisos: 0
```

O validador está funcional e já checa: kebab-case, frontmatter YAML
(`name`/`description`), duplicidade de skill, arquivos soltos fora de
pasta, referências residuais a MazyOS/LKT Plus, links quebrados, e catálogo
desatualizado. **Não precisa ser recriado — só será usado quando houver
skills para validar.**

---

## Memória (`_memoria/`)

Todos os 13 arquivos-modelo existem, mas estão **vazios (apenas
placeholders com campos em branco)**:

- `empresa.md` — campos "Nome, Negócio, O que faz, Perfil..." todos vazios.
- `pendencias.md` — só tem uma pendência de sistema: migrar lkt-plus/MazyOS
  (aguardando autorização).
- `clientes/` e `projetos/` — pastas existem, **sem nenhum cliente ou
  projeto cadastrado ainda**.

Ou seja: a instalação (`/instalar` do prompt mestre) nunca foi rodada de
fato para preencher esses dados — a estrutura foi criada, mas o
onboarding real da Lokat (nome, serviços, equipe, região, tom de voz,
identidade visual, ferramentas) ainda não aconteceu.

---

## Módulos e templates

`modules/` (13 pastas: diagnostico, briefing, estrategia, posicionamento,
produtos-e-ofertas, paginas-e-sites, conteudo, trafego-pago, crm,
financeiro, operacional, automacoes, dados-e-relatorios) e `templates/`
(nova-marca, negocio-local, produto-digital, cliente-modelo) existem só
como pastas — **nenhum arquivo dentro de nenhuma delas**. São só a
intenção de estrutura, sem conteúdo produzido ainda.

---

## Central de arquivos e planilhas — arquivos de entrada

`arquivos/entrada/` está **vazio**. Os 7 arquivos citados no prompt mestre
não estão no repositório:

- `Minha Empresa Organizada - 2026.xlsx`
- `PRECIFICAO_LUCRATIVA_3.0__.xlsx`
- `SKILL.md`, `SKILL(1).md`, `SKILL(2).md`, `SKILL(3).md`, `SKILL(4).md`,
  `SKILL(5).md`

**Não inventei conteúdo nem fui buscar cópias externas.** O que está
descrito no prompt mestre sobre as duas planilhas (15 abas, tabelas
ENTRADAS/SAÍDAS, inconsistência de status "Concluído/cONCLUÍDO/concluído",
nomes genéricos tipo `Coluna1`; 108 abas, aba oculta `BDUNI` com ~500
fórmulas `#REF!`, padrão `VLOOKUP(...,Tabela1[],...)`) é **informação que
você me passou, não algo que eu verifiquei lendo os arquivos** — porque
eles ainda não existem no repositório. Preciso que você copie os 7
arquivos para `arquivos/entrada/` antes que eu possa auditar as fórmulas,
abas e erros de verdade.

---

## Pastas antigas (somente leitura, nada foi alterado)

### `lkt-plus/` (sem `.git`)

Topo: `.claude/`, `_memoria/`, `dados/`, `identidade/`, `marketing/`,
`saidas/`, `scripts/`, `templates/`, `CLAUDE.md`, `README.md`,
`.gitignore`.

`.claude/skills/` tem **16 pastas de skill** + **1 arquivo solto fora de
pasta**: `SKILL Design de Front-end.md` — isso já é um problema de
estrutura (nome com espaços e maiúsculas, e fora do padrão
`nome-da-skill/SKILL.md`; o validador do REC-OS acusaria isso como "arquivo
solto" se essa pasta fosse apontada nele).

Skills encontradas (nomes de pasta): `abrir`, `analisar-dados`,
`anuncio-google`, `aprovar-post`, `atualizar`, `carrossel`,
`diagnostico-lokat`, `email-profissional`, `instalar`, `mapear-rotinas`,
`novo-cliente`, `novo-projeto`, `publicar-tema`, `relatorio-ads`,
`responder-avaliacoes`, `salvar`, `seo`.

### `MazyOS/` (tem `.git` próprio)

Topo: `.claude/`, `_memoria/`, `clientes/` (vazia), `dados/`,
`identidade/`, `marketing/`, `saidas/`, `scripts/`, `templates/`,
`CLAUDE.md`, `README.md`, `.gitignore`.

`.claude/skills/` tem **15 pastas** (mesmas do lkt-plus, exceto sem
`diagnostico-lokat` e sem `novo-cliente`), sem arquivo solto.

Nenhum conteúdo dessas duas pastas foi lido em profundidade ainda (isso é
Fase 9 — migração — que só acontece depois de autorização). O que já se
sabe, porque está no próprio prompt mestre, sobre problemas específicos
dessas skills (frontmatter inválido em `diagnostico-lokat`, menção a "LKT
PLUS" em `mapear-rotinas`, destino `estudos/` em `analisar-dados`, limites
fixos de CTR em `relatorio-ads`) ainda precisa ser confirmado lendo os
arquivos de fato — não fiz essa leitura profunda nesta rodada porque o
escopo desta resposta é só Fases 0 e 1 do repositório principal.

---

## Resumo de problemas, riscos e lacunas

### Problemas encontrados
1. `.claude/skills/` do REC-OS vazio — zero skills operacionais, apesar de
   `CLAUDE.md`/`AGENTS.md`/`docs/roteamento.md` já assumirem a existência
   de `pagina-e-site`, `design-front-end` e `texto-natural-pt-br`.
2. Memória inteiramente vazia (placeholders) — nenhuma sessão de instalação
   real foi feita.
3. `modules/` e `templates/` são só pastas sem conteúdo.
4. `arquivos/entrada/` vazio — os 7 arquivos citados não foram copiados
   para o repositório.
5. Em `lkt-plus/.claude/skills/`, há 1 arquivo solto fora do padrão de
   pasta (`SKILL Design de Front-end.md`).

### Riscos
- Sem Git em `REC-OS`, não há histórico nem forma de reverter alterações
  por commit — qualquer mudança estrutural feita a partir de agora deveria
  primeiro considerar iniciar um repositório Git local (só com autorização
  sua; nenhum init foi feito).
- Sem Python instalado, qualquer ferramenta financeira (`tools/financeiro/*.py`
  previstas no prompt mestre) não roda neste ambiente sem decisão sua:
  instalar Python ou reescrever em Node.
- As duas planilhas financeiras (com ~500 fórmulas `#REF!` e inconsistência
  de status) ainda não foram auditadas de verdade — qualquer número dessas
  planilhas hoje é uma descrição de segunda mão, não uma leitura direta.

### Lacunas
- Nenhum cliente, projeto ou dado real cadastrado.
- Nenhuma skill migrada ou criada.
- Nenhum arquivo de entrada processado.
- `docs/roteamento.md` com todas as células de skill em aberto.

---

## Proposta de arquitetura adaptada (não executar ainda)

A estrutura-alvo do prompt mestre já bate, quase 1:1, com o que existe em
`REC-OS` hoje — não é necessário recriar a árvore. Ajustes sugeridos, sem
duplicar responsabilidade:

- Manter `modules/` como está (já equivale a `modulos/` do prompt mestre).
- Manter `_memoria/` como está (já equivale a `_memoria/` do prompt
  mestre, inclusive com `clientes/` e `projetos/`).
- Criar `docs/auditorias/` (feito agora, para este relatório),
  `docs/referencias/` e `docs/roadmap/` quando chegar a hora das fases
  correspondentes — não criar vazio adiantado.
- Adicionar `financeiro/` (schemas, fontes, índices, mapeamentos,
  relatórios, modelos, versões) e `tools/financeiro/` só na Fase 4, depois
  que as duas planilhas estiverem em `arquivos/entrada/` e auditadas.
- `arquivos/registros/` (manifesto por arquivo, um `.yml` por item) ainda
  não existe — criar na Fase 3, junto com o primeiro arquivo processado.
- Não criar `identidade/`, `saidas/`, `dados/`, `tests/` no nível raiz
  ainda — avaliar se `arquivos/biblioteca/` e `modules/` já cobrem essa
  necessidade antes de abrir pastas novas com função sobreposta.

---

## Roadmap por fases (proposto, aguardando autorização para iniciar Fase 2 em diante)

1. **Auditoria e segurança** — **concluída nesta rodada** (Fases 0 e 1).
2. **Núcleo e memória** — já existe estrutura; falta preencher memória
   real via instalação (perguntas sobre a Lokat) e criar as 3 primeiras
   skills obrigatórias (`pagina-e-site`, `design-front-end`,
   `texto-natural-pt-br`) já referenciadas no `CLAUDE.md`.
3. **Central de arquivos** — aguardando você copiar os 7 arquivos para
   `arquivos/entrada/`; então processar (hash, manifesto, índice).
4. **Financeiro e planilhas** — auditoria das duas planilhas (inclusive
   aba oculta `BDUNI` e inconsistência de status), schemas, skills
   financeiras.
5. **Diagnóstico e estratégia** — só depois de memória da empresa
   preenchida.
6-9. Marketing/conteúdo/audiovisual, comercial/operação, tecnologia,
   migração de legado — na ordem do prompt mestre, cada uma com inventário
   e aprovação prévia.
10. Teste real com casos de cada segmento.

---

## Alterações recomendadas primeiro (lista exata)

1. Copiar os 7 arquivos citados para `arquivos/entrada/` (nenhum está lá).
2. Rodar a instalação/onboarding real da Lokat para preencher
   `_memoria/empresa.md`, `preferencias.md`, `estrategia.md`, `marca.md`,
   `produtos-e-servicos.md`, `equipe.md`, `ferramentas.md` — hoje todos em
   branco.
3. Criar as 3 skills já assumidas pelo `CLAUDE.md` mas inexistentes:
   `pagina-e-site`, `design-front-end`, `texto-natural-pt-br`.
4. Decidir se `REC-OS` vira um repositório Git local (sem push, sem
   remoto) para ter histórico de alterações — hoje não há como reverter
   nada por commit.

Nenhuma dessas quatro ações foi executada. Aguardando sua autorização.

---

## Perguntas de decisão

1. Você quer que eu já inicie um repositório Git **local** dentro de
   `REC-OS` (sem remoto, sem push) para começar a ter histórico de
   commits a partir daqui, ou prefere continuar sem Git por enquanto?
2. Os 7 arquivos de entrada (2 planilhas + 6 SKILL.md) — você vai copiá-los
   para `arquivos/entrada/`, ou eles estão em outro caminho que eu ainda
   não verifiquei?
3. Quer que eu já rode a instalação/onboarding real da Lokat (perguntas
   sobre nome, serviços, equipe, região, tom de voz, ferramentas) antes de
   qualquer outra fase, já que hoje toda a memória está vazia?
