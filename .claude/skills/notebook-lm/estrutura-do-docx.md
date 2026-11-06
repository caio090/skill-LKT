# Estrutura do DOCX — notebook-lm

Seções adaptáveis — remover o que não fizer sentido, nunca forçar
seção vazia com placeholder genérico.

## Dossiê da empresa

1. Capa (nome, tipo de dossiê, data, versão, status, logo se
   autorizada)
2. Sumário
3. Resumo executivo (quem é, o que faz, situação, prioridades,
   números principais, alertas, oportunidades)
4. Identidade empresarial
5. Modelo de negócio
6. Diagnóstico (pilares aplicáveis, evidências, notas, gargalos,
   maturidade, prioridades)
7. Marketing e presença digital
8. Comercial e atendimento
9. Financeiro e projeções
10. Operação e logística
11. Projetos (ativos, planejamento, execução, concluídos, suspensos —
    resumo com link para o dossiê específico)
12. Roadmap empresarial
13. Oportunidades
14. Riscos
15. Decisões
16. Pendências
17. Métricas e metas
17b. Níveis de maturidade (quando houver classificação formal — nível
    atual, nível recomendado, lacuna, plano de avanço, critérios,
    faixas de prazo/custo, confiança e versão da regra; ver
    `knowledge/niveis/`)
18. Índice de fontes
19. Histórico de versões

## Dossiê do projeto

1. Capa (empresa, projeto, tipo, data, versão, status)
2. Sumário
3. Resumo executivo (objetivo, problema, situação, resultado esperado,
   prioridade, prazo, orçamento, status)
4. Contexto (origem, motivo, público, envolvidos por papel, restrições,
   materiais recebidos)
5. Diagnóstico (fatos, gargalos, oportunidades, faltantes, confiança)
6. Modelagem (escopo, fora de escopo, módulos, processos, campanhas,
   funis, pipelines, páginas, integrações, dados)
7. Estratégia
8. Entregáveis (nome, objetivo, formato, responsável por papel,
   dependências, critério de aceite, local do arquivo, status — por
   entrega)
9. Roadmap (fases, marcos, dependências, prazos, validações)
10. Cronograma
11. Financeiro (preço, implantação, recorrência, custos externos,
    ferramentas, mídia, manutenção, condições, cenários)
12. Projeções (conservador, base, agressivo, hipóteses, confiança,
    gatilhos de revisão)
13. Responsabilidades (papel, função, decisão/aprovação/execução/
    consulta/informação — matriz)
14. Campanhas e conversão (quando aplicável)
15. Operação e logística (quando aplicável)
16. Riscos
17. Oportunidades
18. Decisões
19. Pendências
20. Próximos passos
21. Métricas
21b. Níveis de maturidade (quando aplicável — mesmo conteúdo do item
    17b do dossiê de empresa, mas restrito ao projeto)
22. Índice de fontes
23. Histórico de versões

## Elementos visuais

Capa, hierarquia clara de título/subtítulo, tabelas, caixas de
destaque, cartões de indicador, linha do tempo/roadmap, matriz de
responsabilidade, blocos de decisão, alertas, gráfico simples (só
quando o dado existir), cabeçalho, rodapé, número de página, data,
versão, classificação de confidencialidade. Nenhum elemento decorativo
sem função de leitura/decisão. Só fontes já instaladas no sistema
(sem baixar fonte externa). Nunca embutir/compartilhar arquivo de
fonte tipográfica.

## Geração real

Gerado via `tools/notebook-lm/gerar-dossie.js` (biblioteca `docx`,
Node — produz OOXML real, nunca Markdown renomeado). Estilos
consistentes, cabeçalho/rodapé, tabelas, quebra de página controlada,
metadados mínimos (título, autor="Sistema LKT", versão) no próprio
arquivo.
