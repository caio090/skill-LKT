# Validação — notebook-lm

## Antes de gerar

- [ ] Empresa/cliente confirmado, sem ambiguidade.
- [ ] Escopo (empresa vs. projeto) confirmado — nunca os dois
      misturados sem pedido, nunca mais de um cliente no mesmo
      arquivo sem autorização expressa.
- [ ] Fontes escaneadas e mostradas ao usuário (incluídas, excluídas,
      conflitos).

## Depois de gerar (estrutural — `tools/notebook-lm/validar-docx.js`)

- [ ] Arquivo é um ZIP/OOXML válido (abre via `jszip` sem erro).
- [ ] `word/document.xml` presente e é XML bem formado.
- [ ] Seções esperadas presentes no texto extraído (capa, sumário,
      índice de fontes, histórico de versões no mínimo).
- [ ] Nenhuma seção com conteúdo vazio além do que foi
      deliberadamente omitido.
- [ ] Metadados mínimos presentes (título, versão).

## Limitação conhecida: sem renderização visual

Este ambiente não tem LibreOffice/Word instalado, então a etapa da
Seção 12 do prompt de implementação ("renderizar para imagem/PDF,
verificar visualmente todas as páginas, corrigir sobreposição/corte/
tabela quebrada") **não é executada automaticamente aqui** — só a
validação estrutural acima. Isso é uma limitação documentada, não uma
etapa pulada silenciosamente: sempre informar isso ao usuário quando
entregar o DOCX.

Se o ambiente tiver LibreOffice disponível (`soffice` no PATH), rodar:

```
soffice --headless --convert-to pdf --outdir <pasta-temp> "<caminho-do-docx>"
```

e então inspecionar o PDF gerado (visualmente ou convertendo página a
página para imagem) antes de marcar a versão como definitivamente
validada. Documentar no manifesto (`status`) se essa etapa rodou ou
não.

## Depois da troca atômica

- [ ] `_ATUAL` promovido só depois da validação estrutural passar.
- [ ] Versão anterior arquivada em `historico/` com nome
      `AAAA-MM-DD_HHMM_..._vNN.ext`, sem edição.
- [ ] `MANIFESTO_FONTES.json` com `version` incrementada e
      `status: current`.

## Versão compartilhável

- [ ] Nenhum segredo/token/credencial presente (checagem automática
      via padrões de nome/conteúdo).
- [ ] Nenhum dado de outro cliente presente.
- [ ] Custo interno/margem removidos, mantendo só o que é comercial.
- [ ] Metadados do arquivo revisados (autor, comentários internos).
