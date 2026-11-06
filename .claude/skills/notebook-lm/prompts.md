# Prompts — notebook-lm

Depois de gerar o dossiê, sempre perguntar:

> "Qual resultado você quer obter no NotebookLM?"

Opções: proposta, apresentação, diagnóstico, oportunidades, roadmap,
plano de ação, projeção, resumo executivo, reunião, relatório,
conteúdo, página de vendas, comparação, personalizado.

## Modelo geral (`PROMPT_NOTEBOOKLM_ATUAL.txt`)

Todo prompt gerado contém, nesta ordem: (1) papel do NotebookLM, (2)
objetivo, (3) público da saída, (4) formato, (5) estrutura, (6)
critérios, (7) o que não inventar, (8) como lidar com lacunas, (9)
quais fontes priorizar, (10) pedido de citar a base, (11) distinção
entre fato, hipótese e projeção.

Texto-base:

```
Use exclusivamente as informações do dossiê anexado como fonte
principal. Crie [ENTREGA] para [PÚBLICO]. Estruture em [FORMATO].
Diferencie fatos confirmados, hipóteses, projeções, decisões e
pendências. Não invente números. Quando faltar informação, indique
claramente a lacuna. Priorize [SEÇÕES]. Ao final, apresente
recomendações, riscos e próximos passos.
```

## Mini-prompts prontos (gerar o correspondente conforme a escolha)

**Proposta:** "Com base exclusivamente no dossiê, crie uma proposta
comercial clara para o cliente. Explique contexto, problema, objetivo,
escopo, entregáveis, formato de entrega, roadmap, responsabilidades,
dependências, preço, custos externos, condições, itens não inclusos e
próximos passos. Traduza termos técnicos. Não trate projeções como
garantias."

**Apresentação:** "Transforme o dossiê em uma apresentação executiva
visual. Crie narrativa, sequência de slides, título, mensagem
principal, dados, oportunidades, roadmap e chamada final. Para cada
slide, informe título, objetivo, conteúdo e recurso visual
recomendado."

**Oportunidades:** "Analise o dossiê e identifique oportunidades
comerciais, operacionais, financeiras, digitais e de produto.
Classifique por impacto, esforço, prazo, dependências, risco e
confiança. Separe ganhos rápidos, projetos estruturais e
possibilidades futuras."

**Roadmap:** "Crie um roadmap por fases a partir do dossiê. Mostre
objetivo de cada fase, entregas, dependências, responsáveis por papel,
critérios de aceite, prazo, custo e risco. Não invente datas sem
base."

**Projeção:** "Analise os dados e produza cenários conservador, base e
agressivo. Mostre hipóteses, fórmulas, limitações, riscos, gatilhos de
revisão e nível de confiança. Separe dados reais de estimativas."

**Reunião:** "Prepare um briefing para reunião. Resuma contexto,
decisões tomadas, números, pendências, riscos, perguntas importantes,
pontos de negociação e próximos passos. Limite a parte principal a uma
página e inclua anexo detalhado."

Para "diagnóstico", "resumo executivo", "relatório", "conteúdo",
"página de vendas", "comparação" e "personalizado": montar o mesmo
esqueleto de 11 elementos do modelo geral, ajustando ENTREGA/PÚBLICO/
FORMATO/SEÇÕES à escolha do usuário — perguntar detalhes que faltarem
(ex.: "personalizado" sempre pergunta o que exatamente o usuário quer
como saída antes de gerar).

## Comando direto

`/notebook-lm prompt [tipo]` gera só o prompt correspondente sem
regenerar o DOCX (útil quando o dossiê já está atualizado e o usuário
só quer um prompt diferente para a mesma base).
