# Exemplos — notebook-lm

## Classificação de informação no texto do dossiê

```
CONFIRMADO
Valor contratado: R$ 4.000 (fonte: PROPOSTA-COMERCIAL.md, aprovada em 2026-07-10).

PROJEÇÃO
Receita estimada no cenário base: R$ 18.000 (hipótese: manutenção da
taxa de conversão atual — ver projeção completa na seção Financeiro).

HIPÓTESE
A campanha pode converter melhor com prova social local (não
confirmado — sugerir teste A/B).

PENDÊNCIA
Definir responsável pela aprovação final do roteiro.

NÃO INFORMADO
Orçamento de mídia para a fase 2 ainda não foi definido.

CONFLITO
"_memoria.json" registra orçamento de R$ 5.000; PROPOSTA-COMERCIAL.md
(mais recente) registra R$ 4.500 — usada a versão mais recente, conflito
sinalizado para revisão.
```

## Exemplo de geração — dossiê de projeto

Usuário: "Gera o arquivo do NotebookLM do projeto de lançamento do
Cliente A."

1. Confirma workspace `workspaces/clientes/cliente-a/` e projeto
   `lancamento-produto-x`.
2. Escaneia `workspaces/clientes/cliente-a/projetos/lancamento-produto-x/`
   (nunca sobe para fora dessa pasta nem lê `cliente-b/`).
3. Mostra: "12 arquivos vão entrar (PROJETO.md, DIAGNOSTICO.md,
   PROPOSTA-COMERCIAL.md, CAMPANHA.md, FUNIL.md...); 2 ficaram de fora
   (rascunho.tmp, uma versão antiga do orçamento em `historico/`);
   1 conflito encontrado entre memória e proposta (ver acima)."
4. Gera `DOSSIE_PROJETO_ATUAL.docx` em arquivo temporário, valida,
   promove com troca atômica.
5. Pergunta qual resultado o usuário quer no NotebookLM → "proposta" →
   gera `PROMPT_NOTEBOOKLM_ATUAL.txt` com o mini-prompt de proposta.
6. Informa:
   ```
   Dossiê: workspaces/clientes/cliente-a/projetos/lancamento-produto-x/notebook-lm/DOSSIE_PROJETO_ATUAL.docx
   Prompt: .../PROMPT_NOTEBOOKLM_ATUAL.txt
   Manifesto: .../MANIFESTO_FONTES.json (12 fontes, 1 conflito sinalizado)
   Status: atual (v1)
   ```

## Exemplo — usuário pede "tudo"

Usuário: "Gera o NotebookLM de tudo do Cliente A."

Resposta: explica a diferença entre dossiê de empresa (resume todos os
projetos + dados institucionais) e dossiê de projeto (detalha um
projeto só), pergunta qual o usuário realmente precisa, e recomenda o
dossiê de empresa se a intenção for visão geral, ou pede o nome do
projeto se a intenção for detalhe.

## Contraexemplo — nunca fazer

Gerar `DOSSIE_EMPRESA_ATUAL.docx` incluindo, sem pedido explícito,
dados de `workspaces/clientes/cliente-b/` dentro do dossiê de
`cliente-a/` — mesmo que ambos usem o mesmo fornecedor ou campanha
parecida. Isso só pode acontecer num "projeto compartilhado"
explicitamente autorizado e documentado (ver `docs/MODOS_DE_USO.md`).
