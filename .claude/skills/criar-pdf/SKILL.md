---
name: criar-pdf
description: >
  Converte um documento, relatório ou apresentação já finalizado em PDF
  para entrega, preservando o arquivo-fonte original. Use quando o
  usuário pedir "gera isso em PDF", "manda um PDF pro cliente", "exporta
  esse relatório em PDF".
---

# criar-pdf — Exportação final em PDF

Skill de acabamento: converte um conteúdo **já pronto** (de
`criar-documento`, `criar-apresentacao`, relatório de diagnóstico, etc.)
em PDF — não cria conteúdo novo.

## Quando usar

- O conteúdo já existe (documento/apresentação/relatório) e precisa virar
  PDF pra envio/entrega formal.

## Quando não usar

- Conteúdo ainda não escrito — passar por `criar-documento` ou
  `criar-apresentacao` primeiro.
- Planilha que precisa continuar editável pro cliente — PDF "trava" o
  conteúdo; confirmar que é isso mesmo que o usuário quer.

## Entradas

- Caminho do arquivo-fonte já finalizado.

## Dependências

- Ferramenta de conversão disponível no ambiente (depende do formato de
  origem — Markdown, Word, HTML). Se nenhuma ferramenta de conversão
  estiver disponível, avisar e não inventar um PDF sem conteúdo real.

## Contexto que deve ser carregado

Projeto/cliente ativo, para saber onde salvar o resultado.

---

## Workflow

### Passo 1 — Confirmar que o conteúdo está finalizado

Perguntar se o arquivo-fonte já está aprovado — não gerar PDF de rascunho
sem avisar que é rascunho.

### Passo 2 — Converter

Gerar o PDF a partir do arquivo-fonte, preservando o arquivo original
intacto (nunca sobrescrever a fonte editável).

### Passo 3 — Validar

Abrir/conferir que o PDF gerado corresponde ao conteúdo esperado —
páginas completas, sem corte de texto/imagem, sem página em branco
inesperada.

### Passo 4 — Salvar e registrar

Salvar em `<pasta-do-projeto-ativo>/08-entregas/` (mesma pasta do
arquivo-fonte, ou `09-relatorios/` se for relatório) e registrar no
índice.

---

## Saídas

Arquivo PDF exportado, fiel ao conteúdo-fonte aprovado.

## Regras

- Nunca sobrescrever o arquivo-fonte editável — o PDF é uma exportação
  adicional, não substitui o original.
- Se o conteúdo-fonte tiver placeholder/rascunho, avisar antes de gerar
  o PDF final.

## Critérios de qualidade

- PDF final corresponde fielmente ao conteúdo aprovado.

## Critérios de validação

- Arquivo-fonte original continua acessível e inalterado.
- PDF registrado no índice do projeto.

## Limitações

- Não cria conteúdo — só exporta o que já existe.
- Depende de ferramenta de conversão disponível no ambiente; sem ela,
  não improvisa substituto.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/08-entregas/` ou `09-relatorios/`.

## Contrato de handoff

`anti-chat` (quality gate final) roda antes da exportação — este é o
último passo, de fato, só depois disso.

## Exemplos de gatilhos positivos

- "Gera esse relatório em PDF"
- "Manda a proposta em PDF pro cliente"

## Exemplos de gatilhos negativos

- "Escreve a proposta" (conteúdo ainda não existe — é `criar-documento` primeiro)
