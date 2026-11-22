# Ontologia — processos, fluxos, funis, pipelines, jornadas e campanhas

Define os conceitos que atravessam módulos, pra que o sistema escolha o
modelo certo em vez de chamar tudo de "funil". Toda skill ou módulo que
lidar com conversão, oportunidade ou fluxo de trabalho consulta este
documento antes de estruturar algo novo.

## Tabela de decisão

| O usuário quer... | Use |
|---|---|
| Acompanhar tarefas internas (quem faz o quê, em que ordem) | **Fluxo de trabalho** |
| Saber onde cada negociação/oportunidade está agora | **Pipeline** |
| Medir passagem e perda de pessoas entre etapas | **Funil** |
| Organizar uma ação com prazo, canais e orçamento | **Campanha** |
| Compreender a experiência completa da pessoa com a empresa | **Jornada** |
| Desenhar uma ação interna repetível (não voltada a conversão) | **Processo** |

## Conceitos

### Processo

O conjunto de ações que a empresa realiza para produzir um resultado.

**Definição:** sequência de etapas com responsável, regra e ferramenta,
gerando um artefato ou resultado.
**Quando usar:** para descrever "o que a empresa faz" de forma estável
(ex.: atender → diagnosticar → apresentar proposta → negociar → fechar).
**Quando não usar:** quando o objetivo é medir conversão/perda entre
etapas (aí é funil) ou acompanhar item por item em andamento (aí é
pipeline).
**Exemplo:** processo de atendimento de um restaurante: pedido →
preparo → entrega → cobrança.
**Entidades relacionadas:** papel responsável, ferramenta, artefato.
**Dados mínimos:** etapas, responsável por etapa, regra, ferramenta,
saída.
**Métricas possíveis:** tempo de ciclo, taxa de erro, gargalo.
**Erro comum:** confundir processo com funil só porque tem etapas —
processo não conta "quantas pessoas passaram", conta "o que foi feito".

### Fluxo de trabalho

A sequência operacional de tarefas, aprovações, responsáveis e estados.

**Definição:** ordem de tarefas com dependência, responsável e
critério de avanço/bloqueio.
**Quando usar:** produção interna repetível (briefing → roteiro →
produção → revisão → aprovação → publicação).
**Quando não usar:** para medir conversão de pessoas (funil) ou
acompanhar oportunidade comercial (pipeline).
**Exemplo:** fluxo de criação de conteúdo.
**Entidades relacionadas:** tarefa, responsável, aprovador, dependência,
arquivo gerado, status.
**Dados mínimos:** tarefas, ordem, responsável, aprovador, status atual.
**Métricas possíveis:** tempo por etapa, taxa de retrabalho.
**Erro comum:** tratar fluxo de trabalho de conteúdo como "funil
comercial" — não é conversão de pessoa, é produção de artefato.

### Funil

Representação de quantidade e taxa de passagem entre etapas.

**Definição:** contagem de uma entidade (visitante, lead, candidato)
em cada etapa, com taxa de conversão entre elas.
**Quando usar:** quando existe perda mensurável entre etapas e o
objetivo é entender/melhorar essa passagem.
**Quando não usar:** para fluxo financeiro sem motivo analítico real
(nunca renomear fluxo de caixa como "funil" só por hábito de
linguagem), nem para tarefa interna sem entidade contável passando por
etapas.
**Exemplo:** 1.000 visualizações → 100 cliques → 40 respostas → 15
visitas à oferta → 3 compras.
**Entidades relacionadas:** evento de conversão, campanha, página,
oferta.
**Dados mínimos:** etapas, entidade contada, quantidade por etapa,
período, origem.
**Métricas possíveis:** taxa por etapa, taxa total, maior ponto de
perda.
**Erro comum:** medir só a taxa total e não identificar em qual etapa
específica está a perda.

### Pipeline

Visualização operacional das oportunidades em andamento agora.

**Definição:** lista/quadro de itens (leads, candidatos, pedidos) com
etapa atual, responsável e próxima ação.
**Quando usar:** quando existe um conjunto de itens individualizados
que precisam de acompanhamento um a um.
**Quando não usar:** para medir taxa agregada de conversão (isso é
funil) — pipeline é sobre "onde está cada item", não "quantos
passaram".
**Exemplo:** João em diagnóstico, Maria com proposta enviada, Pedro em
negociação.
**Entidades relacionadas:** oportunidade, responsável, critério de
entrada/saída de etapa.
**Dados mínimos:** etapa atual, data de entrada, responsável, próxima
ação, prazo.
**Métricas possíveis:** tempo parado numa etapa, itens sem próxima
ação definida, valor esperado.
**Erro comum:** deixar item no pipeline sem próxima ação nem prazo —
vira lista morta, não pipeline ativo.

### Jornada

Caminho da pessoa ao longo de toda a relação com a empresa.

**Definição:** sequência de fases da experiência da pessoa, com o que
ela pensa, precisa e enfrenta em cada uma.
**Quando usar:** para desenhar experiência completa, não só conversão
comercial (inclui pós-venda, uso, renovação, indicação).
**Quando não usar:** quando o objetivo é só medir números de conversão
(funil) ou acompanhar oportunidades ativas (pipeline).
**Exemplo:** descoberta → consideração → compra → onboarding → uso →
renovação → indicação.
**Entidades relacionadas:** ponto de contato, conteúdo, atendimento,
produto.
**Dados mínimos:** fases, o que a pessoa sente/precisa em cada uma,
pontos de contato.
**Métricas possíveis:** satisfação por fase, tempo até renovação, taxa
de indicação.
**Erro comum:** desenhar jornada só até a venda e ignorar onboarding,
uso e retenção.

### Campanha

Conjunto coordenado de ações, ativos, canais, prazos e orçamento para
alcançar um objetivo específico.

**Definição:** ação com nome, objetivo, público, oferta, canais,
período, orçamento, ativos e métricas próprias.
**Quando usar:** quando há um objetivo específico com prazo definido
(lançamento, evento, promoção) — não é operação contínua.
**Quando não usar:** para descrever a operação recorrente da empresa
sem prazo (isso é processo/módulo, não campanha).
**Exemplo:** campanha de lançamento de um curso, com anúncios, página,
e-mails e prazo de 30 dias.
**Entidades relacionadas:** funil (uma campanha pode gerar vários),
página, ativo, evento de conversão, canal.
**Dados mínimos:** objetivo, público, oferta, canais, período,
orçamento, funil associado, métricas.
**Métricas possíveis:** custo por resultado, ROI/ROAS, taxa de
conversão do funil associado.
**Erro comum:** confundir pipeline de campanhas (onde cada campanha
está no processo de planejamento/produção/aprovação) com o funil de
conversão que a campanha gera — são coisas diferentes.

## Aplicação por área (não obrigatória em toda empresa)

- **Marketing:** funis de alcance→visita→lead ou anúncio→clique→
  formulário→lead; pipeline de campanhas (planejamento → produção →
  aprovação → ativa → encerrada). Não confundir os dois.
- **Comercial:** funil lead→qualificado→diagnóstico→proposta→cliente;
  pipeline com cada oportunidade em sua etapa.
- **Conteúdo:** fluxo de trabalho (ideia→briefing→roteiro→produção→
  aprovação→agendamento→publicação); funil de conteúdo só quando
  houver objetivo de conversão (visualização→engajamento→contato).
- **Produto digital:** funil visitante→cadastro→ativação→assinatura;
  pipeline operacional de ideias→priorizadas→desenvolvimento→teste→
  publicadas.
- **Recrutamento:** funil candidato→triagem→entrevista→aprovado→
  contratado; pipeline por candidato.
- **Atendimento:** processo (entrada→triagem→análise→solução→
  encerramento); pipeline de chamados é possível, mas nunca forçar
  formato comercial num processo de suporte.
- **Financeiro:** fluxo de caixa, contas a pagar/receber, orçamento,
  projeções, conciliação — nunca renomear como "funil" sem motivo
  analítico real (passagem e perda mensuráveis).
- **Logística:** processo, fluxo de pedido, fila, rota, status,
  capacidade, SLA, ocorrência. Funil de pedidos só quando houver
  análise de passagem e perda entre etapas.

## Ciclo de vida integrado (referência, não obrigatório usar inteiro)

```
Conteúdo → marketing → campanha → lead → pré-venda → oportunidade →
venda → onboarding → entrega → uso → retenção → renovação → indicação
```

Cada etapa pode se conectar a: projeto, campanha, contato, empresa,
oportunidade, tarefa, arquivo, página, conteúdo, conversa, orçamento,
contrato, receita, custo, métrica, responsável por papel, decisão,
automação. O diagnóstico decide quais conexões fazem sentido para cada
workspace — nunca obrigar o ciclo completo.

## Pré-venda e qualificação

Pré-venda é a fase de identificação, coleta de informação, triagem e
qualificação anterior à venda — pode ser humana, automática ou híbrida
(formulário, quiz, conversa no WhatsApp, agente, diagnóstico inicial,
ligação, análise de perfil).

Um quiz só é classificado como qualificação quando as respostas
influenciam decisão de avançar, priorizar, segmentar ou encaminhar a
pessoa. Se as perguntas servem só para curiosidade, retenção ou
aquecimento, classificar como interação/aquecimento, não como
pré-venda.

## Atribuição e dupla contagem

Uma campanha pode gerar vários funis; um funil pode receber tráfego de
várias campanhas. Toda oportunidade preserva sua origem (campanha,
canal, conteúdo, anúncio, página, formulário, quiz, indicação, evento,
atendimento). Regras de atribuição precisam ser documentadas
explicitamente por workspace: primeiro contato, último contato,
atribuição escolhida manualmente, ou origem desconhecida — nunca contar
a mesma conversão duas vezes sem essa regra declarada.

Ver também `schemas/processo.schema.json`, `schemas/funil.schema.json`,
`schemas/pipeline.schema.json`, `schemas/campanha.schema.json`,
`schemas/jornada.schema.json`, `docs/ENTENDA_FUNIL_PIPELINE_PROCESSO.txt`
(versão para usuário leigo).
