# Atualização — notebook-lm

Não regenerar a cada pequena mudança. Ao alterar uma fonte relevante:

1. Marcar o dossiê como `status: outdated` em `MANIFESTO_FONTES.json`.
2. Registrar quais fontes mudaram (`escanear-fontes.js` compara hash e
   `modified_at` com o manifesto anterior).
3. Mostrar a data da última versão (`DOSSIE_*_ATUAL.docx`).
4. Oferecer atualização — nunca regenerar sozinho sem avisar (padrão:
   **atualização assistida**, não automática).

## Gatilhos de atualização

Comando manual (`/notebook-lm atualizar`), encerramento de diagnóstico,
aprovação de escopo, nova proposta, alteração de preço, alteração de
roadmap, novo relatório, encerramento de fase, antes de reunião, antes
de exportação.

Quando um desses gatilhos ocorrer dentro de outra skill
(`diagnostico-empresarial`, `proposta-e-precificacao`, etc.), essa
skill deve perguntar: "Isso afeta o dossiê do NotebookLM — quer que eu
marque como desatualizado (ou já atualize agora)?"

## Atualização automática (opcional, configurável)

Pode existir, mas nunca é o padrão. Se o usuário pedir explicitamente
("sempre que eu mudar algo, atualiza sozinho"), registrar essa
preferência em `_memoria.json` do workspace (`preferencias.atualizacao_notebooklm: "automatica"`)
e, mesmo assim, sempre passar pela troca atômica (nunca sobrescrever
`_ATUAL` sem versionar o anterior em `historico/`).

## Troca atômica (sempre, manual ou automática)

1. Gerar em arquivo temporário.
2. Validar (`validar-docx.js`).
3. Arquivar o `_ATUAL` anterior em
   `historico/AAAA-MM-DD_HHMM_..._vNN.docx` (e prompt/manifesto
   correspondentes).
4. Promover o temporário para `_ATUAL`.
5. Atualizar `MANIFESTO_FONTES.json` (`version` +1, `generated_at`,
   `status: current`).

Nunca editar um arquivo já movido para `historico/`.
