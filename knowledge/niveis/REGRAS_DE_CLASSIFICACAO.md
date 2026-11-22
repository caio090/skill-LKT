# Regras de classificação

A classificação por nível deve ser explicável. Nunca classificar
usando só uma impressão vaga.

## Toda regra declara

Dimensão, critério, evidência, peso (quando aplicável), condição,
resultado, confiança, fonte, data, justificativa, versão. Ver
`schemas/classification-rule.schema.json`.

## Tipos de evidência aceitos

Documento, entrevista, diagnóstico, dado financeiro, métrica, processo
existente, ferramenta ativa, contrato, resultado, observação, arquivo,
resposta do usuário, integração, histórico.

## Níveis de confiança

- **Confirmado** — evidência direta e recente sustenta a classificação.
- **Provável** — evidência indireta ou parcial aponta nessa direção.
- **Parcial** — evidência insuficiente para o conjunto de níveis
  inteiro, mas suficiente para parte dele.
- **Incerto** — pouca evidência, classificação sujeita a mudar com
  pouca informação nova.
- **Sem dados** — nenhuma evidência disponível ainda.

## Quando não houver evidência suficiente

- Não inventar.
- Não aplicar nível definitivo.
- Marcar a classificação como **provisória**.
- Listar a informação faltante explicitamente.
- Gerar perguntas específicas para validar (ver skill
  `classificar-nivel`, `perguntas.txt`).

## Versionamento de regra

Toda regra tem `versao`. Uma nova versão nunca altera retroativamente
uma avaliação já registrada com a versão anterior — avaliações antigas
preservam a regra que as gerou (`schemas/level-assessment.schema.json`,
campo `versao_da_regra`). Ajustar uma regra é sempre criar uma nova
versão, não editar a existente in-place.

## Exceções

Quando a regra padrão não representa corretamente o caso (ex.:
negócio muito atípico, contexto especial), registrar a exceção
explicitamente — nunca forçar o encaixe silencioso numa regra que não
serve. A skill `classificar-nivel` sempre oferece a opção "isso não se
aplica bem aqui, quero registrar como exceção".
