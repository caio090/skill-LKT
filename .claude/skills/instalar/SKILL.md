---
name: instalar
description: >
  Instala o Sistema LKT no negócio ou projeto onde a pasta foi copiada. Entrevista
  sobre empresa, tom de voz, foco atual, identidade visual e ferramentas, e
  preenche `_memoria/empresa.md`, `_memoria/preferencias.md`,
  `_memoria/estrategia.md`, `_memoria/marca.md`, `_memoria/produtos-e-servicos.md`
  e `_memoria/ferramentas.md`. Use quando o usuário pedir explicitamente
  "instalar o sistema", "rodar /instalar", "configurar o LKT aqui" ou "primeiro
  setup", ou quando abrir uma pasta com a estrutura do sistema mas memória
  ainda em branco.
---

# instalar — Instalação inicial do Sistema LKT

Esse é o primeiro comando que roda depois de copiar o LKT System para uma
pasta de projeto. Não pode falhar e não pode soar burocrático. Trata como
conversa de descoberta — pergunta uma coisa por vez, escuta de verdade,
não enfileira tudo. O objetivo é o sistema sair daqui sabendo quem é o
negócio, como ele fala, e onde está o atrito do dia a dia.

## Workflow

Pré-checagem → Fase 1 (perfil) → Fase 2 (entrevista) → Fase 3
(preenchimento) → Fase 4 (resumo) → Fase 5 (nome da pasta, se
aplicável) → Fase 6 (próximos passos). Detalhado abaixo.

## Pré-checagem

### 1. Nome da pasta

Conferir o nome da pasta atual. Se for `lkt system`, `LKT System`,
`lkt-system`, `rec-os`, `REC-OS`, `mazyos`, `MazyOS` ou variação genérica
do nome do próprio sistema (não do negócio):

> "Notei que a pasta atual ainda tem nome genérico do sistema
> ('<nome-atual>'), não o nome do negócio. Isso não afeta o
> funcionamento — só sugiro renomear no fim, se fizer sentido pra você.
> Antes de sugerir, vou checar se tem algo (Git, scripts, atalhos) que
> dependa desse nome específico. Bora seguir com o setup?"

Registrar mentalmente o nome atual pra usar na Fase 5.

### 2. Arquivos de contexto

Conferir se algum arquivo de memória já está preenchido (não é
placeholder em branco):

- `_memoria/empresa.md`
- `_memoria/preferencias.md`
- `_memoria/estrategia.md`
- `_memoria/marca.md`
- `_memoria/produtos-e-servicos.md`
- `_memoria/ferramentas.md`

Se algum já tiver conteúdo real, perguntar:

> "Já tem contexto preenchido aqui. Quer que eu sobrescreva (recomeçar do
> zero) ou complemente só o que falta?"

Se for setup limpo (tudo em branco), seguir direto.

---

## Fase 1 — Escolha do perfil

Perguntar qual perfil mais combina com o negócio:

1. **Solopreneur / criador solo** — uma pessoa só, mistura de marca
   pessoal e negócio
2. **Freelancer** — atende clientes, organiza por projeto/cliente
3. **Agência / consultoria** — equipe pequena entregando pra vários
   clientes (ex.: a própria instalação)
4. **Empresa** — negócio estabelecido com setores (marketing, comercial,
   financeiro, etc.), atendendo o próprio negócio ou clientes internos

O perfil não troca a estrutura do sistema (ela é a mesma pra todos) —
só calibra que perguntas priorizar e que módulos (`catalogo/modulos/`) tendem a
ser usados primeiro.

---

## Fase 2 — Entrevista

Fazer essas perguntas em ordem, esperando a resposta de cada uma antes de
seguir. Se vier resposta vaga, repetir uma vez pedindo concretude. Não
insistir mais que isso — registrar o que vier.

**Sobre o negócio:**
1. "Como você chama o que você faz? (nome da empresa, ou seu nome se for
   marca pessoal)"
2. "O que o negócio entrega, em uma frase do jeito que você falaria pro
   vizinho?"
3. "Quem te paga? (perfil de cliente real — descreve em uma ou duas
   frases, sem persona genérica). Se atende vários segmentos diferentes,
   lista os principais."
4. "Você toca sozinho ou tem equipe? Se tem, quantos e cada um fazendo o
   quê?"

**Sobre voz:**
5. "Me cola um exemplo da sua escrita — uma legenda, um email pra
   cliente, qualquer coisa real e recente. Assim calibro o jeito de
   escrever sem precisar adivinhar."
6. "O que te dá ranço quando alguém escreve assim? (ex.: 'vamos juntos!',
   emoji em email formal, 'caro cliente', jargão de guru, 'alavancar',
   'sinergia')"

**Sobre foco:**
7. "Qual o gargalo do negócio hoje? O que tá segurando ele de crescer?"
8. "Se eu pudesse tirar UMA coisa que você repete toda semana das suas
   costas, qual seria?"

**Sobre identidade visual:**
9. "Tem identidade visual definida ou tá no zero? Se tem, me passa as
   cores principais e a fonte. Se tiver manual de marca em PDF/arquivo,
   pode jogar em `arquivos/entrada/` que eu processo e extraio de lá em
   vez de você descrever tudo de novo."
10. "Tem logo? Se sim, aponta o caminho do arquivo (ou joga em
    `arquivos/entrada/`)."

**Sobre ferramentas:**
11. "Que ferramentas o negócio já usa hoje? (CRM, WhatsApp Business,
    planilhas, automações, plataforma de anúncios, etc.)"

---

## Fase 3 — Preenchimento dos arquivos

### `_memoria/empresa.md`
Preencher com base nas perguntas 1-4: nome, o que faz, perfil escolhido
na Fase 1, perfil de cliente, equipe.

### `_memoria/preferencias.md`
Preencher com base nas perguntas 5-6:
- **Tom de voz:** derivar do exemplo de escrita real da pergunta 5
  (descrever em 2-3 frases o jeito de escrever, com referência ao
  exemplo)
- **O que evitar:** lista direta da resposta 6
- **Estilo geral:** síntese do que combina e o que destoa

### `_memoria/estrategia.md`
Preencher com base nas perguntas 7-8:
- **Prioridade principal:** resposta da 7
- **O que pode esperar:** o que não ataca o gargalo direto
- **Contexto com prazo:** registrar "<resposta da 8>" como candidata a
  virar skill via `mapear-rotinas`, se essa skill existir/for criada

### `_memoria/marca.md`
Preencher com base nas perguntas 9-10, se houver resposta. Se o usuário
apontou um arquivo em `arquivos/entrada/`, processar esse arquivo
primeiro (ver central de arquivos no `CLAUDE.md`) e extrair paleta,
tipografia e diretrizes de lá. Se não houver nada, deixar em branco e
avisar:

> "Deixei `_memoria/marca.md` em branco. Sempre que definir identidade
> visual, atualiza lá — qualquer skill de design (`design-front-end`,
> conteúdo visual) lê esse arquivo antes de criar peça nova."

### `_memoria/ferramentas.md`
Preencher com base na pergunta 11.

### `_memoria/produtos-e-servicos.md`
Se surgiu detalhe de produto/serviço/preço durante a entrevista (mesmo
sem pergunta dedicada), registrar aqui. Se não, deixar em branco — não é
obrigatório para o setup inicial.

Não escrever "este arquivo será preenchido pelo instalar" no resultado
final — esse aviso é só do placeholder, sai depois da instalação.

---

## Fase 4 — Resumo

Mostrar o que foi configurado, por exemplo:

```
✓ Perfil aplicado: [perfil]
✓ Negócio: _memoria/empresa.md
✓ Tom de voz: _memoria/preferencias.md
✓ Foco atual: _memoria/estrategia.md
✓ Marca: _memoria/marca.md  [preenchida | em branco — preencher depois]
✓ Ferramentas: _memoria/ferramentas.md
```

Nunca dizer só "pronto, instalado" — sempre esse resumo específico do
que foi gravado.

---

## Fase 5 — Nome da pasta (se aplicável)

Só se a Pré-checagem detectou nome genérico do sistema (não do negócio):
gerar um slug sugerido a partir do nome do negócio (resposta 1) —
minúsculas, sem acentos, espaços viram hífen, caracteres especiais
removidos.

Antes de sugerir, checar rapidamente se algo depende do nome atual da
pasta (remoto Git configurado, caminho absoluto referenciado em algum
script). Se houver dependência, avisar disso explicitamente. Se não
houver, sugerir uma vez, sem insistir:

> "Se quiser, dá pra renomear a pasta pra '<slug>' pra ficar com a cara
> do negócio — isso é opcional e você decide quando fazer. [Se houver
> dependência: 'Só que vi que a pasta tem <o que depende>, então
> renomear pode exigir ajustar isso também.']"

Não fazer isso sozinho — é sugestão, não ação.

---

## Fase 6 — Próximos passos

> "Pronto — o sistema já conhece o negócio.
>
> No começo de cada sessão, roda `abrir` pra eu carregar o contexto antes
> da primeira resposta. Quando precisar de diagnóstico, plano de
> marketing, conteúdo, financeiro, página, comercial ou qualquer outra
> frente, é só pedir — eu procuro a skill ou módulo certo.
>
> Você mencionou que repete '<resposta da pergunta 8>' toda semana.
> Quando quiser tirar isso das costas, me avisa que a gente transforma
> isso em skill."

Não mencionar push, publicação ou GitHub nessa mensagem — o sistema é
local até o usuário decidir explicitamente versionar ou publicar.

---

## Quando usar

- Primeira vez que o LKT System é aberto numa pasta de projeto, ou
  quando o usuário pedir explicitamente pra instalar/configurar.

## Quando não usar

- Memória já preenchida precisando só de ajuste pontual — é
  `atualizar-memoria` ou edição direta.

## Entradas

Respostas do usuário às perguntas da entrevista (Fases 1-2).

## Dependências

`_memoria/` (13 arquivos), `.lkt-system/estado/contexto-ativo.json`.

## Contexto que deve ser carregado

Estado atual de `_memoria/` (pra detectar instalação nova vs. parcial).

## Saídas

`_memoria/empresa.md`, `preferencias.md`, `estrategia.md`, `marca.md`,
`produtos-e-servicos.md`, `ferramentas.md` preenchidos, com resumo do
que foi gravado.

## Caminho de salvamento

`_memoria/` na raiz do projeto onde a skill foi executada.

## Critérios de qualidade

- Nenhuma pergunta pulada sem tentar uma vez pedir concretude.
- Resumo final mostra exatamente o que foi preenchido, nunca só "pronto".

## Critérios de validação

- Todos os arquivos de memória citados têm campo essencial preenchido
  (não mais em branco).

## Limitações

- Não cobre instalação de skills de domínio — só o núcleo (memória +
  estrutura).

## Contrato de handoff

Encaminha pra `catalogo/modulos/diagnostico` (se houver cliente/projeto
específico) ou encerra com a memória geral pronta.

## Regras

- Não inventar dados — se a resposta for vaga, registrar do jeito que
  veio (ou deixar placeholder claro, nunca um dado fictício).
- O setup deve durar poucos minutos. Se o usuário estiver enrolando numa
  pergunta, registrar o que tem e seguir.
- Não fazer perguntas extras além das listadas sem motivo claro.
- Nunca mencionar push ou publicação automática.
- Nunca sobrescrever memória já preenchida sem mostrar o que muda e pedir
  confirmação antes.

## Exemplos de gatilhos positivos

- "Instalar o sistema"
- "Primeiro setup"
- "Configurar o LKT aqui"

## Exemplos de gatilhos negativos

- Memória já preenchida, só uma correção pontual (é "Aprender com
  correções" do `CLAUDE.md`, ou `atualizar-memoria`, não instalação do
  zero)
