---
name: qa-e2e-playwright
description: >
  Cria e executa testes ponta a ponta com Playwright em ambiente isolado:
  navegação, formulários, filtros, estados vazios e de erro, mobile e
  desktop, acessibilidade básica por teclado, rotas protegidas, carrinho
  e checkout só em sandbox, com API mockada quando o serviço real for
  arriscado. Use quando o usuário pedir "testa o site de ponta a ponta",
  "cria testes E2E", "roda o Playwright", "smoke test no PR".
---

# qa-e2e-playwright — Testes ponta a ponta seguros

## Quando usar

Validar fluxos reais de uma interface (site, loja, app web) antes de
considerar a entrega pronta, ou criar a suíte de smoke tests do PR.

## Quando não usar

- Checklist geral de qualidade, segurança e observabilidade → `qa`
  (esta skill complementa o `qa`; não o substitui).
- Revisão de código → `revisar-codigo`.
- Teste de workflow n8n → `n8n-workflow-check`.

## Pré-condições (verificar antes de escrever teste)

1. Playwright disponível no projeto: `npx playwright --version`. Se não
   estiver, propor a instalação (`npm i -D @playwright/test` e
   `npx playwright install chromium`) e **esperar aprovação** — não
   instalar dependência sozinho. Licença do Playwright: Apache-2.0.
2. Alvo do teste é local, preview isolado ou staging. **Nunca** apontar
   para produção. Se a preview usar banco, confirmar que é banco de
   teste (variável de ambiente, nome do projeto) antes de rodar.
3. Nenhuma credencial real em código. Usuário de teste vem de variável
   de ambiente do projeto (ex.: `E2E_USER`) e só em ambiente sintético.

## Workflow

1. **Mapear fluxos críticos** (do briefing, do `ecommerce-loja` ou do
   `pagina-e-site`): no máximo 5–8 para o smoke test do PR.
2. **Configurar projetos** em `playwright.config`: `chromium` desktop e
   um dispositivo móvel (`devices["Pixel 7"]` ou `iPhone 14`). Firefox e
   WebKit só se o público justificar.
3. **Escrever testes** com seletores semânticos e estáveis:
   `getByRole`, `getByLabel`, `getByText` — nunca classe CSS gerada.
   Sem `waitForTimeout` fixo: usar asserções com espera automática
   (`await expect(...).toBeVisible()`).
4. **Cobrir**: navegação e links, menus, formulários (válido e
   inválido), filtros, estados vazio/erro/carregamento, responsividade
   (sem rolagem horizontal: `scrollWidth <= clientWidth`), foco por
   teclado (`Tab` alcança CTA e o foco é visível), rotas protegidas
   redirecionando quem não tem permissão.
5. **Isolar efeitos externos** com `page.route()`: pagamento, WhatsApp,
   e-mail, webhooks e APIs de terceiros respondem com mock. Checkout só
   com gateway em modo sandbox ou totalmente mockado.
6. **Artefatos**: `trace: "on-first-retry"`, `screenshot:
   "only-on-failure"`, retenção controlada (pasta ignorada no Git).
   Screenshot só de tela com dados fictícios.
7. **Rodar** `npx playwright test` e reportar.
8. **Relatório**: para cada falha, passo a passo de reprodução, esperado
   vs. obtido, trace/screenshot, severidade. Reteste após correção.

Exemplo completo e executável (página fictícia + spec + config) em
`exemplos/`. Para rodar: `cd exemplos && npx playwright test`.

## Critérios de reprovação

- Fluxo crítico falha em qualquer projeto (desktop ou mobile).
- Rolagem horizontal no mobile.
- CTA principal inalcançável por teclado.
- Qualquer requisição real a pagamento, mensageria ou produção durante
  o teste (o teste deve falhar se isso acontecer — ver o bloqueio de
  rede no exemplo).

## Saídas

Arquivos de teste no projeto, comando para rodar, relatório de
execução com aprovados/reprovados e artefatos das falhas.

## Caminho de salvamento

Testes: `tests/e2e/` do projeto. Relatório:
`<pasta-do-projeto-ativo>/07-tecnologia/qa-e2e-<entrega>.md`.

## Regras

- Nunca rodar contra produção, nunca criar pedido/cobrança/mensagem real.
- Nunca usar telefone, e-mail ou cartão reais em fixture.
- Não declarar teste aprovado sem a saída do comando como evidência.
- Se o Playwright não puder ser executado no ambiente, dizer isso e
  entregar os testes como "não executados".
