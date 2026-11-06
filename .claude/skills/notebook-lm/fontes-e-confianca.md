# Fontes e confiança — notebook-lm

## O DOCX nunca é fonte de verdade

Fontes de verdade continuam sendo: memória estruturada (`_memoria.json`,
`_memoria/`), arquivos originais, planilhas, contratos, propostas,
diagnósticos, decisões, relatórios, transcrições, imagens, dados do
sistema, registros financeiros, campanhas/funis/pipelines, tarefas,
anexos. O dossiê é regenerado a partir delas — nunca o contrário.

Se o usuário editar o DOCX manualmente, essas mudanças só entram de
volta no sistema quando ele reimportar o arquivo e confirmar
explicitamente que a alteração é válida (nesse caso, tratar como fonte
externa nova, passando por `organizar-arquivos`).

## O que nunca entra automaticamente no manifesto

`node_modules`, `.git`, cache, `_backups/`/`historico/` (são saída do
próprio sistema, não fonte), arquivo temporário (`~$*`, `*.tmp`),
saída antiga (DOCX gerado anteriormente — evita o dossiê citar a si
mesmo como fonte), arquivo de outro workspace/cliente (o escaneamento é
sempre restrito à raiz do workspace/projeto pedido), segredo/token/
credencial (`.env`, `*.key`, `*.pem`, nomes contendo "senha", "token",
"secret", "credential"), dado pessoal desnecessário.

## Classificação de cada fonte no manifesto

`scope`: `company` (nível empresa), `project` (nível projeto) ou
`shared` (usado por mais de um, só quando autorizado explicitamente).

`confidentiality`: `normal`, `restricted` ou `sensitive` — arquivo
`restricted`/`sensitive` nunca entra na versão compartilhável sem
redação prévia (ver `docs/SEGURANCA_E_PERMISSOES.md`).

`confidence`: `confirmed` (dado direto de fonte primária), `partial`
(fonte incompleta ou desatualizada) ou `uncertain` (inferido, precisa
confirmação).

## Classificação de cada informação no texto do dossiê

CONFIRMADO, HIPÓTESE, PROJEÇÃO, DECISÃO, RECOMENDAÇÃO, PENDÊNCIA,
RISCO, NÃO INFORMADO, CONFLITO, HISTÓRICO. Ver exemplos de formatação
em `exemplos.md`. Regras:

- Nunca misturar projeção com resultado realizado.
- Nunca preencher informação ausente por adivinhação — usar "não
  informado" e listar como pendência.
- Todo CONFLITO encontrado entre fontes é registrado em
  `MANIFESTO_FONTES.json` → `conflicts[]` e mostrado no dossiê, nunca
  silenciosamente resolvido a favor de uma fonte sem dizer isso.
