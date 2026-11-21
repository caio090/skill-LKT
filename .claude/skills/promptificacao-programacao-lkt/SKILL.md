---
name: promptificacao-programacao-lkt
description: Criar e complementar prompts de programação no padrão LKT, incluindo auditoria do estado existente, identificação numerada, execução, testes e relatório visual baseado em evidências. Usar ao preparar instruções para agentes de desenvolvimento ou avaliar entregas de projetos LOKAT.
---

# Promptificação de programação LKT

## Identificação
- Iniciar cada prompt nas três primeiras linhas com número, projeto e ação concreta, para identificar o pedido na visualização recolhida.
- Exemplo: PROMPT 07 | LOKAT OS | ENTRADA E JORNADA DO CLIENTE
- Recuperar a sequência confirmada do projeto; se não for possível, usar identificador provisório explícito, sem inventar continuidade.
- Identificar complementos com o número original e sufixo, quando confirmado.

## Preparação
- Recuperar decisões e contexto atual do projeto e do cliente, consultando as fontes relevantes disponíveis.
- Auditar branch, status, diff e alterações recentes antes de orientar mudanças; preservar trabalho de terceiros e restrições de não mexer.
- Distinguir fatos verificados, relatos anteriores, hipóteses e pontos que precisam de confirmação.
- Considerar o fluxo inteiro e efeitos futuros, sem ampliar o escopo autorizado.
- Orientar a reutilização de recursos existentes; não inventar arquitetura, dados, funcionalidades ou evidências.

## Composição do prompt
- Escrever instruções completas e expansivas, com pelo menos 60 linhas para prompts de programação, salvo se o usuário pedir outro formato ou tamanho.
- Usar conteúdo útil e específico, sem repetir linhas para inflar contagem.
- Incluir conforme o caso: objetivo, contexto, estado atual, diagnóstico, escopo, regras de negócio, UX, dados e permissões, impactos, implementação, migração, testes, critérios de aceite e relatório.
- Indicar explicitamente itens a preservar, dependências, tratamento de erros e prevenção de duplicidade.
- Pedir validação do fluxo real, separando inspeção de código, testes automatizados e verificação visual ou operacional.
- Não exigir ações externas, publicação ou mensagens sem autorização aplicável.
- Para trabalho relacionado à Tayannara/CONAD, recuperar o contexto mais recente específico desse projeto e preservar suas decisões.

## Relatório de entrega
- Começar com o resultado e identificar projeto, número do prompt e versão ou commit quando disponível.
- Usar semáforo com texto além da cor: 🟢 concluído e validado; 🟡 parcial, em andamento ou não testado; 🔴 pendente, falhou ou bloqueado.
- Distinguir implementado de validado, e indicar evidência, teste, limitação e motivo para cada achado relevante.
- Apresentar o que entrou, o que não entrou, prioridades e próximos passos; incluir responsável e prazo apenas se conhecidos.
- Não declarar corrigido, publicado ou testado sem evidência.
- Identificar corretamente a ferramenta executora. Para Claude Code, iniciar e encerrar com RELATÓRIO CLAUDE CODE; usar RELATÓRIO CODEX WEB apenas para Codex Web.
- Ao receber relatório de execução, auditar suas afirmações no repositório correto do projeto: commit, arquivos e diff quando disponíveis; distinguir o que o GitHub comprova do que exige banco, deploy ou testes. Não confundir o repositório da skill com o do produto.
- Para trabalhos no Claude Code, usar a interface web quando houver acesso autorizado, preservando o fluxo existente; não alegar operação realizada sem confirmação.
- Adaptar a apresentação ao meio disponível; não afirmar que um painel visual foi criado quando o resultado for apenas textual.
