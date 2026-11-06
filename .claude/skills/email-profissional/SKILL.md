---
name: email-profissional
description: >
  Rascunha um email profissional a partir de um contexto livre.
  Calibra o tom ao destinatário e ao objetivo do email.
  Use quando o usuário disser "escreve um email pra", "preciso mandar um email sobre",
  "como eu respondo isso", "faz um email pra [cliente/pessoa]".
---

# /email-profissional — Rascunho de Email

## Entradas

Contexto livre sobre o email desejado (destinatário, objetivo).

## Dependências

- **Contexto do negócio:** `_memoria/empresa.md`
- **Tom de voz:** `_memoria/preferencias.md`

---

## Workflow

### Passo 1 — Coletar o contexto

Se o usuário não forneceu as informações necessárias, perguntar:
1. "Pra quem é o email? (nome, cargo, relação com você)"
2. "Qual é o objetivo? (cobrar, propor, responder, agradecer, seguir up...)"
3. "Tem algo específico que precisa constar ou que precisa evitar dizer?"

Se o usuário deu o contexto de forma livre (mesmo que bagunçado), extrai o que der e prossegue.

### Passo 2 — Escrever o email

**Considerar:**
- Tom proporcional à relação (cliente novo = mais cuidado, parceiro antigo = mais direto)
- Objetivo claro na abertura (não enterrar o pedido no final)
- Uma ação pedida por vez
- Encerramento sem redundância ("Qualquer dúvida, fico à disposição" é padrão — só usar se fizer sentido)

**Estrutura:**
```
Assunto: [linha de assunto direta, sem clicbait]

[Nome],

[Parágrafo 1 — contexto ou referência ao último contato]

[Parágrafo 2 — o ponto principal ou o pedido]

[Parágrafo 3 — próximo passo, se houver]

[Assinatura]
[Nome do usuário, de _memoria/empresa.md]
```

### Passo 3 — Apresentar opções de tom (quando fizer sentido)

Se o assunto for delicado (cobrança, feedback negativo, recusa), oferecer 2 versões:
- Versão A: mais direta
- Versão B: mais suave

Deixar o usuário escolher.

---

## Quando usar

- Necessidade de email formal/profissional pra cliente, fornecedor ou
  parceiro.

## Quando não usar

- Mensagem de WhatsApp — é `mensagem-whatsapp`, tom e estrutura
  diferentes.

## Contexto que deve ser carregado

Tom de voz do cliente/projeto ativo, se houver.

## Saídas

Rascunho de email pronto pra revisão e envio (envio em si é manual).

## Caminho de salvamento

Não gera arquivo — devolve o texto pra quem pediu.

## Critérios de qualidade

- Assunto específico, nunca vago.
- Objetivo do email claro já na abertura.

## Critérios de validação

- Uma ação pedida por email, não várias amontoadas.

## Limitações

- Não envia o email — só rascunha.

## Contrato de handoff

`texto-natural-pt-br` para acabamento, se o email for pra fora da
empresa.

## Regras

- Tom segue `_memoria/preferencias.md`
- Nunca usar linguagem corporativa genérica sem necessidade
- Assunto do email deve ser específico e descritivo, não vago ("Seguimento", "Proposta")
- Se for um email de cobrança, ser direto mas sem agressividade
- Se for resposta a algo, citar o contexto na primeira linha

## Exemplos de gatilhos positivos

- "Escreve um email pra..."
- "Preciso mandar um email sobre..."
- "Como eu respondo isso" (quando "isso" é um email)

## Exemplos de gatilhos negativos

- "Escreve essa mensagem de WhatsApp" (é `mensagem-whatsapp`, tom e
  estrutura diferentes)
