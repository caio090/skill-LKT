# Fluxo — notebook-lm

```
Identificar empresa/cliente e escopo (empresa vs. projeto)
  → Confirmar que não há mistura de workspaces
  → Escanear fontes (tools/notebook-lm/escanear-fontes.js)
  → Mostrar o que vai entrar / ficar de fora / conflitos
  → Montar conteúdo classificado (CONFIRMADO/HIPÓTESE/PROJEÇÃO/...)
  → Gerar DOCX em arquivo temporário (tools/notebook-lm/gerar-dossie.js)
  → Validar estruturalmente (tools/notebook-lm/validar-docx.js)
  → Troca atômica: arquivar _ATUAL anterior em historico/, promover o novo
  → Atualizar MANIFESTO_FONTES.json (version, generated_at, status)
  → Perguntar qual resultado o usuário quer no NotebookLM
  → Gerar PROMPT_NOTEBOOKLM_ATUAL.txt
  → Informar caminhos (docx, prompt, manifesto) e status final
```

Em modo `/notebook-lm atualizar`, pular direto para o escaneamento de
fontes e comparar hash/data de modificação com o manifesto anterior —
só regenerar as seções afetadas pelas fontes que mudaram (quando
possível) ou o documento inteiro (quando a mudança for estrutural).

Em modo `/notebook-lm status`, só ler o manifesto atual e comparar
datas de modificação das fontes — não gera nada, só informa se está
`current` ou `outdated` e o que mudou.
