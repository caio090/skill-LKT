# Política de sandbox: Supabase, n8n, pagamentos, WhatsApp e deploy

Vale para toda skill, teste e exemplo da biblioteca LKT. Pedido de
diagnóstico nunca vira alteração em produção.

## Supabase / Postgres

- Skills (`planejar-banco-de-dados`, `supabase-postgres-best-practices`)
  **orientam e propõem**. Migração é entregue como arquivo SQL para revisão.
- Teste de skill usa banco local (`supabase start`), branch de
  desenvolvimento ou schema temporário. Nunca o projeto de produção.
- Antes de rodar qualquer coisa, confirmar o alvo: nome do projeto e
  variável de ambiente (`SUPABASE_URL`) apontam para dev/teste.
- Política RLS só é aplicada depois de teste por papel (anon, usuário,
  admin) no sandbox, com a matriz de permissão registrada.
- Índices, constraints e transações são validados no ambiente descartável.

## n8n e automações

- `n8n-workflow-check` entrega workflow com `active: false`; ativação é
  decisão do responsável.
- Teste usa fixtures sintéticas e o script local
  `scripts/check_workflow.py`; não dispara webhook real.
- Credenciais ficam na instância n8n; nunca em JSON, Code node ou repositório.
- Envio de mensagem (WhatsApp, e-mail, SMS) em teste só com autorização
  explícita e destinatário de teste combinado.
- Toda automação documenta: chave de idempotência (evitar cobrança ou
  mensagem duplicada), política de retentativa com limite, e o que
  acontece em falha parcial.

## Pagamentos e e-commerce

- Checkout só em modo sandbox do gateway ou mockado (`page.route`).
- Nunca alterar preço, estoque, cupom ou campanha reais em teste.
- Cartão, CPF, telefone e e-mail de fixture são fictícios.

## WhatsApp

- Lojas sem checkout usam link `wa.me` com mensagem pronta; o cliente
  envia. Sem disparo automatizado.

## Deploy e Git

- Nenhuma skill, teste ou CI faz deploy (Vercel ou outro) ou merge.
- A CI deste repositório roda só validação e testes (`.github/workflows/validar.yml`).
- Nenhum force push, rebase destrutivo ou reescrita de histórico.

## Dados de clientes

- Fixtures e exemplos só com dados fictícios.
- Nada de `.env`, dumps de banco, históricos de sessão, logs com telefone
  ou mensagens reais, tabelas de preço internas.
