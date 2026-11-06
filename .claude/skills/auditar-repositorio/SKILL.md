---
name: auditar-repositorio
description: >
  Audita um repositório de código: estrutura, dependências
  desatualizadas/vulneráveis, segredos expostos, cobertura de teste,
  documentação e convenções — sem corrigir nada sozinha. Use quando o
  usuário pedir "audita esse repositório", "esse código tem segredo
  exposto".
---

# auditar-repositorio — Auditoria de repositório

## Quando usar

Antes de assumir manutenção de um repositório, ou periodicamente pra
saúde técnica.

## Quando não usar

Revisão de uma mudança específica de código → `revisar-codigo`.

## Entradas

Acesso de leitura ao repositório.

## Dependências

Nenhuma obrigatória.

## Contexto que deve ser carregado

Nenhuma memória de negócio necessária — é auditoria técnica.

---

## Workflow

1. Estrutura geral (organização de pastas, convenções seguidas ou não).
2. Dependências: desatualizadas, com vulnerabilidade conhecida (se
   houver forma de checar).
3. **Segredos expostos:** procurar chave/token/senha commitada — se
   encontrar, reportar imediatamente e recomendar rotação da credencial
   (nunca só remover do código sem avisar que a credencial precisa ser
   trocada).
4. Cobertura de teste (existe? cobre o crítico?).
5. Documentação (README, comentários onde necessário).
6. Convenções de commit/branch seguidas.
7. Salvar em `<pasta-do-projeto-ativo>/07-tecnologia/auditoria-repositorio.md`.

## Saídas

Relatório de auditoria com achados priorizados.

## Caminho de salvamento

`<pasta-do-projeto-ativo>/07-tecnologia/`.

## Regras

- Segredo exposto é sempre reportado com urgência alta — nunca tratado
  como item de baixa prioridade.
- Nunca corrigir sozinha — só reportar e recomendar.

## Critérios de qualidade

Todo achado tem localização exata (arquivo, linha) e severidade.

## Critérios de validação

Segredo exposto, se encontrado, gera recomendação explícita de
rotacionar a credencial, não só remover do código.

## Limitações

Não roda scanner de vulnerabilidade automatizado se a ferramenta não
estiver disponível no ambiente — nesse caso, reporta a limitação.

## Contrato de handoff

Encaminha pra `revisar-codigo` (correções pontuais) e
`diagnostico-tecnico` (visão consolidada).

## Exemplos de gatilhos positivos

- "Audita esse repositório antes de eu assumir"
- "Esse código tem alguma chave exposta"

## Exemplos de gatilhos negativos

- "Revisa esse PR específico" (é `revisar-codigo`)
