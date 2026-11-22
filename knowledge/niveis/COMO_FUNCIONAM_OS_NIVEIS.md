# Como funcionam os níveis

O Sistema LKT guarda a inteligência por trás dos níveis — um nível
nunca é só um nome, número, selo ou faixa de preço. É uma estrutura
explicável, verificável, versionada e reutilizável.

## O que o sistema registra para cada nível

Definição, objetivo, contexto de uso, regras de classificação,
evidências necessárias, entregáveis mínimos, entregáveis opcionais,
itens não inclusos, dependências obrigatórias, tarefas relacionadas,
papéis responsáveis, faixas de prazo, faixas de custo, critérios de
validação, indicadores, riscos, restrições, casos anteriores,
aprendizados, templates reutilizáveis, condições para avançar,
condições para recuar, gatilhos de revisão, versão da regra.

Ver `schemas/level-definition.schema.json` para o formato exato.

## O que o sistema precisa conseguir responder

Por que este projeto foi classificado neste nível; quais evidências
sustentam a classificação; o que precisa ser entregue; o que ainda
está faltando; o que depende de outra etapa; qual é a faixa provável
de prazo e custo; qual nível é atual; qual nível é recomendado; qual
diferença existe entre os dois; quais ações fecham essa diferença;
quando a classificação deve ser revisada.

## Não existe um nível único universal

Uma empresa pode estar avançada em operação, básica em marketing,
intermediária em financeiro, inicial em dados, madura em atendimento e
sem estrutura comercial — tudo ao mesmo tempo. Um único número não
representa isso. Por isso o sistema usa **conjuntos de níveis
independentes por dimensão** — ver
`knowledge/niveis/NIVEIS_E_DIMENSOES.md`.

Nenhum projeto é obrigado a classificar todas as dimensões. Uma tarefa
simples de correção de arquivo pode não precisar de nível nenhum; uma
estruturação empresarial, financeira, digital, comercial ou
operacional provavelmente precisa de uma ou mais.

## Conceitos

- **Conjunto de níveis** — uma escala aplicada a uma dimensão (ex.:
  maturidade digital: base → estruturada → integrada → orientada por
  dados). `schemas/level-set.schema.json`.
- **Nível atual** — classificação baseada em evidências disponíveis.
  `schemas/level-assessment.schema.json`.
- **Nível recomendado** — estado adequado para alcançar o objetivo do
  projeto (nunca o nível mais alto por padrão).
  `schemas/level-recommendation.schema.json`.
- **Lacuna** — diferença entre o nível atual e o recomendado.
- **Plano de avanço** — ações, entregáveis, dependências, prazo e
  investimento necessários para reduzir a lacuna. Skill
  `gerar-plano-de-avanco`.
- **Perfil de entrega** — pacote estrutural ligado a um nível, sem
  obrigar que todo cliente receba exatamente a mesma proposta.
  `schemas/deliverable-profile.schema.json`,
  `catalogo/perfis-de-entrega/`.
- **Regra de classificação** — condição que usa evidência para sugerir
  um nível. `schemas/classification-rule.schema.json`. Ver
  `knowledge/niveis/REGRAS_DE_CLASSIFICACAO.md`.
- **Exceção** — situação em que a regra padrão não representa
  corretamente o projeto (registrada, nunca silenciosa).
- **Revisão humana** — decisão registrada que confirma ou altera a
  classificação automática. Skill `revisar-nivel`.

## As camadas internas do Sistema LKT

O Sistema LKT é um sistema único, com quatro camadas internas
(inteligência, operacional, documental, integração) — não existe outro
produto separado. Ver `knowledge/niveis/NIVEIS_E_CAMADA_OPERACIONAL.md`
e `docs/NIVEIS_NA_PROPOSTA_COMERCIAL.md` para a divisão de
responsabilidade completa. Resumo: a camada de inteligência pensa
(classifica, explica, recomenda); a camada operacional executa e mede;
a camada documental (proposta comercial, dossiê) traduz para o cliente
só o que ele precisa decidir.
