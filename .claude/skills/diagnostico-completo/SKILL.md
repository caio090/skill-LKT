---
name: diagnostico-completo
description: >
  Orquestra o diagnóstico completo de um cliente/projeto novo, do
  contexto ao plano de ação, encadeando as skills menores do módulo de
  diagnóstico e estratégia. Use quando o usuário pedir "faz o diagnóstico
  completo", "quero o pacote inteiro de diagnóstico e estratégia pra esse
  cliente novo".
---

# diagnostico-completo — Orquestrador de diagnóstico e estratégia

Encadeia as skills do módulo de diagnóstico/estratégia na ordem correta.
Não repete o conteúdo de cada skill — só coordena a sequência e garante
que nada seja pulado.

## Quando usar

Início de um projeto novo (depois de `novo-projeto`) quando o usuário
quer o pacote completo, não uma etapa isolada.

## Quando não usar

Quando o usuário só quer uma etapa específica (ex.: só pesquisa de
mercado) — chamar a skill correspondente direto.

## Entradas

Projeto/cliente ativo já criado por `novo-projeto`.

## Dependências

`diagnostico-negocio`, `pesquisa-mercado`, `analisar-concorrentes`,
`analisar-publico`, `posicionamento`, `criar-produto-e-oferta`,
`plano-estrategico`.

## Contexto que deve ser carregado

`.lkt-system/estado/contexto-ativo.json` para saber o projeto ativo.

---

## Workflow

Ordem mínima obrigatória, sem pular pra produção de conteúdo:

1. Contexto (herdado de `novo-projeto`/`00-contexto/`).
2. `diagnostico-negocio` — problema, situação atual, o que funciona/trava.
3. `analisar-publico` — quem compra de verdade.
4. `pesquisa-mercado` — se precisar de dado externo de mercado.
5. `analisar-concorrentes` — se precisar mapear concorrência real.
6. `posicionamento` — mensagem central.
7. `criar-produto-e-oferta` — se o projeto envolver oferta nova/revisão.
8. Financeiro básico — encaminhar pro módulo financeiro se houver
   decisão de preço/viabilidade envolvida.
9. Operação — registrar no diagnóstico o que a operação atual suporta ou
   não suporta da ação planejada.
10. `plano-estrategico` — oportunidades, riscos, plano de ação,
    indicadores.

Entre cada etapa, mostrar um resumo curto do que foi encontrado antes de
seguir pra próxima — não rodar tudo em silêncio e só entregar no final.

## Saídas

Todos os arquivos de `01-diagnostico/` e `02-estrategia/` preenchidos.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/01-diagnostico/` e `02-estrategia/`.

## Regras

- Nunca pular direto pra produção de conteúdo/entrega.
- Cada etapa só é pulada se genuinamente não se aplicar ao projeto (ex.:
  projeto sem oferta nova não precisa de `criar-produto-e-oferta`) — e
  isso é registrado, não silenciado.

## Critérios de qualidade

Ao final, `PROJETO.md` tem indicador de sucesso e plano de ação
claramente registrados.

## Critérios de validação

Todas as etapas aplicáveis foram executadas ou explicitamente
descartadas com motivo.

## Limitações

Não substitui a profundidade de cada skill individual — é só a
orquestração da sequência.

## Contrato de handoff

`anti-chat` (quality gate contra recomendação genérica) antes de
entregar; ao final, encaminha pro módulo de execução correspondente à
primeira ação prioritária do plano.

## Exemplos de gatilhos positivos

- "Faz o diagnóstico completo desse cliente novo"
- "Quero o pacote inteiro antes de começar a produzir"

## Exemplos de gatilhos negativos

- "Só quero saber quem são os concorrentes" (é `analisar-concorrentes`
  isolado)
