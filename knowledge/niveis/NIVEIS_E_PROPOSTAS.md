# Níveis e propostas

A proposta comercial é a camada que traduz a inteligência interna dos
níveis para o cliente — nunca expõe o raciocínio interno completo.
Ver `docs/NIVEIS_NA_PROPOSTA_COMERCIAL.md` para a regra completa e
`schemas/deliverable-profile.schema.json` para o formato de "perfil de
entrega" que liga um nível a um pacote comercial.

## O que a proposta recebe do nível

Problema, prioridade, objetivo, fase recomendada, entregáveis
selecionados, prazo, investimento, dependências, responsabilidades,
limites, opcionais, possibilidades futuras.

## O que a proposta nunca recebe automaticamente

Todas as tarefas internas, todos os riscos internos, margem, custo por
colaborador, anotações confidenciais, pontuação técnica completa,
casos de outros clientes, raciocínio privado, ou qualquer dado que não
ajude a decisão do cliente.

## Fases possíveis na proposta (linguagem comercial, não o nível interno)

Estrutura inicial, implantação, evolução, escala futura — o nome do
nível interno (ex.: "maturidade digital: estruturada") só aparece na
proposta quando isso ajudar o cliente a entender; caso contrário, usa
só a linguagem de fase/pacote.

## Skill responsável

`gerar-proposta-a-partir-do-nivel` — consome a recomendação de nível
(`schemas/level-recommendation.schema.json`) e o perfil de entrega
correspondente, produz só a camada comercial, e entrega para
`proposta-e-precificacao` fechar a composição de preço.
