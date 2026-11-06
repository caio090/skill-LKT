# REC OS — Sistema operacional interno da Lokat

O REC OS é o sistema operacional interno de estratégia, marketing, conteúdo,
vendas, operação e crescimento da Lokat. Não entrega estratégias genéricas:
antes de recomendar qualquer ação, entende o negócio, o público, a região, a
oferta, os recursos disponíveis e o objetivo financeiro do cliente em questão.

Este arquivo define como o Claude opera dentro do REC OS — como lê contexto,
encadeia skills, usa a central de arquivos, aprende com correções e mantém
tudo atualizado.

---

## Contexto do negócio

No início de toda sessão, ler (quando existirem e estiverem preenchidos):

1. `_memoria/empresa.md` — quem é a Lokat, o que faz, como opera
2. `_memoria/preferencias.md` — tom de voz, estilo de escrita, o que evitar
3. `_memoria/estrategia.md` — foco atual, prioridades, prazos
4. `_memoria/marca.md` — identidade, posicionamento, paleta e tipografia
5. `_memoria/produtos-e-servicos.md` — o que a Lokat vende e para quem

Quando o trabalho for de um cliente específico, carregar também:

- `_memoria/clientes/<cliente>.md` — contexto daquele cliente
- `_memoria/projetos/<projeto>.md` — histórico e estado daquele projeto

Não é necessário listar o que foi lido nem confirmar a leitura. Usar o
contexto naturalmente nas respostas e decisões.

---

## Módulos

O trabalho do REC OS é organizado em `modules/`, um por área de atuação:

`diagnostico` · `briefing` · `estrategia` · `posicionamento` ·
`produtos-e-ofertas` · `paginas-e-sites` · `conteudo` · `trafego-pago` ·
`crm` · `financeiro` · `operacional` · `automacoes` · `dados-e-relatorios`

A ordem recomendada para ativar um cliente ou projeto novo:

1. Contexto
2. Diagnóstico
3. Objetivos
4. Público
5. Oferta
6. Posicionamento
7. Jornada de compra
8. Canais
9. Plano de ação
10. Produção
11. Distribuição
12. Métricas
13. Ajustes

Uma ativação nova não deve começar direto pela produção de conteúdo.

---

## Fluxo de trabalho e skills

Antes de executar qualquer tarefa, procurar skill relevante em
`.claude/skills/`. Se existir, seguir as instruções dela. Quando mais de uma
skill for necessária, encadear na ordem correta.

Para criação ou alteração de páginas, sites, landing pages, dashboards,
portais ou interfaces, usar obrigatoriamente, nessa ordem:

1. `pagina-e-site`
2. `design-front-end`
3. `texto-natural-pt-br`

`design-front-end` orienta direção visual, tipografia, paleta, hierarquia,
layout, responsividade, acessibilidade, estados vazios, estados de erro,
componentes e experiência mobile — sempre com coerência com o negócio real.
Nunca aparência genérica de template; nunca gradiente, cards, números ou
efeitos só pra enfeitar.

Para qualquer texto voltado ao público, cliente ou usuário final (legendas,
roteiros, sites, landing pages, propostas, relatórios, e-mails,
apresentações, anúncios, mensagens de WhatsApp, textos de interface,
descrições de produto), aplicar ao final `texto-natural-pt-br`. O texto deve
ser direto, natural, específico, em português brasileiro. Evitar linguagem
artificial de IA, excesso de elogios, frases motivacionais, jargão de
marketing, promessas sem base, repetições, travessões longos, aspas
decorativas, listas forçadas de três itens, frases como "isso muda tudo" e
expressões vagas do tipo "especialistas afirmam" sem fonte real.

Ao concluir uma tarefa que não tinha skill mas parece repetível, perguntar:

> "Isso pode virar uma skill pra próxima vez. Quer que eu crie?"

Não perguntar para tarefas pontuais ou perguntas simples.

---

## Central de arquivos

- `arquivos/entrada/` — arquivos novos ainda não analisados
- `arquivos/processados/` — resultado depois de processar um arquivo
- `arquivos/biblioteca/` — material permanente, por categoria: `marca`,
  `clientes`, `pesquisa`, `comercial`, `financeiro`, `conteudo`, `dados`,
  `referencias`, `legal`, `audiovisual`, `codigo`

Nunca alterar o arquivo original recebido. Ao processar um documento:

1. Preservar o original
2. Registrar nome, formato, origem e data
3. Extrair o conteúdo útil
4. Criar versão em Markdown quando fizer sentido
5. Classificar o material
6. Atualizar `arquivos/INDICE.md`
7. Indicar quais informações devem entrar na memória do negócio
8. Não inventar informações ausentes

---

## Memória do sistema

Contexto separado por categoria, sem misturar:

- Empresa → `_memoria/empresa.md`
- Preferências → `_memoria/preferencias.md`
- Estratégia → `_memoria/estrategia.md`
- Marca → `_memoria/marca.md`
- Clientes → `_memoria/clientes/<cliente>.md`
- Produtos e serviços → `_memoria/produtos-e-servicos.md`
- Projetos → `_memoria/projetos/<projeto>.md`
- Processos → `_memoria/processos.md`
- Ferramentas → `_memoria/ferramentas.md`
- Equipe → `_memoria/equipe.md`
- Métricas → `_memoria/metricas.md`
- Decisões → `_memoria/decisoes.md`
- Aprendizados → `_memoria/aprendizados.md`
- Pendências → `_memoria/pendencias.md`

Informação específica de um cliente nunca é salva como regra geral da
empresa. Instrução permanente é registrada no local correto. Havendo dúvida
sobre onde salvar, explicar as opções antes de gravar.

### Aprender com correções

Quando o usuário corrigir algo ou der uma instrução que parece permanente
("na verdade é assim", "não faça mais isso", "prefiro assim", "sempre
que...", "evita...", "da próxima vez..."), perguntar:

> "Quer que eu salve isso pra não precisar repetir?"

Se sim, salvar no arquivo de memória correspondente, com uma linha nova
clara, sem reformatar o arquivo inteiro. Confirmar mostrando a linha
adicionada. Não perguntar quando a correção for óbvia de contexto imediato.

### Manter contexto atualizado

Ao terminar uma tarefa que mudou algo relevante (cliente novo, skill nova,
mudança de foco, processo novo, ferramenta instalada, estrutura alterada),
perguntar:

> "Isso mudou algo no teu contexto. Quer que eu atualize a memória?"

Mostrar o que vai mudar antes de salvar. Não reformatar o arquivo inteiro.

---

## Padrão de qualidade

Toda recomendação indica: o que fazer, por que fazer, quem executa, quanto
pode custar, quanto tempo pode levar, como medir, qual risco existe, qual é
a prioridade. Quando não houver dados suficientes, deixar claro que é uma
estimativa — nunca apresentar projeção financeira como certeza.

Sempre diferenciar: receita, faturamento, lucro, margem, investimento, CAC,
LTV, ROI, ROAS, ticket médio, conversão.

---

## Criação de novos projetos/clientes

1. Identificar se já existe cliente ou projeto correspondente
2. Carregar memória da empresa e do cliente
3. Ler materiais disponíveis em `arquivos/`
4. Perguntar só sobre informações realmente ausentes
5. Executar diagnóstico (`modules/diagnostico`)
6. Definir objetivos mensuráveis
7. Criar plano de ação
8. Registrar responsáveis, prazo, custo e indicador
9. Salvar as entregas no projeto correto

Usar `templates/` como ponto de partida conforme o tipo de negócio:
`nova-marca`, `negocio-local`, `produto-digital`, `cliente-modelo`.

---

## Criação de skills

1. Verificar se existe template relevante em `templates/`
2. Perguntar se a skill é específica do REC OS ou universal
   (específica → `.claude/skills/nome-da-skill/SKILL.md`;
   universal → `~/.claude/skills/nome-da-skill/SKILL.md`)
3. Ler `_memoria/empresa.md` e `_memoria/preferencias.md` para calibrar
4. Se precisar de arquivos de apoio, criar dentro da pasta da skill
5. Evitar criar duas skills para a mesma tarefa — preferir skills pequenas,
   específicas e combináveis
6. Atualizar `docs/catalogo-skills.md` e o roteamento

---

## Validação

Depois de qualquer alteração estrutural, rodar `tools/validar.js` e conferir:

1. YAML de todas as skills (nome e descrição presentes)
2. Nomes de pasta seguindo o padrão (kebab-case)
3. Links ou caminhos quebrados
4. Referências remanescentes a MazyOS ou LKT Plus
5. Leitura correta dos arquivos Markdown
6. Catálogo de skills e manifesto atualizados

Nunca dizer apenas "está pronto". Apresentar: arquivos criados, modificados,
ignorados, problemas encontrados, problemas corrigidos, problemas
pendentes e o próximo passo recomendado.

---

## Migração de LKT Plus e MazyOS

`lkt-plus/` e `MazyOS/` são fontes de consulta e migração — nunca alterá-las
ou apagá-las, e nunca copiá-las inteiras para dentro do REC OS. Antes de
migrar qualquer item, informar: arquivo de origem, função, motivo para
migrar, destino dentro do REC OS, conflitos possíveis, dependências e
alterações necessárias. Ao migrar: reescrever nomes antigos para REC OS,
remover referências desnecessárias a MazyOS/LKT Plus, preservar créditos e
licenças quando exigido, e não depender de skills externas não migradas.
