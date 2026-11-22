# Workflow — automações

Sequência de referência para transformar uma etapa recorrente em
automação. Executada por `automatizar-fluxo`.

```
Identificar etapa candidata (de processo, funil ou pipeline)
  → Definir gatilho, condição e ação
  → Classificar nível de autonomia (0 a 5 — nunca o mais alto por padrão)
  → Checar se a ação é sempre crítica (docs/SEGURANCA_E_PERMISSOES.md)
  → Salvar com status "pausada"
  → Ativar somente após confirmação explícita separada
```
