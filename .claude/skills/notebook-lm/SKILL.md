---
name: notebook-lm
description: >
  Gera um dossiê Word (DOCX real, não Markdown renomeado) consolidando
  as informações de uma empresa ou de um projeto — memória, diagnóstico,
  proposta, projeções, roadmap, campanhas/funis/pipelines, decisões e
  pendências — preparado para uso como fonte no NotebookLM. Mantém dois
  níveis de dossiê (empresa e projeto), nunca mistura workspaces
  diferentes, versiona com histórico e gera um prompt específico para
  acompanhar o arquivo. Use quando o usuário disser "gera o arquivo do
  NotebookLM", "junta tudo do projeto em Word", "atualiza o dossiê",
  "cria um prompt pra proposta no NotebookLM", ou comandos
  `/notebook-lm gerar|atualizar|status|fontes|validar|historico|prompt`.
---

# notebook-lm — Dossiê NotebookLM (Word consolidado por empresa/projeto)

Consolida as fontes reais de um workspace ou projeto num único DOCX
visual, versionado e rastreável — nunca uma fonte de verdade nova, só
uma saída regenerável a partir da memória e dos arquivos existentes.
Ver `docs/DOSSIE_NOTEBOOKLM.md` para a arquitetura completa.

## Quando usar

- Usuário quer levar o contexto de uma empresa ou projeto para o
  NotebookLM (ou qualquer uso externo que precise de um documento
  único consolidado).
- Encerramento de diagnóstico, aprovação de escopo, nova proposta,
  alteração de preço/roadmap, novo relatório, encerramento de fase,
  antes de reunião ou antes de exportação (gatilhos de atualização —
  ver `atualizacao.md`).

## Quando não usar

- Para gerar uma entrega específica (proposta, relatório, apresentação)
  isolada — isso é a skill específica (`proposta-e-precificacao`,
  `criar-apresentacao`, etc.). O dossiê consolida o que essas skills já
  produziram, não substitui a produção delas.
- Para editar a memória do projeto — o dossiê é gerado a partir da
  memória, nunca o contrário (ver `fontes-e-confianca.md`).

## Entradas

- Empresa/cliente e, se aplicável, projeto (perguntar se ambíguo — ver
  `perguntas.txt`).
- Tipo de dossiê: empresa ou projeto (nunca os dois misturados sem
  pedido explícito, nunca mais de um cliente no mesmo arquivo sem
  autorização expressa).
- Se for atualização: o que mudou desde a última versão.
- Se for prompt: qual resultado o usuário quer obter no NotebookLM
  (ver `prompts.md`).

## Dependências

- `tools/notebook-lm/escanear-fontes.js` — varre o workspace/projeto e
  gera `MANIFESTO_FONTES.json`.
- `tools/notebook-lm/gerar-dossie.js` — monta o conteúdo e gera o DOCX
  real (biblioteca `docx`, Node — ver decisão de arquitetura em
  `docs/DOSSIE_NOTEBOOKLM.md`).
- `tools/notebook-lm/validar-docx.js` — validação estrutural do DOCX
  gerado (OOXML válido via `jszip`) antes de marcar como pronto.
- `schemas/manifesto-fontes.schema.json`
- `templates/notebook-lm/` (modelos de referência)
- `.lkt-system/estado/contexto-ativo.json` (workspace/projeto ativo)

## Contexto que deve ser carregado

- `_memoria.json`, `WORKSPACE.txt` do workspace.
- `PROJETO.md`, diagnóstico, proposta, projeções, roadmap do projeto
  (quando existirem — nunca inventar o que não existe, marcar como
  "não informado").
- `_memoria/sistema/marca.md` (para dados institucionais no dossiê de
  empresa).

---

## Workflow

### Passo 1 — Identificar escopo (ver `perguntas.txt`)

1. Confirmar empresa/cliente.
2. Se houver mais de um projeto, perguntar qual (ou se é dossiê de
   empresa, que resume todos).
3. Se o usuário disser "tudo", explicar a diferença entre dossiê de
   empresa e de projeto (Seção 2 de `docs/DOSSIE_NOTEBOOKLM.md`) e
   recomendar a opção certa — nunca gerar os dois sem perguntar, e
   nunca juntar mais de um cliente no mesmo arquivo sem autorização
   expressa.

### Passo 2 — Escanear fontes

Rodar `tools/notebook-lm/escanear-fontes.js` com a raiz do
workspace/projeto certo. Isso gera/atualiza `MANIFESTO_FONTES.json`
com: arquivos incluídos, excluídos (e por quê), hash, data de
modificação, escopo, confidencialidade, e nível de confiança.

Nunca inclui automaticamente: `node_modules`, `.git`, cache, backup,
arquivo temporário, saída antiga (DOCX gerado anteriormente), arquivo
de outro cliente, segredo/token/credencial. Ver `fontes-e-confianca.md`.

### Passo 3 — Mostrar o que vai entrar

Antes de gerar, mostrar ao usuário: quantos arquivos entraram, quais
ficaram de fora e por quê, se há conflito entre fontes, se há
informação sensível. Perguntar se algo precisa ser ajustado antes de
seguir.

### Passo 4 — Montar o conteúdo classificado

Para cada seção (ver `estrutura-do-docx.md`), preencher com o que
existe nas fontes, classificando cada informação como CONFIRMADO,
HIPÓTESE, PROJEÇÃO, DECISÃO, RECOMENDAÇÃO, PENDÊNCIA, RISCO, NÃO
INFORMADO, CONFLITO ou HISTÓRICO. Nunca preencher lacuna por
adivinhação — usar "não informado" explicitamente. Nunca misturar
projeção com resultado realizado.

### Passo 5 — Gerar o DOCX

Rodar `tools/notebook-lm/gerar-dossie.js` com o conteúdo classificado.
Gera em arquivo temporário primeiro (nunca sobrescreve o `_ATUAL`
direto).

### Passo 6 — Validar

Rodar `tools/notebook-lm/validar-docx.js` (estrutura OOXML válida,
seções presentes, sem erro de geração). Ver `validacao.md` — inclui a
limitação conhecida de não haver renderização visual pixel-a-pixel
neste ambiente (sem LibreOffice instalado) e o que fazer quando houver.

### Passo 7 — Publicar a versão (troca atômica)

1. Validar o arquivo temporário.
2. Arquivar o `_ATUAL` anterior em `historico/AAAA-MM-DD_HHMM_..._vNN.docx`.
3. Promover o temporário para `_ATUAL`.
4. Atualizar `MANIFESTO_FONTES.json` (`version`, `generated_at`,
   `status: current`).

Nunca editar uma versão de `historico/`.

### Passo 8 — Gerar o prompt do NotebookLM

Perguntar: "Qual resultado você quer obter no NotebookLM?" (ver
`prompts.md` para as opções e os mini-prompts prontos). Gerar
`PROMPT_NOTEBOOKLM_ATUAL.txt` correspondente.

### Passo 9 — Informar caminhos

Sempre terminar informando: caminho do DOCX, caminho do prompt,
caminho do manifesto, status (atual/desatualizado), e o que fazer para
atualizar depois.

---

## Comandos

```
/notebook-lm gerar       — gera a primeira versão ou uma versão nova completa
/notebook-lm atualizar   — regenera a partir das fontes que mudaram
/notebook-lm status      — mostra se o dossiê está atual ou desatualizado, e o que mudou
/notebook-lm fontes      — mostra o manifesto de fontes (incluídas/excluídas/conflitos)
/notebook-lm validar     — roda a validação estrutural do DOCX atual
/notebook-lm historico   — lista as versões anteriores
/notebook-lm prompt      — gera/regenera só o PROMPT_NOTEBOOKLM_ATUAL.txt
```

## Saídas

```
workspaces/<tipo>/<slug>/notebook-lm/empresa/
  DOSSIE_EMPRESA_ATUAL.docx
  PROMPT_NOTEBOOKLM_EMPRESA.txt
  INDICE_FONTES.txt
  MANIFESTO_FONTES.json
  historico/

workspaces/<tipo>/<slug>/notebook-lm/projetos/<projeto>/
  DOSSIE_PROJETO_ATUAL.docx
  PROMPT_NOTEBOOKLM_ATUAL.txt
  INDICE_FONTES.txt
  MANIFESTO_FONTES.json
  historico/
```

Versão compartilhável (só quando pedida explicitamente — ver
`docs/SEGURANCA_E_PERMISSOES.md`): `DOSSIE_COMPARTILHAVEL_ATUAL.docx`
ao lado de `DOSSIE_INTERNO_ATUAL.docx` (o `_ATUAL` normal é sempre a
versão interna).

## Regras

- Nunca misturar automaticamente empresas ou projetos diferentes num
  mesmo dossiê.
- Nunca gerar dossiê de mais de um cliente no mesmo arquivo sem
  autorização expressa.
- Nunca tratar o DOCX como fonte de verdade — ele é regenerado a
  partir da memória/arquivos, nunca o contrário. Edição manual do DOCX
  só entra de volta no sistema se o usuário reimportar e confirmar.
- Nunca preencher lacuna por adivinhação — marcar "não informado".
- Nunca misturar projeção com resultado realizado.
- Nunca incluir segredo, token, credencial ou dado de outro cliente.
- Nunca editar arquivo de `historico/`.
- Nunca sobrescrever `_ATUAL` sem passar pela troca atômica (Passo 7).
- Não regenerar a cada mudança pequena — marcar como desatualizado e
  oferecer atualização (atualização assistida é o padrão, não
  automática).

## Critérios de qualidade

- Todo dossiê tem capa, sumário, resumo executivo, índice de fontes e
  histórico de versões.
- Toda informação tem classificação visível (confirmado/hipótese/
  projeção/etc.).
- Seções sem conteúdo real são omitidas, não preenchidas com
  placeholder genérico.

## Critérios de validação

- DOCX gerado é um OOXML válido (`tools/notebook-lm/validar-docx.js`
  passa).
- `MANIFESTO_FONTES.json` válido contra
  `schemas/manifesto-fontes.schema.json`.
- Nenhuma fonte de outro workspace presente no manifesto.

## Limitações

- Não há renderização visual pixel-a-pixel do DOCX neste ambiente (sem
  LibreOffice/Word instalado) — a validação é estrutural (OOXML válido,
  seções presentes). Ver `validacao.md` para o procedimento completo
  quando uma ferramenta de renderização estiver disponível.
- Não lê o conteúdo de todo tipo de arquivo (ex.: áudio, vídeo) — esses
  entram no manifesto como fonte, mas o conteúdo precisa já estar
  transcrito/processado por `organizar-arquivos` antes de aparecer no
  dossiê.

## Caminho de salvamento

`workspaces/<tipo>/<slug>/notebook-lm/empresa/` ou
`workspaces/<tipo>/<slug>/notebook-lm/projetos/<projeto>/`

## Contrato de handoff

Consulta, sem substituir: `novo-projeto`, `diagnostico-empresarial`,
`proposta-e-precificacao`, `projecoes`, `mapear-processo`,
`desenhar-funil`, `configurar-pipeline`, `criar-campanha`,
`organizar-arquivos`, `continuar-projeto`. O dossiê consolida as saídas
delas — não recria o trabalho.

## Exemplos de gatilhos positivos

- "Gera o arquivo do NotebookLM"
- "Junta tudo do projeto em Word"
- "Atualiza o dossiê"
- "/notebook-lm gerar"

## Exemplos de gatilhos negativos

- "Cria uma proposta pra esse cliente" (é `proposta-e-precificacao`,
  não consolidação em dossiê)

Arquivos de apoio desta skill: `perguntas.txt`, `fluxo.md`,
`estrutura-do-docx.md`, `atualizacao.md`, `fontes-e-confianca.md`,
`prompts.md`, `validacao.md`, `exemplos.md`.
