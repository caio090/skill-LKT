# Níveis e a camada operacional

Registra, como regra institucional, como a inteligência dos níveis se
conecta à execução real dentro do Sistema LKT — um sistema único, sem
outro produto separado. Ver `docs/CONTRATO_DE_DADOS_DOS_NIVEIS.md`
para o contrato de dados completo entre as camadas internas.

## O Sistema LKT é um único sistema, com quatro camadas

1. **Camada de inteligência** — diagnóstico, memória, regras, níveis,
   projeções, recomendações, aprendizados.
2. **Camada operacional** — projetos, tarefas, entregáveis, prazos,
   custos, métricas, progresso, validações.
3. **Camada documental** — propostas, relatórios, dossiês,
   apresentações, arquivos Word, prompts, templates.
4. **Camada de integração** — importação, exportação, eventos,
   contratos de dados, módulos externos futuros.

Todas as quatro pertencem ao Sistema LKT — não são produtos separados,
nem uma interface distinta com nome próprio. Quando a interface
operacional for mencionada, chamá-la de "interface do Sistema LKT",
"camada operacional do Sistema LKT", "painel do Sistema LKT" ou
"aplicação do Sistema LKT", conforme o contexto — nunca com outro
nome de produto.

## Como a inteligência dos níveis se conecta à operação

A camada de inteligência entende, diagnostica, documenta, classifica,
recomenda e projeta. A camada operacional mostra, organiza, calcula,
distribui, acompanha, alerta, registra execução, mede e atualiza
progresso. A camada operacional **não inventa a inteligência dos
níveis** — consome regras, recomendações e estruturas produzidas pela
camada de inteligência.

## Fluxo entre as camadas

```
Camada de inteligência (classifica + recomenda + explica)
  → exporta: exports/niveis/{workspace}/{projeto}/level-recommendation.json
    → Camada operacional (executa, mede, acompanha, devolve progresso)
      → Camada de inteligência revisa a recomendação com o retorno (revisar-nivel)
  → gerar-proposta-a-partir-do-nivel traduz para a camada documental
    → proposta-e-precificacao fecha escopo e preço
```

Esta consolidação **não cria integração remota** — só o contrato, o
formato de arquivo, um exemplo e um teste local (ver
`docs/CONTRATO_DE_DADOS_DOS_NIVEIS.md`).

## A proposta comercial

A proposta comercial não é outro sistema — é um documento gerado pelo
Sistema LKT (camada documental). Ver
`knowledge/niveis/NIVEIS_E_PROPOSTAS.md` e
`docs/NIVEIS_NA_PROPOSTA_COMERCIAL.md`.
