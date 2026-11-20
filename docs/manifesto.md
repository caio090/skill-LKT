# Manifesto de arquivos

Registro de origem, função e destino de cada item migrado (ou avaliado e
descartado) para o REC OS. Atualizar a cada migração — nunca copiar
conteúdo de `lkt-plus/` ou `MazyOS/` sem registrar aqui antes.

Colunas:

- **Origem** — caminho no repositório antigo
- **Função** — o que o item faz
- **Classificação** — Migrar / Adaptar / Mesclar / Já existe / Descartar / Precisa de revisão
- **Destino** — caminho de destino dentro do REC OS
- **Conflitos/dependências** — o que precisa ser resolvido antes ou depois

## Itens avaliados

| Origem | Função | Classificação | Destino | Conflitos/dependências |
|---|---|---|---|---|
| Prompt Vidigal PNG V22 R10 enviado pelo usuário | Processo de design assistido | Adaptar | `.claude/skills/vidigal-png/` | Skill nova, referência integral preservada. R10 prevalece nas regras conflitantes de pesquisa visual. |

## Itens descartados

_Nenhum ainda._

## Histórico

- **2026-07-20** — REC OS criado do zero (estrutura base, memória,
  documentação). Nenhum conteúdo de `lkt-plus/` ou `MazyOS/` copiado ainda.
