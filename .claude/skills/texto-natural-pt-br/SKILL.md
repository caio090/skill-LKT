---
name: texto-natural-pt-br
description: >
  Acabamento final de qualquer texto voltado a público, cliente ou
  usuário final — legendas, roteiros, sites, landing pages, propostas,
  relatórios, e-mails, apresentações, anúncios, mensagens de WhatsApp,
  textos de interface, descrições de produto. Reescreve pra soar
  brasileiro, direto e específico, removendo linguagem artificial de IA.
  Use ao final de qualquer skill que produza texto para fora, ou quando
  o usuário pedir "deixa esse texto mais natural", "tira esse jeito de
  IA", "revisa esse texto".
---

# texto-natural-pt-br — Acabamento de texto público

Última etapa de qualquer texto que vai sair do sistema pra alguém ler.
Não cria conteúdo do zero — pega um texto já escrito (por outra skill ou
pelo usuário) e corrige o que soa artificial, genérico ou fora do tom da
marca.

## Quando usar

- Ao final de qualquer skill que gere texto pra público externo
  (`carrossel`, `publicar-tema`, `email-profissional`,
  `responder-avaliacoes`, propostas, relatórios de cliente, textos de
  página/site).
- Quando o usuário pedir revisão explícita de um texto já pronto.

## Quando não usar

- Texto interno (notas de decisão, `PROJETO.md`, comentário de código) —
  isso não precisa desse acabamento.
- Texto que ainda não tem conteúdo definido — primeiro escreve o
  conteúdo (na skill de origem), depois passa por aqui.

## Entradas

- O texto a revisar.
- Contexto de quem fala (empresa ou cliente) e pra quem (público-alvo).

## Dependências

- `_memoria/preferencias.md` (tom de voz, o que evitar) — ou
  `clientes/<cliente>/_memoria/preferencias.md` se o texto for de um
  cliente específico.
- `_memoria/marca.md` (se o texto precisar refletir posicionamento).

## Contexto que deve ser carregado

- Preferências de tom (geral ou do cliente ativo).
- Palavras/expressões proibidas registradas em `_memoria/preferencias.md`
  ou `clientes/<cliente>/_memoria/preferencias.md`.

---

## Workflow

### Passo 1 — Ler o texto e o contexto de tom

Carregar preferências de tom relevantes (geral, ou do cliente ativo se
houver um em `.lkt-system/contexto-ativo.json`).

### Passo 2 — Remover os problemas abaixo, nessa ordem de prioridade

1. **Promessas sem base** — qualquer afirmação numérica ou de resultado
   que não tenha fonte real vira estimativa marcada como tal, ou é
   removida.
2. **Termos proibidos** — os registrados em `preferencias.md` pro
   negócio/cliente.
3. **Linguagem artificial de IA** — frases como "isso muda tudo", "em um
   mundo cada vez mais...", "não é só X, é Y", "espero que isso ajude!",
   abertura de email robótica.
4. **Jargão fora do contexto do público** — termos técnicos de marketing
   ("ticket médio", "performance", "sinergia") quando o público real não
   fala assim.
5. **Elogio vazio / frase motivacional pronta** — "juntos somos mais
   fortes", "o sucesso está ao seu alcance".
6. **Repetição de ideia** — a mesma informação reaparecendo em
   parágrafos diferentes com palavras trocadas.
7. **Travessão longo (—) usado como muleta de estilo** — trocar por
   ponto, vírgula ou reestruturar a frase.
8. **Aspas decorativas** em palavras que não precisam de aspas.
9. **Listas forçadas de três itens** quando o conteúdo real pede dois ou
   quatro — não redondar artificialmente.
10. **Expressões vagas sem fonte** — "especialistas afirmam",
    "estudos mostram", sem citar qual estudo.

### Passo 3 — Reescrever mantendo o conteúdo

Reescrever preservando 100% da informação factual do texto original —
esta skill corrige forma, não conteúdo. Se o conteúdo em si parecer
errado ou incompleto, sinalizar isso separadamente em vez de inventar
correção.

### Passo 4 — Conferir against preferências específicas

Reler contra `preferencias.md`: tom bate? Palavras proibidas sumiram?
Se o texto for de um cliente, checar também `CLIENTE.md` por qualquer
instrução de tom particular.

### Passo 5 — Entregar

Mostrar o texto final. Se a mudança foi grande, oferecer mostrar o
antes/depois pra comparação — não obrigatório para ajustes pequenos.

---

## Saídas

Texto revisado, sem linguagem artificial de IA, pronto pra publicar.

## Regras

- Português brasileiro, nunca tradução literal do inglês.
- Direto: informação relevante logo no início, não enterrada no meio do
  parágrafo.
- Específico: preferir número, nome, exemplo concreto a generalidade.
- Nunca inventar fato, número ou fonte que não estava no texto original
  ou no contexto fornecido.
- Não adicionar emoji que não estava no texto original, a menos que o
  tom de voz do negócio use emoji de propósito.

## Critérios de qualidade

- Nenhum dos 10 problemas do Passo 2 sobrevive no texto final.
- O texto final é mais curto ou do mesmo tamanho que o original — nunca
  mais longo só por causa da reescrita.

## Critérios de validação

- Toda informação factual do texto original está preservada no texto
  final (checagem manual de conteúdo, não só de forma).

## Limitações

- Não decide estratégia de conteúdo, só a forma do texto já decidido.
- Não traduz para outros idiomas — é especificamente para português
  brasileiro.

## Caminho de salvamento

Não gera arquivo próprio — devolve o texto revisado pra quem chamou a
skill (que decide onde salvar).

## Contrato de handoff

Encerra a cadeia de produção de texto — é sempre o último passo, nunca
encaminha para outra skill depois.

## Exemplos de gatilhos positivos

- "Deixa esse texto mais natural"
- "Tira esse jeito de robô dessa legenda"
- Chamada automática ao final de `carrossel`, `email-profissional`,
  `publicar-tema`

## Exemplos de gatilhos negativos

- "Escreve uma legenda sobre X" (isso é a skill de conteúdo criando o
  texto — `texto-natural-pt-br` só revisa depois)
- "Traduz isso pro inglês" (fora de escopo — é só para português)
