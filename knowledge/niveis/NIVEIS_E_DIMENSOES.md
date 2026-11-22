# Níveis e dimensões

> **RASCUNHO DE REFERÊNCIA.** As dimensões e os nomes de nível abaixo
> são um ponto de partida configurável, não uma regra oficial fixa.
> Nenhuma instalação é obrigada a usar exatamente estes nomes ou estas
> quatro faixas — ajuste em `catalogo/niveis/` conforme os casos reais
> da instalação. Só passa a valer como regra oficial depois de
> validado com uso real (ver "Revisão humana" em
> `COMO_FUNCIONAM_OS_NIVEIS.md`).

## Por que várias dimensões, nunca uma só

Uma empresa não tem "um nível" — ela tem maturidade diferente em cada
frente. Um projeto também pode precisar de níveis diferentes por
dimensão (ex.: complexidade alta, mas risco baixo).

## Dimensões iniciais sugeridas

- **Maturidade empresarial** — geral, quando nenhuma dimensão
  específica for necessária.
- **Complexidade do projeto** — quantidade de partes móveis,
  dependências, integrações.
- **Profundidade da entrega** — o quanto uma entrega vai além do
  mínimo funcional.
- **Maturidade digital** — presença online, ferramentas, automação.
- **Maturidade financeira** — controle de custo, fluxo de caixa,
  precificação, projeção.
- **Maturidade comercial** — processo de vendas, funil, pipeline, CRM.
- **Maturidade operacional** — processos documentados, capacidade,
  qualidade.
- **Maturidade logística** — estoque, fornecedores, entrega, SLA.
- **Maturidade de dados** — coleta, consolidação, uso de métrica na
  decisão.
- **Autonomia da empresa** — quanto a empresa consegue operar sem
  depender do prestador.
- **Integração tecnológica** — quantidade e qualidade de integrações
  entre ferramentas.
- **Risco do projeto** — probabilidade e impacto de algo dar errado.

## Regra de uso

Nunca obrigar todas as dimensões em todo projeto — usar só as
pertinentes ao diagnóstico (`diagnostico-empresarial` decide isso).
Um projeto de correção pontual pode não precisar de nenhuma dimensão
classificada.

## Exemplo de conjunto de níveis (rascunho)

```
Dimensão: maturidade digital
Níveis (em ordem):
  1. base            — presença mínima, sem processo definido
  2. estruturada      — processo definido, ferramentas básicas ativas
  3. integrada          — ferramentas conectadas, dado central
  4. orientada por dados  — decisão guiada por métrica consolidada
```

Cada nível desse conjunto é uma instância completa de
`schemas/level-definition.schema.json` — com critérios, evidências,
entregáveis, prazo/custo em faixa, etc. Ver
`catalogo/niveis/maturidade-digital.exemplo.json` para o exemplo
completo (marcado como rascunho).

## Faixas de prazo e custo nunca são preço final

Ver `knowledge/niveis/NIVEIS_E_PROJECOES.md` — faixa alimenta
projeção, projeção nunca é garantia, garantia nunca é automática.
