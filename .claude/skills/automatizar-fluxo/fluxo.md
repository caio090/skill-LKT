FLUXO — automatizar-fluxo

1. Coletar respostas de perguntas.txt.
2. Classificar o nível de autonomia (0 a 5) — nunca assumir o mais
   alto sem pedido explícito.
3. Checar se a ação é sempre crítica; se for, forçar confirmação por
   execução mesmo em nível 4.
4. Preencher todos os campos de schemas/regra-automacao.schema.json.
5. Salvar com status "pausada".
6. Só ativar (mudar status para "ativa") depois de confirmação
   explícita separada, mostrando o resumo da regra.
